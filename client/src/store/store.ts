import { configureStore } from '@reduxjs/toolkit';
import { openerSlice } from '.';

const store = configureStore({
  reducer: { open: openerSlice.reducer },
});

export default store;

export type RootState = ReturnType<typeof store.getState>;
