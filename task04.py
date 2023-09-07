import re

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = 'fox'

position = re.search('fox', sample_text)

print(f"{position.group()} Start: {position.start()} End: {position.end()}")