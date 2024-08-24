import { createSlice } from "@reduxjs/toolkit";

export const openerSlice = createSlice({
  name: "opener",
  initialState: {
    value: false,
  },
  reducers: {
    open: (state) => {
      state.value = true;
    },
    close: (state) => {
      state.value = false;
    },
  },
});

export const openerActions = openerSlice.actions;
export default openerSlice.reducer;
