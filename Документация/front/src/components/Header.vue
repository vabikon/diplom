<template>
  <header
    class="fixed top-0 left-0 right-0 bg-gray-900/90 backdrop-blur-xl border-b border-orange-500/20 shadow-2xl shadow-black/30 z-50"
  >
    <!-- Анимированный огненный эффект -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div
        class="absolute -bottom-10 left-1/4 w-1/2 h-20 bg-gradient-to-t from-orange-600/20 to-transparent blur-xl animate-pulse"
      ></div>
      <div
        class="absolute -bottom-5 left-1/3 w-1/3 h-12 bg-gradient-to-t from-orange-500/15 to-transparent blur-lg animate-pulse delay-500"
      ></div>
    </div>

    <div class="container mx-auto px-4 py-4">
      <div class="flex items-center justify-between">
        <!-- Логотип -->
        <router-link to="/" class="flex items-center space-x-3 group relative">
          <div class="flex flex-col">
            <span
              class="text-xl sm:text-2xl font-bold bg-gradient-to-r from-orange-500 via-red-500 to-yellow-500 bg-clip-text text-transparent animate-gradient"
            >
              Мангал Хаус
            </span>
            <span class="text-xs text-gray-400 tracking-widest"
              >RESTAURANT</span
            >
          </div>

          <!-- Эффект при наведении -->
          <div
            class="absolute -inset-2 bg-gradient-to-r from-orange-500/0 via-orange-500/5 to-orange-500/0 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-500"
          ></div>
        </router-link>

        <!-- Навигация для десктопа -->
        <nav
          class="hidden lg:flex items-center space-x-1 bg-gray-800/50 backdrop-blur-sm rounded-2xl p-1 border border-gray-700/50"
        >
          <router-link
            v-for="item in navItems"
            :key="item.to"
            :to="item.to"
            class="relative px-4 xl:px-6 py-3 rounded-xl text-gray-300 hover:text-white transition-all duration-300 group"
            active-class="text-white bg-gradient-to-r from-orange-500/20 to-red-500/10"
          >
            <div class="flex items-center space-x-2">
              <!-- SVG иконки напрямую -->
              <svg
                v-if="item.to === '/'"
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>

              <svg
                v-else-if="item.to === '/menu'"
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                />
              </svg>

              <svg
                v-else-if="item.to === '/about'"
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>

              <svg
                v-else-if="item.to === '/reviews'"
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
                />
              </svg>

              <span class="font-medium text-sm xl:text-base">{{
                item.text
              }}</span>
            </div>

            <!-- Активный индикатор -->
            <div
              class="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-0 group-hover:w-12 xl:group-hover:w-16 h-0.5 bg-gradient-to-r from-transparent via-orange-500 to-transparent transition-all duration-300"
            ></div>

            <!-- Эффект свечения -->
            <div
              class="absolute inset-0 rounded-xl bg-gradient-to-r from-orange-500/0 via-orange-500/5 to-orange-500/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
            ></div>
          </router-link>
        </nav>

        <!-- Корзина и мобильное меню -->
        <div class="flex items-center space-x-3">
          <!-- Корзина -->
          <button
            @click="toggleCart"
            class="relative p-2.5 sm:p-3 rounded-xl bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 hover:border-orange-500/30 transition-all duration-300 group"
          >
            <div class="flex items-center space-x-2">
              <svg
                class="w-5 h-5 sm:w-6 sm:h-6 text-gray-400 group-hover:text-orange-400 transition-colors"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
              <span
                class="hidden xl:inline text-gray-300 group-hover:text-white text-sm"
                >Корзина</span
              >
            </div>

            <!-- Бейдж -->
            <span
              v-if="cartItemCount > 0"
              class="absolute -top-1 -right-1 sm:-top-2 sm:-right-2 bg-gradient-to-r from-orange-500 to-red-500 text-white text-xs font-bold rounded-full w-5 h-5 sm:w-6 sm:h-6 flex items-center justify-center animate-pulse"
            >
              {{ cartItemCount }}
            </span>

            <!-- Свечение -->
            <div
              class="absolute inset-0 rounded-xl bg-gradient-to-r from-orange-500/0 via-orange-500/10 to-orange-500/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
            ></div>
          </button>

          <!-- Кнопка мобильного меню -->
          <button
            @click="toggleMobileMenu"
            class="lg:hidden p-2.5 sm:p-3 rounded-xl bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 hover:border-orange-500/30 transition-all duration-300 group"
            :class="{ 'border-orange-500/50': mobileMenuOpen }"
          >
            <div class="relative w-5 h-5 sm:w-6 sm:h-6">
              <!-- Анимированное меню -->
              <span
                class="absolute top-0 left-0 w-full h-0.5 bg-gradient-to-r from-gray-400 to-gray-300 rounded transition-all duration-300"
                :class="mobileMenuOpen ? 'rotate-45 translate-y-2' : ''"
              ></span>
              <span
                class="absolute top-2 left-0 w-full h-0.5 bg-gradient-to-r from-gray-400 to-gray-300 rounded transition-all duration-300"
                :class="mobileMenuOpen ? 'opacity-0' : ''"
              ></span>
              <span
                class="absolute top-4 left-0 w-full h-0.5 bg-gradient-to-r from-gray-400 to-gray-300 rounded transition-all duration-300"
                :class="mobileMenuOpen ? '-rotate-45 -translate-y-2' : ''"
              ></span>
            </div>
          </button>
        </div>
      </div>
    </div>

    <!-- Мобильное меню -->
    <div
      v-if="mobileMenuOpen"
      class="lg:hidden absolute top-full left-0 right-0 bg-gray-900 lg:bg-gray-900/95 backdrop-blur-xl border-t border-orange-500/20 shadow-2xl animate-slideDown z-50"
    >
      <div class="container mx-auto px-4 py-6">
        <div class="space-y-2">
          <router-link
            v-for="item in navItems"
            :key="item.to"
            :to="item.to"
            @click="closeMobileMenu"
            class="flex items-center space-x-3 px-4 py-4 rounded-xl text-gray-300 hover:text-white hover:bg-gradient-to-r from-gray-800/50 to-gray-900/50 transition-all duration-300 group border border-transparent hover:border-orange-500/20"
            active-class="text-white bg-gradient-to-r from-orange-500/10 to-red-500/5 border-orange-500/30"
          >
            <!-- SVG иконки для мобильного меню -->
            <svg
              v-if="item.to === '/'"
              class="w-6 h-6 text-gray-400 group-hover:text-orange-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
              />
            </svg>

            <svg
              v-else-if="item.to === '/menu'"
              class="w-6 h-6 text-gray-400 group-hover:text-orange-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
              />
            </svg>

            <svg
              v-else-if="item.to === '/about'"
              class="w-6 h-6 text-gray-400 group-hover:text-orange-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>

            <svg
              v-else-if="item.to === '/reviews'"
              class="w-6 h-6 text-gray-400 group-hover:text-orange-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
              />
            </svg>

            <span class="font-medium text-lg">{{ item.text }}</span>

            <svg
              class="ml-auto w-5 h-5 text-gray-500 group-hover:text-orange-400 transition-colors"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </router-link>

          <!-- Корзина в мобильном меню -->
          <button
            @click="toggleCart"
            class="w-full flex items-center space-x-3 px-4 py-4 rounded-xl text-gray-300 hover:text-white hover:bg-gradient-to-r from-gray-800/50 to-gray-900/50 transition-all duration-300 group border border-transparent hover:border-orange-500/20 mt-4"
          >
            <svg
              class="w-6 h-6 text-gray-400 group-hover:text-orange-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
              />
            </svg>
            <span class="font-medium text-lg">Корзина</span>
            <span
              v-if="cartItemCount > 0"
              class="ml-auto bg-gradient-to-r from-orange-500 to-red-500 text-white text-sm font-bold rounded-full w-6 h-6 flex items-center justify-center animate-pulse"
            >
              {{ cartItemCount }}
            </span>
            <svg
              v-else
              class="ml-auto w-5 h-5 text-gray-500 group-hover:text-orange-400 transition-colors"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeader",
  data() {
    return {
      mobileMenuOpen: false,
      navItems: [
        { to: "/", text: "Главная" },
        { to: "/menu", text: "Меню" },
        { to: "/about", text: "О нас" },
        { to: "/reviews", text: "Отзывы" },
      ],
    };
  },
  computed: {
    cartItemCount() {
      return this.$store?.getters?.cartItemCount || 0;
    },
  },
  methods: {
    toggleCart() {
      this.$emit("toggle-cart");
      this.closeMobileMenu();
    },
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
    },
    closeMobileMenu() {
      this.mobileMenuOpen = false;
    },
  },
};
</script>

<style scoped>
@keyframes gradient {
  0%,
  100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

.animate-gradient {
  background-size: 200% 200%;
  animation: gradient 3s ease infinite;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slideDown {
  animation: slideDown 0.3s ease-out;
}
</style>
