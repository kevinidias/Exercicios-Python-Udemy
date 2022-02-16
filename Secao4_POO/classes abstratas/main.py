from classes_abstratas import Conta, ContaPoupanca, ContaCorrente

cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(6)
cp.depositar(20)
print('#########')

cc = ContaCorrente(111, 333, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)