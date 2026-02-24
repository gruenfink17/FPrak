#Funktionen und Dinge, die wichtig zu wissen sind
import numpy as np
import matplotlib.pyplot as plt
import uncertainties as uc
import tabulate as tl
import scipy.optimize as opt


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

def optimal_params (function, xdata, ydata, yerr):
    """
           gibt die optimalen Parameter und deren Fehler aus.

           :param function: vorher definierte Funktion, z.B. linreg
           :param xdata: Liste mit x-Werten
           :param ydata: Liste mit y-Werten
           :param yerr: Fehler auf y-Werte (scalar oder 1d-array)
           :return: Liste der optimalen Parameter mit Fehlern als ufloat
           """
    params, cov = opt.curve_fit(function, xdata, ydata, sigma=yerr, absolute_sigma=True)
    param_errors = np.sqrt(np.diag(cov))
    # Erstelle ufloats für jeden Parameter
    param_with_errors = [uc.ufloat(val, err) for val, err in zip(params, param_errors)]
    return param_with_errors


###fitten in einer funktion – bin mir sehr unsicher ob diese funktion hilfreich sein wird oder ob man letztendlich eh immer die zu fittende funktion definiert und dann einfach das obige verwendet


def generate_curve_func(equation, parameter_names):
    """
    Erzeugt eine Funktion für curve_fit aus einer mathematischen Gleichung als String.

    :param equation: String, z.B. 'm * x + a'
    :param parameter_names: Liste von Parameternamen, z.B. ['m', 'a']
    :return: Funktion, die in curve_fit verwendet werden kann
    """

    def func(x, *params):
        local_dict = {'x': x}
        # Parameter in local_dict einfügen
        for name, value in zip(parameter_names, params):
            local_dict[name] = value
        # Gleichung auswerten: wertet equation aus und ersetzt die parameter durch die params im local dict.
        # verwendet keine builtin funktionen.
        return eval(equation, {"__builtins__": None}, local_dict)

    return func


def fit_curve (equation,parameter_names,xdata,ydata, yerr, p0):
    """
        Verwendet generate_curve_func und macht damit den opt.curve_fit, gibt also die optimalen Parameter und deren Fehler aus.

        :param equation: String, z.B. 'm * x + a'
        :param parameter_names: Liste von Parameternamen, z.B. ['m', 'a']
        :param xdata: Liste mit x-Werten
        :param ydata: Liste mit y-Werten
        :param yerr: Fehler auf y-Werte (scalar oder 1d-array)
        :param p0: Initial guess, z.B. p0=[1,1]. Muss in der gleichen Reihenfolge sein wie parameter_names.
        :return: optimale Parameter mit Fehlern als ufloat
        """
    fit_func=generate_curve_func(equation, parameter_names)
    params, cov = opt.curve_fit(fit_func, xdata, ydata, p0=p0, sigma=yerr,absolute_sigma=True)
    param_errors = np.sqrt(np.diag(cov))
    # Erstelle ufloats für jeden Parameter
    param_with_errors = [uc.ufloat(val, err) for val, err in zip(params, param_errors)]
    return param_with_errors

#Tabellen fürs Protokoll erstellen
def latex(data: list, headers: list):
    """Funktion für LaTeX Booktabs-Tabellen.

    :param data: table data as a list (of lists or arrays)(e.g. [x,y])
    :param headers: headers of the table as a list of strings (e.g. ["x","y"])"""
    tab = np.array(data).transpose() #macht ein vertikales array aus dem horizontalen
    table = tl.tabulate(tab, headers=headers, tablefmt="latex_booktabs", numalign="center", stralign="center")
    return table

#Zusammengesetzten Messfehler aus statistischem Fehler und Messfehler des Messgeräts berechnen
def Gesamtfehler(Gerätfehler, Stabw):
    Gesfehler= np.sqrt(Stabw**2+Gerätfehler**2)
    return Gesfehler

#TODO: Funktion für Plots?
