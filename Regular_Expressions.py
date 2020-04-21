'''
What is a Regular Expression?
	- A regular expression or RegEx for short is a Pattern matching Language.
	- The Regular language was invented by American Mathematician Stephen Kleene.
	- Used for Searches, Find, Replace, validation.
	- Most programming languages support RegEx and others require additional libraries.
	- The Expression is a string of characters. 
	There is two types of characters: Metacharacters which have a special meaning, and Regular Characters which have literal meaning. 
	- Can be simple and easy to learn. However, takes a long time to master and use advanced expressions
	METACHARACTERS:
	'.'    -> Matches any single character (".at" would match cat, hat, sat,...)
	'[]'   -> Matches a single character contained with the brackets ("[ch]at" would match cat, hat but not sat)
	'[^ ]' -> Matches a single character NOT contained within the brackets ("[^c]at" would match hat, sat but not cat)
	'^'    -> Matches the expression if at the start of the string ("^.at" would match cat, hat, sat if located at the start of the string)
	'$'    -> Same as above however at the end (".at$" would match cat, hat, sat if located at the end of the string)
	'()'   -> Contained sub expression (Think BODMAS/BOMDAS)
	'*'    -> Matches the preceding element zero or more times ("c.*" would match any word starting with c, cat, coat, class,...)
	OPTION FLAGS:
	re.I   -> Ignore case matching.
	re.M   -> Make $ match the end of a line and ^ the start of a line.
	re.S   -> Make . match any character even the new line character.
	re.U   -> Interprets in Unicode.
	re.X   -> Ignores whitespace within the pattern.
How it works!
	- There is a few different algorithms that regular expressions can use. The most common being a DFA (Deterministic Finite Automaton)
	- The DFA algorithm is modified to use a pattern to specific it's computation rules.
	- The DFA algorithm takes O(2^m) to construct the Regular Expression (Where m is the lenght of the RegEx Pattern) then O(n) time to search a string of lenght n.
'''

import re 
def Main():
	line = " I think I understand regular expressions"
	matchResult = re.match("think", line, re.M|re.I)
	if(matchResult):
		print("Match Found: " + matchResult.group())
	else:
		print("No match was found!")
	searchResult = re.search('think', line, re.M|re.I)
	if(searchResult):
		print("Search found: " + searchResult.group())
	else:
		print("Nothing found in search!")

if(__name__ == '__main__'):
	Main()