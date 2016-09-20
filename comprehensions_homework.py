# comments to make flake go away

origin_sentence = "List Comprehensions are the Greatest!"
vowels = ['a', 'e', 'i', 'o', 'u']
result = ""
for letter in origin_sentence:
    if letter not in vowels:
        result += letter
    # don't append the letter, if it's a vowel!!!!

print(result)
'''this is an intentional gap made just for the fun of banging on my keyboard'''
# phase two

with open('dataset.txt') as contents:
    contents = contents.readlines()
row_of_temp = [col[18-21]for col in contents]

print(row_of_temp)


'''water_temps = 26.5, 26.2, 26.2, 26.2, 26.5,
                 26.9, 27.1, 27.0, 26.9, 27.1,
                 27.0, 26.9, 26.8, 26.9, 27.1,
                 27.1, 27.5, 27.7, 27.6, 28.1,
                 27.5, 27.7, 27.4, 27.4, 28.0,
                 28.7, 28.9, 28.5'''
'''print(water_temps)'''
