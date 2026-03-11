<template>
  <div id="app" class="min-h-screen relative">
    <!-- Фоновое изображение для всего сайта -->
    <div class="fixed inset-0 z-0">
      <img
        src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
        alt="Интерьер ресторана"
        class="w-full h-full object-cover"
      />
      <!-- Затемнение -->
      <div class="absolute inset-0 bg-black/70"></div>
      <!-- Градиентное затемнение -->
      <div
        class="absolute inset-0 bg-gradient-to-b from-black/50 via-black/60 to-black/80"
      ></div>
    </div>

    <!-- Шапка -->
    <AppHeader @toggle-cart="toggleCart" />

    <!-- Корзина -->
    <Cart :is-visible="cartVisible" @close="cartVisible = false" class="z-50" />

    <!-- Основной контент -->
    <main class="relative z-10 pt-24 pb-16">
      <div class="container mx-auto px-4">
        <router-view v-slot="{ Component }">
          <transition name="page" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </div>
    </main>

    <!-- Подвал -->
    <AppFooter class="relative z-10" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import AppHeader from "./components/Header.vue";
import AppFooter from "./components/Footer.vue";
import Cart from "./components/Cart.vue";

export default {
  name: "App",
  components: {
    AppHeader,
    AppFooter,
    Cart,
  },
  data() {
    return {
      cartVisible: false,
    };
  },
  computed: {
    ...mapGetters(["cartItemCount"]),
  },
  methods: {
    toggleCart() {
      this.cartVisible = !this.cartVisible;
    },
  },
};
</script>

<style>
/* Глобальные стили */
#app {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, sans-serif;
}

/* Анимации страниц */
.page-enter-active,
.page-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.page-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.page-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Кастомные стили для скроллбара */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(17, 24, 39, 0.5);
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, #f97316, #dc2626);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(to bottom, #ea580c, #b91c1c);
}

/* Поддержка Firefox */
* {
  scrollbar-width: thin;
  scrollbar-color: #f97316 rgba(17, 24, 39, 0.5);
}

/* Улучшение выделения текста */
::selection {
  background: rgba(249, 115, 22, 0.3);
  color: #ffffff;
}

::-moz-selection {
  background: rgba(249, 115, 22, 0.3);
  color: #ffffff;
}

body {
  margin: 0;
  padding: 0;
}
</style>
