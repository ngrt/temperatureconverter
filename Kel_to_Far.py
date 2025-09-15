def main():
    msg = str(input('\nHello! You opened Kelvin to Fahrenheit\nTo begin type "start" below!\nTo see this message again type "instructions": '))
    
    if msg == "start":
        num = int(input('Type your number in Kelvin: '))
        
        result = (num-273.15)*9/5+32
        print('Number in Fahrenheit:', result)
        
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