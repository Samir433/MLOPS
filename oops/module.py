from Chtabook import Chatbook

user1 = Chatbook()

print(user1.id)

Chatbook.set_id(5)

user2 = Chatbook()
print(user2.id)

user3 = Chatbook()
print(user3.id)