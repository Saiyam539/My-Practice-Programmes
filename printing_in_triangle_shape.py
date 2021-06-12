word = input("Enter the word\n")

for row in range(len(word)):
    for col in range(row+1):
        print(word[col],end=' ')
    print()
