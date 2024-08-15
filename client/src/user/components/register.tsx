import { Button } from "@headlessui/react";
import { useForm } from "react-hook-form";
import { AppDispatch } from "../../store/sotre";
import { useDispatch } from "react-redux";
import { registerNeedActions } from "../../store/login/regiterNeed";
import { registerUser } from "../../store/login/registerUser";

export const Register = () => {
  const { register, getValues, handleSubmit } = useForm();
  const dispatch = useDispatch<AppDispatch>();

  const onSubmit = async () => {
    const email: string = getValues("email");
    const password: string = getValues("password");
    const nick_name: string | null = getValues("nick_name");
    const first_name: string | null = getValues("first_name");
    const last_name: string | null = getValues("last_name");
    await dispatch(registerUser({ email, password, nick_name, first_name, last_name }))
      .unwrap()
      .then(() => {
        dispatch(registerNeedActions.notNeed())
      });
  };

  return (
      <form onSubmit={handleSubmit(onSubmit)}>
        <h1 className="text-4xl pb-4">회원 가입</h1>
        <div className="max-w-96">
          <input
            {...register("email", { required: true })}
            className="w-full rounded border border-solid border-gray-300 px-4 py-2 text-sm"
            type="text"
            placeholder="이메일 주소"
          />
          <input
            {...register("password", { required: true })}
            className="mt-4 w-full rounded border border-solid border-gray-300 px-4 py-2 text-sm"
            type="password"
            placeholder="비밀번호"
          />
          <input
            {...register("nick_name", { required: false })}
            className="mt-4 w-full rounded border border-solid border-gray-300 px-4 py-2 text-sm"
            type="text"
            placeholder="별명"
          />
          <div className="mt-4 max-w-96 justify-between flex text-sm">
            <input
              {...register("first_name", { required: false })}
              className="w-full mr-2 rounded border border-solid border-gray-300 px-4 py-2 text-sm"
              type="text"
              placeholder="성"
            />
            <input
              {...register("last_name", { required: false })}
              className="w-full ml-2 rounded border border-solid border-gray-300 px-4 py-2 text-sm"
              type="text"
              placeholder="이름"
            />
          </div>
          <Button className="mt-6 w-full items-center gap-2 rounded-md bg-gray-700 py-1.5 px-3 text-sm/6 font-semibold text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white"
                  type="submit">
            가입하기
          </Button>
          <Button
            className="mt-4 w-full items-center gap-2 rounded-md bg-gray-700 py-1.5 px-3 text-sm/6 font-semibold text-white shadow-inner shadow-white/10 focus:outline-none data-[hover]:bg-gray-600 data-[open]:bg-gray-700 data-[focus]:outline-1 data-[focus]:outline-white"
            onClick={() => dispatch(registerNeedActions.notNeed())}
          >
            로그인 창으로 돌아가기
          </Button>
        </div>
      </form>
  );
};
