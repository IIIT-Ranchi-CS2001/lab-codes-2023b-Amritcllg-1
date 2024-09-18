singers=set(input('ENTER NAME OF SINGERS : ').split())
dancers=set(input('ENTER NAME OF DANCERS : ').split())
artist=singers | dancers
allrounders=singers & dancers
print(f"NUMBER OF ARTISTS ARE : {artist}")
print(f"NUMBER OF ALLROUNDERS ARE : {allrounders}")
print(f"NUMBER OF DANCERS WHO ARE NOT SINGERS ARE : {dancers-singers}")
print(f"NUMBER OF SINGERS WHO ARE NOT DANCERS ARE : {singers-dancers}")
print(f"NUMBER OF SINGERS WHO ARE NOT DANCERS CUM DANCERS WHO ARE NOT SINGERS : {artist-allrounders}")


