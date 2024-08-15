import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";


const initialState = {
  loading: false,
  error: null,
};

export const registerUser = createAsyncThunk(
  "user",
  async (data: { email: string; password: string, nick_name: string | null, first_name: string |null, last_name: string | null }) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    console.log(data)
    await axios
      .post("http://localhost:8000/api/v1/user/", data, config)
      .then(() => {
      })
      .catch(err => {
        throw err;
      });
  }
);

export const registerUserSlice = createSlice({
  name: "registerUser",
  initialState,
  reducers: {},
  extraReducers: builder => {
    builder.addCase(registerUser.pending, state => {
      state.loading = true;
    });
    builder.addCase(registerUser.fulfilled, state => {
      state.loading = false;
    });
    builder.addCase(registerUser.rejected, state => {
      state.loading = false;
    });
  },
});


export const registerUserActions = registerUserSlice.actions;
export default registerUserSlice.reducer;
