def hello():
    print("Hello!")
hello()

def pack(a,b,c):
    return [a,b,c]

print(pack("a", "b", "c"))

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("I don't have any lunch")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")

eat_lunch([])
eat_lunch(["Ramen"])
eat_lunch(["Ramen", "Crackers and Guac", "Pizza", "Salad"])

