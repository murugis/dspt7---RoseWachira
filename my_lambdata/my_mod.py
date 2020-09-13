#my_lambdata/my_mod.py
def enlarge(n):
    """
    Param n is a number(either foat or interger is ok)

    Function will enlarge the number
    """
    return n * 100

if __name__=="__main__":

    print("HELLO")
    y=int(input("Please choose number"))
    print(y,enlarge(y))