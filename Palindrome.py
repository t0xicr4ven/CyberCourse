
print("""
 _______  _______  _       _________ _        ______   _______  _______  _______  _______
(  ____ )(  ___  )( \      \__   __/( (    /|(  __  \ (  ____ )(  ___  )(       )(  ____ \\
| (    )|| (   ) || (         ) (   |  \  ( || (  \  )| (    )|| (   ) || () () || (    \/
| (____)|| (___) || |         | |   |   \ | || |   ) || (____)|| |   | || || || || (__    
|  _____)|  ___  || |         | |   | (\ \) || |   | ||     __)| |   | || |(_)| ||  __)   
| (      | (   ) || |         | |   | | \   || |   ) || (\ (   | |   | || |   | || (      
| )      | )   ( || (____/\___) (___| )  \  || (__/  )| ) \ \__| (___) || )   ( || (____/\\
|/       |/     \|(_______/\_______/|/    )_)(______/ |/   \__/(_______)|/     \|(_______/

**** Enter a word and this script will test to see if it a palindrome.

 """)
#get input
word_to_test = input("please enter a word to test: ")
forward_list = []
backward_list = []
count = 0
word_len = len(word_to_test)

#iterate over user input and put into two lists
for letter in word_to_test:
    forward_list.append(letter)
    backward_list.append(letter)

# reverse second list
backward_list.reverse()

#iterate over word lists
for x in range(len(forward_list)):
    #check if letters match
    if forward_list[x] == backward_list[x]:
        count += 1
        #if count == the len of the word, then we have a palindrome
        if count == word_len:
            print("You have a Palindrome!!!")
            break
        #if one match fails then no palindrome and break loop
    else:
        print("Sorry this is not a Palindrome!")
        break

