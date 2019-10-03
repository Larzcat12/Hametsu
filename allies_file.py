print("Hello!")

## Response variable holds response from human
response = input("How are you?: >>> ")
if(response.lower() == "good"):
    print("Great!")
else:
    print("Thats a bummer")

print("Check out my choose your own adventure game!")
response = input("Which direction do you want to go?: >>> ")
if(response == "up"):
    print("Going up...")
elif(response == "down"):
    print("Going down...")
elif(response == "left"):
    print("Going left...")
elif(response == "right"):
    print("Going right...")
else:
    print("Are you sure you really know where you are going?")

print("Continuing the story...")