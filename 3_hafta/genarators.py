###♦ Generators ###

# bellekte yer isgal etmeyen iterater olusturur.
def cube():
    for i in range(5):
         yield i ** 3       # bellekte yer kaplamadan uretmek




for i in cube():
    print(i)
