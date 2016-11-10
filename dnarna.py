from Bio import SeqIO
from Bio.SeqUtils import GC
import sys


if(len(sys.argv) < 3):
    print("Usage: python dnarna.py -r/d fasta_file ")
else:
    for seq_record in SeqIO.parse(sys.argv[2], "fasta"):
        print("Sequence ID:  "+seq_record.id)
        print("Sequence length "+str(len(seq_record))+"\n")
        print("Input Sequence :\n"+str(seq_record.seq))
        if(sys.argv[1] == "-d"):
            print("DNA Sequence:\n"+str(seq_record.seq.back_transcribe())+"\n")
            print("cDNA Sequence:\n"+str(seq_record.seq.back_transcribe().reverse_complement())+"\n")
        if(sys.argv[1] == "-p"):
            print("RNA Sequence:\n"+str(seq_record.seq.transcribe())+"\n")
            print("Protien Sequence:\n"+str(seq_record.seq.translate())+"\n")
        print("\n")
