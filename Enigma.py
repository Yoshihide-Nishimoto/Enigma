import argparse
import string
ALPHABETS = string.ascii_uppercase

def enigma(rotor1,rotor2,rotor3,reflector,count,inp):

    cRotors = convertRotors(rotor1,rotor2,rotor3,count)
    cRotor1 = cRotors[0]
    cRotor2 = cRotors[1]
    cRotor3 = cRotors[2]

    p1 = cRotor1[inp]
    p2 = cRotor2[p1]
    p3 = cRotor3[p2]
    p4 = reflector[p3]
    p5 = cRotor3.index(p4)
    p6 = cRotor2.index(p5)
    out = cRotor1.index(p6)
    return out

def convertRotors(rotor1,rotor2,rotor3,count):
    rotor1Shift = count % len(rotor1)
    rotor2Shift = (count / len(rotor2)) % len(rotor2)
    rotor3Shift = (count / (len(rotor3) ** 2)) % len(rotor3)

    cRotor1 = convertRotor(rotor1,rotor1Shift)
    cRotor2 = convertRotor(rotor2,rotor2Shift)
    cRotor3 = convertRotor(rotor3,rotor3Shift)

    return cRotor1,cRotor2,cRotor3

def convertRotor(list,rotation):
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
    return c.upper()

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
    rotor1 = args.r1
    rotor2 = args.r2
    rotor3 = args.r3
    reflector = args.ref
    inp  = args.inp

    count = 0
    for char in inp:
        num  = char_to_int(char)
        out  = enigma(rotor1,rotor2,rotor3,reflector,count,num)
        rout = enigma(rotor1,rotor2,rotor3,reflector,count,out)
        print('count: %s inp: %s out: %s rout: %s result: %s' % (count,char,int_to_char(out),int_to_char(rout),num==rout))
        count += 1
