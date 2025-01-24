import os
import requests
from dotenv import load_dotenv

load_dotenv()
PROXY_CURL_ENDPOINT = 'https://nubela.co/proxycurl/api/v2/linkedin'
def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False)-> dict:
    """Scrape information from LinkedIn profiles.
    Manually scrapes information from LinkedIn profiles."""
    if mock:
        return mock_data_request()
    else:
        return proxycurl_request(linkedin_profile_url)


def mock_data_request()->dict:
    """Get mock data from a predefined URL."""
    print("Returning mock data...")
    mock_profile_url = ("https://gist.githubusercontent.com/rishu1601/a0971c993b7a36cd38666db26c4dccdd/raw/"
                        "f3da7792058cf3b5080b1e705072dec2089f41f9/rishabhLinkedinDesc.json")
    response = requests.get(mock_profile_url, timeout=10)
    response.raise_for_status()
    print(f"Received GitHub response code: {response.status_code}")
    data = response.json()
    clean_data = data_cleanup(data)
    return clean_data


def proxycurl_request(linkedin_profile_url: str) -> dict:
    """Call ProxyCurl API to scrape real LinkedIn profile data."""
    print("Invoking ProxyCurl API...")
    api_key = os.getenv("PROXYCURL_API_KEY")
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'linkedin_profile_url': linkedin_profile_url}
    response = requests.get(PROXY_CURL_ENDPOINT, params=params, timeout=10, headers=headers)
    response.raise_for_status()
    print(f"Received ProxyCurl response code: {response.status_code}")
    data = response.json()
    clean_data = data_cleanup(data)
    return clean_data

def data_cleanup(data: dict) -> dict:
    data = {
        k: v for k, v in data.items()
        if v not in [[], "", '', None]
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data["groups"]:
            group_dict.pop("profile_pic_url")
    
    return data

if __name__ == "__main__":
    linkedin_profile_url = "www.linkedin.com/in/rishabh16kumar01"
    res = scrape_linkedin_profile(linkedin_profile_url, True)
    print(res)