singers=set(input('ENTER NAME OF SINGERS : ').split())
dancers=set(input('ENTER NAME OF DANCERS : ').split())
artist=singers | dancers
allrounders=singers & dancers
print(f"ARTISTS ARE : {artist}")
print(f"ALLROUNDERS ARE : {allrounders}")
print(f"DANCERS WHO ARE NOT SINGERS ARE : {dancers-singers}")
print(f"SINGERS WHO ARE NOT DANCERS ARE : {singers-dancers}")
print(f"SINGERS WHO ARE NOT DANCERS CUM DANCERS WHO ARE NOT SINGERS : {artist-allrounders}")


