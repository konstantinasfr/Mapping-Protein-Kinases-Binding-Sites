#!/bin/bash




for dir in pdb_files_single_chains_no_ligands_corrected_res/*
do
#  echo $(basename $dir)
#  ./prank predict $(basename $dir)
#  echo -e $dir $"\n"> our_input.ds  
  printf $dir >> our_final_input.ds 
  printf "\n" >> our_final_input.ds 
done
