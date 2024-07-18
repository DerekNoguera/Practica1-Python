# import colorise
import requests

# def getDatos() -> str:
#     response = requests.get("https://api.chucknorris.io/jokes/random")
#     return response.json()["value"]
# colorise.cprint(getDatos(), fg="blue")

def getDatos2() -> str:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()
print(getDatos2())

