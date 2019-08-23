from flaskblog import create_app

app = create_app()

if __name__ == '__main__':  # if we run the app in Python this statement is triggered
    app.run(debug=True)
