"""
Probability Gauge
-----------------
Creates a Plotly gauge chart for churn probability.
"""

import plotly.graph_objects as go


def probability_gauge(probability: float):
    """
    Create a gauge chart for churn probability.

    Parameters
    ----------
    probability : float
        Probability between 0 and 1.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    probability = max(0.0, min(1.0, probability))

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            number={
                "suffix": "%",
                "font": {"size": 40}
            },
            title={
                "text": "<b>Churn Probability</b>",
                "font": {"size": 22}
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1
                },
                "bar": {
                    "thickness": 0.35
                },
                "steps": [
                    {
                        "range": [0, 30],
                        "color": "#2ECC71"
                    },
                    {
                        "range": [30, 60],
                        "color": "#F4D03F"
                    },
                    {
                        "range": [60, 100],
                        "color": "#E74C3C"
                    }
                ],
                "threshold": {
                    "line": {
                        "width": 4
                    },
                    "thickness": 0.8,
                    "value": probability * 100
                },
            },
        )
    )

    fig.update_layout(
    height=450,
    margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig