import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Loading dataset
def load_data():
    df = pd.read_csv("jumia_enhanced_with_ratings.csv")
    # Cleaning Price column
    df["Price"] = df["Price"].str.replace("KSh", "").str.replace(",", "").str.strip()
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    # Cleaning Rating column
    df["Rating"] = df["Rating"].str.extract(r"(\d+\.\d+)").astype(float)
    # Dropping rows with missing values
    df = df.dropna(subset=["Price", "Rating"])
    return df

# Loading data
df = load_data()

# Initializing Dash app
app = Dash(__name__)

# App Layout
app.layout = html.Div([
    html.H1("Jumia Smartphone Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Label("Price Range (KSh):"),
        dcc.RangeSlider(
            id="price-slider",
            min=int(df["Price"].min()),
            max=int(df["Price"].max()),
            step=1000,
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
    ], style={"width": "50%", "margin": "auto"}),

    html.Div([
        dcc.Graph(id="price-distribution"),
        dcc.Graph(id="price-vs-rating"),
        html.Div(id="top-products-table")
    ]),
])

# Callback for updating graphs and table based on filters
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
    # Filtering data based on user inputs
    filtered_df = df[df["Price"].between(price_range[0], price_range[1])]
    if min_rating > 0:
        filtered_df = filtered_df[filtered_df["Rating"] >= min_rating]

    # Price Distribution
    price_hist = px.histogram(
        filtered_df,
        x="Price",
        nbins=30,
        title="Price Distribution of Smartphones",
        labels={"Price": "Price (KSh)"},
    )

    # Price vs. Rating Scatter Plot
    scatter_fig = px.scatter(
        filtered_df,
        x="Price",
        y="Rating",
        color="Rating",
        title="Price vs. Rating",
        labels={"Price": "Price (KSh)", "Rating": "Rating"},
        hover_data=["Product Name"]
    )

    # Top Products Table
    top_products = filtered_df.sort_values(by="Rating", ascending=False).head(10)
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

    return price_hist, scatter_fig, table_html

# Running the app
if __name__ == "__main__":
    app.run_server(debug=True)
