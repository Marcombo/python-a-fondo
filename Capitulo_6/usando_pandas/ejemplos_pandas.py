import pandas as pd

if __name__ == '__main__':
    ds = pd.read_csv('planetas.csv')
    print(ds.head())
    print(ds.to_json())
    print(ds.to_html())
    print(ds.to_pickle('archivo_pickle'))
