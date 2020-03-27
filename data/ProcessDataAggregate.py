# AGGREGATE FINAL
import pandas as pd
confirmedData = pd.read_csv("time_series_covid19_confirmed_global.csv") 
deathData = pd.read_csv("time_series_covid19_deaths_global.csv")
recoveredData = pd.read_csv("time_series_covid19_recovered_global.csv")

new = confirmedData.filter([confirmedData.columns[1], confirmedData.columns[-1]], axis=1)
new.columns = ['Country', 'Confirmed']
aggregation_functions = {'Confirmed': 'sum'}
confirmed = new.groupby(new['Country']).aggregate(aggregation_functions)

#this will be the final table
Final = confirmed

new = deathData.filter([deathData.columns[1], deathData.columns[-1]], axis=1)
new.columns = ['Country', 'Death']
aggregation_functions = {'Death': 'sum'}
death = new.groupby(new['Country']).aggregate(aggregation_functions)

new = recoveredData.filter([recoveredData.columns[1], recoveredData.columns[-1]], axis=1)
new.columns = ['Country', 'Recovered']
aggregation_functions = {'Recovered': 'sum'}
recovered = new.groupby(new['Country']).aggregate(aggregation_functions)

Final = pd.merge(Final, death, on="Country")
Final = pd.merge(Final, recovered, on="Country")

Final = Final.rename(index={'US': 'United States', 'Bahamas' : 'Bahamas, The', 'Cabo Verde' : 'Cape Verde', 'Congo (Brazzaville)' : 'Congo, Republic of the', 'Congo (Kinshasa)': 'Congo, Democratic Republic of the', 'Czechia' : 'Czech Republic', 'Gambia' : 'Gambia, The', 'Holy See' : 'Holy See (Vatican City)', 'Taiwan*' : 'Taiwan'})

coronaData = pd.read_csv('corona_data.tsv',delimiter='\t',encoding='utf-8')
coronaData.drop('Confirmed', axis=1, inplace=True)
coronaData.drop('Death', axis=1, inplace=True)
coronaData.drop('Recovered', axis=1, inplace=True)
coronaData = coronaData.merge(Final, on="Country", how = 'left')

coronaData = coronaData.fillna(0)

coronaData.to_csv('Corona_Final.csv', index = True, header=True)

#Most Cases Table
import numpy as np
MostCases = coronaData.sort_values('Confirmed', ascending=False).head(10)

MostCases.drop('Population', axis=1, inplace=True)
MostCases.drop('id', axis=1, inplace=True)
MostCases = MostCases.astype({"Confirmed": int, "Death": int, "Recovered" : int})
MostCases.to_csv('MostCases.csv', index=False, header=True)

#Summary Table
TotalConfirmed = Final['Confirmed'].sum()
TotalDeath = Final['Death'].sum()
TotalRecovered = Final['Recovered'].sum()

d = {'Confirmed': [TotalConfirmed], 'Death': [TotalDeath], 'Recovered' : [TotalRecovered]}
Summary = pd.DataFrame(data=d)
Summary.to_csv('Summary.csv', index=False, header=True)