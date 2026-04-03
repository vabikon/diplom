<template>
  <div class="space-y-6">
    <h3 class="text-2xl font-bold text-white">Бронирования столов</h3>

    <div class="max-w-md">
      <input
        v-model="searchQuery"
        @input="filterReservations"
        type="text"
        placeholder="Поиск по телефону, статусу или источнику..."
        class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
      />
    </div>

    <div v-if="loading" class="text-center py-20">
      <div
        class="inline-block w-16 h-16 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-6"
      ></div>
      <p class="text-gray-400">Загружаем бронирования...</p>
    </div>

    <div v-else-if="error" class="text-center py-20">
      <p class="text-red-400">Ошибка: {{ error }}</p>
    </div>

    <div
      v-else
      class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl overflow-hidden"
    >
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-900/50 border-b border-gray-700">
            <tr>
              <th class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider">
                ID
              </th>
              <th class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider">
                Дата
              </th>
              <th class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider">
                Телефон
              </th>
              <th class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider">
                Источник
              </th>
              <th class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider">
                Статус
              </th>
              <th class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider">
                Действия
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-700">
            <tr
              v-for="reservation in filteredReservations"
              :key="reservation.id"
              class="hover:bg-gray-800/50 transition-colors"
            >
              <td class="px-4 py-3 text-gray-300 font-mono text-sm">
                #{{ reservation.id }}
              </td>
              <td class="px-4 py-3 text-gray-300 text-sm">
                {{ formatDate(reservation.created_at) }}
              </td>
              <td class="px-4 py-3 text-white font-medium">
                {{ reservation.customer_phone }}
              </td>
              <td class="px-4 py-3 text-gray-300">
                {{ getSourceLabel(reservation.source) }}
              </td>
              <td class="px-4 py-3">
                <select
                  :value="reservation.status"
                  @change="updateReservationStatus(reservation.id, $event.target.value)"
                  class="px-3 py-1.5 bg-gray-900 border border-gray-700 text-gray-300 text-sm rounded-lg focus:outline-none focus:border-orange-500 cursor-pointer"
                >
                  <option value="pending">Ожидает</option>
                  <option value="confirmed">Подтверждено</option>
                  <option value="completed">Завершено</option>
                  <option value="cancelled">Отменено</option>
                </select>
              </td>
              <td class="px-4 py-3">
                <button
                  @click="deleteReservation(reservation.id)"
                  class="px-3 py-1.5 bg-gray-900 border border-red-700 text-red-400 text-sm rounded-lg hover:bg-red-500 hover:text-white hover:border-red-500 transition-all"
                >
                  Удалить
                </button>
              </td>
            </tr>
            <tr v-if="filteredReservations.length === 0">
              <td colspan="6" class="px-4 py-8 text-center text-gray-500">
                Бронирования не найдены
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { bookingApi } from "@/api";

export default {
  name: "ReservationsManager",
  data() {
    return {
      loading: false,
      error: null,
      reservations: [],
      filteredReservations: [],
      searchQuery: "",
    };
  },
  async mounted() {
    await this.loadReservations();
  },
  methods: {
    async loadReservations() {
      try {
        this.loading = true;
        this.error = null;
        const response = await bookingApi.getAll();
        this.reservations = response.data;
        this.filteredReservations = response.data;
      } catch (error) {
        this.error = error.message || "Ошибка загрузки бронирований";
        console.error("Ошибка загрузки бронирований:", error);
      } finally {
        this.loading = false;
      }
    },

    filterReservations() {
      const query = this.searchQuery.trim().toLowerCase();
      if (!query) {
        this.filteredReservations = this.reservations;
        return;
      }

      this.filteredReservations = this.reservations.filter((reservation) => {
        return (
          String(reservation.id).includes(query) ||
          (reservation.customer_phone || "").toLowerCase().includes(query) ||
          (reservation.status || "").toLowerCase().includes(query) ||
          (reservation.source || "").toLowerCase().includes(query)
        );
      });
    },

    async updateReservationStatus(reservationId, status) {
      try {
        await bookingApi.updateStatus(reservationId, status);
        const reservation = this.reservations.find((item) => item.id === reservationId);
        if (reservation) {
          reservation.status = status;
        }
        this.filterReservations();
        this.$emit("reservations-updated");
      } catch (error) {
        this.error = error.message || "Ошибка обновления статуса бронирования";
        console.error("Ошибка обновления статуса бронирования:", error);
        await this.loadReservations();
      }
    },

    async deleteReservation(reservationId) {
      if (!confirm("Вы уверены, что хотите удалить это бронирование?")) {
        return;
      }

      try {
        await bookingApi.delete(reservationId);
        this.reservations = this.reservations.filter(
          (reservation) => reservation.id !== reservationId
        );
        this.filterReservations();
        this.$emit("reservations-updated");
      } catch (error) {
        this.error = error.message || "Ошибка удаления бронирования";
        console.error("Ошибка удаления бронирования:", error);
      }
    },

    formatDate(dateString) {
      if (!dateString) return "Не указана";
      const date = new Date(dateString);
      return date.toLocaleString("ru-RU");
    },

    getSourceLabel(source) {
      const labels = {
        home: "Главная",
        about: "О нас",
      };
      return labels[source] || "Не указан";
    },
  },
};
</script>
