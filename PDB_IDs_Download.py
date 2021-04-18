from Bio.PDB import *


def process():
    pdb_ids_file = open("C:\\Users\\georg\\Gathered\\Μεταπτυχιακο_Μαθηματα\\Summer_2021\\Algorithms in Structural Biology\\Projects\\scPDB_Proteins_BindingSites.txt", "r")
    pdb_ids_only_file = open("C:\\Users\\georg\\Gathered\\Μεταπτυχιακο_Μαθηματα\\Summer_2021\\Algorithms in Structural Biology\\Projects\\scPDB_IDs.txt", "w")
    pdb_ids_only_file_list = open("C:\\Users\\georg\\Gathered\\Μεταπτυχιακο_Μαθηματα\\Summer_2021\\Algorithms in Structural Biology\\Projects\\scPDB_IDs_List.txt", "w")

    pdb_lines = pdb_ids_file.readlines()
    lines = []
    for new_line in pdb_lines:
        new_line = new_line.rstrip("\n")
        lines.append(new_line)

    counter_pdbs = 0
    pdb_list = []
    for line in lines:
        splited_1 = line.split("||")
        pdb_id_extended = splited_1[0]
        splited_2 = pdb_id_extended.split("_")
        pdb_id = splited_2[0]
        counter_pdbs += 1
        pdb_ids_only_file.write(pdb_id + "\n")
        pdb_ids_only_file_list.write(pdb_id + ", ")
        pdb_list.append(pdb_id)

        if counter_pdbs % 100 == 0:
            print(counter_pdbs)

        if len(pdb_id) != 4:
            print("This PDB ID should be examined further...")
            print(pdb_id)
            exit()

    print("PDB IDs:")
    print(len(pdb_list))

    pdbl = PDBList()
    # First was: [:1000]
    # Second was: [1000:3001]
    # Fourth was: [3001:5000]
    pdb_list = pdb_list[1000:3001]
    print(pdb_list)
    print(len(pdb_list))
    # pdbl.retrieve_pdb_file(pdb_id, pdir="C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\PDB_Files", file_format="pdb")
    pdbl.download_pdb_files(pdb_list, pdir="C:\\Users\\georg\\PycharmProjects\\Titled1\\Msc\\Algorithms_in_Structual_Bioinformatics\\Project\\PDB_Files", file_format="pdb")

    pdb_ids_file.close()
    pdb_ids_only_file.close()
    pdb_ids_only_file_list.close()


if __name__ == "__main__":
    process()
