<template>
  <div class="space-y-6">
    <h3 class="text-2xl font-bold text-white">Управление отзывами</h3>

    <!-- Форма добавления/редактирования -->
    <div
      class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-6"
    >
      <h4 class="text-xl font-semibold text-white mb-6">
        {{ editingReview ? "Редактировать отзыв" : "Добавить новый отзыв" }}
      </h4>

      <form @submit.prevent="saveReview" class="space-y-4">
        <!-- Первая строка -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label class="block text-gray-400 text-sm mb-2" for="reviewName">
              Имя
            </label>
            <input
              id="reviewName"
              v-model="form.name"
              type="text"
              required
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>

          <div>
            <label class="block text-gray-400 text-sm mb-2" for="reviewEmail">
              Email
            </label>
            <input
              id="reviewEmail"
              v-model="form.email"
              type="email"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>

          <div>
            <label class="block text-gray-400 text-sm mb-2" for="reviewRating">
              Оценка
            </label>
            <select
              id="reviewRating"
              v-model.number="form.rating"
              required
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white focus:outline-none focus:border-orange-500 transition-colors"
            >
              <option v-for="n in 5" :key="n" :value="n">{{ n }} звезд</option>
            </select>
          </div>
        </div>

        <!-- Отзыв -->
        <div>
          <label class="block text-gray-400 text-sm mb-2" for="reviewText">
            Отзыв
          </label>
          <textarea
            id="reviewText"
            v-model="form.text"
            rows="4"
            required
            class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors resize-none"
          ></textarea>
        </div>

        <!-- Ответ администратора -->
        <div>
          <label class="block text-gray-400 text-sm mb-2" for="reviewAnswer">
            Ответ администратора
          </label>
          <textarea
            id="reviewAnswer"
            v-model="form.answer"
            rows="3"
            class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors resize-none"
          ></textarea>
        </div>

        <!-- Кнопки -->
        <div class="flex gap-3 pt-4">
          <button
            type="submit"
            class="px-6 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300"
          >
            {{ editingReview ? "Сохранить изменения" : "Добавить отзыв" }}
          </button>
          <button
            v-if="editingReview"
            type="button"
            @click="cancelEdit"
            class="px-6 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 text-white rounded-xl hover:border-gray-600 transition-all duration-300"
          >
            Отмена
          </button>
        </div>
      </form>
    </div>

    <!-- Статус загрузки -->
    <div v-if="loading" class="text-center py-20">
      <div
        class="inline-block w-16 h-16 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-6"
      ></div>
      <p class="text-gray-400">Загружаем отзывы...</p>
    </div>

    <!-- Ошибка -->
    <div v-else-if="error" class="text-center py-20">
      <p class="text-red-400">Ошибка: {{ error }}</p>
    </div>

    <!-- Таблица отзывов -->
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
                Имя
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Оценка
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Отзыв
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Дата
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Ответ администратора
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
              v-for="review in reviews"
              :key="review.id"
              class="hover:bg-gray-800/50 transition-colors"
            >
              <td class="px-4 py-3 text-white font-medium">
                {{ review.name }}
              </td>
              <td class="px-4 py-3">
                <div class="flex items-center gap-2">
                  <div class="flex">
                    <span
                      v-for="n in 5"
                      :key="n"
                      :class="
                        n <= review.rating ? 'text-orange-400' : 'text-gray-600'
                      "
                      class="text-lg"
                    >
                      ★
                    </span>
                  </div>
                  <span class="text-gray-400 text-sm"
                    >({{ review.rating }})</span
                  >
                </div>
              </td>
              <td class="px-4 py-3 text-gray-300 max-w-xs truncate">
                {{ review.text }}
              </td>
              <td class="px-4 py-3 text-gray-400 text-sm">
                {{ formatDate(review.date) }}
              </td>
              <td class="px-4 py-3">
                <span
                  v-if="review.answer"
                  class="text-gray-300 max-w-xs truncate block"
                >
                  {{ review.answer }}
                </span>
                <span v-else class="text-gray-500 text-sm italic">
                  Не отвечено
                </span>
              </td>
              <td class="px-4 py-3">
                <div class="flex gap-2">
                  <button
                    @click="editReview(review)"
                    class="px-3 py-1.5 bg-gray-900 border border-gray-700 text-gray-300 text-sm rounded-lg hover:border-orange-500 hover:text-orange-400 transition-all"
                  >
                    Редактировать
                  </button>
                  <button
                    @click="deleteReview(review.id)"
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
  </div>
