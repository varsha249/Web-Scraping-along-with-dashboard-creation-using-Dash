# Jumia Smartphone Dashboard with Dash and Plotly

The code creates an interactive dashboard using **Dash** and **Plotly** to visualize and analyze smartphone data scraped from Jumia. 

---

## **1. Import Libraries**
```python
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
```
- **`pandas`**: Used for loading and cleaning the data.
- **`Dash`**: A web framework for creating interactive dashboards.
- **`plotly.express`**: A library for creating visualizations like scatter plots and histograms.

---

## **2. Load and Clean the Dataset**
### **Load Data Function**
```python
def load_data():
    df = pd.read_csv("jumia_enhanced_with_ratings.csv")
    # Clean the Price column
    df["Price"] = df["Price"].str.replace("KSh", "").str.replace(",", "").str.strip()
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    # Clean the Rating column
    df["Rating"] = df["Rating"].str.extract(r"(\d+\.\d+)").astype(float)
    # Drop rows with missing values
    df = df.dropna(subset=["Price", "Rating"])
    return df
```
1. **Load CSV**: Reads the scraped CSV file (`jumia_enhanced_with_ratings.csv`) into a Pandas DataFrame.
2. **Clean Price**:
   - Removes `"KSh"` and commas from the `Price` column.
   - Converts the cleaned `Price` to numeric.
3. **Clean Rating**:
   - Extracts numeric ratings from strings (e.g., `"4.4 out of 5"`).
   - Converts ratings to float.
4. **Drop Missing Values**: Removes rows where `Price` or `Rating` is `NaN`.

### **Load Data**
```python
df = load_data()
```
- Loads and cleans the dataset into a DataFrame.

---

## **3. Initialize Dash App**
```python
app = Dash(__name__)
```
- Initializes the Dash application.

---

## **4. Define App Layout**
```python
app.layout = html.Div([
    html.H1("Jumia Smartphone Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Label("Price Range (KSh):"),
        dcc.RangeSlider(
            id="price-slider",
            min=int(df["Price"].min()),
            max=int(df["Price"].max()),
            step=5000,
            value=[int(df["Price"].min()), int(df["Price"].max())],
            marks={i: f"KSh {i}" for i in range(0, int(df["Price"].max()) + 1, 5000)}
        ),
        html.Label("Minimum Rating:"),
        dcc.Dropdown(
            id="rating-dropdown",
            options=[
                {"label": "All Ratings", "value": 0},
                {"label": "4.0 and above", "value": 4.0},
                {"label": "4.5 and above", "value": 4.5},
                {"label": "5.0 only", "value": 5.0},
            ],
            value=0,
            clearable=False
        ),
    ], style={"width": "100%", "margin": "auto"}),

    html.Div([
        dcc.Graph(id="price-distribution"),
        dcc.Graph(id="price-vs-rating"),
        html.Div(id="top-products-table")
    ]),
])
```

### **Layout Components**
1. **Price Range Slider**:
   - Allows users to filter smartphones by price range.
   - Dynamically adjusts min and max values based on the dataset.
   - Displays price ticks at intervals of `5000 KSh`.
2. **Rating Dropdown**:
   - Allows users to filter smartphones by minimum rating.
   - Options include "All Ratings," "4.0 and above," "4.5 and above," and "5.0 only."
3. **Graphs**:
   - **Price Distribution**: A histogram showing the frequency of smartphones in different price ranges.
   - **Price vs. Rating Scatter Plot**: Displays the relationship between price and rating.
4. **Top Products Table**:
   - A table displaying the top 10 products with the highest ratings.

---

## **5. Callback for Interactivity**
### **Define Callback**
```python
@app.callback(
    [
        Output("price-distribution", "figure"),
        Output("price-vs-rating", "figure"),
        Output("top-products-table", "children"),
    ],
    [
        Input("price-slider", "value"),
        Input("rating-dropdown", "value"),
    ]
)
def update_dashboard(price_range, min_rating):
    ...
```
- Defines a callback function to update graphs and the table when the user changes the filters.

---

### **Filter Data Based on User Inputs**
```python
filtered_df = df[df["Price"].between(price_range[0], price_range[1])]
if min_rating > 0:
    filtered_df = filtered_df[filtered_df["Rating"] >= min_rating]
```
- Filters the dataset based on:
  1. **Price Range**: Products within the selected range.
  2. **Minimum Rating**: Products with ratings greater than or equal to the selected value.

---

### **Generate Visualizations**
1. **Price Distribution**
```python
price_hist = px.histogram(
    filtered_df,
    x="Price",
    nbins=30,
    title="Price Distribution of Smartphones",
    labels={"Price": "Price (KSh)"},
)
```
- Creates a histogram to show the distribution of smartphone prices.

2. **Price vs. Rating Scatter Plot**
```python
scatter_fig = px.scatter(
    filtered_df,
    x="Price",
    y="Rating",
    color="Rating",
    title="Price vs. Rating",
    labels={"Price": "Price (KSh)", "Rating": "Rating"},
    hover_data=["Product Name"]
)
```
- Displays the relationship between price and rating with:
  - **Color-coded Ratings**.
  - **Hover Data**: Product names.

---

### **Generate Top Products Table**
```python
top_products = filtered_df.sort_values(by="Rating", ascending=False).head(100)
table_html = html.Table([
    html.Thead(html.Tr([html.Th("Product Name"), html.Th("Price"), html.Th("Rating")])),
    html.Tbody([
        html.Tr([
            html.Td(product["Product Name"]),
            html.Td(f"KSh {product['Price']:,}"),
            html.Td(f"{product['Rating']}")
        ]) for _, product in top_products.iterrows()
    ])
])
```
- Sorts products by `Rating` in descending order.
- Displays the top 10 products with:
  - Product Name
  - Price (formatted with commas)
  - Rating

---

## **6. Run the App**
```python
if __name__ == "__main__":
    app.run(debug=True)
```
- Runs the Dash application locally with debug mode enabled.

---

## **Summary**
This dashboard allows users to:
1. Filter smartphones by price range and minimum rating.
2. Visualize price distribution and the relationship between price and rating.
3. View a table of the top 10 smartphones with the highest ratings.

