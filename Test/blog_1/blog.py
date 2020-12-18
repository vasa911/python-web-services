#from waitress import serve
from app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
    #serve(app, host='0.0.0.0', port=80) #uncomment to run on separate http server