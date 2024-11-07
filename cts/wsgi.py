from waitress import serve
from cts import cts
import os

if __name__ == "__main__":
    serve(cts, host=0.0.0.0, port=int(os.environ.get('PORT', 8080)))
