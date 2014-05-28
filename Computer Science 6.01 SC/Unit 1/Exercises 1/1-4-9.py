def extract_tags(s):
	"""
	Args
		s: A string containing tags surrounded by brackets.

	Returns
		A list of the tags.
	"""
	tags = []
	capture = False
	start = None
	for index in range(len(s)):
		if s[index] == "]" and capture:
			tags.append(s[start:index])
			capture = False
		elif s[index] == "[":
			start = index + 1
			capture = True
	return tags
