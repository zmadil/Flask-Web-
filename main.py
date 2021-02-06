from website import create_app

app= create_app()

if __name__ == '__main__':                #ONly we run main.py, not by importing
    app.run(debug=True)                   #Debug=true means if we make changes, it will automatically rerun the web server