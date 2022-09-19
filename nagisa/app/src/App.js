import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/test" element={<Test />}></Route>
      </Routes>
    </Router>
  );
}

const Home = () => (
  <h2>Home</h2>
);
const Test = () => (
  <h2>Test</h2>
);

export default App;
