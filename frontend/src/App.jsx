import { useEffect, useState } from "react";
import { getHealth } from "./services/predictionService";

function App() {

    const [status, setStatus] = useState("Checking...");

    useEffect(() => {

        async function checkAPI() {

            try {

                const response = await getHealth();

                setStatus(response.data.status);

            } catch (error) {

                console.error(error);

                setStatus("Backend Offline");

            }

        }

        checkAPI();

    }, []);

    return (

        <div className="container mt-5">

            <h1 className="text-center">
                Customer Churn Prediction Dashboard
            </h1>

            <hr />

            <div className="card p-4 shadow">

                <h4>Backend Status</h4>

                <h2 className="text-success">
                    {status}
                </h2>

            </div>

        </div>

    );
}

export default App;