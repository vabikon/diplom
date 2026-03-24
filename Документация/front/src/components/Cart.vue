<template>
  <div
    v-if="isVisible"
    class="fixed inset-0 bg-black/50 z-[2000] flex justify-end animate-fadeIn"
    @click.self="$emit('close')"
  >
    <div
      class="w-full max-w-lg bg-gradient-to-b from-gray-900 via-black to-gray-900 h-full flex flex-col animate-slideInRight"
    >
      <!-- Заголовок -->
      <div
        class="px-6 py-6 border-b border-gray-700 flex justify-between items-center"
      >
        <h2 class="text-2xl font-bold text-white">Корзина</h2>
        <button
          @click="$emit('close')"
          aria-label="Закрыть корзину"
          class="p-2 rounded-lg text-gray-400 hover:text-white hover:bg-gray-800 transition-colors"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path d="M18 6L6 18M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Пустая корзина -->
      <div
        v-if="cart.length === 0 && !showPhoneDialog && !showSuccessDialog"
        class="flex-1 flex flex-col items-center justify-center px-6 py-10"
      >
        <div
          class="w-32 h-32 mb-6 flex items-center justify-center rounded-full bg-gradient-to-br from-gray-800/50 to-gray-900/50"
        >
          <svg
            width="64"
            height="64"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            class="text-gray-600"
          >
            <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z" />
            <line x1="3" y1="6" x2="21" y2="6" />
            <path d="M16 10a4 4 0 01-8 0" />
          </svg>
        </div>
        <p class="text-gray-400 text-lg mb-8 text-center">Ваша корзина пуста</p>
        <button
          @click="continueShopping"
          class="px-6 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 text-white rounded-xl hover:border-orange-500/50 transition-all duration-300 flex items-center gap-2"
        >
          <span>Продолжить покупки</span>
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path d="M5 12h14M12 5l7 7-7 7" />
          </svg>
        </button>
      </div>

      <!-- Содержимое корзины -->
      <div v-else class="flex-1 flex flex-col px-6 py-4">
        <!-- Список товаров -->
        <div class="flex-1 overflow-y-auto mb-6 space-y-4">
          <div
            v-for="item in cart"
            :key="item.id"
            class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-4 hover:border-orange-500/50 transition-all duration-300"
          >
            <div class="flex gap-4">
              <!-- Изображение -->
              <div
                class="w-20 h-20 rounded-lg overflow-hidden bg-gray-800 flex-shrink-0"
              >
                <img
                  :src="item.image || '/placeholder.jpg'"
                  :alt="item.name"
                  loading="lazy"
                  class="w-full h-full object-cover"
                />
              </div>

              <!-- Детали -->
              <div class="flex-1 min-w-0">
                <div class="flex justify-between items-start mb-2">
                  <h3 class="text-white font-semibold truncate flex-1 pr-2">
                    {{ item.name }}
                  </h3>
                  <button
                    @click="removeItem(item.id)"
                    aria-label="Удалить"
                    class="p-1 text-gray-500 hover:text-red-500 transition-colors flex-shrink-0"
                  >
                    <svg
                      width="16"
                      height="16"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                    >
                      <path d="M18 6L6 18M6 6l12 12" />
                    </svg>
                  </button>
                </div>

                <p class="text-gray-400 text-sm mb-3">
                  {{ item.price }} ₽ × {{ item.quantity }}
                </p>

                <!-- Управление количеством -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-2">
                    <button
                      @click="updateQuantity(item.id, item.quantity - 1)"
                      :disabled="item.quantity <= 1"
                      aria-label="Уменьшить количество"
                      class="w-8 h-8 bg-gray-900 border border-gray-700 rounded-lg flex items-center justify-center text-white hover:border-orange-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:border-gray-700"
                    >
                      −
                    </button>
                    <span
                      class="text-white font-semibold min-w-[24px] text-center"
                    >
                      {{ item.quantity }}
                    </span>
                    <button
                      @click="updateQuantity(item.id, item.quantity + 1)"
                      aria-label="Увеличить количество"
                      class="w-8 h-8 bg-gray-900 border border-gray-700 rounded-lg flex items-center justify-center text-white hover:border-orange-500 transition-colors"
                    >
                      +
                    </button>
                  </div>

                  <div class="text-orange-500 font-bold text-lg">
                    {{ item.price * item.quantity }} ₽
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Итоги -->
        <div class="border-t-2 border-orange-500 pt-6 pb-4 space-y-4">
          <div class="flex justify-between items-center text-gray-300">
            <span>Товары:</span>
            <span>{{ subtotal }} ₽</span>
          </div>

          <div class="h-px bg-gray-700"></div>

          <div class="flex justify-between items-center">
            <span class="text-white text-lg font-semibold">Итого:</span>
            <span
              class="text-2xl font-bold bg-gradient-to-r from-orange-500 to-red-500 bg-clip-text text-transparent"
            >
              {{ subtotal }} ₽
            </span>
          </div>
        </div>

        <!-- Кнопки действий -->
        <div class="grid grid-cols-2 gap-3 pb-6">
          <button
            @click="clearCart"
            class="px-4 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 text-white rounded-xl hover:border-red-500/50 transition-all duration-300 flex items-center justify-center gap-2"
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"
              />
            </svg>
            <span>Очистить</span>
          </button>
          <button
            @click="checkout"
            class="px-4 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300 transform hover:scale-105 flex items-center justify-center gap-2"
          >
            <span>Оформить</span>
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path d="M5 12h14M12 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Диалог ввода телефона -->
      <div
        v-if="showPhoneDialog"
        class="fixed inset-0 bg-black/70 z-[3000] flex items-center justify-center px-4 animate-fadeIn"
        @click="cancelOrder"
      >
        <div
          class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-2xl w-full max-w-md p-6 animate-scaleIn"
          @click.stop
        >
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-xl font-semibold text-white">Оформление заказа</h3>
            <button
              @click="cancelOrder"
              aria-label="Закрыть"
              class="p-1 text-gray-400 hover:text-white transition-colors"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M18 6L6 18M6 6l12 12" />
              </svg>
            </button>
          </div>

          <p class="text-gray-400 text-sm mb-6 text-center">
            С вами свяжутся для подтверждения заказа
          </p>

          <input
            v-model="phoneNumber"
            type="tel"
            placeholder="+7 (___) ___-__-__"
            inputmode="numeric"
            maxlength="18"
            @input="handlePhoneInput"
            @keydown="handlePhoneKeydown"
            @keyup.enter="confirmOrder"
            class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors mb-6"
          />

          <div class="flex gap-3">
            <button
              @click="cancelOrder"
              class="flex-1 px-4 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 text-white rounded-xl hover:border-gray-600 transition-all duration-300"
            >
              Отмена
            </button>
            <button
              @click="confirmOrder"
              class="flex-1 px-4 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300"
            >
              Подтвердить
            </button>
          </div>
        </div>
      </div>

      <!-- Диалог успеха -->
      <div
        v-if="showSuccessDialog"
        class="fixed inset-0 bg-black/70 z-[3000] flex items-center justify-center px-4 animate-fadeIn"
        @click="closeSuccessDialog"
      >
        <div
          class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-2xl w-full max-w-md p-8 text-center animate-scaleIn"
          @click.stop
        >
          <div class="flex justify-between items-start mb-6">
            <h3 class="text-xl font-semibold text-orange-500 flex-1">
              Заказ оформлен!
            </h3>
            <button
              @click="closeSuccessDialog"
              aria-label="Закрыть"
              class="p-1 text-gray-400 hover:text-white transition-colors"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M18 6L6 18M6 6l12 12" />
              </svg>
            </button>
          </div>

          <div class="mb-6 animate-bounceIn">
            <svg
              width="64"
              height="64"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              class="text-orange-500 mx-auto"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>

          <p class="text-white text-lg font-semibold mb-3">
            Ваш заказ успешно оформлен!
          </p>
          <p class="text-gray-400 mb-8 leading-relaxed">
            С вами свяжутся по указанному номеру телефона для подтверждения.
          </p>

          <button
            @click="closeSuccessDialog"
            class="w-full px-6 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300"
          >
            Понятно
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations } from "vuex";
import { ordersApi } from "@/api";
import {
  formatRussianPhone,
  isValidRussianPhone,
  removePhoneDigit,
} from "@/utils/phone";

