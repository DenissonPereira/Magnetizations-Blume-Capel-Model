# Código para calcular as magnetizações de spin das sub-redes
# Baseado no modelo de Blume-Capel.

# Parâmetros:
# m_i - Magnetiação por unidade de partícula da sub-rede i
# D_i - Anisotropia da sub-rede i
# gamma_i - Parametro variacional da sub-rede i
# beta - 1 / Kb*T, onde Kb é a constante de Boltzmann e T é a temperatura

import sys

tipo_A = str(input("Digite o tipo de spin da primeira sub-rede (semi ou int): "))
if not (tipo_A == "semi" or tipo_A == "int"):
    print("Tipo de spin não reconhecido. \nReinicie o programa!")
    sys.exit()

tipo_B = str(input("Digite o tipo de spin da segunda sub-rede (semi ou int): "))
if not (tipo_B == "semi" or tipo_B == "int"):
    print("Tipo de spin não reconhecido. \nReinicie o programa!")
    sys.exit()

if tipo_A == "semi" and tipo_B == "semi":
    from spin_semi_inteiro_A import sub_rede_semi_A, m_semi_A
    from spin_semi_inteiro_B import sub_rede_semi_B, m_semi_B
    print("m_{} = {}; \n\nm_{} = {}.".format(sub_rede_semi_A, m_semi_A, sub_rede_semi_B, m_semi_B))

if tipo_A == "semi" and tipo_B == "int":
    from spin_semi_inteiro_A import sub_rede_semi_A, m_semi_A
    from spin_inteiro_B import sub_rede_int_B, m_int_B
    print("m_{} = {}; \n\nm_{} = {}.".format(sub_rede_semi_A, m_semi_A, sub_rede_int_B, m_int_B))

if tipo_A == "int" and tipo_B == "semi":
    from spin_inteiro_A import sub_rede_int_A, m_int_A
    from spin_semi_inteiro_B import sub_rede_semi_B, m_semi_B
    print("m_{} = {}; \n\nm_{} = {}.".format(sub_rede_int_A, m_int_A, sub_rede_semi_B, m_semi_B))

if tipo_A == "int" and tipo_B == "int":
    from spin_inteiro_A import sub_rede_int_A, m_int_A
    from spin_inteiro_B import sub_rede_int_B, m_int_B
    print("m_{} = {}; \n\nm_{} = {}.".format(sub_rede_int_A, m_int_A, sub_rede_int_B, m_int_B))