#
# # callbacks and updates for the graphs and values
# @app.callback(
#     Output('confirmed' , 'figure'),
#     [Input('w_countries' , 'value')]
# )
# def update_graph(w_countries):
#     value_cases = df2[df2['Country'] == w_countries]['confirmed'].iloc[-1] - df2[df2['Country'] == w_countries]['confirmed'].iloc[-2]
#     change_cases = df2[df2['Country'] == w_countries]['confirmed'].iloc[-2] - df2[df2['Country'] == w_countries]['confirmed'].iloc[-3]
#
#
#     return {
#         'data':[ go.Indicator(
#             mode= 'number+delta',
#             value = value_cases,
#             delta ={
#                 'reference':change_cases,
#                 'position':'right',
#                 'valueformat':'.9',
#                 'relative':False,
#                 'font':{'size':15}
#             },
#             number={'valueformat': '.' , 'font':{'size':20},},
#             domain={'y':[0,1] , 'x':[0,1]}
#             )
#         ],
#         'layout':go.Layout(
#             title={
#                 'text':'New Confirmed',
#                 'y':1,
#                 'x':0.5,
#                 'xanchor':'center',
#                 'yanchor':'top',
#             },
#             font=dict(color ='orange'),
#             paper_bgcolor='#1f2c56',
#             plot_bgcolor='#1f2c57',
#             height=300,
#             width =200
#         ),
#     }
#
# @app.callback(
#     Output('deaths' , 'figure'),
#     [Input('w_countries' , 'value')]
# )
#
# def update_graph(w_countries):
#     value_deaths = df2[df2['Country'] == w_countries]['deaths'].iloc[-1] - df2[df2['Country'] == w_countries]['deaths'].iloc[-2]
#     change_deaths = df2[df2['Country'] == w_countries]['deaths'].iloc[-2] - df2[df2['Country'] == w_countries]['deaths'].iloc[-3]
#
#
#     return {
#         'data':[ go.Indicator(
#             mode= 'number+delta',
#             value = value_deaths,
#             delta ={
#                 'reference':change_deaths,
#                 'position':'right',
#                 'valueformat':'.9',
#                 'relative':False,
#                 'font':{'size':15}
#             },
#             number={'valueformat': '.' , 'font':{'size':20},},
#             domain={'y':[0,1] , 'x':[0,1]}
#             )
#         ],
#         'layout':go.Layout(
#             title={
#                 'text':'New detahts',
#                 'y':1,
#                 'x':0.5,
#                 'xanchor':'center',
#                 'yanchor':'top',
#             },
#             font=dict(color ='orange'),
#             paper_bgcolor='#1f2c56',
#             plot_bgcolor='#1f2c57',
#             height=300,
#             width =200
#         ),
#     }
#
# @app.callback(
#     Output('recovered' , 'figure'),
#     [Input('w_countries' , 'value')]
# )
# def update_graph(w_countries):
#     value_recover = df2[df2['Country'] == w_countries]['recovery'].iloc[-1] - df2[df2['Country'] == w_countries]['recovery'].iloc[-2]
#     change_recover = df2[df2['Country'] == w_countries]['recovery'].iloc[-2] - df2[df2['Country'] == w_countries]['recovery'].iloc[-3]
#
#
#     return {
#         'data':[ go.Indicator(
#             mode= 'number+delta',
#             value = value_recover,
#             delta ={
#                 'reference':change_recover,
#                 'position':'right',
#                 'valueformat':'.9',
#                 'relative':False,
#                 'font':{'size':15}
#             },
#             number={'valueformat': '.' , 'font':{'size':20},},
#             # domain={'y':[0,1] , 'x':[0,1]}
#             )
#         ],
#         'layout':go.Layout(
#             title={
#                 'text':'New Recovery',
#                 'y':1,
#                 'x':0.5,
#                 'xanchor':'center',
#                 'yanchor':'top',
#             },
#             font=dict(color ='orange'),
#             paper_bgcolor='#1f2c56',
#             plot_bgcolor='#1f2c57',
#             height=300,
#             width =200
#         ),
#     }
#
# @app.callback(
#     Output('active' , 'figure'),
#     [Input('w_countries' , 'value')]
# )
# def update_graph(w_countries):
#     value_active = df2[df2['Country'] == w_countries]['active'].iloc[-1] - df2[df2['Country'] == w_countries]['active'].iloc[-2]
#     change_active = df2[df2['Country'] == w_countries]['active'].iloc[-2] - df2[df2['Country'] == w_countries]['active'].iloc[-3]
#
#
#     return {
#         'data':[ go.Indicator(
#             mode= 'number+delta',
#             value = value_active,
#             delta ={
#                 'reference':change_active,
#                 'position':'right',
#                 'valueformat':'.9',
#                 'relative':False,
#                 'font':{'size':15}
#             },
#             number={'valueformat': '.' , 'font':{'size':20},},
#             domain={'y':[0,1] , 'x':[0,1]}
#             )
#         ],
#         'layout':go.Layout(
#             title={
#                 'text':'New active',
#                 'y':1,
#                 'x':0.5,
#                 'xanchor':'center',
#                 'yanchor':'top',
#             },
#             font=dict(color ='orange'),
#             paper_bgcolor='#1f2c56',
#             plot_bgcolor='#1f2c57',
#             height=300,
#             width =200
#         ),
#     }
