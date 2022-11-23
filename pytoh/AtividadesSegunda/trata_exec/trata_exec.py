if __name__ == "__main__":
    while True:
        try:
            x = int(input("Digite um inteiro:")) 
            print("Muito bem")
            break        

        except ValueError:
            for i in range(25):
                print("SEU BURRO")
            print("Seu animal, é um inteiro")
