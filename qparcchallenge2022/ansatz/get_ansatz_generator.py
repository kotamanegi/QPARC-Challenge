from enum import Enum
from functools import partial

from qparcchallenge2022.ansatz.kotamanegi_normal import (
    kotamanegi_ansatz_circuit,
    kotamanegi_ansatz_circuit_theta_len,
)
from qparcchallenge2022.ansatz.qulacs_ansatz_circuit import (
    qulacs_ansatz_circuit,
    qulacs_ansatz_circuit_theta_len,
)
from qparcchallenge2022.ansatz.ry_ansatz_circuit import (
    ry_ansatz_circuit,
    ry_ansatz_circuit_theta_len,
)
from qparcchallenge2022.ansatz.rxzx_ansatz_circuit import (
    rxzx_ansatz_circuit,
    rxzx_ansatz_circuit_theta_len,
)
from qparcchallenge2022.ansatz.watle_uccs_circuit import (
    watle_uccs_circuit,
    watle_uccs_circuit_theta_len,
)


class AnsatzType(Enum):
    ry_ansatz_circuit = 1
    qulacs_ansatz_circuit = 2
    kotamanegi_ansatz_circuit = 3
    rxzx_ansatz_circuit = 4
    watle_uccs_circuit = 5


def get_ansatz_generator(name: AnsatzType, *, n_qubits: int, depth: int):
    theta_list_len = 0
    if name == AnsatzType.ry_ansatz_circuit:
        circuit_generator_module = ry_ansatz_circuit
        theta_list_len = ry_ansatz_circuit_theta_len(n_qubits, depth)
    elif name == AnsatzType.qulacs_ansatz_circuit:
        circuit_generator_module = qulacs_ansatz_circuit
        theta_list_len = qulacs_ansatz_circuit_theta_len(n_qubits, depth)
    elif name == AnsatzType.kotamanegi_ansatz_circuit:
        circuit_generator_module = kotamanegi_ansatz_circuit
        theta_list_len = kotamanegi_ansatz_circuit_theta_len(n_qubits, depth)
    elif name == AnsatzType.rxzx_ansatz_circuit:
        circuit_generator_module = rxzx_ansatz_circuit
        theta_list_len = rxzx_ansatz_circuit_theta_len(n_qubits, depth)
    elif name == AnsatzType.watle_uccs_circuit:
        circuit_generator_module = watle_uccs_circuit
        theta_list_len = watle_uccs_circuit_theta_len(n_qubits, depth)

    return (
        partial(circuit_generator_module, n_qubits=n_qubits, depth=depth),
        theta_list_len,
    )

