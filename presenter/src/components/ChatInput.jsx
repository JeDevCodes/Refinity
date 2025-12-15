const ChatInput = ({ value, onChange, onSend }) => {
    return (
      <div className="query">

      <div className="w-full p-4 sticky bottom-0 z-50 light-gray-100 query-text">
        <div className="max-w-4xl mx-auto flex gap-2 rounded">
          <input
            type="text"
            value={value}
            onChange={onChange}
            placeholder="Type your query..."
            className="flex-1 p-2 focus:outline-none "
          />
          <button
            onClick={onSend}
            className="bg-white text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition"
          >
            Send
          </button>
        </div>
      </div>
      </div>
    );
  };
  
  export default ChatInput;
  