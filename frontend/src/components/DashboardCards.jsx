function DashboardCards({

    total,
    highRisk,
    lowRisk,
    averageProbability,

}) {

    return (

        <div className="row mb-4">

            <div className="col-md-3">

                <div className="card shadow border-0 bg-primary text-white">

                    <div className="card-body">

                        <h6>Total Predictions</h6>

                        <h2>{total}</h2>

                    </div>

                </div>

            </div>

            <div className="col-md-3">

                <div className="card shadow border-0 bg-danger text-white">

                    <div className="card-body">

                        <h6>High Risk</h6>

                        <h2>{highRisk}</h2>

                    </div>

                </div>

            </div>

            <div className="col-md-3">

                <div className="card shadow border-0 bg-success text-white">

                    <div className="card-body">

                        <h6>Low Risk</h6>

                        <h2>{lowRisk}</h2>

                    </div>

                </div>

            </div>

            <div className="col-md-3">

                <div className="card shadow border-0 bg-warning">

                    <div className="card-body">

                        <h6>Average Probability</h6>

                        <h2>{averageProbability}%</h2>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default DashboardCards;