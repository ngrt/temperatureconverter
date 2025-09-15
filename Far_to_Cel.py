def main():
    msg = str(input('\nHello! You opened Fahrenheit to Celsius\nTo begin type "start" below!\nTo see this message again type "instructions": '))
    
    if msg == "start":
        num = int(input('Type your number in Fahrenheit: '))
        
        result = (num-32)*5/9
        print('Number in Celsius:', result)
        
        def restart():
            rst = str(input('\nStart again? yes/no: '))
            if rst == 'yes':
                main()
            if rst == 'no':
                print('')
        restart()
        
    if msg == "instructions":
        main()
main()