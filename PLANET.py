import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('planets')

print("First 5 rows:")
print(df.head())

print()

print(df.info())

print()

print(df.describe())

print()

print("Years:", df['year'].unique())





sns.histplot(data=df, x='year', bins=20, color='steelblue')

plt.title('Distrbution of exoplanet decovries by year')

plt.xlabel('Decovry Year')

plt.ylabel('Count')

plt.show()




sns.kdeplot(data=df, x='distance', fill=True, log_scale=True)

plt.title('Distance shape (KDE)')

plt.xlabel('Distance (parsecs - log scale)')

plt.show()




sns.histplot(data=df, x='orbital_period', log_scale=True, kde=True, color='coral')

plt.title('Orbital period — histgram with kde curve')

plt.xlabel('Orbital period (Days - log scale)')

plt.ylabel('Count')

plt.show()




sns.scatterplot(data=df, x='orbital_period', y='distance')

plt.xscale('log')

plt.yscale('log')

plt.title('Orbital period vs distance graph')

plt.xlabel('Orbital period (Days - log scale)')

plt.ylabel('Distance (parsecs - log scale)')

plt.show()




corr = df.corr(numeric_only=True)

print("Corelation table:")

print(corr)

print()




sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title('Corelation heatmap — planet measurments')

plt.show()





