import requests 

url = 'http://127.0.0.1:5000/results'

r = requests.post(url, json={'age': 40, 'bmi':20, 'heart_disease':1, 'married':1})
print(r.json())