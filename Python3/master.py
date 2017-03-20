# -*- coding: utf-8 -*-
"""
DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER

Copyright 2016 LiJie, lj201112@163.com

Mineral Formula Calculation is free software: you can redistribute it and / or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Mineral Formula Calculation is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along with Mineral Formula Calculation. If not, see <http://www.gnu.org/licenses/>.

Created on 2016/12/15
Author: LiJie
Email: lj201112@163.com
License: GNU Lesser General Public License (LGPL)

"""
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(sys.argv[0])) + os.sep + 'main')

width = 50
print()
print('=' * width)
print("Mineral Formula Calculation")
print('-' * width)
print("Created on 2016/12/15")
print("Author: LiJie")
print("Email: lj201112@163.com")
print("License: GNU Lesser General Public License (LGPL)")
print('=' * width)
print()

import numpy as np
import pandas as pd
filename = input('Input the filename with ".xls" extension and press ENTER:\n>>>')

names = pd.ExcelFile(filename).sheet_names

filename_output = str(filename.split('.')[len(filename.split('.')) -2] + "_calc" + '.' + filename.split('.')[len(filename.split('.')) -1])
names_new = {}

if 'mag' in names:
    import Magnetite
    df = pd.read_excel(filename, sheetname = 'mag', index_col = 0)
    row_index = np.linspace(1, len(df.index), len(df.index))
    df_mag = pd.DataFrame()
    for i in row_index:
        df_mag = df_mag.append(Magnetite.Mag_Calc(df.loc[int(i)], int(i)))
    names_new['mag'] = df_mag
    print("Magnetite calculations finished")
    
    
if 'ol' in names:
    import Olivine
    df = pd.read_excel(filename, sheetname = 'ol', index_col = 0)
    row_index = np.linspace(1, len(df.index), len(df.index))
    df_ol = pd.DataFrame()
    for i in row_index:
        df_ol = df_ol.append(Olivine.Ol_Calc(df.loc[int(i)], int(i)))
    names_new['ol'] = df_ol
    print("Olivine calculations finished")
   
if 'py' in names:
    import Pyroxene
    df = pd.read_excel(filename, sheetname = 'py', index_col = 0)
    row_index = np.linspace(1, len(df.index), len(df.index))
    df_py = pd.DataFrame()
    for i in row_index:
        df_py = df_py.append(Pyroxene.Py_Calc(df.loc[int(i)], int(i)))
    names_new['py'] = df_py
    print("Pyroxene calculations finished")
        
if 'fd' in names:
    import Feldspar
    df = pd.read_excel(filename, sheetname = 'fd', index_col = 0)
    row_index = np.linspace(1, len(df.index), len(df.index))
    df_fd = pd.DataFrame()
    for i in row_index:
        df_fd = df_fd.append(Feldspar.Fd_Calc(df.loc[int(i)], int(i)))
    names_new['fd'] = df_fd
    print("Feldspar calculations finished")
    
if 'ilm' in names:
    import Ilmenite
    df = pd.read_excel(filename, sheetname = 'ilm', index_col = 0)
    row_index = np.linspace(1, len(df.index), len(df.index))
    df_ilm = pd.DataFrame()
    for i in row_index:
        df_ilm = df_ilm.append(Ilmenite.Ilm_Calc(df.loc[int(i)], int(i)))
    names_new['ilm'] = df_ilm
    print("Ilmenite calculations finished")
    
with pd.ExcelWriter(filename_output) as writer:
    i = 0
    while (i < len(names)):
        names_new[names[i]].to_excel(writer, sheet_name = names[i])
        i += 1
print()
print("Calculations successfully finished")
print("Results are stored in %s \n" % filename_output)
print("Press ENTER to exit the program...")
input()
sys.exit()