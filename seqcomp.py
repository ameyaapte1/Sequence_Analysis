from Bio import SeqIO
from Bio.SeqUtils import GC
import sys

if(len(sys.argv) < 1):
    print("Usage python seqcomp.py fasta_file")
else:
    for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
        print("Sequence ID:  "+seq_record.id)
        print("Sequence :\n"+str(seq_record.seq))
        print("Sequence length "+str(len(seq_record))+"\n\n")
        ##print("Complement Sequence:\n"+str(seq_record.seq.complement())+"\n\n")
        print("Reverse Complement Sequence:\n"+str(seq_record.seq.reverse_complement())+"\n\n")
        
