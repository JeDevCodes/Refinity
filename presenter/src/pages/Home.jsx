import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  const boxes = [
    {
      id: 'r2',
      title: 'R2',
      desc: 'Refine and Refactor your code',
    },
    {
      id: 'r3',
      title: 'R3',
      desc: 'Regenerate, Refine and Refactor',
    },
  ];

  return (
    <div className="flex flex-col h-screen flex items-center justify-center h-full overflow-x-hidden">
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-15">
        {boxes.map((box) => (
          <div
            key={box.id}
            onClick={() => navigate(`/${box.id}`)}
            className="cursor-pointer border-2 border-gray-100 hover:bg-gray-50 rounded-2xl px-16 py-20 text-center shadow-lg transition-transform hover:scale-105 light-gray-100"
          >
            <h2 className="text-4xl font-bold text-white light-gray-100">{box.title}</h2>
            <p className="text-md text-gray-600 mt-4 light-gray-100">{box.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
