import pandas as pd
import json
f=open("new.json")
data=json.load(f)
df1=pd.json_normalize(
    data["b2b"],
    record_path=["inv"],
    meta=["ctin"],
          
    record_prefix="item_"
)

df2 = pd.json_normalize(
    data["b2b"],
    record_path=["inv", "itms"],
    meta=["ctin"],
    meta_prefix="party_",
    record_prefix="item_"
)
df=pd.concat([df1,df2],axis=1)
df.to_excel("j.xlsx")
print(df)

