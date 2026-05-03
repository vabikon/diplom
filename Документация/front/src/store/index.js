import { createStore } from "vuex";
import { menuApi, reviewsApi, galleryApi } from "@/api";

export default createStore({
  state: {
    cart: [],
    menuItems: [],
    reviews: [],
    galleryImages: [],
    loading: {
      menu: false,
      reviews: false,
      gallery: false,
    },
    error: null,
  },
  mutations: {
    // Мутации для меню
    SET_MENU_ITEMS(state, items) {
      state.menuItems = items;
    },
    SET_MENU_LOADING(state, isLoading) {
      state.loading.menu = isLoading;
    },
    SET_MENU_ERROR(state, error) {
      state.error = error;
    },

    // Мутации для отзывов
    SET_REVIEWS(state, reviews) {
      state.reviews = reviews;
    },
    ADD_REVIEW(state, review) {
      state.reviews.unshift(review);
    },
    SET_REVIEWS_LOADING(state, isLoading) {
      state.loading.reviews = isLoading;
    },

    // Мутации для галереи
    SET_GALLERY_IMAGES(state, images) {
      state.galleryImages = images;
    },
    SET_GALLERY_LOADING(state, isLoading) {
      state.loading.gallery = isLoading;
    },

    // Мутации для корзины
    ADD_TO_CART(state, item) {
      const existingItem = state.cart.find((i) => i.id === item.id);
      if (existingItem) {
        existingItem.quantity += 1;
      } else {
        state.cart.push({ ...item, quantity: 1 });
      }
    },
    REMOVE_FROM_CART(state, itemId) {
      state.cart = state.cart.filter((item) => item.id !== itemId);
    },
    UPDATE_QUANTITY(state, { itemId, quantity }) {
      const item = state.cart.find((i) => i.id === itemId);
      if (item) {
        item.quantity = quantity;
      }
    },
    CLEAR_CART(state) {
      state.cart = [];
    },
  },
  actions: {
    // Действия для меню
    async fetchMenuItems({ commit }) {
      try {
        commit("SET_MENU_LOADING", true);
        commit("SET_MENU_ERROR", null);

        const response = await menuApi.getAll();
        commit("SET_MENU_ITEMS", response.data);

        return response.data;
      } catch (error) {
        commit("SET_MENU_ERROR", error.message);
        throw error;
      } finally {
        commit("SET_MENU_LOADING", false);
      }
    },

    async fetchMenuByCategory({ commit }, category) {
      try {
        commit("SET_MENU_LOADING", true);
        const response = await menuApi.getByCategory(category);
        return response.data;
      } catch (error) {
        commit("SET_MENU_ERROR", error.message);
        throw error;
      } finally {
        commit("SET_MENU_LOADING", false);
      }
    },

    // Действия для отзывов
    async fetchReviews({ commit }) {
      try {
        commit("SET_REVIEWS_LOADING", true);
        const response = await reviewsApi.getAll();
        commit("SET_REVIEWS", response.data);
        return response.data;
      } catch (error) {
        console.error("Error fetching reviews:", error);
        throw error;
      } finally {
        commit("SET_REVIEWS_LOADING", false);
      }
    },

    async addReview({ commit }, reviewData) {
      try {
        const response = await reviewsApi.create(reviewData);
        commit("ADD_REVIEW", response.data);
        return response.data;
      } catch (error) {
        console.error("Error adding review:", error);
        throw error;
      }
    },

    // Действия для галереи
    async fetchGalleryImages({ commit }) {
      try {
        commit("SET_GALLERY_LOADING", true);
        const response = await galleryApi.getAll();
        commit("SET_GALLERY_IMAGES", response.data);
        return response.data;
      } catch (error) {
        console.error("Error fetching gallery:", error);
        throw error;
      } finally {
        commit("SET_GALLERY_LOADING", false);
      }
    },

    async fetchGalleryByCategory({ commit }, category) {
      try {
        commit("SET_GALLERY_LOADING", true);
        const response = await galleryApi.getByCategory(category);
        return response.data;
      } catch (error) {
        console.error("Error fetching gallery by category:", error);
        throw error;
      } finally {
        commit("SET_GALLERY_LOADING", false);
      }
    },

    // Действия для корзины
    addToCart({ commit }, item) {
      commit("ADD_TO_CART", item);
    },

    removeFromCart({ commit }, itemId) {
      commit("REMOVE_FROM_CART", itemId);
    },

    updateCartQuantity({ commit }, { itemId, quantity }) {
      commit("UPDATE_QUANTITY", { itemId, quantity });
    },

    async createOrder({ state }) {
      try {
        const orderData = {
          items: state.cart,
          total: state.cart.reduce(
            (sum, item) => sum + item.price * item.quantity,
            0
          ),
          timestamp: new Date().toISOString(),
        };

        return { id: Date.now(), ...orderData };
      } catch (error) {
        console.error("Error creating order:", error);
        throw error;
      }
    },
  },
  getters: {
    // Геттеры для меню
    menuItems: (state) => state.menuItems,
    menuLoading: (state) => state.loading.menu,
    menuError: (state) => state.error,

    // Геттеры для отзывов
    reviews: (state) => state.reviews,
    reviewsLoading: (state) => state.loading.reviews,

    // Геттеры для галереи
    galleryImages: (state) => state.galleryImages,
    galleryLoading: (state) => state.loading.gallery,

    // Геттеры для корзины
    cart: (state) => state.cart,
    cartTotal: (state) => {
      return state.cart.reduce(
        (total, item) => total + item.price * item.quantity,
        0
      );
    },
    cartItemCount: (state) => {
      return state.cart.reduce((count, item) => count + item.quantity, 0);
    },

    // Геттеры для фильтрации
    menuItemsByCategory: (state) => (category) => {
      if (category === "all") return state.menuItems;
      return state.menuItems.filter((item) => item.category === category);
    },

    featuredMenuItems: (state) => {
      return state.menuItems.filter((item) => item.featured).slice(0, 3);
    },

    featuredReviews: (state) => {
      return state.reviews.slice(0, 3);
    },

    averageRating: (state) => {
      if (state.reviews.length === 0) return 0;
      const sum = state.reviews.reduce((acc, review) => acc + review.rating, 0);
      return (sum / state.reviews.length).toFixed(1);
    },
  },
});
