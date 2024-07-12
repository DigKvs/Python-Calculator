# função pegar valores

def valValidReal() :
    while True : 
        try:
            num = float(input('digite um numero --> '))
            
        except ValueError :
            print('digite somente numeros')
            
        else :
            return(num)
        
# função pegar valores sem ser zero

def valValidRealNoZero() :
    while True : 
        try:
            num = float(input('digite um numero --> '))
            if num == 0 :
                num = 's'
            
            
        except ValueError :
            print('digite somente numeros')
            
        else :
            return(num)

# funcão operações validar

def oprValid() :
    opr = input('digite a operação que vc quer (+, -, *, /, 1/x, ^, !, E) --> ')
    while True :
        if opr == '+' :
            
            res = soma()
            return res
            
        if opr == '-' :
            
            res = subtra()
            return res
            
        if opr == '*' :
            
            res = multp()
            return res
            
        if opr == '/' :
                        
            print("\npara questoes de segurança digite denovo os 2 numeros\n")
            
            num1 = valValidReal()
            num2 = valValidRealNoZero()
            
            res = divide(num1, num2)
            return res
            
        if opr == '1/x' :

            while True :            
                print('vc quer o inverso do 1 ou 2 numero?')
                oneOrTwo = int(input('( 1 ou 2 )-->  '))
                if oneOrTwo not in [1,2] :
                    print('digite somente 1 ou 2')
                else :
                    break

            if oneOrTwo == 1 :
                res = inverso1()
                return res
            else:
                res = inverso2()
                return res
            
        if opr == '^' :
            res = potencia()
            return res
        
        if opr == '!' :

            while True :            
                print('vc quer o fatorial do 1 ou 2 numero?')
                oneOrTwo = int(input('( 1 ou 2 )-->  '))
                if oneOrTwo not in [1,2] :
                    print('digite somente 1 ou 2')
                else :
                    break

            if oneOrTwo == 1 :
                res = fatorial1()
                return res
            else:
                
                res = fatorial2()
                return res

        if opr == 'E' :
            while True :            
                print('vc quer o numero de euler do 1 ou 2 numero?')
                oneOrTwo = int(input('( 1 ou 2 )-->  '))
                if oneOrTwo not in [1,2] :
                    print('digite somente 1 ou 2')
                else :
                    break

            if oneOrTwo == 1 :
                res = euler1()
                return res
            else:
                res = euler2()
                return res

# função das operações

def soma() :
    soma = num1 + num2
    return soma

def subtra() :
    subtra = num1 - num2
    return subtra

def multp() :
    multp = num1 * num2
    return multp

def divide(num1, num2) :
    divide = num1 / num2
    return divide

def inverso1() :
    inverso = 1 / num1
    return inverso

def inverso2() :
    inverso = 1 / num2
    return inverso

def potencia() :
    potencia = num1 ** num2
    return potencia

def fatorial1() :
    fatorial = 1
    num = int(num1)
    for i in range(1, num + 1) :
        fatorial = fatorial * i
    
    return fatorial

def fatorial2() :
    fatorial = 1
    k = int(num2)
    for i in range(1, k + 1) :
        fatorial = fatorial * i
    
    return fatorial

def euler1() :
    euler = 1
    num = int(num1)
    for i in range(1, num) :
        euler = euler + 1 / i

    
    return euler


def euler2() :
    euler = 1
    num = int(num2)
    for i in range(1, num + 1) :
        euler = euler + euler / i
    
    return euler
    

# função para transformar em notação cientifica

def cie(res) :
    count = 0

    if res >= 1 and res <= 9 :
        res = res
    elif res >= 1 :
        while res > 9 :
            res = res / 10
            count += 1
    else :
        while res < 1 :
            res = res * 10
            count -= 1

    return [res, count]
    
# função para transformar de cientifica para engenharia

def eng(resAndCount) :
    if resAndCount[1] % 3 == 0 :
        if resAndCount[1] == 0 :
            resFinal = resAndCount[0]
            return resFinal
        else :
            resFinal = f"{resAndCount[0]} x 10^{resAndCount[1]}"
            return resFinal
        
    elif resAndCount[1] % 3 == 1 :
        if resAndCount[1] == 1 :
            cache1 = resAndCount[0] * 10
            resFinal = f"{cache1}"        
            return resFinal
        else :
            cache1 = resAndCount[0] * 10
            cache2 = resAndCount[1] - 1
            resFinal = f"{cache1} x 10^{cache2}"
            return resFinal
    
    elif resAndCount[1] % 3 == 2 :
        cache1 = resAndCount[0] / 10
        cache2 = resAndCount[1] + 1
        resFinal = f"{cache1} x 10^{cache2}"
        return resFinal

# função tranformar 10^3 em K
    
def eng2(resFinal) :
    resFinal = str(resFinal)
    resFinal = resFinal.split(' ')
    if len(resFinal) == 1 :
        return " ".join(resFinal)
    else:
            
        if resFinal[2] == "10^3" :
            resFinal[2] = "K"
            resFinal.pop(1)

        elif resFinal[2] == "10^6" :
            resFinal[2] = "M"
            resFinal.pop(1)

        elif resFinal[2] == "10^9" :
            resFinal[2] = "G"
            resFinal.pop(1)
        
        elif resFinal[2] == "10^-3" :
            resFinal[2] = "m"
            resFinal.pop(1)

        elif resFinal[2] == "10^-6" :
            resFinal[2] = "u"
            resFinal.pop(1)

        elif resFinal[2] == "10^-9" :
            resFinal[2] = "n"
            resFinal.pop(1)

        resFinal = " ".join(resFinal)
            
        return resFinal

num1 = valValidReal()
num2 = valValidReal()

res = oprValid()

resAndCount = cie(res)

resFinal = eng(resAndCount)

resFinalTrue = eng2(resFinal)
print(resFinalTrue)
