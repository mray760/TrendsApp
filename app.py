from dash import Dash, html, dcc, page_container
import dash
import plotly.express as px

# Initialize Dash app
app = Dash(__name__, use_pages=True,pages_folder='pages')

# App layout with navigation and multi-page support
app.layout = html.Div([
    html.H1("Trends Dashboard", style={'textAlign': 'center'}),

    # Links to navigate between pages
    html.Div([
        dcc.Link('Home', href='/'),
        html.Br(),
        dcc.Link('Treasury Rates', href='/treasury_curve'),
        html.Br(),
        dcc.Link('EPS', href='/EPS')
    ], style={'textAlign': 'center', 'margin': '20px'}),

    # Container to render pages
    dcc.Location(id='url', refresh=False),
    dash.page_container

])

if __name__ == '__main__':
    app.run_server(debug=True)
