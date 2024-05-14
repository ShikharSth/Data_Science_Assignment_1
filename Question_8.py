# Create a tuple of your favorite colors and print it. Check if a certain color is present in the tuple and print the result.

tuple_fav_color = ('green', 'blue', 'red', 'black')
tuple_fav_color
check = 'green'
if check in tuple_fav_color:
    print(check, "is in the tuple.")
else:
    print(check, "is not in the tuple.")
