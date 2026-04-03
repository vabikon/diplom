<template>
  <div class="space-y-6">
    <!-- Шапка с кнопкой добавления -->
    <div
      class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4"
    >
      <h2 class="text-2xl font-bold text-white">Управление меню</h2>
      <button
        @click="showAddForm = true"
        class="px-6 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300 transform hover:scale-105 flex items-center gap-2"
      >
        <svg
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
        >
          <line x1="12" y1="5" x2="12" y2="19" />
          <line x1="5" y1="12" x2="19" y2="12" />
        </svg>
        <span>Добавить блюдо</span>
      </button>
    </div>

    <!-- Форма добавления/редактирования -->
    <div
      v-if="showAddForm"
      class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl p-6"
    >
      <h3 class="text-xl font-semibold text-white mb-6">
        {{ editingItem ? "Редактировать блюдо" : "Добавить новое блюдо" }}
      </h3>

      <form @submit.prevent="saveItem" class="space-y-4">
        <!-- Первая строка -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-gray-400 text-sm mb-2" for="itemName">
              Название
            </label>
            <input
              id="itemName"
              v-model="form.name"
              type="text"
              required
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>

          <div>
            <label class="block text-gray-400 text-sm mb-2" for="itemPrice">
              Цена (₽)
            </label>
            <input
              id="itemPrice"
              v-model.number="form.price"
              type="number"
              required
              min="0"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>
        </div>

        <!-- Вторая строка -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-gray-400 text-sm mb-2" for="itemWeight">
              Вес (г)
            </label>
            <input
              id="itemWeight"
              v-model.number="form.weight"
              type="number"
              required
              min="0"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>

          <div>
            <label class="block text-gray-400 text-sm mb-2" for="itemCategory">
              Категория
            </label>
            <select
              id="itemCategory"
              v-model="form.category"
              required
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white focus:outline-none focus:border-orange-500 transition-colors"
            >
              <option value="appetizers">Закуски</option>
              <option value="main">Основные</option>
              <option value="desserts">Десерты</option>
              <option value="drinks">Напитки</option>
            </select>
          </div>
        </div>

        <!-- Описание -->
        <div>
          <label class="block text-gray-400 text-sm mb-2" for="itemDescription">
            Описание
          </label>
          <textarea
            id="itemDescription"
            v-model="form.description"
            rows="3"
            class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors resize-none"
          ></textarea>
        </div>

        <!-- Состав -->
        <div>
          <label class="block text-gray-400 text-sm mb-2" for="itemComposition">
            Состав
          </label>
          <textarea
            id="itemComposition"
            v-model="form.composition"
            rows="3"
            class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors resize-none"
          ></textarea>
        </div>

        <!-- Изображение -->
        <div>
          <label class="block text-gray-400 text-sm mb-2" for="itemImage">
            Изображение (URL)
          </label>
          <div class="flex gap-2">
            <input
              id="itemImage"
              v-model="form.image"
              type="text"
              class="flex-1 px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
              placeholder="https://example.com/image.jpg"
            />
            <button
              type="button"
              @click="browseImageFile"
              class="px-4 py-3 bg-gray-900 border border-gray-700 text-white rounded-xl hover:border-orange-500 transition-colors"
            >
              Выбрать файл
            </button>
          </div>

          <!-- Превью изображения -->
          <div v-if="form.image" class="mt-3">
            <p class="text-gray-400 text-sm mb-2">Превью изображения:</p>
            <img
              :src="form.image"
              :alt="form.name || 'Превью блюда'"
              class="w-32 h-32 object-cover rounded-lg border border-gray-700"
              @error="handleImagePreviewError"
            />
          </div>

          <!-- Скрытое поле для выбора файла -->
          <input
            type="file"
            ref="imageFileInput"
            @change="handleImageFileChange"
            accept="image/*"
            class="hidden"
          />
        </div>

        <!-- Чекбокс -->
        <div class="flex items-center gap-3">
          <input
            id="itemFeatured"
            type="checkbox"
            v-model="form.featured"
            class="w-5 h-5 bg-gray-900 border-gray-700 rounded focus:ring-2 focus:ring-orange-500"
          />
          <label for="itemFeatured" class="text-gray-300 cursor-pointer">
            Рекомендуемое блюдо
          </label>
        </div>

        <!-- Кнопки -->
        <div class="flex gap-3 pt-4">
          <button
            type="submit"
            class="px-6 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300"
          >
            {{ editingItem ? "Сохранить изменения" : "Добавить блюдо" }}
          </button>
          <button
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
      <p class="text-gray-400">Загружаем меню...</p>
    </div>

    <!-- Ошибка -->
    <div v-else-if="error" class="text-center py-20">
      <p class="text-red-400">Ошибка: {{ error }}</p>
    </div>

    <!-- Таблица меню -->
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
                Изображение
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Название
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Категория
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Цена
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Вес
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Рекомендуемое
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
              v-for="item in menuItems"
              :key="item.id"
              class="hover:bg-gray-800/50 transition-colors"
            >
              <td class="px-4 py-3">
                <img
                  :src="item.image || placeholderImage"
                  :alt="item.name"
                  @error="handleImageError"
                  class="w-16 h-16 object-cover rounded-lg"
                />
              </td>
              <td class="px-4 py-3 text-white font-medium">{{ item.name }}</td>
              <td class="px-4 py-3 text-gray-300">
                {{ getCategoryName(item.category) }}
              </td>
              <td class="px-4 py-3 text-orange-400 font-semibold">
                {{ formatPrice(item.price) }} ₽
              </td>
              <td class="px-4 py-3 text-gray-300">{{ item.weight }} г</td>
              <td class="px-4 py-3">
                <span
                  v-if="item.featured"
                  class="px-2 py-1 bg-orange-500/20 text-orange-400 text-xs font-medium rounded-lg"
                >
                  Да
                </span>
                <span v-else class="text-gray-500 text-xs">Нет</span>
              </td>
              <td class="px-4 py-3">
                <div class="flex gap-2">
                  <button
                    @click="editItem(item)"
                    class="px-3 py-1.5 bg-gray-900 border border-gray-700 text-gray-300 text-sm rounded-lg hover:border-orange-500 hover:text-orange-400 transition-all"
                  >
                    Редактировать
                  </button>
                  <button
                    @click="deleteItem(item.id)"
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
import { menuApi, imageApi } from "@/api";

