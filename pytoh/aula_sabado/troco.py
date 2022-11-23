import time
start_time = time.time()
def calc_troco(valor,cedulas,troco_agora,pos):
    cedulas[pos] += 1
    troco_agora+=valor
    return troco_agora

def print_cedulas(cedulas):
    if cedulas[0] != 0:
        print("cedulas de 100: %d" % cedulas[0])
    if cedulas[1] != 0:
        print("cedulas de 50: %d" % cedulas[1])
    if cedulas[2] != 0:
        print("cedulas de 10: %d" % cedulas[2])
    if cedulas[3] != 0:
        print("cedulas de 5: %d" % cedulas[3])
    if cedulas[4] != 0:
        print("cedulas de 1: %d" % cedulas[4])
    if cedulas[5] != 0:
        print("moedas de 0.50: %d" % cedulas[5])
    if cedulas[6] != 0:
        print("moedas de 0.10: %d" % cedulas[6])
    if cedulas[7] != 0:
        print("moedas de 0.05: %d" % cedulas[7])
    if cedulas[8] != 0:
        print("moedas de 0.01: %d" % cedulas[8])

total = float(input('Valor total da compra'))
dinheiro_dado = float(input('Dinnheiro dado'))

troco = dinheiro_dado-total
print(troco)
troco_ok=False
# 100 , 50, 10, 5, 1, 0.5, 0.10, 0.05,0.01
cedulas = [0,0,0,0,0,0,0,0,0]
troco_agora = 0
while troco_ok == False:
    print(troco_agora)
    if (troco-troco_agora) >=100:
        troco_agora=calc_troco(100,cedulas,troco_agora,0)
    elif (troco-troco_agora) >=50:
        troco_agora=calc_troco(50,cedulas,troco_agora,1)
    elif (troco-troco_agora) >=10:
        troco_agora=calc_troco(10,cedulas,troco_agora,2)
    elif (troco-troco_agora) >=5:
        troco_agora=calc_troco(5,cedulas,troco_agora,3)
    elif (troco-troco_agora) >=1:
        troco_agora=calc_troco(1,cedulas,troco_agora,4)
    elif (troco-troco_agora) >=0.50:
        troco_agora=calc_troco(0.50,cedulas,troco_agora,5)
    elif (troco-troco_agora) >=0.10:
        troco_agora=calc_troco(0.10,cedulas,troco_agora,6)
    elif (troco-troco_agora) >=0.05:
        troco_agora=calc_troco(0.05,cedulas,troco_agora,7)
    elif (troco-troco_agora) >0.01:
        troco_agora=calc_troco(0.01,cedulas,troco_agora,8)
    if troco_agora >= troco or  troco_agora >= (troco-0.01):
        troco_ok = True
print(cedulas)

print_cedulas(cedulas)
print("---- %s seconds ----" % (time.time() - start_time))




