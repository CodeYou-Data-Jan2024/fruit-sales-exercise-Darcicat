import pandas as pd
fruit_sales = pd.DataFrame({"Apples" : ['35', '21'],
              "Bananas" : ['21', '34']},
              index=['2017 Sales', '2018 Sales'])# add your code here
fruit_sales.to_csv('fruit.csv', index=True)