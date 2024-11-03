conjunto1 =  {1, 4, 7, 10}

print(f'O conjunto 1 é {conjunto1}')

conjunto2 = {1, 3, 5, 7}

print(f'O conjunto 2 é {conjunto2}')

conjunto1.intersection_update(conjunto2)
print(f'A intersseção é {conjunto1}')