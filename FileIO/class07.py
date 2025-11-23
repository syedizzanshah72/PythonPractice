# File I/O In Python
# Python can Be Used To Perform Operations On a file(read and Write data)
# Types Of All Files
# 1.Text Files : .txt,.docx etc
# 2. Binary Files : audio,video,mp4,jpg etc
# f = open("demo.txt","r")# Default Also Read

# data = f.read(5)
# print(data)
# f.close()
# f.readline() # Is used fr learning Line By Line
# # Agar Aik dafa Data Read Hogya Aor dosri Dafa phr read karwaya means pehlay read or  phr readline to readline pa empty spaces hee hongii
# f.write()# Is Another But aapko open my 'w' mode karna hoga
# # Write means overwrite from Scratch
# f.write()# Append At The last
# # To Craete New File That Isn't exist
# t = open('sample.txt','w')# Or append
# t.close()
# f = open("demo.txt","r+")# It Responsible For Two Actions Reading And Writing But data is  Overwrite In this case 
# f.write("I Want To Become A Python Developer")
# f.close()
# There Are Another Modes like
# i.r+ read + overwrite (not Truncate)pointer at start
# ii. w+ write + read (truncate)
# iii. Read + append(not Truncate)pointer at end
# With KeyWord
# with open("demo.txt","a+") as f:
#     f.append("Muhammad Izzan Abbas naqvi Is one The Best")
#     f.read()
#     f.close()
with open("demo.txt","r") as g:
    data = g.read()
    print(data)
# syntax for deleting a file 
# it uses A module
# Modeule (like a code Library) is a file written by another Programmer that has generally usefull functions