
import dash

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


app = dash.Dash()
server = app.server
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(children="Odds for team1", style={"margin-left": "750px", 'textAlign': 'left'}, className="menu-title"),
                dcc.Input(
                    id='input-x',
                    type='number',
                    value=0,
                    min=0, max=50,step = 0.01,
                    placeholder="Player1 odds",
                     style={"margin-left": "750px", 'textAlign': 'center', 'width' : '4%' },
               ),
            ]
        ),
      #  html.Br(),
        html.Div("` ", style={"color": "white", "font-size": '1%'}),

        html.Div(
            children=[
                html.Div(children="Odds for draw", style={"margin-left": "750px", 'textAlign': 'left'}, className="menu-title"),
                dcc.Input(
                    id='input-y',
                    type='number',
                    value=0,
                    min=0, max=50,step = 0.01,
                    placeholder="Draw odds",
                    style={"margin-left": "750px", 'textAlign': 'center', 'width' : '4%' },
                ),
            ],
        ),
       # html.Br(),
        html.Div("` ", style={ "color": "white", "font-size": '50%'}),

        html.Div(
            children=[
                html.Div(style={"margin-left": "1000px", 'textAlign': 'left'},
                    children="Odds for team2",
                    className="menu-title"
                    ),
                dcc.Input(
                    id='input-z',
                    type='number',
                    value=0,
                    min=0, max=50,step = 0.01,
                    placeholder="Odds for player2",
                    style={"margin-left": "750px", 'textAlign': 'center', 'width' : '4%' },
                ),


            ]
        ),
        html.Div("` ",style={"color": "white", "font-size" : '5%'}),
     #   html.Br(   style= {"height": "1%" } ),
        html.Div(
                children=[
                    html.Div(style={"margin-left": "750px", 'textAlign': 'left'},
                             children="   Total budget",
                             className="menu-title"
                             ),
                    dcc.Input(
                        id='input-a',
                        type='number',
                        value=15,
                        min=0, max=1000.0001,step = 0.1,
                        placeholder="Total budget",
                        style={"margin-left": "750px", 'textAlign': 'center', 'width' : '4%' },
                    )
                ]
        ),
#        html.Br(),
        html.Div("` ", style={"color": "white", "font-size": '5%'}),

        html.Button('Submit',  id='submit_button', n_clicks=0, style={"font-size" : '90%', "margin-left": "750px", 'textAlign': 'center' , 'width' : '4%' },),

        html.Hr(),
        html.Div(id='result', style={"font-size" : '120%', "margin-left": "600px", 'textAlign': 'left' , 'width' : '50%' },),#style={"margin-left": "700px", 'textAlign': 'center'},),
        html.Div(id='result1', style={"font-size": '120%', "margin-left": "600px", 'textAlign': 'left', 'width': '50%'}, ),
        html.Div(id='result2', style={"font-size": '120%', "margin-left": "600px", 'textAlign': 'left', 'width': '50%'}, ),
        html.Div(id='result3', style={"font-size": '120%', "margin-left": "600px", 'textAlign': 'left', 'width': '50%'}, )
        # style={"margin-left": "700px", 'textAlign': 'center'},),


    ],

    className="menu",
)

@app.callback(
    [dash.dependencies.Output('result', 'children'),
     dash.dependencies.Output('result1', 'children'),
     dash.dependencies.Output('result2', 'children'),
     dash.dependencies.Output('result3', 'children')],
    [dash.dependencies.Input('submit_button', 'n_clicks')],
     state= [State(component_id='input-x', component_property='value'),
    State(component_id='input-y', component_property='value'),
             State(component_id='input-z', component_property='value'),
             State(component_id='input-a', component_property='value')
             ],
)

def update_result(n_clicks,x, y,z,a ):
    if n_clicks <1 :
        raise PreventUpdate
        return " "

    if  x == 0 or y ==0 or z ==0 :
       return [" Please enter a valid odd",'','','']

#x team1  y draw z team 2

    elif z> x*3 :
        #win profit by draw
        betonteam1 = round(a / x,2)
        betondraw = round(a - betonteam1,2)
        #win profit by Team1
        betondrawprofiton1 = round(a / y,2)
        betonteam1profiton1 = round(a - betondrawprofiton1,2)

        return ["Option1 : {} on Team1, {} on draw, 0 on Team2".format(betonteam1,betondraw),
                "Option2 : {} on Team1, {} on draw, 0 on Team2".format(betonteam1profiton1,betondrawprofiton1),
                "Option3 : No bets recommended",
                ""]
    elif abs(x-z)<2 :
        #win profit by draw

        return ["No bets recommended" ,'','','']

    elif x> z*3 :
        #win profit by draw
        betonteam3 = round(a / x,2)
        betondraw = round(a - betonteam3,2)
        #win profit by Team1
        betondrawprofiton3 = round(a / y,2)
        betonteam3profiton3 = round(a - betondrawprofiton3,2)

        return ["Option1 : {} on Team2, {} on draw, 0 on Team1".format(betonteam3,betondraw),
                "Option2 : {} on Team2, {} on draw, 0 on Team1".format(betonteam3profiton3,betondrawprofiton3),
                "Option3 : No bets recommended",
                ""]

    else:
        return ["No bets recommended", '', '', '']


if __name__ == "__main__":
    app.run_server(debug=True)



