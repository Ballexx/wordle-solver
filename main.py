from wordlist import word_list

temp_list = []
banned_letters = []
_word_list = word_list


def green(letter, x):
    global _word_list, banned_letters

    banned_letters.append(letter)

    for i in range(len(_word_list)):
        if _word_list[i][x] == letter:
            temp_list.append(_word_list[i])

    _word_list = find_instance_amount(list(temp_list))
    suggestion_word()
    temp_list.clear()


def yellow(letter, x):
    global _word_list

    for i in range(len(_word_list)):
        if _word_list[i].find(letter) != -1 and _word_list[i][x] != letter:
            temp_list.append(_word_list[i])

    _word_list = find_instance_amount(list(temp_list))
    suggestion_word()
    temp_list.clear()


def white(letter):
    global _word_list, banned_letters

    banned_letters.append(letter)

    for i in range(len(_word_list)):
        if _word_list[i].find(letter) == -1:
            temp_list.append(_word_list[i])

    _word_list = find_instance_amount(list(temp_list))
    suggestion_word()
    temp_list.clear()


def find_instance_amount(temp_word_list):

    letters = ""

    two = False
    three = False

    one_instance = []
    two_instance = []
    three_instance = []

    for i in range(len(temp_word_list)):
        for j in range(5):
            letters += temp_word_list[i][j]

        for x in range(5):
            if letters.count(temp_word_list[i][x]) == 2:
                two = True
            elif letters.count(temp_word_list[i][x]) == 3:
                three = True

        if not two and not three:
            one_instance.append(temp_word_list[i])
        elif two and not three:
            two_instance.append(temp_word_list[i])
        elif three:
            three_instance.append(temp_word_list[i])

        two = False
        three = False
        letters = ""

    one_instance.extend(two_instance)
    one_instance.extend(three_instance)

    return one_instance


def suggestion_word():
    global banned_letters

    suggest_list = []

    bad_letters = ["z", "q", "w", "x", "y", "j", "k", "v", "b", "g", "p"]

    for i in range(len(word_list)):
        for j in range(len(banned_letters)):
            if word_list[i].find(banned_letters[j]) == -1:
                for x in range(len(bad_letters)):
                    if word_list[i].find(bad_letters[x]) == -1:
                        suggest_list.append(word_list[i])
                    else:
                        suggest_list.insert(0, word_list[i])

    suggest_list = find_instance_amount(suggest_list)

    print("Suggested words to guess: ", suggest_list)


def main():
    x = 0
    while True:
        if x == 5:
            x = 0

        letter = input(f"Enter letter {x+1}\n")
        color = input("Enter color (g, y, w) of letter\n")

        if color == "g":
            green(letter, x)
        elif color == "y":
            yellow(letter, x)
        elif color == "w":
            white(letter)
        else:
            print("Illegal letter, quitting...")
            exit()

        print("Possible words: ", _word_list)

        x += 1


main()
