import axios from "axios";

// Настройки Axios
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: parseInt(import.meta.env.VITE_API_TIMEOUT),
  headers: {
    "Content-Type": "application/json",
  },
});

// Интерцептор для добавления JWT токена к запросам администратора
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("adminToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    console.log(
      `📤 API Request: ${config.method.toUpperCase()} ${config.baseURL}${
        config.url
      }`
    );
    return config;
  },
  (error) => {
    console.error("📤 API Request Error:", error);
    return Promise.reject(error);
  }
);

// Интерцепторы для логирования ответов
api.interceptors.response.use(
  (response) => {
    console.log(`📥 API Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error("📥 API Response Error:", {
      status: error.response?.status,
      message: error.response?.data || error.message,
      url: error.config?.url,
    });

    // Если получили 401, возможно токен истек
    if (error.response?.status === 401) {
      console.warn("⚠️ Unauthorized. Token may be expired.");
      // Можно добавить редирект на страницу входа
      // window.location.href = '/admin';
    }

    // Показываем пользователю понятную ошибку
    if (error.response?.status === 404) {
      throw new Error("Ресурс не найден");
    } else if (error.response?.status === 500) {
      throw new Error("Ошибка сервера");
    } else if (error.code === "ECONNABORTED") {
      throw new Error(
        "Время ожидания истекло. Проверьте подключение к серверу."
      );
    } else if (!navigator.onLine) {
      throw new Error("Нет подключения к интернету");
    }

    throw error;
  }
);

// API для меню
export const menuApi = {
  getAll() {
    return api.get("/menu");
  },

  getByCategory(category) {
    return api.get(`/menu?category=${category}`);
  },

  getById(id) {
    return api.get(`/menu/${id}`);
  },

  create(data) {
    return api.post("/menu", data);
  },

  update(id, data) {
    return api.put(`/menu/${id}`, data);
  },

  delete(id) {
    return api.delete(`/menu/${id}`);
  },

  getFeatured() {
    return api.get("/menu/featured");
  },
};

// API для отзывов
export const reviewsApi = {
  getAll() {
    return api.get("/reviews");
  },

  getPaginated(page = 1, limit = 10) {
    return api.get(`/reviews?page=${page}&limit=${limit}`);
  },

  getById(id) {
    return api.get(`/reviews/${id}`);
  },

  create(data) {
    return api.post("/reviews", data);
  },

  update(id, data) {
    return api.put(`/reviews/${id}`, data);
  },

  delete(id) {
    return api.delete(`/reviews/${id}`);
  },

  getStats() {
    return api.get("/reviews/stats");
  },
};

// API для галереи
export const galleryApi = {
  getAll() {
    return api.get("/gallery");
  },

  getPaginated(page = 1, limit = 20) {
    return api.get(`/gallery?page=${page}&limit=${limit}`);
  },

  getByCategory(category) {
    return api.get(`/gallery?category=${category}`);
  },

  upload(data) {
    return api.post("/gallery", data);
  },

  update(id, data) {
    return api.put(`/gallery/${id}`, data);
  },

  delete(id) {
    return api.delete(`/gallery/${id}`);
  },
};

// API для заказов
export const ordersApi = {
  getAll() {
    return api.get("/orders");
  },

  getById(id) {
    return api.get(`/orders/${id}`);
  },

  create(data) {
    return api.post("/orders", data);
  },

  update(id, data) {
    return api.put(`/orders/${id}`, data);
  },

  updateStatus(id, status) {
    return api.put(`/orders/${id}/status`, { status });
  },

  delete(id) {
    return api.delete(`/orders/${id}`);
  },
};

// Общий поиск
export const searchApi = {
  search(query) {
    return api.get(`/search?query=${encodeURIComponent(query)}`);
  },
};

// Проверка здоровья API
export const healthApi = {
  check() {
    return api.get("/health");
  },
};

// API для работы с изображениями
export const imageApi = {
  // Загрузка изображения
  upload(file) {
    const formData = new FormData();
    formData.append("file", file);

    return api.post("/upload-image", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  },

  // Получение списка всех изображений
  list() {
    return api.get("/images");
  },

  // Получение информации о конкретном изображении
  get(filename) {
    return api.get(`/images/${filename}`);
  },
};

// API для бронирования стола
export const bookingApi = {
  createReservation(data) {
    return api.post("/table-reservations", data);
  },

  getAll() {
    return api.get("/table-reservations");
  },

  getById(id) {
    return api.get(`/table-reservations/${id}`);
  },

  updateStatus(id, status) {
    return api.put(`/table-reservations/${id}/status`, { status });
  },

  delete(id) {
    return api.delete(`/table-reservations/${id}`);
  },
};

export default api;
