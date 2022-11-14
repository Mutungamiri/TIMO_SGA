import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects
from matplotlib import ticker
from __init__ import structure
from numpy import *
import matplotlib
import pandas as pd
from mpl_toolkits import mplot3d

class ReturnFunc:
    def __init__(self):
        self.obj = "-1"
        self.ci1 = "-1"
        self.ci2 = "-1"
        self.ci3 = "-1"
        self.ci4 = "-1"
        self.ci5 = "-1"
        self.nvar = "0"

    def func(self, x):

        obj = self.obj
        ci1 = self.ci1
        ci2 = self.ci2
        ci3 = self.ci3
        ci4 = self.ci4
        ci5 = self.ci5
        return [obj, ci1, ci2, ci3, ci4, ci5]


def func(x):
    obj = eval(funkcja_obj)
    ci1 = eval(funkcjaDlaApp.ci1)
    ci2 = eval(funkcjaDlaApp.ci2)
    ci3 = eval(funkcjaDlaApp.ci3)
    ci4 = eval(funkcjaDlaApp.ci4)
    ci5 = eval(funkcjaDlaApp.ci5)
    return [obj, ci1, ci2, ci3, ci4, ci5]

# Definicja zmiennych
funkcjaDlaApp = ReturnFunc()
funkcja_obj=-1
ogr_1=-1
ci1=-1
lista_ograniczen =[]


# Definicja problemu
problem = structure()
problem.costfunc = func
problem.nvar = int(funkcjaDlaApp.nvar)
problem.varmin = []
problem.varmax = []
problem.cons_flag=["NRow","NRow","NRow","NRow","NRow"]
problem.button_counter = 0
# Parametry GA
paramsy = structure()
paramsy.maxit = 69
paramsy.npop = 20
paramsy.beta = 1
paramsy.pc = 1
paramsy.gamma = 0.1
paramsy.mu = 0.1
paramsy.sigma = 0.1
paramsy.crosspro = 0.8

