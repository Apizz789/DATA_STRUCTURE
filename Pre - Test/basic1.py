lis = ["3", "4", "5", "6"]
# lis =["ss", "ss", "ss", "ss"]

print(f"list = {lis}")

# sol 1 for int solution
# n = [int(x) for x in lis]
# print(f"list = {n}")

# sol 2 for all solution
print("[{0}]".format(", ".join(map(str, lis))))


