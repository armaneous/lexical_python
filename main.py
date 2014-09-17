"""
||| AUTHOR:		Andrew Armaneous
||| PROJECT:	Lexical Analyzer
||| FILE:		main.py
|||
||| SUMMARY:
||| A simple lexical analyzer that uses an external,
||| simple-format, file for definitions and the respective
||| tokens. Input file can then be specified for checking
||| language against language definition. Output can be
||| presented via print() method or write(filename) method.
"""

from lex import Lexer
yesAnswers = ["y", "yes", "YES", "Yes"]

# Run loop by default
while True:
	# Let user choose file for rule definitions
	ruleDef = input("Enter rules file for definitions: ")
	lex = Lexer(ruleDef)
	lex.setRules()

	# Let user choose input file to be analyzed
	inputFile = input("Choose code file to read: ")
	lex.analyze(inputFile)
	
	# User response to prompt for output type
	answer = input("Enter 'print' to output to console, otherwise enter output file name: ")
	if answer == "print":
		lex.print()
	else:
		lex.writeToFile(answer)

	# Break loop if user does not wish to read another file
	answer = input("Analyze another file? ")
	if answer not in yesAnswers:
		break