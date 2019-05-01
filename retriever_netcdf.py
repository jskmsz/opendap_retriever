#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:53:00 2018

@author: Umbriel Miranda
"""

from netCDF4 import Dataset
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta


diaInicio = datetime.date.fromordinal(723546) #1st jan, 1982
diaFim = datetime.date(1992, 1, 1) # 10 anos de dados, só definir a data aqui

numeroDados = (((diaFim-diaInicio).days)//14)+1 #se der um numero quebrado de dados..

nome_arquivo = []
contador = 723546
#diaD = date_1 + datetime.timedelta(days=10)

for i in range(numeroDados+1): # dando loop para cada dia de dado (a cada 14 dias), coloquei +1 pra abarcar 10 anos
    if i == 0: #primeiro dia de dados
        diaD = diaInicio
        ano = diaD.year
        mes = diaD.month
        dias = diaD.day
        data_formatada = diaD.strftime("%Y%m%d")+"120000"
        nome_arquivo.append(data_formatada)
    else:
        diaD = diaInicio + datetime.timedelta(days=(i*14))
        ano = diaD.year
        mes = diaD.month
        dias = diaD.day
        data_formatada = diaD.strftime("%Y%m%d")+"120000"
        nome_arquivo.append(data_formatada)

print(diaInicio)
print(diaD)

param = "?lat[279:8:391],lon[480:8:800],analysed_sst[0:1:0][279:8:391][480:8:800],mask[0:1:0][279:8:391][480:8:800]"
matrixSST = np.empty((0, 391), int)

################################
# deprecated code below
# not sure if eligible to deletion
# as of 28/06/2018
#
#for i in range(1,524):
#    ano = diaInicio.year
#    if i <= 9:
#        dia = "00"+str(i)
#    elif i < 100:
#        dia = "0"+str(i)
#    else:
#        dia = str(i)
#    url = "https://podaac-opendap.jpl.nasa.gov:443/opendap/allData/ghrsst/data/GDS2/L4/GLOB/NCEI/AVHRR_OI/v2/" + str(ano) + \
#    "/" + str(dia) + "/" + nome_arquivo[i-1] + "-NCEI-L4_GHRSST-SSTblend-AVHRR_OI-GLOB-v02.0-fv02.0.nc"
#    data = Dataset(url+param)
#    sst = np.squeeze(data.variables['analysed_sst'][:], axis=0)
#    sst_corr = np.array(sst[~sst.mask]) - 273.15
#    matrixSST = np.vstack((matrixSST, sst_corr))
#
################################

for i in range(numeroDados+1):
    if i == 0:
        dia_cont = diaInicio
        dia = dia_cont.day
        ano = dia_cont.year
    else:
        dia_cont = diaInicio + datetime.timedelta(days=(i*14))
        if dia_cont.year == diaInicio.year:
            dia_dif = dia_cont - diaInicio
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=1)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=1))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=2)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=2))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=3)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=3))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=4)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=4))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=5)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=5))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=6)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=6))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=7)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=7))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=8)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=8))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=9)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=9))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
        elif dia_cont.year == (diaInicio + relativedelta(years=10)).year:
            dia_dif = dia_cont - (diaInicio + relativedelta(years=10))
            dia = int(dia_dif.days)+1
            ano = dia_cont.year
    if int(dia) <= 9:
        dia = "00"+str(dia)
    elif int(dia) < 100:
        dia = "0"+str(dia)
    else:
        dia = str(dia)
    url = "https://podaac-opendap.jpl.nasa.gov/opendap/allData/ghrsst/data/GDS2/L4/GLOB/NCEI/AVHRR_OI/v2/" + str(ano) + "/" + str(dia) + "/" + nome_arquivo[i] + "-NCEI-L4_GHRSST-SSTblend-AVHRR_OI-GLOB-v02.0-fv02.0.nc"
    print(url) # for testing
    data = Dataset(url+param)
    sst = np.squeeze(data.variables['analysed_sst'][:], axis=0)
    sst_corr = np.array(sst[~sst.mask]) - 273.15
    matrixSST = np.vstack((matrixSST, sst_corr))
      

#    np.append(matrixSST, sst_corr, axis=0)

#matrixSST = np.transpose(matrixSST)
np.savetxt('TSM_quinzenal.out', matrixSST, delimiter=',')