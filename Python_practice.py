print("Hello World")
counties= ["Arapahoe", "Denver", "Jefferson"]
print(counties)
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
counties[2] = "El Paso"
print(counties)
counties.insert(1, "El Paso")
counties.remove("Arapahoe")
counties.insert(2, "Denver")
counties.insert(1, "Jefferson")
counties.append("Arapahoe")
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
counties_tuple[1]
counties_dict = {""}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
print(type(Dict))