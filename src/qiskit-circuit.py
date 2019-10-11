from qiskit import *
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.cx(q[0], q[1])
qc.measure(q, c)
backend_sim = BasicAer.get_backend('qasm_simulator')
result = execute(qc, backend_sim).result()
print(result.get_counts(qc))
