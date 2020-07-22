import pandas as pd
import numpy as np
#read file as dataframe
dtype =\
    {'orderid': np.int64,
    'pick': np.int64,
    '1st_deliver_attempt': np.int64,
    '2nd_deliver_attempt': np.float64,
    'buyeraddress': np.object,
    'selleraddress': np.object,}

df = pd.read_csv("delivery_orders_march.csv",dtype = dtype)

holiday = ['2020-03-08','2020-03-25', '2020-03-30', '2020-03-31']
week_mask = [1,1,1,1,1,1,0]
gmt8 = 3600 * 8
one_day = 3600 * 24

# def change_names(series):

#create columns needed
df["buyeraddress"] = df["buyeraddress"].apply(lambda s: s.split(" ")[-1].lower())
df["selleraddress"] = df["selleraddress"].apply(lambda s: s.split(" ")[-1].lower())
locations = ["Metro Manila", "Luzon", "Visayas", "Mindanao"]
d = {"manila":{"manila":3,"luzon":5,"visayas":7,"mindanao":7},
     "luzon":{"manila":5,"luzon":5,"visayas":7,"mindanao":7},
     "visayas":{"manila":7,"luzon":7,"visayas":7,"mindanao":7},
     "mindanao":{"manila":7,"luzon":7,"visayas":7,"mindanao":7}}

def allow(buy,sell):
    return d[buy][sell]
df["time_allow"] = df.apply(lambda row: allow(row["buyeraddress"],row["selleraddress"]),axis = 1)
dt_columns = ['pick', '1st_deliver_attempt', '2nd_deliver_attempt']
df[dt_columns[-1]] = df['2nd_deliver_attempt'].fillna(0).astype(np.int64)
df[dt_columns] = (df[dt_columns] + gmt8) // one_day

t1 = df["pick"].values.astype("datetime64[D]")
t2 = df['1st_deliver_attempt'].values.astype('datetime64[D]')
t3 = df['2nd_deliver_attempt'].values.astype('datetime64[D]')

df["time_used1"] = np.busday_count(t1, t2, weekmask=week_mask, holidays=holiday)
df["time_used2"] = np.busday_count(t2, t3, weekmask=week_mask, holidays=holiday)

df["is_late"] = (df["time_allow"] < df["time_used1"]) | (df["time_used2"] > 3)
df["is_late"] = df["is_late"].astype(int)
df[["orderid","is_late"]].to_csv("export.csv",index = False)