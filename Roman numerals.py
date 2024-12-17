try:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    print("Roman Numeral converter")
    user_num = int(input("Enter number to convert: "))
    # I checker
    I_checker1 = user_num + 1
    I_checker2 = I_checker1 % 10
    I_checker3 = I_checker1 // 10
    # Variables
    M_check = 0
    D_check = 0
    C_check = 0
    L_check = 0
    X_check = 0
    V_check = 0
    I_check = 0
    # Main
    if I_checker2 == 0:
        print("I" + "X" * I_checker3)
    elif I_checker2 != 0:
        M_check = user_num // M
        D_check = M_check // D
        C_check = D_check // C
        L_check = C_check // L
        X_check = L_check // X
        V_check = X_check // V
        I_check = I_check // I
        print(
            "M" * M_check + "D" * D_check + "C" * C_check + "L" * L_check + "X" * X_check + "V" * V_check + "I" * I_check)
except ValueError:
    print("Invalid Input")