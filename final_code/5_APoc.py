import os
import re
import sys
import csv
import numpy as np


def process_2(pocket_1, pocket_2):
    positions1 = []
    with open(pocket_1,'r') as f:
        for line in f:
            j = 2
            sentence = []
            while "." not in line.split()[j]:
                sentence.append(line.split()[j])
                j += 1
            positions1.append(re.sub("[^0-9]", "",sentence[-1]))

    positions1 = [int(i) for i in positions1]
    positions1_unique = np.unique(positions1)
    pocket_len1 = len(positions1_unique)
    max1 = max(positions1) + round(pocket_len1*0.2)
    min1 = max(0,min(positions1) - round(pocket_len1*0.2))

    positions2 = []
    with open(pocket_2,'r') as f:
        for line in f:
            j = 2
            sentence = []
            while "." not in line.split()[j]:
                sentence.append(line.split()[j])
                j += 1
            positions2.append(re.sub("[^0-9]", "",sentence[-1]))

    positions2 = [int(i) for i in positions2]
    positions2_unique = np.unique(positions2)
    pocket_len2 = len(positions2_unique)
    max2 = max(positions2) + round(pocket_len2*0.2)
    min2 = max(0,min(positions2) - round(pocket_len2*0.2))

    if min(max1,max2) - max(min1,min2) < 0:
        overlap = 0
    else:
        overlap = 1

    return overlap


def process_1():
    pocket_folder = "C:\\Users\\georg\\Gathered\\MSc_Courses\\Summer_2021\\Algorithms_in_Structural_Biology\\Rework\\Pocket_PDBs\\convertions70\\"
    total_pocks = os.listdir(pocket_folder)
    simil_matrix = np.ones((len(total_pocks),len(total_pocks)))
    print(total_pocks)
    exit()

    for i in range(len(total_pocks)):
        for j in range(i+1,len(total_pocks)):
            print(str(i) + " " + str(j) + "   " + str(total_pocks[i]) + " " + str(total_pocks[j]))

            name_pocket_1 += pocket_folder + str(total_pocks[i])
            name_pocket_2 = pocket_folder + str(total_pocks[j])
            overlap = process_2(name_pocket_1, name_pocket_2)

            if overlap == 1:
                command = "apoc " + name_pocket_1 + " " + name_pocket_2 + " | awk -F'[ :]+' '/TM-score /{print $3}'"
                similarity = os.system(command)
                simil_matrix[i,j] = simil_matrix[j,i] = float(similarity)
            else:
                simil_matrix[i, j] = simil_matrix[j, i] = 0


if __name__ == "__main__":
    process_1()
