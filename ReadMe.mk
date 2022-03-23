###INSTRUCTIONS:
* Your task is to use the contents of all provided files to create a dictionary of acceptable 5-letter words that we will later use in your wordle_v1 game.

* Once you have built your dictionary, print out the list in alphabetic order, and the count of how many words are in the dictionary. Since there will be a lot of words, when printing, please print 5 words per line, separated by a comma or space.

* For now we will write this as a stand-alone program, but later we will integrate our code with the actual game of Wordle and make Wordle_V2

* There are 4 text files available. Each is numbered ( 1, 2, 3, 4 ). Since accessing them is a little beyond where we are so far, I have provided a function to do the task of reading the file and returning the text contained in that file.


###NOTES:
* Do not edit code in the files.py file provided!
* ALL code should be in the provided function
    create_dictionary()
* The text in the 4 files comes from different sources:
            1) An SAT Reading Passage
            2) Brown Girl Dreaming - By Jacqueline Woods
            3) Pawn of Prophecy - By David Eddings
            4) I am Malala - By Malala Yousafzai

###HINTS:
* Don't forget to think about punctuation!
* It is ok to assume that the grammar in the books is correct.
* It is highly recommended that you review the words in your final dictionary to ensure that you didn't make any obvious errors.
* It is expected that this is a challenging problem, so don't try to solve everything in one step, break it into major pieces and solve one at a time.

###READING FILES:
As noted, I have provided you with a function that will read the text contained in a file (# 1, 2, 3 or 4) and return it as a single text element. To read the text from file # 3 into a variable named passage_3 we would simply do the following:

    passage_3 = f.read_file(3)