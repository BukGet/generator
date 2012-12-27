import json
import bleach
from bottle import Bottle

app = Bottle()


@app.hook('before_request')
def set_headers():
    response.set_header('Content-Type', 'application/json')
    response.set_header('Access-Control-Allow-Origin', '*')


@app.post('/login')
def login():
    '''
    '''
    pass
    


@app.put('/plugin')
def update_plugin():
    '''
    '''
    pass


@app.put('/gen')
def update_geninfo():
    '''
    '''
    pass

