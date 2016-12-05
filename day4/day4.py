from collections import defaultdict

with open('day4.txt') as f:
    section_id_sum = 0

    for line in f.readlines():
        char_dict = defaultdict(lambda:0)

        for char in line[:len(line) - 6]:
            if char.isalpha():
                char_dict[char] += 1

        sorted_dict = [v[0] for v in sorted(char_dict.iteritems(), key=lambda(k, v): (-v, k))][:5]
        sorted_dict = sorted_dict[:5]
        checksum = line[len(line) - 7 : len(line) - 2]

        valid = True
        for letter in checksum:
            if letter not in sorted_dict:
                valid = False
                break

        if valid:
            section_id = int(line[len(line) - 11: len(line) - 8])
            section_id_sum += section_id

            room_name = ''
            for char in line[:len(line) - 11]:
                if char == '-':
                    char = ' '
                elif char.isalpha():
                    char = chr(((ord(char) - ord('a') + section_id)) % 26 + ord('a'))

                room_name += (str(char))

            print room_name

    print 'total section ids: ' + str(section_id_sum)
