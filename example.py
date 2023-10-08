import matplotlib.pyplot as plt
import pandas as pd

fname = "2023100609.CSV"

df = pd.read_csv(fname, index_col=0, header=None)
df = df.iloc[:, :-1]
df = df.T

df["Datetime_UTC"] = pd.to_datetime(df["Date"]) + pd.to_timedelta(df["Time"])
df.set_index("Datetime_UTC", inplace=True)
df.drop(
    columns=["Date", "Time", "Memo", "Sensor", "Wavelength(nm)"], inplace=True
)
df = df.astype(float)

# select and plot one measurement
spectrum = df.iloc[0][3:]

spectrum.plot()
plt.title(spectrum.name)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Irradiance (W/m2/um)")
plt.show()
