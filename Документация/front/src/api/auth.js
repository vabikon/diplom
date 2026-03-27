import axios from "axios";

// Создаем отдельный экземпляр для авторизации
const authAxios = axios.create({
  baseURL: import.meta.env.VITE_AUTH_API_BASE_URL,
  timeout: parseInt(import.meta.env.VITE_API_TIMEOUT),
  headers: {
    "Content-Type": "application/json",
  },
});

// Интерцептор для добавления токена к запросам
authAxios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("adminToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    console.log(
      `📤 Auth Request: ${config.method.toUpperCase()} ${config.url}`
    );
    return config;
  },
  (error) => {
    console.error("📤 Auth Request Error:", error);
    return Promise.reject(error);
  }
);

// Интерцептор для обработки ответов
authAxios.interceptors.response.use(
  (response) => {
    console.log(`📥 Auth Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error("📥 Auth Response Error:", {
      status: error.response?.status,
      message: error.response?.data || error.message,
      url: error.config?.url,
    });

    // Если токен истек или невалиден, удаляем его
    if (error.response?.status === 401) {
      localStorage.removeItem("adminToken");
    }

    return Promise.reject(error);
  }
);

// API для авторизации
export const authApi = {
  // Вход в систему
  login(credentials) {
    return authAxios.post("/login", credentials);
  },

  // Проверка валидности токена
  verify() {
    return authAxios.get("/verify");
  },

  // Получение информации о текущем пользователе
  me() {
    return authAxios.get("/me");
  },

  // Выход из системы (просто удаляем токен)
  logout() {
    localStorage.removeItem("adminToken");
    return Promise.resolve();
  },
};

export default authApi;
