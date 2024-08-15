import { Login } from "./components";
import { Register } from "./components/register";
import { useSelector } from "react-redux";
import { RootState } from "../store/sotre";

export const UserHome = () => {
  const needRegister = useSelector((state: RootState) => state.registerNeed.value);

  return (
    <section className="mx-5 my-2 flex h-screen flex-col items-center justify-center space-y-10 md:m-0 md:flex-row md:space-x-16 md:space-y-0">
      <div className="max-w-sm md:w-1/3">
        <img
          src="https://tecdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
          alt="Sample image"
        />
      </div>
      {!needRegister ? <Login /> : <Register />}
    </section>
  );
};
