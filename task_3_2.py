n_of_guests = input('Enter number of guests: ')

n_of_guests = int (n_of_guests)

if n_of_guests >= 50:
    print('ресторан')
elif 50 > n_of_guests >= 20:
   print('кафе')
elif 20 > n_of_guests > 0:
    print('дом')
elif n_of_guests <= 0:
    print("Enter correct number")

