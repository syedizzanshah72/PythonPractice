# Dictionaries And Sets
# Dictionaries (key:value)
# This Is Almost Said to be Another Built-in data Type like tuples or list
# ya aik key hoti ha aor dosri taraf us ka ya value or matlab ya meaning
# Is Kay Andar aap assigning value ma list aor tuple tak likh saktay han
# Dictionary may keys string , integer aor float  kuch bhi hoskti ha lakin list aor tuple(just special case) nahi , wo sirf is kay meaning/value ma hoskti 
# Dictionaries are mutable,unordered (means no index) aor 2 keys aik name ki nahi
# index nahi hota bas  key hee sa value ko access karsaktay
# empty dictionary variable = {}

info = {
    "name" : "M.Izzan Abbas Naqvi",
    "class" : "I.C.S",
    "subjects" : ["Physics","Computer","Mathematics","English"],
    "fail" : False,
    
    
    
}
print(type(info))
print(info["name"])
info["class"] = "2ndyear"
# for assigning of new value 
info["Father Name"] = "Syed Khizar Abbas"
print(info)

# Nested Dictionary
student = {
    "name" : "M.Izzan Abbas Naqvi",
    "marks" : {
        "phy" : 98,
        "math" : 99,
        "computer" : 75,
        "english" : 98
    },
    "class" : "I.C.S",
    "Goal" : {
        "physics" : 100,
        "chemistry" : 100,
    }
}
print(student["marks"] ["math"])

# Methods of dictionary

print(student.keys())# It Gives all key values
print(student.values())# it give all values
print(student.items())# it give all key,value pairs
# we can also use type casting , dictionary converted into list and we change or access elements by index
print(student.get("name"))# it give value according to key
# But the question arose that why we use .get() function in the presence of simple print
# Answer is that kay ethod wala means .get()ma agar kuch galat value hoi to none return karay ga aor simple wala error
student.update({"key" : "Vaue"} )# isma koi new dic purani ma add hojay gi ya koi new key value pair add hojay ga
print(student)
# update hojany kay baad bhi kisi dosri dictionary ma say same key value pair nahi askta pechla hii update hoga

# Sets 
# set is a collection of well-defined and didtinct objects
# It Is also an Built-In Data type like dictioary but it is unmutable or unchangeable but unordered (means no index)
# It Can Store All Other Data Types That Are Immutable like string, integer,float,tuple but don't store list and dictionaries
# set is unordered to print items or set ignores 2nd thing same 
# to create an empty set this syntax must b followed variable = set()
# set kay elements immutable han par sets are mutable 
# That's why there are methods like add,remove or many other
nameofsection = {2,("Izzan",)}
nameofsec = {["izzan","Hassan"]}
print(nameofsec)