def temp_converter():
    print("\nTemperature converter")
    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")

    pick = input("pick 1 or 2: ")
    if pick == "1":
        c = float(input("celsius ? "))
        f = c * 9/5 + 32
        print(c, "°C is", round(f, 2), "°F")  

    elif pick == "2":
        f = float(input("fahrenheit ? "))
        c = (f - 32) * 5/9
        print(f, "°F is", round(c, 2), "°C")

    else:
        print("try again my friend")
def length_stuff():
   print("\nLength converter")
   print("1. Kilometers to meters")
   print("2. meters to Kilometers")
   choice = input("choose: ")
   if choice == "1":
        km = float(input("how many km ? "))
        print(km, "km =", km*1000, "meters")

   elif choice == "2":
        m = float(input("how many meters: "))
        print(m, "m =", m/1000, "km")

   else:
        print("invalid boss")
def weight_converter():
    print("\nWeight Converter")
    print("1. kg to grams")
    print("2. grams to kg")
    choice = input("choose: ")
    if choice == "1":
        kg = float(input("kilograms ? "))
        print(kg, "kg =", kg * 1000, "grams")

    elif choice == "2":
        g = float(input("grams pls ? "))
        print(g, "g =", g / 1000, "kg")
    else:
        print("beep beep try again!!")
def main():

    print("Guys welcome to my unit Converter") 
    while True:
        print("\no=o=o=o=o=o=o=o=o=o=o=o")
        print("1 temp")
        print("2 length")
        print("3 weight")
        print("4 quit")
        print("o=o=o=o=o=o=o=o=o=o=o=o")
        
        ans = input("\nwhat do u want > ").lower().strip()
        
        if ans in ["1", "temp", "temperature"]:
            temp_converter()
        elif ans in ["2", "len", "length"]:
            length_stuff()
        elif ans in ["3", "weight", "w"]:
            weight_converter()
        elif ans in ["4", "quit", "exit", "bye", "q"]:
            print("bye bye")
            break
        else:
            print(" type a real option ")
if __name__ == "__main__":
    main()