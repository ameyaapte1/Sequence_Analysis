from Bio import SeqIO
from Bio.SeqUtils import GC
import sys

if(len(sys.argv) < 2):
    print("Usage python gc.py fasta_file ")
else:
    for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
        print("Sequence ID:  "+seq_record.id)
        print("Sequence :\n"+str(seq_record.seq))
        print("Sequence length "+str(len(seq_record))+"\n")
        print("GC content: "+str(GC(seq_record.seq))+"\n")
        print("A :"+str(100.00*seq_record.seq.count("A")/len(seq_record))+"%")
        print("T :"+str(100.00*seq_record.seq.count("T")/len(seq_record))+"%")
        print("G :"+str(100.00*seq_record.seq.count("G")/len(seq_record))+"%")
        print("C :"+str(100.00*seq_record.seq.count("C")/len(seq_record))+"%")
        print("\n")
        
