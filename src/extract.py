import requests

class Extract:

    def _init_(self):
        pass

    def extract_data(self, country):

        url = f"http://universities.hipolabs.com/search?country={country}"

        
        # Acessando o link da internet
        response = requests.get(url)
        response.raise_for_status()  
        universities = response.json()

        return universities