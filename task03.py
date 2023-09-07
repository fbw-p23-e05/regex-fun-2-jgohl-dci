import re

sample_text = 'The quick brown fox jumps over the lazy dog.'

print(re.findall('fox|dog|horse', sample_text))