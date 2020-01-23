

import requests

try:
    url  = "https://api.github.com/"

    response = requests.get(url,auth = ("kumbamashwin", "fafd5d1bb0c026fea9dca4e94092c0c4af0177ee"))
    
    if response.status_code == 200:
        data = json.loads(response.text)
        for key,value in data.items():
            print(key,value)
    else:
        print("invalid request")
        
except requests.HTTPError as err:
    print(err)