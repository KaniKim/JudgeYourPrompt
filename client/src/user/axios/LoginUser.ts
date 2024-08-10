import { useNavigate } from 'react-router-dom';
import { Axios } from '../../axios';

import { Cookies } from 'react-cookie';

const cookies = new Cookies();

export const loginUser = (id: string, password: string) => {
  const navigate = useNavigate();
  return Axios({
    method: 'post',
    url: '/api/v1/user/token',
    withCredentials: true,
    data: {
      email: id,
      password: password,
    },
  })
    .then(res => {
      cookies.set('access-token', `${res.data.accessToken}`);
      cookies.set('refresh-token', `${res.data.refreshToken}`);
      navigate('/editor');
    })
    .catch(error => {
      throw error;
    });
};
