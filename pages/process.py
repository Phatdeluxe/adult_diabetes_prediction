import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process


            """
        ),

        dcc.Markdown('The first step to building a model is to find a dataset. I got this dataset from the USDA Food Environment Atlas. This data was collected from census data.'),

        dcc.Markdown('Next you want to look through your data and begin to familiarize yourself with the column titles. Most of the time they are labeled in strange ways that may be hard to interpret, thankfully they provide a key of what the titles mean. Also while familiarizing with the data, if you have not already chosen a feature to predict, you will need to find what you want to predict. I saw the health category and though it would be interesting to see if it was possible to predict the percentage of adults with diabetes. Unfortunately, the most recent data that I had from this dataset was from 2013.'),

        dcc.Markdown('Once you have looked over the data it is time to start coding.'),

        dcc.Markdown('First step is to load the data into Pandas Dataframes. A simplified description of a Pandas Dataframe is a table that allows you to use code to find out tons of helpful information, then manipulate the information within. Below is an image of a dataframe.'),

        html.Img(src='assets/pandas_dataframe.png', className='img-fluid'),

        dcc.Markdown('Once you have it loaded into you dataframe, you need to clean and wrangle the data. This will most likely be the most time consuming part of the whole project. It involves steps such as ensuring that you have no missing values in your columns and replacing those missing values with a correct missing value indicator, removing features that will not help your predictions, and removing redundant features. For this model there were a ton of features that were unusable. This was mostly because the information was gathered after 2013, which is when the data for my target was gathered. I reduced the number of features from around 320 to 150.'),

        dcc.Markdown('When creating models it is important to seperate your data into training and testing data. This is so that you have some data that allows you to see how good your model is at making actual predictions. I did a three way train/validation/test split, so I had data to train the model with, and data to test the data with before making changes. The test set was saved for what I believed was the final iteration of the model.'),

        html.Img(src='assets/train_split.png', className='img-fluid'),

        dcc.Markdown('After cleaning and wrangling the data you can begin to make your model. For my process I tried many different model types, such as a linear regression and random forest regression. For this model I used an XGBoosted regressor. This is similar to a random forest regression, but it will run through many iterations of the data, and slowly learn each iteration. This can be compared to reading a choose your own adventure book, where each time it will remember its past reading to get the best ending.'),

        dcc.Markdown('Once you have selected the model you can tune your hyper-parameters. Hyper-parameters affect how your model behaves when it is learning. If we continue to use the choose your own adventure comparison, out hyper parameters might tell it to stop reading after making three choices and to read the book ten times. This sounds hard, but we can use another library to do the heavy lifting for us.'),

        html.Img(src='assets/pipeline.png', className='img-fluid'),

        dcc.Markdown('After all that, the model can be fit to our data and implemented.'),  
        
        dcc.Link(dbc.Button('The model!', color='primary'), href='/predictions')
    ],
)

layout = dbc.Row([column1])