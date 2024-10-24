#! /usr/bin/python3
import chess.pgn
import os
import sys
import time
import re



def file_contains_string(file_path, search_string): 
    try: 
        with open(file_path, 'r') as file: 
            # Read the file line by line 
            for line in file: 
                if search_string in line: 
                    return True 
        return False 
    except FileNotFoundError: 
        print(f"The file {file_path} does not exist.") 
        return False 
    except Exception as e: 
        print(f"An error occurred: {e}") 
        return False 
 

# Tis function split all PGN  games in PNG file into A00.png files to E99.png in openings directory

def split_file_pgn(file):
	if not os.path.exists("openings"):
		os.makedirs("openings")
	count=0
	with open(file, 'r') as fichier:
		pgn = chess.pgn.read_game(fichier)
		while pgn:
			try :
				eco=pgn.headers["ECO"]
				# convert A00a to A00 A00b to A00
				ecoshort=re.sub('[a-z]$','',eco)
				print (pgn, file=open("openings/"+ecoshort+".pgn" , "a"),end="\n\n")
			except:
				print("Game number ",count," without  ECO")
			count=count+1
			sys.stdout.write("Conversion: %d  \r" % (count) )
			sys.stdout.flush()

			
#read the next game
			pgn = chess.pgn.read_game(fichier)


# The script is launched as :
# pngsplitter.py file1.png file2.png
# A01.pgn ... E99.png are created in the directory where files png are stored


for fichier in  (sys.argv[1:]):
	print(fichier)
	split_file_pgn(fichier)


#for fichier in os.listdir("openings"):
#	name=os.path.splitext(fichier)[0]
#	print(name)
#	print (ECO[name])
#	if os.path.isfile("openings/"+fichier) and not os.path.islink(ECO[name]):
#		os.symlink("openings/"+fichier,"openings/"+ECO[name])
		




	

