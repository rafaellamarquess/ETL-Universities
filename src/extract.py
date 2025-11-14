import requests
import time

class Extract:
    BASE_URL = "http://universities.hipolabs.com/search"

    def extract_data(self, country):
        """Extrai dados de um país específico."""
        url = f"{self.BASE_URL}?country={country}"
        print(f"Extraindo dados de {country}...")
        
        for attempt in range(3):
            try:
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                data = response.json()
                print(f"{country}: {len(data)} universidades encontradas.")
                return data
            except requests.exceptions.RequestException as e:
                print(f"Erro ao buscar {country} (tentativa {attempt + 1}/3): {e}")
                if attempt < 2:
                    time.sleep(3)
                else:
                    print(f"Falha ao buscar {country}")
                    return []
        
        return []

    def extract_all_countries(self):
        """Extrai dados da API com tentativas e timeout."""
        print("Extraindo dados da API...")
        countries = [
            "Brazil", "United States", "Mexico", "Canada", "Argentina",
            "Germany", "France", "Italy", "Spain", "Japan", "India"
        ]

        all_universities = []

        for country in countries:
            url = f"{self.BASE_URL}?country={country}"
            print(f"\nBaixando dados de {country}...")

            for attempt in range(3):  # até 3 tentativas por país
                try:
                    response = requests.get(url, timeout=30)
                    response.raise_for_status()
                    data = response.json()
                    print(f"{country}: {len(data)} universidades encontradas.")
                    all_universities.extend(data)
                    break  # sai do loop se der certo

                except requests.exceptions.RequestException as e:
                    print(f"Erro ao buscar {country} (tentativa {attempt + 1}/3): {e}")
                    if attempt < 2:
                        print("Tentando novamente em 3 segundos...")
                        time.sleep(3)
                    else:
                        print(f"Falha definitiva ao buscar {country}. Pulando...")

        print(f"\nTotal geral: {len(all_universities)} universidades extraídas.")
        return all_universities