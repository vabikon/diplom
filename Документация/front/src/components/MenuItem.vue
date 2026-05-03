<template>
  <div
    :class="[
      'group bg-gradient-to-br from-gray-800/50 to-gray-900/50 backdrop-blur-xl border border-gray-700/50 rounded-2xl overflow-hidden hover:border-orange-500/50 transition-all duration-500 transform hover:-translate-y-2 hover:shadow-2xl hover:shadow-orange-500/10',
      mobile ? 'rounded-xl hover:-translate-y-1' : '',
    ]"
    @mouseenter="isHovered = true"
    @mouseleave="isHovered = false"
  >
    <!-- Мобильная версия -->
    <div v-if="mobile" class="flex gap-4 p-4">
      <!-- Изображение для мобильных -->
      <div
        class="relative w-20 h-20 flex-shrink-0 overflow-hidden rounded-xl bg-gradient-to-br from-gray-800 to-gray-900"
      >
        <img
          :src="item.image || placeholderImage"
          :alt="item.name"
          loading="lazy"
          @error="handleImageError"
          :class="[
            'w-full h-full object-cover transition-opacity duration-300',
            imageLoaded ? 'opacity-100' : 'opacity-0',
          ]"
          @load="imageLoaded = true"
        />

        <!-- Категория для мобильных -->
        <div class="absolute top-1 left-1">
          <span
            class="px-1.5 py-0.5 bg-gradient-to-r from-gray-900/80 to-black/80 backdrop-blur-sm border border-gray-700/50 rounded text-xs text-gray-300 font-medium"
          >
            {{ getCategoryName(item.category) }}
          </span>
        </div>
      </div>

      <!-- Контент для мобильных -->
      <div class="flex-1 min-w-0">
        <!-- Заголовок и цена -->
        <div class="flex justify-between items-start mb-2">
          <h3
            class="text-lg font-bold text-white group-hover:text-orange-400 transition-colors truncate pr-2"
          >
            {{ item.name }}
          </h3>
          <div class="text-orange-400 font-bold text-lg whitespace-nowrap">
            {{ formatPrice(item.price) }} ₽
          </div>
        </div>

        <!-- Вес -->
        <div class="mb-2">
          <span class="text-gray-500 text-sm font-medium">
            {{ item.weight }} г
          </span>
        </div>

        <!-- Описание (сокращенное для мобильных) -->
        <p class="text-gray-300 text-sm mb-3 line-clamp-2">
          {{ item.description }}
        </p>

        <!-- Кнопка добавления в корзину для мобильных -->
        <div v-if="itemQuantity === 0">
          <button
            @click="$emit('add-to-cart', item)"
            class="w-full px-3 py-2 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-lg hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300 flex items-center justify-center gap-2 text-sm"
          >
            <span>В корзину</span>
            <svg
              class="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 6v6m0 0v6m0-6h6m-6 0H6"
              />
            </svg>
          </button>
        </div>

        <!-- Контролы количества для мобильных -->
        <div v-else class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <button
              @click="decreaseQuantity"
              class="w-8 h-8 flex items-center justify-center rounded-lg border border-gray-700 bg-gradient-to-br from-gray-800 to-gray-900 text-gray-300 hover:text-white hover:border-gray-600 transition-all duration-300"
            >
              <svg
                class="w-4 h-4"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M20 12H4"
                />
              </svg>
            </button>

            <span class="text-lg font-bold text-white px-2">{{
              itemQuantity
            }}</span>

            <button
              @click="$emit('add-to-cart', item)"
              class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-r from-orange-500 to-red-500 text-white hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300"
            >
              <svg
                class="w-4 h-4"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                />
              </svg>
            </button>
          </div>

          <span class="text-xs text-gray-500">в корзине</span>
        </div>
      </div>
    </div>

    <!-- Десктопная версия -->
    <div v-else>
      <!-- Изображение -->
      <div
        class="relative h-48 overflow-hidden bg-gradient-to-br from-gray-800 to-gray-900"
      >
        <img
          :src="item.image || placeholderImage"
          :alt="item.name"
          loading="lazy"
          @error="handleImageError"
          :class="[
            'w-full h-full object-cover transform transition-transform duration-700',
            isHovered ? 'scale-110' : 'scale-100',
            imageLoaded ? 'opacity-100' : 'opacity-0',
          ]"
          @load="imageLoaded = true"
        />
        <!-- Оверлей при наведении -->
        <div
          :class="[
            'absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent transition-opacity duration-300',
            isHovered ? 'opacity-100' : 'opacity-0',
          ]"
        ></div>

        <!-- Категория -->
        <div class="absolute top-3 left-3">
          <span
            class="px-3 py-1 bg-gradient-to-r from-gray-900/80 to-black/80 backdrop-blur-sm border border-gray-700/50 rounded-full text-xs text-gray-300 font-medium"
          >
            {{ getCategoryName(item.category) }}
          </span>
        </div>
      </div>

      <!-- Контент -->
      <div class="p-6 flex flex-col flex-1">
        <!-- Заголовок и цена -->
        <div class="flex justify-between items-start mb-3">
          <h3
            class="text-xl font-bold text-white group-hover:text-orange-400 transition-colors flex-1 pr-2"
          >
            {{ item.name }}
          </h3>
          <div class="text-orange-400 font-bold text-xl whitespace-nowrap">
            {{ formatPrice(item.price) }} ₽
          </div>
        </div>

        <!-- Вес -->
        <div class="mb-4">
          <span class="text-gray-500 text-sm font-medium">
            {{ item.weight }} г
          </span>
        </div>

        <!-- Описание -->
        <p class="text-gray-300 text-sm mb-4 flex-1 line-clamp-2">
          {{ item.description }}
        </p>

        <!-- Состав -->
        <div class="mb-6 pt-4 border-t border-gray-700/50">
          <p class="text-gray-400 text-xs">
            <span class="font-semibold text-gray-300">Состав:</span>
            {{ item.composition }}
          </p>
        </div>

        <!-- Кнопка добавления в корзину -->
        <div class="mt-auto">
          <div v-if="itemQuantity === 0">
            <button
              @click="$emit('add-to-cart', item)"
              class="w-full px-4 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300 transform hover:-translate-y-0.5 flex items-center justify-center gap-2"
            >
              <span>Добавить в корзину</span>
              <svg
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                />
              </svg>
            </button>
          </div>

          <!-- Контролы количества -->
          <div v-else class="flex items-center justify-center gap-4">
            <button
              @click="decreaseQuantity"
              class="w-10 h-10 flex items-center justify-center rounded-xl border border-gray-700 bg-gradient-to-br from-gray-800 to-gray-900 text-gray-300 hover:text-white hover:border-gray-600 transition-all duration-300 transform hover:scale-110"
              aria-label="Уменьшить количество"
            >
              <svg
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M20 12H4"
                />
              </svg>
            </button>

            <div class="flex flex-col items-center">
              <span class="text-2xl font-bold text-white">{{
                itemQuantity
              }}</span>
              <span class="text-xs text-gray-500">в корзине</span>
            </div>

            <button
              @click="$emit('add-to-cart', item)"
              class="w-10 h-10 flex items-center justify-center rounded-xl bg-gradient-to-r from-orange-500 to-red-500 text-white hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300 transform hover:scale-110"
              aria-label="Увеличить количество"
            >
              <svg
                class="w-5 h-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Декоративный элемент -->
    <div
      class="absolute inset-0 rounded-2xl bg-gradient-to-r from-orange-500/0 via-orange-500/5 to-orange-500/0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
    ></div>
  </div>
