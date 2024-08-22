# Step 1 - import af nødvendige moduler
import string
import random

# Step 2 - få tekststrenge af både alle bogstaver og tal
letters = string.ascii_letters
numbers = string.digits

# Step 3 - lav en samlet liste ud af alle bogstaver og tal
pwd_options = list(letters + numbers)

# Step 4 - Få 10 tilfældige karakterer fra listen
pwd_chars = random.choices(pwd_options, k=10)

# Step 5 - lav listen om til én lang tekststreng
pwd_string = "".join(pwd_chars)

# Step 6 - print dit password
print(pwd_string)
