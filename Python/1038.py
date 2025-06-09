import pandas as pd

lancheMatrix = {
    "codigo":[0,1,2,3,4,5],
    "preco":[0,4.00,4.50,5.00,2.00,1.50]
}

lanche = pd.DataFrame(lancheMatrix)

codigo,quant= map(int, input().split())

valor=lanche.loc[codigo,"preco"]
valor = valor*quant

print(f"Total: R$ {valor:.2f}")




