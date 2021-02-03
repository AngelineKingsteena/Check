import pandas as pd
import datetime as dt

df = pd.DataFrame({
    'atable':     ['22-10-2020 14:07', '22-10-2020 14:07', '22-10-2020 14:07', '22-10-2020 14:07', '22-10-2020 14:07'],
    'column':     ['col_1', 'col_2', 'col_a', 'col_b', 'col']})

df['atable'] = df['atable'].fillna(pd.to_datetime('1900-01-01 00:00:00'))
df['atable'] = pd.to_datetime(df['atable'], errors='coerce')
df['atable-Weekday Num'] = df['atable'].dt.dayofweek + 1
df['atable-Weekday Num'] = df['atable-Weekday Num'].astype('int32')
# df['atable-Weekday'] = df['atable'].dt.weekday_name
# df['atable-Weekday Combo'] = (df['atable-Weekday Num'].astype(str)+'-'+df['atable-Weekday'])
df['atable-Hour Num'] = df['atable'].dt.hour
df['atable-Hour Num'] = df['atable-Hour Num'].astype('int32')
df['atable-Hour'] = ""
df['atable-Month-Year'] = df['atable'].apply(lambda x: x.strftime('%B-%Y'))
df['atable-Month-Year'] = pd.to_datetime(df['atable-Month-Year'], errors='coerce')
# df['atable-Month-Year'] = pd.to_datetime(df['atable-Month-Year']).dt.date
# df['atable-Week'] = df['atable'].apply(lambda x: (x - timedelta(days=x.dayofweek)))
# df['atable-Week'] = pd.to_datetime(df['atable-Week'], errors='coerce')
# df['atable-Week'] = pd.to_datetime(df['atable-Week']).dt.date


df['atable'] = pd.to_datetime(df['atable'])
df['month_year'] = df['atable'].dt.strftime('%B-%Y')
df['month_year']= pd.to_datetime(df['month_year'])
df['week_year']=df['atable'].dt.strftime('%W-%Y')
# df['week_year']=pd.to_datetime(df['week_year'])
df['day_year']=df['atable'].dt.dayofyear
# df['day_year']=pd.to_datetime(df['day_year'])
# df['day_year']

# cols = ['CREATEDTTM', 'RESOLVEDTTM', 'CLOSEDTTM']
#         for x in cols:
#             df[x] = df[x].fillna(pd.to_datetime('1900-01-01 00:00:00'))
#             df[x] = pd.to_datetime(df[x], errors='coerce')
#             df[f'{x} - Weekday Num'] = df[x].dt.dayofweek + 1
#             df[f'{x} - Weekday Num'] = df[f'{x} - Weekday Num'].astype('int32')
#             df[f'{x} - Weekday'] = df[x].dt.weekday_name
#             df[f'{x} - Weekday Combo'] = (df[f'{x} - Weekday Num'].astype(str)+'-'+df[f'{x} - Weekday'])
#             df[f'{x} - Hour Num'] = df[x].dt.hour
#             df[f'{x} - Hour Num'] = df[f'{x} - Hour Num'].astype('int32')
#             df[f'{x} - Hour'] = ""
#             df[f'{x} - Month-Year'] = df[x].apply(lambda x: x.strftime('%B-%Y'))
#             df[f'{x} - Month-Year'] = pd.to_datetime(df[f'{x} - Month-Year'], errors='coerce')
#             df[f'{x} - Month-Year'] = pd.to_datetime(df[f'{x} - Month-Year']).dt.date
#             df[f'{x} - Week'] = df[x].apply(lambda x: (x - timedelta(days=x.dayofweek)))
#             df[f'{x} - Week'] = pd.to_datetime(df[f'{x} - Week'], errors='coerce')
#             df[f'{x} - Week'] = pd.to_datetime(df[f'{x} - Week']).dt.date


