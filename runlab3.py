import lab3.functions

while 1:
    mode = input("Какую диаграмму строить?\nВыберите: 1,2,3,4,5,6? 0-exit\n>")
    if mode == '1':
        lab3.functions.graph1()
    elif mode == '2':
        lab3.functions.graph2()
    elif mode == '3':
        lab3.functions.graph3()
    elif mode == '4':
        lab3.functions.graph4()
    elif mode == '5':
        lab3.functions.graph5()
    elif mode == '6':
        lab3.functions.graph6()
    elif mode == '0':
        exit(0)