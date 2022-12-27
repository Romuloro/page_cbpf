import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8080",
  withCredentials: true,
});

export const uploadArq = async (files) => {
  return api.get("/data");
};

export const preparedImage = async (dir) => {
  const dirName = String(dir)
  console.log(dirName);
  return api.post("/preparedImage", {dirName});
};
