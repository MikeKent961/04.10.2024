import math  

def main():
    inputA = int(input("First vaule: ")) #user inputs value of first leg of triangle 
    inputB = int(input("Second value: ")) #user input value of second leg of triangle
    outputC = pythag(inputA, inputB) #calls pythag with the two user inputs and the output result of pythag will be assigned to outputC as the length of the hypotenuse
    print("Hypotenuse = " , outputC) #prints the result


def pythag(A,B):
 return round(math.sqrt((A**2) + (B**2)), 2) #receives the two triangle values, adds together the square of each value, squareroots the sum, rounds it to 2 decimal places, and returns it straight away.

main()
