import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="w-full py-4 shadow sticky top-0 z-50 light-gray-100">
      <Link to="/">
        <h1 className="text-center text-3xl font-bold text-white tracking-wide light-gray-100">
          Refinity
        </h1>
      </Link>
    </header>
  );
};

export default Header;
