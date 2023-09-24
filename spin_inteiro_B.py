from sympy import Symbol, exp, Sum, cosh, sinh, simplify

sub_rede_int_B = str(input("Qual o nome da segunda sub-rede?: "))
spin = int(input("Digite o valor do spin: "))

def S_(sub_rede_int_B: str):
    S_1 = "S_" + sub_rede_int_B
    return S_1

def D_(sub_rede_int_B: str):
    D_1 = "D_" + sub_rede_int_B
    return D_1

def gamma_(sub_rede_int_B: str):
    gamma_1 = "gamma_" + sub_rede_int_B
    return gamma_1

spin_rede = S_(sub_rede_int_B)
anisotropia_rede = D_(sub_rede_int_B)
gamma_rede = gamma_(sub_rede_int_B)

S = Symbol(spin_rede)
D = Symbol(anisotropia_rede)
gamma = Symbol(gamma_rede)
beta = Symbol("beta")

expr_1 = 2*S*exp(beta*D*S*S)*sinh(beta*gamma*S)
somatorio_1 = Sum(expr_1, (S, 1, spin))
resultado_1 = somatorio_1.doit()

expr_2 = 2*exp(beta*D*S*S)*cosh(beta*gamma*S)
somatorio_2 = Sum(expr_2, (S, 1, spin))
resultado_2 = somatorio_2.doit()

m_int_B = resultado_1 / (resultado_2 + 1)