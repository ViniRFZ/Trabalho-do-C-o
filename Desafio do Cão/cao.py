class Cao:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        self.fome = 0
        self.cansaco = 0
        self.esta_dormindo = True
        self.esta_vivo = True

    def acordar(self):
        if self.esta_vivo:
            self.esta_dormindo = False
            print(f"{self.nome} acordou e está pronto para brincar!")
        else:
            print(f"{self.nome} não está mais entre nós...")

    def alimentar(self):
        if self.esta_vivo:
            self.fome = 0
            print(f"{self.nome} foi alimentado e não está mais com fome.")
        else:
            print(f"{self.nome} não está mais entre nós...")

    def brincar(self):
        if self.esta_vivo:
            if not self.esta_dormindo:
                self.fome += 1
                self.cansaco += 1
                print(f"Você brincou com {self.nome}. Fome: {self.fome}, Cansaço: {self.cansaco}")
                if self.fome >= 6:
                    print(f"! {self.nome} está com muita fome! {self.nome} morreu.")
                    self.esta_vivo = False
                if self.cansaco >= 5:
                    self.dormir()
            else:
                print(f"{self.nome} está dormindo. Você precisa acordar {self.nome} primeiro!")
        else:
            print(f"{self.nome} não está mais entre nós...")

    def dormir(self):
        if self.esta_vivo:
            self.cansaco = 0
            self.esta_dormindo = True
            print(f"{self.nome} está dormindo e agora está descansado.")
        else:
            print(f"{self.nome} não está mais entre nós...")

    def status(self):
        if self.esta_vivo:
            mensagem_status = (f"Status de {self.nome}:\n"
                               f"- Fome: {self.fome}\n"
                               f"- Cansaço: {self.cansaco}\n"
                               f"- Dormindo: {'Sim' if self.esta_dormindo else 'Não'}\n")
            print(mensagem_status)
        else:
            print(f"{self.nome} faleceu.")
