from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_dataframe():
 
    # Read dataframe
    df = pd.read_csv("random_data.csv")
    
    # Convert dataframe to HTML
    table = df.to_html(classes='table table-striped')

    # Render HTML string
    template = """
    <html>
        <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
            {{ table|safe }}
        </body>
    </html>
    """
    return render_template_string(template, table=table)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

