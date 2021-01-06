import pandas as pd


def max_min_anomalies(year1, year2, df):
    if year1 > year2:
        year1, year2 = year2, year1
    cut_df_in_a_range = df.loc[df['Year'].between(year1, year2)]
    print(f"La massima anomalia tra {year1} e {year2} è {cut_df_in_a_range['Mean'].max()}")
    print(f"La minima anomalia tra {year1} e {year2} è {cut_df_in_a_range['Mean'].min()}")


def createDict(df):
    modify_df = df.groupby('Year').mean()
    dictionary = modify_df.to_dict()
    final_dictionary = dictionary['Mean']
    return final_dictionary


df = pd.read_csv("annual.csv")
myDict=createDict(df)
print(myDict)
year1=int(input("Inserire la prima:"))
year2=int(input("Inserire la seconda:"))
max_min_anomalies(year1,year2,df)
