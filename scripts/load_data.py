import pandas as pd 
from utils.config import create_db_engine 


df = pd.read_excel('data/Online Retail.xlsx')

df['Total_Price'] = df['Quantity'] * df['UnitPrice']

print(f"Lignes avant nettoyage: {len(df)}")
df.dropna(subset=['CustomerID'], inplace=True)
print(f"Lignes après suppression des NaN CustomerID: {len(df)}")

df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
print(f"Lignes après exclusion des retours/erreurs: {len(df)}")

df['CustomerID'] = df['CustomerID'].astype(str)

try : 
    engine = create_db_engine()
    df.to_sql(
            name='transactions',   
            con=engine,              
            if_exists='replace',     
            index=False,
            chunksize=10000              
        )
    print("les données ont été transféré avec succès")
except:
    print("les données n'ont pas été transférées dans la base de donnée.")