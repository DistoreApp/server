import distoreapp

from config import *


if __name__ == "__main__":
    distoreapp.create_app(Production).run()
    # distoreapp.create_app(Development).run()
    # distoreapp.create_app(Testing).run()