<template>
  <div
    class="min-h-screen bg-gradient-to-b from-gray-900 via-black to-gray-900"
  >
    <!-- Шапка админки -->
    <div
      class="border-b border-gray-700 bg-gradient-to-br from-gray-800 to-gray-900"
    >
      <div class="container mx-auto px-4 py-6">
        <div class="flex justify-between items-center">
          <div>
            <h1 class="text-3xl font-bold text-white mb-1">
              Панель администратора
            </h1>
            <p class="text-gray-400 text-sm">
              Управление рестораном "Гастрономия"
            </p>
          </div>
          <button
            @click="handleLogout"
            class="px-6 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 text-white rounded-xl hover:border-red-500/50 transition-all duration-300 flex items-center gap-2"
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4" />
              <polyline points="16 17 21 12 16 7" />
              <line x1="21" y1="12" x2="9" y2="12" />
            </svg>
            <span>Выйти</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Вкладки -->
    <div class="container mx-auto px-4 py-6">
      <div
        class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-2xl overflow-hidden"
      >
        <!-- Навигация по вкладкам -->
        <div class="border-b border-gray-700 bg-gray-900/50">
          <div class="flex overflow-x-auto">
            <button
              v-for="tab in tabs"
              :key="tab.id"
              @click="currentTab = tab.id"
              :class="[
                'flex-1 px-6 py-4 text-center font-medium transition-all duration-300 relative whitespace-nowrap',
                currentTab === tab.id
                  ? 'text-white bg-gradient-to-br from-gray-800 to-gray-900'
                  : 'text-gray-400 hover:text-white hover:bg-gray-800/50',
              ]"
            >
              {{ tab.name }}
              <div
                v-if="currentTab === tab.id"
                class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-500 to-red-500"
              ></div>
            </button>
          </div>
        </div>

        <!-- Контент вкладок -->
        <div class="p-6">
          <div v-show="currentTab === 'menu'" class="animate-fadeIn">
            <MenuManager @menu-updated="handleMenuUpdate" />
          </div>
          <div v-show="currentTab === 'gallery'" class="animate-fadeIn">
            <GalleryManager @gallery-updated="handleGalleryUpdate" />
          </div>
          <div v-show="currentTab === 'orders'" class="animate-fadeIn">
            <OrdersManager @orders-updated="handleOrdersUpdate" />
          </div>
          <div v-show="currentTab === 'reservations'" class="animate-fadeIn">
            <ReservationsManager
              @reservations-updated="handleReservationsUpdate"
            />
          </div>
          <div v-show="currentTab === 'reviews'" class="animate-fadeIn">
            <ReviewsManager @reviews-updated="handleReviewsUpdate" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MenuManager from "@/components/Admin/MenuManager.vue";
import GalleryManager from "@/components/Admin/GalleryManager.vue";
import ReviewsManager from "@/components/Admin/ReviewsManager.vue";
import OrdersManager from "@/components/Admin/OrdersManager.vue";
import ReservationsManager from "@/components/Admin/ReservationsManager.vue";

export default {
  name: "AdminPanel",
  components: {
    MenuManager,
    GalleryManager,
    ReviewsManager,
    OrdersManager,
    ReservationsManager,
  },
  data() {
    return {
      currentTab: "menu",
      tabs: [
        { id: "menu", name: "Управление меню" },
        { id: "gallery", name: "Управление галереей" },
        { id: "orders", name: "Управление заказами" },
        { id: "reservations", name: "Бронирования столов" },
        { id: "reviews", name: "Управление отзывами" },
      ],
    };
  },
  methods: {
    handleLogout() {
      if (confirm("Вы уверены, что хотите выйти?")) {
        this.$emit("logout");
      }
    },

    handleMenuUpdate() {
      console.log("Меню обновлено");
    },

    handleGalleryUpdate() {
      console.log("Галерея обновлена");
    },

    handleOrdersUpdate() {
      console.log("Заказы обновлены");
    },

    handleReservationsUpdate() {
      console.log("Бронирования обновлены");
    },

    handleReviewsUpdate() {
      console.log("Отзывы обновлены");
    },
  },
};
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.animate-fadeIn {
  animation: fadeIn 0.3s ease;
}

/* Стилизация скроллбара для навигации */
.overflow-x-auto::-webkit-scrollbar {
  height: 4px;
}

.overflow-x-auto::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
}

.overflow-x-auto::-webkit-scrollbar-thumb {
  background: rgba(255, 107, 53, 0.5);
  border-radius: 2px;
}

.overflow-x-auto::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 107, 53, 0.7);
}

@media (max-width: 768px) {
  .flex.overflow-x-auto button {
    flex: 0 0 auto;
    min-width: 150px;
  }
}
</style>
