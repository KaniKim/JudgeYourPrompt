import { configureStore } from "@reduxjs/toolkit";
import { openerSlice } from "./opener/opener";
import { loginSlice } from "./login/login";
import { registerNeedSlice } from "./login/regiterNeed";
import { registerUserSlice } from "./login/registerUser";

const store = configureStore({
  reducer: {
    open: openerSlice.reducer,
    login: loginSlice.reducer,
    registerNeed: registerNeedSlice.reducer,
    registerUser: registerUserSlice.reducer
  },
});

export default store;

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
