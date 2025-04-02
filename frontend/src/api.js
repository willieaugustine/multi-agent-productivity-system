import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export const sendEmail = (data) => axios.post(`${API_BASE_URL}/send-email/`, data);
export const scheduleTask = (data) => axios.post(`${API_BASE_URL}/schedule-task/`, data);
export const fetchResearch = (query) => axios.post(`${API_BASE_URL}/fetch-research/`, { query });

