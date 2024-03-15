import re

# Sample text
text = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversations?"
"""

# Define a regular expression pattern
pattern = r'\b[Aa]\w+'  # Matches words starting with 'A' or 'a'

# Use re.findall to find all matches in the text
matches = re.findall(pattern, text)

# Print the matches
print("Words starting with 'A' or 'a':", matches)

# Use re.search to find the first occurrence of the pattern
match = re.search(pattern, text)

# Print the first match
if match:
    print("First word starting with 'A' or 'a':", match.group())
else:
    print("No match found.")
