def wrapper(f):
    
    def fun(phone_numbers):
        # complete the function
        for i in range(len(phone_numbers)):
            
            if (phone_numbers[i].startswith("+") or phone_numbers[i].startswith("+91")) and len(phone_numbers[i]) == 13:
                continue
            elif phone_numbers[i].startswith("91") and len(phone_numbers[i]) == 12:
                phone_numbers[i] = "+" + phone_numbers[i]
            elif phone_numbers[i].startswith("0") and len(phone_numbers[i]) == 11:
                phone_numbers[i] = "+91" + phone_numbers[i][1:]
            else:
                phone_numbers[i] = "+91" + phone_numbers[i]
                
            phone_numbers[i] = format_number(phone_numbers[i])
        
        return f(phone_numbers)
    return fun
    
def format_number(number):
    return number[0:3] + " " + number[3:8] + " " + number[8:]

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 