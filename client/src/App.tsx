import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { EditingHome } from "./home/edit-home";
import { Provider } from "react-redux";
import store from "./store/sotre";
import { UserHome } from "./user/user-home";

function App() {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<UserHome />} />
          <Route path="/editor" element={<EditingHome />} />
        </Routes>
      </BrowserRouter>
    </Provider>
  );
}

export default App;
