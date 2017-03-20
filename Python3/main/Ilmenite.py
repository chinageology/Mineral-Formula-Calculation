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
def Ilm_Calc(data, data_index):
    
    import numpy as np
    import pandas as pd
    print("------Magnetite formula Calculation------")
    print("The formula calculation of Magnetite only includede 10 elements: SiO2 Al2O3 TiO2 FeO MnO MgO CaO NiO V2O3 Cr2O3. If you have a different list, please rewrite the source code")
    input("Press ENTER to continue...")
    print()
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
    TFeO_wt = data['FeO']
    MnO_wt = data['MnO'] 
    MgO_wt = data['MgO']
    CaO_wt = data['CaO'] 
    NiO_wt = data['NiO'] 
    V2O3_wt = data['V2O3'] 
    Cr2O3_wt= data['Cr2O3']

#mol per 100g molecules
    SiO2_n = SiO2_wt / SiO2_M
    Al2O3_n = Al2O3_wt / Al2O3_M
    TiO2_n = TiO2_wt / TiO2_M
    TFeO_n = TFeO_wt / FeO_M
    MnO_n = MnO_wt / MnO_M
    MgO_n = MgO_wt / MgO_M
    CaO_n = CaO_wt / CaO_M
    NiO_n = NiO_wt / NiO_M
    V2O3_n = V2O3_wt / V2O3_M
    Cr2O3_n = Cr2O3_wt / Cr2O3_M
#Cation number
    SiO2_ca = SiO2_n
    Al2O3_ca = Al2O3_n * 2
    TiO2_ca = TiO2_n
    TFeO_ca = TFeO_n
    MnO_ca = MnO_n
    MgO_ca = MgO_n
    CaO_ca = CaO_n
    NiO_ca = NiO_n
    V2O3_ca = V2O3_n * 2
    Cr2O3_ca = Cr2O3_n * 2
#Total number of cations
    sum_ca = SiO2_ca + Al2O3_ca + TiO2_ca + TFeO_ca + MnO_ca + MgO_ca + CaO_ca + NiO_ca + V2O3_ca + Cr2O3_ca
        
#---Electrovalency Difference Calculation of Fe2+/Fe3+---     
#General formula of limenite is FeTiO3, calculate the cation ratio on the basis of 2
    ca_ratio = sum_ca / 2
    SiO2_co = SiO2_ca / ca_ratio
    Al2O3_co= Al2O3_ca / ca_ratio
    TiO2_co = TiO2_ca / ca_ratio
    TFeO_co = TFeO_ca / ca_ratio
    MnO_co = MnO_ca / ca_ratio
    MgO_co = MgO_ca / ca_ratio
    CaO_co = CaO_ca / ca_ratio
    NiO_co = NiO_ca / ca_ratio
    V2O3_co = V2O3_ca / ca_ratio
    Cr2O3_co = Cr2O3_ca / ca_ratio           
#Electrovalency of Cation ratio
    SiO2_el = SiO2_co * 4
    Al2O3_el = Al2O3_co * 3
    TiO2_el = TiO2_co * 4
    TFeO_el = TFeO_co * 2
    MnO_el = MnO_co * 2
    MgO_el = MgO_co * 2
    CaO_el = CaO_co * 2
    NiO_el = NiO_co * 2
    V2O3_el = V2O3_co * 3
    Cr2O3_el = Cr2O3_co * 3
    sum_el = SiO2_el + Al2O3_el + TiO2_el + TFeO_el + MnO_el + MgO_el + CaO_el + NiO_el + V2O3_el + Cr2O3_el
#Ideal Anion Electrovalency = O * 3 = 6
#Calculation of Fe3+ and Fe2+
    Fe2O3_co = 6 - sum_el
    FeO_co = TFeO_co - Fe2O3_co
    Fe2O3_wt = Fe2O3_co * ca_ratio * Fe2O3_M / 2
    FeO_wt = FeO_co * ca_ratio * FeO_M
    

