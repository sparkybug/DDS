from app.app import app

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    # db.init_app(app)
    app.run(debug=True)