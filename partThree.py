def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    print(pounds, percent) #test to see if what I did works
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    # TODO
    #d = d.removeprefix("£")
    #d = float(d)
    return float(d.removeprefix("£")) #removes the character "£" from the string and converts the string into a float, then returns the coverted variable

def percent_to_float(p):
    # TODO
    #p = p.removesuffix("%")
    #p = float(p)/100
    #return p
    return float(p.removesuffix("%"))/100 #removes the character "%" from the string, converts p into a float and divides the float by 100 to get a decimal percentage value, then returns the converted variable


main()
