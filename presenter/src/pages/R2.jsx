import { useState } from 'react';
import axios from 'axios';
import CodeBlock from '../components/CodeBlock';
import ChatInput from '../components/ChatInput';

const API_URL = 'http://127.0.0.1:8000/api/r2/';
const TASK_URL = 'http://127.0.0.1:8000/api/task-status';

const R2 = () => {
  const [inputCode, setInputCode] = useState('');
  const [outputCode, setOutputCode] = useState('// Refined code will appear here');
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);


  // const handleSend =  async (e) => {
  //   e.preventDefault();
  //   let data = {
  //     'code':inputCode,
  //     'context':query
  //   }

  //   try{
  //       const response = await axios.post(API_URL,data);
  //       // const responseData = response.data;
  //       const taskID = response.data.task_id;
  //       const op=responseData['output'];
  //       console.log(response)
  //       setOutputCode(`// Refined Output for given \n Query: ${query} \n\n ------------------------------------\n\n\n ${op}`);
  //       setQuery('');
  //   }
  //   catch (error) {
  //     console.log(error)
  //   }

  //   try {
  //     // 1. Submit task to Django
  //     const response = await axios.post(API_URL, data);
  //     const taskID = response.data.task_id;
  
  //     // 2. Start polling for result
  //     pollTaskResult(taskID);
  //   } catch (error) {
  //     console.error("Error submitting task:", error);
  //     setOutputCode("// Error submitting task. Please try again.");
  //   }
    
  // };

  const handleSend = async (e) => {
    e.preventDefault();
  
    let data = {
      code: inputCode,
      context: query
    };
  
    try {
      // 1. Submit task to Django
      const response = await axios.post(API_URL, data);
      const responseData = response.data;
      const taskID = responseData['task_id']
      console.log(taskID);
      
  
      // 2. Start polling for result
      pollTaskResult(taskID);
    } catch (error) {
      console.error("Error submitting task:", error);
      setOutputCode("// Error submitting task. Please try again.");
    }
  };
  
  const pollTaskResult = async (taskID) => {
    try {
      const response = await axios.get(`${TASK_URL}/${taskID}/`);
      const responseData = response.data;
      const status = responseData['status'];
      setLoading(true);
      console.log(response);
      
  
      if (status === 'done') {
        const output = responseData['result'];
        console.log(responseData);
        
        setOutputCode(`// Refined Output for given \n Query: ${query} \n\n ------------------------------------\n\n\n ${output}`);
        setQuery('');
        setLoading(false)
      } else if (status === 'pending' || status === 'processing') {
        // Retry polling after a delay
        setTimeout(() => pollTaskResult(taskID), 2000);
      } else {
        setOutputCode("// Task failed or unknown status.");
      }
    } catch (error) {
      console.error("Error polling task status:", error);
      setOutputCode("// Error checking task status. Please try again.");
    }
  };
  


  return (
    <div className="r2-full">
      <div className="r2-code-screen">
        {/* Left - Input */}
        <div className="r2-left-ip">
          <textarea
            className="r2-text"
            placeholder="// Paste your code here..."
            value={inputCode}
            onChange={(e) => setInputCode(e.target.value)}
          />
        </div>

        {/* Right - Output */}
        <div className="r2-right-op">
          <CodeBlock title="Refined Output" code={outputCode} />
        </div>
      </div>

      <ChatInput value={query} onChange={(e) => setQuery(e.target.value)} onSend={handleSend} />
    </div>
  );
};

export default R2;
