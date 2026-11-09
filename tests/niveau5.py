from tests.framework import Case as C, Exercise, Level

LOOP = {"must_loop": True}

CONSOLE_HEAD = "== CIPHER CONSOLE ==\n1) encode  2) decode  3) quit\n"

EXERCISES = [
    Exercise("echo_upper", "echo_upper.py", ["echo_upper"], stars=2,
             express=True, rules=LOOP, cases=[
        C("echo_upper", (), 2, inputs=["hello", "Python 3", "STOP"],
          out="> hello\nHELLO\n> Python 3\nPYTHON 3\n> STOP\n2 line(s) echoed.\n"),
        C("echo_upper", (), 0, inputs=["STOP"], out="> STOP\n0 line(s) echoed.\n"),
        C("echo_upper", (), 1, inputs=["stop", "STOP"],
          out="> stop\nSTOP\n> STOP\n1 line(s) echoed.\n"),
        C("echo_upper", (), 2, inputs=["", "a-z!", "STOP"],
          out="> \n\n> a-z!\nA-Z!\n> STOP\n2 line(s) echoed.\n"),
    ]),
    Exercise("sum_until_zero", "sum_until_zero.py", ["sum_until_zero"],
             stars=2, rules=LOOP, cases=[
        C("sum_until_zero", (), 13, inputs=["5", "-2", "10", "0"],
          out="number: 5\nnumber: -2\nnumber: 10\nnumber: 0\n"
              "total: 13 (3 numbers)\n"),
        C("sum_until_zero", (), 0, inputs=["0"],
          out="number: 0\ntotal: 0 (0 numbers)\n"),
        C("sum_until_zero", (), 0, inputs=["4", "-4", "0"],
          out="number: 4\nnumber: -4\nnumber: 0\ntotal: 0 (2 numbers)\n"),
    ]),
    Exercise("guess", "guess.py", ["guess"], stars=2, rules=LOOP, cases=[
        C("guess", (37,), 3, inputs=["50", "25", "37"],
          out="guess: 50\ntoo high\nguess: 25\ntoo low\nguess: 37\n"
              "found in 3 tries!\n"),
        C("guess", (7,), 1, inputs=["7"], out="guess: 7\nfound in 1 try!\n"),
        C("guess", (-5,), 2, inputs=["0", "-5"],
          out="guess: 0\ntoo high\nguess: -5\nfound in 2 tries!\n"),
    ]),
    Exercise("min_max", "min_max.py", ["min_max"], stars=3, rules=LOOP, cases=[
        C("min_max", (), None, inputs=["4", "7", "-3", "12", "0"],
          out="how many? 4\n> 7\n> -3\n> 12\n> 0\nmin: -3\nmax: 12\n"),
        C("min_max", (), None, inputs=["3", "5", "8", "9"],
          out="how many? 3\n> 5\n> 8\n> 9\nmin: 5\nmax: 9\n"),
        C("min_max", (), None, inputs=["2", "-8", "-2"],
          out="how many? 2\n> -8\n> -2\nmin: -8\nmax: -2\n"),
        C("min_max", (), None, inputs=["1", "42"],
          out="how many? 1\n> 42\nmin: 42\nmax: 42\n"),
        C("min_max", (), None, inputs=["0"], out="how many? 0\nnothing to do\n"),
        C("min_max", (), None, inputs=["-3"], out="how many? -3\nnothing to do\n"),
    ]),
    Exercise("cipher_console", "cipher_console.py", ["cipher_console"],
             stars=4, express=True, rules=LOOP, cases=[
        C("cipher_console", (), 2,
          inputs=["1", "Hello, World!", "3", "2", "Khoor", "3", "7", "3"],
          out=CONSOLE_HEAD + "choice: 1\ntext: Hello, World!\nshift: 3\n"
              "Khoor, Zruog!\nchoice: 2\ntext: Khoor\nshift: 3\nHello\n"
              "choice: 7\nunknown choice\nchoice: 3\nbye (2 operations)\n"),
        C("cipher_console", (), 0, inputs=["3"],
          out=CONSOLE_HEAD + "choice: 3\nbye (0 operations)\n"),
        C("cipher_console", (), 2, inputs=["1", "xyz", "29", "2", "abc", "-1", "3"],
          out=CONSOLE_HEAD + "choice: 1\ntext: xyz\nshift: 29\nabc\n"
              "choice: 2\ntext: abc\nshift: -1\nbcd\nchoice: 3\n"
              "bye (2 operations)\n"),
        C("cipher_console", (), 1, inputs=["quit", "", "1", "Zz 9", "1", "3"],
          out=CONSOLE_HEAD + "choice: quit\nunknown choice\nchoice: \n"
              "unknown choice\nchoice: 1\ntext: Zz 9\nshift: 1\nAa 9\n"
              "choice: 3\nbye (1 operations)\n"),
    ]),
]

LEVEL = Level(5, "niveau5_interactif", "Programmes interactifs (while + input)",
              EXERCISES)
