import requests
import json
import conf

def get_token():
    requests.packages.urllib3.disable_warnings()

    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
    data = {
          "aaaUser":{
                "attributes":{
                      "name":conf.user,
                      "pwd": conf.password
                }
          }
    }
    header={"content-type": "application/json"}
    respuesta=requests.post(url, json.dumps(data), headers=header, verify=False)

    respuesta_json=respuesta.json()

    API_TOKEN=respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return API_TOKEN

API_TOKEN = get_token()

url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Tenant_cliente5/ap-app_cliente5/epg-epg_cliente5.json"

payload = "payload{\"fvAEPg\":{\"attributes\":{\"dn\":\"uni/tn-Tenant_cliente5/ap-app_cliente5/epg-epg_cliente5\",\"prio\":\"level3\",\"name\":\"epg_cliente5\",\"rn\":\"epg-epg_cliente5\",\"status\":\"created\"},\"children\":[{\"fvRsBd\":{\"attributes\":{\"tnFvBDName\":\"bd_cliente5\",\"status\":\"created,modified\"},\"children\":[]}}]}}\nresponse: {\"totalCount\":\"0\",\"imdata\":[]}"
headers = {
  'Content-Type': 'text/plain'
}
cookie = {"APIC-cookie":API_TOKEN}
response = requests.request("POST", url, headers=headers, cookies=cookie, data=payload, verify=False)

print(response.text)