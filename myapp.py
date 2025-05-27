from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = px.data.gapminder()

countries = df['country'].unique()


# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'  # Значение по умолчанию
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback for dynamic updates
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    # Фильтруем данные по выбранной стране
    filtered_df = df[df['country'] == selected_country]

    # Создаём график с годом по оси X и gdpPercap по оси Y
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f'GDP per Capita Growth for {selected_country}'
    )

    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 
