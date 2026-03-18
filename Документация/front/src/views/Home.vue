<template>
  <div class="home min-h-screen relative">
    <!-- Основной контент -->
    <div class="relative z-10">
      <!-- Герой-секция -->
      <section class="relative py-16 sm:py-20 lg:py-32 overflow-hidden">
        <!-- Декоративные элементы -->
        <div class="absolute inset-0 pointer-events-none">
          <div
            class="absolute top-1/4 left-1/4 w-32 h-32 sm:w-64 sm:h-64 bg-orange-500/10 rounded-full blur-3xl animate-pulse"
          ></div>
          <div
            class="absolute bottom-1/4 right-1/4 w-32 h-32 sm:w-64 sm:h-64 bg-red-500/10 rounded-full blur-3xl animate-pulse delay-1000"
          ></div>
        </div>

        <div class="container mx-auto px-4 relative z-10">
          <div class="max-w-6xl mx-auto">
            <div
              class="flex flex-col lg:flex-row items-start gap-8 sm:gap-12 lg:gap-20"
            >
              <!-- Текстовый блок -->
              <div class="lg:w-1/2 space-y-4 sm:space-y-6">
                <div class="space-y-3 sm:space-y-4">
                  <h1
                    class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-white leading-tight"
                  >
                    <span
                      class="block opacity-0 animate-slideUp"
                      style="animation-delay: 0.1s"
                    >
                      Искусство
                    </span>
                    <span
                      class="block bg-gradient-to-r from-orange-400 via-red-400 to-yellow-400 bg-clip-text text-transparent opacity-0 animate-slideUp"
                      style="animation-delay: 0.2s"
                    >
                      гастрономии
                    </span>
                  </h1>
                  <p
                    class="text-orange-300 text-base sm:text-lg font-medium opacity-0 animate-slideUp"
                    style="animation-delay: 0.3s"
                  >
                    Основано в 2015 году
                  </p>
                  <p
                    class="text-gray-300 text-base sm:text-lg leading-relaxed opacity-0 animate-slideUp"
                    style="animation-delay: 0.4s"
                  >
                    Минимализм в интерьере, максимализм во вкусе. Каждое блюдо —
                    история, рассказанная шеф-поваром.
                  </p>
                </div>

                <!-- Кнопки действий -->
                <div
                  class="flex flex-col sm:flex-row flex-wrap gap-3 sm:gap-4 pt-4 opacity-0 animate-slideUp"
                  style="animation-delay: 0.5s"
                >
                  <router-link
                    to="/menu"
                    class="group px-6 sm:px-8 py-3 sm:py-4 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-xl hover:shadow-orange-500/25 transition-all duration-300 transform hover:-translate-y-1 inline-flex items-center justify-center gap-3"
                  >
                    <span>Меню</span>
                    <svg
                      class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M17 8l4 4m0 0l-4 4m4-4H3"
                      />
                    </svg>
                  </router-link>
                  <router-link
                    to="/about"
                    class="px-6 sm:px-8 py-3 sm:py-4 border-2 border-gray-600 text-gray-300 font-semibold rounded-xl hover:border-orange-500 hover:text-orange-400 transition-all duration-300 transform hover:-translate-y-1 text-center"
                  >
                    О нас
                  </router-link>
                </div>
              </div>

              <!-- Часы работы -->
              <div class="lg:w-1/2 w-full">
                <div
                  class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-2xl p-6 sm:p-8 max-w-md lg:ml-auto transform lg:hover:rotate-2 transition-transform duration-500"
                >
                  <div class="flex items-center justify-between mb-4 sm:mb-6">
                    <h3 class="text-lg sm:text-xl font-bold text-white">
                      Часы работы
                    </h3>
                  </div>

                  <div class="space-y-3 sm:space-y-4">
                    <div
                      v-for="(hour, index) in hours"
                      :key="hour.days"
                      class="flex justify-between items-center py-2 sm:py-3 border-b border-gray-700/30 last:border-0 opacity-0 animate-slideUp"
                      :style="`animation-delay: ${0.6 + index * 0.1}s`"
                    >
                      <span class="text-gray-400 text-sm sm:text-base">{{
                        hour.days
                      }}</span>
                      <span
                        class="text-white font-semibold text-sm sm:text-base"
                        >{{ hour.time }}</span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Популярные блюда -->
      <section class="py-16 sm:py-20">
        <div class="container mx-auto px-4">
          <div class="max-w-4xl mx-auto text-center mb-8 sm:mb-12">
            <h2
              class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-3 sm:mb-4 opacity-0 animate-slideUp"
            >
              Популярные позиции
            </h2>
            <p
              class="text-gray-400 text-sm sm:text-base opacity-0 animate-slideUp"
              style="animation-delay: 0.1s"
            >
              То, что выбирают чаще всего
            </p>
          </div>

          <div
            v-if="featuredItems.length > 0"
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 max-w-6xl mx-auto"
          >
            <router-link
              v-for="(item, index) in featuredItems"
              :key="item.id"
              to="/menu"
              class="group block bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-2xl overflow-hidden hover:border-orange-500/50 transition-all duration-500 transform hover:-translate-y-2 hover:shadow-2xl hover:shadow-orange-500/10 opacity-0 animate-slideUp"
              :style="`animation-delay: ${0.2 + index * 0.1}s`"
            >
              <!-- Изображение -->
              <div class="relative h-40 sm:h-48 overflow-hidden">
                <img
                  :src="item.image"
                  :alt="item.name"
                  class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700"
                />
                <div
                  class="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
                ></div>
              </div>

              <!-- Контент -->
              <div class="p-4 sm:p-6">
                <div class="flex justify-between items-start mb-3 sm:mb-4">
                  <h3
                    class="text-lg sm:text-xl font-bold text-white group-hover:text-orange-400 transition-colors flex-1 pr-2"
                  >
                    {{ item.name }}
                  </h3>
                  <span
                    class="text-orange-400 font-bold text-lg sm:text-xl whitespace-nowrap"
                  >
                    {{ item.price }} ₽
                  </span>
                </div>

                <div
                  class="flex items-center justify-between pt-3 sm:pt-4 border-t border-gray-700/30"
                >
                  <span class="text-gray-400 text-xs sm:text-sm"
                    >Попробовать</span
                  >
                  <div
                    class="w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center rounded-full bg-gradient-to-r from-gray-700 to-gray-800 group-hover:from-orange-500 group-hover:to-red-500 transition-all duration-300 transform group-hover:scale-110"
                  >
                    <svg
                      class="w-3 h-3 sm:w-4 sm:h-4 text-gray-400 group-hover:text-white transition-colors"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M17 8l4 4m0 0l-4 4m4-4H3"
                      />
                    </svg>
                  </div>
                </div>
              </div>
            </router-link>
          </div>

          <!-- Кнопка "Полное меню" -->
          <div
            class="text-center mt-8 sm:mt-12 opacity-0 animate-slideUp"
            style="animation-delay: 0.5s"
          >
            <router-link
              to="/menu"
              class="inline-flex items-center gap-2 text-orange-400 hover:text-orange-300 font-semibold group"
            >
              <span>Полное меню</span>
              <svg
                class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 8l4 4m0 0l-4 4m4-4H3"
                />
              </svg>
            </router-link>
          </div>
        </div>
      </section>

      <!-- Банкеты и мероприятия -->
      <section class="py-12 sm:py-16 lg:py-20">
        <div class="container mx-auto px-4">
          <div class="max-w-4xl mx-auto">
            <!-- Заголовок секции -->
            <div class="text-center mb-8 sm:mb-12">
              <h2
                class="text-2xl sm:text-3xl lg:text-4xl font-bold text-white mb-2 sm:mb-4 opacity-0 animate-slideUp"
              >
                Банкеты и мероприятия
              </h2>
              <p
                class="text-gray-300 text-sm sm:text-base lg:text-lg leading-relaxed opacity-0 animate-slideUp max-w-2xl mx-auto"
                style="animation-delay: 0.1s"
              >
                Создаем атмосферу для ваших особенных моментов
              </p>
            </div>

            <!-- Мобильная версия -->
            <div class="block sm:hidden space-y-4">
              <!-- Услуги для мобильных -->
              <div
                v-for="(item, index) in banquetItems"
                :key="item.title"
                class="bg-gradient-to-r from-gray-800/60 to-gray-900/60 backdrop-blur-xl border border-gray-700/40 rounded-xl p-4 hover:border-orange-500/30 transition-all duration-300 opacity-0 animate-slideUp"
                :style="`animation-delay: ${0.2 + index * 0.1}s`"
              >
                <div class="flex items-center gap-3 mb-2">
                  <div
                    class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-r from-orange-500/20 to-red-500/20"
                  >
                    <span class="text-lg">{{ item.icon }}</span>
                  </div>
                  <h3 class="text-white font-semibold text-base">
                    {{ item.title }}
                  </h3>
                </div>
                <p class="text-gray-400 text-sm pl-11">
                  {{ item.description }}
                </p>
              </div>

              <!-- Краткая информация для мобильных -->
              <div
                class="bg-gradient-to-br from-gray-800/60 to-gray-900/60 backdrop-blur-xl border border-gray-700/40 rounded-xl p-4 text-center opacity-0 animate-slideUp"
                style="animation-delay: 0.6s"
              >
                <div class="flex justify-center items-center gap-6 mb-4">
                  <div>
                    <div class="text-xl font-bold text-orange-400">100</div>
                    <div class="text-gray-400 text-xs">человек</div>
                  </div>
                  <div class="w-px h-8 bg-gray-700"></div>
                  <div>
                    <div class="text-xl font-bold text-orange-400">5+</div>
                    <div class="text-gray-400 text-xs">лет опыта</div>
                  </div>
                </div>

                <!-- Кнопка для мобильных -->
                <button
                  @click="showBookingDialog"
                  class="w-full py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-lg transition-all duration-300"
                >
                  Забронировать
                </button>

                <p class="text-gray-400 text-xs mt-3">
                  Или звоните:
                  <span class="text-orange-400">+7 (495) 123-45-67</span>
                </p>
              </div>
            </div>

            <!-- Десктопная версия -->
            <div class="hidden sm:block">
              <div
                class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-2xl p-6 lg:p-8"
              >
                <!-- Список услуг в сетке -->
                <div
                  class="grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 mb-6 lg:mb-8"
                >
                  <div
                    v-for="(item, index) in banquetItems"
                    :key="item.title"
                    class="flex items-start gap-4 p-4 rounded-xl bg-gradient-to-br from-gray-700/30 to-gray-800/30 border border-gray-600/20 hover:border-orange-500/30 transition-all duration-300 opacity-0 animate-slideUp"
                    :style="`animation-delay: ${0.2 + index * 0.1}s`"
                  >
                    <!-- Иконка -->
                    <div
                      class="w-10 h-10 lg:w-12 lg:h-12 flex items-center justify-center rounded-xl bg-gradient-to-r from-orange-500/20 to-red-500/20 flex-shrink-0"
                    >
                      <span class="text-xl lg:text-2xl">{{ item.icon }}</span>
                    </div>

                    <!-- Контент -->
                    <div class="flex-1">
                      <h3
                        class="text-white font-semibold text-base lg:text-lg mb-1"
                      >
                        {{ item.title }}
                      </h3>
                      <p class="text-gray-400 text-sm">
                        {{ item.description }}
                      </p>
                    </div>
                  </div>
                </div>

                <!-- Информация и статистика -->
                <div
                  class="grid grid-cols-3 gap-4 lg:gap-6 mb-6 lg:mb-8 pt-6 border-t border-gray-700/30"
                >
                  <div
                    class="text-center p-3 lg:p-4 rounded-xl bg-gradient-to-br from-gray-700/20 to-gray-800/20"
                  >
                    <div
                      class="text-2xl lg:text-3xl font-bold text-orange-400 mb-1"
                    >
                      100
                    </div>
                    <div class="text-gray-400 text-sm">человек</div>
                    <div class="text-gray-500 text-xs">вместимость</div>
                  </div>

                  <div
                    class="text-center p-3 lg:p-4 rounded-xl bg-gradient-to-br from-gray-700/20 to-gray-800/20"
                  >
                    <div
                      class="text-2xl lg:text-3xl font-bold text-orange-400 mb-1"
                    >
                      24/7
                    </div>
                    <div class="text-gray-400 text-sm">поддержка</div>
                    <div class="text-gray-500 text-xs">организация</div>
                  </div>

                  <div
                    class="text-center p-3 lg:p-4 rounded-xl bg-gradient-to-br from-gray-700/20 to-gray-800/20"
                  >
                    <div
                      class="text-2xl lg:text-3xl font-bold text-orange-400 mb-1"
                    >
                      5+
                    </div>
                    <div class="text-gray-400 text-sm">лет опыта</div>
                    <div class="text-gray-500 text-xs">банкеты</div>
                  </div>
                </div>

                <!-- Кнопка бронирования -->
                <div class="text-center">
                  <button
                    @click="showBookingDialog"
                    class="group w-full sm:w-auto px-8 lg:px-10 py-4 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-xl hover:shadow-orange-500/25 transition-all duration-300 transform hover:-translate-y-1 inline-flex items-center justify-center gap-3 opacity-0 animate-slideUp"
                    style="animation-delay: 0.7s"
                  >
                    <span>Забронировать мероприятие</span>
                    <svg
                      class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M17 8l4 4m0 0l-4 4m4-4H3"
                      />
                    </svg>
                  </button>

                  <p
                    class="text-gray-400 text-sm mt-4 opacity-0 animate-slideUp"
                    style="animation-delay: 0.8s"
                  >
                    Или позвоните нам:
                    <span class="text-orange-400 font-semibold"
                      >+7 (495) 123-45-67</span
                    >
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Галерея -->
      <section v-if="galleryImages.length > 0" class="py-16 sm:py-20">
        <div class="container mx-auto px-4">
          <div class="max-w-4xl mx-auto text-center mb-8 sm:mb-12">
            <h2
              class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-3 sm:mb-4 opacity-0 animate-slideUp"
            >
              Атмосфера
            </h2>
            <p
              class="text-gray-400 text-sm sm:text-base opacity-0 animate-slideUp"
              style="animation-delay: 0.1s"
            >
              Уютный минимализм
            </p>
          </div>

          <Gallery
            :images="galleryImages"
            :limit="3"
            :columns="1"
            class="sm:hidden"
          />
          <Gallery
            :images="galleryImages"
            :limit="3"
            :columns="2"
            class="hidden sm:block lg:hidden"
          />
          <Gallery
            :images="galleryImages"
            :limit="3"
            :columns="3"
            class="hidden lg:block"
          />

          <!-- Кнопка "Смотреть галерею" -->
          <div
            class="text-center mt-8 sm:mt-12 opacity-0 animate-slideUp"
            style="animation-delay: 0.5s"
          >
            <router-link
              to="/about"
              class="inline-flex items-center gap-2 text-orange-400 hover:text-orange-300 font-semibold group"
            >
              <span>Смотреть галерею</span>
              <svg
                class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 8l4 4m0 0l-4 4m4-4H3"
                />
              </svg>
            </router-link>
          </div>
        </div>
      </section>

      <!-- Отзывы -->
      <section v-if="featuredReviews.length > 0" class="py-16 sm:py-20">
        <div class="container mx-auto px-4">
          <div class="max-w-4xl mx-auto text-center mb-8 sm:mb-12">
            <h2
              class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-3 sm:mb-4 opacity-0 animate-slideUp"
            >
              Отзывы гостей
            </h2>
            <p
              class="text-gray-400 text-sm sm:text-base opacity-0 animate-slideUp"
              style="animation-delay: 0.1s"
            >
              Что говорят о нас
            </p>
          </div>

          <div
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 max-w-6xl mx-auto"
          >
            <div
              v-for="(review, index) in featuredReviews"
              :key="review.id"
              class="group bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-2xl p-4 sm:p-6 hover:border-orange-500/50 transition-all duration-500 transform hover:-translate-y-2 opacity-0 animate-slideUp"
              :style="`animation-delay: ${0.2 + index * 0.1}s`"
            >
              <!-- Заголовок отзыва -->
              <div class="flex justify-between items-start mb-3 sm:mb-4">
                <div class="flex items-center gap-1">
                  <span
                    v-for="star in 5"
                    :key="star"
                    :class="
                      star <= review.rating
                        ? 'text-orange-400'
                        : 'text-gray-600'
                    "
                    class="text-base sm:text-lg"
                  >
                    ★
                  </span>
                </div>
                <span class="text-gray-500 text-xs sm:text-sm">
                  {{ formatDate(review.date) }}
                </span>
              </div>

              <!-- Текст отзыва -->
              <p
                class="text-gray-300 italic mb-4 sm:mb-6 leading-relaxed text-sm sm:text-base"
              >
                "{{ review.text }}"
              </p>

              <!-- Автор -->
              <div class="pt-3 sm:pt-4 border-t border-gray-700/30">
                <p class="text-white font-semibold text-sm sm:text-base">
                  — {{ review.name }}
                </p>
              </div>

              <!-- Эффект при наведении -->
              <div
                class="absolute inset-0 rounded-2xl bg-gradient-to-r from-orange-500/0 via-orange-500/5 to-orange-500/0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
              ></div>
            </div>
          </div>

          <!-- Кнопка "Все отзывы" -->
          <div
            class="text-center mt-8 sm:mt-12 opacity-0 animate-slideUp"
            style="animation-delay: 0.5s"
          >
            <router-link
              to="/reviews"
              class="inline-flex items-center gap-2 text-orange-400 hover:text-orange-300 font-semibold group"
            >
              <span>Все отзывы</span>
              <svg
                class="w-5 h-5 transform group-hover:translate-x-1 transition-transform"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 8l4 4m0 0l-4 4m4-4H3"
                />
              </svg>
            </router-link>
          </div>
        </div>
      </section>

      <!-- Диалог бронирования -->
      <div
        v-if="showBookingPhoneDialog"
        class="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-fadeIn"
        @click="cancelBooking"
      >
        <div
          class="bg-gradient-to-br from-gray-800/90 to-gray-900/90 backdrop-blur-xl border border-gray-700/50 rounded-2xl p-6 w-full max-w-md transform scale-95 animate-scaleIn"
          @click.stop
        >
          <!-- Заголовок -->
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-lg sm:text-xl font-bold text-white">
              Бронирование стола
            </h3>
            <button
              @click="cancelBooking"
              class="text-gray-400 hover:text-white transition-colors p-1"
              aria-label="Закрыть"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>

          <p class="text-gray-400 mb-6 text-sm sm:text-base">
            Мы перезвоним Вам для уточнения деталей
          </p>

          <!-- Поле для телефона -->
          <input
            v-model="bookingPhoneNumber"
            type="tel"
            placeholder="+7 (___) ___-__-__"
            inputmode="numeric"
            maxlength="18"
            class="w-full px-4 py-3 bg-gray-900/50 border border-gray-700 rounded-xl text-white placeholder-gray-500 focus:outline-none focus:border-orange-500 transition-colors mb-6 text-sm sm:text-base"
            @input="handleBookingPhoneInput"
            @keydown="handleBookingPhoneKeydown"
            @keyup.enter="confirmBooking"
          />

          <!-- Кнопки -->
          <div class="flex flex-col sm:flex-row gap-3">
            <button
              @click="cancelBooking"
              class="flex-1 px-4 py-3 border border-gray-700 text-gray-300 rounded-xl hover:border-gray-600 hover:text-white transition-colors text-sm sm:text-base"
            >
              Отмена
            </button>
            <button
              @click="confirmBooking"
              class="flex-1 px-4 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all text-sm sm:text-base"
            >
              Подтвердить
            </button>
          </div>
        </div>
      </div>

      <!-- Диалог успешного бронирования -->
      <div
        v-if="showBookingSuccessDialog"
        class="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-fadeIn"
        @click="closeBookingSuccessDialog"
      >
        <div
          class="bg-gradient-to-br from-gray-800/90 to-gray-900/90 backdrop-blur-xl border border-gray-700/50 rounded-2xl p-6 sm:p-8 w-full max-w-md text-center transform scale-95 animate-scaleIn"
          @click.stop
        >
          <!-- Иконка успеха -->
          <div
            class="w-16 h-16 sm:w-20 sm:h-20 mx-auto mb-4 sm:mb-6 flex items-center justify-center rounded-full bg-gradient-to-r from-green-500/20 to-green-600/20"
          >
            <svg
              class="w-8 h-8 sm:w-10 sm:h-10 text-green-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
          </div>

          <!-- Заголовок -->
          <h3 class="text-xl sm:text-2xl font-bold text-white mb-2">
            Спасибо!
          </h3>
          <p class="text-gray-300 mb-4 sm:mb-6 text-sm sm:text-base">
            Ожидайте, мы скоро перезвоним
          </p>

          <!-- Кнопка -->
          <button
            @click="closeBookingSuccessDialog"
            class="px-6 sm:px-8 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all text-sm sm:text-base"
          >
            Понятно
          </button>
        </div>
      </div>

      <!-- Состояние загрузки -->
      <section v-if="loading" class="py-32 sm:py-40">
        <div class="container mx-auto px-4 text-center">
          <div
            class="inline-block w-12 h-12 sm:w-16 sm:h-16 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-4 sm:mb-6"
          ></div>
          <p class="text-gray-400 text-sm sm:text-base">Загружаем данные...</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Gallery from "@/components/Gallery.vue";
