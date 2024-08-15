import { useDispatch } from "react-redux";
import { Field, Label, Switch } from "@headlessui/react";
import { useState } from "react";
import { openerActions } from "../../store/opener/opener";
import { MyProfile } from "./profile/my-profile";

export const NavBar = () => {
  const dispatch = useDispatch();
  const [enabled, setEnabled] = useState<boolean>(false);
  return (
    <nav className="bg-gray-900 fixed w-full z-20 top-0 start-0 ">
      <div className="flex justify-between mx-auto p-4">
        <div className="justify-start flex">
          <button
            data-collapse-toggle="navbar-hamburger"
            type="button"
            className="inline-flex items-center justify-center p-2 w-10 h-10 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
            aria-controls="navbar-hamburger"
            aria-expanded="false"
            onClick={() => dispatch(openerActions.open())}
          >
            <span className="sr-only">Open main menu</span>
            <svg
              className="w-5 h-5"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 17 14"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M1 1h15M1 7h15M1 13h15"
              />
            </svg>
          </button>
        </div>
        <div className="flex ">
          <Field>
            <Label className="text-m pr-3">자동 저장</Label>
            <Switch
              checked={enabled}
              onChange={setEnabled}
              name="자동 저장"
              className="group inline-flex h-6 w-11 mt-2 items-center rounded-full bg-gray-200 transition data-[checked]:bg-gray-600"
            >
              <span className="size-4 translate-x-1 rounded-full bg-white transition group-data-[checked]:translate-x-6" />
            </Switch>
          </Field>
          <div className="ml-3 mt-1">
            <MyProfile/>
          </div>
        </div>
      </div>
    </nav>
  );
};
