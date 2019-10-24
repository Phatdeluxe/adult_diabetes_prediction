import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## How is diabetes impacting your community?

            Diabetes was the seventh leading cause of death in the United States in 2015 (ADA)

            Have you ever been curious what changes could be made to reduce adult diabetes?

            This app will predict what the percentage of adults with diabetes for counties in the United States.
            You can use use it to see how certain features increase and reduce the percentage of adults with diabetes
            

            This model was created using data from 2013 and earlier.

            """
        ),
        dcc.Link(dbc.Button('Lets find out', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/Choropleth_diabetes.png', className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])