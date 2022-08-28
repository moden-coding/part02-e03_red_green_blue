#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    
    with open(filename, "r") as f:
        f.readline()
        result = []
        expression = "\s?(\d{1,3})\s*(\d{1,3})\s*(\d{1,3})\s*(.*)"
        for line in f:
            mo = re.findall(expression,line)
            if mo:
                
                temp = ""
                for i in range(3):
                    temp += str(mo[0][i])
                    temp += "\t"

                temp += mo[0][3]
                result.append(temp)
            
    return result


def main():
    li = red_green_blue()
    print()


if __name__ == "__main__":
    main()
