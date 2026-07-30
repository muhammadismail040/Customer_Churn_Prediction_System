import PredictionForm from "./components/PredictionForm";
import PredictionHistory from "./components/PredictionHistory";
import { useState } from "react";

function App() {

    const [refresh, setRefresh] = useState(false);

    const refreshHistory = () => {
        setRefresh(prev => !prev);
    };

    return (

        <div className="container my-5">

            <h1 className="text-center mb-4">
                Customer Churn Prediction Dashboard
            </h1>

            <PredictionForm
                onPredictionSuccess={refreshHistory}
            />

            <hr className="my-5" />

            <PredictionHistory
                refresh={refresh}
            />

        </div>

    );

}

export default App;