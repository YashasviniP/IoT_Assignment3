# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV into a DataFrame
df1 = pd.read_csv('feeds-Station1.csv')
df2 = pd.read_csv('feeds-Station2.csv')

# Convert 'created_at' column to datetime format
df1['time'] = pd.to_datetime(df1['created_at'])
df2['time'] = pd.to_datetime(df2['created_at'])

# Calculate timestamp 5 hours ago
five_hours_ago = str(pd.Timestamp.now() - pd.Timedelta(hours=5))

# Filter DataFrame to keep data from the last 5 hours
df1 = df1[df1['time'] >= five_hours_ago]
df2 = df2[df2['time'] >= five_hours_ago]

# Plot Field1 [Temperature] vs Time for Station 1
plt.subplot(2, 2, 1)
plt.plot(df1['time'], df1['field1'], marker='o', color='blue')
plt.title('Station-1 Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')

# Plot Field2 [Humidity] vs Time for Station 1
plt.subplot(2, 2, 2)
plt.plot(df1['time'], df1['field2'], marker='o', color='green')
plt.title('Station-1 Humidity')
plt.xlabel('Time')
plt.ylabel('Humidity')

# Plot Field3 [Co2] vs Time for Station 1
plt.subplot(2, 2, 3)
plt.plot(df1['time'], df1['field3'], marker='o', color='red')
plt.title('Station-1 CO2')
plt.xlabel('Time')
plt.ylabel('Co2')

# Plot all fields together for Station 1
plt.subplot(2, 2, 4)
plt.plot(df1['time'], df1['field1'], marker='o', color='blue', label='Field1')
plt.plot(df1['time'], df1['field2'], marker='o', color='green', label='Field2')
plt.plot(df1['time'], df1['field3'], marker='o', color='red', label='Field3')
plt.title('Station-1 All Fields')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()

plt.show()

# Plot Field1 [Temperature] vs Time for Station 1
plt.subplot(1, 2, 1)
plt.plot(df1['time'], df1['field1'], marker='o', color='blue')
plt.title('Station-1 Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')

# Plot Field1 [Temperature] vs Time for Station 2
plt.subplot(1, 2, 2)
plt.plot(df2['time'], df2['field1'], marker='o', color='green')
plt.title('Station-2 Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')

plt.show()