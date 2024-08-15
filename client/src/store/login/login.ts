import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";
import { Cookies } from "react-cookie";

const initialState = {
  loading: false,
  error: null,
};

const cookies = new Cookies();

export const login = createAsyncThunk(
  "user/token",
  async (data: { email: string; password: string }) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    await axios
      .post("http://localhost:8000/api/v1/user/token", data, config)
      .then(res => {
        cookies.set("accessToken", res.data.access_token);
        cookies.set("refreshToken", res.data.refresh_token);
      })
      .catch(err => {
        throw err;
      });

    

  },
);

export const loginSlice = createSlice({
  name: "login",
  initialState,
  reducers: {},
  extraReducers: builder => {
    builder.addCase(login.pending, state => {
      state.loading = true;
    });
    builder.addCase(login.fulfilled, state => {
      state.loading = false;
    });
    builder.addCase(login.rejected, state => {
      state.loading = false;
    });
  },
});

export const loginActions = loginSlice.actions;
export default loginSlice.reducer;
