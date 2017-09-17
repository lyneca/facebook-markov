# Facebook Messenger Markov Generator
Generates Markov chains and sentences off your Facebook messages.

## Usage
1. Download your Facebook data from [Facebook](https://facebook.com) - it's under settings.
2. Find `messages.htm` and put it in the same directory as these files.
3. `pip install markovify`
3. Edit `people.txt` and enter **full names** (i.e. John Smith, as they appear on Facebook) on seperate lines.
4. Run `conversation.py` and hope that it works! If not, make an issue!

It's _really_ slow to load (at least on my tiny computer). Optimisations are on the way!

# Credits
All the Markov stuff was done by the excellent [`markovify`](https://github.com/jsvine/markovify) library.