##########################################testy drukowania
def plot_graph(problem, pop, current_it, bestcost):


    matplotlib.use("Agg")
    tolerance = 0.001
    n_values = 100
    # Z = problem.costfunc[0]
    costfunc = problem.costfunc
    # constraints=costfunc[1:]
    # constraints_count = len(problem.costfunc[1:])
    varmin_p = problem.varmin     #[startx, starty]
    varmax_p = problem.varmax     #[stopx, stopy]
    start_pos = [0] * problem.nvar
    stop_pos = [0] * problem.nvar
    X = [0] * problem.nvar
    pos_vals = [0] * problem.nvar
    for var_it in range(problem.nvar):
        start_pos[var_it], stop_pos[var_it] = varmin_p[var_it], varmax_p[var_it]
        pos_vals[var_it] = np.linspace(start_pos[var_it], stop_pos[var_it], n_values)


    if len(X) == 2:
        X[0], X[1] = np.meshgrid(pos_vals[0], pos_vals[1])
    elif len(X) == 3:
        X[0], X[1], X[2] = np.meshgrid(pos_vals[0], pos_vals[1], pos_vals[2])
    elif len(X) == 4:
        X[0], X[1], X[2], X[3] = np.meshgrid(pos_vals[0], pos_vals[1], pos_vals[2], pos_vals[3])
    elif len(X) == 5:
        X[0], X[1], X[2], X[3], X[4] = np.meshgrid(pos_vals[0], pos_vals[1], pos_vals[2], pos_vals[3], pos_vals[4])
    Z = problem.costfunc(X)[0]

    konsy=[0] * problem.button_counter
    for button_counter_plot in range(0, problem.button_counter):
        if button_counter_plot == 0:
            konsy[0]=problem.costfunc(X)[1]
            Z[konsy[0] >= 0] = nan
        if button_counter_plot == 1:
            konsy[1]=problem.costfunc(X)[2]
            Z[konsy[1] >= 0] = nan
        if button_counter_plot == 2:
            konsy[2]=problem.costfunc(X)[3]
            Z[konsy[2] >= 0] = nan
        if button_counter_plot == 3:
            konsy[3]=problem.costfunc(X)[4]
            Z[konsy[3] >= 0] = nan
        if button_counter_plot == 4:
            konsy[4]=problem.costfunc(X)[5]
            Z[konsy[4] >= 0] = nan

    # for con in constraints:
    #     Z[con >= 0] = nan


    # for counter_it in range(problem.button_counter):
    #     if counter_it==0:
    #         if problem.cons_flag[0]=='NRow': # cons_flag nie jest iterowane
    #             Z[costfunc(X[0], X[1])[1]-tolerance > 0] = nan
    #         elif problem.cons_flag[0]=='Row':
    #             Z[costfunc(X[0], X[1])[1] >= 0] = nan
    #         elif problem.cons_flag[0]=='ORow':
    #             Z[costfunc(X[0], X[1])[1] >= 0] = nan
    #     if counter_it==1:
    #         if problem.cons_flag[2] == 'NRow':
    #             Z[costfunc(X[0], X[1])[2] - tolerance > 0] = nan
    #         elif problem.cons_flag[2] == 'Row':
    #             Z[costfunc(X[0], X[1])[2] >= 0] = nan
    #         elif problem.cons_flag[2] == 'ORow':
    #             Z[costfunc(X[0], X[1])[2] >= 0] = nan
    #     if counter_it==2:
    #         if problem.cons_flag[2] == 'NRow':
    #             Z[costfunc(X[0], X[1])[3] - tolerance > 0] = nan
    #         elif problem.cons_flag[2] == 'Row':
    #             Z[costfunc(X[0], X[1])[3] >= 0] = nan
    #         elif problem.cons_flag[2] == 'ORow':
    #             Z[costfunc(X[0], X[1])[3] >= 0] = nan
    #     if counter_it==3:
    #         if problem.cons_flag[3] == 'NRow':
    #             Z[costfunc(X[0], X[1])[4] - tolerance > 0] = nan
    #         elif problem.cons_flag[3] == 'Row':
    #             Z[costfunc(X[0], X[1])[4] >= 0] = nan
    #         elif problem.cons_flag[3] == 'ORow':
    #             Z[costfunc(X[0], X[1])[4] >= 0] = nan
    #     if counter_it==4:
    #         if problem.cons_flag[4] == 'NRow':
    #             Z[costfunc(X[0], X[1])[5] - tolerance > 0] = nan
    #         elif problem.cons_flag[4] == 'Row':
    #             Z[costfunc(X[0], X[1])[5] >= 0] = nan
    #         elif problem.cons_flag[4] == 'ORow':
    #             Z[costfunc(X[0], X[1])[5] >= 0] = nan




    # n_values = 100
    # startx, stopx = -1.5, 1.5
    # starty, stopy = -1.5, 1.5
    # x_vals = np.linspace(startx, stopx, n_values)
    # y_vals = np.linspace(starty, stopy, n_values)
    # X, Y = np.meshgrid(x_vals, y_vals)
    # Z = (1 - X) ** 2 + 100 * (Y - X ** 2) ** 2
    # Z[X ** 2 + Y ** 2 - 2 >= 0] = nan


    # Opcje osi
    fig = plt.figure(figsize=(6, 5))
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes([left, bottom, width, height])
    ax.set_title('Badany obszar')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # Wyswietlanie warstwic
    cp = plt.contourf(X[0], X[1], Z, 90, cmap='RdGy') # locator=ticker.LogLocator(subs=range(1,10))
    for element in range(len(pop)):
        if pop[element].cost==bestcost:
            plt.scatter(pop[element].position[0], pop[element].position[1], c='teal', s=12)


    plt.colorbar(cp)

    # Zapisywanie
    org_string = "Graphs/imageN.png"
    new_string = org_string.replace('N', str("0")) #new_string = org_string.replace('N', str(current_it))
    plt.savefig(new_string, bbox_inches='tight')
    print(new_string)
    plt.close('all')






