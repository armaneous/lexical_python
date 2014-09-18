"""
||| AUTHOR:		Andrew Armaneous
||| PROJECT:	Lexical Analyzer
||| FILE:		lex.py
|||
||| SUMMARY:
||| A simple lexical analyzer that uses an external,
||| simple-format, file for definitions and the respective
||| tokens. Input file can then be specified for checking
||| language against language definition. Output can be
||| presented via print() method or write(filename) method.
"""

# Importing module for regular expressions
import re

class Lexer(object):
	
	"""
	Class constructor sets definitions file to be read.
	"""
	def __init__(self, definitions):
		# Specify definitions file
		self.file = open(definitions)
		# Used for storing rules in language
		self.ruleDictionary = {}
		# Used for output tokens from input
		self.tokens = []
		# Used for reg expression rules
		self.regexRules = []
		
	"""
	Run analysis on all lines in definition file.
	Uses definition file to generate dictionary of 
	rules to check code against for validation.
	"""
	def setRules(self):
		# For every line in the file, add to dictionary
		for line in self.file:
			# Strip trailing newline characters
			line = line.rstrip('\n')
			# Split using regular expression at '::'
			tokenDef = re.split("\s+::\s+", line)
			tokenItem = tokenDef[0]
			# Split using regular expression at '|'
			tokenRules = re.split("\s+\|\s+", tokenDef[1])
			
			# Generate dictionary of rules for language
			for rule in tokenRules:
				# Check for regular expression rules
				if re.match("&", tokenItem):
					tokenItem = tokenItem.lstrip('&')
					self.regexRules.append(rule)
				# Create dictionary entry for token and production
				self.ruleDictionary[rule] = tokenItem
	
	"""
	Set input file of code and run analysis of code to
	generate tokens with respect to language definition.
	"""
	def analyze(self, input):
		# Specify input file to analyze
		self.file = open(input)
		
		# For every line in the file, run analysis
		for line in self.file:
			items = line.split()
			tokenLine = []
			
			# For every item within input line, analyze
			for item in items:
				# If item is a set rule, add to tokenLine
				if item in self.ruleDictionary.keys():
					tokenLine.append(self.ruleDictionary[item])
				# Check if item follows a reg expression, else UNKNOWN
				else:
					for rule in self.ruleDictionary.keys():
						# If item matches rule reg expression, add appropriate token
						# KNOWN token added to verify proper addition of token
						print (rule, ", ", item)
						if re.match(rule, item):
							tokenLine.append(self.ruleDictionary[rule])
							tokenLine.append("KNOWN")
							break
					# Use KNOWN tokens to identify whether a reg expression has been
					# matched or not. Add UNKNOWN if none has been matched.
					if tokenLine[len(tokenLine)-1] == "KNOWN":
						tokenLine.pop()
					else:
						tokenLine.append("UNKNOWN")
			
			# Add tokenLine to tokens list
			self.tokens.append(tokenLine)
	
	"""
	Print out tokens to screen.
	"""
	def print(self):
		# For every line of tokens print with spaces
		for tokenLine in self.tokens:
			print (" ".join(tokenLine))
			
	"""
	Write tokens to output file specified.
	"""
	def writeToFile(self, output):
		self.file = open(output, "a")
		# For every line of tokens, write tokens with spaces
		for tokenLine in self.tokens:
			self.file.write("%s\n" % " ".join(tokenLine))
		self.file.close

