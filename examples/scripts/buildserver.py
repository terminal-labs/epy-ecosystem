from noderunner.runners import run
from jobrunner.core import app, simplejob

import multiprocessing

def measure_progress():
    pass


def p_function():
    run()

@app.route('/build')
def home():
    p1 =  multiprocessing.Process(target=p_function)
    p1.start()
    return simplejob

app.run(debug=True, port=8080)
