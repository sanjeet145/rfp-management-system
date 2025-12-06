import './App.css';
import { Routes, Route } from "react-router-dom"
import Home from './components/Home';
import RFPS from './components/RFPs';
import Vendors from './components/Vendors';
import Responses from './components/Responses';
import Login from './components/Login';
import Navbar from './components/Navbar';

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/rfps' element={<RFPS />} />
        <Route path='/vendors' element={<Vendors />} />
        <Route path='/responses' element={<Responses />} />
        <Route path='/login' element={<Login />} />
      </Routes>
    </>
  );
}

export default App;