#Anion number
    SiO2_an = SiO2_n * 2
    Al2O3_an = Al2O3_n * 3
    TiO2_an = TiO2_n * 2
    TFeO_an = TFeO_n
    MnO_an = MnO_n
    MgO_an = MgO_n
    CaO_an = CaO_n
    NiO_an = NiO_n
    V2O3_an = V2O3_n * 3
    Cr2O3_an = Cr2O3_n * 3
    
    sum_an = SiO2_an + Al2O3_an + TiO2_an + TFeO_an + MnO_an + MgO_an + CaO_an + NiO_an + V2O3_an + Cr2O3_an
    
    an_ratio = sum_an / 3
    
    sum_wt = SiO2_wt + TiO2_wt + Al2O3_wt + Fe2O3_wt + FeO_wt + MnO_wt + MgO_wt + CaO_wt + NiO_wt + V2O3_wt + Cr2O3_wt    
    
#Normalizing the wt% and then calculate the anion ratio on the basis of 3O
    SiO2_co3 = SiO2_wt / sum_wt * 100 / SiO2_M * 1 / an_ratio
    Al2O3_co3= Al2O3_wt / sum_wt * 100 / Al2O3_M * 2 / an_ratio
    TiO2_co3 = TiO2_wt / sum_wt * 100 / TiO2_M * 1 / an_ratio
    Fe2O3_co3 = Fe2O3_wt / sum_wt * 100 / Fe2O3_M * 2 / an_ratio
    FeO_co3 = FeO_wt / sum_wt * 100 / FeO_M * 1 / an_ratio
    MnO_co3 = MnO_wt / sum_wt * 100 / MnO_M * 1 / an_ratio
    MgO_co3 = MgO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    CaO_co3 = CaO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    NiO_co3 = NiO_wt / sum_wt * 100 / MgO_M * 1 / an_ratio
    V2O3_co3 = V2O3_wt / sum_wt * 100 / V2O3_M * 2 / an_ratio
    Cr2O3_co3 = Cr2O3_wt / sum_wt * 100 / Cr2O3_M * 2 /an_ratio
    
    
    sum_co = SiO2_co + Al2O3_co + TiO2_co + FeO_co + Fe2O3_co + MnO_co + MgO_co + CaO_co + NiO_co + V2O3_co + Cr2O3_co
    
    data_cali = {'SiO2': float("%.3f" % SiO2_wt),
                'TiO2': float("%.3f" % TiO2_wt),
                'Al2O3': float("%.3f" % Al2O3_wt),
                'Fe2O3': float("%.3f" % Fe2O3_wt),
                'FeO': float("%.3f" % FeO_wt),
                'MnO': float("%.3f" % MnO_wt),
                'MgO': float("%.3f" % MgO_wt),
                'CaO': float("%.3f" % CaO_wt),
                'NiO': float("%.3f" % NiO_wt),
                'V2O3': float("%.3f" % V2O3_wt),
                'Cr2O3': float("%.3f" % Cr2O3_wt),
                'Total': float("%.3f" % sum_wt),
                'Comment': data['Comment'],
                'Si': float("%.4f" % SiO2_co3), 
                'Ti': float("%.4f" % TiO2_co3),
                'Al': float("%.4f" % Al2O3_co3),
                'Fe3+': float("%.4f" % Fe2O3_co3),
                'Fe2+': float("%.4f" % FeO_co3),
                'Mn': float("%.4f" % MnO_co3),
                'Mg': float("%.4f" % MgO_co3),
                'Ca': float("%.4f" % CaO_co3),
                'Ni': float("%.4f" % NiO_co3),
                'V': float("%.4f" % V2O3_co3),
                'Cr': float("%.4f" % Cr2O3_co3)
                }
      
    return pd.DataFrame(data_cali, index = [data_index], columns = ['SiO2', 'TiO2', 'Al2O3', 'Fe2O3', 'FeO', 'MnO', 'MgO', 'CaO', 'NiO', 'V2O3', 'Cr2O3', 'Total', 'Comment', 'Si', 'Ti', 'Al', 'Fe3+', 'Fe2+', 'Mn', 'Mg', 'Ca', 'Ni', 'V', 'Cr'])
        
