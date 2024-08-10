import './App.css';
import Login from './user/components/login';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Home } from './home/entire-home';
import { Provider } from 'react-redux';
import store from './store/store';

function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/editor" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
