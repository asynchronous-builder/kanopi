// src/services/api.js
const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

export const getSwatches = async (count = 5) => {
  const response = await fetch(`${BASE_URL}/swatches/?count=${count}`, {
    headers: {
      'Content-Type': 'application/json',
    },
  });
  
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  
  return response.json();
};