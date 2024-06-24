# prompt the user for words
adjective1 = input("enter an adjective: ")
adjective2 = input("enter another adjective: ")
adjective3 = input("enter another adjective: ")
adjective4 = input("enter another adjective: ")

# story template
story = f"On a beautiful {adjective1} day, I went to the zoo. I saw a funny {adjective2} monkey swinging from the trees. Then, I spotted a majestic {adjective3} lion lounging in the sun.  What a wild and {adjective3} experience!"

# ascertain if the user used the same adjective twice
if adjective1 == adjective2:
    story += "the teargas was worth it"
else:
    story += "reject finance bill"

# display story
print(story)