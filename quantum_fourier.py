"""
This module contains the Quantum Fourier Transform class.
"""

from numpy import pi
from qiskit import QuantumCircuit


class QuantumFourierTransform:
    """Class for operations of the Quantum Fourier Transform."""

    @staticmethod
    def qft(circuit: QuantumCircuit) -> QuantumCircuit:
        """Apply QFT to a circuit.

        Parameters
        ----------
            circuit (QuantumCircuit):  The circuit to apply the QFT to.

        Returns
        -------
            QuantumCircuit: The circuit with the QFT applied.
        """
        # Apply the QFT to the circuit.
        circuit = QuantumFourierTransform._qft_append_circuit(
            circuit, circuit.num_qubits - 1
        )

        # Apply the swaps to the circuit.
        circuit = QuantumFourierTransform._qft_append_swaps(circuit)

        return circuit

    @staticmethod
    def qft_circuit(qubit_count: int) -> QuantumCircuit:
        """Create a QFT circuit with given Qubit count.

        Parameters
        ----------
        qubit_count : int
            The number of qubits to use in the circuit.

        Returns
        -------
        QuantumCircuit
            The QFT circuit.
        """
        return QuantumFourierTransform.qft(QuantumCircuit(qubit_count))

    @staticmethod
    def _qft_append_circuit(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
        """Apply a rotation to a qubit.

        Parameters
        ----------
            circuit (QuantumCircuit): The circuit to apply the rotation to.
            qubit (int): The qubit to apply the rotation to.

        Returns
        -------
            QuantumCircuit: The circuit with the rotation applied.
        """
        # Recursive stop condition.
        if qubit < 0:
            return circuit

        # Construct the minimal QFT circuit.
        circuit.h(qubit)
        for qubit_line in reversed(range(qubit)):
            circuit.cp(pi / 2 ** (qubit - qubit_line), qubit_line, qubit)
        circuit.barrier()

        # Recursively apply the QFT to the next qubit.
        return QuantumFourierTransform._qft_append_circuit(circuit, qubit - 1)

    @staticmethod
    def _qft_append_swaps(circuit: QuantumCircuit) -> QuantumCircuit:
        """Apply swaps to a circuit.

        Parameters
        ----------
            circuit (QuantumCircuit): The circuit to apply the swaps to.
            qubit (int): The qubit to apply the rotation to.

        Returns
        -------
            QuantumCircuit: The circuit with the swaps applied.
        """
        qubit_count = circuit.num_qubits

        for qubit in reversed(range(qubit_count // 2)):
            circuit.swap(qubit, qubit_count - qubit - 1)
        return circuit
