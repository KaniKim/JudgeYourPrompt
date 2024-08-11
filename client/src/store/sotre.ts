import { configureStore } from "@reduxjs/toolkit";
import { openerSlice } from "./opener/opener";
import { loginSlice } from "./login/login";
import { registerSlice } from "./login/register";

const store = configureStore({
  reducer: {
    open: openerSlice.reducer,
    login: loginSlice.reducer,
    register: registerSlice.reducer,
  },
});

export default store;

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
