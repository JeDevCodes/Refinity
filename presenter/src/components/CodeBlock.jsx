const CodeBlock = ({ title, code }) => {
    return (
      <div className="w-full h-full p-4 black-0 shadow font-semibold">
        {title && <div className="text-sm font-semibold text-white mb-2">{title}</div>}
        <pre className="bg-gray-900 text-gray-100 text-m p-5 rounded-md overflow-auto h-full whitespace-pre-wrap">
          <code>{code}</code>
        </pre>
      </div>
    );
  };
  
  export default CodeBlock;
  