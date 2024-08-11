import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./home/entire-home";
import { Provider } from "react-redux";
import store from "./store/sotre";
import { UserHome } from "./user/user-home";

function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<UserHome />} />
          <Route path="/editor" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
