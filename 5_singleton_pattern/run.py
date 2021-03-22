from chocolate_boiler import ChocolateBoiler

if __name__ == '__main__':
    cb1 = ChocolateBoiler.get_instance()
    print(cb1)
    cb2 = ChocolateBoiler.get_instance()
    print(cb2)
    print(cb1 == cb2)

    if id(cb1) == id(cb2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")