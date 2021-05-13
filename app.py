import dash
import dash_core_components as dcc
import dash_html_components as html

#import libs for processing>
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Output, Input, State

# import data

from data import df , df2 , df1
# define the app


# import data

from data import df , df2 , df1
# define the app



# get the key values from the env
import os
from dotenv import load_dotenv

load_dotenv()

MYKEY = os.getenv('KEY')
DEBUG = os.getenv('DEBUG')
print(MYKEY)
bootstrap =  "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css"
app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[bootstrap],
)


app.title ="steve's Covid Dashboard"
app.layout = html.Div([
# title
    html.Div([
        html.Div([
            html.Div([
                html.H3("Covid 19 " ,
                style={
                    "margin-bottom":"8px" ,"color":"white",
                }
                ),
                html.H5("Tracking covid 19 casess " , style ={"margin-top":"8px" , "color":"white"})
            ] , className='myTracker'),
        ] ,
        className = 'col-md-7 text-center' ,  id ='title1'),

        html.Div([
            html.H6(f'Last Updated  {df2.date.iloc[-1].strftime("%B  %d , %Y")}' , style={"color":"orange"} , className="float-end"),
            html.H6("More Info.......   +254798355947" , style={"color":"white" , "font-weight":"bold"})
            ],
        className = "col-md-4 float-right", id ='title2'
        ),

    ] , className='row  app-header'),
    # title end

    # start of information one cards
    html.Div([
        html.Div([
        #global cases
        html.H6(children = "GLobal Cases" ,
            style ={
                "textAlign":"center",
                "color":"white",
            }
        ),

        html.P(f"{df1['confirmed'].iloc[-1]:,.0f}",
            style ={
            "textAlign":"center",
            "color":"orange",
            }
            ,className ='data_mid'
        ),
        html.P('new  ' + f"{df1['confirmed'].iloc[-1]-  df1['confirmed'].iloc[-2]:,.0f}  "
        + '(' + str(round(((df1['confirmed'].iloc[-1] -df1['confirmed'].iloc[-2])/
        df1['confirmed'].iloc[-1])*100 , 3)) +'%',
            style={
            "textAlign":"center",
            'color':'orange',
            'margin-top':'-12px',
            }
            ,className ='data_end'
        ),
        ] , className="col-md-3 col-sm-6  col-lg-3  global_cases"),#end of cases

        #global deaths
        html.Div([
            html.H6(children = "GLobal Deaths" ,
                style ={
                    "textAlign":"center",
                    "color":"white",
                }
            ),
        html.P(f"{df1['deaths'].iloc[-1]:,.0f}",
            style ={
                "textAlign":"center",
                "color":"#dd1e33",
            }
            ,className ='data_mid'
        ),

        html.P('new  ' +f"{df1['deaths'].iloc[-1]-  df1['deaths'].iloc[-2]:,.0f}  "
        + '(' + str(round(((df1['deaths'].iloc[-1] -df1['deaths'].iloc[-2])/
        df1['deaths'].iloc[-1])*100 , 3)) +'%',
            style={
                "textAlign":"center",
                'color':'#dd1e23',
                'margin-top':'-12px',
            } , className ='data_end'
        ) , ],
        className="col-md-3 col-sm-6 col-lg-3 global_deaths"
        ),
        # end of global deaths

        #global recoiverey
        html.Div([
            html.H6(children = "GLobal recovered" ,
                style ={
                    "textAlign":"center",
                    "color":"white",
                }
            ),
        html.P(f"{df1['recovery'].iloc[-1]:,.0f}",
            style ={
                "textAlign":"center",
                "color":"green",
            }
            ,className ='data_mid'
        ),

        html.P('new  ' + f"{df1['recovery'].iloc[-1]-  df1['recovery'].iloc[-2]:,.0f}  "
        + '(' + str(round(((df1['recovery'].iloc[-1] -df1['recovery'].iloc[-2])/
        df1['recovery'].iloc[-1])*100 , 3)) +'%',
            style={
                "textAlign":"center",
                'color':'green',
                'margin-top':'-12px',
            }
            ,className ='data_end'
        )],
        className="col-md-3 col-sm-6 col-lg-3 global_recovery"
        ),
        # end of global recovery


        #global active
        html.Div([
            html.H6(children = "GLobal Active" ,
                style ={
                    "textAlign":"center",
                    "color":"white",
                }
            ),
        html.P(f"{df1['active'].iloc[-1]:,.0f}",
        style ={
            "textAlign":"center",
            "color":"#e55467",
        }
        ,className ='data_mid'
        ),

        html.P('new  ' + f"{df1['active'].iloc[-1]-  df1['active'].iloc[-2]:,.0f}  "
        + '(' + str(round(((df1['active'].iloc[-1] -df1['active'].iloc[-2])/
        df1['active'].iloc[-1])*100 , 3)) +'%',
            style={
                "textAlign":"center",
                'color':'#e55467',
                'margin-top':'-12px',
            }
            ,className ='data_end'
        )],
        className="col-md-3 col-sm-6  col-lg-3 global_active"
        ),
        # end of global active

        ] , className='row  infor1'),
        #end gloabl infor

        #design for the second part of the body..with graphs
        html.Div([

        #here we will be creating graph placeholders
            html.Div([
                html.P('selecyt Country  :'  , className = 'country_placeholder' , style={"color":"white"}),
                dcc.Dropdown(
                    id='selected_country',
                    multi =False,
                    clearable =True,
                    value = "Kenya",
                    placeholder ="Select countrie",
                    options =[
                        {"label":country , "value":country}
                         for country in df2['Country'].unique()
                    ],
                    className ='dash_overview'
                ),

                html.P('New Cases '  + '  ' + ' '  + str(df2['date'].iloc[-1].strftime('%B %d %Y')) + ' ' , className = 'country_placeholder' , style={"color":"#fff" , 'text-align':'center'}),

                #graph confirmed
                dcc.Graph(id ='confirmed' , config ={'displayModeBar':False} , className ='dash_overview' ),

                #graph deaths
                dcc.Graph(id ='deaths' , config ={'displayModeBar':False} , className ='dash_overview'),

                #graph recoverd
                dcc.Graph(id ='recovered' , config ={'displayModeBar':False} , className ='dash_overview'),

                #graph actice
                dcc.Graph(id ='active' , config ={'displayModeBar':False} , className ='dash_overview'),
            ],
            className= 'col-md-3 col-sm-6 col-lg-3  options_container ' , id ='options_container'
            ),


            # dounot chart.
            html.Div([
                dcc.Graph(id= 'pie_chart' ,config ={'displayModeBar':'hover'})
            ],className ='col-md-3  col-sm-6 col-lg-3 options_container'
            ),

            #line and bar graph
            html.Div([
                dcc.Graph(id ='line_chart')],
                className = 'options_container col-md-5 col-lg-5 col-sm-12'
                ),

        ] , className="row infor2"),

        html.Div([
        html.Br(),
        html.Br(),
        ], className='row  '),
        #map graph
        html.Div([
            html.Div([dcc.Graph(id ='map')],
                className = '  col-12 col-md-12 col-sm-12 col-lg-12'
                ),
                ],className='row infor3'),


        html.Div([
        html.Footer([
        html.P(f"Designed by  steve  ©   2021" , className='footer_body'),
        html.Small(" COntact:   stiveckamash@gmail.com  "),
        html.A(html.Button('Website', className=''),href='http://stivec.herokuapp.com/'),
        ]),
        ], className='footer'),


    ] , className ="MainBody")













