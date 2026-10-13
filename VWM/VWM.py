from matplotlib.patheffects import withSimplePatchShadow

from functions import *
import pandas as pd
import io

#normalise
#1-(f-f_0)/f_0

def get_df(filename):
    results = np.loadtxt(filename, unpack=True, skiprows=2)

    df = pd.DataFrame({
        "t": results[0],
        "f": results[1],
        "x": results[2],
    })
    return df

#list of files
file_list = ["0.05.txt", "0.07.txt", "0.09.txt", "0.11.txt", "0.13.txt", "0.15.txt", "0.25.txt", "0.5.txt"]
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
df_25 = get_df(file_list[-2])
df_25.name = "0.25 mm/s"
df_50 = get_df(file_list[-1])
df_50.name = "0.5 mm/s"
df_17 = get_df("0.17.txt")
df_17.name = "0.17 mm/s"
df_21 = get_df("0.21.txt")
df_21.name = "0.21 mm/s"

#uncovered
df_05_u = get_df("0.05 uncovered.txt")
df_05_u.name = "0.05 mm/s uncovered"
df_15_u = get_df("0.15 uncovered.txt")
df_15_u.name = "0.15 mm/s uncovered"
df_25_u = get_df("0.25 uncovered.txt")
df_25_u.name = "0.25 mm/s uncovered"



#print(df_05.head())

df_list = [df_05, df_09, df_13, df_17, df_21, df_25, df_50]

#f(x)
fig, axes = plt.subplots(nrows=7, ncols=1, figsize=(8,8))
for i, df in enumerate(df_list):

    axes[i].scatter(df["x"], (df["f"]), label=df.name, marker=".")
    axes[i].set_xlabel("x [mm]")
    axes[i].set_ylabel("f [Hz]")
    axes[i].set_xlim(df["x"].min(), df["x"].max())
    axes[i].set_ylim(df["f"].min(), df["f"].max())
    axes[i].legend(loc="lower left")
    axes[i].grid()

fig.subplots_adjust(hspace =0.46)
plt.savefig("plots/f(x).png", bbox_inches="tight")
#plt.show()

#background reduction
#i guess lets first do this with the two points at the start and the end???
#f_0(t)
#def lin(x,a,b):
 #   return a*x + b

#fig, axes = plt.subplots(nrows=8, ncols=1, figsize=(8,8))
#for i, df in enumerate(df_list):
 #   a,b = optimal_params(lin, [df["t"].iloc[0], df["t"].iloc[-1]], [1/df["f"].iloc[0], 1/df["f"].iloc[-1]], None)
#    print((1/df["f"]-lin(df["t"],a.n,b.n)).max())
#    axes[i].scatter(df["t"], (1/df["f"]-lin(df["t"],a.n,b.n))/(1/df["f"]-lin(df["t"],a.n,b.n)).max(), label=df.name, marker=".")
#  #  axes[i].set_xlabel("t [s]")
 #   axes[i].set_ylabel(r"$f_{min}/f$ [a.u]")
 #   axes[i].set_ylim(0,1)
 #   axes[i].set_xlim(0,df["t"].iloc[-1])
 #   axes[i].legend()
 #   axes[i].grid()

#fig.subplots_adjust(hspace =0.312)

#f(t)
fig, axes = plt.subplots(nrows=7, ncols=1, figsize=(8,8))
for i, df in enumerate(df_list):

    axes[i].scatter(df["t"], (df["f"]), label=df.name, marker=".")
    axes[i].set_xlabel("t [s]")
    axes[i].set_ylabel("f [Hz]")
    axes[i].legend(loc="lower left")
    axes[i].set_xlim(df["t"].min(), df["t"].max())
    axes[i].set_ylim(df["f"].min(), df["f"].max())
    axes[i].grid()

fig.subplots_adjust(hspace =0.464)
plt.savefig("plots/f(t).png", bbox_inches="tight")

###merged (relative intensity)
#load data
def get_merged_df(filename):
    with open(filename, "r", encoding="utf-8-sig") as f:
        text = f.read()

    results = np.loadtxt(io.StringIO(text), unpack=True, delimiter=",")
    df = pd.DataFrame({
        "x": results[0],
        "I": results[1],
    })
    return df

merged_05 = get_merged_df("0.05-error-4.052057e-4.txt")
merged_05.name = "0.05 mm/s"
err_05 = 4.052057e-4

merged_09 = get_merged_df("0.09-error-4.500853e-4.txt")
merged_09.name = "0.09 mm/s"
err_09 = 4.500853e-4

merged_13 = get_merged_df("0.13-error-7.576557e-4.txt")
merged_13.name = "0.13 mm/s"
err_13 = 7.576557e-4

merged_15 = get_merged_df("0.15-error-1.502403e-3.txt")
merged_15.name = "0.15 mm/s"
err_15 = 1.502403e-3

merged_17 = get_merged_df("0.17-error-1.842828e-3.txt")
merged_17.name = "0.17 mm/s"
err_17 = 1.842828e-3

merged_21 = get_merged_df("0.21-error-2.097986e-3.txt")
merged_21.name = "0.21 mm/s"
err_21 = 2.097986e-3

merged_25 = get_merged_df("0.25-error-4.593151e-3.txt")
merged_25.name = "0.25 mm/s"
err_25 = 4.593151e-3

merged_50 = get_merged_df("0.5-error-7.203219e-2.txt")
merged_50.name = "0.5 mm/s"
err_50 = 7.203219e-2

merged_05_u = get_merged_df("0.05unc-error-2.965028e-3.txt")
merged_05_u.name = "0.05 mm/s uncovered"
err_05_u = 2.965028e-3

