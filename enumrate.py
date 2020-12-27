word = "hello"
w_lst = list(word)
guess = "l"
print( list(enumerate(w_lst)))

ind = [ i for i, letter in enumerate(w_lst) if guess == letter]
print(ind)