# callbacks and updates for the graphs and values
@app.callback(
    Output('confirmed' , 'figure'),
    [Input('selected_country' , 'value')]
)
def update_graph(selected_country):
    value_cases = df2[df2['Country'] == selected_country]['confirmed'].iloc[-1] - df2[df2['Country'] == selected_country]['confirmed'].iloc[-2]
    change_cases = df2[df2['Country'] == selected_country]['confirmed'].iloc[-2] - df2[df2['Country'] == selected_country]['confirmed'].iloc[-3]


    return {
        'data':[ go.Indicator(
            mode= 'number+delta',
            value = value_cases,
            delta ={
                'reference':change_cases,
                'position':'right',
                'valueformat':'.9',
                'relative':False,
                'font':{'size':15}
            },
            number={'valueformat': '.' , 'font':{'size':20},},
            domain={'y':[0,1] , 'x':[0,1]}
            )
        ],
        'layout':go.Layout(
            title={
                'text':'New Confirmed',
                'y':1,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            font=dict(color ='orange'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            # height=50,
            # width =100
        ),
    }

@app.callback(
    Output('deaths' , 'figure'),
    [Input('selected_country' , 'value')]
)

def update_graph(selected_country):
    value_deaths = df2[df2['Country'] == selected_country]['deaths'].iloc[-1] - df2[df2['Country'] == selected_country]['deaths'].iloc[-2]
    change_deaths = df2[df2['Country'] == selected_country]['deaths'].iloc[-2] - df2[df2['Country'] == selected_country]['deaths'].iloc[-3]


    return {
        'data':[ go.Indicator(
            mode= 'number+delta',
            value = value_deaths,
            delta ={
                'reference':change_deaths,
                'position':'right',
                'valueformat':'.9',
                'relative':False,
                'font':{'size':15}
            },
            number={'valueformat': '.' , 'font':{'size':20},},
            domain={'y':[0,1] , 'x':[0,1]}
            )
        ],
        'layout':go.Layout(
            title={
                'text':'New detahts',
                'y':1,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            font=dict(color ='orange'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            # height=100,
            # width =50
        ),
    }

@app.callback(
    Output('recovered' , 'figure'),
    [Input('selected_country' , 'value')]
)
def update_graph(selected_country):
    value_recover = df2[df2['Country'] == selected_country]['recovery'].iloc[-1] - df2[df2['Country'] == selected_country]['recovery'].iloc[-2]
    change_recover = df2[df2['Country'] == selected_country]['recovery'].iloc[-2] - df2[df2['Country'] == selected_country]['recovery'].iloc[-3]


    return {
        'data':[ go.Indicator(
            mode= 'number+delta',
            value = value_recover,
            delta ={
                'reference':change_recover,
                'position':'right',
                'valueformat':'.9',
                'relative':False,
                'font':{'size':15}
            },
            number={'valueformat': '.' , 'font':{'size':20},},
            domain={'y':[0,1] , 'x':[0,1]}
            )
        ],
        'layout':go.Layout(
            title={
                'text':'New Recovery',
                'y':1,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            font=dict(color ='orange'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            # height=50,
            # width =100
        ),
    }

@app.callback(
    Output('active' , 'figure'),
    [Input('selected_country' , 'value')]
)
def update_graph(selected_country):
    value_active = df2[df2['Country'] == selected_country]['active'].iloc[-1] - df2[df2['Country'] == selected_country]['active'].iloc[-2]
    change_active = df2[df2['Country'] == selected_country]['active'].iloc[-2] - df2[df2['Country'] == selected_country]['active'].iloc[-3]


    return {
        'data':[ go.Indicator(
            mode= 'number+delta',
            value = value_active,
            delta ={
                'reference':change_active,
                'position':'right',
                'valueformat':'.9',
                'relative':False,
                'font':{'size':15}
            },
            number={'valueformat': '.' , 'font':{'size':20},},
            domain={'y':[0,1] , 'x':[0,1]}
            )
        ],
        'layout':go.Layout(
            title={
                'text':'New active',
                'y':1,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            font=dict(color ='orange'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            # height=50,
            # width =100
        ),
    }



# pie chart callback

@app.callback(
    Output('pie_chart' , 'figure'),
    [Input('selected_country' , "value")]
)

def update_graph(selected_country):
    new_case = df2[df2['Country'] == selected_country]['confirmed'].iloc[-1]
    new_death = df2[df2['Country'] == selected_country]['deaths'].iloc[-1]
    new_active = df2[df2['Country'] == selected_country]['active'].iloc[-1]
    new_recover = df2[df2['Country'] == selected_country]['recovery'].iloc[-1]

    return {
        'data':[
            go.Pie(
                labels = ['confirmed' , 'deaths' , 'recovery' , 'active'],
                values = [new_case , new_death , new_active, new_recover],
                marker = dict(colors =['orange' , '#dd1e15' , '#e55467' , 'green']),
                textinfo='label+value+percent',
                textfont = dict(size =15),
                hole =.7,
                rotation =45,
                #insidetextorientation ='radial',
            )
        ],

        'layout':go.Layout(
            # width =800,
            # height =541,
            plot_bgcolor='#1f2c56',
            paper_bgcolor='#1f2c56',
            hovermode ='closest',
            title={
                'text':f'Total Cases  {selected_country}',
                'y':0.92,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            titlefont ={
                'color':'#fff',
                'size':19
            },
            font=dict(
                size=14,
                color='#fff',
            ),
            legend={
                'orientation':'h',
                'bgcolor':'#1f2c56',
                'xanchor':'center','x':0.5 ,'y':0.17
            },
        ),
    }


# line and bar for 30 dtays

@app.callback(
    Output('line_chart' , 'figure'),
    [Input('selected_country' , 'value')]
)


def update_graph(selected_country):
    df3 = df[df['Country'] == selected_country][['Country' , 'date' ,'confirmed']].reset_index()
    df3['daily_shift'] = df3['confirmed']- df3['confirmed'].shift(1)
    df3['rolling_avg'] = df3['daily_shift'].rolling(window =7).mean()
    return {
        'data':[
                go.Bar(
                x = df3[df3['Country'] ==  selected_country]['date'].tail(31),
                y = df3[df3['Country'] == selected_country]['daily_shift'].tail(31),
                name = "Daily cases",
                marker =dict(
                    color ='#e55467',
                ),
                hoverinfo='text',
                hovertext =
                '<b>Date  </b> ' + df3[df3['Country'] == selected_country]['date'].tail(31).astype(str) + '  <br>' +
                '<b>Daily Cases </b>  ' + [f'{x:,.0f}' for x in df3[df3['Country'] == selected_country]['daily_shift'].tail(31) ] + '  <br>' +
                '<b>Country  </b>  ' + df3[df3['Country'] == selected_country]['Country'].tail(31).astype(str)  + '  <br>'
            ) ,
                go.Scatter(
                x = df3[df3['Country'] == selected_country]['date'].tail(31),
                y = df3[df3['Country'] == selected_country]['rolling_avg'].tail(31),
                mode = 'lines',
                name = 'Rolling Avg of the last 7 days ',
                line = dict(width=3 , color ="#fff"),
                marker=dict(color ="green"),
                hoverinfo='text',
                hovertext=
                '<b>Date  </b> ' + df3[df3['Country'] == selected_country]['date'].tail(31).astype(str) + '  <br>' +
                '<b>Rolling_avg for Last 7 days </b>  ' + [f'{x:,.0f}' for x in df3[df3['Country'] == selected_country]['rolling_avg'].tail(31) ] + '  <br>'
            )
    ],

        'layout':go.Layout(
            # width = 1200,
            # height = 520,
            barmode = 'stack',
            plot_bgcolor ='rgba(23,36,100,.8)',
            paper_bgcolor ='#1f2c56',
            title={
                'text':f"Last 31 days cases in   {selected_country}",
                'y':0.93,
                'x':0.5,
                'xanchor':'center',
                'yanchor':'top',
            },
            titlefont={
                'color':'#fff',
                'size':23,

            },
            hovermode='x',
            xaxis = dict(
                title = '<b>Date</b>',
                color ='#fff',
                showline =True,
                showgrid = True,
                ticks='outside',
                showticklabels = True,
                linewidth=2,
                linecolor ='blue',
                tickfont=dict(
                    size =14,
                    color ='#fff',
                )
            ),

            yaxis = dict(
                title = '<b>daily cases</b>',
                color ='#fff',
                showline =True,
                showgrid = True,
                ticks='outside',
                showticklabels =True,
                linewidth=2,
                linecolor ='blue',
                tickfont=dict(
                    size =14,
                    color ='#fff',
                )
            ),

            legend={
                'orientation':'h',
                'bgcolor':'red',
                'xanchor':'center',
                'x':0.5,'y':-0.3,
            },
            font= dict(
                size =14,
                color ='#fff',
            ),


        )
    }


#map graphs

@app.callback(
    Output('map' , 'figure') ,
    [Input('selected_country' , 'value')]
)


def update_graph(selected_country):
    df5 = df.groupby(['Long' , 'Lat' ,"Country"])[['confirmed' , 'deaths' , 'active' , 'recovery']].max().reset_index(drop =False)
    return {
        'data':[
            go.Scattermapbox(
                lon =df5['Long'],
                lat = df5['Lat'],
                mode = 'markers',
                marker =go.scattermapbox.Marker(
                    size = df5['confirmed']/1500,
                    color =df5['confirmed'],
                    colorscale ='hsv',
                    sizemode = 'area',
                    opacity =0.4
                ),

                hoverinfo = 'text',
                hovertext =
                '<b>Country : </b>  '+ df5['Country'].astype(str) +'<br>'+
                '<b>Longitude :</b> '+ df5['Long'].astype(str)+ '<br>'+
                '<b>Latitude :</b> '+ df5['Lat'].astype(str)+ '<br>'+
                '<b>Confirmed : </b> '+ [f'{x:,.0f} ' for x in df5['confirmed']] + '<br>'+
                '<b>Recoverd : </b> '+ [f'{x:,.0f} ' for x in df5['recovery']] + '<br>'+
                '<b>Deaths : </b> '+ [f'{x:,.0f} ' for x in df5['deaths']] + '<br>'+
                '<b>Active : </b> '+ [f'{x:,.0f} ' for x in df5['active']] + '<br>'

            )
        ],

        'layout':go.Layout(
            margin = {'r':0 , 'l':0 ,'b':0 ,"t":0},
            # width = 1020,
            # height=650,
            plot_bgcolor ='rgba(23,36,100,.8)',
            paper_bgcolor ='#1f2c56',
            hovermode='closest',
            mapbox=dict(
                accesstoken =MYKEY,
                center =go.layout.mapbox.Center(lat =-0.02 , lon =37),
                #style ='open-street-map',
                style ='dark',
                zoom =1.5,
            ),
            autosize =True,
        )
    }


if __name__ == '__main__':
    app.run_server(debug=DEBUG)
