word = 'Hello'
for l in range(len(word)):
    print(word[l])
    
    
team = ["TJ","Ewura","Gordon","Simon","Alex"]
for name in team:
    print(f" {name} contributed to this exercise.")
    

stga_dict = {
    "TJ" : "INST 327",
    "Ewura": "INST 311",
    "Gordon": "INST 326",
    "Simon": "INST 408i",
    "TJ": "INST 412"
    
}
[print(f"{names} is taking {stga_dict[names]}") for names in stga_dict]