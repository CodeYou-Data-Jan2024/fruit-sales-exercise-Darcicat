import pandas as pd
fruit_sales = pd.DataFrame({"Apples" : ['35', '41'],
              "Bananas" : ['21', '34']},
              index=['2017 Sales', '2018 Sales'])
print(fruit_sales)
fruit_sales.to_csv('fruit.csv', index=True)