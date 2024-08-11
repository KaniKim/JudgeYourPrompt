import { Drawer, QuillEditor } from "./components";
import { NavBar } from "./components/nav-bar";

export const Home = () => {
  return (
    <>
      <NavBar />
      <Drawer />
      <QuillEditor />
    </>
  );
};
