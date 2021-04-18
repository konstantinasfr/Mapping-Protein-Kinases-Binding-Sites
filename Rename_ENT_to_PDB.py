import os
from shutil import copyfile


def process():
    original_files = os.listdir("C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\Keep\\3000_PDB_IDs")

    file_counter = 0
    for file in original_files:
        ent_file_name = "C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\Keep\\3000_PDB_IDs\\" + file
        new_file_name = "C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\Keep\\New_PDBs\\" + file[3:-4] + ".pdb"
        copyfile(ent_file_name, new_file_name)

        file_counter += 1
        if file_counter % 100 == 0:
            print(file_counter)


if __name__ == "__main__":
    process()
