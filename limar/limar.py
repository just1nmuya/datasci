import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from dash import no_update
import datetime as dt

app = dash.Dash(__name__)

app.config.suppress_callback_exceptions = True

expense_data = pd.read_csv("Limar Soya 2024 Finacial Record.csv")

expense_data["amount"] = expense_data["amount"].str.replace(",", "")

expense_data["amount"] = pd.to_numeric(expense_data["amount"], errors="coerce")

expense_data["amount"] = expense_data["amount"].astype(int)

expense_data["Month"] = pd.to_datetime(expense_data["date"]).dt.month_name()
# expense_data["Year"] = pd.to_datetime(expense_data["date"]).dt.year
month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
expense_data["Month"] = pd.Categorical(
    expense_data["Month"], categories=month_order, ordered=True
)

app.layout = html.Div(
    children=[
        html.H1(
            "Limar Expenses Dashboard",
            style={"textAlign": "center", "color": "#00000", "font-size": 26},
        ),
        html.Div(
            [
                html.H2("Select Expense", style={"margin-right": "2em"}),
                dcc.Dropdown(
                    expense_data.particulars.unique(),
                    value="Transport Expense",
                    id="month",
                ),
            ]
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div([], id="plot1"),
                        html.Div([], id="plot2"),
                    ]
                )
            ]
        ),
    ]
)


@app.callback(
    [
        Output(component_id="plot1", component_property="children"),
        Output(component_id="plot2", component_property="children"),
    ],
    [
        # Input(component_id="month", component_property="value"),
        Input(component_id="month", component_property="value"),
    ],
)
def amount_month(expense_entered):
    df = expense_data[expense_data["particulars"] == expense_entered]

    data1 = df.groupby(["Month", "particulars"])["amount"].sum().reset_index()
    fig1 = px.pie(
        data1,
        values="amount",
        names="Month",
        title=" Monthly Total Expenses",
    )

    data2 = df.groupby(["Month", "particulars"])["amount"].sum().reset_index()
    fig2 = px.bar(
        data2,
        x="Month",
        y="amount",
        title=" Monthly Total Expenses ",
    )

    return [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
    ]


if __name__ == "__main__":
    app.run_server()
