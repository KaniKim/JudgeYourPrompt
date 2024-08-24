import { Drawer, QuillEditor } from "./components";
import { NavBar } from "./components/nav-bar";

export const EditingHome = () => {
  return (
    <>
      <NavBar />
      <Drawer />
      <QuillEditor />
    </>
  );
};
