import dash
from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px

to_date = pd.to_datetime('10/11/24')
from_date = pd.to_datetime('10/01/24')

df = pd.read_csv('/Users/mattray/Desktop/Python/Trends App/daily-treasury-rates.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')



dash.register_page(__name__,path = '/treasury_curve', name= 'Treasury Rates')

layout = html.Div([
    html.H1("Daily Treasury Rates Dashboard", style={'textAlign': 'center'}),

    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=from_date,
        end_date=to_date,
        display_format='MM/DD/YYYY'
    ),

    dcc.Dropdown(
        id= 'mty-picker',
        options= [{'label': col, 'value': col} for col in df.columns[1:]],
        value= [df.columns[1]],
        multi = True
    ),

    dcc.Graph(id='line-chart'),  # Placeholder for the chart
])

# Callback to update the chart based on date range selection
@callback(
    Output('line-chart', 'figure'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date'),
    Input('mty-picker', 'value')
)
def update_chart(start_date, end_date, selected_rates):
    # Filter the DataFrame based on selected dates
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Create the line chart
    fig = px.line(
        filtered_df,
        x='Date',
        y= selected_rates,  # Plot all columns except 'Date'
        title='Daily Treasury Rates',
        markers=True
    )

    fig.update_layout(xaxis_title='Date', yaxis_title='Rate (%)')
    return fig
