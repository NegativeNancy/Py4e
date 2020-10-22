def count(check_word, check_letter):
    counter = 0
    for letter in check_word:
        if letter == check_letter:
            counter = counter + 1
    return counter


word = 'banana'
input_letter = 'a'

print(count(word, input_letter))
print(word.count(input_letter))
