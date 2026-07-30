import {

    PieChart,
    Pie,
    Cell,
    Tooltip,
    Legend,
    ResponsiveContainer,

    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,

} from "recharts";

function PredictionCharts({

    highRisk,
    lowRisk,
    history,

}) {

    const pieData = [

        {
            name: "High Risk",
            value: highRisk,
        },

        {
            name: "Low Risk",
            value: lowRisk,
        },

    ];

    const COLORS = [

        "#dc3545",

        "#198754",

    ];

    const clusterData = [

        {
            cluster: "Cluster 0",
            count: history.filter(
                (item) => item.cluster === 0
            ).length,
        },

        {
            cluster: "Cluster 1",
            count: history.filter(
                (item) => item.cluster === 1
            ).length,
        },

        {
            cluster: "Cluster 2",
            count: history.filter(
                (item) => item.cluster === 2
            ).length,
        },

    ];

    return (

        <div className="row mb-4">

            <div className="col-md-6">

                <div className="card shadow">

                    <div className="card-header bg-primary text-white">

                        Churn Distribution

                    </div>

                    <div className="card-body">

                        <ResponsiveContainer
                            width="100%"
                            height={300}
                        >

                            <PieChart>

                                <Pie
                                    data={pieData}
                                    dataKey="value"
                                    outerRadius={100}
                                    label
                                >

                                    {

                                        pieData.map(

                                            (entry, index) => (

                                                <Cell

                                                    key={index}

                                                    fill={COLORS[index]}

                                                />

                                            )

                                        )

                                    }

                                </Pie>

                                <Tooltip />

                                <Legend />

                            </PieChart>

                        </ResponsiveContainer>

                    </div>

                </div>

            </div>

            <div className="col-md-6">

                <div className="card shadow">

                    <div className="card-header bg-success text-white">

                        Customer Clusters

                    </div>

                    <div className="card-body">

                        <ResponsiveContainer
                            width="100%"
                            height={300}
                        >

                            <BarChart
                                data={clusterData}
                            >

                                <CartesianGrid strokeDasharray="3 3" />

                                <XAxis dataKey="cluster" />

                                <YAxis />

                                <Tooltip />

                                <Legend />

                                <Bar
                                    dataKey="count"
                                    fill="#0d6efd"
                                />

                            </BarChart>

                        </ResponsiveContainer>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default PredictionCharts;