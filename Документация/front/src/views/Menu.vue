<template>
  <div class="min-h-screen">
    <!-- Заголовок страницы -->
    <div class="container mx-auto px-4 mb-8 sm:mb-12 text-center">
      <h1
        class="text-3xl sm:text-4xl md:text-5xl font-bold text-white mb-3 sm:mb-4 animate-slideUp"
      >
        Меню
      </h1>
      <p
        class="text-gray-400 text-base sm:text-lg animate-slideUp"
        style="animation-delay: 0.1s"
      >
        Тщательно отобранные блюда от нашего шеф-повара
      </p>
    </div>

    <!-- Статус загрузки -->
    <div
      v-if="menuLoading"
      class="container mx-auto px-4 text-center py-16 sm:py-20"
    >
      <div
        class="inline-block w-12 h-12 sm:w-16 sm:h-16 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-4 sm:mb-6"
      ></div>
      <p class="text-gray-400 text-sm sm:text-base">Загружаем меню...</p>
    </div>

    <!-- Ошибка -->
    <div
      v-else-if="menuError"
      class="container mx-auto px-4 text-center py-16 sm:py-20"
    >
      <div
        class="w-16 h-16 sm:w-20 sm:h-20 mx-auto mb-4 sm:mb-6 flex items-center justify-center rounded-full bg-gradient-to-br from-red-500/20 to-red-600/20"
      >
        <span class="text-2xl sm:text-3xl">❌</span>
      </div>
      <p class="text-gray-300 mb-4 sm:mb-6 text-sm sm:text-base">
        Ошибка загрузки меню: {{ menuError }}
      </p>
      <button
        @click="loadMenu"
        class="px-4 sm:px-6 py-2.5 sm:py-3 border border-gray-700 text-gray-300 rounded-xl hover:border-gray-600 hover:text-white transition-colors text-sm sm:text-base"
      >
        Попробовать снова
      </button>
    </div>

    <!-- Основной контент -->
    <div v-else class="container mx-auto px-4">
      <!-- Фильтры и поиск -->
      <div class="max-w-6xl mx-auto mb-6 sm:mb-8">
        <!-- Мобильная версия фильтров -->
        <div class="block sm:hidden space-y-4">
          <!-- Поиск для мобильных -->
          <div class="relative">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Поиск по меню..."
              class="w-full pl-10 pr-4 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-orange-500 transition-colors text-sm"
            />
            <div
              class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500"
            >
              🔍
            </div>
          </div>

          <!-- Категории для мобильных -->
          <div class="flex gap-2 overflow-x-auto pb-2 scrollbar-hide">
            <button
              v-for="category in categories"
              :key="category.id"
              @click="activeCategory = category.id"
              :class="[
                'px-4 py-2 rounded-lg border transition-all duration-300 font-medium text-sm whitespace-nowrap flex-shrink-0',
                activeCategory === category.id
                  ? 'bg-gradient-to-r from-orange-500 to-red-500 text-white border-orange-500 shadow-lg shadow-orange-500/25'
                  : 'bg-gradient-to-br from-gray-800 to-gray-900 border-gray-700 text-gray-300 hover:border-orange-500/50 hover:text-orange-300',
              ]"
            >
              {{ category.name }}
            </button>
          </div>
        </div>

        <!-- Десктопная версия фильтров -->
        <div
          class="hidden sm:flex flex-col lg:flex-row gap-6 items-start lg:items-center justify-between"
        >
          <!-- Категории -->
          <div class="flex flex-wrap gap-2">
            <button
              v-for="category in categories"
              :key="category.id"
              @click="activeCategory = category.id"
              :class="[
                'px-5 py-2.5 rounded-xl border transition-all duration-300 font-medium',
                activeCategory === category.id
                  ? 'bg-gradient-to-r from-orange-500 to-red-500 text-white border-orange-500 shadow-lg shadow-orange-500/25'
                  : 'bg-gradient-to-br from-gray-800 to-gray-900 border-gray-700 text-gray-300 hover:border-orange-500/50 hover:text-orange-300',
              ]"
            >
              {{ category.name }}
            </button>
          </div>

          <!-- Поиск -->
          <div class="relative w-full lg:w-64">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Поиск по меню..."
              class="w-full pl-12 pr-4 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-orange-500 transition-colors"
            />
            <div
              class="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-500"
            >
              🔍
            </div>
          </div>
        </div>
      </div>

      <!-- Состояние пустого поиска -->
      <div v-if="filteredItems.length === 0" class="text-center py-16 sm:py-20">
        <div
          class="w-24 h-24 sm:w-32 sm:h-32 mx-auto mb-4 sm:mb-6 flex items-center justify-center rounded-full bg-gradient-to-br from-gray-800/50 to-gray-900/50"
        >
          <span class="text-3xl sm:text-5xl">🍽️</span>
        </div>
        <p class="text-gray-400 text-base sm:text-lg mb-2">
          По вашему запросу ничего не найдено
        </p>
        <p class="text-gray-500 text-sm">
          Попробуйте изменить поисковый запрос или выбрать другую категорию
        </p>
      </div>

      <!-- Сетка меню -->
      <div v-else>
        <!-- Мобильная сетка (1 колонка) -->
        <div class="block sm:hidden space-y-4 mb-6">
          <MenuItem
            v-for="item in filteredItems"
            :key="item.id"
            :item="item"
            :cart="cart"
            @add-to-cart="addToCart"
            @remove-from-cart="removeFromCart"
            @update-quantity="updateQuantity"
            :mobile="true"
          />
        </div>

        <!-- Десктопная сетка -->
        <div class="hidden sm:block">
          <div
            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto mb-8"
          >
            <MenuItem
              v-for="item in filteredItems"
              :key="item.id"
              :item="item"
              :cart="cart"
              @add-to-cart="addToCart"
              @remove-from-cart="removeFromCart"
              @update-quantity="updateQuantity"
            />
          </div>
        </div>

        <!-- Итог -->
        <div class="max-w-6xl mx-auto pt-4 sm:pt-6 border-t border-gray-800">
          <p class="text-gray-400 text-center text-sm sm:text-base">
            Найдено блюд:
            <span class="text-orange-400 font-semibold">{{
              filteredItems.length
            }}</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex";
