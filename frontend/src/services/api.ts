import axios from "axios";

const api = axios.create({
  baseURL: "https://lensify-backend-r4wm.onrender.com",
});

export default api;