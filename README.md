# NYC Airbnb Data Workflow

## Project Overview

This project develops a reproducible data workflow using the NYC Airbnb Open Data dataset from 2019.

The workflow covers:

- Data ingestion
- Data quality assessment
- Missing-value analysis
- Duplicate detection
- Data cleaning
- Exploratory data analysis
- Data visualization
- Interpretation of findings
- Limitations and responsible data practices
- Reproducibility

The project establishes a reusable data foundation for future machine learning, deep learning, generative AI, and agentic AI projects.

---

## Dataset

The project uses the **NYC Airbnb Open Data** dataset from 2019.

The raw dataset is stored in:

```text
data/AB_NYC_2019.csv
```

The raw CSV file is treated as the source dataset and is not modified during the analysis.

The dataset contains:

- **48,895 listings**
- **16 columns**
- Five NYC boroughs:
  - Manhattan
  - Brooklyn
  - Queens
  - Bronx
  - Staten Island

Important variables include:

- `id`
- `name`
- `host_id`
- `host_name`
- `neighbourhood_group`
- `neighbourhood`
- `latitude`
- `longitude`
- `room_type`
- `price`
- `minimum_nights`
- `number_of_reviews`
- `last_review`
- `reviews_per_month`
- `calculated_host_listings_count`
- `availability_365`

---

## Project Structure

