#function to check a charcter is vowel or not

def is_vow(c):

  vowels = "aeiouAEIOU"

  for vowel in vowels:

    if c==vowel:

      return True

  return False



# Take the inputs

fileName = input("Enter the file name: ")

inputFile = open(fileName, 'r')

text = inputFile.read()



# Count the sentences

sentences = text.count('.') + text.count('?')

text.count(':') + text.count(';')

text.count('!')



# Count the words

words = len(text.split())



# Count the syllables

syllables = 0

vowels = "aeiouAEIOU"



for word in text.split():





  for vowel in vowels:

    syllables += word.count(vowel)



  #decrease the count of consecutive vowels

  for i in range(1,len(word)):

    if(is_vow(word[i-1])==True and is_vow(word[i])==True):

      syllables-=1



  for ending in ['es', 'ed', 'e']:

    if word.endswith(ending):

      syllables -= 1

    if word.endswith('le'):

      syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
