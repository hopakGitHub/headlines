import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_news():
	return "no news is good news"

if __name__ == '__main__':
        app.run()
