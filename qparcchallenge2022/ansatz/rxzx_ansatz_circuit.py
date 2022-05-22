from qulacs import QuantumCircuit
from qulacs.gate import CZ, RY, RX, RZ

# Set up the ansatz


def rxzx_ansatz_circuit(theta_list, *, n_qubits, depth):
    """rxzx_ansatz_circuit
    Returns Rx Rz Rx ansatz circuit.

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

    # ローテーションゲートをマシマシにして、自由度を高めた一品。
    circuit = QuantumCircuit(n_qubits)
    params_id = 0
    for _ in range(depth):
        for i in range(n_qubits):
            circuit.add_gate(RX(i, theta_list[params_id]))
            circuit.add_gate(RZ(i, theta_list[params_id+1]))
            circuit.add_gate(RX(i, theta_list[params_id+2]))
            params_id += 3

        for i in range(n_qubits // 2):
            circuit.add_gate(CZ(2 * i, 2 * i + 1))

        for i in range(n_qubits):
            circuit.add_gate(RX(i, theta_list[params_id]))
            circuit.add_gate(RZ(i, theta_list[params_id+1]))
            circuit.add_gate(RX(i, theta_list[params_id+2]))
            params_id += 3

        for i in range(n_qubits // 2 - 1):
            circuit.add_gate(CZ(2 * i + 1, 2 * i + 2))

    for i in range(n_qubits):
        circuit.add_gate(RX(i, theta_list[params_id]))
        circuit.add_gate(RZ(i, theta_list[params_id+1]))
        circuit.add_gate(RX(i, theta_list[params_id+2]))
        params_id += 3

    return circuit


def rxzx_ansatz_circuit_theta_len(n_qubits, depth):
    """rxzx_ansatz_circuit
    Returns length of theta_list for ry ansatz circuit.

    Args:
        n_qubits:
            The number of qubit used
        depth:
            Depth of the circuit.
    Returns:
        theta_len:
            length of theta_list for ry ansatz circuit.
    """
    return (depth * 6 + 3) * n_qubits
