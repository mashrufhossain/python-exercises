import urllib.request
import urllib.parse
import json

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    parms = dict()
    parms['q'] = address
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "features" not in js:
        print("==== Failure To Retrieve ====")
        continue

    # The plus_code is stored in js['features'][0]['properties']['plus_code']
    plus_code = js['features'][0]['properties']['plus_code']
    print("Plus code", plus_code)
