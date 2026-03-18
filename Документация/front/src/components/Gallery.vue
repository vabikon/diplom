<template>
  <div class="gallery">
    <!-- Статус загрузки -->
    <div v-if="loading" class="loading-state">
      <div class="loading-spinner"></div>
      <p>Загружаем фотографии...</p>
    </div>

    <!-- Основной контент -->
    <div v-else>
      <div
        class="gallery-grid"
        :style="{ gridTemplateColumns: `repeat(${columns}, 1fr)` }"
      >
        <div
          v-for="(image, index) in displayedImages"
          :key="image.id"
          class="gallery-item"
          @click="openLightbox(index)"
        >
          <div class="image-container">
            <img
              :src="image.src || image.url"
              :alt="image.alt"
              class="gallery-image"
              loading="lazy"
              @error="handleImageError"
            />
            <div v-if="image.description" class="image-overlay">
              <span class="image-description">{{ image.description }}</span>
            </div>
            <div v-if="image.category" class="image-category">
              {{ getCategoryName(image.category) }}
            </div>
          </div>
        </div>
      </div>

      <!-- Кнопка "Загрузить еще" если есть больше изображений -->
      <div v-if="hasMore && !loadingMore" class="load-more">
        <button class="btn btn-outline" @click="$emit('load-more')">
          Показать еще
        </button>
      </div>

      <div v-if="loadingMore" class="loading-more">
        <div class="loading-spinner small"></div>
      </div>
    </div>

    <!-- Лайтбокс -->
    <div v-if="showLightbox" class="lightbox" @click="closeLightbox">
      <button
        class="lightbox-close"
        @click="closeLightbox"
        aria-label="Закрыть"
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
      <button
        class="lightbox-nav prev"
        @click.stop="prevImage"
        aria-label="Предыдущее фото"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
        >
          <path d="M15 18l-6-6 6-6" />
        </svg>
      </button>
      <button
        class="lightbox-nav next"
        @click.stop="nextImage"
        aria-label="Следующее фото"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
        >
          <path d="M9 18l6-6-6-6" />
        </svg>
      </button>

      <div class="lightbox-content" @click.stop>
        <img
          :src="currentImage.src || currentImage.url"
          :alt="currentImage.alt"
          class="lightbox-image"
          loading="lazy"
        />
        <div v-if="currentImage.description" class="lightbox-caption">
          {{ currentImage.description }}
        </div>
        <div class="lightbox-counter">
          {{ currentIndex + 1 }} / {{ displayedImages.length }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Gallery",
  props: {
    images: {
      type: Array,
      default: () => [],
    },
    limit: {
      type: Number,
      default: null,
    },
    columns: {
      type: Number,
      default: 3,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    loadingMore: {
      type: Boolean,
      default: false,
    },
    hasMore: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      currentIndex: 0,
      showLightbox: false,
    };
  },
  computed: {
    displayedImages() {
      if (this.limit && this.limit > 0) {
        return this.images.slice(0, this.limit);
      }
      return this.images;
    },
    currentImage() {
      return this.displayedImages[this.currentIndex] || {};
    },
  },
  methods: {
    openLightbox(index) {
      this.currentIndex = index;
      this.showLightbox = true;
      document.body.style.overflow = "hidden";
      document.addEventListener("keydown", this.handleKeydown);
    },
    closeLightbox() {
      this.showLightbox = false;
      document.body.style.overflow = "auto";
      document.removeEventListener("keydown", this.handleKeydown);
    },
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.displayedImages.length;
    },
    prevImage() {
      this.currentIndex =
        (this.currentIndex - 1 + this.displayedImages.length) %
        this.displayedImages.length;
    },
    handleKeydown(event) {
      switch (event.key) {
        case "Escape":
          this.closeLightbox();
          break;
        case "ArrowRight":
          this.nextImage();
          break;
        case "ArrowLeft":
          this.prevImage();
          break;
      }
    },
    handleImageError(event) {
      // Запасное изображение при ошибке загрузки
      event.target.src =
        "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjZjVmNWY1Ii8+PHRleHQgeD0iMjAwIiB5PSIxNTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+R2FzdHJvbm9taWEgUmVzdGF1cmFudDwvdGV4dD48L3N2Zz4=";
      event.target.onerror = null;
    },
    getCategoryName(category) {
      const categories = {
        interior: "Интерьер",
        food: "Блюда",
        events: "События",
        staff: "Персонал",
        main: "Основные",
        appetizers: "Закуски",
        desserts: "Десерты",
        drinks: "Напитки",
      };
      return categories[category] || category;
    },
  },
};
</script>

