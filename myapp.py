import requests
import json

URL='http://127.0.0.1:8000/stu/'
def get_req(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data,indent=4)
    r=requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)
# get_req()

def post_data():
    data={
        'name':'ritik',
        'roll':5,
        'city':'danapur'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    print(r)
post_data()