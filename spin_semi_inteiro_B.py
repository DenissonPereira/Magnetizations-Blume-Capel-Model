from sympy import Symbol, Sum, exp, cosh, sinh, simplify

sub_rede_semi_B = str(input("Qual o nome da segunda sub-rede? "))
spin = int(input("Digite o valor do spin: "))

def S_(sub_rede_semi_B: str):
    S_2 = "S_" + sub_rede_semi_B
    return S_2

def D_(sub_rede_semi_B: str):
    D_2 = "D_" + sub_rede_semi_B
    return D_2

def gamma_(sub_rede_semi_B: str):
    gamma_2 = "gamma_" + sub_rede_semi_B
    return gamma_2

spin_rede = S_(sub_rede_semi_B)
anisotropia_rede = D_(sub_rede_semi_B)
gamma_rede = gamma_(sub_rede_semi_B)

S = Symbol(spin_rede)
D = Symbol(anisotropia_rede)
gamma = Symbol(gamma_rede)
beta = Symbol("beta")

expr_1 = S*exp(beta*D*((2*S - 1)/2)**2)*sinh(beta*gamma*S/2)
somatorio_1 = Sum(expr_1, (S, 1, spin))
resultado_1 = somatorio_1.doit()

# Criando e resolvendo o somatório do denominador
expr_2 = 2*exp(beta*D*((2*S - 1)/2)**2)*cosh(beta*gamma*S/2)
somatorio_2 = Sum(expr_2, (S, 1, spin))
resultado_2 = somatorio_2.doit()

# Calculando a magnetização de sub-rede A
m_semi_B = simplify((resultado_1 / resultado_2))