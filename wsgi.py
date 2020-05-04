from application import create_app

app = create_app('config.Config', debug=True)

if __name__ == "__main__":
    app.run(debug=True)