export default {
  name: "Cart",
  props: {
    isVisible: Boolean,
  },
  data() {
    return {
      showPhoneDialog: false,
      showSuccessDialog: false,
      phoneNumber: "",
    };
  },
  computed: {
    ...mapState(["cart"]),
    ...mapGetters(["cartTotal"]),
    subtotal() {
      return this.cartTotal;
    },
  },
  methods: {
    ...mapMutations(["UPDATE_QUANTITY", "REMOVE_FROM_CART", "CLEAR_CART"]),
    updateQuantity(itemId, quantity) {
      if (quantity > 0) {
        this.UPDATE_QUANTITY({ itemId, quantity });
      } else {
        this.REMOVE_FROM_CART(itemId);
      }
    },
    removeItem(itemId) {
      this.REMOVE_FROM_CART(itemId);
    },
    clearCart() {
      if (confirm("Вы уверены, что хотите очистить корзину?")) {
        this.CLEAR_CART();
      }
    },
    continueShopping() {
      this.$emit("close");
      this.$router.push("/menu");
    },
    checkout() {
      this.showPhoneDialog = true;
      this.phoneNumber = "";
    },
    handlePhoneInput() {
      this.phoneNumber = formatRussianPhone(this.phoneNumber);
    },
    handlePhoneKeydown(event) {
      if (event.key !== "Backspace" && event.key !== "Delete") {
        return;
      }

      const input = event.target;
      const cursor = input.selectionStart ?? this.phoneNumber.length;
      const nextValue = removePhoneDigit(
        this.phoneNumber,
        cursor,
        event.key === "Delete" ? "forward" : "backward"
      );

      if (nextValue === this.phoneNumber) {
        return;
      }

      event.preventDefault();
      this.phoneNumber = nextValue;
      this.$nextTick(() => {
        const nextCursor = Math.min(cursor, this.phoneNumber.length);
        input.setSelectionRange(nextCursor, nextCursor);
      });
    },

    async confirmOrder() {
      // Проверяем валидность номера телефона
      if (!this.validatePhoneNumber(this.phoneNumber)) {
        alert("Пожалуйста, введите корректный номер телефона");
        return;
      }

      try {
        // Подготовим данные для отправки
        const orderData = {
          items: this.cart.map((item) => ({
            id: item.id,
            name: item.name,
            price: item.price,
            quantity: item.quantity,
          })),
          total: this.subtotal,
          customer_name: "Гость",
          customer_phone: this.phoneNumber,
        };

        const response = await ordersApi.create(orderData);

        this.showPhoneDialog = false;
        this.showSuccessDialog = true;
        this.CLEAR_CART();
        this.phoneNumber = "";
      } catch (error) {
        console.error("Ошибка при оформлении заказа:", error);
        alert("Ошибка при оформлении заказа. Пожалуйста, попробуйте еще раз.");
      }
    },

    validatePhoneNumber(phone) {
      return isValidRussianPhone(phone);
    },

    cancelOrder() {
      this.showPhoneDialog = false;
      this.phoneNumber = "";
    },

    closeSuccessDialog() {
      this.showSuccessDialog = false;
      this.$emit("close");
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

@keyframes slideInRight {
  from {
    transform: translateX(100%);
  }
  to {
    transform: translateX(0);
  }
}

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

@keyframes bounceIn {
  0% {
    opacity: 0;
    transform: scale(0.3) translateY(20px);
  }
  50% {
    transform: scale(1.05) translateY(-5px);
  }
  70% {
    transform: scale(0.9) translateY(2px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.2s ease;
}

.animate-slideInRight {
  animation: slideInRight 0.3s ease;
}

.animate-scaleIn {
  animation: scaleIn 0.2s ease;
}

.animate-bounceIn {
  animation: bounceIn 0.5s ease 0.2s both;
}

@media (max-width: 640px) {
  .grid-cols-2 {
    grid-template-columns: 1fr;
  }
}
</style>
