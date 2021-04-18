import os
import re


def process():
    original_files = os.listdir("C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\Keep\\3000_PDB_IDs")

    pattern = re.compile(r'^HEADER')

    file_counter = 0
    for file in original_files:
        new_file_name = "C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\Keep\\New_PDBs_No_Headers\\" + file[3:-4] + ".pdb"
        new_file = open(new_file_name, "w")

        ent_file_name = "C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\Keep\\3000_PDB_IDs\\" + file
        ent_file = open(ent_file_name, "r")
        new_lines = ent_file.readlines()
        lines = []
        for cur_line in new_lines:
            cur_line = cur_line.rstrip("\n")
            lines.append(cur_line)

        header_counter = 0
        for line in lines:
            result = pattern.search(line)
            if not result:
                new_file.write(line + "\n")
            else:
                header_counter += 1

        if header_counter != 1:
            print("Problem encoutered.")
            exit()

        file_counter += 1
        if file_counter % 100 == 0:
            print(file_counter)

        new_file.close()


if __name__ == "__main__":
    process()
