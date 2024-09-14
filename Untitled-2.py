import pandas as pd 
import sqlalchemy
import matplotlib.pyplot as plt
engine=sqlalchemy.create_engine('mysql+pymysql://deepti:deepti@localhost:3306/taskdb')
#query=''' select product.name,product.price,orders.customer_name,orders.order_item from product inner join orders on product.id=orders.id;'''
query='''select id,name from product'''
df3=pd.read_sql_query(query,engine)
print(df3)