print('cálculo dos raios verticais'.title())

d = int(input('Entre com a extensão do trecho (m): '))
ac_a = float(input('Entre com o angulo entre alinhamentos 1-2 (dec): '))
ac_b = float(input('Entre com o angulo entre alinhamentos 2-3 (dec): '))

#1º hipotese CCS x CCS

t=d/2
raio_a = t/tan(ac_a/2)

if raio_a >= 440:
    raio_b = t/tan(ac_b/2)
    if raio_b >= 440:
        print('1º Hipotese atendida com raio 1 = {}.'.format(raio_a))
        print('1º Hipotese atendida com raio 2 = {}.'.format(raio_b))
    else:
        #2º hipotese CCS x CCT
        raio_b1=raio_b
        while True:
            ic_n2 = 6*(raio_b1)^0.5
            q_n2 = ic_n2/2
            raio_b2 = (t-q_n2)/tan(ac_b/2)
            if raio_b1 == raio_b2:
                p = (ic_n2^2)/24*raio_b2
                raio_b = raio_b2 - p
                break
            elif raio_b1 != raio_b2:
                raio_b1 = raio_b2
                continue
        print('2º Hipotese atendida com raio 1 = {}.'.format(raio_a))
        print('2º Hipotese atendida com raio 2 = {}.'.format(raio_b))
        print('Dados para curva 2: Ic = {}'.format(ic_n2))
            
else:
    #3º hipotese CCT x CCT
    raio_a1=raio_a
    while True:
        ic_n1 = 6*(raio_a1)^0.5
        q_n1 = ic_n1/2
        raio_a2 = (t-q_n1)/tan(ac_a/2)
        if raio_a1 == raio_a2:
            p = (ic_n1^2)/24*raio_a2
            raio_a = raio_a2 - p
            break
        elif raio_a1 != raio_a2:
            raio_a1 = raio_a2
            continue
    raio_b1=raio_b
    while True:
        ic_n2 = 6*(raio_b1)^0.5
        q_n2 = ic_n2/2
        raio_b2 = (t-q_n2)/tan(ac_b/2)
        if raio_b1 == raio_b2:
            p = (ic_n2^2)/24*raio_b2
            raio_b = raio_b2 - p
            break
        elif raio_b1 != raio_b2:
            raio_b1 = raio_b2
            continue
    
    print('3º Hipotese atendida com raio 1 = {}.'.format(raio_a))
    print('Dados para curva 1: Ic = {}'.format(ic_n1))
    print('3º Hipotese atendida com raio 2 = {}.'.format(raio_b))
    print('Dados para curva 2: Ic = {}'.format(ic_n2))
    
print('Final do Programa')