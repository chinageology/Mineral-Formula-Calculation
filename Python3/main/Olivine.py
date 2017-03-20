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
def Ol_Calc(data, data_index):
    
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
# mass percent of the elements
    SiO2_wt = data['SiO2']
    Al2O3_wt = data['Al2O3']
    TiO2_wt = data['TiO2']
    FeO_wt = data['FeO']
    MnO_wt = data['MnO'] 
    MgO_wt = data['MgO']
    CaO_wt = data['CaO'] 
    NiO_wt = data['NiO'] 
    Cr2O3_wt= data['Cr2O3']
    
    sum_wt = data['Total']
#Normalized Cation number
    SiO2_ca = SiO2_wt / sum_wt * 100 / SiO2_M
    Al2O3_ca = Al2O3_wt / sum_wt * 100 / Al2O3_M * 2
    TiO2_ca = TiO2_wt / sum_wt * 100 / TiO2_M
    FeO_ca = FeO_wt / sum_wt * 100 / FeO_M
    MnO_ca = MnO_wt / sum_wt * 100 / MnO_M
    MgO_ca = MgO_wt / sum_wt * 100 / MgO_M
    CaO_ca = CaO_wt / sum_wt * 100 / CaO_M
    NiO_ca = NiO_wt / sum_wt * 100 / NiO_M
    Cr2O3_ca = Cr2O3_wt / sum_wt * 100 / Cr2O3_M * 2
    
    sum_ca = SiO2_ca + Al2O3_ca + TiO2_ca + FeO_ca + MnO_ca + MgO_ca + CaO_ca + NiO_ca + Cr2O3_ca
    
    ca_ratio = sum_ca / 3

#Normalized Anion number
    SiO2_an = SiO2_wt / sum_wt * 100 / SiO2_M * 2
    Al2O3_an = Al2O3_wt / sum_wt * 100 / Al2O3_M * 3
    TiO2_an = TiO2_wt / sum_wt * 100 / TiO2_M * 2
    FeO_an = FeO_wt / sum_wt * 100 / FeO_M
    MnO_an = MnO_wt / sum_wt * 100 / MnO_M
    MgO_an = MgO_wt / sum_wt * 100 / MgO_M
    CaO_an = CaO_wt / sum_wt * 100 / CaO_M
    NiO_an = NiO_wt / sum_wt * 100 / NiO_M
    Cr2O3_an = Cr2O3_wt / sum_wt * 100 / Cr2O3_M * 3
    
    sum_an = SiO2_an + Al2O3_an + TiO2_an + FeO_an + MnO_an + MgO_an + CaO_an + NiO_an + Cr2O3_an

    an_ratio = sum_an / 4

#Normalizing to 100%wt and then calculate the cation ratio on the basis of 4O
    SiO2_co = SiO2_wt / sum_wt * 100 / SiO2_M * 1 / an_ratio
    Al2O3_co= Al2O3_wt / sum_wt * 100 / Al2O3_M * 2 / an_ratio
    TiO2_co = TiO2_wt / sum_wt * 100 / TiO2_M * 1 / an_ratio
    FeO_co = FeO_wt / sum_wt * 100 / FeO_M * 1 / an_ratio
    MnO_co = MnO_wt / sum_wt * 100 / MnO_M * 1 / an_ratio
    MgO_co = MgO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    CaO_co = CaO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    NiO_co = NiO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    Cr2O3_co = Cr2O3_wt / sum_wt * 100 / Cr2O3_M * 2 /an_ratio
    
    Fo = MgO_wt / MgO_M / (MgO_wt / MgO_M + FeO_wt / FeO_M) * 100
        
    data_cali = {'SiO2': float("%.3f" % SiO2_wt),
                'TiO2': float("%.3f" % TiO2_wt),
                'Al2O3': float("%.3f" % Al2O3_wt),
                'FeO': float("%.3f" % FeO_wt),
                'MnO': float("%.3f" % MnO_wt),
                'MgO': float("%.3f" % MgO_wt),
                'CaO': float("%.3f" % CaO_wt),
                'NiO': float("%.3f" % NiO_wt),
                'Cr2O3': float("%.3f" % Cr2O3_wt),
                'Total': float("%.3f" % sum_wt),
                'Comment': data['Comment'],
                'Si': float("%.4f" % SiO2_co), 
                'Ti': float("%.4f" % TiO2_co),
                'Al': float("%.4f" % Al2O3_co),
                'Fe2+': float("%.4f" % FeO_co),
                'Mn': float("%.4f" % MnO_co),
                'Mg': float("%.4f" % MgO_co),
                'Ca': float("%.4f" % CaO_co),
                'Ni': float("%.4f" % NiO_co),
                'Cr': float("%.4f" % Cr2O3_co),
                'Fo': float("%.2f" % Fo)
                }

    return pd.DataFrame(data_cali, index = [data_index], columns = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MnO', 'MgO', 'CaO', 'NiO', 'Cr2O3', 'Total', 'Comment', 'Si', 'Ti', 'Al', 'Fe2+', 'Mn', 'Mg', 'Ca', 'Ni', 'Cr', 'Fo'])

        
