def summarize_listings(df):
    """
    Generate descriptive statistics and grouped summaries
    for the NYC Airbnb listings dataset.
    """
    summary = {
        "shape": df.shape,
        "price_statistics": df["price"].describe(),
        "room_type_counts": df["room_type"].value_counts(),
        "borough_counts": df["neighbourhood_group"].value_counts(),
        "average_price_by_room_type": (
            df.groupby("room_type")["price"]
            .mean()
            .sort_values(ascending=False)
        ),
        "average_price_by_borough": (
            df.groupby("neighbourhood_group")["price"]
            .mean()
            .sort_values(ascending=False)
        )
    }

    return summary