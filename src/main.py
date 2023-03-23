from src.data import madlibs_list

madlibs_list_titles = ["Bowling", "Emmy Acceptance Speech", "Medical Drama", "Rock Music", "Tarzan", "Video Games"]
word_list = ["Grizzly", "Damp", "Gasp", "SPERKLUNK", "Tabletop", "Fridge", "Desk", "Elevator", "468", "Nipple", "Coventry", "Doors", "Graves"]
madlib_story = """Almost every community in America now has a bowling %s

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
bowling_list = madlibs_list.bowling_word_list
# def setting_madlibs_variables(madlib : int) -> list:
print(madlibs_list.madlib_input_generator(bowling_list))
    