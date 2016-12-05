from hashlib import md5

input = 'wtnhxymk'

first_password = ''
charsNeeded = 8
second_password = [None] * charsNeeded

index = 0

while None in second_password:
    digest = md5(input + str(index)).hexdigest()
    index += 1

    if digest.startswith('00000'):
        if len(first_password) < charsNeeded:
            first_password += digest[5]

        position = int(digest[5], 16)
        if position < 8 and second_password[position] is None:
            second_password[position] = digest[6]

print first_password
print ''.join(second_password)
