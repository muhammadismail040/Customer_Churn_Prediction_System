import axios from "axios";

export default axios.create({
    baseURL: "https://customerchurnpredictionsystem-production.up.railway.app",

    headers: {
        "Content-Type": "application/json",

        "x-api-key": "customer_churn_ml_api_2026",
    },
});