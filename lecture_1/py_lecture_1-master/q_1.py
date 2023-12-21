# ამოცანა 1.
country_codes = ['US', 'UK', 'GE', 'CA']

del country_codes[0]
country_codes.append('IR')
country_codes.sort()

# ამოცანა 2.
country_codes_2 = country_codes[2:]

# ამოცანა 3.

for c in country_codes:
    print(c)

# ამოცანა 4.
copy_of_country_codes = country_codes[:]
