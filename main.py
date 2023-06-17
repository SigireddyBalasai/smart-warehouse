from routing import get_new_app

app = get_new_app()

if __name__ == "__main__":
    app.run(debug=True)
