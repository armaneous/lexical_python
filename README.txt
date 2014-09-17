/=====================================\
|	Lexical			      |
|	    Analyzer		      |
|		in Python	      |
\=====================================/
AUTHOR:		Andrew Armaneous
PROJECT:	Lexical Analyzer
FILE:		lex.py

SUMMARY:
A simple lexical analyzer that uses an external, simple-format, file for definitions and the respective tokens. Input file can then be specified for checking language against language definition. Output can be presented via print() method or write(filename) method.

----------------------------
HOW TO USE:

----------------------------
1. Create local file with definitions list for language
	- sampleDef.txt is included for reference
	- Regular expression syntax must follow python rules:
		- https://docs.python.org/3.4/howto/regex.html
	- Regular expression token must be preceded by an ampersand '&' (i.e. &sampleToken...)
	- Definitions must inlude at least one space between separators and grammar generators (' | ' and ' :: ')

2. Place input file(s) for analyzing in local folder
	- sampleInput.txt is included for reference

3. Run main.py:
	- "python main.py"

4. Any generated output files will be in the same folder


----------------------------
KNOWN BUGS:
----------------------------
Analyzer needs to be adjusted for concatenated tokens (i.e. 5*4 vs 5 * 4), currently throws out UNKNOWN tokens.