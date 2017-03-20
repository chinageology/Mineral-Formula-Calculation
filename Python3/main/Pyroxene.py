# -*- coding: utf-8 -*-
"""
DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER

Copyright 2016 LiJie, lj201112@163.com

This file is part of Mineral Formula Calculation.
Mineral Formula Calculation is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Mineral Formula Calculation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along with Mineral Formula Calculation. If not, see <http://www.gnu.org/licenses/>.

Created on 2016/12/15
Author: LiJie
Email: lj201112@163.com
License: GNU Lesser General Public License (LGPL)

"""
def Py_Calc(data, data_index):
    
    import numpy as np
    import pandas as pd
    SiO2_M = 28.086 + 15.999 * 2
    Al2O3_M = 26.982 * 2 + 15.999 * 3
    TiO2_M = 47.867 + 15.999 * 2
    FeO_M = 55.845 + 15.999
    Fe2O3_M = 55.845 * 2 + 15.999 * 3
    MnO_M = 54.938 + 15.999
    MgO_M = 24.305 + 15.999
    CaO_M = 40.078 + 15.999
    Na2O_M = 22.990 * 2 + 15.999
    K2O_M = 39.098 * 2 + 15.999
    NiO_M = 58.693 + 15.999
    V2O3_M = 50.942 * 2 + 15.999 * 3
    Cr2O3_M = 51.996 * 2 + 15.999 * 3

    SiO2_wt = data['SiO2']
    Al2O3_wt = data['Al2O3']
    TiO2_wt = data['TiO2']
    TFeO_wt = data['FeO']
    MnO_wt = data['MnO'] 
    MgO_wt = data['MgO']
    CaO_wt = data['CaO'] 
    Cr2O3_wt= data['Cr2O3']
    K2O_wt = data['K2O']
    Na2O_wt = data['Na2O']
    
    SiO2_ca = SiO2_wt / SiO2_M
    Al2O3_ca = Al2O3_wt / Al2O3_M * 2
    TiO2_ca = TiO2_wt / TiO2_M
    TFeO_ca = TFeO_wt / FeO_M
    MnO_ca = MnO_wt / MnO_M
    MgO_ca = MgO_wt / MgO_M
    CaO_ca = CaO_wt / CaO_M
    Cr2O3_ca = Cr2O3_wt / Cr2O3_M * 2
    K2O_ca = K2O_wt / K2O_M * 2
    Na2O_ca = Na2O_wt / Na2O_M * 2
    
    sum_ca = SiO2_ca + Al2O3_ca + TiO2_ca + TFeO_ca + MnO_ca + MgO_ca + CaO_ca + Cr2O3_ca + K2O_ca + Na2O_ca
        
#---Electrovalency Difference Calculation of Fe2+/Fe3+---     
#General formula of pyroxene is XY[T2O6], calculate the cation ratio on the basis of 4
    ca_ratio = sum_ca / 4
    SiO2_co = SiO2_ca / ca_ratio
    Al2O3_co= Al2O3_ca / ca_ratio
    TiO2_co = TiO2_ca / ca_ratio
    TFeO_co = TFeO_ca / ca_ratio
    MnO_co = MnO_ca / ca_ratio
    MgO_co = MgO_ca / ca_ratio
    CaO_co = CaO_ca / ca_ratio
    Cr2O3_co = Cr2O3_ca / ca_ratio
    K2O_co = K2O_ca / ca_ratio
    Na2O_co = Na2O_ca / ca_ratio
      
#Electrovalency of Cation ratio
    SiO2_el = SiO2_co * 4
    Al2O3_el = Al2O3_co * 3
    TiO2_el = TiO2_co * 4
    TFeO_el = TFeO_co * 2
    MnO_el = MnO_co * 2
    MgO_el = MgO_co * 2
    CaO_el = CaO_co * 2
    Cr2O3_el = Cr2O3_co * 3
    K2O_el = K2O_co * 1
    Na2O_el = Na2O_co * 1
    
    sum_el = SiO2_el + Al2O3_el + TiO2_el + TFeO_el + MnO_el + MgO_el + CaO_el + Cr2O3_el + K2O_el + Na2O_el
