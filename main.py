# define the function 
def fuzzbuzz(alist):
#     start looping through the list
    for i in alist:
        # check for the numbers
        if i % 5 == 0 and i % 3 != 0:
            print(i, 'fuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print(i, 'buzz')
        elif i % 5 == 0 and i % 3 == 0:
            print(i, 'fuzzbuzz')
        else:
            print(i, 'neither')
# populate the list
my_list = []
for j in range(1, 101):
    my_list.append(j)

fuzzbuzz(my_list)


