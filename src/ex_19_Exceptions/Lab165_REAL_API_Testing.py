import requests

# Scenario 1:
# response = requests.get("https://google.com")
# print(response.status_code) # 200

# Scenario 2:
# response = requests.get("http://api.example.com/data")
# print(response.status_code) # requests.exceptions.ConnectionError

# Scenario 3:
try:
    url = input("Enter a url: ") # Provide invalid url - http://api.example.com/data
    response = requests.get(url,timeout=3)
    print(response.status_code) # requests.exceptions.ConnectionError...
except requests.exceptions.ConnectionError:
    print("Error due to the wrong URL or Connection failure!")
except requests.exceptions.Timeout:
    print("Timeout error, not able to load the URL")
except Exception as e:
    print(e)



