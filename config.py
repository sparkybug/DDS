from sqlalchemy import create_engine

class Config:
    SECRET_KEY = '8d4a54daa26ea319e39b6d44'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/dds'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = ''

# defining db credentials
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'dds'

# python function to connect to the mySQL db and return the SQLAlchemy engine object
def get_connection():
    return create_engine(
        url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
        user,
        password,
        host,
        port,
        database
        )
    )

if __name__ == '__main__':
    try:
        # get the connection object for the database
        engine = get_connection()
        print(f"Connection to the {host} for user {user} created successfully")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

    