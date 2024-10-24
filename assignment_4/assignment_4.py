from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
app = Dash(__name__)


app.layout = html.Div([
    html.H4('Interactive normal distribution'),
    dcc.Graph(id="graph"),
    html.P("s:"),
    dcc.Slider(id="s", min=1, max=25, value=0, 
               marks={1: '1', 25: '25'}),
    html.P("P(L|Y):"),

    dcc.Slider(id="P_L_given_Y", min=0, max=1, value=1, 
               marks={0: '0', 1: '1'}),
   html.P([
    "P(", 
    html.Span("Y", style={"text-decoration": "overline"}), 
    "):"]),
    dcc.Slider(id="P_Y", min=0, max=1, value=0, 
               marks={0: '0', 1: '1'}),
    html.P([
    "P(",
    html.Span("L", style={"text-decoration": "overline"}),
    " | ",
    html.Span("Y", style={"text-decoration": "overline"}),
    ")"]),
    dcc.Slider(id="P_not_L_given_not_Y", min=0, max=1, value=1, 
               marks={0: '0', 1: '1'}),
])


# @app.callback(
#     Output("graph", "figure"), 
#     Input("mean", "value"), 
#     Input("std", "value"))
# def display_color(mean, std):
#     x_values = [1, 2, 3]  # Example x-axis values
#     y_values = [0.5, 0.8, 0.3]  # Predefined y-values for each bar
#     data = [1, 2, 2]# replace with your own data source
#     # fig = px.histogram(data, range_x=[0, 8], range_y=[0,1])
#     fig = go.Figure([go.Bar(x=x_values, y=y_values)])
#     fig.update_layout(
#         xaxis=dict(range=[0, 8]),
#         yaxis=dict(range=[0, 1]),
#         bargap=0  # No gap between bars
#     )

#     return fig


@app.callback(
    Output("graph", "figure"), 
    Input("s", "value"), 
    Input("P_L_given_Y", "value"),
    Input("P_Y", "value"),
    Input("P_not_L_given_not_Y", "value"),
    )
def display_color(s, P_L_given_Y, P_Y, P_not_L_given_not_Y):
    x_values = [1, 2, 3]  # Example x-axis values
    y_values = [0.5, 0.8, 0.3]  # Predefined y-values for each bar
    data = [1, 2, 2]# replace with your own data source
    # fig = px.histogram(data, range_x=[0, 8], range_y=[0,1])

    P_not_L_given_Y=1-P_L_given_Y
    P_not_Y=1-P_Y

    pi_1_unnormalized=P_Y**4*P_not_L_given_Y**7
    pi_2_unnormalized=P_Y**3*P_not_L_given_Y**6*s*(P_L_given_Y*P_Y+P_not_L_given_not_Y*P_not_Y)
    pi_3_unnormalized=P_Y**2*P_not_L_given_Y**5*s**2*(P_L_given_Y*P_Y+P_not_L_given_not_Y*P_not_Y)**2
    pi_4_unnormalized=P_Y**1*P_not_L_given_Y**4*s**3*(P_L_given_Y*P_Y+P_not_L_given_not_Y*P_not_Y)**3
    pi_5_unnormalized=P_Y**0*P_not_L_given_Y**3*s**4*(P_L_given_Y*P_Y+P_not_L_given_not_Y*P_not_Y)**4
    pi_6_unnormalized=P_Y**0*P_L_given_Y*P_not_L_given_Y**2*s**5*(P_L_given_Y*P_Y+P_not_L_given_not_Y*P_not_Y)**4
    pi_7_unnormalized=P_Y**0*P_L_given_Y**2*P_not_L_given_Y**1*s**6*(P_L_given_Y*P_Y+P_not_L_given_not_Y*P_not_Y)**4
    pi_8_unnormalized=P_Y**0*P_L_given_Y**3*P_not_L_given_Y**0*s**7*(P_L_given_Y*P_Y+P_not_L_given_not_Y*P_not_Y)**4

# Sum of unnormalized π'_i values
    sum_of_pi_unnormalized = (pi_1_unnormalized + pi_2_unnormalized + pi_3_unnormalized +
                            pi_4_unnormalized + pi_5_unnormalized + pi_6_unnormalized +
                            pi_7_unnormalized + pi_8_unnormalized)
        
    print(sum_of_pi_unnormalized)
    print("P_Y is", P_Y)
    print("P_not_L_given_Y is", P_not_L_given_Y)
    print("P_L_given_Y is", P_L_given_Y)
    print("P_not_L_given_not_Y is", P_not_L_given_not_Y)
    print("P_not_Y is", P_not_Y)
# Calculate α
    alpha = 1 / sum_of_pi_unnormalized

# Now calculate normalized π_i values
    pi_1 = alpha * pi_1_unnormalized
    pi_2 = alpha * pi_2_unnormalized
    pi_3 = alpha * pi_3_unnormalized
    pi_4 = alpha * pi_4_unnormalized
    pi_5 = alpha * pi_5_unnormalized
    pi_6 = alpha * pi_6_unnormalized
    pi_7 = alpha * pi_7_unnormalized
    pi_8 = alpha * pi_8_unnormalized
    x_values = [1, 2, 3, 4, 5, 6, 7, 8]
    y_values = [pi_1, pi_2, pi_3, pi_4, pi_5, pi_6, pi_7, pi_8]
    fig = go.Figure([go.Bar(x=x_values, y=y_values)])
    fig.update_layout(
        xaxis=dict(range=[0, 8]),
        yaxis=dict(range=[0, 1]),
        bargap=0  # No gap between bars
    )
    fig.add_shape(
    type="line",
    x0=4.5, y0=0, x1=4.5, y1=1,  # The vertical line from y=0 to y=1 at x=4
    line=dict(
        color="red",  # Color of the line
        width=2,
        dash="dot"  # Dotted line style
    )
)
    


    return fig

def update_slider_values(s, P_L_given_Y, P_Y, P_not_L_given_not_Y):
    # Return the current values as a formatted string in a div
    return html.Div([
        html.P(f"Current value of s: {s}"),
        html.P(f"Current value of P(L|Y): {P_L_given_Y}"),
        html.P(f"Current value of P(Ȳ): {P_Y}"),
        html.P(f"Current value of P(Ƚ|Ȳ): {P_not_L_given_not_Y}")
    ])

app.run_server(debug=True)