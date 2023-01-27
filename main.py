import pandas as pd
from webScrapping import dict_produtos_existentes

df_produtos = pd.DataFrame(dict_produtos_existentes)

df_produtos.to_csv( r'produtosForaEstoque.csv', index=False, encoding='utf-8',
                sep=';')


