import argparse
import string
ALPHABETS = string.ascii_uppercase

def enigma(wList1,wList2,wList3,pList,count,inp):

    cLists = convertLists(wList1,wList2,wList3,count)
    cList1 = cLists[0]
    cList2 = cLists[1]
    cList3 = cLists[2]

    p1 = cList1[inp]
    p2 = cList2[p1]
    p3 = cList3[p2]
    p4 = pList[p3]
    p5 = cList3.index(p4)
    p6 = cList2.index(p5)
    out = cList1.index(p6)
    return out

def convertLists(wList1,wList2,wList3,count):
    wList1Shift = count % len(wList1)
    wList2Shift = (count / len(wList2)) % len(wList2)
    wList3Shift = (count / (len(wList3) ** 2)) % len(wList3)

    clist1 = convertList(wList1,wList1Shift)
    clist2 = convertList(wList2,wList2Shift)
    clist3 = convertList(wList3,wList3Shift)

    return clist1,clist2,clist3

def convertList(list,rotation):
    clist = [0] * len(list)
    count = 0
    for v in list:
        if(count + rotation > len(list) - 1):
            clist[count + rotation - len(list)] = v
        else:
            clist[count + rotation] = v
        count += 1
    return clist

def char_to_int(char):
    char = char.upper()
    i = ALPHABETS.index(char)
    return i

def int_to_char(int):
    c = ALPHABETS[int]
    return c

parser = argparse.ArgumentParser(description="")
parser.add_argument("-r1",
		     type=int,
		     nargs="+",
		     help="rotor1"
		   )
parser.add_argument("-r2",
		     type=int,
		     nargs="+",
		     help="rotor2"
		   )
parser.add_argument("-r3",
		     type=int,
		     nargs="+",
		     help="rotor3"
		   )
parser.add_argument("-ref",
		     type=int,
		     nargs="+",
		     help="reflector"
		   )
parser.add_argument("-inp",
		     type=str,
		     help="inputString"
		   )

if __name__ == "__main__":
    args = parser.parse_args()
    wList1 = args.r1
    wList2 = args.r2
    wList3 = args.r3
    pList  = args.ref
    inp  = args.inp

count = 0

for char in inp:
    num  = char_to_int(char)
    out  = enigma(wList1,wList2,wList3,pList,count,num)
    rout = enigma(wList1,wList2,wList3,pList,count,out)
    print('count: %s inp: %s out: %s rout: %s result: %s' % (count,char,int_to_char(out),int_to_char(rout),num==rout))
    count += 1
