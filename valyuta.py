import requests

def to_sum(val):
    url = f'https://cbu.uz/oz/arkhiv-kursov-valyut/json/{val}/'
    nat = requests.get(url)
    javob = nat.json()[0]['Rate']
    return f"1 {val} - <code><b>{javob}</b> SUM</code>"

