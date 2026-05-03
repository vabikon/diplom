<template>
  <div class="space-y-6">
    <h3 class="text-2xl font-bold text-white">Управление заказами</h3>

    <!-- Форма поиска -->
    <div class="max-w-md">
      <input
        type="text"
        v-model="searchQuery"
        @input="filterOrders"
        placeholder="Поиск по номеру заказа, имени клиента или email..."
        class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
      />
    </div>

    <!-- Статус загрузки -->
    <div v-if="loading" class="text-center py-20">
      <div
        class="inline-block w-16 h-16 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-6"
      ></div>
      <p class="text-gray-400">Загружаем заказы...</p>
    </div>

    <!-- Ошибка -->
    <div v-else-if="error" class="text-center py-20">
      <p class="text-red-400">Ошибка: {{ error }}</p>
    </div>

    <!-- Таблица заказов -->
    <div
      v-else
      class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl overflow-hidden"
    >
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-900/50 border-b border-gray-700">
            <tr>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                ID заказа
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Дата
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Имя
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Телефон
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Товары
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Сумма
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Статус
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Действия
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-700">
            <tr
              v-for="order in filteredOrders"
              :key="order.id"
              class="hover:bg-gray-800/50 transition-colors"
            >
              <td class="px-4 py-3 text-gray-300 font-mono text-sm">
                #{{ formatOrderId(order.id) }}
              </td>
              <td class="px-4 py-3 text-gray-300 text-sm">
                {{ formatDate(order.created_at || order.timestamp) }}
              </td>
              <td class="px-4 py-3 text-white">
                {{
                  order.customer_name ||
                  order.name ||
                  order.customer_phone ||
                  "Гость"
                }}
              </td>
              <td class="px-4 py-3 text-gray-300">
                {{ order.customer_phone || order.phone || "Не указан" }}
              </td>
              <td class="px-4 py-3 text-gray-300">
                {{ order.items ? order.items.length : 0 }} шт.
              </td>
              <td class="px-4 py-3 text-orange-400 font-semibold">
                {{ formatPrice(order.total || 0) }} ₽
              </td>
              <td class="px-4 py-3">
                <select
                  :value="order.status"
                  @change="updateOrderStatus(order.id, $event.target.value)"
                  class="px-3 py-1.5 bg-gray-900 border border-gray-700 text-gray-300 text-sm rounded-lg focus:outline-none focus:border-orange-500 cursor-pointer"
                >
                  <option value="pending">В обработке</option>
                  <option value="confirmed">Подтвержден</option>
                  <option value="preparing">Готовится</option>
                  <option value="ready">Готов</option>
                  <option value="delivered">Доставлен</option>
                  <option value="cancelled">Отменен</option>
                </select>
              </td>
              <td class="px-4 py-3">
                <div class="flex gap-2">
                  <button
                    @click="viewOrder(order)"
                    class="px-3 py-1.5 bg-gray-900 border border-gray-700 text-gray-300 text-sm rounded-lg hover:border-orange-500 hover:text-orange-400 transition-all"
                  >
                    Детали
                  </button>
                  <button
                    @click="deleteOrder(order.id)"
                    class="px-3 py-1.5 bg-gray-900 border border-red-700 text-red-400 text-sm rounded-lg hover:bg-red-500 hover:text-white hover:border-red-500 transition-all"
                  >
                    Удалить
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Модальное окно деталей заказа -->
    <div
      v-if="selectedOrder"
      class="fixed inset-0 bg-black/70 z-[3000] flex items-center justify-center px-4"
      @click="closeModal"
    >
      <div
        class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-2xl w-full max-w-2xl max-h-[80vh] overflow-y-auto"
        @click.stop
      >
        <!-- Заголовок модалки -->
        <div
          class="flex justify-between items-center p-6 border-b border-gray-700"
        >
          <h4 class="text-xl font-semibold text-white">
            Детали заказа #{{ formatOrderId(selectedOrder.id) }}
          </h4>
          <button
            @click="closeModal"
            class="p-2 text-gray-400 hover:text-white transition-colors"
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

        <!-- Тело модалки -->
        <div class="p-6 space-y-6">
          <!-- Информация о клиенте -->
          <div>
            <h5 class="text-lg font-semibold text-white mb-3">
              Информация о клиенте
            </h5>
            <div class="space-y-2 text-gray-300">
              <p>
                <span class="text-gray-500">Имя:</span>
                {{
                  selectedOrder.customer_name ||
                  selectedOrder.name ||
                  selectedOrder.customer_phone ||
                  "Гость"
                }}
              </p>
              <p>
                <span class="text-gray-500">Телефон:</span>
                {{
                  selectedOrder.customer_phone ||
                  selectedOrder.phone ||
                  "Не указан"
                }}
              </p>
            </div>
          </div>

          <!-- Состав заказа -->
          <div>
            <h5 class="text-lg font-semibold text-white mb-3">Состав заказа</h5>
            <div class="space-y-2">
              <div
                v-for="(item, index) in selectedOrder.items"
                :key="index"
                class="flex justify-between items-center py-2 border-b border-gray-700 last:border-0"
              >
                <span class="text-white flex-1">{{
                  item.name || item.item_name
                }}</span>
                <span class="text-gray-400 mx-4"
                  >x{{ item.quantity || 1 }}</span
                >
                <span class="text-orange-400 font-semibold">
                  {{ formatPrice(item.price || 0) }} ₽
                </span>
              </div>
            </div>
          </div>

          <!-- Итого -->
          <div class="pt-4 border-t border-gray-700">
            <div class="flex justify-between items-center">
              <h5 class="text-lg font-semibold text-white">Итого:</h5>
              <span class="text-2xl font-bold text-orange-400">
                {{ formatPrice(selectedOrder.total || 0) }} ₽
              </span>
            </div>
          </div>
        </div>

        <!-- Футер модалки -->
        <div class="p-6 border-t border-gray-700 flex justify-end">
          <button
            @click="closeModal"
            class="px-6 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 text-white rounded-xl hover:border-gray-600 transition-all duration-300"
          >
            Закрыть
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ordersApi } from "@/api";

