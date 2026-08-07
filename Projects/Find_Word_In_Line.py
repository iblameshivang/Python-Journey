def find_line_of_word(word):
    line_no=0
    
    with open("Gori.txt") as f:
        for line in f:
            line_no+=1

            if word in line:
                print(f"Word is in line:{line_no}")
                break
        else:
            print("Word not Found!")

word=input("Enter your Word:")
find_line_of_word(word)