# def plot_graph(problem, pop, end_flag):
#
#
#     # Przekazywanie zakresu wspolrzednych - done
#     # Przekazywanie funkcji - done
#     # Przekazywanie ograniczen
#     # Przekazanie punktow - osobnikow - done
#     n_values = 100
#     constraints=problem.costfunc[1:]
#     varmin_p = problem.varmin     #[startx, starty]
#     varmax_p = problem.varmax     #[stopx, stopy]
#     start_pos=[]
#     stop_pos=[]
#     for var in range(problem.nvar):
#         start_pos[var], stop_pos[var] = varmin_p[var], varmax_p[var]
#         pos_vals = np.linspace(start_pos[var],stop_pos[var], n_values)
#     Z = problem.costfunc[0]
#     for element in range(len(pop)):
#
#         # n_values = 100
#         # startx, stopx = -1.5, 1.5
#         # starty, stopy = -1.5, 1.5
#         # x_vals = np.linspace(startx, stopx, n_values)
#         # y_vals = np.linspace(starty, stopy, n_values)
#         # X, Y = np.meshgrid(x_vals, y_vals)
#         # Z = (1 - X) ** 2 + 100 * (Y - X ** 2) ** 2
#         # Z[X ** 2 + Y ** 2 - 2 >= 0] = nan
#         for con in constraints:
#             Z[con>=0] = nan
#
#
#         # Opcje osi
#         fig = plt.figure(figsize=(6,5))
#         left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
#         ax = fig.add_axes([left, bottom, width, height])
#
#         # Wyswietlanie warstwic
#         cp = plt.contourf(X, Y, Z,90, locator=ticker.LogLocator(subs=range(1,10)), cmap='RdGy') #90 RdGy
#         # plt.imshow(Z, extent=[-1.5, 1.5, -1.5, 1.5], cmap='RdGy')
#
#         if end_flag:
#             plt.scatter(pop[element].position[0], pop[element].position[1], c='navy', s=12)
#         else:
#             plt.scatter(pop[element].position[0], pop[element].position[1], c='blue', s=7)
#         plt.colorbar(cp)
#         ax.set_title('Badany obszar')
#         ax.set_xlabel('x')
#         ax.set_ylabel('y')
#         # plt.show()
#         # plt.draw()
#         # Zapisywanie
#         #
#         org_string = "Graphs/imageN.png"
#         new_string = org_string.replace('N', str(element))
#         plt.savefig(new_string, bbox_inches='tight')
#         print(new_string)
#         plt.close()
























# Funkcja testowa
# def func(x):
#     # obj = ((1-x[0])**2)+100*(x[1]-x[0]**2)**2
#     # ci1=(x[0]**2+x[1]**2)-2
#     # ci2 =-1+x[0]
#
#     # obj = ((1-x[0])**2)+100*(x[1]-x[0]**2)**2
#     # ci1= (x[0]-1)**3-x[1]+1
#     # ci2=x[0]+x[1]-2
#
#     # obj = sin(x[1])*np.exp((1-cos(x[0]))**2)+cos(x[0])*np.exp((1-sin(x[1]))**2)+(x[0]-x[1])**2
#     # ci1 = ((x[0]+5)**2+((x[1])+5)**2)-25
#     # ci2 = -1
#
#     # obj = 4*x[0]**2-2.1*x[0]**4+1/3*x[0]**6+x[0]*x[1]-4*x[1]**2+4*x[1]**4
#     # ci1 = -1*sin(4*x[0]*np.pi)+2*sin(2*np.pi*x[1])**2-1.5
#     # ci2 = -1
#
#     # obj = ((x[0]-2)**2)+((x[1]-1)**2)
#     # ci1 = -2+x[0]+x[1]
#     # ci2 = -x[1]+(x[0])**2
#
#     return [obj, ci1, ci2]

# # Definicja problemu
# problem = structure()
# problem.costfunc = func
# problem.nvar = 2
# #######
# # problem.varmin = [-1.5, -0.5]
# # problem.varmax = [1.5, 2.5]
#
# # problem.varmin = [-1.5, -1.5]
# # problem.varmax = [1.5, 1.5]
#
# # problem.varmin = [-10, -6.5]
# # problem.varmax = [0, 0]
#
# # problem.varmin = [-1, -1]
# # problem.varmax = [0.75, 1]
#
# # problem.varmin = [-2, 0]
# # problem.varmax = [3, 4]
# #############
# problem.constraints=[];
#
# #Parametry GA
# params = structure()
# params.maxit = 150
# params.npop = 20
# params.beta = 1
# params.pc = 1
# params.gamma = 0.1
# params.mu = 0.1
# params.sigma = 0.1
# params.crosspro = 0.8
# Algorytm genetyczny
# out = ga.run(problem, params)

# Wynik
# plt.plot(out.bestcost)
# plt.xlim(0, params.maxit)
# plt.xlabel('iterations')
# plt.ylabel('best cost')
# plt.title('GA')
# plt.grid(True)
# plt.show()