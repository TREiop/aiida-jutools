#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Periodic table of elements;
contains: atomic number, period, group and IUPAC index for ordering
"""

__copyright__ = (u"Copyright (c), 2019-2020, Forschungszentrum Jülich GmbH, "
                 "IAS-1/PGI-1, Germany. All rights reserved.")
__license__ = "MIT license, see LICENSE.txt file"
__version__ = "0.1"
__contributors__ = u"Roman Kováčik"

ptable = {
    'X' : [ 0 , 0 , 100 , 1000 ],
    'H' : [ 1 , 1 , 1 , 106 ],
    'He' : [ 2 , 1 , 32 , 7 ],
    'Li' : [ 3 , 2 , 1 , 13 ],
    'Be' : [ 4 , 2 , 2 , 19 ],
    'B' : [ 5 , 2 , 27 , 93 ],
    'C' : [ 6 , 2 , 28 , 99 ],
    'N' : [ 7 , 2 , 29 , 105 ],
    'O' : [ 8 , 2 , 30 , 112 ],
    'F' : [ 9 , 2 , 31 , 118 ],
    'Ne' : [ 10 , 2 , 32 , 6 ],
    'Na' : [ 11 , 3 , 1 , 12 ],
    'Mg' : [ 12 , 3 , 2 , 18 ],
    'Al' : [ 13 , 3 , 27 , 92 ],
    'Si' : [ 14 , 3 , 28 , 98 ],
    'P' : [ 15 , 3 , 29 , 104 ],
    'S' : [ 16 , 3 , 30 , 111 ],
    'Cl' : [ 17 , 3 , 31 , 117 ],
    'Ar' : [ 18 , 3 , 32 , 5 ],
    'K' : [ 19 , 4 , 1 , 11 ],
    'Ca' : [ 20 , 4 , 2 , 17 ],
    'Sc' : [ 21 , 4 , 3 , 51 ],
    'Ti' : [ 22 , 4 , 18 , 55 ],
    'V' : [ 23 , 4 , 19 , 59 ],
    'Cr' : [ 24 , 4 , 20 , 63 ],
    'Mn' : [ 25 , 4 , 21 , 67 ],
    'Fe' : [ 26 , 4 , 22 , 71 ],
    'Co' : [ 27 , 4 , 23 , 75 ],
    'Ni' : [ 28 , 4 , 24 , 79 ],
    'Cu' : [ 29 , 4 , 25 , 83 ],
    'Zn' : [ 30 , 4 , 26 , 87 ],
    'Ga' : [ 31 , 4 , 27 , 91 ],
    'Ge' : [ 32 , 4 , 28 , 97 ],
    'As' : [ 33 , 4 , 29 , 103 ],
    'Se' : [ 34 , 4 , 30 , 110 ],
    'Br' : [ 35 , 4 , 31 , 116 ],
    'Kr' : [ 36 , 4 , 32 , 4 ],
    'Rb' : [ 37 , 5 , 1 , 10 ],
    'Sr' : [ 38 , 5 , 2 , 16 ],
    'Y' : [ 39 , 5 , 3 , 50 ],
    'Zr' : [ 40 , 5 , 18 , 54 ],
    'Nb' : [ 41 , 5 , 19 , 58 ],
    'Mo' : [ 42 , 5 , 20 , 62 ],
    'Tc' : [ 43 , 5 , 21 , 66 ],
    'Ru' : [ 44 , 5 , 22 , 70 ],
    'Rh' : [ 45 , 5 , 23 , 74 ],
    'Pd' : [ 46 , 5 , 24 , 78 ],
    'Ag' : [ 47 , 5 , 25 , 82 ],
    'Cd' : [ 48 , 5 , 26 , 86 ],
    'In' : [ 49 , 5 , 27 , 90 ],
    'Sn' : [ 50 , 5 , 28 , 96 ],
    'Sb' : [ 51 , 5 , 29 , 102 ],
    'Te' : [ 52 , 5 , 30 , 109 ],
    'I' : [ 53 , 5 , 31 , 115 ],
    'Xe' : [ 54 , 5 , 32 , 3 ],
    'Cs' : [ 55 , 6 , 1 , 9 ],
    'Ba' : [ 56 , 6 , 2 , 15 ],
    'La' : [ 57 , 6 , 3 , 49 ],
    'Ce' : [ 58 , 6 , 4 , 48 ],
    'Pr' : [ 59 , 6 , 5 , 47 ],
    'Nd' : [ 60 , 6 , 6 , 46 ],
    'Pm' : [ 61 , 6 , 7 , 45 ],
    'Sm' : [ 62 , 6 , 8 , 44 ],
    'Eu' : [ 63 , 6 , 9 , 43 ],
    'Gd' : [ 64 , 6 , 10 , 42 ],
    'Tb' : [ 65 , 6 , 11 , 41 ],
    'Dy' : [ 66 , 6 , 12 , 40 ],
    'Ho' : [ 67 , 6 , 13 , 39 ],
    'Er' : [ 68 , 6 , 14 , 38 ],
    'Tm' : [ 69 , 6 , 15 , 37 ],
    'Yb' : [ 70 , 6 , 16 , 36 ],
    'Lu' : [ 71 , 6 , 17 , 35 ],
    'Hf' : [ 72 , 6 , 18 , 53 ],
    'Ta' : [ 73 , 6 , 19 , 57 ],
    'W' : [ 74 , 6 , 20 , 61 ],
    'Re' : [ 75 , 6 , 21 , 65 ],
    'Os' : [ 76 , 6 , 22 , 69 ],
    'Ir' : [ 77 , 6 , 23 , 73 ],
    'Pt' : [ 78 , 6 , 24 , 77 ],
    'Au' : [ 79 , 6 , 25 , 81 ],
    'Hg' : [ 80 , 6 , 26 , 85 ],
    'Tl' : [ 81 , 6 , 27 , 89 ],
    'Pb' : [ 82 , 6 , 28 , 95 ],
    'Bi' : [ 83 , 6 , 29 , 101 ],
    'Po' : [ 84 , 6 , 30 , 108 ],
    'At' : [ 85 , 6 , 31 , 114 ],
    'Rn' : [ 86 , 6 , 32 , 2 ],
    'Fr' : [ 87 , 7 , 1 , 8 ],
    'Ra' : [ 88 , 7 , 2 , 14 ],
    'Ac' : [ 89 , 7 , 3 , 34 ],
    'Th' : [ 90 , 7 , 4 , 33 ],
    'Pa' : [ 91 , 7 , 5 , 32 ],
    'U' : [ 92 , 7 , 6 , 31 ],
    'Np' : [ 93 , 7 , 7 , 30 ],
    'Pu' : [ 94 , 7 , 8 , 29 ],
    'Am' : [ 95 , 7 , 9 , 28 ],
    'Cm' : [ 96 , 7 , 10 , 27 ],
    'Bk' : [ 97 , 7 , 11 , 26 ],
    'Cf' : [ 98 , 7 , 12 , 25 ],
    'Es' : [ 99 , 7 , 13 , 24 ],
    'Fm' : [ 100 , 7 , 14 , 23 ],
    'Md' : [ 101 , 7 , 15 , 22 ],
    'No' : [ 102 , 7 , 16 , 21 ],
    'Lr' : [ 103 , 7 , 17 , 20 ],
    'Rf' : [ 104 , 7 , 18 , 52 ],
    'Db' : [ 105 , 7 , 19 , 56 ],
    'Sg' : [ 106 , 7 , 20 , 60 ],
    'Bh' : [ 107 , 7 , 21 , 64 ],
    'Hs' : [ 108 , 7 , 22 , 68 ],
    'Mt' : [ 109 , 7 , 23 , 72 ],
    'Ds' : [ 110 , 7 , 24 , 76 ],
    'Rg' : [ 111 , 7 , 25 , 80 ],
    'Cn' : [ 112 , 7 , 26 , 84 ],
    'Nh' : [ 113 , 7 , 27 , 88 ],
    'Fl' : [ 114 , 7 , 28 , 94 ],
    'Mc' : [ 115 , 7 , 29 , 100 ],
    'Lv' : [ 116 , 7 , 30 , 107 ],
    'Ts' : [ 117 , 7 , 31 , 113 ],
    'Og' : [ 118 , 7 , 32 , 1 ],
}