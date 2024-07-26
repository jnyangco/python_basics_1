#! python3
# mclip.py - A multiple clipboard program.
import sys, pyperclip

text_dict = {'agree': """Yes, I agree. That sounds fine to me.""",
             'busy': """Sorry, can we do this later this week or next week?""",
             'upsell': """Would you consider making this a monthly donation?"""}

# Capture arguments from terminal -> using sys.argv
# Note: The first argument will always be the filename.py
# sys.argv = ['mclip.py', 'agree', 'busy']...
# run -> python mclip.py agree
# run -> python mclip.py agree busy
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

# Note that you don’t actually need the keyphrase variable; you could just use sys.argv[1] everywhere keyphrase is
# used in this program. But a variable named keyphrase is much more readable than something cryptic like sys.argv[1].
keyphrase = sys.argv[1]  # first command line arg is the keyphrase

# Handle if there is no argument passed
if keyphrase in text_dict:
    pyperclip.copy(text_dict[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)



