<template>
  <div class="space-y-8">
    <!-- Заголовок -->
    <div>
      <h2 class="text-2xl font-bold text-white mb-2">Управление галереей</h2>
      <p class="text-gray-400 text-sm">Загрузка и управление изображениями</p>
    </div>

    <!-- Загрузка изображений -->
    <div
      class="bg-gradient-to-br from-gray-800/50 to-gray-900/50 border-2 border-dashed rounded-2xl p-8 transition-all duration-300"
      :class="
        isDragOver
          ? 'border-orange-500 bg-orange-500/10'
          : 'border-gray-700 hover:border-gray-600'
      "
      @dragover.prevent="handleDragOver"
      @drop.prevent="handleDrop"
      @dragleave="handleDragLeave"
    >
      <input
        type="file"
        ref="fileInput"
        @change="handleFileChange"
        accept="image/*"
        multiple
        class="hidden"
      />

      <div class="text-center">
        <div
          class="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-orange-500/20 to-red-500/20 rounded-full flex items-center justify-center"
        >
          <svg
            width="32"
            height="32"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            class="text-orange-500"
          >
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
            <polyline points="17 8 12 3 7 8" />
            <line x1="12" y1="3" x2="12" y2="15" />
          </svg>
        </div>

        <h4 class="text-lg font-semibold text-white mb-2">
          Загрузка изображений галереи
        </h4>

        <p class="text-gray-400 mb-3">
          Перетащите файлы сюда или
          <button
            type="button"
            @click="browseFiles"
            class="text-orange-500 hover:text-orange-400 font-semibold underline"
          >
            выберите вручную
          </button>
        </p>

        <p class="text-gray-500 text-sm">
          Поддерживаются форматы: JPG, PNG, GIF, WEBP
        </p>
      </div>
    </div>

    <!-- Процесс загрузки -->
    <div v-if="uploads.length > 0" class="space-y-4">
      <h4 class="text-lg font-semibold text-white">Загрузки</h4>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div
          v-for="upload in uploads"
          :key="upload.id"
          class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-xl overflow-hidden"
        >
          <!-- Загрузка -->
          <div v-if="upload.status === 'uploading'" class="p-6 text-center">
            <div class="w-full bg-gray-700 rounded-full h-2 mb-3">
              <div
                class="bg-gradient-to-r from-orange-500 to-red-500 h-2 rounded-full transition-all duration-300"
                :style="{ width: upload.progress + '%' }"
              ></div>
            </div>
            <p class="text-gray-400 text-sm">
              Загрузка... {{ upload.progress }}%
            </p>
          </div>

          <!-- Успех -->
          <div v-else-if="upload.status === 'success'">
            <img
              :src="upload.url || upload.src || upload.imageUrl"
              :alt="upload.filename"
              class="w-full h-40 object-cover"
              @error="handleImageError"
            />
            <div class="p-4">
              <p class="text-white font-medium text-sm truncate mb-1">
                {{ upload.filename }}
              </p>
              <p class="text-gray-500 text-xs mb-3">
                {{ formatFileSize(upload.size) }}
              </p>
              <div class="flex gap-2">
                <a
                  :href="upload.url || upload.src || upload.imageUrl"
                  target="_blank"
                  class="flex-1 px-3 py-2 bg-gray-900 border border-gray-700 text-white text-xs rounded-lg hover:border-orange-500/50 transition-colors text-center"
                >
                  Открыть
                </a>
                <button
                  @click="copyUrl(upload.url || upload.src || upload.imageUrl)"
                  class="flex-1 px-3 py-2 bg-gray-900 border border-gray-700 text-white text-xs rounded-lg hover:border-orange-500/50 transition-colors"
                >
                  Копировать
                </button>
              </div>
            </div>
          </div>

          <!-- Ошибка -->
          <div v-else-if="upload.status === 'error'" class="p-6 text-center">
            <p class="text-red-400 text-sm mb-3">Ошибка: {{ upload.error }}</p>
            <button
              @click="retryUpload(upload)"
              class="px-4 py-2 bg-gray-900 border border-gray-700 text-white text-sm rounded-lg hover:border-orange-500/50 transition-colors"
            >
              Повторить
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Статус загрузки галереи -->
    <div v-if="loading" class="text-center py-12">
      <div
        class="inline-block w-12 h-12 border-4 border-gray-700 border-t-orange-500 rounded-full animate-spin mb-4"
      ></div>
      <p class="text-gray-400">Загружаем галерею...</p>
    </div>

    <!-- Ошибка -->
    <div v-else-if="error" class="text-center py-12">
      <p class="text-red-400">Ошибка: {{ error }}</p>
    </div>

    <!-- Форма добавления в галерею -->
    <div
      v-else
      class="bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 rounded-2xl p-6"
    >
      <h3 class="text-xl font-bold text-white mb-6">
        {{
          editingImage
            ? "Редактировать изображение"
            : "Добавить изображение в галерею"
        }}
      </h3>

      <form @submit.prevent="addGalleryImage" class="space-y-6">
        <!-- URL изображения и описание -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-gray-400 text-sm mb-2" for="imageUrl">
              URL изображения *
            </label>
            <input
              id="imageUrl"
              v-model="form.imageUrl"
              type="text"
              required
              placeholder="https://example.com/image.jpg"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>

          <div>
            <label
              class="block text-gray-400 text-sm mb-2"
              for="imageDescription"
            >
              Описание изображения
            </label>
            <input
              id="imageDescription"
              v-model="form.description"
              type="text"
              placeholder="Краткое описание"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>
        </div>

        <!-- Alt текст и категория -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-gray-400 text-sm mb-2" for="imageAlt">
              Текст для alt (для SEO)
            </label>
            <input
              id="imageAlt"
              v-model="form.alt"
              type="text"
              placeholder="Описание для поисковых систем"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white placeholder-gray-600 focus:outline-none focus:border-orange-500 transition-colors"
            />
          </div>

          <div>
            <label class="block text-gray-400 text-sm mb-2" for="imageCategory">
              Категория
            </label>
            <select
              id="imageCategory"
              v-model="form.category"
              class="w-full px-4 py-3 bg-gray-900 border border-gray-700 rounded-xl text-white focus:outline-none focus:border-orange-500 transition-colors"
            >
              <option value="">Без категории</option>
              <option value="interior">Интерьер</option>
              <option value="food">Блюда</option>
              <option value="events">События</option>
              <option value="staff">Персонал</option>
            </select>
          </div>
        </div>

        <!-- Кнопки -->
        <div class="flex gap-3">
          <button
            type="submit"
            class="px-6 py-3 bg-gradient-to-r from-orange-500 to-red-500 text-white font-semibold rounded-xl hover:shadow-lg hover:shadow-orange-500/25 transition-all duration-300"
          >
            {{ editingImage ? "Сохранить изменения" : "Добавить в галерею" }}
          </button>
          <button
            v-if="editingImage"
            type="button"
            @click="cancelEdit"
            class="px-6 py-3 bg-gradient-to-br from-gray-800 to-gray-900 border border-gray-700 text-white rounded-xl hover:border-gray-600 transition-all duration-300"
          >
            Отмена
          </button>
        </div>
      </form>
    </div>

    <!-- Таблица галереи -->
    <div v-if="!loading && !error && galleryImages.length > 0">
      <h3 class="text-xl font-bold text-white mb-4">
        Текущие изображения галереи
      </h3>

      <div class="overflow-x-auto rounded-xl border border-gray-700">
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
                Описание
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Категория
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-semibold text-gray-400 uppercase tracking-wider"
              >
                Действия
              </th>
            </tr>
          </thead>
          <tbody class="bg-gradient-to-br from-gray-800 to-gray-900">
            <tr
              v-for="image in galleryImages"
              :key="image.id"
              class="border-b border-gray-700 hover:bg-gray-800/50 transition-colors"
            >
              <td class="px-4 py-3">
                <img
                  :src="image.src || image.url || image.imageUrl"
                  :alt="image.description || 'Галерея'"
                  class="w-20 h-20 object-cover rounded-lg"
                  @error="handleImageError"
                />
              </td>
              <td class="px-4 py-3 text-gray-300">
                {{ image.description || "Без описания" }}
              </td>
              <td class="px-4 py-3 text-gray-300">
                {{ getCategoryName(image.category) || "Без категории" }}
              </td>
              <td class="px-4 py-3">
                <div class="flex gap-2">
                  <button
                    @click="editImage(image)"
                    class="px-3 py-1.5 bg-gray-900 border border-gray-700 text-white text-sm rounded-lg hover:border-orange-500/50 transition-colors"
                  >
                    Изменить
                  </button>
                  <button
                    @click="deleteImage(image.id)"
                    class="px-3 py-1.5 bg-gray-900 border border-red-500/50 text-red-400 text-sm rounded-lg hover:bg-red-500/10 hover:border-red-500 transition-colors"
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

    <!-- Пустое состояние -->
    <div
      v-if="!loading && !error && galleryImages.length === 0"
      class="text-center py-12"
    >
      <div
        class="w-24 h-24 mx-auto mb-4 bg-gradient-to-br from-gray-800/50 to-gray-900/50 rounded-full flex items-center justify-center"
      >
        <svg
          width="48"
          height="48"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          class="text-gray-600"
        >
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />
          <circle cx="8.5" cy="8.5" r="1.5" />
          <polyline points="21 15 16 10 5 21" />
        </svg>
      </div>
      <p class="text-gray-400 text-lg">Галерея пуста</p>
      <p class="text-gray-500 text-sm">Загрузите первое изображение</p>
    </div>
  </div>
