from flask import Flask

app = Flask(__name__)

@app.route('/bus_stop')
def hello():
    return render_template('../bus_stop.html')

if __name__ == "__main__":
    app.run()
