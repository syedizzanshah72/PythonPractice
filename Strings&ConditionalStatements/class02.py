# String is a data type in which in " ",any data is witten
# Generally In String Double Quotes Are Use , But Single Quotes Or Triple Quotes Can Also Used
# Escape Sequences  
str1 = "My name Is\tIzzan"
print(str1)

# Concationation Of A String
a = "Izzan"
b = "Abbas"
c = a+ " " + b
print(c)
# len() Is Also A Built-In Function That is used to find length of string
print(len(c))
# Index 
name = "Izzan" # In which I is Index no.0 And n is Index 1 And So on lank Spaces Are Also Countable As Index
# I Can Access The Chracter By Calling Through Its Index Like
name1 = name[2]
print(name1)
# But As I know Strings Are Immutable/Unchangeable So , Hum Index Kay Character Ko New Value Assign Nae Karsaktay

# Slicing s An Important Topic
# We Can Pull Any Part Of String Like
a = "Izzan Shah Sb"
b = a[6:14]#last Character Count Nahi hota 1st index shamil hota par last nahi print ma
print(b)

# Negative Slicing Is Also Usefull I Those Cases In Which String BHot Baray Ho Aor End Say Slicing Karni Ho, Last Digit Ka Index -1 Hota ha 
pak = "In Shaa Allah! There Is An Election IN Pakistan On 8th February "
pak2 = pak[-13:-1]
print(pak2)
# Neagtive Ho Ya positive Characters aor words seedhay he rhay gaen ultay nahi hoga means pakistan negative slicin ma bhi pakistan hii print hoskta ha natsikap nahi 
# String Function 
# Dont Forget Strings Are Immutable
name = "my Name Is Muhammad Izzan Abbas Naqvi"
print(name.endswith("Naqvi"))
name = name.capitalize() # Strings Are Immutable But In This Case variable ko new value assign ki ha
name = name.reversed()
print(name)
# Isi Tarah Aor bhi String Functions Exist Kartay han jo different jga pa use karsaktay han wo apni zaroorat ka mutabiq search karnay ha
# Example ka lia replace function , find function or many many more

# Conditional Statements 
# syntax Are if-elif-else 
# Nested If
license = int(input("Enter Your Age "))
if(license >= 18):
    if(license > 80):
        print("You Cannot Drive")
    elif(license == 80):
        print("Drive But Not Recommended")
    else:
        print("Yeah! you Drive")
else:
    print("no")  
    
      