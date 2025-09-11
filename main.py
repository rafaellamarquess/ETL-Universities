from src.extract import Extract
from src.load import Load

extract = Extract()
load = Load()

mexico = extract.extract_data("Mexico")
load.load_data(mexico)


