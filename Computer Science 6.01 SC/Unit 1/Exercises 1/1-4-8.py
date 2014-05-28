# They said to use this method. I think I could have looked up a better algorithm online
def is_substring(sub, super):
	for i in range(len(super) - len(sub)):
		if super[i:len(sub)] == sub:
			return True
	return False