import { mapState, mapActions, mapGetters } from "vuex";
import { bookingApi } from "@/api";
import {
  formatRussianPhone,
  isValidRussianPhone,
  removePhoneDigit,
} from "@/utils/phone";

export default {
  name: "Home",
  components: {
    Gallery,
  },
  data() {
    return {
      hours: [
        { days: "Пн-Чт", time: "12:00-23:00" },
        { days: "Пт-Сб", time: "12:00-00:00" },
        { days: "Вс", time: "12:00-22:00" },
      ],
      banquetItems: [
        {
          icon: "💒",
          title: "Свадебные банкеты",
          description: "Незабываемый день в элегантной обстановке",
        },
        {
          icon: "🏢",
          title: "Корпоративные мероприятия",
          description: "Деловые встречи и корпоративы",
        },
        {
          icon: "🎂",
          title: "Дни рождения",
          description: "Празднование в кругу близких",
        },
        {
          icon: "🍽️",
          title: "Бизнес-ланчи",
          description: "Деловые обеды и переговоры",
        },
      ],
      loading: false,
      cardHovered: [],
      showBookingPhoneDialog: false,
      showBookingSuccessDialog: false,
      bookingPhoneNumber: "",
    };
  },
  computed: {
    ...mapState({
      menuItems: (state) => state.menuItems,
      reviews: (state) => state.reviews,
      galleryImages: (state) => state.galleryImages,
    }),

    // Получаем первые 3 элемента меню для главной страницы
    featuredItems() {
      return this.menuItems.slice(0, 3);
    },

    // Получаем первые 3 отзыва для главной страницы
    featuredReviews() {
      return this.reviews.slice(0, 3);
    },
  },
  async mounted() {
    try {
      this.loading = true;

      // Загружаем данные если они еще не загружены
      if (!this.menuItems || this.menuItems.length === 0) {
        await this.$store.dispatch("fetchMenuItems");
      }
      if (!this.reviews || this.reviews.length === 0) {
        await this.$store.dispatch("fetchReviews");
      }
      if (!this.galleryImages || this.galleryImages.length === 0) {
        await this.$store.dispatch("fetchGalleryImages");
      }
    } catch (error) {
      console.error("Failed to load data:", error);
    } finally {
      this.loading = false;
    }

    // Анимация появления элементов
    setTimeout(() => {
      const elements = document.querySelectorAll(".animate-slideUp");
      elements.forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "translateY(0)";
      });
    }, 100);
  },
  methods: {
    formatDate(dateString) {
      if (!dateString) return "";
      const date = new Date(dateString);
      return date.toLocaleDateString("ru-RU", {
        day: "numeric",
        month: "short",
      });
    },

    // Методы для бронирования стола
    showBookingDialog() {
      this.showBookingPhoneDialog = true;
      this.bookingPhoneNumber = "";
    },

    cancelBooking() {
      this.showBookingPhoneDialog = false;
      this.bookingPhoneNumber = "";
    },

    handleBookingPhoneInput() {
      this.bookingPhoneNumber = formatRussianPhone(this.bookingPhoneNumber);
    },
    handleBookingPhoneKeydown(event) {
      if (event.key !== "Backspace" && event.key !== "Delete") {
        return;
      }

      const input = event.target;
      const cursor = input.selectionStart ?? this.bookingPhoneNumber.length;
      const nextValue = removePhoneDigit(
        this.bookingPhoneNumber,
        cursor,
        event.key === "Delete" ? "forward" : "backward"
      );

      if (nextValue === this.bookingPhoneNumber) {
        return;
      }

      event.preventDefault();
      this.bookingPhoneNumber = nextValue;
      this.$nextTick(() => {
        const nextCursor = Math.min(cursor, this.bookingPhoneNumber.length);
        input.setSelectionRange(nextCursor, nextCursor);
      });
    },

    closeBookingSuccessDialog() {
      this.showBookingSuccessDialog = false;
    },

    validatePhoneNumber(phone) {
      return isValidRussianPhone(phone);
    },

    async confirmBooking() {
      // Проверяем валидность номера телефона
      if (!this.validatePhoneNumber(this.bookingPhoneNumber)) {
        alert("Пожалуйста, введите корректный номер телефона");
        return;
      }

      try {
        const response = await bookingApi.createReservation({
          customer_phone: this.bookingPhoneNumber,
          reservation_type: "table_reservation",
          source: "home",
        });

        this.showBookingPhoneDialog = false;
        this.bookingPhoneNumber = "";
        this.showBookingSuccessDialog = true;
      } catch (error) {
        console.error("Ошибка при бронировании стола:", error);
        alert("Ошибка при отправке запроса. Пожалуйста, попробуйте еще раз.");
      }
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

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-slideUp {
  opacity: 0;
  transform: translateY(20px);
  animation: slideUp 0.6s ease forwards;
}

.animate-fadeIn {
  animation: fadeIn 0.2s ease forwards;
}

.animate-scaleIn {
  animation: scaleIn 0.2s ease forwards;
}

@media (max-width: 640px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  section {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
  }

  .grid {
    gap: 0.75rem !important;
  }

  .p-6 {
    padding: 1rem !important;
  }

  .p-8 {
    padding: 1.25rem !important;
  }

  .space-y-6 > * + * {
    margin-top: 1rem !important;
  }

  .space-y-8 > * + * {
    margin-top: 1.25rem !important;
  }
}

@media (max-width: 480px) {
  .text-3xl {
    font-size: 1.75rem !important;
  }

  .text-4xl {
    font-size: 2rem !important;
  }

  .text-5xl {
    font-size: 2.25rem !important;
  }

  .text-6xl {
    font-size: 2.5rem !important;
  }
}

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

* {
  scrollbar-width: thin;
  scrollbar-color: #f97316 rgba(17, 24, 39, 0.5);
}

::selection {
  background: rgba(249, 115, 22, 0.3);
  color: #ffffff;
}

::-moz-selection {
  background: rgba(249, 115, 22, 0.3);
  color: #ffffff;
}
</style>
