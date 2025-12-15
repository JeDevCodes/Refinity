import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import R2 from './pages/R2';
import R3 from './pages/R3';
import Header from './components/Header';

function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Header />
        <div className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/r2" element={<R2 />} />
            <Route path="/r3" element={<R3 />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
