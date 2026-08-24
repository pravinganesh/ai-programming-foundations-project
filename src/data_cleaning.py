import pandas as pd


def clean_review_fields(df):
    """
    Clean review-related fields by converting the last review date
    to datetime and replacing missing review-frequency values with zero
    when listings have no reviews.
    """
    cleaned = df.copy()

    cleaned["last_review"] = pd.to_datetime(
        cleaned["last_review"],
        errors="coerce"
    )

    cleaned.loc[
        cleaned["number_of_reviews"] == 0,
        "reviews_per_month"
    ] = cleaned.loc[
        cleaned["number_of_reviews"] == 0,
        "reviews_per_month"
    ].fillna(0)

    return cleaned


def clean_text_fields(df):
    """
    Clean missing listing and host names by replacing missing text
    values with descriptive placeholder labels.
    """
    cleaned = df.copy()

    cleaned["name"] = cleaned["name"].fillna("Unknown Listing")
    cleaned["host_name"] = cleaned["host_name"].fillna("Unknown Host")

    return cleaned