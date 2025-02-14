//API calls to interact with the backend for stock data
import axios from 'axios';

export const fetchStocks = async () => {
    const response = await axios.get('http://localhost:5000/stocks');
    return response.data;
};
