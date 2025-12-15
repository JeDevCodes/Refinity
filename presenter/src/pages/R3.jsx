import { useState } from 'react';
import axios from 'axios'; 
import CodeBlock from '../components/CodeBlock';
import ChatInput from '../components/ChatInput';

const API_URL = 'http://127.0.0.1:8000/api/r3/';

const R3 = () => {
  const [outputCode, setOutputCode] = useState('// Generated code will appear here');
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);


  const handleSend = async (e) => {
    e.preventDefault();
    let data = {
      'context': query
    };

    try {
      // 1. Submit task to Django
      const response = await axios.post(API_URL, data);
      const responseData = response.data;
      const taskID = responseData['task_id']
      console.log(taskID);
      setLoading(true);

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
      console.log(responseData);
      
  
      if (status === 'done') {
        const output = responseData['result'];
        console.log(responseData);
        
        setOutputCode(`// Generated Output for given \n Query: ${query} \n\n ------------------------------------\n\n\n ${output}`);
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
    <div className="r3-full">
      <div className="r3-op">
        <CodeBlock title="Generated Code" code={outputCode} />
      </div>

      <ChatInput value={query} onChange={(e) => setQuery(e.target.value)} onSend={handleSend} />
    </div>
  );
};

export default R3;
