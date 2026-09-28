def trans():
    while True:
        try:
            choice = input("\n1. Цельсій в фаренгейт\n2. Фаренгейт в цельсій\n")

            if choice == "1":
                celsia = float(input("Цельсій = "))
                farangeit = (celsia * 1.8) + 32
                print(f"Відповідь: {farangeit:.2f} F")

            elif choice == "2":
                farangeit = float(input("Введи Фаренгейт = "))
                celsia = (farangeit - 32) * 5 / 9
                print(f"Відповідь: {celsia:.2f} °C")

            else:
                print("німа")
                choice2 = input("\nПовторити? 1 так 2 ні ")

                if choice2 != "1":
                    break

        except ValueError:
            print("Цифри пиши як треба")


if __name__ == "__main__":
    trans()