export default {
  name: "MenuManager",
  data() {
    return {
      loading: false,
      error: null,
      menuItems: [],
      showAddForm: false,
      editingItem: null,
      form: {
        name: "",
        price: 0,
        weight: 0,
        category: "main",
        description: "",
        composition: "",
        image: "",
        featured: false,
      },
      placeholderImage:
        "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjZjVmNWY1Ii8+PHRleHQgeD0iMjAwIiB5PSIxNTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+R2FzdHJvbm9taWE8L3RleHQ+PC9zdmc+",
    };
  },
  async mounted() {
    await this.loadMenuItems();
  },
  methods: {
    async loadMenuItems() {
      try {
        this.loading = true;
        this.error = null;
        const response = await menuApi.getAll();

        // Обработка изображений при загрузке
        this.menuItems = response.data.map(item => {
          if (item.image) {
            // Проверяем, является ли изображение уже полным URL или требует корректировки
            if (!item.image.startsWith('http') && !item.image.startsWith('/')) {
              // Если URL не начинается с http/https или / - возможно это относительный путь
              item.image = item.image;
            }
          }
          return item;
        });
      } catch (error) {
        this.error = error.message || "Ошибка загрузки меню";
        console.error("Ошибка загрузки меню:", error);
      } finally {
        this.loading = false;
      }
    },

    editItem(item) {
      this.editingItem = item;
      this.form = { ...item };
      this.showAddForm = true;
    },

    cancelEdit() {
      this.showAddForm = false;
      this.editingItem = null;
      this.resetForm();
    },

    resetForm() {
      this.form = {
        name: "",
        price: 0,
        weight: 0,
        category: "main",
        description: "",
        composition: "",
        image: "",
        featured: false,
      };
    },

    async saveItem() {
      try {
        // Убедимся, что URL изображения корректно сформирован
        const imageData = { ...this.form };
        if (imageData.image) {
          // Проверяем, является ли изображение уже полным URL или требует корректировки
          if (!imageData.image.startsWith('http') && !imageData.image.startsWith('/')) {
            // Если URL не начинается с http/https или / - возможно это относительный путь
            imageData.image = imageData.image;
          }
        }

        if (this.editingItem) {
          // Обновление существующего блюда
          await menuApi.update(this.editingItem.id, imageData);
          // Обновляем элемент в списке
          const index = this.menuItems.findIndex(
            (item) => item.id === this.editingItem.id
          );
          if (index !== -1) {
            this.menuItems[index] = { ...imageData, id: this.editingItem.id };
          }
        } else {
          // Добавление нового блюда
          const response = await menuApi.create(imageData);
          this.menuItems.unshift(response.data);
        }

        this.cancelEdit();
        this.$emit("menu-updated");
      } catch (error) {
        this.error = error.message || "Ошибка сохранения блюда";
        console.error("Ошибка сохранения блюда:", error);
      }
    },

    async deleteItem(itemId) {
      if (!confirm("Вы уверены, что хотите удалить это блюдо?")) {
        return;
      }

      try {
        await menuApi.delete(itemId);
        this.menuItems = this.menuItems.filter((item) => item.id !== itemId);
        this.$emit("menu-updated");
      } catch (error) {
        this.error = error.message || "Ошибка удаления блюда";
        console.error("Ошибка удаления блюда:", error);
      }
    },

    getCategoryName(category) {
      const categories = {
        'interior': 'Интерьер',
        'food': 'Блюда',
        'events': 'События',
        'staff': 'Персонал',
        'main': 'Основные',
        'appetizers': 'Закуски',
        'desserts': 'Десерты',
        'drinks': 'Напитки'
      };
      return categories[category] || category;
    },

    formatPrice(price) {
      return new Intl.NumberFormat("ru-RU").format(price);
    },

    handleImageError(event) {
      event.target.src = this.placeholderImage;
    },

    browseImageFile() {
      this.$refs.imageFileInput.click();
    },

    async handleImageFileChange(e) {
      const file = e.target.files[0];
      if (!file) return;

      if (!file.type.startsWith('image/')) {
        alert('Пожалуйста, выберите файл изображения');
        return;
      }

      try {
        // Показываем процесс загрузки
        const uploadId = Date.now();
        this.$emit('show-upload-progress', uploadId);

        const response = await imageApi.upload(file);

        // Обновляем поле изображения
        this.form.image = response.data.url || response.data.imageUrl || response.data.src;

        this.$emit('hide-upload-progress', uploadId);
      } catch (error) {
        console.error('Ошибка загрузки изображения:', error);
        this.$emit('hide-upload-progress', uploadId);
        alert('Ошибка загрузки изображения: ' + (error.message || 'Неизвестная ошибка'));
      }

      // Сбрасываем значение input
      e.target.value = '';
    },

    handleImagePreviewError(event) {
      event.target.src = this.placeholderImage;
    },
  },
};
</script>
