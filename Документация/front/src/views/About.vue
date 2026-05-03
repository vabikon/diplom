<template>
  <div class="min-h-screen">
    <!-- Заголовок страницы -->
    <div class="container mx-auto px-4 mb-8 sm:mb-12 text-center">
      <h1
        class="text-3xl sm:text-4xl md:text-5xl font-bold text-white mb-3 sm:mb-4 animate-slideUp"
      >
        О нас
      </h1>
      <p
        class="text-gray-400 text-base sm:text-lg animate-slideUp"
        style="animation-delay: 0.1s"
      >
        Основано в 2015 году
      </p>
    </div>

    <!-- Статус загрузки галереи -->
    <div
      v-if="galleryLoading"
      class="container mx-auto px-4 text-center py-16 sm:py-20"
    >
      <div
        class="inline-block w-12 h-12 sm:w-16 sm:h-16 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-4 sm:mb-6"
      ></div>
      <p class="text-gray-400 text-sm sm:text-base">Загружаем фотографии...</p>
    </div>

    <!-- Основной контент -->
    <div v-else class="container mx-auto px-4">
      <!-- Hero секция -->
      <section class="max-w-6xl mx-auto mb-16 sm:mb-20">
        <div
          class="text-center space-y-6 sm:space-y-8 animate-slideUp"
          style="animation-delay: 0.2s"
        >
          <div class="max-w-4xl mx-auto">
            <h2
              class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-4 sm:mb-6"
            >
              Мангал Хаус — это философия
            </h2>
            <p
              class="text-gray-300 text-base sm:text-lg leading-relaxed mb-6 sm:mb-8"
            >
              Мы верим, что еда — это больше, чем просто утоление голода. Это
              искусство, наука и эмоция в одной тарелке. С 2015 года мы создаем
              блюда, которые рассказывают истории.
            </p>

            <!-- Статистика -->
            <div class="grid grid-cols-3 gap-4 sm:gap-8 max-w-2xl mx-auto">
              <div class="text-center">
                <div
                  class="text-2xl sm:text-3xl md:text-4xl font-bold bg-gradient-to-r from-orange-500 to-red-500 bg-clip-text text-transparent mb-2"
                >
                  8+
                </div>
                <div class="text-gray-500 text-xs sm:text-sm">лет работы</div>
              </div>
              <div class="text-center">
                <div
                  class="text-2xl sm:text-3xl md:text-4xl font-bold bg-gradient-to-r from-orange-500 to-red-500 bg-clip-text text-transparent mb-2"
                >
                  {{ menuItemsCount }}+
                </div>
                <div class="text-gray-500 text-xs sm:text-sm">блюд в меню</div>
              </div>
              <div class="text-center">
                <div
                  class="text-2xl sm:text-3xl md:text-4xl font-bold bg-gradient-to-r from-orange-500 to-red-500 bg-clip-text text-transparent mb-2"
                >
                  {{ reviewsCount }}+
                </div>
                <div class="text-gray-500 text-xs sm:text-sm">
                  довольных гостей
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Философия -->
      <section class="max-w-6xl mx-auto mb-16 sm:mb-20">
        <div class="text-center mb-8 sm:mb-12">
          <h2
            class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-3 sm:mb-4 animate-slideUp"
          >
            Наша философия
          </h2>
          <p
            class="text-gray-400 text-sm sm:text-base animate-slideUp"
            style="animation-delay: 0.1s"
          >
            Три принципа, которые определяют нас
          </p>
        </div>

        <div
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 sm:gap-6"
        >
          <div
            class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-xl p-6 sm:p-8 text-center hover:border-orange-500/50 transition-all duration-300 transform hover:-translate-y-2 animate-slideUp"
            style="animation-delay: 0.2s"
          >
            <div class="flex justify-center mb-4 sm:mb-6">
              <div
                class="w-12 h-12 sm:w-16 sm:h-16 flex items-center justify-center rounded-xl bg-gradient-to-r from-orange-500/20 to-red-500/20"
              >
                <svg
                  class="w-6 h-6 sm:w-8 sm:h-8 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 8v4"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M8 12h8"
                  />
                </svg>
              </div>
            </div>
            <h3
              class="text-lg sm:text-xl font-semibold text-white mb-3 sm:mb-4"
            >
              Сезонность
            </h3>
            <p class="text-gray-400 leading-relaxed text-sm sm:text-base">
              Работаем только со свежими, сезонными продуктами от локальных
              фермеров.
            </p>
          </div>

          <div
            class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-xl p-6 sm:p-8 text-center hover:border-orange-500/50 transition-all duration-300 transform hover:-translate-y-2 animate-slideUp"
            style="animation-delay: 0.3s"
          >
            <div class="flex justify-center mb-4 sm:mb-6">
              <div
                class="w-12 h-12 sm:w-16 sm:h-16 flex items-center justify-center rounded-xl bg-gradient-to-r from-orange-500/20 to-red-500/20"
              >
                <svg
                  class="w-6 h-6 sm:w-8 sm:h-8 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"
                  />
                </svg>
              </div>
            </div>
            <h3
              class="text-lg sm:text-xl font-semibold text-white mb-3 sm:mb-4"
            >
              Минимализм
            </h3>
            <p class="text-gray-400 leading-relaxed text-sm sm:text-base">
              Каждое блюдо — баланс вкусов и текстур. Ничего лишнего, только
              суть.
            </p>
          </div>

          <div
            class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-xl p-6 sm:p-8 text-center hover:border-orange-500/50 transition-all duration-300 transform hover:-translate-y-2 animate-slideUp sm:col-span-2 md:col-span-1"
            style="animation-delay: 0.4s"
          >
            <div class="flex justify-center mb-4 sm:mb-6">
              <div
                class="w-12 h-12 sm:w-16 sm:h-16 flex items-center justify-center rounded-xl bg-gradient-to-r from-orange-500/20 to-red-500/20"
              >
                <svg
                  class="w-6 h-6 sm:w-8 sm:h-8 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 2c1 3 3.97 5 7 5-3.97 2.97-5 5.97-5 9-1.03 0-2.03-.97-3-3-1.03 3-2.03 3-3 3-3.97 0-6.97-2.97-7-5 3.03 0 6-2 7-5-1-3-1-6 0-9z"
                  />
                </svg>
              </div>
            </div>
            <h3
              class="text-lg sm:text-xl font-semibold text-white mb-3 sm:mb-4"
            >
              Традиции
            </h3>
            <p class="text-gray-400 leading-relaxed text-sm sm:text-base">
              Уважаем классические рецепты, но не боимся экспериментировать.
            </p>
          </div>
        </div>
      </section>

      <!-- Команда -->
      <section class="max-w-6xl mx-auto mb-16 sm:mb-20">
        <div class="text-center mb-8 sm:mb-12">
          <h2
            class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-3 sm:mb-4 animate-slideUp"
          >
            Команда
          </h2>
          <p
            class="text-gray-400 text-sm sm:text-base animate-slideUp"
            style="animation-delay: 0.1s"
          >
            Те, кто создает магию
          </p>
        </div>

        <div
          class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8 max-w-4xl mx-auto"
        >
          <div
            class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-xl p-6 sm:p-8 hover:border-orange-500/50 transition-all duration-300 animate-slideUp"
            style="animation-delay: 0.2s"
          >
            <div
              class="flex flex-col sm:flex-row gap-4 sm:gap-6 items-center sm:items-start"
            >
              <div
                class="w-20 h-20 sm:w-28 sm:h-28 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-full flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="w-8 h-8 sm:w-12 sm:h-12 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"
                  />
                  <circle cx="12" cy="7" r="4" />
                </svg>
              </div>
              <div class="text-center sm:text-left">
                <h3 class="text-lg sm:text-xl font-semibold text-white mb-1">
                  Александр Иванов
                </h3>
                <p
                  class="text-orange-400 font-medium mb-2 sm:mb-3 text-sm sm:text-base"
                >
                  Шеф-повар
                </p>
                <p class="text-gray-400 leading-relaxed text-sm sm:text-base">
                  15 лет в гастрономии. Работал в лучших ресторанах Европы.
                  Создатель концепции минималистичной кухни.
                </p>
              </div>
            </div>
          </div>

          <div
            class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-xl p-6 sm:p-8 hover:border-orange-500/50 transition-all duration-300 animate-slideUp"
            style="animation-delay: 0.3s"
          >
            <div
              class="flex flex-col sm:flex-row gap-4 sm:gap-6 items-center sm:items-start"
            >
              <div
                class="w-20 h-20 sm:w-28 sm:h-28 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-full flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="w-8 h-8 sm:w-12 sm:h-12 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"
                  />
                  <circle cx="12" cy="7" r="4" />
                </svg>
              </div>
              <div class="text-center sm:text-left">
                <h3 class="text-lg sm:text-xl font-semibold text-white mb-1">
                  Мария Петрова
                </h3>
                <p
                  class="text-orange-400 font-medium mb-2 sm:mb-3 text-sm sm:text-base"
                >
                  Шеф-кондитер
                </p>
                <p class="text-gray-400 leading-relaxed text-sm sm:text-base">
                  Мастер французской кондитерской школы. Ее десерты — это баланс
                  сладости и изысканности.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Галерея -->
      <section class="max-w-6xl mx-auto mb-16 sm:mb-20">
        <div class="text-center mb-8 sm:mb-12">
          <h2
            class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-3 sm:mb-4 animate-slideUp"
          >
            Галерея
          </h2>
          <p
            class="text-gray-400 text-sm sm:text-base animate-slideUp"
            style="animation-delay: 0.1s"
          >
            Наша атмосфера в фотографиях
          </p>
        </div>

        <Gallery
          :images="galleryImages"
          :loading="galleryLoading"
          @load-more="loadMoreGallery"
        />
      </section>

      <!-- Контакты -->
      <section class="max-w-4xl mx-auto">
        <div class="text-center mb-8 sm:mb-12">
          <h2
            class="text-2xl sm:text-3xl md:text-4xl font-bold text-white mb-3 sm:mb-4 animate-slideUp"
          >
            Контакты
          </h2>
          <p
            class="text-gray-400 text-sm sm:text-base animate-slideUp"
            style="animation-delay: 0.1s"
          >
            Свяжитесь с нами
          </p>
        </div>

        <!-- Контактная информация -->
        <div
          class="bg-gradient-to-br from-gray-800/70 to-gray-900/70 backdrop-blur-xl border border-gray-700/50 rounded-xl p-6 sm:p-8 animate-slideUp"
          style="animation-delay: 0.2s"
        >
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 sm:gap-8">
            <!-- Адрес -->
            <div class="flex gap-4">
              <div
                class="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-lg flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="w-5 h-5 sm:w-6 sm:h-6 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"
                  />
                  <circle cx="12" cy="10" r="3" />
                </svg>
              </div>
              <div>
                <p class="text-gray-500 text-xs sm:text-sm mb-1">Адрес</p>
                <p class="text-white font-medium text-sm sm:text-base">
                  Москва, ул. Ресторанная, 15
                </p>
                <p class="text-gray-400 text-xs sm:text-sm mt-1">
                  Метро: Охотный ряд (5 мин пешком)
                </p>
              </div>
            </div>

            <!-- Телефон -->
            <div class="flex gap-4">
              <div
                class="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-lg flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="w-5 h-5 sm:w-6 sm:h-6 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0116.92 22z"
                  />
                </svg>
              </div>
              <div>
                <p class="text-gray-500 text-xs sm:text-sm mb-1">Телефон</p>
                <a
                  href="tel:+74951234567"
                  class="text-white font-medium hover:text-orange-400 transition-colors text-sm sm:text-base"
                >
                  +7 (495) 123-45-67
                </a>
                <p class="text-gray-400 text-xs sm:text-sm mt-1">
                  Ежедневно с 12:00 до 23:00
                </p>
              </div>
            </div>

            <!-- Email -->
            <div class="flex gap-4">
              <div
                class="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-lg flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="w-5 h-5 sm:w-6 sm:h-6 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M22 6l-10 7L2 6"
                  />
                </svg>
              </div>
              <div>
                <p class="text-gray-500 text-xs sm:text-sm mb-1">Email</p>
                <a
                  href="mailto:info@mangalhouse.ru"
                  class="text-white font-medium hover:text-orange-400 transition-colors text-sm sm:text-base"
                >
                  info@mangalhouse.ru
                </a>
                <p class="text-gray-400 text-xs sm:text-sm mt-1">
                  Бронирование и вопросы
                </p>
              </div>
            </div>

            <!-- Часы работы -->
            <div class="flex gap-4">
              <div
                class="w-10 h-10 sm:w-12 sm:h-12 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-lg flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="w-5 h-5 sm:w-6 sm:h-6 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <circle cx="12" cy="12" r="10" />
                  <polyline points="12,6 12,12 16,14" />
                </svg>
              </div>
              <div>
                <p class="text-gray-500 text-xs sm:text-sm mb-1">Часы работы</p>
                <p class="text-white font-medium text-sm sm:text-base">
                  Пн-Вс: 12:00-23:00
                </p>
                <p class="text-gray-400 text-xs sm:text-sm mt-1">
                  Парковка: есть
                </p>
              </div>
            </div>
          </div>

          <!-- Кнопка бронирования -->
          <div
            class="mt-6 sm:mt-8 pt-6 sm:pt-8 border-t border-gray-700/30 text-center"
          >
            <button
              @click="showBookingDialog"
              class="w-full sm:w-auto px-6 sm:px-8 py-3 sm:py-4 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-xl hover:shadow-orange-500/25 transition-all duration-300 transform hover:-translate-y-1 inline-flex items-center justify-center gap-3"
            >
              <span>Забронировать стол</span>
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
                  d="M17 8l4 4m0 0l-4 4m4-4H3"
                />
              </svg>
            </button>
          </div>
        </div>
      </section>
    </div>

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
        <h3 class="text-xl sm:text-2xl font-bold text-white mb-2">Спасибо!</h3>
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
  </div>
