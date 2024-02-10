'''Write a program that counts the number of vowels in a sentence.'''

def count_vowels(sentence):
    vowels = set("aeiouAEIOU")
    return sum(sentence.count(vowel) for vowel in vowels)
user_input= input("Enter a sentence: ")
result= count_vowels(user_input)
print("Number of vowels: ", result)