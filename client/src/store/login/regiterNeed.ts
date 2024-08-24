import { createSlice } from "@reduxjs/toolkit";

export const registerNeedSlice = createSlice({
  name: "need",
  initialState: {
    value: false,
  },
  reducers: {
    need: (state) => {
      state.value = true;
    },
    notNeed: (state) => {
      state.value = false;
    },
  },
});

export const registerNeedActions = registerNeedSlice.actions;
export default registerNeedSlice.reducer;
