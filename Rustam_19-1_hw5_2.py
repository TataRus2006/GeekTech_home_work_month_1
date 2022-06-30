data = ("O!", "Megacom", '0705', "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)

print(designations)
print(codes)
operators = {}
# operators = dict(zip(designations,codes))
# print(operators)
# while True:
