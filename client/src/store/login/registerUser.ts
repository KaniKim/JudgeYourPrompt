import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";

const initialState = {
  loading: false,
  payload: "",
  error: null,
};

type registerReturnType = {
  message: string;
};

type UserDataType = {
  email: string;
  password: string;
  nick_name: string | null;
  first_name: string | null;
  last_name: string | null;
  phone_number: string | null;
};

export const registerUser = createAsyncThunk(
  "user",
  async (data: UserDataType, thunkAPI) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    try {
      const response = await axios.post(
        "http://localhost:8000/api/v1/user/",
        data,
        config,
      );

      return thunkAPI.fulfillWithValue(response.data);
    } catch (err) {
      return thunkAPI.rejectWithValue(err);
    }
  },
);

export const registerUserSlice = createSlice({
  name: "registerUser",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(registerUser.pending, (state) => {
      state.loading = true;
    });
    builder.addCase(
      registerUser.fulfilled,
      (state, action: PayloadAction<registerReturnType>) => {
        state.loading = true;
        state.payload = action.payload.message;
      },
    );
    builder.addCase(registerUser.rejected, (state) => {
      state.loading = false;
    });
  },
});

export const registerUserActions = registerUserSlice.actions;
export default registerUserSlice.reducer;
