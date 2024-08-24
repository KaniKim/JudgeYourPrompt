import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { openerSlice } from "./opener/opener";
import { loginSlice } from "./login/login";
import { registerNeedSlice } from "./login/regiterNeed";
import { registerUserSlice } from "./login/registerUser";

const store = configureStore({
  reducer: combineReducers({
    open: openerSlice.reducer,
    login: loginSlice.reducer,
    registerNeed: registerNeedSlice.reducer,
    registerUser: registerUserSlice.reducer,
  }),
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({ serializableCheck: false }),
  devTools: true,
});

export default store;

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
