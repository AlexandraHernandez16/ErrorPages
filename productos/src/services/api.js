// Servicio para conectar con el backend de producto_drf
import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/productos-drf';

// 1. LISTAR (GET)
export const read = () => {
    return axios.get(`${BASE_URL}/`);
};

// 2. CREAR (POST)
export const create = (data) => {
    const formData = new FormData();
    for (const key in data) {
        formData.append(key, data[key]);
    }
    return axios.post(`${BASE_URL}/`, formData);
};

// 3. ACTUALIZAR (PUT)
export const update = (id, data) => {
    const formData = new FormData();
    for (const key in data) {
        formData.append(key, data[key]);
    }
    return axios.put(`${BASE_URL}/${id}/`, formData);
};

// 4. ELIMINAR (DELETE)
export const deleteProducto = (id) => {
    return axios.delete(`${BASE_URL}/${id}/`);
};
