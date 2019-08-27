print("Type the secret word: ")
secret_word = input()
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

    if guess == secret_word[:1]:
        if guess == secret_word:
            break
        print("Close")
    elif guess == secret_word[:2]:
        if guess == secret_word:
            break
        print("Closer")
    elif guess == secret_word[:3]:
        if guess == secret_word:
            break
        print("Very Close")
    elif guess == secret_word[:4]:
        if guess == secret_word:
            break
        print("Super Close")    # and so on...

if out_of_guesses:
    print("You lose")
else:
    print("You win!")
print(guess_count)