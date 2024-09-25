# Part 1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'F:\DSA\Week 3\archive (1)\dailyActivity_merged.csv')
print(df.head())
print(df.columns)
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
daily_steps = df.groupby('ActivityDate')['TotalSteps'].sum().reset_index()
list1 = daily_steps['ActivityDate'] 
list2 = daily_steps['TotalSteps']
plt.figure(figsize=(12, 6))
plt.plot(list1, list2, marker='o', color='blue')
plt.title('Total Number of Steps on Daily Basis')
plt.xlabel('Date')
plt.ylabel('Total Steps')
plt.xticks(rotation=45)
plt.show()


# Part 2
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'F:\DSA\Week 3\archive (1)\dailyActivity_merged.csv')
print(df.head())
print(df.columns)
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
daily_distance = df.groupby('ActivityDate')['TotalDistance'].sum().reset_index()
list1 = daily_distance['ActivityDate']  
list2 = daily_distance['TotalDistance'] 
plt.figure(figsize=(12, 6))
plt.bar(list1, list2, color='green', width=0.5)  
plt.title('Total Distance Covered on Daily Basis')
plt.xlabel('Date')
plt.ylabel('Total Distance')
plt.xticks(rotation=45)
plt.show()


# Part 3
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'F:\DSA\Week 3\archive (1)\sleepDay_merged.csv')
print(df.head())
print(df.columns)
df['SleepDay'] = pd.to_datetime(df['SleepDay'])
list1 = df['SleepDay']  
list2 = df['TotalTimeInBed'] 
plt.figure(figsize=(12, 6))
plt.scatter(list1, list2, color='orange', alpha=0.5) 
plt.title('Total Time in Bed on Daily Basis')
plt.xlabel('Date')
plt.ylabel('Total Time in Bed')
plt.xticks(rotation=45)
plt.show()


# Part 4
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'F:\DSA\Week 3\archive (1)\hourlySteps_merged.csv')
print(df.head())
print(df.columns)
df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])
april_12_data = df[df['ActivityHour'].dt.date == pd.to_datetime('2016-04-12').date()]
hourly_steps = april_12_data.groupby(april_12_data['ActivityHour'].dt.hour)['StepTotal'].sum()
plt.figure(figsize=(8, 8))
plt.pie(hourly_steps, labels=hourly_steps.index, autopct='%1.1f%%')
plt.title('Hourly Steps on April 12, 2016')
plt.show()

