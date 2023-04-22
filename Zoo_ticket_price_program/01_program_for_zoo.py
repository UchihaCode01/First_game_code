
while True:
    babies = 0
    children = 0
    pensioners = 0
    adult = 0

    amount_of_visitor = input(
        "\nEnter here a number of person, who want visit zoo : ")

    if amount_of_visitor == "":
        break
    else:
        amount_of_visitor = int(amount_of_visitor)
        for person in range(1, amount_of_visitor+1):
            age_of_person = int(
                input(f"\nEnter the age of {person} person : "))

            if age_of_person >= 0 and age_of_person < 3:
                babies += 1
            elif age_of_person > 2 and age_of_person < 13:
                children += 1
            elif age_of_person >= 65:
                pensioners += 1
            else:
                adult += 1

    price_is_free = babies * 0
    price_is_14_dollars = children * 14
    price_is_18_dollars = pensioners * 18
    price_is_23_dollars = adult * 23

    total_sum = int(price_is_free + price_is_14_dollars +
                    price_is_18_dollars + price_is_23_dollars)

    if babies > 0:
        print(
            f"\nYou should pay for {babies} baby/babies {price_is_free} dollars.")
    if children > 0:
        print(
            f"You should pay for {children} child/children {price_is_14_dollars} dollars.")
    if pensioners > 0:
        print(
            f"You should pay for {pensioners} pensioner/pensioners {price_is_18_dollars} dollars.")
    if adult > 0:
        print(
            f"You should pay for {adult} adult/adults {price_is_23_dollars} dollars.")

    print(f"\nYour total price for pay is : {total_sum:.2f} dollars.")
