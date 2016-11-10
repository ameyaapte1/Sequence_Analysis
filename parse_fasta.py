from Bio import SeqIO
table = 11
min_pro_len = 100
for seq_record in SeqIO.parse("test.fasta", "fasta"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(repr(seq_record.seq.complement()))
        print(repr(seq_record.seq.reverse_complement()))
        print(repr(seq_record.seq.transcribe()))
        print(len(seq_record))
for strand, nuc in [(+1, seq_record.seq), (-1, seq_record.seq.reverse_complement())]:
     for frame in range(3):
         length = 3 * ((len(seq_record)-frame) // 3) #Multiple of three
         for pro in nuc[frame:frame+length].translate(table).split("*"):
             if len(pro) >= min_pro_len:
                 print("%s...%s - length %i, strand %i, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))
