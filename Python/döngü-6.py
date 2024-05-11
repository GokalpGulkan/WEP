# short if kullanimi
is_active = False
# is_active = False

user_info = "active" if is_active else "deactive"
print(user_info)


user_index = []

user_index_v1 = [item for item in range(1, 10)]

print(user_index_v1)

user_index_v2 = [item * 10 for item in range(1, 10)]

print (user_index_v2)

user_index_v3 = [item for item in range(1, 10) if item % 2 != 0]

print(user_index_v3)