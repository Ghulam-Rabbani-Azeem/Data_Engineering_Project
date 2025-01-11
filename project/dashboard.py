import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc  # Using Bootstrap for styling
import plotly.express as px
import pandas as pd
import sqlite3

# Database path
DB_PATH = "./data/renewable_energy.sqlite3"

# Load data from SQLite database
with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql("SELECT * FROM renewable_energy", conn)

# Display sample of the data (You can uncomment this line to visually check it)
# print(df.head())

# Initialize Dash app with Bootstrap styling
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Renewable Energy Impact Dashboard"
)

# Dropdown options
state_options = [{"label": state, "value": state} for state in df["state-name"].unique()]
sector_options = [{"label": sector, "value": sector} for sector in df["sector-name"].unique()]

# Dashboard Layout
app.layout = dbc.Container(
    [
        # Header Section
        html.H1(
            "Impact of Renewable Energy Adoption on U.S. Carbon Emissions",
            style={'textAlign': 'center', 'margin-top': '20px'}
        ),
        html.P(
            "Explore the relationship between renewable energy adoption and carbon emissions in the U.S.",
            style={'textAlign': 'center', 'margin-bottom': '30px'}
        ),

        # KPI Section
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4("Total Renewable Energy Usage"),
                            html.H2(id="kpi-renewable", style={"color": "green"})
                        ]),
                        className="text-center"
                    ),
                    width=4
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4("Years of Data"),
                            html.H2(id="kpi-years")
                        ]),
                        className="text-center"
                    ),
                    width=4
                ),
            ],
            className="mb-4"
        ),

        # Dropdown Filters Section
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="state-dropdown",
                        options=state_options,
                        placeholder="Select a state",
                        value=None,
                        multi=True
                    ),
                    width=6
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="sector-dropdown",
                        options=sector_options,
                        placeholder="Select a sector",
                        value=None
                    ),
                    width=6
                )
            ],
            className="mb-4"
        ),

        # Graph Section
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="energy-trend-graph"), width=12),
                dbc.Col(dcc.Graph(id="top-states-bar"), width=12),
                dbc.Col(dcc.Graph(id="sector-pie-chart"), width=12),
                dbc.Col(dcc.Graph(id="renewable-energy-yearwise"), width=12)  # Added Year-wise Renewable Energy graph
            ]
        )
    ],
    fluid=True
)

# Callbacks

# Update KPIs
@app.callback(
    [Output("kpi-renewable", "children"),
     Output("kpi-years", "children")],
    [Input("state-dropdown", "value"), Input("sector-dropdown", "value")]
)
def update_kpis(selected_states, selected_sector):
    filtered_df = df
    if selected_states:
        filtered_df = filtered_df[filtered_df["state-name"].isin(selected_states)]
    if selected_sector:
        filtered_df = filtered_df[filtered_df["sector-name"] == selected_sector]

    # Calculate Total Renewable Energy Usage
    total_energy = filtered_df["value"].sum()

    years_of_data = filtered_df["year"].nunique()

    # Return total values for KPIs
    return f"{total_energy:.2f} GWh", f"{years_of_data} years"

# Update Renewable Energy Usage Trends Graph
@app.callback(
    Output("energy-trend-graph", "figure"),
    [Input("state-dropdown", "value"), Input("sector-dropdown", "value")]
)
def update_energy_trend_graph(selected_states, selected_sector):
    filtered_df = df
    if selected_states:
        filtered_df = filtered_df[filtered_df["state-name"].isin(selected_states)]
    if selected_sector:
        filtered_df = filtered_df[filtered_df["sector-name"] == selected_sector]

    fig = px.line(
        filtered_df,
        x="year",
        y="value",
        color="fuel-name",
        title="Renewable Energy Usage Trends",
        labels={"value": "Energy Consumption (GWh)", "year": "Year"}
    )
    fig.update_layout(legend_title_text="Fuel Type")
    return fig

# Update Top States Bar Graph
@app.callback(
    Output("top-states-bar", "figure"),
    [Input("state-dropdown", "value")]
)
def update_top_states_bar(selected_states):
    filtered_df = df
    if selected_states:
        filtered_df = filtered_df[filtered_df["state-name"].isin(selected_states)]

    state_wise_energy = filtered_df.groupby("state-name")["value"].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(
        state_wise_energy.head(10),
        x="value",
        y="state-name",
        orientation="h",
        title="Top 10 States by Renewable Energy Usage",
        labels={"value": "Energy Consumption (GWh)", "state-name": "State"}
    )
    return fig

# Update Sector-Wise Pie Chart
@app.callback(
    Output("sector-pie-chart", "figure"),
    [Input("sector-dropdown", "value")]
)
def update_sector_pie_chart(selected_sector):
    filtered_df = df
    if selected_sector:
        filtered_df = filtered_df[filtered_df["sector-name"] == selected_sector]

    sector_wise_energy = filtered_df.groupby("sector-name")["value"].sum().reset_index()
    fig = px.pie(
        sector_wise_energy,
        values="value",
        names="sector-name",
        title="Renewable Energy Usage by Sector",
    )
    return fig

# Update Renewable Energy Usage Year-wise Graph
@app.callback(
    Output("renewable-energy-yearwise", "figure"),
    [Input("state-dropdown", "value"), Input("sector-dropdown", "value")]
)
def update_renewable_energy_yearwise(selected_states, selected_sector):
    filtered_df = df
    if selected_states:
        filtered_df = filtered_df[filtered_df["state-name"].isin(selected_states)]
    if selected_sector:
        filtered_df = filtered_df[filtered_df["sector-name"] == selected_sector]

    # Aggregate total renewable energy usage by year
    renewable_energy_by_year = filtered_df.groupby('year')['value'].sum().reset_index()

    # Create the graph using Plotly
    fig = px.bar(
        renewable_energy_by_year,
        x="year",
        y="value",
        title="Total Renewable Energy Usage Year-wise",
        labels={"year": "Year", "value": "Energy Consumption (GWh)"},
    )
    return fig

# Run the application
if __name__ == "__main__":
    app.run_server(debug=True)
