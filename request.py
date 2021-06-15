import requests 

url = 'http://127.0.0.1:5000/results'

r = requests.post(url, json={'gender': 1, 'married': 1, 'residence_type': 1, 'hypertension': 1, 'heart_disease':1, 'work_type': 1, 'smoking_status':2})
print(r.json())