</template>

<script>
export default {
  name: "MenuItem",
  props: {
    item: {
      type: Object,
      required: true,
      default: () => ({
        id: "",
        name: "",
        category: "",
        price: 0,
        weight: 0,
        composition: "",
        description: "",
        image: "",
        featured: false,
      }),
    },
    cart: {
      type: Array,
      default: () => [],
    },
    mobile: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isHovered: false,
      imageLoaded: false,
      placeholderImage:
        "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjMjEyMTIxIi8+PHRleHQgeD0iMjAwIiB5PSIxNTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TWVudSBJdGVtPC90ZXh0Pjwvc3ZnPg==",
    };
  },
  computed: {
    itemQuantity() {
      if (!this.cart || !this.item) return 0;

      const cartItem = this.cart.find(
        (cartItem) => cartItem.id === this.item.id
      );
      return cartItem ? cartItem.quantity : 0;
    },
  },
  methods: {
    getCategoryName(category) {
      const categories = {
        interior: "Интерьер",
        food: "Блюда",
        events: "События",
        staff: "Персонал",
        main: "Основные",
        appetizers: "Закуски",
        desserts: "Десерты",
        drinks: "Напитки",
      };
      return categories[category] || category;
    },
    formatPrice(price) {
      return new Intl.NumberFormat("ru-RU").format(price);
    },
    handleImageError(event) {
      console.error(
        "Ошибка загрузки изображения:",
        this.item.name,
        this.item.image
      );
      event.target.src = this.placeholderImage;
    },
    decreaseQuantity() {
      if (this.itemQuantity > 1) {
        this.$emit("update-quantity", {
          itemId: this.item.id,
          quantity: this.itemQuantity - 1,
        });
      } else {
        this.$emit("remove-from-cart", this.item.id);
      }
    },
  },
};
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
