#Funktionen und Dinge, die wichtig zu wissen sind
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import uncertainties as uc
import uncertainties.unumpy as unp
import tabulate as tl
import scipy.optimize as opt
import sklearn.metrics as skm

#futureWarnings von uncertainties ausschalten
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="uncertainties")

#Standardabweichung (Stichprobenvarianz) richtig berechnen:
#np.std(list, ddof=1)

#Mittelwert mit Fehler berechnen (berechnet Abweichung des Mittelwerts vom wahren Wert):
def get_mean (list):
    mean = np.mean(list)
    meanerr = np.std(list, ddof=1)/np.sqrt(len(list))
    return uc.ufloat(mean,meanerr) #returns mean as a ufloat


###fitten
#zuerst muss man die funktion definieren, die gefittet werden soll, wobei der erste parameter die unabhängige variable (x) sein muss:
#z.B. für lineare regression:
#def linreg(x,m,a):
    #return m*x+a


def optimal_params (function, xdata, ydata, yerr, p0=None):
    """
           gibt die optimalen Parameter und deren Fehler aus.

           :param function: vorher definierte Funktion, z.B. linreg
           :param xdata: Liste mit x-Werten (oder array)
           :param ydata: Liste mit y-Werten (oder array)
           :param yerr: Fehler auf y-Werte (scalar oder 1d-array)
           :param p0: Liste von initial guesses
           :return: tuple(?) der optimalen Parameter mit Fehlern als ufloat
           """
    params, cov = opt.curve_fit(function, np.asarray(xdata), np.asarray(ydata), p0=p0, nan_policy='omit', sigma=yerr, absolute_sigma=True)
    #creating correlated variables to handle correlation correctly
    param_with_errors = uc.correlated_values(params,cov)
    return param_with_errors


#Tabellen fürs Protokoll erstellen
def latex(data: list, headers: list):
    """Funktion für LaTeX Booktabs-Tabellen.

    :param data: table data as a list (of lists or arrays)(e.g. [x,y])
    :param headers: headers of the table as a list of strings (e.g. ["x","y"])"""
    #TODO: pandas-Unterstützung
    tab = np.array(data).transpose() #macht ein vertikales array aus dem horizontalen
    table = tl.tabulate(tab, headers=headers, tablefmt="latex_booktabs", numalign="center", stralign="center")
    return table

#Zusammengesetzten Messfehler aus statistischem Fehler und Messfehler des Messgeräts berechnen
def Gesamtfehler(Gerätfehler, Stabw):
    Gesfehler= np.sqrt(Stabw**2+Gerätfehler**2)
    return Gesfehler


