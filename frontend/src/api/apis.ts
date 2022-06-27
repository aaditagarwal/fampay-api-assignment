import { GET } from "./apiHandler";
import { API_BASE_URL } from "../lib/globals";

export const fetchVideos = (params: {
    page: number
    query: string,
}) => {
    return GET(`${API_BASE_URL}/search`, params)
}