</template>

<script>
import Gallery from "@/components/Gallery.vue";
import {
  formatRussianPhone,
  isValidRussianPhone,
  removePhoneDigit,
} from "@/utils/phone";

export default {
  name: "About",
  components: {
    Gallery,
  },
  data() {
    return {
      galleryImages: [],
      galleryLoading: true,
      showBookingPhoneDialog: false,
      showBookingSuccessDialog: false,
      bookingPhoneNumber: "",
      menuItemsCount: 50,
      reviewsCount: 1000,
    };
  },
  mounted() {
    this.loadGalleryImages();
  },
  methods: {
    async loadGalleryImages() {
      try {
        this.galleryLoading = true;
        // Симуляция загрузки галереи
        await new Promise((resolve) => setTimeout(resolve, 1000));

        this.galleryImages = [
          {
            id: 1,
            url: "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&h=600&fit=crop",
            alt: "Интерьер ресторана",
            category: "interior",
          },
          {
            id: 2,
            url: "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&h=600&fit=crop",
            alt: "Блюдо от шефа",
            category: "food",
          },
          {
            id: 3,
            url: "https://images.unsplash.com/photo-1551218808-94e220e084d2?w=800&h=600&fit=crop",
            alt: "Кухня ресторана",
            category: "kitchen",
          },
          {
            id: 4,
            url: "https://images.unsplash.com/photo-1559329007-40df8a9345d8?w=800&h=600&fit=crop",
            alt: "Атмосфера вечером",
            category: "atmosphere",
          },
          {
            id: 5,
            url: "https://images.unsplash.com/photo-1578474846511-04ba529f0b88?w=800&h=600&fit=crop",
            alt: "Барная зона",
            category: "bar",
          },
          {
            id: 6,
            url: "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&h=600&fit=crop",
            alt: "Команда поваров",
            category: "team",
          },
        ];
      } catch (error) {
        console.error("Ошибка загрузки галереи:", error);
      } finally {
        this.galleryLoading = false;
      }
    },

    loadMoreGallery() {
      // Логика для загрузки дополнительных изображений
      console.log("Загрузка дополнительных изображений галереи");
    },

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

    async confirmBooking() {
      if (!isValidRussianPhone(this.bookingPhoneNumber)) {
        alert("Пожалуйста, введите корректный номер телефона");
        return;
      }

      try {
        // Здесь будет логика отправки заявки на бронирование
        console.log("Бронирование:", this.bookingPhoneNumber);

        this.showBookingPhoneDialog = false;
        this.showBookingSuccessDialog = true;
        this.bookingPhoneNumber = "";
      } catch (error) {
        console.error("Ошибка бронирования:", error);
        alert("Произошла ошибка. Попробуйте позже.");
      }
    },

    closeBookingSuccessDialog() {
      this.showBookingSuccessDialog = false;
    },
  },
};
</script>

<style scoped>
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
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
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-slideUp {
  animation: slideUp 0.6s ease forwards;
  opacity: 0;
}

.animate-fadeIn {
  animation: fadeIn 0.3s ease forwards;
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

/* Улучшение выделения текста */
::selection {
  background: rgba(249, 115, 22, 0.3);
  color: #ffffff;
}

::-moz-selection {
  background: rgba(249, 115, 22, 0.3);
  color: #ffffff;
}
</style>
