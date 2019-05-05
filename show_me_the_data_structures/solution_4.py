class Group(object):
	def __init__(self, _name):
		self.name = _name
		self.groups = []
		self.users = []

	def add_group(self, group):
		self.groups.append(group)

	def add_user(self, user):
		self.users.append(user)

	def get_groups(self):
		return self.groups

	def get_users(self):
		return self.users

	def get_name(self):
		return self.name


parent = Group('parent')
child = Group('child')
sub_child = Group('subchild')

user1 = 'user1'
user2 = 'user2'
user3 = 'user3'
user4 = 'user4'
user5 = 'user5'
parent.add_user(user1)
child.add_user(user2)
sub_child.add_user(user3)
sub_child.add_user(user4)
sub_child.add_user(user5)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
	'''
	Return True if user is in the group, False otherwise.

	Args:
	user(str): user name/id
	group(class:Group): group to check user membership against
	'''
	if user in group.get_users():
		return True

	for grp in group.get_groups():
		if is_user_in_group(user, grp):
			return True

	return False

# Test Case: 1
print('User exists in this group.'
if is_user_in_group(user1, parent)
else 'User does not exist in this group.')

# Test Case: 2
print('User exists in this group.'
if is_user_in_group(user2, parent)
else 'User does not exist in this group.')

# Test Case: 3
print('User exists in this group.'
if is_user_in_group(user1, sub_child)
else 'User does not exist in this group.')