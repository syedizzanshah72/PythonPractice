# Lists 
# List Is Built-in data Type That is Used To Store Data Of Different Kinds (string,integer) But basic is 5 data types which is written peviously
# strings Are Immutable And Lists Are Mutable
studentdata = ["M Izzan Abbas",98,"class11th","ICS"]
studentdata[3] = "FSC"
print(studentdata)# Lists Are Mutable 
stre = "izzab"
print(stre.capitalize())
print(stre)
# In List Slicing Are Also Possible 
nameofcon = ["Pakistan","Iran","KSA","Usa","UK","Ind."]
print(nameofcon[1:4])
print(nameofcon[-3:-1])# tarteeb Seedhai He rhay gee -slicing may 

# List methods 
nums = [1,2,4,3]
print(nums.append(5))# append Function Last Pa append / add karta ha
# ya jo upar line likhi ha ya asal list ma shamil to hogae prr,print(nums.append )function kuch return nahi karta
nums.sort()
print(nums)
#return kuch nahi karta,means list mutable ya jakar asal value change karta ha while in string methods strings are immutable to tring methods kuch return kartay tha new value. list may bhi ma be kuch methods kuch return kartay hon.
# .sort()ascending sa descending ma value karta aor .sort(reverse=True)Descending tto Ascending To Descending Return Karta
# Strings ma bhi sort() kaam karta ha aplhabet pa , means a,b,c,d jo pehlay aay ga wo print hojay ga,lakin Capital prefer hoga
criclov = ["Pak","Ind","ban","Ksa"]
criclov.sort(reverse=True)
print(criclov)
criclov.reverse()# ya bilkul reverse kardey gi list ko
criclov.insert(2,"Eng")# ya jo index aapnay diya ha first pa us jga pa jo value apnay second porton pa di ha add hojay gee
print(criclov)
criclov.remove("Eng")#ya hmari list may sa First 2 k remove kry ga , first ko sirf
print(criclov)
print(criclov.pop())#it requires index that to be deleted
print(criclov)
# There are many Others methods of 
# Tuple Is Another Data Type Which Is Immutable
tup = (1)#agar sirf aik value ho to comma lgana zaroori , phir hee tuple bnay ga
print(tup)
print(type(tup))
# Tuple Slicing Also occours
admission = ("Ali","Haider","Nazeer","Musa")
print(admission[1:4]) 
# Tuple Methods Also Have
#.count()# count occurence of element in tuple
# .index()
# And Many Many More
# Practice Question No.01
userInput01 = input("Tell Me The Name OF your Favourite Movie : ")
userInput02 = input("Tell Me The Name Of The Movie You Liked At The Second Number : ")
userInput03 = input("Tell Me The Name Of The Movie You Liked At The Third Number : ")
userFavMovies = [userInput01,userInput02,userInput03]
print(type(userFavMovies))