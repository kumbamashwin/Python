data = {
  "id": "0001",
  "type": "donut",
  "name": "Cake",
  "image": {
    "url": "images/0001.jpg",
    "width": 200,
    "height": 200
  },
  "thumbnail": {
    "url": "images/thumbnails/0001.jpg",
    "width": 32,
    "height": 32
  }
}
  
for key,value in data.items():
    if isinstance(value,str):
        print(key.ljust(10),value)
    elif isinstance(value,dict):
        for subkey,subvalue in value.items():
            print(subkey.ljust(10),subvalue)