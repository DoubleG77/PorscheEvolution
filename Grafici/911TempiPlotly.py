import pandas as pd
import plotly.graph_objs as go


t = pd.read_csv("tempi_porsche.csv", sep = ';', encoding='latin1')
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x = t['Rank'],
        y = t['PS/KG'],
        name="PS/KG",
        yaxis='y2',
        marker_color ='rgb(104,204,238)',
        marker_line_width=1.5,
        marker_line_color='rgb(104,204,238)',
        opacity=0.5,
        text=t['PS/KG'],
        textfont=dict(
            family="Arial",
            color='black',
            size=25
        )
    )
)

fig.add_trace(
    go.Scatter(
        mode='lines+markers',
        x = t['Rank'],
        y = t['Time'],
        name="Time Lap",
        marker_color='rgb(170,51,119)'
    )
)

fig.update_layout(
    go.Layout(
    title=dict(
        text="Tempi delle 911 al Nürburgring",
        font_family="Arial",
        font_size=36
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    xaxis=dict(
        zeroline=False,
        title=dict(
            text="Rank",
            font_family="Arial",
            font_size=24
        ),
        range=[1,50], # set x-axis range to include the origin
        tickmode='linear',
        tickfont_size=15
    ),
    yaxis=dict(
        showgrid=False,
        title=dict(
            text="Time lap",
            font_family="Arial",
            font_size=24
        ),
        tickfont_size=15
    ),
    yaxis2=dict(
        overlaying='y',
        showgrid=False,
        title=dict(
            text="PS/KG",
            font_family="Arial",
            font_size=24
        ),
        tickfont_size=15,
        side = 'right'
    )
    )
)

fig.show()