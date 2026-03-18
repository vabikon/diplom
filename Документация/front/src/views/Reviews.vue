<template>
  <div class="min-h-screen">
    <!-- Заголовок страницы -->
    <div class="container mx-auto px-4 mb-12 text-center">
      <h1
        class="text-4xl md:text-5xl font-bold text-white mb-4 animate-slideUp"
      >
        Отзывы
      </h1>
      <p
        class="text-gray-400 text-lg animate-slideUp"
        style="animation-delay: 0.1s"
      >
        Мнения наших гостей
      </p>
    </div>

    <!-- Статус загрузки -->
    <div v-if="reviewsLoading" class="container mx-auto px-4 text-center py-20">
      <div
        class="inline-block w-16 h-16 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-6"
      ></div>
      <p class="text-gray-400">Загружаем отзывы...</p>
    </div>

    <!-- Основной контент -->
    <div v-else class="container mx-auto px-4">
      <div
        class="grid grid-cols-1 lg:grid-cols-3 gap-8 max-w-7xl mx-auto mb-12"
      >
        <!-- Левая колонка - Статистика и список отзывов -->
        <div class="lg:col-span-2 space-y-8">
          <!-- Статистика -->
          <div class="grid grid-cols-2 gap-4 mb-8">
            <div
              class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-6 text-center transform hover:scale-105 transition-transform duration-300"
            >
              <div
                class="text-4xl font-bold bg-gradient-to-r from-orange-500 to-red-500 bg-clip-text text-transparent mb-2"
              >
                {{ reviews.length }}
              </div>
              <div class="text-gray-400 text-sm uppercase tracking-wider">
                Всего отзывов
              </div>
            </div>

            <div
              class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-6 text-center transform hover:scale-105 transition-transform duration-300"
            >
              <div
                class="text-4xl font-bold bg-gradient-to-r from-orange-500 to-red-500 bg-clip-text text-transparent mb-2"
              >
                {{ averageRating }}
              </div>
              <div class="text-gray-400 text-sm uppercase tracking-wider">
                Средний рейтинг
              </div>
            </div>
          </div>

          <!-- Состояние пустого списка -->
          <div v-if="reviews.length === 0" class="text-center py-20">
            <div
              class="w-32 h-32 mx-auto mb-6 flex items-center justify-center rounded-full bg-gradient-to-br from-gray-800/50 to-gray-900/50"
            >
              <span class="text-5xl">💭</span>
            </div>
            <p class="text-gray-400 text-lg mb-2">Пока нет отзывов</p>
            <p class="text-gray-500 text-sm">Будьте первым!</p>
          </div>

          <!-- Список отзывов -->
          <div v-else class="space-y-4">
            <div
              v-for="review in reviews"
              :key="review.id"
              class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-6 hover:border-orange-500/50 transition-all duration-300 animate-slideUp"
            >
              <!-- Заголовок отзыва -->
              <div class="flex justify-between items-start mb-4">
                <div>
                  <h4 class="text-white font-semibold text-lg mb-1">
                    {{ review.name }}
                  </h4>
                  <span class="text-gray-500 text-sm">{{
                    formatDate(review.date || review.createdAt)
                  }}</span>
                </div>

                <!-- Рейтинг -->
                <div class="flex gap-1">
                  <span
                    v-for="star in 5"
                    :key="star"
                    :class="
                      star <= review.rating
                        ? 'text-orange-500'
                        : 'text-gray-600'
                    "
                    class="text-xl"
                  >
                    ★
                  </span>
                </div>
              </div>

              <!-- Текст отзыва -->
              <p class="text-gray-300 leading-relaxed mb-4">
                {{ review.text }}
              </p>

              <!-- Ответ ресторана -->
              <div
                v-if="review.answer"
                class="mt-4 pl-4 border-l-4 border-orange-500 bg-gradient-to-r from-orange-500/10 to-transparent rounded-r-lg p-3"
              >
                <p class="text-orange-400 font-semibold text-sm mb-1">
                  Ответ ресторана:
                </p>
                <p class="text-gray-300 text-sm">{{ review.answer }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Правая колонка - Форма добавления отзыва -->
        <div class="lg:col-span-1">
          <div
            class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-6 sticky top-8"
          >
            <h2 class="text-2xl font-bold text-white mb-2">Оставить отзыв</h2>
            <p class="text-gray-400 text-sm mb-6">
              Поделитесь вашим впечатлением
            </p>

            <form @submit.prevent="submitReview" class="space-y-4">
              <!-- Имя -->
              <div>
                <label class="block text-gray-400 text-sm mb-2" for="name">
                  Имя *
                </label>
                <input
                  id="name"
                  v-model="newReview.name"
                  type="text"
                  required
                  placeholder="Ваше имя"
                  :disabled="isSubmitting"
                  class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors disabled:opacity-50"
                />
              </div>

              <!-- Email -->
              <div>
                <label class="block text-gray-400 text-sm mb-2" for="email">
                  Email
                </label>
                <input
                  id="email"
                  v-model="newReview.email"
                  type="email"
                  placeholder="Ваш email (необязательно)"
                  :disabled="isSubmitting"
                  class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors disabled:opacity-50"
                />
              </div>

              <!-- Рейтинг -->
              <div>
                <label class="block text-gray-400 text-sm mb-2">
                  Оценка *
                </label>
                <div class="flex items-center gap-2">
                  <button
                    v-for="rating in 5"
                    :key="rating"
                    type="button"
                    @click="newReview.rating = rating"
                    :disabled="isSubmitting"
                    :class="
                      rating <= newReview.rating
                        ? 'text-orange-500'
                        : 'text-gray-600'
                    "
                    class="text-2xl hover:text-orange-400 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    ★
                  </button>
                  <span class="text-gray-500 text-sm ml-2"
                    >{{ newReview.rating }}/5</span
                  >
                </div>
              </div>

              <!-- Текст отзыва -->
              <div>
                <label class="block text-gray-400 text-sm mb-2" for="review">
                  Отзыв *
                </label>
                <textarea
                  id="review"
                  v-model="newReview.text"
                  required
                  rows="5"
                  placeholder="Расскажите о вашем опыте..."
                  :disabled="isSubmitting"
                  class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors resize-none disabled:opacity-50"
                ></textarea>
              </div>

              <!-- Кнопка отправки -->
              <button
                type="submit"
                :disabled="isSubmitting || !isFormValid"
                :class="
                  isSubmitting || !isFormValid
                    ? 'opacity-50 cursor-not-allowed'
                    : 'hover:shadow-lg hover:shadow-orange-500/25 transform hover:scale-105'
                "
                class="w-full py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl transition-all duration-300"
              >
                {{ isSubmitting ? "Отправка..." : "Отправить отзыв" }}
              </button>

              <p class="text-gray-500 text-xs text-center">
                * Обязательные поля
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>

    <!-- Уведомление -->
    <div
      v-if="notification.show"
      :class="
        notification.type === 'success'
          ? 'bg-gradient-to-r from-orange-500 to-red-500'
          : 'bg-gradient-to-r from-red-600 to-red-700'
      "
      class="fixed top-8 right-8 px-6 py-4 rounded-xl text-white font-medium shadow-2xl z-50 animate-slideIn"
    >
      {{ notification.message }}
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from "vuex";

export default {
  name: "Reviews",
  data() {
    return {
      newReview: {
        name: "",
        email: "",
        rating: 5,
        text: "",
      },
      isSubmitting: false,
      notification: {
        show: false,
        message: "",
        type: "info",
      },
    };
  },
  computed: {
    ...mapState({
      reviewsLoading: (state) => state.loading.reviews,
    }),
    ...mapGetters(["reviews", "averageRating"]),

    isFormValid() {
      return (
        this.newReview.name.trim() &&
        this.newReview.text.trim() &&
        this.newReview.rating > 0
      );
    },
  },
  async mounted() {
    await this.loadReviews();
  },
  methods: {
    ...mapActions(["fetchReviews", "addReview"]),

    async loadReviews() {
      try {
        await this.fetchReviews();
      } catch (error) {
        console.error("Failed to load reviews:", error);
        this.showNotification("Ошибка загрузки отзывов", "error");
      }
    },

    formatDate(dateString) {
      if (!dateString) return "";
      const date = new Date(dateString);
      return date.toLocaleDateString("ru-RU", {
        day: "numeric",
        month: "long",
        year: "numeric",
      });
    },

    async submitReview() {
      if (!this.isFormValid) {
        this.showNotification(
          "Пожалуйста, заполните все обязательные поля",
          "error"
        );
        return;
      }

      this.isSubmitting = true;

      try {
        const reviewData = {
          ...this.newReview,
          date: new Date().toISOString(),
        };

        await this.addReview(reviewData);

        this.newReview = {
          name: "",
          email: "",
          rating: 5,
          text: "",
        };

        this.showNotification("Спасибо за ваш отзыв!", "success");
      } catch (error) {
        console.error("Error submitting review:", error);
        this.showNotification("Произошла ошибка при отправке отзыва", "error");
      } finally {
        this.isSubmitting = false;
      }
    },

    showNotification(message, type = "info") {
      this.notification = {
        show: true,
        message,
        type,
      };

      setTimeout(() => {
        this.notification.show = false;
      }, 3000);
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

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(100%);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animate-slideUp {
  opacity: 0;
  transform: translateY(20px);
  animation: slideUp 0.6s ease forwards;
}

.animate-slideIn {
  animation: slideIn 0.3s ease forwards;
}

.space-y-4 > * {
  animation-delay: calc(var(--index, 0) * 0.1s);
}

@media (max-width: 1024px) {
  .sticky {
    position: static;
  }
}

@media (max-width: 640px) {
  .grid {
    gap: 1rem !important;
  }
}
</style>
