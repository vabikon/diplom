<template>
  <div class="min-h-screen">
    <!-- Страница входа -->
    <div
      v-if="!isAuthenticated"
      class="flex items-center justify-center min-h-screen px-4"
    >
      <div
        class="w-full max-w-md bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-2xl p-8 animate-scaleIn"
      >
        <!-- Логотип/Заголовок -->
        <div class="text-center mb-8">
          <div
            class="w-20 h-20 mx-auto mb-4 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-full flex items-center justify-center"
          >
            <svg
              width="40"
              height="40"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              class="text-orange-500"
            >
              <path
                d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"
              />
            </svg>
          </div>
          <h1 class="text-3xl font-bold text-white mb-2">
            Панель администратора
          </h1>
          <p class="text-gray-400">Введите учетные данные для входа</p>
        </div>

        <!-- Форма входа -->
        <form @submit.prevent="handleLogin" class="space-y-5">
          <!-- Логин -->
          <div>
            <label class="block text-gray-400 text-sm mb-2" for="username">
              Логин
            </label>
            <input
              id="username"
              v-model="loginForm.username"
              type="text"
              required
              placeholder="admin"
              :disabled="isLoading"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors disabled:opacity-50"
            />
          </div>

          <!-- Пароль -->
          <div>
            <label class="block text-gray-400 text-sm mb-2" for="password">
              Пароль
            </label>
            <input
              id="password"
              v-model="loginForm.password"
              type="password"
              required
              placeholder="••••••••"
              :disabled="isLoading"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors disabled:opacity-50"
            />
          </div>

          <!-- Ошибка -->
          <div
            v-if="loginError"
            class="p-3 bg-red-500/10 border border-red-500/50 rounded-lg text-red-400 text-sm"
          >
            {{ loginError }}
          </div>

          <!-- Кнопка входа -->
          <button
            type="submit"
            :disabled="isLoading"
            class="w-full px-6 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <span v-if="!isLoading">Войти</span>
            <span v-else class="flex items-center gap-2">
              <svg
                class="animate-spin h-5 w-5"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  class="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  stroke-width="4"
                ></circle>
                <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              Вход...
            </span>
          </button>
        </form>

        <!-- Подсказка -->
        <div class="mt-6 p-4 bg-gray-900/50 border border-gray-700 rounded-lg">
          <p class="text-gray-500 text-xs text-center">
            По умолчанию: admin / admin123
          </p>
        </div>
      </div>
    </div>

    <!-- Админ-панель -->
    <div v-else>
      <AdminPanel @logout="handleLogout" />
    </div>
  </div>
</template>

<script>
import AdminPanel from "@/components/Admin/AdminPanel.vue";
import { authApi } from "@/api/auth";

export default {
  name: "Admin",
  components: {
    AdminPanel,
  },
  data() {
    return {
      isAuthenticated: false,
      isLoading: false,
      loginForm: {
        username: "",
        password: "",
      },
      loginError: "",
    };
  },
  async mounted() {
    await this.checkAuth();
  },
  methods: {
    async checkAuth() {
      const token = localStorage.getItem("adminToken");
      if (!token) {
        this.isAuthenticated = false;
        return;
      }

      try {
        // Проверяем валидность токена
        await authApi.verify();
        this.isAuthenticated = true;
      } catch (error) {
        console.error("Token verification failed:", error);
        localStorage.removeItem("adminToken");
        this.isAuthenticated = false;
      }
    },

    async handleLogin() {
      this.loginError = "";
      this.isLoading = true;

      try {
        const response = await authApi.login({
          username: this.loginForm.username,
          password: this.loginForm.password,
        });

        // Сохраняем токен
        localStorage.setItem("adminToken", response.data.access_token);

        // Устанавливаем авторизацию
        this.isAuthenticated = true;

        // Очищаем форму
        this.loginForm.username = "";
        this.loginForm.password = "";
      } catch (error) {
        console.error("Login failed:", error);
        if (error.response?.status === 401) {
          this.loginError = "Неверный логин или пароль";
        } else if (error.response?.status === 422) {
          this.loginError = "Неверный формат данных";
        } else {
          this.loginError = "Ошибка подключения к серверу";
        }
      } finally {
        this.isLoading = false;
      }
    },

    handleLogout() {
      localStorage.removeItem("adminToken");
      this.isAuthenticated = false;
      this.loginForm.username = "";
      this.loginForm.password = "";
    },
  },
};
</script>

<style scoped>
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-scaleIn {
  animation: scaleIn 0.3s ease;
}
</style>
