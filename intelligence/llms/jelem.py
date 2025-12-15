from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
from langchain_core.language_models import LLM
from langchain_core.outputs import Generation, LLMResult
from typing import List, Optional
import torch
import os
from dotenv import load_dotenv

load_dotenv()


class LangchainLLMWrapper(LLM):
    model: AutoModelForCausalLM
    tokenizer: AutoTokenizer
    temperature: float = 0.5
    max_new_tokens: int = 4096

    @property
    def _llm_type(self) -> str:
        return "custom-codellama-jelem"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.cuda()
        output = self.model.generate(
            input_ids,
            do_sample=False,
            temperature=self.temperature,
            max_new_tokens=self.max_new_tokens
        )
        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return decoded.split(prompt, 1)[-1].strip()

    def generate(self, prompts: List[str], **kwargs) -> LLMResult:
        generations = [Generation(text=self._call(prompt)) for prompt in prompts]
        return LLMResult(generations=[generations])


def _load_jelem_llm() -> LangchainLLMWrapper:
    base_model_path = os.getenv("BASE_MODEL_PATH")  # e.g. "./intelligence/models/llama_7b"
    lora_path = os.getenv("LORA_ADAPTER_PATH")      # e.g. "./intelligence/models/jelem_lora"

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )

    print("[INFO] Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_path,
        device_map="auto",
        quantization_config=bnb_config,
        torch_dtype=torch.float16,
        trust_remote_code=True
    )

    print("[INFO] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(base_model_path, trust_remote_code=True)
    tokenizer.padding_side = "left"
    tokenizer.truncation = True

    print("[INFO] Loading LoRA adapters...")
    model = PeftModel.from_pretrained(base_model, lora_path)
    model.eval()

    return LangchainLLMWrapper(model=model, tokenizer=tokenizer)

jelem_llm: LangchainLLMWrapper = _load_jelem_llm()
