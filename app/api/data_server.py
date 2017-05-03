from eve import Eve
from flask_cors import CORS


app = Eve(settings='settings.py')
CORS(app)


if __name__=='__main__':
    app.run(debug=True, port=8080)
