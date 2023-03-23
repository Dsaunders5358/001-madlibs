bowling_word_list = ["Adjective 1", "Adjective 2", "Funny Noise 1", "Funny Noise 2", "Noun 1", "Noun 2", "Noun 3", "Noun 4"
               , "Number", "Part of the body", "Place", "Plural Noun 1", "Plural Noun 2"]


bowling_story = """Almost every community in America now has a bowling %s
because bowling has become very %s with young
%s. Most of them become very %s
at the game. The main object of the game is to roll a heavy bowling
%s down the alley and knock down the %s pins
which are at the other end. If you knock them down in one roll, it's
called a %s. If it takes two rolls, it's called
a %s. Many alleys have automatic %s
setters. Others hire %s who set the pins by %s.
The most important thing to remember when bowling is to make
sure you have a good grip on the %s or you're liable to
drop it on your %s!"""


bowling_list_order = [11, 1, 12, 2, 5, 9, 3, 4, 6, 13, 7, 8, 10]
def rearranging_madlib_word_list(madlib_order_list : list, madlib_word_list : list) -> list:
    outputted_list = []
    for order in madlib_order_list:
        outputted_list.append(madlib_word_list[order - 1])
    return outputted_list
        


def madlib_input_generator(selected_list : list) -> list:
    print("Please enter words based on their descriptions given")
    outputted_list = []
    for word in selected_list:
        new_madlib = input(word + ":" )
        outputted_list.append(new_madlib)
    new_output_list = rearranging_madlib_word_list(bowling_list_order, outputted_list)
    return new_output_list
