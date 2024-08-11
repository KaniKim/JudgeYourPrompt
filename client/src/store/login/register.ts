import { createSlice } from "@reduxjs/toolkit";

export const registerSlice = createSlice({
  name: "register",
  initialState: {
    value: false,
  },
  reducers: {
    need: state => {
      state.value = true;
    },
    notNeed: state => {
      state.value = false;
    },
  },
});

export const registerActions = registerSlice.actions;
export default registerSlice.reducer;
