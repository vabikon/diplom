/**
 * Нормализует URL изображения
 * @param {string} url - URL изображения
 * @param {string} baseUrl - Базовый URL API
 * @returns {string} Нормализованный URL
 */
export const normalizeImageUrl = (
  url,
  baseUrl = import.meta.env.VITE_API_BASE_URL || "/api"
) => {
  if (!url || typeof url !== "string") {
    return "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjZjVmNWY1Ii8+PHRleHQgeD0iMjAwIiB5PSIxNTAiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNiIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+R2FzdHJvbm9taWE8L3RleHQ+PC9zdmc+";
  }

  // Убираем возможные пробелы
  url = url.trim();

  // Проверяем, абсолютный ли URL
  if (url.startsWith("http://") || url.startsWith("https://")) {
    return url;
  }

  // Проверяем, является ли URL data URL
  if (url.startsWith("data:")) {
    return url;
  }

  // Для относительных путей
  const resolvedBaseUrl =
    typeof window !== "undefined" && baseUrl.startsWith("/")
      ? `${window.location.origin}${baseUrl}`
      : baseUrl;

  if (url.startsWith("/")) {
    return `${resolvedBaseUrl.replace("/api", "")}${url}`;
  }

  // Если путь без слэша
  return `${resolvedBaseUrl.replace("/api", "")}/${url}`;
};

/**
 * Проверяет, загрузилось ли изображение
 * @param {string} url - URL изображения
 * @returns {Promise<boolean>}
 */
export const checkImageExists = (url) => {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(true);
    img.onerror = () => resolve(false);
    img.src = url;
  });
};

/**
 * Создает placeholder изображение
 * @param {string} text - Текст для placeholder
 * @param {number} width - Ширина
 * @param {number} height - Высота
 * @returns {string} Data URL
 */
export const createPlaceholderImage = (
  text = "Gastronomia",
  width = 400,
  height = 300
) => {
  const svg = `<svg width="${width}" height="${height}" version="1.1" xmlns="http://www.w3.org/2000/svg">
    <rect width="${width}" height="${height}" fill="#f5f5f5"/>
    <text x="${width / 2}" y="${
    height / 2
  }" font-family="Arial" font-size="16" fill="#999" text-anchor="middle">${text}</text>
  </svg>`;
  return `data:image/svg+xml;base64,${btoa(svg)}`;
};

/**
 * Ленивая загрузка изображений
 * @param {HTMLElement} imgElement - Элемент img
 * @param {string} src - URL изображения
 */
export const lazyLoadImage = (imgElement, src) => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = src;
        observer.unobserve(img);
      }
    });
  });

  observer.observe(imgElement);
};
