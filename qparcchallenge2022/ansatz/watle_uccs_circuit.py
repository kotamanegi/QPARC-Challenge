from qulacs import QuantumCircuit
from qulacs.gate import CZ, RY , H ,CNOT, Z, RX,RZ,X,Y
from qparcchallenge2022.WATLE import get_energy_EX, hamil_think, make_pair_patan



import numpy as np
# Set up the ansatz


def watle_uccs_circuit(theta_list, *, n_qubits, depth):
    #疑似UCCS です。
    """
    Args:
        n_qubits:
            The number of qubit used
        depth:
            Depth of the circuit.
        theta_list:
            Rotation angles.
    Returns:
        circuit:
            Resulting Ry ansatz circuit.
    """
    
    RZ_kando = 1.0 
    patan =  make_pair_patan(n_qubits,random_map=False)

    ha_qubit = n_qubits //2
    circuit = QuantumCircuit(n_qubits)
    (pata_XXU,pata_XXD,unuse) = patan
    n_qubit = n_qubits
    params_id = 0
    for tlot_kai in range(depth):
        for k in range(n_qubit):
            circuit.add_gate(RZ(k, theta_list[params_id]*RZ_kando))
            params_id+=1
            
        #すべてを[Z Z]で適当につなげる
        for a in range(n_qubit):
            for b in range(a+1,n_qubit):
                #aとbをつなげる
                circuit.add_gate(CNOT(a, b))
                circuit.add_gate(RZ(b, theta_list[params_id]*RZ_kando))
                params_id+=1
                circuit.add_gate(CNOT(a, b))



        for i in range(len(pata_XXU)):
            pair_syo = list(range(n_qubit))
            pata_XXUD = pata_XXU[i] + pata_XXD[i]
            for pa in pata_XXUD:
                (a, b) = pa
                pair_syo[a] = a
                pair_syo[b] = a
            
            for k in range(n_qubit):
                for h in range(k + 1, n_qubit):
                    if pair_syo[k] > pair_syo[h]:
                        circuit.add_gate(CZ(k, h))

            for k in range(n_qubit):
                circuit.add_gate(Z(k))
                circuit.add_gate(RX(k, np.pi / 2))

            for pa in pata_XXUD:
                (a, b) = pa
                circuit.add_gate(CNOT(a, b))
                circuit.add_gate(H(a))
            
            for k in range(n_qubit):
                circuit.add_gate(RZ(k, theta_list[params_id]*RZ_kando))
                params_id+=1
            
            for pa in pata_XXUD:
                (a, b) = pa
                circuit.add_gate(H(a))
                circuit.add_gate(CNOT(a, b))
                
            for k in range(n_qubit):
                circuit.add_gate(RX(k, -np.pi / 2))
                circuit.add_gate(Z(k))

            for k in range(n_qubit):
                for h in range(k + 1, n_qubit):
                    if pair_syo[k] > pair_syo[h]:
                        circuit.add_gate(CZ(k, h))

    return circuit


def watle_uccs_circuit_theta_len(n_qubits, depth):
    """ry_ansatz_circuit
    Returns length of theta_list for uccs ansatz circuit.

    Args:
        n_qubits:
            The number of qubit used
        depth:
            Depth of the circuit.
    Returns:
        theta_len:
            length of theta_list for ry ansatz circuit.
    """
    ha_qubit = n_qubits // 2
    ans = ((ha_qubit + ha_qubit%2) * n_qubits  + n_qubits*(n_qubits-1)//2 )* depth
    
    return ans
