def generate_recommendation(row):

    recommendations = []

    # Contract Type
    if row["Contract"] == "Month-to-month":
        recommendations.append(
            "Offer a long-term contract with a discount."
        )

    # Internet Service
    if row["InternetService"] == "Fiber optic":
        recommendations.append(
            "Provide premium technical support."
        )

    # Online Security
    if row["OnlineSecurity"] == "No":
        recommendations.append(
            "Recommend the Online Security package."
        )

    # Tech Support
    if row["TechSupport"] == "No":
        recommendations.append(
            "Offer free technical support for one month."
        )

    # Payment Method
    if row["PaymentMethod"] == "Electronic check":
        recommendations.append(
            "Encourage automatic payment methods."
        )

    # Paperless Billing
    if row["PaperlessBilling"] == "Yes":
        recommendations.append(
            "Provide loyalty rewards for paperless customers."
        )

    # Monthly Charges
    if row["MonthlyCharges"] > 80:
        recommendations.append(
            "Offer a discount on monthly charges."
        )

    # Tenure
    if row["tenure"] < 12:
        recommendations.append(
            "Send a welcome retention package."
        )

    return recommendations