</template>

<script>
import { galleryApi, imageApi } from "@/api";

export default {
  name: "GalleryManager",
  data() {
    return {
      loading: false,
      error: null,
      galleryImages: [],
      isDragOver: false,
      uploads: [],
      progressMap: new Map(),
      form: {
        imageUrl: "",
        description: "",
        category: "",
        alt: "Изображение галереи",
        src: "",
      },
      editingImage: null,
      showImageForm: false,
    };
  },
  async mounted() {
    await this.loadGalleryImages();
  },
  methods: {
    async loadGalleryImages() {
      try {
        this.loading = true;
        this.error = null;
        const response = await galleryApi.getAll();

        // Обработка изображений при загрузке
        this.galleryImages = response.data.map(image => {
          if (image.src || image.url) {
            // Убедимся, что URL изображения корректно сформирован
            image.src = image.src || image.url;
          }
          return image;
        });
      } catch (error) {
        this.error = error.message || "Ошибка загрузки галереи";
        console.error("Ошибка загрузки галереи:", error);
      } finally {
        this.loading = false;
      }
    },

    browseFiles() {
      this.$refs.fileInput.click();
    },

    handleDragOver(e) {
      e.preventDefault();
      this.isDragOver = true;
    },

    handleDragLeave(e) {
      if (!e.currentTarget.contains(e.relatedTarget)) {
        this.isDragOver = false;
      }
    },

    handleDrop(e) {
      e.preventDefault();
      this.isDragOver = false;
      const files = Array.from(e.dataTransfer.files);
      this.processFiles(files);
    },

    handleFileChange(e) {
      const files = Array.from(e.target.files);
      this.processFiles(files);
      e.target.value = "";
    },

    processFiles(files) {
      const imageFiles = files.filter((file) => file.type.startsWith("image/"));

      if (imageFiles.length === 0) {
        alert("Пожалуйста, выберите файлы изображений (JPEG, PNG, GIF, WEBP)");
        return;
      }

      imageFiles.forEach((file) => {
        const uploadId = Date.now() + Math.random();
        const uploadObject = {
          id: uploadId,
          file,
          filename: file.name,
          size: file.size,
          status: "uploading",
          progress: 0,
        };

        this.uploads.unshift(uploadObject);
        this.uploadFile(file, uploadId);
      });
    },

    async uploadFile(file, uploadId) {
      try {
        const upload = this.uploads.find((u) => u.id === uploadId);
        if (!upload) return;

        this.progressMap.set(uploadId, 0);

        const response = await imageApi.upload(file);

        const index = this.uploads.findIndex((u) => u.id === uploadId);
        if (index !== -1) {
          // Убедимся, что URL изображения корректно сформирован
        const imageUrl = response.data.url || response.data.imageUrl || response.data.src;

        this.uploads[index] = {
            ...upload,
            status: "success",
            url: imageUrl,
            ...response.data,
          };
        }

        this.progressMap.delete(uploadId);

        // Убедимся, что URL изображения корректно сформирован
        const imageUrl = response.data.url || response.data.imageUrl || response.data.src;

        this.form = {
          ...this.form,
          imageUrl: imageUrl,
          description: upload.filename,
          category: "",
          alt: upload.filename || "Изображение галереи",
        };
        this.showImageForm = true;
      } catch (error) {
        console.error("Ошибка загрузки изображения:", error);

        const index = this.uploads.findIndex((u) => u.id === uploadId);
        if (index !== -1) {
          this.uploads[index] = {
            ...this.uploads[index],
            status: "error",
            error: error.message || "Неизвестная ошибка",
          };
        }

        this.progressMap.delete(uploadId);
      }
    },

    async addGalleryImage() {
      try {
        // Убедимся, что URL изображения корректно сформирован
        const imageUrl = this.form.imageUrl;

        const galleryItem = {
          src: imageUrl,
          alt: this.form.alt || this.form.description || "Изображение галереи",
          description: this.form.description,
          category: this.form.category,
        };

        if (this.editingImage) {
          const response = await galleryApi.update(
            this.editingImage.id,
            galleryItem
          );
          const index = this.galleryImages.findIndex(
            (img) => img.id === this.editingImage.id
          );
          if (index !== -1) {
            // Обновляем изображение с корректным URL
            this.galleryImages[index] = {
              ...response.data,
              src: response.data.src || response.data.url || imageUrl
            };
          }
        } else {
          const response = await galleryApi.upload(galleryItem);
          this.galleryImages.unshift({
            ...response.data,
            src: response.data.src || response.data.url || imageUrl
          });
        }

        this.cancelEdit();
        this.$emit("gallery-updated");
      } catch (error) {
        this.error = error.message || "Ошибка сохранения изображения в галерее";
        console.error("Ошибка сохранения изображения в галерее:", error);
      }
    },

    editImage(image) {
      this.editingImage = image;
      this.form = {
        imageUrl: image.src || image.url || image.imageUrl,
        description: image.description,
        category: image.category || "",
        alt: image.alt || image.description || "Изображение галереи",
      };

      // Прокрутка к форме
      window.scrollTo({ top: 0, behavior: "smooth" });
    },

    async deleteImage(imageId) {
      if (!confirm("Вы уверены, что хотите удалить это изображение?")) {
        return;
      }

      try {
        await galleryApi.delete(imageId);
        this.galleryImages = this.galleryImages.filter(
          (image) => image.id !== imageId
        );
        this.$emit("gallery-updated");
      } catch (error) {
        this.error = error.message || "Ошибка удаления изображения";
        console.error("Ошибка удаления изображения:", error);
      }
    },

    resetForm() {
      this.form = {
        imageUrl: "",
        description: "",
        category: "",
        alt: "Изображение галереи",
        src: "",
      };
      this.editingImage = null;
    },

    cancelEdit() {
      this.editingImage = null;
      this.showImageForm = false;
      this.resetForm();
    },

    retryUpload(upload) {
      const index = this.uploads.findIndex((u) => u.id === upload.id);
      if (index !== -1) {
        this.uploads[index] = {
          ...upload,
          status: "uploading",
          progress: 0,
        };
        this.uploadFile(upload.file, upload.id);
      }
    },

    copyUrl(url) {
      // Убедимся, что URL корректно сформирован
      const fullUrl = url.startsWith('http') ? url : window.location.origin + url;
      navigator.clipboard
        .writeText(fullUrl)
        .then(() => {
          alert("URL скопирован в буфер обмена");
        })
        .catch((err) => {
          console.error("Ошибка копирования URL:", err);
          alert("Ошибка копирования URL");
        });
    },

    handleImageError(event) {
      event.target.src =
        "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjZjVmNWY1Ii8+PHRleHQgeD0iMjAwIiB5PSIxNTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+R2FzdHJvbm9taWEgUmVzdGF1cmFudDwvdGV4dD48L3N2Zz4=";
      event.target.onerror = null;
    },

    formatFileSize(bytes) {
      if (bytes === 0) return "0 Bytes";
      const k = 1024;
      const sizes = ["Bytes", "KB", "MB", "GB"];
      const i = Math.floor(Math.log(bytes) / Math.log(k));
      return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
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
  },
};
</script>
