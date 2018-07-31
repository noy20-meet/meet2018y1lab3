name=input("what's your name?")

print("hello there, "+(name))

print(name)


print(len(name))
lenname=str(len(name))

print("your name is "+(lenname)+" letter long!")

print("The first letter of your name is "+name[0].capitalize()+" and the last letter is "+name[-1].capitalize())

namec="hi there, my name is claire.Nice to meet you!"
print(namec[20:27])

mood=input("how are you doing so far?")

print(mood.lower())
if mood== "Good":
    print("great! keep going!")
if mood== "bad":
     print("I'm sorry to hear that.How can I help?")
