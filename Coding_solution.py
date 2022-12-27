import pandas as pd
budget=float(input("Enter weekly budget:"))
values={'Monday':[3,2.5,4,1.5,2],'Tuesday':[3,2.5,4,1.5,2],'Wednesday':[3,2.5,4,1.5,2],'Thursday':[3,2.5,4,1.5,2],'Friday':[3,2.5,4,1.5,2],'Saturday':[5,4,4,1.5,4],'Sunday':[6,4,10,1.5,4]}
val=pd.DataFrame(values,index=['TOI','Hindu','ET','BM','HT'])
price={}
for i in val.index:
    total_price=val.loc[i]['Monday']+val.loc[i]['Tuesday']+val.loc[i]['Wednesday']+val.loc[i]['Thursday']+val.loc[i]['Friday']+val.loc[i]['Saturday']+val.loc[i]['Sunday']
    price[i]=total_price
answer=set()
for i in price.keys():
    for j in price.keys():
        if i!=j and price[i]+price[j]<=budget and not((j,i) in answer):
            answer.add((i,j))

print(answer)