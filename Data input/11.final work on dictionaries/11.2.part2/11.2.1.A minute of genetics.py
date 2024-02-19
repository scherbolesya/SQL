### A minute of genetics
As you know from the biology course, DNA and RNA are nucleotide sequences.
Four nucleotides in DNA:
adenine (A);
cytosine (C);
guanine (G);
thymine (T).
Four nucleotides in RNA:
adenine (A);
cytosine (C);
guanine (G);
uracil (U).
The RNA chain is built on the basis of the DNA chain by sequential addition of complementary nucleotides:
G → C;
C → G;
T → A;
A → U.
Write a program that converts a DNA strand into an RNA strand.
  
# Минутка генетики
Как известно из курса биологии ДНК и РНК – последовательности нуклеотидов.
Четыре нуклеотида в ДНК:
аденин (A);
цитозин (C);
гуанин (G);
тимин (T).
Четыре нуклеотида в РНК:
аденин (A);
цитозин (C);
гуанин (G);
урацил (U).
Цепь РНК строится на основе цепи ДНК последовательным присоединением комплементарных нуклеотидов:
G → C;
C → G;
T → A;
A → U.
Напишите программу, переводящую цепь ДНК в цепь РНК.###

a = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
for i in input():
    print(a[i], end = '')
  
Sample Input 1:
ACTG
Sample Output 1:
UGAC
Sample Input 2:
CC
Sample Output 2:
GG
Sample Input 3:
GTA
Sample Output 3:
CAU
