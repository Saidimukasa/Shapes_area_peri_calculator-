# Importing properties from the Shapes Files or Modules 
from Shapes_area_and_perimeter import * # We can use (*) to show that we are importing all
def main():
#     The Choices Function being Evoked 
    Choice()
#     Input loop
    while True:
        print()
        choice = input("Do you want to continue? (y(yes)/n(no)): ")
        if choice=='y' or choice=='Y':
            Choice()
        else:
            break
main()
    
    