export default {
  name: "OrdersManager",
  data() {
    return {
      loading: false,
      error: null,
      orders: [],
      filteredOrders: [],
      searchQuery: "",
      selectedOrder: null,
    };
  },
  async mounted() {
    await this.loadOrders();
  },
  methods: {
    async loadOrders() {
      try {
        this.loading = true;
        this.error = null;
        const response = await ordersApi.getAll();
        this.orders = response.data;
        this.filteredOrders = this.orders;
      } catch (error) {
        this.error = error.message || "Ошибка загрузки заказов";
        console.error("Ошибка загрузки заказов:", error);
      } finally {
        this.loading = false;
      }
    },

    updateOrderStatus(orderId, newStatus) {
      ordersApi
        .updateStatus(orderId, newStatus)
        .then(() => {
          // Обновляем статус в списке
          const order = this.orders.find((o) => o.id === orderId);
          if (order) {
            order.status = newStatus;
          }
        })
        .catch((error) => {
          this.error = error.message || "Ошибка обновления статуса заказа";
          console.error("Ошибка обновления статуса заказа:", error);
          this.loadOrders();
        });
    },

    viewOrder(order) {
      this.selectedOrder = order;
    },

    closeModal() {
      this.selectedOrder = null;
    },

    deleteOrder(orderId) {
      if (!confirm("Вы уверены, что хотите удалить этот заказ?")) {
        return;
      }

      ordersApi
        .delete(orderId)
        .then(() => {
          this.orders = this.orders.filter((order) => order.id !== orderId);
          this.filteredOrders = this.filteredOrders.filter(
            (order) => order.id !== orderId
          );
        })
        .catch((error) => {
          this.error = error.message || "Ошибка удаления заказа";
          console.error("Ошибка удаления заказа:", error);
        });
    },

    filterOrders() {
      if (!this.searchQuery) {
        this.filteredOrders = this.orders;
        return;
      }

      const query = this.searchQuery.toLowerCase();
      this.filteredOrders = this.orders.filter((order) => {
        const orderId = this.formatOrderId(order.id).toLowerCase();
        return (
          orderId.includes(query) ||
          (order.customer_name &&
            order.customer_name.toLowerCase().includes(query)) ||
          (order.name && order.name.toLowerCase().includes(query)) ||
          (order.customer_phone && order.customer_phone.includes(query)) ||
          (order.phone && order.phone.includes(query)) ||
          (order.customer_email &&
            order.customer_email.toLowerCase().includes(query)) ||
          (order.email && order.email.toLowerCase().includes(query))
        );
      });
    },

    formatOrderId(id) {
      // Безопасное форматирование ID заказа
      if (!id) return "N/A";

      // Если это строка, используем slice
      if (typeof id === "string") {
        return id.length > 8 ? id.slice(0, 8) : id;
      }

      // Если это число, конвертируем в строку
      if (typeof id === "number") {
        return id.toString();
      }

      // Для любого другого типа, конвертируем в строку и обрезаем
      const idString = String(id);
      return idString.length > 8 ? idString.slice(0, 8) : idString;
    },

    formatDate(dateString) {
      if (!dateString) return "Не указана";
      const date = new Date(dateString);
      return date.toLocaleString("ru-RU", {
        day: "2-digit",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      });
    },

    formatPrice(price) {
      return new Intl.NumberFormat("ru-RU").format(price);
    },
  },
};
</script>

