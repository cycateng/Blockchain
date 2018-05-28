from hashlib import sha256
x = 5
y = 0 # We don't know what y should be yet...
h = sha256(f'{x*y}'.encode()).hexdigest()
print('calc y(nonce)...', end='\n\n')
while h[-1] != "0":
    print(f'y = {y}:\thash = {h}')
    y += 1
    h = sha256(f'{x*y}'.encode()).hexdigest()

print(f'y = {y}:\thash = {h}')
print(f'The solution is y = {y}')

#y = 0
#while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
#    y += 1
#    print(f'The solution is y = {y}')