</template>

<script>
import { reviewsApi } from "@/api";

export default {
  name: "ReviewsManager",
  data() {
    return {
      loading: false,
      error: null,
      reviews: [],
      editingReview: null,
      form: {
        name: "",
        email: "",
        rating: 5,
        text: "",
        answer: "",
        date: null,
      },
    };
  },
  async mounted() {
    await this.loadReviews();
  },
  methods: {
    async loadReviews() {
      try {
        this.loading = true;
        this.error = null;
        const response = await reviewsApi.getAll();
        this.reviews = response.data;
      } catch (error) {
        this.error = error.message || "Ошибка загрузки отзывов";
        console.error("Ошибка загрузки отзывов:", error);
      } finally {
        this.loading = false;
      }
    },

    editReview(review) {
      this.editingReview = review;
      this.form = { ...review };
    },

    cancelEdit() {
      this.editingReview = null;
      this.resetForm();
    },

    resetForm() {
      this.form = {
        name: "",
        email: "",
        rating: 5,
        text: "",
        answer: "",
        date: null,
      };
    },

    async saveReview() {
      try {
        if (this.editingReview) {
          // Обновление существующего отзыва
          const response = await reviewsApi.update(
            this.editingReview.id,
            this.form
          );
          // Обновляем элемент в списке
          const index = this.reviews.findIndex(
            (review) => review.id === this.editingReview.id
          );
          if (index !== -1) {
            this.reviews[index] = response.data;
          }
        } else {
          // Добавление нового отзыва
          const response = await reviewsApi.create(this.form);
          this.reviews.unshift(response.data);
        }

        this.cancelEdit();
        this.$emit("reviews-updated");
      } catch (error) {
        this.error = error.message || "Ошибка сохранения отзыва";
        console.error("Ошибка сохранения отзыва:", error);
      }
    },

    async deleteReview(reviewId) {
      if (!confirm("Вы уверены, что хотите удалить этот отзыв?")) {
        return;
      }

      try {
        await reviewsApi.delete(reviewId);
        this.reviews = this.reviews.filter((review) => review.id !== reviewId);
        this.$emit("reviews-updated");
      } catch (error) {
        this.error = error.message || "Ошибка удаления отзыва";
        console.error("Ошибка удаления отзыва:", error);
      }
    },

    formatDate(dateString) {
      if (!dateString) return "Не указана";
      const date = new Date(dateString);
      return date.toLocaleDateString("ru-RU");
    },
  },
};
</script>

<style scoped>
.reviews-manager {
  padding: 20px 0;
}

.form-container {
  background: var(--color-gray-light);
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.form-container h4 {
  margin-top: 0;
  margin-bottom: 20px;
  font-size: 20px;
}

.review-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-row {
  display: flex;
  gap: 20px;
}

.form-group {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 5px;
  font-weight: 500;
  color: var(--color-text);
}

.form-control {
  padding: 10px;
  border: 1px solid var(--color-gray);
  border-radius: 4px;
  font-size: 14px;
  transition: border-color 0.2s ease;
}

.form-control:focus {
  outline: none;
  border-color: var(--color-black);
}

.form-actions {
  display: flex;
  gap: 15px;
  justify-content: flex-start;
  margin-top: 10px;
}

.table-container {
  overflow-x: auto;
}

.reviews-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--color-white);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.reviews-table th,
.reviews-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid var(--color-gray);
}

.reviews-table th {
  background: var(--color-gray-light);
  font-weight: 600;
  color: var(--color-text);
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.5px;
}

.star-filled {
  color: #fbbf24;
}

.star-empty {
  color: #d1d5db;
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

.btn-primary {
  background: var(--color-black);
  color: var(--color-white);
  border-color: var(--color-black);
}

.btn-primary:hover {
  background: var(--color-fire);
  border-color: var(--color-fire);
}

.btn-secondary {
  background: var(--color-gray-light);
  color: var(--color-text);
  border-color: var(--color-gray);
}

.btn-secondary:hover {
  background: var(--color-gray);
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

@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
    gap: 0;
  }

  .reviews-table {
    font-size: 14px;
  }

  .reviews-table th,
  .reviews-table td {
    padding: 8px 10px;
  }

  .action-buttons {
    flex-direction: column;
  }

  .btn-small {
    width: 100%;
    margin-bottom: 5px;
  }

  .form-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>
