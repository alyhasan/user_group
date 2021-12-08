counter = 0

with open('sonar day 1.txt', encoding = 'UTF-8') as file:
    for x, line in enumerate(file):
        if x == 0:
            a = int(line)
        else:
            if int(line) - a > 0:
                print ('increase')
                counter += 1
            else:
                print ('decrease')
            a = int(line)
            
        
        print(line.strip('\r\n'))
print(counter)
