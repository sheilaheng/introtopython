from database import User

users = User.select()
# Use forloop to display
for user in users:
    print(user.name, user.email, user.password)

