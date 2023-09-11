#this is a function that reduces one from every number 

def remove_one (num):
    oper = int(num) - 1
    return oper

num_Reduc = input("Give me number you wish to reduce by one - ")

answer = remove_one(num_Reduc)

print(f"when {num_Reduc} is reduced by one it gives {answer}")