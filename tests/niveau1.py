from tests.framework import Case as C, Exercise, Level

EXERCISES = [
    Exercise("count_digits", "count_digits.py", ["count_digits"], stars=1,
             rules={"must_loop": True}, cases=[
        C("count_digits", ("R2-D2 et C-3PO",), 3),
        C("count_digits", ("2026",), 4),
        C("count_digits", ("",), 0),
        C("count_digits", ("abc",), 0),
        C("count_digits", ("a1b2c3d4e5f6g7h8i9j0",), 10),
        C("count_digits", ("::99::",), 2),
        C("count_digits", ("/:@`",), 0),   # voisins de '0'..'9' dans la table
    ]),
    Exercise("remove_char", "remove_char.py", ["remove_char"], stars=1,
             rules={"must_loop": True}, cases=[
        C("remove_char", ("b-a-n-a-n-a", "-"), "banana"),
        C("remove_char", ("hello", "l"), "heo"),
        C("remove_char", ("abc", "z"), "abc"),
        C("remove_char", ("", "a"), ""),
        C("remove_char", ("aaaa", "a"), ""),
        C("remove_char", ("Aa", "a"), "A"),
    ]),
    Exercise("swap_case", "swap_case.py", ["swap_case"], stars=1,
             rules={"must_loop": True}, cases=[
        C("swap_case", ("Hello World 42",), "hELLO wORLD 42"),
        C("swap_case", ("PyThOn",), "pYtHoN"),
        C("swap_case", ("123 !?",), "123 !?"),
        C("swap_case", ("",), ""),
        C("swap_case", ("azAZ",), "AZaz"),
        C("swap_case", ("[`{@",), "[`{@"),  # voisins des lettres dans la table
    ]),
    Exercise("find_index", "find_index.py", ["first_index", "last_index"],
             stars=1, rules={"must_loop": True}, cases=[
        C("first_index", ("banana", "n"), 2),
        C("first_index", ("banana", "b"), 0),
        C("first_index", ("banana", "z"), -1),
        C("first_index", ("", "a"), -1),
        C("first_index", ("abcabc", "c"), 2),
        C("last_index", ("banana", "a"), 5),
        C("last_index", ("banana", "b"), 0),
        C("last_index", ("banana", "n"), 4),
        C("last_index", ("", "a"), -1),
        C("last_index", ("abc", "z"), -1),
    ]),
    Exercise("is_number", "is_number.py", ["is_number"], stars=2,
             rules={"must_loop": True}, cases=[
        C("is_number", ("42",), True),
        C("is_number", ("-42",), True),
        C("is_number", ("007",), True),
        C("is_number", ("0",), True),
        C("is_number", ("4-2",), False),
        C("is_number", ("-",), False),
        C("is_number", ("",), False),
        C("is_number", ("+3",), False),
        C("is_number", ("--1",), False),
        C("is_number", ("12a",), False),
        C("is_number", ("a12",), False),
        C("is_number", (" 12",), False),
    ]),
    Exercise("count_words", "count_words.py", ["count_words"], stars=2,
             express=True, rules={"must_loop": True}, cases=[
        C("count_words", ("hello world",), 2),
        C("count_words", ("  hello   world  ",), 2),
        C("count_words", ("one",), 1),
        C("count_words", ("     ",), 0),
        C("count_words", ("",), 0),
        C("count_words", ("a b c d",), 4),
        C("count_words", (" a",), 1),
        C("count_words", ("a ",), 1),
    ]),
]

LEVEL = Level(1, "niveau1_strings", "Échauffement : strings et boucles", EXERCISES)
