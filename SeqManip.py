# -*- coding: utf-8 -*-
"""
assingment No. 1
"""
#this DNA sequence was download and copy and pasted from https://github.com/jembrown/CompPhylo_Spr17/blob/master/CodingSeq.txt
DNA = 'aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg'
#print(DNA)
#the following command display a sentence and combined the length of the variable DNA with the setence to explain the meaning of the value
print("The lenght of the DNA sequence is = " + str (len(DNA)) + " base pairs")
#print(DNA)
#The following portion replace all the base pairs = t to u
RNA_equivalent = (DNA.replace("t","u"))
#print(RNA_equivalent)
#the following command create the complement string for the DNA sequence
rev_comp = ''
for i in RNA_equivalent:
    if i == 'a':
        rev_comp += 't'
    elif i == 'u':
        rev_comp += 'a'
    elif i == 'c':
        rev_comp += 'g'
    elif i == 'g':
        rev_comp += 'c'    
    else:
        rev_comp += i
#print(rev_comp)
next = "reversed complement"
#print(next)
#the following command reverse the DNA sequence and print in the screen
reverse = rev_comp[::-1]
print ('The reverse complement of the DNA sequence is : ')
print(reverse)
#part = (reverse[12:15])
#print (part + " cuantos hay")
#cuantos = len(part)
#print(cuantos)
#codon13 = 3*12
#print(codon13)
codons = [reverse[i:i+3] for i in range(0,len(reverse),3)]
#print(codons)
#nofcodons = len(codons)
#print(nofcodons)
Thirteen = (codons[12])
fourteen = (codons[13])
print(str (Thirteen )+ " and " + str ( fourteen ) + " are the bases corresponding 13rd and 14th codons respectetively")
"""
The following four lines is another way to extract and print the 13rd and 14th codons
"""
#extract_codon =(codons[12:14])
#print(extract_codon)
#print(codons)
#print (str (extract_codon) + 'are the bases corresponding 13rd and 14th codons respectetively')
"""
The following function translate the codons into aminoacids using the vertebrate mitochondrial genetic code 
evaluate the values of each individual codon, and if match change the values of the list to the assigned value for the code 
and create a new variable called translate, that contains the translated sequence 
"""
Translate = ''
for i in codons:
    if i == 'ttt' or i == 'ttc':
        Translate += 'F'
    elif i == 'tta' or i == 'ttg' or i == 'ctt' or i == 'ctc' or i == 'cta' or i == 'ctg':
        Translate += 'L'
    elif i == 'tct' or i == 'tcc' or i == 'tca' or i == 'tcg' or i == 'agt' or i == 'agc':
        Translate += 'S'
    elif i == 'tat' or i == 'tac':
        Translate += 'Y'
    elif i == 'taa' or i == 'tag':
        Translate += '*'
    elif i == 'tgt' or i == 'tgc' or i == 'aga' or i == 'agg':
        Translate += 'C'
    elif i == 'tga' or i== 'tgg':
        Translate += 'W'
    elif i == 'cct' or i == 'ccc' or i == 'cca' or i == 'ccg':
        Translate += 'P'
    elif i == 'cat' or i == 'cac':
        Translate += 'H'
    elif i == 'caa' or i == 'cag':
        Translate += 'Q'
    elif i == 'cgt' or i == 'cgc' or i == 'cga' or i == 'cgg':
        Translate += 'R'
    elif i == 'att' or i =='atc':
        Translate += 'I'
    elif i == 'ata' or i == 'atg':
        Translate += 'M'
    elif i == 'act' or i == 'acc' or i == 'aca' or i == 'acg':
        Translate += 'T'
    elif i == 'aat' or i == 'aac':
        Translate += 'N'
    elif i == 'aaa' or i == 'aag':
        Translate += 'K' 
    elif i == 'gtt' or i == 'gtc' or i == 'gta' or i == 'gtg':
        Translate += 'V'
    elif i == 'gct' or i == 'gcc' or i == 'gca' or i == 'gcg': 
        Translate += 'A'
    elif i == 'gat' or i == 'gac': 
        Translate += 'D'
    elif i == 'gaa' or i == 'gag':
        Translate += 'E'
    elif i == 'ggt' or i == 'ggc' or i == 'gga' or i == 'ggg':
        Translate += 'G'    
        
    else:
        Translate += i
print('The following is the translated sequence of the original DNA sequence: ' + str(Translate))
