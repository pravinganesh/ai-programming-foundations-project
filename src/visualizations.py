import matplotlib.pyplot as plt
import seaborn as sns


def plot_price_distribution(df, max_price=500):
    """
    Plot the distribution of Airbnb listing prices.

    A price cutoff is used only for visualization so that
    extreme values do not dominate the plot.
    """
    price_plot = df[df["price"] <= max_price]

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=price_plot,
        x="price",
        bins=50,
        kde=True
    )

    plt.title("Distribution of Airbnb Listing Prices")
    plt.xlabel("Price per Night ($)")
    plt.ylabel("Number of Listings")
    plt.tight_layout()

    return plt.gca()


def plot_average_price_by_borough(df):
    """
    Plot average Airbnb listing price by NYC borough.
    """
    borough_prices = (
        df.groupby("neighbourhood_group")["price"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=borough_prices.index,
        y=borough_prices.values
    )

    plt.title("Average Airbnb Price by Borough")
    plt.xlabel("Borough")
    plt.ylabel("Average Price per Night ($)")
    plt.xticks(rotation=30)
    plt.tight_layout()

    return plt.gca()


def plot_price_by_room_type(df, max_price=500):
    """
    Plot Airbnb price distributions by room type.

    A price cutoff is used only for visualization.
    """
    price_boxplot = df[df["price"] <= max_price]

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=price_boxplot,
        x="room_type",
        y="price"
    )

    plt.title("Airbnb Prices by Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Price per Night ($)")
    plt.tight_layout()

    return plt.gca()