from src.extract import Extract
from src.transform import Transform
from src.load import Load

if __name__ == "__main__":
    print("=== ETL UNIVERSIDADES ===")

    extract = Extract()
    transform = Transform()
    load = Load()

    # 1️EXTRAÇÃO
    data = extract.extract_all_countries()

    # 2️TRANSFORMAÇÃO
    df = transform.clean_data(data)

    # 3 CARGA
    load.create_table()
    load.load_data(df)

    print("ETL concluído com sucesso.")
