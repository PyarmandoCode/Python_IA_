"""
Clase = Una Cuenta Bancaria
Atributos:
- Titular
- Numero de cuenta
- Saldo
Metodos:
-Depositar Dinero
-Retirar Dinero
-Consultar Dinero
********** Objetivo = es crear objetos en base a la cuenta bancaria*****
"""
class CuentaBancaria:
    def __init__(self,titular,numero,saldo):
        self.titular=titular
        self.numero=numero
        self.saldo=saldo
    def depositar(self,monto):
        self.saldo += monto   
        print(f"Se deposito S/. {monto}") 
    def retirar(self,monto):
        if monto<=self.saldo:
            self.saldo -= monto 
            print(f"Se retiro S/. {monto}")
        else:
            print("Saldo Insuficiente") 
    def mostrar_saldo(self):
        print("=============CUENTA=============")
        print("Titular:" + self.titular)
        print("Cuenta:" , self.numero)
        print(f"Saldo: {self.saldo}")
                   
                
cuenta1 = CuentaBancaria("Juan Perez","0023-4566",1000)        
cuenta2 = CuentaBancaria("Maria Lopez", "0003-33434",5000)
cuenta2.mostrar_saldo()
cuenta2.depositar(500)
cuenta2.mostrar_saldo()
cuenta2.depositar(250)
cuenta2.mostrar_saldo()
cuenta2.retirar(150)
cuenta2.mostrar_saldo()

#print(cuenta1.__dict__)
#print(cuenta2.__dict__)