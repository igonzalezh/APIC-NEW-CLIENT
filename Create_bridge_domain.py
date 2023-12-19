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

#Reemplazar nombre de tenant y bridge domain segùn lo requerido ##

url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Tenant_cliente5/BD-bd_cliente5.json"

headers = {
  'Content-Type': 'text/plain'
}
cookie = {"APIC-cookie":API_TOKEN}

payload = "payload{\"fvBD\":{\"attributes\":{\"dn\":\"uni/tn-Tenant_cliente5/BD-bd_cliente5\",\"mac\":\"00:22:BD:F8:19:FF\",\"arpFlood\":\"true\",\"name\":\"bd_cliente5\",\"rn\":\"BD-bd_cliente5\",\"status\":\"created\"},\"children\":[{\"fvSubnet\":{\"attributes\":{\"dn\":\"uni/tn-Tenant_cliente5/BD-bd_cliente5/subnet-[10.100.5.254/24]\",\"ctrl\":\"\",\"ip\":\"10.100.5.254/24\",\"rn\":\"subnet-[10.100.5.254/24]\",\"status\":\"created\"},\"children\":[]}},{\"fvRsCtx\":{\"attributes\":{\"tnFvCtxName\":\"vrf_cliente5\",\"status\":\"created,modified\"},\"children\":[]}}]}}\nresponse: {\"totalCount\":\"0\",\"imdata\":[]}"
response = requests.request("POST", url, headers=headers, data=payload, cookies=cookie, verify=False )
print(response.text)

