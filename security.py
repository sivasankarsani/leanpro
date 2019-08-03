from werkzeug.security import safe_str_cmp
from user import User

users = [
		User(1,"sank","abc")
		User(2,"sankar","123")
]
print(users)

# users = [
# 	{
# 		"id":1
# 		"username":"sank"
# 		"password":"abc"
# 	},
# 	{
# 		"id":2
# 		"username":"sankar"
# 		"password":"123"
# 	}
# ]

# username_mapping = {
	# "sank": {
# 		"id":1
# 		"username":"sank"
# 		"password":"abc"
# 	},
	# "sankar":{
		# "id":2
# 		"username":"sankar"
# 		"password":"123"
# 	}
# }
# user_id_mapping= {
	# 1: {
# 		"id":1
# 		"username":"sank"
# 		"password":"abc"
# 	},
	# 2: {
		# "id":2
# 		"username":"sankar"
# 		"password":"123"
# 	}
# }

username_mapping = {u.username: ud for ud in users}

user_id_mapping = {u.id: ud for ud in users}

def autenauthenticate(username,password):
	user = username_mapping.get(username,None)
	if user and safe_str_cmp(user.password,password):
		return user

def identify(payload):
	user_id = payload['identify']
	return user_id_mapping.get(user_id,None)

