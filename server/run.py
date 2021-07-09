from app.factory import create_app
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def run():
    app = create_app()
    app.run(host='localhost', port=9000, debug=True)


if __name__ == '__main__':
    run()
