// src/api.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api'; // Django API base URL

// Function to fetch books
export const getBooks = async () => {
  try {
    const response = await axios.get(`${API_URL}/books/`);  // Adjust this to match your Django API endpoint
    return response.data;  // Return the data from the response
  } catch (error) {
    console.error('Error fetching books:', error);
    return [];
  }
};
