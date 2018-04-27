family={'dad':'Marshal','mom':'sexy girl','son':'Kevin'}
Junfa={'dad':'jiujiu','mom':'jiuma','son':'Dajun'}
Kefa={'dad':['Engineer','Papa'],'mom':'Considerator','son':'Kevin'}
print(family['dad'])
print(family)
family['grandson']="Rex"
print(family)
family['grandson']="Jack"
print(family)
for position, name in family.items():
    print ("position:",position,"name:",name)

for names in set(family.values()):
    print(names)

for familymember in family:
    print(familymember)
Families=[family, Junfa, Kefa]
for family in Families:
    print (family)
