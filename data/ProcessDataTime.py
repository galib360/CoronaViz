#Final
import pandas as pd
confirmedData = pd.read_csv("time_series_covid19_confirmed_global.csv") 
deathData = pd.read_csv("time_series_covid19_deaths_global.csv")
recoveredData = pd.read_csv("time_series_covid19_recovered_global.csv")

tempDF = deathData.sum(axis=0)
tempDF = tempDF.drop([tempDF.index[0] , tempDF.index[1]])

#tempDF = pd.DataFrame(data=tempDF)

tempDF = tempDF.reset_index()
tempDF.columns = ["date", "deathFreq"]
DeathTimeSeries = tempDF
#DeathTimeSeries
tempDF = confirmedData.sum(axis=0)
tempDF = tempDF.drop([tempDF.index[0] , tempDF.index[1]])

#tempDF = pd.DataFrame(data=tempDF)

tempDF = tempDF.reset_index()
tempDF.columns = ["date", "confirmedFreq"]
ConfirmedTimeSeries = tempDF

tempDF = recoveredData.sum(axis=0)
tempDF = tempDF.drop([tempDF.index[0] , tempDF.index[1]])

#tempDF = pd.DataFrame(data=tempDF)

tempDF = tempDF.reset_index()
tempDF.columns = ["date", "recoveredFreq"]
RecoveredTimeSeries = tempDF

TotalTimeSeries = ConfirmedTimeSeries.join(DeathTimeSeries.set_index('date'), on='date')
TotalTimeSeries = TotalTimeSeries.join(RecoveredTimeSeries.set_index('date'), on='date')
TotalTimeSeries.reset_index(level=0, inplace=True)
TotalTimeSeries.to_csv('TotalTimeSeries.csv', index = True, header=True)
TotalTimeSeries.to_json('TotalTimeSeries.json', orient="records", index = True)