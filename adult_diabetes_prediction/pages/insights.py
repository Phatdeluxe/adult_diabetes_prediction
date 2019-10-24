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
        
            ## Insights


            """
        ),

        dcc.Markdown('Predictive models can be complicated and hard to understand. Fortunately we can look into some of the decisions that the model made when trying to make these predictions. '),

        dcc.Markdown('First it is interesting to find out which features provide the most insight into making predictions. Before we get into it, think about what you think might be the most useful feature in predicting whether or not an adult has diabetes. Using a library called eli5, we can look at the permutation importance of the features, and be given an organized table of the features and their importance. This table will tell us the feature and the weight of the feature. The easy way to interpret this table is that green is good. To get a bit more technical, higher positive weights mean the feature will change the outcome of our prediction the most if it is changed. The image to the right is what the table will look like. Did you guess correctly? Are you surprised by the outcome? I can tell you that I was.'),

        html.Img(src='assets/feature_importance.png', className='img-fluid'),

        dcc.Markdown('Now that we know which features are important we will look at a Shapley plots. These plots are confusing at first, but very informative if you understand what you are looking for. The example below is of my home county Boulder County, CO.'),

        html.Img(src='assets/boulder_shap.png', className='img-fluid'),

        dcc.Markdown('At first look you will see two sides, red and blue. In our model, red represents features that increase the percent of adults with diabetes, and blue represents features that decrease the percent of adults with diabetes. As you can see with this example the feature making the most change on this particular prediction is The percent of adults over the age of 65. In contrast to the feature importance above, this might be expected.'),

        dcc.Markdown('You will then see that there is a base and an output value. The output value is the prediction that the model made for this specific observation. For any regression models, models that predict a continuous value similar to a linear equation, the output value is the actual prediction. Looking back to the red and blue chevrons, the amount they change the output is an actual percentage.'),

        dcc.Markdown('For more info on the process click here:'),

        dcc.Link(dbc.Button('The process', color='primary'), href='/process!')

    ],

)


layout = dbc.Row([column1])