<style scoped>
/* Стили для статусов загрузки */
.loading-state {
  text-align: center;
  padding: 60px 20px;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #374151;
  border-top-color: #f97316;
  border-radius: 50%;
  margin: 0 auto 20px;
  animation: spin 1s linear infinite;
}

.loading-spinner.small {
  width: 24px;
  height: 24px;
  border-width: 2px;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Основные стили галереи */
.gallery-grid {
  display: grid;
  gap: 20px;
  margin: 0;
}

.gallery-item {
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.3s ease;
  aspect-ratio: 1;
  position: relative;
}

.gallery-item:hover {
  transform: scale(1.02);
}

.image-container {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 12px;
  background: linear-gradient(
    135deg,
    rgba(31, 41, 55, 0.7),
    rgba(17, 24, 39, 0.7)
  );
  backdrop-filter: blur(16px);
  border: 1px solid rgba(75, 85, 99, 0.5);
}

.gallery-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.gallery-item:hover .gallery-image {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
  padding: 20px;
  transform: translateY(100%);
  transition: transform 0.3s ease;
}

.gallery-item:hover .image-overlay {
  transform: translateY(0);
}

.image-description {
  color: white;
  font-size: 14px;
  display: block;
}

.image-category {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

/* Кнопка "Загрузить еще" */
.load-more {
  text-align: center;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid rgba(75, 85, 99, 0.3);
}

.btn {
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
  cursor: pointer;
}

.btn-outline {
  background: linear-gradient(
    135deg,
    rgba(31, 41, 55, 0.7),
    rgba(17, 24, 39, 0.7)
  );
  border: 1px solid rgba(75, 85, 99, 0.5);
  color: #d1d5db;
}

.btn-outline:hover {
  border-color: #f97316;
  color: #f97316;
  transform: translateY(-2px);
}

.loading-more {
  text-align: center;
  margin-top: 20px;
  padding: 20px;
}

/* Лайтбокс */
.lightbox {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.95);
  z-index: 3000;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: fadeIn 0.3s ease;
}

.lightbox-close {
  position: absolute;
  top: 24px;
  right: 24px;
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
  padding: 8px;
  border-radius: 4px;
  transition: background 0.2s ease;
  z-index: 3001;
}

.lightbox-close:hover {
  background: rgba(255, 255, 255, 0.1);
}

.lightbox-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s ease;
  z-index: 3001;
}

.lightbox-nav:hover {
  background: rgba(255, 255, 255, 0.2);
}

.lightbox-nav.prev {
  left: 24px;
}

.lightbox-nav.next {
  right: 24px;
}

.lightbox-content {
  max-width: 90vw;
  max-height: 90vh;
  position: relative;
}

.lightbox-image {
  max-width: 100%;
  max-height: 70vh;
  object-fit: contain;
  display: block;
  margin: 0 auto;
}

.lightbox-caption {
  color: white;
  text-align: center;
  padding: 16px;
  font-size: 16px;
  background: rgba(0, 0, 0, 0.7);
  border-radius: 4px;
  margin-top: 10px;
}

.lightbox-counter {
  position: absolute;
  top: 16px;
  left: 16px;
  color: white;
  font-size: 14px;
  background: rgba(0, 0, 0, 0.7);
  padding: 4px 12px;
  border-radius: 20px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Адаптивность */
@media (max-width: 768px) {
  .gallery-grid {
    gap: 10px;
  }

  .lightbox-nav {
    width: 40px;
    height: 40px;
  }

  .lightbox-nav.prev {
    left: 16px;
  }

  .lightbox-nav.next {
    right: 16px;
  }

  .lightbox-close {
    top: 16px;
    right: 16px;
  }
}

@media (max-width: 480px) {
  .lightbox-nav {
    width: 36px;
    height: 36px;
  }

  .lightbox-image {
    max-height: 60vh;
  }
}
</style>
