fileToUse = input("What wordlist to use (words seperated by \\n)")

letter = input("Choose a letter to search")

mode = input("""

Search:

1. First letter

2. Whole word

""")

 

with open(fileToUse, "r") as wordlist:

  wordlist = wordlist.read()

 

  words = wordlist.split('\n')

  for i in range(len(words)):

    if words[i][:1] == letter:

      print(words[i])