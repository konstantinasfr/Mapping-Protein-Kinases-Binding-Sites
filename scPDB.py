import re


def process():
    pattern_aa = re.compile(r'^\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+)')

    f_new = open("C:\\Users\\georg\\Gathered\\Μεταπτυχιακο_Μαθηματα\\Summer_2021\\Algorithms in Structural Biology\\Projects\\scPDB_Proteins_BindingSites.txt", "w")

    start = False
    counter_lines = 0
    amino_acids_list = []
    sites_counter = 0
    with open("E:\\scPDB\\scPDB") as file_go:
        for line in file_go:
            counter_lines += 1
            line = line.rstrip("\n")

            if counter_lines % 1000000 == 0:
                print(counter_lines)

            if "scPDB" in line and "site" in line:
                line = line.replace("\x00", "")
                splited = line.split("/")
                pdb_id = splited[1]
                start = True
                aa_region = False
                amino_acids_list = []
                sites_counter += 1

            if start:
                result_aa = pattern_aa.search(line)
                if result_aa:
                    aa_region = True
                    amino_acid = result_aa.group(1)
                    if amino_acid not in amino_acids_list:
                        amino_acids_list.append(amino_acid)
                else:
                    if aa_region:
                        start = False
                        f_new.write(pdb_id)
                        for i in amino_acids_list:
                            f_new.write("||" + i)
                        f_new.write("\n")
    f_new.close()
    print()
    print("Binding sites found:")
    print(sites_counter)


if __name__ == "__main__":
    process()

