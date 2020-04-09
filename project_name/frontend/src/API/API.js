import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class ApiCalls {

    example() {
        const url = `${API_URL}/api/example/`;
        const authToken = 'authToken'
        return axios.get(url, {
                headers: {
                    'Authorization': `Token ${authToken}`
                }
            })
            .then(response => response.data);
    }
}