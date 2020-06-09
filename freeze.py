from flask_frozen import Freezer
from run import application

freezer = Freezer(application)

if __name__ == '__main__':
    freezer.freeze()
    