merged_15_u = get_merged_df("0.15unc-error-8.227634e-3.txt")
merged_15_u.name = "0.15 mm/s uncovered"
err_15_u = 8.227634e-3

merged_25_u = get_merged_df("0.25unc-error-3.035157e-2.txt")
merged_25_u.name = "0.25 mm/s uncovered"
err_25_u = 3.035157e-2

merged_list = [merged_05, merged_09, merged_13, merged_17, merged_21, merged_25, merged_50]
err_list = [err_05, err_09, err_13, err_17, err_21, err_25, err_50]

fig, axes = plt.subplots(nrows=7, ncols=1, figsize=(8,8))
for i, df in enumerate(merged_list):

    axes[i].scatter(df["x"], (df["I"]), label=df.name, marker=".")
    axes[i].set_xlabel("x [mm]")
    axes[i].set_ylabel(r"$1-\frac{\Delta f}{f_0}$ [a.u.]")
    axes[i].grid()
    axes[i].set_xlim(df["x"].min(), df["x"].max())
    axes[i].set_ylim(df["I"].min(), df["I"].max())
    axes[i].plot([], [], linestyle="none", label=(rf"$\sigma = {err_list[i]:.4f}$"))
    axes[i].legend(loc="upper right")

fig.subplots_adjust(hspace =0.43, bottom=0.1)
plt.savefig("plots/merged.png", bbox_inches="tight")


#covered vs uncovered --> different plot?
c_u_list = [merged_05, merged_05_u, merged_15, merged_15_u, merged_25, merged_25_u]
c_u_err_list = [err_05, err_05_u, err_15, err_15_u, err_25, err_25_u]
color_list = ["red", "red", "blue", "blue", "purple", "purple"]

fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(8,8))
for i, df in enumerate(c_u_list):
    axes[i].scatter(df["x"], (df["I"]), label=df.name, marker=".", color=color_list[i])
    axes[i].set_xlabel("x [mm]")
    axes[i].set_ylabel(r"$1-\frac{\Delta f}{f_0}$ [a.u.]")
    axes[i].plot([], [], linestyle="none", label=(rf"$\sigma = {c_u_err_list[i]:.4f}$"))
    axes[i].legend(loc="upper right")
    axes[i].grid()
    axes[i].set_xlim(df["x"].min(),df["x"].max())
    axes[i].set_ylim(df["I"].min(),df["I"].max())
fig.subplots_adjust(hspace =0.375)

plt.savefig("plots/covered_uncovered.png", bbox_inches="tight")

#FWHM
#use 0.09 mm/s
#make Gaussian fit
def gaussian(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2 * c**2))

p_0 = [1/(np.sqrt(2*np.pi)*1), 24.5, 1]

a,b,c = optimal_params(gaussian, merged_09["x"], merged_09["I"], err_09, p_0)
r2 = skm.r2_score(merged_09["I"], gaussian(merged_09["x"], a.n, b.n, c.n))
#max = gaussian(merged_09["x"], a.n, b.n, c.n).max()
FWHM = 2*np.sqrt(2*np.log(2))*c

fig, ax = plt.subplots()
ax.scatter(merged_09["x"], merged_09["I"], label=merged_09.name)
ax.plot(merged_09["x"], gaussian(merged_09["x"], a.n, b.n, c.n), color="red", label="Gaussian Fit")
a_str = str(a).replace("+/-", r"\pm")
b_str = str(b).replace("+/-", r"\pm")
c_str = str(c).replace("+/-", r"\pm")
FWHM_str = str(FWHM).replace("+/-", r"\pm")
plt.plot([],[],linestyle="none", label = (rf"$1-\frac{{\Delta f}}{{f_0}} = {a_str}\cdot \exp\left( - \frac{{x-({b_str})\,\text{{mm}}}}{{2\cdot (({c_str})\,\text{{mm}})^2}}\right)$" "\n" 
        rf"$R^2 = {r2:.3f}, \quad \text{{FWHM}}=({FWHM_str})\,\text{{mm}}$"))
ax.legend(loc="upper center")
ax.set_xlabel("x [mm]")
ax.set_ylabel(r"$1-\frac{\Delta f}{f_0}$ [a.u.]")
ax.set_xlim(merged_09["x"].min(),merged_09["x"].max())
ax.set_ylim(0,1.5)
plt.savefig("plots/beamwidth.png", bbox_inches="tight")


#baseline
results_bg = np.loadtxt("background.txt", unpack=True, skiprows=1)

background = pd.DataFrame({
    "t": results_bg[0],
    "f": results_bg[1],
    "x": results_bg[2],
})

fig, ax = plt.subplots()
ax.scatter(background["t"], background["f"], label=r"$f_0$")
ax.legend()
ax.grid()
ax.set_xlabel("t [s]")
ax.set_ylabel("f [Hz]")
ax.set_ylim(3015,3030)
plt.savefig("plots/background.png", bbox_inches="tight")

#calibration
I_real = uc.ufloat(78,1)#mW
dx = merged_09["x"].diff()
I_total = np.nansum((merged_09["I"]*dx).to_numpy())
print(I_total)
cal = I_real/I_total
print("a", cal)

#Probe
I_real_calc = np.nansum((merged_09["I"]*dx*cal.n).to_numpy())
print(I_real_calc)

fig, ax = plt.subplots()
ax.scatter(merged_09["x"], merged_09["I"]*cal.n, label=merged_09.name)
ax.legend()
ax.set_xlabel("x [mm]")
ax.set_ylabel(r"Transversal Intensity [mW/mm]")
ax.grid()
ax.set_xlim(merged_09["x"].min(),merged_09["x"].max())

plt.savefig("plots/real_intensity_profile.png", bbox_inches="tight")



plt.show()

#uncertainties merged plots!!

