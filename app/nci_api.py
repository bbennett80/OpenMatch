import requests


def nci_api(NCTID: str):
    API_KEY = "YOUR API KEY HERE"
    HEADERS = {"x-api-key": API_KEY}

    v2_base_trials = "https://clinicaltrialsapi.cancer.gov/api/v2/trials/"
    url = f"{v2_base_trials}{NCTID}"
    r = requests.get(url, headers=HEADERS)
    return r.json()
