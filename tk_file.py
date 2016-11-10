#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
from Bio import SeqIO
import tkFileDialog
table = 11
min_pro_len = 100

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title('Open Reading Frame')
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Open', command=self.onOpen)
        menubar.add_cascade(label='File', menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):

        ftypes = [('Fasta files', '*.fasta'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            self.ORF(fl)
    
    def ORF(self,filename):
        for seq_record in SeqIO.parse(filename, "fasta"):
            for strand, nuc in [(+1, seq_record.seq), (-1, seq_record.seq.reverse_complement())]:
                for frame in range(3):
                    length = 3 * ((len(seq_record)-frame) // 3) #Multiple of three
                    for pro in nuc[frame:frame+length].translate(table).split("*"):
                        if len(pro) >= min_pro_len:
                            text="%s\n - length %i, strand %i, frame %i\n\n" % (pro[0:], len(pro), strand, frame)
                            self.txt.insert(END, text)




def main():

    root = Tk()
    ex = Example(root)
    root.geometry('300x250+300+300')
    root.mainloop()


if __name__ == '__main__':
    main()

			
