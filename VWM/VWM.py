from matplotlib.patheffects import withSimplePatchShadow

from functions import *
import pandas as pd


def get_df(filename):
    results = np.loadtxt(filename, unpack=True, skiprows=2)

    df = pd.DataFrame({
        "t": results[0],
        "f": results[1],
        "x": results[2],
    })
    return df

#list of files
file_list = ["0.05.txt", "0.07.txt", "0.09.txt", "0.11.txt", "0.13.txt", "0.15.txt"]
#list of dfs:
df_05 = get_df(file_list[0])
df_05.name = "0.05 mm/s"
df_07 = get_df(file_list[1])
df_07.name = "0.07 mm/s"
df_09 = get_df(file_list[2])
df_09.name = "0.09 mm/s"
df_11 = get_df(file_list[3])
df_11.name = "0.11 mm/s"
df_13 = get_df(file_list[4])
df_13.name = "0.13 mm/s"
df_15 = get_df(file_list[5])
df_15.name = "0.15 mm/s"

#print(df_05.head())

df_list = [df_05, df_07, df_09, df_11, df_13, df_15]

#plot results
fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(8,8))
for i, df in enumerate(df_list):
    axes[i].scatter(df["t"], 1/df["f"], label=df.name, marker=".")
    axes[i].set_xlabel("t [s]")
    axes[i].set_ylabel("f [Hz]")
    axes[i].legend()
    axes[i].grid()

fig.subplots_adjust(hspace =0.312, left=0.164)

#plt.show()

#background reduction
#i guess lets first do this with the two points at the start and the end???
#f_0(t)
def lin(x,a,b):
    return a*x + b

fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(8,8))
for i, df in enumerate(df_list):
    a,b = optimal_params(lin, [df["t"].iloc[0], df["t"].iloc[-1]], [1/df["f"].iloc[0], 1/df["f"].iloc[-1]], None)
    print((1/df["f"]-lin(df["t"],a.n,b.n)).max())
    axes[i].scatter(df["t"], (1/df["f"]-lin(df["t"],a.n,b.n))/(1/df["f"]-lin(df["t"],a.n,b.n)).max(), label=df.name, marker=".")
    axes[i].set_xlabel("t [s]")
    axes[i].set_ylabel(r"$f/f_{max}$ [a.u]")
    axes[i].set_ylim(0,1)
    axes[i].set_xlim(0,df["t"].iloc[-1])
    axes[i].legend()
    axes[i].grid()

fig.subplots_adjust(hspace =0.312)
plt.show()

a_05, b_05 = optimal_params(lin,[df_05["t"].iloc[0], df_05["t"].iloc[-1]], [1/df_05["f"].iloc[0], 1/df_05["f"].iloc[-1]], None)
print(a_05, b_05)

#axes[0].scatter(df_05["t"], df_05["f"]-lin(df_05["t"],a_05.n, b_05.n), marker=".")

fig, ax = plt.subplots()
ax.scatter(df_05["t"], 1/df_05["f"], label=df_05.name, marker=".")
ax.scatter(df_05["t"], lin(df_05["t"],a_05.n, b_05.n), marker=".")
ax.scatter(df_05["t"], 1/df_05["f"]-lin(df_05["t"],a_05.n, b_05.n), marker=".")

plt.show()