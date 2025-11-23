# Practice Question No.01
userFavMovies = []
userInput01 = input("Tell Me The Name OF your Favourite Movie: ")
userInput02 = input("Tell Me The Name Of The Movie You Liked At The Second Number: ")
userInput03 = input("Tell Me The Name Of The Movie You Liked At The Third Number: ")
userFavMovies.append(userInput01)
userFavMovies.append(userInput02)
userFavMovies.append(userInput03)
print(type(userFavMovies))

# Practice Question N0.02
palindrolic = ["racecar"]
palindrolic20 = palindrolic.copy()
palindrolic40 = palindrolic20.reverse()
if(palindrolic == palindrolic40):
    print("Yes It Is palindrolic")
else:
    print("It IS not palindrlic")
    
# Practice Question No.03
gradesofstudents = ("A","B","D","A")
count = gradesofstudents.count("A")
print(count)

# Practice Question No.04
grades = ["C","D","A","A","B","B","A"]
grades.sort()
print(grades)

