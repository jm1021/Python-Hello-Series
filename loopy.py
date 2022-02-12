"""
 * Creator: Nighthawk Coding Society
 * Mini Lab Name: Hello Series, featuring Monkey Jumpers
 * Level: Medium
 *
 * Exploration Ideas
 * 1. Build more or entire rhyme for the "Monkey Jumpers" countdown poem (or create your own poem/countdown)
 * 2. Add names or other properties to the monkeys
 * 3. Print these monkeys horizontally
 *
 * Learning Considerations
 * Note: Loopy (Imperative Programming Style)
 * Project Focus: Animated Monkey Jumpers
 * A. Observe variable assignments
 * B. Study loops and zero based counting
 * C. Study two-dimensional (2D) arrays
 * D. Learn about and describe Imperative and Procedural Programming
 * E. Build a class diagram on a monkey as an object versus two-dimensional array
"""


def main():
    print("Hello Series: loopy.py")  # identification message
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"

    """ 2D array data assignment """
    monkeys = [
        [
            Red,
            "ʕง ͠° ͟ل͜ ͡°)ʔ ",  # [0][0] eyes
            "  \\_⏄_/  ",  # [0][1] chin
            "  --0--   ",  # [0][2] body
            "  ⎛   ⎞   "  # [0][3] legs
        ],
        [
            Green,
            " ʕ༼ ◕_◕ ༽ʔ ",  # [1][0]
            "  \\_⎏_/  ",
            "  ++1++  ",
            "   ⌋ ⌊   "
        ],
        [
            Yellow,
            " ʕ(▀ ⍡ ▀)ʔ",  # [2][0]
            "  \\_⎐_/ ",
            "  <-2->  ",
            "  〈  〉 "
        ],
        [
            Blue,
            "ʕ ͡° ͜ʖ ° ͡ʔ",  # [3][0]
            "  \\_⍾_/  ",
            "  ==3==  ",
            "  _/ \\_  "
        ],
        [
            Magenta,
            "  (◕‿◕✿) ",  # [4][0]
            "  \\_⍾_/ ",  # [4][1]
            "  ==4==  ",  # [4][2]
            "  _/ \\_ "  # [4][3]
        ]
    ]

    """ 2D array program logic """
    # cycles through 2D array backwards
    for i in range(len(monkeys), -1, -1):
        # this print statement shows current count of Monkeys
        # concatenation (+) of the loop variable and string to form a countdown message
        print(str(i) + " little monkeys jumping on the bed...")

        # cycle through monkeys that are left in poem countdown
        for row in range(i - 1, -1, -1):  # cycles through remaining monkeys in countdown

            # cycles through monkey part by part
            for col in range(len(monkeys[row])):
                # prints specific part of the monkey from the 2D cell
                print(monkeys[row][col] + " ")

            # this new line gives separation between stanza of poem
            print("\u001b[0m")  # reset color

    # out of all the loops, prints finishing messages
    print("No more monkeys jumping on the bed")
    print("0000000000000000000000000000000000")
    print("             THE END              ")


if __name__ == "__main__":
    main()
