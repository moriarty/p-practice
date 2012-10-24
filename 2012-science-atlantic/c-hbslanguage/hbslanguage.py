'''
Problem C: HBS Language
'''

def main():
    try: 
        # Get the number of sample strings
        n = int(input())
    except NameError:
        print("Not an integer!")
        return -1
    ostr = ''
    for i in range(n):
        # For each string. (Maybe add try except later)
        istr = input()
        ostr += str(istr) #hbs_valid(s)
        if i < n-1:
            ostr += '\n'
    
    return ostr

if __name__ == '__main__':
    print main()
