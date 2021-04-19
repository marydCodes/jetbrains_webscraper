import requests, json

url_input = input("Input the URL: ")

dom = requests.get(url_input)
text_dict = json.loads(dom.text)

if dom.status_code == 200:
    # check headers
    if dom.headers["Content-Length"] == "200":
        print(text_dict["content"])
    else:
        print("Invalid quote resource!")
else:
    print("Invalid quote resource")