<style scoped>
.orders-manager {
  padding: 20px 0;
}

.search-container {
  margin-bottom: 20px;
}

.search-input {
  width: 100%;
  max-width: 400px;
  padding: 12px;
  border: 1px solid var(--color-gray);
  border-radius: 4px;
  font-size: 14px;
  transition: border-color 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: var(--color-black);
}

.table-container {
  overflow-x: auto;
}

.orders-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--color-white);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.orders-table th,
.orders-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid var(--color-gray);
}

.orders-table th {
  background: var(--color-gray-light);
  font-weight: 600;
  color: var(--color-text);
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.5px;
}

.status-select {
  padding: 6px 10px;
  border: 1px solid var(--color-gray);
  border-radius: 4px;
  font-size: 12px;
  background: var(--color-white);
  cursor: pointer;
}

.action-buttons {
  white-space: nowrap;
  display: flex;
  gap: 5px;
}

.btn {
  padding: 8px 16px;
  border-radius: 4px;
  border: 1px solid;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-block;
  text-align: center;
}

.btn-outline {
  background: transparent;
  color: var(--color-black);
  border-color: var(--color-gray);
}

.btn-outline:hover {
  background: var(--color-black);
  color: var(--color-white);
  border-color: var(--color-black);
}

.btn-danger {
  background: transparent;
  color: #dc2626;
  border-color: #dc2626;
}

.btn-danger:hover {
  background: #dc2626;
  color: var(--color-white);
}

.btn-small {
  padding: 6px 12px;
  font-size: 13px;
}

.loading-state {
  text-align: center;
  padding: 40px;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--color-gray-light);
  border-top-color: var(--color-fire);
  border-radius: 50%;
  margin: 0 auto 20px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.error-state {
  text-align: center;
  padding: 40px;
  color: #dc2626;
}

/* Модальное окно */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: var(--color-white);
  border-radius: 8px;
  max-width: 600px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 20px 10px;
  border-bottom: 1px solid var(--color-gray);
}

.modal-header h4 {
  margin: 0;
  font-size: 20px;
  color: var(--color-black);
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: var(--color-text-light);
  padding: 0;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn:hover {
  color: var(--color-black);
}

.modal-body {
  padding: 20px;
}

.order-info,
.order-details {
  margin-bottom: 20px;
}

.order-info h5,
.order-details h5 {
  margin-top: 0;
  margin-bottom: 10px;
  color: var(--color-black);
}

.order-info p {
  margin: 5px 0;
}

.order-items-list {
  list-style-type: none;
  padding: 0;
}

.order-items-list li {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid var(--color-gray-light);
}

.item-name {
  flex: 1;
}

.item-quantity {
  margin: 0 15px;
  color: var(--color-text-light);
}

.item-price {
  color: var(--color-fire);
  font-weight: 600;
}

.order-total {
  text-align: right;
  font-size: 18px;
  font-weight: 700;
  color: var(--color-black);
  padding-top: 10px;
  border-top: 1px solid var(--color-gray);
}

.modal-footer {
  padding: 15px 20px 20px;
  display: flex;
  justify-content: flex-end;
}

.btn-secondary {
  background: var(--color-gray-light);
  color: var(--color-text);
  border-color: var(--color-gray);
}

.btn-secondary:hover {
  background: var(--color-gray);
}

@media (max-width: 768px) {
  .orders-table {
    font-size: 14px;
  }

  .orders-table th,
  .orders-table td {
    padding: 8px 10px;
  }

  .orders-table th {
    font-size: 11px;
  }

  .action-buttons {
    flex-direction: column;
  }

  .btn-small {
    width: 100%;
    margin-bottom: 5px;
  }

  .modal-content {
    margin: 10px;
    max-height: 90vh;
  }
}
</style>
