import { useState } from "react";
import { predictCustomer } from "../services/predictionService";

function PredictionForm({ onPredictionSuccess }) {

    // ==========================================
    // Customer Form Data
    // ==========================================

    const [formData, setFormData] = useState({

        gender: "Male",

        SeniorCitizen: 0,

        Partner: "Yes",

        Dependents: "Yes",

        tenure: "",

        PhoneService: "Yes",

        MultipleLines: "No",

        InternetService: "DSL",

        OnlineSecurity: "Yes",

        OnlineBackup: "Yes",

        DeviceProtection: "Yes",

        TechSupport: "Yes",

        StreamingTV: "Yes",

        StreamingMovies: "Yes",

        Contract: "Month-to-month",

        PaperlessBilling: "Yes",

        PaymentMethod: "Electronic check",

        MonthlyCharges: "",

        TotalCharges: ""

    });

    // ==========================================
    // Prediction Result
    // ==========================================

    const [predictionResult, setPredictionResult] = useState(null);

    // ==========================================
    // Loading
    // ==========================================

    const [loading, setLoading] = useState(false);

    // ==========================================
    // Handle Change
    // ==========================================

    const handleChange = (e) => {

        const { name, value } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]:
                name === "SeniorCitizen"
                    ? Number(value)
                    : value

        }));

    };

    // ==========================================
    // Submit Form
    // ==========================================

    const handleSubmit = async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            const response = await predictCustomer(formData);

            setPredictionResult(response.data);
            if (onPredictionSuccess) {
    onPredictionSuccess();
}

        }

        catch (error) {

            console.error(error);

            alert("Prediction Failed");

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div className="card shadow p-4">

            <h3 className="mb-4 text-center">

                Customer Information

            </h3>

            <form onSubmit={handleSubmit}>

                {/* ========================================== */}
                {/* Module 4.1 */}
                {/* ========================================== */}

                <div className="row">

                    <div className="col-md-6 mb-3">

                        <label className="form-label">

                            Gender

                        </label>

                        <select

                            className="form-select"

                            name="gender"

                            value={formData.gender}

                            onChange={handleChange}

                        >

                            <option>Male</option>

                            <option>Female</option>

                        </select>

                    </div>

                    <div className="col-md-6 mb-3">

                        <label className="form-label">

                            Senior Citizen

                        </label>

                        <select

                            className="form-select"

                            name="SeniorCitizen"

                            value={formData.SeniorCitizen}

                            onChange={handleChange}

                        >

                            <option value={0}>No</option>

                            <option value={1}>Yes</option>

                        </select>

                    </div>

                </div>

                {/* ========================================== */}
                {/* Module 4.2 */}
                {/* ========================================== */}

                <div className="row">

                    <div className="col-md-4 mb-3">

                        <label className="form-label">

                            Partner

                        </label>

                        <select

                            className="form-select"

                            name="Partner"

                            value={formData.Partner}

                            onChange={handleChange}

                        >

                            <option>Yes</option>

                            <option>No</option>

                        </select>

                    </div>

                    <div className="col-md-4 mb-3">

                        <label className="form-label">

                            Dependents

                        </label>

                        <select

                            className="form-select"

                            name="Dependents"

                            value={formData.Dependents}

                            onChange={handleChange}

                        >

                            <option>Yes</option>

                            <option>No</option>

                        </select>

                    </div>

                    <div className="col-md-4 mb-3">

                        <label className="form-label">

                            Tenure

                        </label>

                        <input

                            type="number"

                            className="form-control"

                            name="tenure"

                            value={formData.tenure}

                            onChange={handleChange}

                            placeholder="Enter Tenure"

                        />

                    </div>

                </div>
                                {/* ========================================== */}
                {/* Module 4.3 */}
                {/* ========================================== */}

                <div className="row">

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Phone Service
                        </label>

                        <select
                            className="form-select"
                            name="PhoneService"
                            value={formData.PhoneService}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                        </select>

                    </div>

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Multiple Lines
                        </label>

                        <select
                            className="form-select"
                            name="MultipleLines"
                            value={formData.MultipleLines}
                            onChange={handleChange}
                        >
                            <option>No</option>
                            <option>Yes</option>
                            <option>No phone service</option>
                        </select>

                    </div>

                </div>

                {/* ========================================== */}
                {/* Module 4.4 */}
                {/* ========================================== */}

                <div className="row">

                    <div className="col-md-4 mb-3">

                        <label className="form-label">
                            Internet Service
                        </label>

                        <select
                            className="form-select"
                            name="InternetService"
                            value={formData.InternetService}
                            onChange={handleChange}
                        >
                            <option>DSL</option>
                            <option>Fiber optic</option>
                            <option>No</option>
                        </select>

                    </div>

                    <div className="col-md-4 mb-3">

                        <label className="form-label">
                            Online Security
                        </label>

                        <select
                            className="form-select"
                            name="OnlineSecurity"
                            value={formData.OnlineSecurity}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                            <option>No internet service</option>
                        </select>

                    </div>

                    <div className="col-md-4 mb-3">

                        <label className="form-label">
                            Online Backup
                        </label>

                        <select
                            className="form-select"
                            name="OnlineBackup"
                            value={formData.OnlineBackup}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                            <option>No internet service</option>
                        </select>

                    </div>

                </div>

                <div className="row">

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Device Protection
                        </label>

                        <select
                            className="form-select"
                            name="DeviceProtection"
                            value={formData.DeviceProtection}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                            <option>No internet service</option>
                        </select>

                    </div>

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Tech Support
                        </label>

                        <select
                            className="form-select"
                            name="TechSupport"
                            value={formData.TechSupport}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                            <option>No internet service</option>
                        </select>

                    </div>

                </div>

                {/* ========================================== */}
                {/* Module 4.5 */}
                {/* ========================================== */}

                <div className="row">

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Streaming TV
                        </label>

                        <select
                            className="form-select"
                            name="StreamingTV"
                            value={formData.StreamingTV}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                            <option>No internet service</option>
                        </select>

                    </div>

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Streaming Movies
                        </label>

                        <select
                            className="form-select"
                            name="StreamingMovies"
                            value={formData.StreamingMovies}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                            <option>No internet service</option>
                        </select>

                    </div>

                </div>

                <div className="row">

                    <div className="col-md-4 mb-3">

                        <label className="form-label">
                            Contract
                        </label>

                        <select
                            className="form-select"
                            name="Contract"
                            value={formData.Contract}
                            onChange={handleChange}
                        >
                            <option>Month-to-month</option>
                            <option>One year</option>
                            <option>Two year</option>
                        </select>

                    </div>

                    <div className="col-md-4 mb-3">

                        <label className="form-label">
                            Paperless Billing
                        </label>

                        <select
                            className="form-select"
                            name="PaperlessBilling"
                            value={formData.PaperlessBilling}
                            onChange={handleChange}
                        >
                            <option>Yes</option>
                            <option>No</option>
                        </select>

                    </div>

                    <div className="col-md-4 mb-3">

                        <label className="form-label">
                            Payment Method
                        </label>

                        <select
                            className="form-select"
                            name="PaymentMethod"
                            value={formData.PaymentMethod}
                            onChange={handleChange}
                        >
                            <option>Electronic check</option>
                            <option>Mailed check</option>
                            <option>Bank transfer (automatic)</option>
                            <option>Credit card (automatic)</option>
                        </select>

                    </div>

                </div>

                {/* ========================================== */}
                {/* Module 4.6 */}
                {/* ========================================== */}

                <div className="row">

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Monthly Charges
                        </label>

                        <input
                            type="number"
                            step="0.01"
                            className="form-control"
                            name="MonthlyCharges"
                            value={formData.MonthlyCharges}
                            onChange={handleChange}
                            placeholder="Enter Monthly Charges"
                        />

                    </div>

                    <div className="col-md-6 mb-3">

                        <label className="form-label">
                            Total Charges
                        </label>

                        <input
                            type="number"
                            step="0.01"
                            className="form-control"
                            name="TotalCharges"
                            value={formData.TotalCharges}
                            onChange={handleChange}
                            placeholder="Enter Total Charges"
                        />

                    </div>

                </div>
                                {/* ========================================== */}
                {/* Submit Button */}
                {/* ========================================== */}

                <div className="d-grid mt-4">

                    <button
                        type="submit"
                        className="btn btn-primary btn-lg"
                        disabled={loading}
                    >

                        {
                            loading ? (
    <>
        <span
            className="spinner-border spinner-border-sm me-2"
            role="status"
        ></span>

        Predicting Customer...
    </>
) : (
    "Predict Customer Churn"
)

                        }

                    </button>

                </div>

            </form>

            {/* ========================================== */}
            {/* Prediction Result */}
            {/* ========================================== */}

            {

                predictionResult && (

                    <div className="card mt-5 border-success shadow">

                        <div className="card-header bg-success text-white">

                            <h4 className="mb-0">

                                Prediction Result

                            </h4>

                        </div>

                        <div className="card-body">

                            <h5>

    Prediction

</h5>

{

    predictionResult.prediction === "Yes"

        ?

        <span className="badge bg-danger fs-5">

            🔴 High Risk Customer

        </span>

        :

        <span className="badge bg-success fs-5">

            🟢 Low Risk Customer

        </span>

}

                            <h5 className="mt-4">

    Churn Probability

</h5>

<div className="progress mb-3">

    <div

        className="progress-bar progress-bar-striped progress-bar-animated"

        role="progressbar"

        style={{

            width: `${predictionResult.probability * 100}%`

        }}

    >

        {(predictionResult.probability * 100).toFixed(2)}%

    </div>

</div>
                            <h5>

    Customer Segment

</h5>

<p className="fs-5">

{

predictionResult.cluster === 1

?

"⭐ Loyal Customer"

:

predictionResult.cluster === 2

?

"🟠 High Value Customer"

:

"🟢 New Customer"

}

</p>

                            <hr />

                            <h5>

                                Recommendations

                            </h5>

                            <ul className="list-group">

                                {
    predictionResult.recommendations.map((item, index) => (

        <li
            key={index}
            className="list-group-item"
        >
            ✅ {item}
        </li>

    ))
}

                            </ul>

                        </div>

                    </div>

                )

            }

        </div>

    );

}

export default PredictionForm;