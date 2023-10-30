from app import app

@app.route('/')
def api_default():
    return 'Hello, world.'