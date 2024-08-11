import { useForm } from "react-hook-form";
import { useDispatch } from "react-redux";
import { login } from "../../store/login/login";
import { AppDispatch } from "../../store/sotre";
import { useNavigate } from "react-router-dom";
import { registerActions } from "../../store/login/register";
import { Button } from "@headlessui/react";
export const Login = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { register, getValues, handleSubmit } = useForm();
  const navigate = useNavigate();

  const onSubmit = async () => {
    const email: string = getValues("email");
    const password: string = getValues("password");
    await dispatch(login({ email, password })).unwrap();
    navigate("/editor");
  };
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="max-w">
        <input
          {...register("email", { required: true })}
          className="w-full rounded border border-solid border-gray-300 px-4 py-2 text-sm"
          type="text"
          placeholder="Email Address"
        />
        <input
          {...register("password", { required: true })}
          className="mt-4 w-full rounded border border-solid border-gray-300 px-4 py-2 text-sm"
          type="password"
          placeholder="Password"
        />
        <div className="mt-4 flex justify-between text-sm font-semibold">
          <a className="text-blue-600 hover:text-blue-700 hover:underline hover:underline-offset-4">
            Forgot Password?
          </a>
          <Button
            className="rounded bg-gray-700 px-4 py-2 text-xs uppercase tracking-wider text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white"
            type="submit"
          >
            로그인
          </Button>
        </div>
        <div className="mt-4 text-center text-sm font-semibold text-slate-500 md:text-left">
          Don&apos;t have an account?{" "}
          <a
            className="text-red-600 hover:underline hover:underline-offset-4"
            onClick={() => dispatch(registerActions.need())}
          >
            Register
          </a>
        </div>
      </div>
    </form>
  );
};
