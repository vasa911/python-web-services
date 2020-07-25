import json 
from app import app

def test_create_post():
    app.test_client().post('/posts', data=json.dumps(
        {
            "title": "Title1",
            "body": "sdgdsaf",
            "date": "2018-04-01T00:00"
        }, content_type="application/json"
    ))