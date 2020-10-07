from flask import Flask
from flask import request

import requests

app = Flask(__name__)

ipa = "http://35.237.92.100"
ipb = "http://104.196.187.68"


@app.route('/')
def index():
    return 'Server-1-Api funcionando (instancia 1)'


@app.route('/data', methods=["POST"])
def data_post():
    req_data = request.get_json()

    print(req_data)
    server_a_resp = {}
    try:
        data = requests.get(ipa + "/stats")
        server_a_resp = data.json()
        server_a_resp = server_a_resp["stats"]
    except Exception as e:
        print(" ERROR LLAMANDO AL SERVER A ")
        print(e)
        if hasattr(e, 'message'):
            print(" MENSAJE DE ERROR EN SERVER A: ")
            print(e.message)

    server_b_resp = {}
    try:
        data = requests.get(ipb + "/stats")
        server_b_resp = data.json()
        server_b_resp = server_b_resp["stats"]
    except Exception as e:
        print(" ERROR LLAMANDO AL SERVER B ")
        print(e)
        if hasattr(e, 'message'):
            print(" MENSAJE DE ERROR EN SERVER B: ")
            print(e.message)

    print("Server A: ")
    print(server_a_resp)
    print("Server B: ")
    print(server_b_resp)

    server_ip = ""
    docs_a = server_a_resp["docs"]
    docs_b = server_b_resp["docs"]

    ram_a = server_a_resp["ram"]
    ram_b = server_b_resp["ram"]

    cpu_a = server_a_resp["cpu"]
    cpu_b = server_b_resp["cpu"]

    if (docs_a != docs_b):
        server_ip = ipa if docs_a < docs_b else ipb
    elif (ram_a != ram_b):
        server_ip = ipa if ram_a < ram_b else ipb
    elif (cpu_a != cpu_b):
        server_ip = ipa if cpu_a < cpu_b else ipb
    else:
        server_ip = ipa
    
    _obj = {
        "author": req_data["author"],
        "sentence": req_data["sentence"]
    }

    try:
        print("PUBLICANDO DATOS AL SERVER: " + server_ip)
        http_post = requests.post(server_ip + "/data", json=_obj)
        code = http_post.status_code
        recieved_data = http_post.json()
        if (code == 200 or code == 201):
            print(" OK " + str(code) + " ")
            print(str(recieved_data))
        else:
            print(" ERROR " + str(code) + " ")
            print(str(recieved_data))
        
    except Exception as e:
        print(" ERROR REALIZANDO POST AL SERVER ")
        print(e)
        if hasattr(e, 'message'):
            print(" MENSAJE DE ERROR EN SERVER B: ")
            print(e.message)

    return { "msg": "ok" }, 201

@app.route('/ipa')
def ipa_def(new_ipa):
    global ipa
    ipa = "http://" + new_ipa
    return { "msg": 'ok' }


@app.route('/ipb')
def ipb_def(new_ipb):
    global ipb
    ipb = "http://" + new_ipb
    return { "msg": 'ok' }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