#Ideal Anion Electrovalency = O * 6 = 12
#Calculation of Fe3+ and Fe2+
    Fe2O3_co = 12 - sum_el
    FeO_co = TFeO_co - Fe2O3_co
    Fe2O3_wt = Fe2O3_co * ca_ratio * Fe2O3_M / 2
    FeO_wt = FeO_co * ca_ratio * FeO_M
    
    if float(Fe2O3_wt) <= 0 or (FeO_wt) <= 0:
        Fe2O3_wt = 0.0
        FeO_wt = TFeO_wt
    
    sum_an = SiO2_ca * 2 + Al2O3_ca * 3 / 2 + TiO2_ca * 2 + FeO_wt / FeO_M * 1 + Fe2O3_wt / Fe2O3_M * 3 + MnO_ca * 1 + MgO_ca * 1 + CaO_ca * 1 + Cr2O3_ca / 2 * 3 + K2O_ca / 2  + Na2O_ca / 2
    
    an_ratio = sum_an / 6
#Normalizing the wt% and then calculate the anion ratio on the basis of 6O
    sum_wt = SiO2_wt + TiO2_wt + Al2O3_wt + Fe2O3_wt + FeO_wt + MnO_wt + MgO_wt + CaO_wt + Cr2O3_wt + K2O_wt + Na2O_wt
    
    SiO2_co2 = SiO2_wt / sum_wt * 100 / SiO2_M * 1 / an_ratio
    Al2O3_co2= Al2O3_wt / sum_wt * 100 / Al2O3_M * 2 / an_ratio
    TiO2_co2 = TiO2_wt / sum_wt * 100 / TiO2_M * 1 / an_ratio
    Fe2O3_co2 = Fe2O3_wt / sum_wt * 100 / Fe2O3_M * 2 / an_ratio
    FeO_co2 = FeO_wt / sum_wt * 100 / FeO_M * 1 / an_ratio
    MnO_co2 = MnO_wt / sum_wt * 100 / MnO_M * 1 / an_ratio
    MgO_co2 = MgO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    CaO_co2 = CaO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    Cr2O3_co2 = Cr2O3_wt / sum_wt * 100 / Cr2O3_M * 2 /an_ratio
    K2O_co2 = K2O_wt / sum_wt * 100 / K2O_M * 2 / an_ratio
    Na2O_co2 = Na2O_wt / sum_wt * 100 / Na2O_M * 2 / an_ratio
    Mg_value = MgO_ca / (MgO_ca + FeO_wt / FeO_M) * 100
    
    Al4 = np.nan
    Al6 = np.nan
    if float(SiO2_co2) < 2:
        if float(Al2O3_co2) < 2 - float(SiO2_co2):
            Al4 = float(Al2O3_co2)
            Al6 = 0 
        else:
            Al4 = 2 - float(SiO2_co2)
            Al6 = float(Al2O3_co2) - Al4
    else:
        Al4 = 0
        Al6 = Al2O3_co2
        
    data_cali = {
                'SiO2': float("%.3f" % SiO2_wt),
                'TiO2': float("%.3f" % TiO2_wt),
                'Al2O3': float("%.3f" % Al2O3_wt),
                'Fe2O3': float("%.3f" % Fe2O3_wt),
                'FeO': float("%.3f" % FeO_wt),
                'MnO': float("%.3f" % MnO_wt),
                'MgO': float("%.3f" % MgO_wt),
                'CaO': float("%.3f" % CaO_wt),
                'Cr2O3': float("%.3f" % Cr2O3_wt),
                'K2O': float("%.3f" % K2O_wt),
                'Na2O': float("%.3f" % Na2O_wt),
                'Total': float("%.3f" % sum_wt),
                'Comment': data['Comment'],
                'Si': float("%.4f" % SiO2_co2), 
                'Ti': float("%.4f" % TiO2_co2),
                'Al(4)': float("%.4f" % Al4),
                'Al(6)': float("%.4f" % Al6),
                'Fe3+': float("%.4f" % Fe2O3_co2),
                'Fe2+': float("%.4f" % FeO_co2),
                'Mn': float("%.4f" % MnO_co2),
                'Mg': float("%.4f" % MgO_co2),
                'Ca': float("%.4f" % CaO_co2),
                'Cr': float("%.4f" % Cr2O3_co2),
                'K': float("%.4f" % K2O_co2),
                'Na': float("%.4f" % Na2O_co2),
                'Mg#': float("%.2f" % Mg_value)
                }
      
    return pd.DataFrame(data_cali, index = [data_index], columns = ['SiO2', 'TiO2', 'Al2O3', 'Fe2O3', 'FeO', 'MnO', 'MgO', 'CaO', 'Cr2O3', 'K2O', 'Na2O', 'Total', 'Comment', 'Si', 'Ti', 'Al(4)', 'Al(6)', 'Fe3+', 'Fe2+', 'Mn', 'Mg', 'Ca', 'Cr', 'K', 'Na', 'Mg#'])
        
