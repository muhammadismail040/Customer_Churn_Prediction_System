import api from "../api/api";

// ======================================================
// Health Check
// ======================================================

export const getHealth = () =>
    api.get("/health");

// ======================================================
// Predict Customer
// ======================================================

export const predictCustomer = (data) =>
    api.post("/predict", data);

// ======================================================
// Get All Prediction History
// ======================================================

export const getPredictionHistory = () =>
    api.get("/predictions");

// ======================================================
// Get Latest Prediction
// ======================================================

export const getLatestPrediction = () =>
    api.get("/predictions/latest");

// ======================================================
// Get Prediction Count
// ======================================================

export const getPredictionCount = () =>
    api.get("/predictions/count");

// ======================================================
// Delete Prediction
// ======================================================

export const deletePrediction = (id) =>
    api.delete(`/predictions/${id}`);