```text
project_01_data_workflow/
│
├── data/
│   └── AB_NYC_2019.csv
│
├── outputs/
│   └── figures/
│       ├── figure_1_price_distribution.png
│       ├── figure_2_average_price_borough.png
│       └── figure_3_price_by_room_type.png
│
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── eda.py
│   └── visualizations.py
│
├── notebooks/
│   ├── data_workflow.ipynb
│   └── data_workflow.html
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Environment

The project was developed and tested using Python in a project-specific virtual environment.

The main libraries used include:

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter

The complete Python environment dependencies are documented in:

```text
requirements.txt
```

To install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Workflow

## 1. Setup

The notebook imports the required Python libraries and verifies the Python executable being used by the project environment.

The primary analysis libraries are:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 2. Data Ingestion

The raw CSV file is loaded using Pandas:

```python
df = pd.read_csv("../data/AB_NYC_2019.csv")
```

The dataset was verified to contain:

- **Rows:** 48,895
- **Columns:** 16

The original dataset is retained as the raw source and is not overwritten during cleaning.

---

## 3. Data Quality Assessment

The project performs several data-quality checks before cleaning the dataset.

These checks include:

- Missing-value analysis
- Duplicate-row detection
- Data-type inspection
- Review-field diagnostics

The dataset contains missing values in:

- `last_review`
- `reviews_per_month`
- `name`
- `host_name`

There are no duplicate rows.

A review-specific diagnostic was also performed to determine whether missing review fields were related to listings with zero reviews.

The analysis found:

| Diagnostic | Count |
|---|---:|
| Listings with zero reviews | 10,052 |
| Missing `last_review` | 10,052 |
| Missing `reviews_per_month` | 10,052 |
| Listings with reviews but missing `last_review` | 0 |
| Listings with reviews but missing `reviews_per_month` | 0 |

This indicates a systematic relationship between zero reviews and missing review-related fields.

---

## 4. Data Cleaning

The cleaning logic is implemented as reusable functions in:

```text
src/data_cleaning.py
```

The project uses two main cleaning functions:

- `clean_review_fields()`
- `clean_text_fields()`

### Review Fields

The `last_review` column is converted to a datetime type.

For listings with zero reviews, missing `reviews_per_month` values are replaced with `0`.

The `last_review` values remain missing for listings with no reviews because there is no meaningful review date to assign.

### Text Fields

Missing listing names are replaced with:

```text
Unknown Listing
```

Missing host names are replaced with:

```text
Unknown Host
```

This approach preserves the affected listings rather than deleting them.

The cleaned dataset retains the original dimensions:

```text
Original shape: (48895, 16)
Cleaned shape: (48895, 16)
```

After cleaning:

- Unknown listings: **16**
- Unknown hosts: **21**

The cleaning process therefore preserves all **48,895 observations**.

---

## 5. Exploratory Data Analysis

Reusable exploratory-analysis functions are implemented in:

```text
src/eda.py
```

The `summarize_listings()` function generates:

- Dataset dimensions
- Price statistics
- Room-type counts
- Borough listing counts
- Average price by room type
- Average price by borough

### Price Statistics

The cleaned dataset has the following price statistics:

| Statistic | Value |
|---|---:|
| Count | 48,895 |
| Mean | $152.72 |
| Standard deviation | $240.15 |
| Minimum | $0 |
| 25th percentile | $69 |
| Median | $106 |
| 75th percentile | $175 |
| Maximum | $10,000 |

The difference between the mean and median indicates that listing prices are strongly right-skewed.

---

### Room Type Distribution

The number of listings by room type is:

| Room Type | Listings |
|---|---:|
| Entire home/apt | 25,409 |
| Private room | 22,326 |
| Shared room | 1,160 |

Entire homes or apartments represent the largest room-type category in the dataset.

### Average Price by Room Type

| Room Type | Average Price |
|---|---:|
| Entire home/apt | $211.79 |
| Private room | $89.78 |
| Shared room | $70.13 |

Entire homes or apartments have substantially higher average prices than private and shared rooms.

---

### Listings by Borough

The number of listings by borough is:

| Borough | Listings |
|---|---:|
| Manhattan | 21,661 |
| Brooklyn | 20,104 |
| Queens | 5,666 |
| Bronx | 1,091 |
| Staten Island | 373 |

Manhattan and Brooklyn account for the largest number of listings in the dataset.

### Average Price by Borough

| Borough | Average Price |
|---|---:|
| Manhattan | $196.88 |
| Brooklyn | $124.38 |
| Staten Island | $114.81 |
| Queens | $99.52 |
| Bronx | $87.50 |

Manhattan has the highest average listing price, while the Bronx has the lowest average listing price among the five boroughs.

---

# 6. Visualizations

Reusable visualization functions are implemented in:

```text
src/visualizations.py
```

The project includes three primary visualizations.

---

## Figure 1: Distribution of Airbnb Listing Prices

The first visualization shows the distribution of Airbnb listing prices.

A maximum price of **$500** is used only for visualization so that extreme values do not dominate the plot.

The underlying cleaned dataset remains unchanged.

Output:

```text
outputs/figures/figure_1_price_distribution.png
```

### Interpretation

Airbnb listing prices are concentrated toward the lower end of the displayed range, while a smaller number of expensive listings create a strong right-skewed distribution.

The $500 cutoff is used only to improve visualization readability. Listings above $500 were not removed from the cleaned dataset.

---

## Figure 2: Average Airbnb Price by Borough

The second visualization compares average listing prices across NYC boroughs.

Output:

```text
outputs/figures/figure_2_average_price_borough.png
```

### Interpretation

Average listing prices vary substantially across boroughs.

Manhattan has the highest average listing price at approximately **$196.88 per night**, followed by Brooklyn at approximately **$124.38**.

The Bronx has the lowest average listing price at approximately **$87.50 per night**.

This indicates that geographic location is associated with differences in average listing prices within this dataset.

---

## Figure 3: Airbnb Prices by Room Type

The third visualization uses a boxplot to compare price distributions across room types.

A $500 price cutoff is used only for visualization.

Output:

```text
outputs/figures/figure_3_price_by_room_type.png
```

### Interpretation

Listing prices differ substantially by room type.

Entire homes or apartments generally have the highest prices, while private rooms and shared rooms have lower prices.

The boxplot also shows substantial variation within each room type, indicating that room type alone does not explain all differences in listing prices.

---

# 7. Summary and Key Insights

The analysis identified clear differences in Airbnb listing prices based on room type and borough.

The main findings are:

- The dataset contains **48,895 listings** across five NYC boroughs.
- Entire homes or apartments are the largest room-type category.
- Entire homes or apartments have the highest average price at approximately **$211.79 per night**.
- Private rooms have an average price of approximately **$89.78 per night**.
- Shared rooms have an average price of approximately **$70.13 per night**.
- Manhattan has the highest average listing price at approximately **$196.88 per night**.
- The Bronx has the lowest average listing price at approximately **$87.50 per night**.
- Listing prices are strongly right-skewed.
- A relatively small number of expensive listings can substantially influence the mean.
- Missing review information is systematically associated with listings that have zero reviews.
- The dataset contains substantial variation within both borough and room-type categories.

These findings provide a useful descriptive foundation for future predictive modeling and machine learning work.

---

# 8. Limitations and Responsible Data Practice

## Limitations

This dataset represents Airbnb listings from 2019 and therefore does not necessarily reflect current Airbnb prices, availability, or listing patterns in New York City.

The analysis is descriptive. It identifies associations between listing characteristics, borough, room type, and price but does not establish causal relationships.

The `price` variable also contains substantial variation, including listings with:

```text
price = $0
```

and listings with prices as high as:

```text
price = $10,000
```

Extreme values can influence summary statistics such as the mean.

For visualization purposes, a $500 cutoff is applied to selected plots. This cutoff is not applied to the cleaned dataset and does not remove observations from the analysis dataset.

## Responsible Data Practice

Cleaning decisions can affect analytical results.

Instead of removing listings with missing names or host names, the project replaces those missing values with descriptive placeholders:

```text
Unknown Listing
Unknown Host
```

This preserves the observations and prevents unnecessary data loss.

Review-related missing values were examined before cleaning.

All **10,052 listings with zero reviews** had missing:

- `last_review`
- `reviews_per_month`

No listings with existing reviews were missing these fields.

Based on this pattern:

- Missing `reviews_per_month` values for listings with zero reviews were replaced with `0`.
- Missing `last_review` values were preserved because a listing with no reviews does not have a meaningful review date.

The dataset also represents Airbnb listings rather than the entire housing or lodging market. Therefore, the findings should be interpreted as patterns within the available Airbnb listings and should not be treated as a complete representation of New York City's housing market.

### Future Analysis

Future analysis could:

- Investigate unusual price values in greater detail.
- Compare mean and median prices.
- Examine price distributions using additional statistical methods.
- Investigate neighborhood-level differences.
- Explore relationships between reviews, availability, minimum nights, and price.
- Evaluate alternative approaches for handling extreme observations.

---

# 9. Reproducibility

The project is structured so that the workflow can be rerun using the same dataset, Python environment, and project structure.

Reusable data-processing and analysis functions are stored in:

```text
src/
```

The raw dataset is stored in:

```text
data/
```

Visualization outputs are stored in:

```text
outputs/figures/
```

The complete analysis notebook is stored in:

```text
notebooks/data_workflow.ipynb
```

An HTML version of the completed notebook is also included:

```text
notebooks/data_workflow.html
```

The Python dependencies used by the project are documented in:

```text
requirements.txt
```

To install the dependencies:

```bash
pip install -r requirements.txt
```

The notebook can then be opened and executed using Jupyter:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

The workflow:

1. Loads the raw dataset.
2. Performs data-quality checks.
3. Applies the reusable cleaning functions.
4. Generates exploratory summaries.
5. Creates visualization outputs.
6. Supports interpretation and documentation of the results.

---

# 10. Reusable Project Components

The project separates reusable logic from notebook-specific analysis.

## `src/data_cleaning.py`

Contains reusable functions for:

- Cleaning review-related fields
- Converting review dates to datetime
- Handling missing review-frequency values
- Cleaning missing listing names
- Cleaning missing host names

## `src/eda.py`

Contains reusable exploratory-analysis functions for:

- Dataset summaries
- Price statistics
- Room-type counts
- Borough counts
- Average prices by room type
- Average prices by borough

## `src/visualizations.py`

Contains reusable plotting functions for:

- Price distribution
- Average price by borough
- Price distribution by room type

This structure makes the workflow easier to maintain and reuse in future projects.

---

# 11. Outputs

The project generates the following visualization files:

```text
outputs/
└── figures/
    ├── figure_1_price_distribution.png
    ├── figure_2_average_price_borough.png
    └── figure_3_price_by_room_type.png
```

The completed analysis is available in:

```text
notebooks/data_workflow.ipynb
```

A rendered HTML version is also available in:

```text
notebooks/data_workflow.html
```

---

# 12. Conclusion

This project demonstrates a complete and reproducible data-analysis workflow using the NYC Airbnb Open Data dataset.

The workflow moves from raw data ingestion through data-quality assessment, cleaning, exploratory analysis, visualization, interpretation, and responsible data practices.

The resulting project structure separates reusable Python functions from notebook-based analysis and provides a foundation that can be extended into future machine learning, deep learning, generative AI, and agentic AI projects.