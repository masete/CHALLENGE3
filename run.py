"""The main method to start my application """
from API.controllers.controllers import start_app                   

app = start_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    