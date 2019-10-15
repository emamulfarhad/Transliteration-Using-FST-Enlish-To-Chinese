#Transliteration using FST - English syllable to Chinese syllable

#Import library
from nltk.nltk_contrib.fst.fst import *
#Write the input and output in dat file
writedoc=open("eng_chi_tra.dat","a")
#declarition of fst class
class myFST(FST):    
    def recognize(self, iput, oput):
        self.inp = list(iput)
        self.outp = list(oput)
        if list(oput) == f.transduce(list(iput)):
            return True
        else:
            return False
        #return oput

f = myFST('transliteration')
#Loop for states
for i in range(1,5):
    f.add_state(str(i)) 
#declation of initial state
f.initial_state = '1'
#Assign all the syllable in states
f.add_arc('1', '2', ('vi'), ('wei'))
f.add_arc('2', '3', ('ta'), ('ta')) 
f.add_arc('3', '4', ('min'), ('ming'))
f.add_arc('1', '2', ('la'), ('na'))
f.add_arc('2', '4', ('tte'), ('tie'))
f.add_arc('1', '2', ('mo'), ('mo'))
f.add_arc('2', '4', ('cha'), ('ka'))
f.add_arc('1', '2', ('ti'), ('ti'))
f.add_arc('2', '3', ('ra'), ('la'))
f.add_arc('3', '3', ('mi'), ('mi'))
f.add_arc('3', '4', ('su'), ('su'))
f.add_arc('1', '3', ('bun'), ('beng'))
f.add_arc('3', '4', ('gee'), ('ji'))
f.add_arc('1', '3', ('la'), ('lei'))
f.add_arc('3', '4', ('ser'), ('she'))
f.add_arc('1', '2', ('hac'), ('hei'))
f.add_arc('2', '4', ('ker'), ('ke'))

#final state
f.set_final('4') 

#For showing the maping of syllable
map1=['vi','ta','min','la','tte','mo','cha','ti','ra','mi','su','bun','gee','la','ser','hac','hei']
map2=["wei","ta","ming","na","tie","mo","ka","ti","la","mi","su","beng","ji","lei","she","hei","ke"]
print("The maping English syllable to Chinese syllable","\n")
writedoc.write("The maping English syllable to Chinese syllable\n")
print("English ---> Chinese")
writedoc.write("English ---> Chinese")
for x in range(len(map1)): 
    print("  ",map1[x],"--->",map2[x])
    writedoc.write("\n   ")
    writedoc.write(map1[x])
    writedoc.write("--->")
    writedoc.write(map2[x])

#taking input
inp = input("Enter the word:")
#List for English word(inp1) that have trans in Chinese word(outp1), accordingly arranged
inp1=['vitamin','latte','mocha','tiramisu','bungee','laser','hacker']
outp1 = ["weitaming","natie","moka","tilamisu","bengji","leishe","heike"]
#loop for matching the words
for i in range(len(inp1)):
    if inp==inp1[i]:
        outp1=outp1[i]
outp=outp1

#For successfull transliteration
if f.recognize(inp, outp):
    print("\n English----->","Chinese","\n",inp,"----->",outp)
    writedoc.write("\nEnglish----->Chinese")
    writedoc.write("\n")
    writedoc.write(inp)
    writedoc.write("----->")
    writedoc.write(outp)
    print("The transliteration is accepted.")
    writedoc.write("\nThe transliteration is accepted.\n")
    
#For unsuccessful transliteration
else:
    print("The transliteration is rejected.")
    writedoc.write("\nThe transliteration is rejected. Because the input did not match. The input Was: ")
    writedoc.write(inp)
    writedoc.write("\n")

#Showing the mapping in diagram
disp = FSTDemo(f)
disp.mainloop()