import MenuItem from "@/components/MenuItem.vue";

export default {
  name: "Menu",
  components: {
    MenuItem,
  },
  data() {
    return {
      activeCategory: "all",
      searchQuery: "",
      categories: [
        { id: "all", name: "Все" },
        { id: "appetizers", name: "Закуски" },
        { id: "main", name: "Основные" },
        { id: "desserts", name: "Десерты" },
        { id: "drinks", name: "Напитки" },
      ],
    };
  },
  computed: {
    ...mapState({
      menuLoading: (state) => state.loading.menu,
      menuError: (state) => state.error,
    }),
    ...mapGetters(["menuItems", "menuItemsByCategory", "cart"]),

    filteredItems() {
      let items =
        this.activeCategory === "all"
          ? this.menuItems
          : this.menuItemsByCategory(this.activeCategory);

      // Поиск по запросу
      if (this.searchQuery.trim()) {
        const query = this.searchQuery.toLowerCase().trim();
        items = items.filter(
          (item) =>
            item.name.toLowerCase().includes(query) ||
            (item.description &&
              item.description.toLowerCase().includes(query)) ||
            (item.composition && item.composition.toLowerCase().includes(query))
        );
      }

      return items;
    },
  },
  async mounted() {
    await this.loadMenu();
  },
  methods: {
    ...mapActions([
      "fetchMenuItems",
      "addToCart",
      "removeFromCart",
      "updateCartQuantity",
    ]),

    async loadMenu() {
      try {
        await this.fetchMenuItems();
      } catch (error) {
        console.error("Failed to load menu:", error);
      }
    },

    updateQuantity({ itemId, quantity }) {
      this.updateCartQuantity({ itemId, quantity });
    },
  },
};
</script>

<style scoped>
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slideUp {
  opacity: 0;
  transform: translateY(20px);
  animation: slideUp 0.6s ease forwards;
}

/* Скрытие скроллбара для горизонтального скролла категорий */
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

@media (max-width: 640px) {
  .container {
    padding-left: 0.75rem;
    padding-right: 0.75rem;
  }

  .space-y-4 > * + * {
    margin-top: 1rem;
  }

  .py-16 {
    padding-top: 3rem;
    padding-bottom: 3rem;
  }

  .mb-8 {
    margin-bottom: 1.5rem;
  }

  .mb-6 {
    margin-bottom: 1rem;
  }
}

@media (max-width: 480px) {
  .container {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }

  .text-3xl {
    font-size: 1.75rem;
  }

  .py-16 {
    padding-top: 2rem;
    padding-bottom: 2rem;
  }
}
</style>
