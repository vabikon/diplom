<template>
  <footer
    class="relative bg-gradient-to-b from-gray-900 to-black pt-12 sm:pt-16 pb-6 sm:pb-8 overflow-hidden"
  >
    <!-- Огненные акценты -->
    <div
      class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-orange-500 to-transparent animate-pulse"
    ></div>

    <!-- Парящие искры -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div
        v-for="i in 8"
        :key="i"
        class="absolute w-2 h-2 bg-gradient-to-b from-yellow-400 to-orange-500 rounded-full animate-float"
        :style="`left: ${10 + i * 10}%; animation-delay: ${i * 0.3}s; top: ${
          Math.random() * 30
        }%`"
      ></div>
    </div>

    <div class="container mx-auto px-4 relative z-10">
      <!-- Мобильная версия -->
      <div class="block lg:hidden space-y-8 mb-8">
        <!-- Бренд для мобильных -->
        <div class="text-center space-y-4">
          <span
            class="text-xl sm:text-2xl font-bold bg-gradient-to-r from-orange-500 to-yellow-500 bg-clip-text text-transparent"
          >
            Гастрономия
          </span>
          <p class="text-gray-400 text-sm leading-relaxed max-w-sm mx-auto">
            Место, где рождается настоящий вкус огня. Авторские рецепты и
            традиции мангала в современном исполнении.
          </p>
        </div>

        <!-- Контакты для мобильных -->
        <div class="space-y-4">
          <h3
            class="text-lg font-bold text-white text-center mb-4 flex items-center justify-center space-x-2"
          >
            <svg
              class="w-5 h-5 text-orange-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
              />
            </svg>
            <span>Контакты</span>
          </h3>

          <div class="grid grid-cols-1 gap-3">
            <!-- Адрес -->
            <div
              class="flex items-center space-x-3 p-3 rounded-xl bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-gray-700/30"
            >
              <div
                class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-br from-orange-500/20 to-red-500/20 flex-shrink-0"
              >
                <svg
                  class="w-4 h-4 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
              </div>
              <div class="min-w-0 flex-1">
                <p class="text-white font-medium text-sm">
                  Ростов-на-Дону, Ченцова 95м
                </p>
                <p class="text-gray-400 text-xs">Ростов-на-Дону, Россия</p>
              </div>
            </div>

            <!-- Телефон -->
            <div
              class="flex items-center space-x-3 p-3 rounded-xl bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-gray-700/30"
            >
              <div
                class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-br from-orange-500/20 to-red-500/20 flex-shrink-0"
              >
                <svg
                  class="w-4 h-4 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                  />
                </svg>
              </div>
              <div class="min-w-0 flex-1">
                <a
                  href="tel:+74951234567"
                  class="text-white font-medium hover:text-orange-400 transition-colors text-sm"
                >
                  +7 (495) 123-45-67
                </a>
                <p class="text-gray-400 text-xs">Ежедневно с 12:00 до 00:00</p>
              </div>
            </div>

            <!-- Email -->
            <div
              class="flex items-center space-x-3 p-3 rounded-xl bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-gray-700/30"
            >
              <div
                class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-br from-orange-500/20 to-red-500/20 flex-shrink-0"
              >
                <svg
                  class="w-4 h-4 text-orange-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                  />
                </svg>
              </div>
              <div class="min-w-0 flex-1">
                <a
                  href="mailto:info@mangalhouse.ru"
                  class="text-white font-medium hover:text-orange-400 transition-colors text-sm"
                >
                  info@mangalhouse.ru
                </a>
                <p class="text-gray-400 text-xs">Бронирование и вопросы</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Навигация для мобильных -->
        <div class="space-y-4">
          <h3
            class="text-lg font-bold text-white text-center mb-4 flex items-center justify-center space-x-2"
          >
            <svg
              class="w-5 h-5 text-orange-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"
              />
            </svg>
            <span>Навигация</span>
          </h3>

          <div class="grid grid-cols-2 gap-2">
            <router-link
              v-for="link in quickLinks"
              :key="link.to"
              :to="link.to"
              class="flex items-center space-x-2 p-3 rounded-xl text-gray-300 hover:text-white hover:bg-gradient-to-r from-gray-800/50 to-gray-900/50 transition-all duration-300 group border border-transparent hover:border-orange-500/20"
            >
              <!-- Иконка Главная -->
              <svg
                v-if="link.to === '/'"
                class="w-4 h-4 text-gray-400 group-hover:text-orange-400 flex-shrink-0"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>

              <!-- Иконка Меню -->
              <svg
                v-else-if="link.to === '/menu'"
                class="w-4 h-4 text-gray-400 group-hover:text-orange-400 flex-shrink-0"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                />
              </svg>

              <!-- Иконка О нас -->
              <svg
                v-else-if="link.to === '/about'"
                class="w-4 h-4 text-gray-400 group-hover:text-orange-400 flex-shrink-0"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>

              <!-- Иконка Отзывы -->
              <svg
                v-else-if="link.to === '/reviews'"
                class="w-4 h-4 text-gray-400 group-hover:text-orange-400 flex-shrink-0"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
                />
              </svg>

              <span class="font-medium text-sm">{{ link.text }}</span>
            </router-link>
          </div>
        </div>

        <!-- Соцсети для мобильных -->
        <div class="flex justify-center space-x-4">
          <a
            v-for="social in socialLinks"
            :key="social.name"
            :href="social.url"
            class="w-10 h-10 flex items-center justify-center rounded-xl bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 hover:border-orange-500/50 transition-all duration-300 group hover:scale-110"
            target="_blank"
            :aria-label="social.name"
          >
            <!-- Иконка Telegram -->
            <svg
              v-if="social.name === 'Telegram'"
              class="w-5 h-5 text-gray-400 group-hover:text-orange-400 transition-colors"
              fill="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"
              />
            </svg>

            <!-- Иконка VK -->
            <svg
              v-else-if="social.name === 'VK'"
              class="w-5 h-5 text-gray-400 group-hover:text-orange-400 transition-colors"
              fill="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                d="M15.684 0H8.316C1.592 0 0 1.592 0 8.316v7.368C0 22.408 1.592 24 8.316 24h7.368C22.408 24 24 22.408 24 15.684V8.316C24 1.592 22.408 0 15.684 0zm3.692 17.123h-1.744c-.66 0-.864-.525-2.05-1.727-1.033-1.01-1.49-.9-1.744-.9-.356 0-.458.102-.458.593v1.575c0 .424-.135.678-1.253.678-1.846 0-3.896-1.118-5.335-3.202C4.624 10.857 4.03 8.57 4.03 8.096c0-.254.102-.491.593-.491h1.744c.441 0 .61.203.78.678.863 2.49 2.303 4.675 2.896 4.675.22 0 .322-.102.322-.66V9.721c-.068-1.186-.695-1.287-.695-1.71 0-.204.169-.407.441-.407h2.744c.373 0 .508.203.508.643v3.473c0 .372.169.508.271.508.22 0 .407-.136.813-.542 1.254-1.406 2.151-3.574 2.151-3.574.119-.254.322-.491.763-.491h1.744c.525 0 .644.271.525.643-.22 1.017-2.354 4.031-2.354 4.031-.186.305-.254.44 0 .78.186.254.796.779 1.203 1.253.745.847 1.32 1.558 1.473 2.05.17.49-.085.744-.576.744z"
              />
            </svg>
          </a>
        </div>
      </div>

      <!-- Десктопная версия -->
      <div class="hidden lg:grid lg:grid-cols-4 gap-8 mb-12">
        <!-- Бренд -->
        <div class="space-y-4">
          <div class="flex items-center space-x-3">
            <span
              class="text-2xl font-bold bg-gradient-to-r from-orange-500 to-yellow-500 bg-clip-text text-transparent"
            >
              Гастрономия
            </span>
          </div>

          <p class="text-gray-400 text-sm leading-relaxed">
            Место, где рождается настоящий вкус огня. Авторские рецепты и
            традиции мангала в современном исполнении.
          </p>

          <!-- Соцсети -->
          <div class="flex space-x-3 pt-4">
            <a
              v-for="social in socialLinks"
              :key="social.name"
              :href="social.url"
              class="w-10 h-10 flex items-center justify-center rounded-xl bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 hover:border-orange-500/50 transition-all duration-300 group hover:scale-110"
              target="_blank"
              :aria-label="social.name"
            >
              <!-- Иконка Telegram -->
              <svg
                v-if="social.name === 'Telegram'"
                class="w-5 h-5 text-gray-400 group-hover:text-orange-400 transition-colors"
                fill="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"
                />
              </svg>

              <!-- Иконка VK -->
              <svg
                v-else-if="social.name === 'VK'"
                class="w-5 h-5 text-gray-400 group-hover:text-orange-400 transition-colors"
                fill="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  d="M15.684 0H8.316C1.592 0 0 1.592 0 8.316v7.368C0 22.408 1.592 24 8.316 24h7.368C22.408 24 24 22.408 24 15.684V8.316C24 1.592 22.408 0 15.684 0zm3.692 17.123h-1.744c-.66 0-.864-.525-2.05-1.727-1.033-1.01-1.49-.9-1.744-.9-.356 0-.458.102-.458.593v1.575c0 .424-.135.678-1.253.678-1.846 0-3.896-1.118-5.335-3.202C4.624 10.857 4.03 8.57 4.03 8.096c0-.254.102-.491.593-.491h1.744c.441 0 .61.203.78.678.863 2.49 2.303 4.675 2.896 4.675.22 0 .322-.102.322-.66V9.721c-.068-1.186-.695-1.287-.695-1.71 0-.204.169-.407.441-.407h2.744c.373 0 .508.203.508.643v3.473c0 .372.169.508.271.508.22 0 .407-.136.813-.542 1.254-1.406 2.151-3.574 2.151-3.574.119-.254.322-.491.763-.491h1.744c.525 0 .644.271.525.643-.22 1.017-2.354 4.031-2.354 4.031-.186.305-.254.44 0 .78.186.254.796.779 1.203 1.253.745.847 1.32 1.558 1.473 2.05.17.49-.085.744-.576.744z"
                />
              </svg>
            </a>
          </div>
        </div>

        <!-- Контакты -->
        <div class="space-y-4">
          <h3
            class="text-xl font-bold text-white mb-4 flex items-center space-x-2"
          >
            <svg
              class="w-5 h-5 text-orange-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
              />
            </svg>
            <span>Контакты</span>
          </h3>

          <div class="space-y-3">
            <div class="flex items-start space-x-3 group">
              <div
                class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 group-hover:border-orange-500/30 transition-colors"
              >
                <svg
                  class="w-4 h-4 text-gray-400 group-hover:text-orange-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
              </div>
              <div>
                <p class="text-white font-medium">
                  Ростов-на-Дону, Ченцова 95м
                </p>
                <p class="text-gray-400 text-sm">Ростов-на-Дону, Россия</p>
              </div>
            </div>

            <div class="flex items-start space-x-3 group">
              <div
                class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 group-hover:border-orange-500/30 transition-colors"
              >
                <svg
                  class="w-4 h-4 text-gray-400 group-hover:text-orange-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                  />
                </svg>
              </div>
              <div>
                <a
                  href="tel:+74951234567"
                  class="text-white font-medium hover:text-orange-400 transition-colors"
                >
                  +7 (495) 123-45-67
                </a>
                <p class="text-gray-400 text-sm">Ежедневно с 12:00 до 00:00</p>
              </div>
            </div>

            <div class="flex items-start space-x-3 group">
              <div
                class="w-8 h-8 flex items-center justify-center rounded-lg bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 group-hover:border-orange-500/30 transition-colors"
              >
                <svg
                  class="w-4 h-4 text-gray-400 group-hover:text-orange-400"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                  />
                </svg>
              </div>
              <div>
                <a
                  href="mailto:info@mangalhouse.ru"
                  class="text-white font-medium hover:text-orange-400 transition-colors"
                >
                  info@mangalhouse.ru
                </a>
                <p class="text-gray-400 text-sm">Бронирование и вопросы</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Часы работы -->
        <div class="space-y-4">
          <h3
            class="text-xl font-bold text-white mb-4 flex items-center space-x-2"
          >
            <svg
              class="w-5 h-5 text-orange-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <circle cx="12" cy="12" r="10" />
              <polyline points="12,6 12,12 16,14" />
            </svg>
            <span>Часы работы</span>
          </h3>

          <div class="space-y-3">
            <div
              v-for="slot in workingHours"
              :key="slot.days"
              class="flex justify-between items-center p-3 rounded-xl bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-gray-700/30 hover:border-orange-500/20 transition-colors group"
            >
              <div>
                <p class="text-white font-medium">{{ slot.days }}</p>
                <p class="text-gray-400 text-sm">{{ slot.hours }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Быстрые ссылки -->
        <div class="space-y-4">
          <h3
            class="text-xl font-bold text-white mb-4 flex items-center space-x-2"
          >
            <svg
              class="w-5 h-5 text-orange-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"
              />
            </svg>
            <span>Навигация</span>
          </h3>

          <div class="space-y-2">
            <router-link
              v-for="link in quickLinks"
              :key="link.to"
              :to="link.to"
              class="flex items-center space-x-3 p-3 rounded-xl text-gray-300 hover:text-white hover:bg-gradient-to-r from-gray-800/50 to-gray-900/50 transition-all duration-300 group border border-transparent hover:border-orange-500/20"
            >
              <!-- Иконка Главная -->
              <svg
                v-if="link.to === '/'"
                class="w-5 h-5 text-gray-400 group-hover:text-orange-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                />
              </svg>

              <!-- Иконка Меню -->
              <svg
                v-else-if="link.to === '/menu'"
                class="w-5 h-5 text-gray-400 group-hover:text-orange-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                />
              </svg>

              <!-- Иконка О нас -->
              <svg
                v-else-if="link.to === '/about'"
                class="w-5 h-5 text-gray-400 group-hover:text-orange-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>

              <!-- Иконка Отзывы -->
              <svg
                v-else-if="link.to === '/reviews'"
                class="w-5 h-5 text-gray-400 group-hover:text-orange-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
                />
              </svg>

              <span class="font-medium">{{ link.text }}</span>
              <svg
                class="ml-auto w-4 h-4 text-gray-500 group-hover:text-orange-400 transform group-hover:translate-x-1 transition-transform"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </router-link>
          </div>
        </div>
      </div>

      <!-- Разделитель -->
      <div class="relative my-6 sm:my-8">
        <div class="absolute inset-0 flex items-center">
          <div class="w-full border-t border-gray-800"></div>
        </div>
        <div class="relative flex justify-center">
          <div class="px-4 bg-gradient-to-b from-gray-900 to-black"></div>
        </div>
      </div>

      <!-- Нижняя часть -->
      <div
        class="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0"
      >
        <!-- Копирайт -->
        <div class="text-center md:text-left">
          <p class="text-gray-400 text-sm">
            © 2015-{{ currentYear }} Гастрономия. Все права защищены.
          </p>
          <p class="text-gray-500 text-xs mt-1">
            Традиции огня в современном исполнении
          </p>
        </div>

        <!-- Юридические ссылки -->
        <div class="flex flex-wrap justify-center gap-4">
          <router-link
            to="/privacy"
            class="text-gray-500 hover:text-orange-400 text-sm transition-colors"
          >
            Политика конфиденциальности
          </router-link>
          <router-link
            to="/terms"
            class="text-gray-500 hover:text-orange-400 text-sm transition-colors"
          >
            Условия использования
          </router-link>
        </div>
      </div>
    </div>

    <!-- Кнопка наверх -->
    <button
      @click="scrollToTop"
      class="fixed bottom-6 right-6 sm:bottom-8 sm:right-8 w-10 h-10 sm:w-12 sm:h-12 flex items-center justify-center rounded-full bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700/50 hover:border-orange-500/50 transition-all duration-300 shadow-2xl hover:scale-110 group z-50"
      aria-label="Наверх"
    >
      <svg
        class="w-5 h-5 sm:w-6 sm:h-6 text-gray-400 group-hover:text-orange-400 transform group-hover:-translate-y-1 transition-all"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M5 10l7-7m0 0l7 7m-7-7v18"
        />
      </svg>
      <div
        class="absolute inset-0 rounded-full bg-gradient-to-r from-orange-500/0 via-orange-500/5 to-orange-500/0 opacity-0 group-hover:opacity-100 transition-opacity"
      ></div>
    </button>
  </footer>
</template>

<script>
export default {
  name: "AppFooter",
  data() {
    return {
      currentYear: new Date().getFullYear(),
      socialLinks: [
        { name: "Telegram", url: "#" },
        { name: "VK", url: "#" },
      ],
      quickLinks: [
        { to: "/", text: "Главная" },
        { to: "/menu", text: "Меню" },
        { to: "/about", text: "О нас" },
        { to: "/reviews", text: "Отзывы" },
      ],
      workingHours: [
        { days: "Пн-Чт", hours: "12:00 -23:00", open: true },
        { days: "Пт-Сб", hours: "12:00 - 02:00", open: true },
        { days: "Воскресенье", hours: "12:00 - 22:00", open: false },
      ],
    };
  },
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
  },
};
</script>

<style scoped>
@keyframes float {
  0%,
  100% {
    transform: translateY(0) rotate(0deg);
    opacity: 0.5;
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
    opacity: 1;
  }
}

.animate-float {
  animation: float 4s ease-in-out infinite;
  filter: blur(0.5px);
}

@media (max-width: 640px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .space-y-8 > * + * {
    margin-top: 1.5rem !important;
  }

  .space-y-4 > * + * {
    margin-top: 1rem !important;
  }

  .space-y-3 > * + * {
    margin-top: 0.75rem !important;
  }

  .p-3 {
    padding: 0.75rem !important;
  }

  .text-xl {
    font-size: 1.125rem !important;
  }

  .text-2xl {
    font-size: 1.25rem !important;
  }
}

@media (max-width: 480px) {
  .grid-cols-2 {
    grid-template-columns: repeat(1, minmax(0, 1fr)) !important;
  }

  .text-lg {
    font-size: 1rem !important;
  }

  .space-x-4 > * + * {
    margin-left: 0.75rem !important;
  }

  .space-x-3 > * + * {
    margin-left: 0.5rem !important;
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
