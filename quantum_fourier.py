# """
# This module contains the Quantum Fourier Transform class.
# """

# from numpy import pi
# from qiskit import QuantumCircuit, transpile 
# from qiskit_aer  import Aer
# from qiskit import QuantumCircuit, transpile
# from qiskit import QuantumCircuit,assemble



# class QuantumFourierTransform:
#     """Class for operations of the Quantum Fourier Transform."""

#     @staticmethod
#     def simulate(state: int) -> dict:
#         """Simulate the QFT and iQFT.

#         Parameters
#         ----------
#             state (int): The state to simulate.

#         Returns
#         -------
#             dict: The simulated state.
#         """
#         # Get the number of qubits.
#         qubit_count = state.bit_length()

#         # Create the circuit.
#         circuit = QuantumCircuit(qubit_count, qubit_count)

#         # Apply the initial state.
#         for qubit in range(qubit_count):
#             if state & (1 << qubit):
#                 circuit.x(qubit)

#         # Apply the QFT.
#         circuit = QuantumFourierTransform.qft(circuit)

#         # Apply the inverse QFT.
#         circuit = QuantumFourierTransform.iqft(circuit)

#         # Append the measurement.
#         circuit.measure(range(qubit_count), range(qubit_count))

#         # Run the simulation.
#         simulator = Aer.get_backend("aer_simulator")
#         circuit = transpile(circuit, simulator)
#         job = simulator.run(assemble(circuit))
#         result = job.result().get_counts()

#         answer_as_list = list(result.keys())
#         answer_int = int(answer_as_list[0], 2)
#         return {"result": answer_int}

#     @staticmethod
#     def qft(circuit: QuantumCircuit) -> QuantumCircuit:
#         """Apply QFT to a circuit.

#         Parameters
#         ----------
#             circuit (QuantumCircuit):  The circuit to apply the QFT to.

#         Returns
#         -------
#             QuantumCircuit: The circuit with the QFT applied.
#         """
#         # Apply the QFT to the circuit.
#         circuit = QuantumFourierTransform._qft_append_circuit(
#             circuit, circuit.num_qubits - 1
#         )

#         # Apply the swaps to the circuit.
#         circuit = QuantumFourierTransform._qft_append_swaps(circuit)

#         return circuit

#     @staticmethod
#     def qft_circuit(qubit_count: int) -> QuantumCircuit:
#         """Create a QFT circuit with given Qubit count.

#         Parameters
#         ----------
#         qubit_count : int
#             The number of qubits to use in the circuit.

#         Returns
#         -------
#         QuantumCircuit
#             The QFT circuit.
#         """
#         return QuantumFourierTransform.qft(QuantumCircuit(qubit_count))

#     @staticmethod
#     def iqft_circuit(qubit_count: int) -> QuantumCircuit:
#         """Create a iQFT circuit with given Qubit count.

#         Parameters
#         ----------
#         qubit_count : int
#             The number of qubits to use in the circuit.

#         Returns
#         -------
#         QuantumCircuit
#             The iQFT circuit.
#         """
#         return QuantumFourierTransform.iqft(QuantumCircuit(qubit_count))

#     @staticmethod
#     def iqft(circuit: QuantumCircuit) -> QuantumCircuit:
#         """Apply inverse QFT to a circuit.

#         Parameters
#         ----------
#             circuit (QuantumCircuit):  The circuit to apply the IQFT to.

#         Returns
#         -------
#             QuantumCircuit: The circuit with the iQFT applied.
#         """
#         # Apply the swaps to the circuit.
#         circuit = QuantumFourierTransform._qft_append_swaps(circuit, inverse=True)
#         circuit.barrier()

#         # Apply the QFT to the circuit.
#         circuit = QuantumFourierTransform._iqft_append_circuit(circuit, 0)

#         return circuit

#     @staticmethod
#     def _qft_append_circuit(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
#         """Apply a rotation to a qubit.

#         Parameters
#         ----------
#             circuit (QuantumCircuit): The circuit to apply the rotation to.
#             qubit (int): The qubit to apply the rotation to.

#         Returns
#         -------
#             QuantumCircuit: The circuit with the rotation applied.
#         """
#         # Recursive stop condition.
#         if qubit < 0:
#             return circuit

#         # Construct the minimal QFT circuit.
#         circuit.h(qubit)
#         for qubit_line in reversed(range(qubit)):
#             circuit.cp(pi / 2 ** (qubit - qubit_line), qubit_line, qubit)
#         circuit.barrier()

#         # Recursively apply the QFT to the next qubit.
#         return QuantumFourierTransform._qft_append_circuit(circuit, qubit - 1)

#     @staticmethod
#     def _iqft_append_circuit(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
#         """Apply a rotation to a qubit.

#         Parameters
#         ----------
#             circuit (QuantumCircuit): The circuit to apply the rotation to.
#             qubit (int): The qubit to apply the rotation to.

#         Returns
#         -------
#             QuantumCircuit: The circuit with the rotation applied.
#         """
#         # Recursive stop condition.
#         if qubit >= circuit.num_qubits:
#             return circuit

#         # Construct the minimal QFT circuit.
#         for qubit_line in range(qubit):
#             circuit.cp(-pi / 2 ** (qubit - qubit_line), qubit_line, qubit)
#         circuit.h(qubit)
#         circuit.barrier()

#         # Recursively apply the QFT to the next qubit.
#         return QuantumFourierTransform._iqft_append_circuit(circuit, qubit + 1)

#     @staticmethod
#     def _qft_append_swaps(
#         circuit: QuantumCircuit, inverse: bool = False
#     ) -> QuantumCircuit:
#         """Apply swaps to a circuit.

#         Parameters
#         ----------
#             circuit (QuantumCircuit): The circuit to apply the swaps to.
#             qubit (int): The qubit to apply the rotation to.

#         Returns
#         -------
#             QuantumCircuit: The circuit with the swaps applied.
#         """
#         qubit_count = circuit.num_qubits
#         qubits_list = (
#             reversed(range(qubit_count // 2))
#             if not inverse
#             else range(qubit_count // 2)
#         )
#         for qubit in qubits_list:
#             circuit.swap(qubit, qubit_count - qubit - 1)
#         return circuit



# if __name__ == "__main__":
#     print("===================================")
#     print("Quantum Fourier Transform Simulator")
#     print("===================================")

#     # Get the input state as integer decimal.
#     state_int = int(input("> Enter the state as decimal integer: "))

#     # Run the algorithm.
#     result = QuantumFourierTransform.simulate(state_int)
#     print(f"iQFT result: {result['result']}")
"""
This module contains the Quantum Fourier Transform class.
"""

from numpy import pi
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
# Removed redundant imports and 'assemble'


class QuantumFourierTransform:
    """Class for operations of the Quantum Fourier Transform."""

    @staticmethod
    def simulate(state: int) -> dict:
        """Simulate the QFT and iQFT.

        Parameters
        ----------
            state (int): The state to simulate.

        Returns
        -------
            dict: The simulated state.
        """
        # Get the number of qubits.
        qubit_count = state.bit_length()
        if qubit_count == 0 and state == 0: # Handle the case for state = 0
            qubit_count = 1 # QFT on 0 qubits is not well-defined, simulate on 1 qubit |0>

        # Create the circuit.
        circuit = QuantumCircuit(qubit_count, qubit_count)

        # Apply the initial state.
        for qubit in range(qubit_count):
            if state & (1 << qubit):
                circuit.x(qubit)

        # Apply the QFT.
        circuit = QuantumFourierTransform.qft(circuit)

        # Apply the inverse QFT.
        circuit = QuantumFourierTransform.iqft(circuit)

        # Append the measurement.
        circuit.measure(range(qubit_count), range(qubit_count))

        # Run the simulation.
        simulator = Aer.get_backend("aer_simulator")
        # Transpile the circuit for the simulator
        circuit = transpile(circuit, simulator)
        # Run the circuit directly, without assemble
        job = simulator.run(circuit)
        result = job.result().get_counts()

        # The result keys are binary strings. If there's only one outcome (ideal simulation),
        # this will get it. For noisy simulations, you might get multiple outcomes.
        # We assume an ideal simulation for this problem structure.
        if not result: # Handle cases where simulation might yield no counts (e.g., very small qubit_count with oddities)
            # This case should ideally not happen with the current setup if state > 0 or state = 0 with qubit_count = 1
            # For state = 0, after QFT and iQFT, it should remain 0.
            return {"result": 0}

        answer_as_list = list(result.keys())
        # Qiskit's bit ordering is typically Qn-1 ... Q1 Q0.
        # The integer conversion should handle this correctly if the binary string represents the state.
        answer_int = int(answer_as_list[0], 2)
        return {"result": answer_int}

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
        # The _qft_append_circuit starts from the most significant qubit (num_qubits - 1) down to 0
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
        if qubit_count <= 0:
            raise ValueError("Qubit count must be positive.")
        return QuantumFourierTransform.qft(QuantumCircuit(qubit_count))

    @staticmethod
    def iqft_circuit(qubit_count: int) -> QuantumCircuit:
        """Create a iQFT circuit with given Qubit count.

        Parameters
        ----------
        qubit_count : int
            The number of qubits to use in the circuit.

        Returns
        -------
        QuantumCircuit
            The iQFT circuit.
        """
        if qubit_count <= 0:
            raise ValueError("Qubit count must be positive.")
        return QuantumFourierTransform.iqft(QuantumCircuit(qubit_count))

    @staticmethod
    def iqft(circuit: QuantumCircuit) -> QuantumCircuit:
        """Apply inverse QFT to a circuit.

        Parameters
        ----------
            circuit (QuantumCircuit):  The circuit to apply the IQFT to.

        Returns
        -------
            QuantumCircuit: The circuit with the iQFT applied.
        """
        # Apply the swaps to the circuit first for iQFT if QFT ended with swaps.
        circuit = QuantumFourierTransform._qft_append_swaps(circuit, inverse=False) # Swaps are their own inverse in this symmetric context
        circuit.barrier()

        # Apply the inverse QFT operations to the circuit.
        # The _iqft_append_circuit starts from qubit 0 up to num_qubits - 1
        circuit = QuantumFourierTransform._iqft_append_circuit(circuit, 0)

        return circuit

    @staticmethod
    def _qft_append_circuit(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
        """Apply QFT core operations recursively, from MSB to LSB.

        Parameters
        ----------
            circuit (QuantumCircuit): The circuit to apply the rotation to.
            qubit (int): The current qubit to apply operations to (from num_qubits-1 down to 0).

        Returns
        -------
            QuantumCircuit: The circuit with the rotation applied.
        """
        # Recursive stop condition.
        if qubit < 0:
            return circuit

        # Apply H gate to the current qubit.
        circuit.h(qubit)
        # Apply controlled rotations.
        for control_qubit in range(qubit): # Corrected loop: control_qubit should be less than qubit
            # The controlled phase rotation angle depends on the distance between control and target
            # For QFT, target is 'qubit', control is 'control_qubit'
            # The rotation is P(pi / 2^(k)) where k is (target - control)
            # Qiskit's cp(theta, control, target)
            # In standard QFT definition, we iterate j from 0 to qubit-1
            # and apply CROT_k from qubit j to qubit n-1 (current MSB).
            # Here, 'qubit' is the target (n-1, then n-2, etc.).
            # 'qubit_line' is the control qubit (0, 1, ..., 'qubit'-1)
            # Standard QFT definition from Nielsen & Chuang applies H to qubit k,
            # then for j = k+1 to n-1, applies CROT_{j-k} to qubit k controlled by qubit j.
            # This implementation seems to go from MSB (qubit = n-1) down.
            # When processing `qubit`, it is the target for H and controlled rotations.
            # Control qubits are those with lower indices (0 to qubit-1).
            # The order of loops in most textbooks:
            # for j = 0 to n-1:
            #   H(j)
            #   for k = j+1 to n-1:
            #     CP(pi/2^(k-j), k, j)  <-- note control is k, target is j
            # This code structure: process qubit 'qubit' (from n-1 down to 0)
            # H(qubit)
            # for 'qubit_line' from 0 to 'qubit'-1 (reversed in the code, but range is fine)
            #   CP(pi/2^('qubit' - 'qubit_line'), 'qubit_line', 'qubit')
            # This corresponds to another valid way of writing QFT.
            # `qubit_line` iterates from `qubit-1` down to `0`.
            # Example: n=3.
            # qubit = 2 (MSB): H(2).
            #   qubit_line = 1: cp(pi/2^(2-1), 1, 2) = cp(pi/2, 1, 2)
            #   qubit_line = 0: cp(pi/2^(2-0), 0, 2) = cp(pi/4, 0, 2)
            # qubit = 1: H(1).
            #   qubit_line = 0: cp(pi/2^(1-0), 0, 1) = cp(pi/2, 0, 1)
            # qubit = 0: H(0).
            # This looks correct.
            circuit.cp(pi / 2 ** (qubit - control_qubit), control_qubit, qubit)

        # It's common to put a barrier after processing each qubit stage in QFT for visualization
        if circuit.num_qubits > 1 and qubit > 0 : # Avoid barrier after the last H if it's the only op on LSB
             circuit.barrier()


        # Recursively apply the QFT to the next qubit.
        return QuantumFourierTransform._qft_append_circuit(circuit, qubit - 1)

    @staticmethod
    def _iqft_append_circuit(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
        """Apply inverse QFT core operations recursively, from LSB to MSB.

        Parameters
        ----------
            circuit (QuantumCircuit): The circuit to apply the rotation to.
            qubit (int): The current qubit to apply operations to (from 0 up to num_qubits-1).

        Returns
        -------
            QuantumCircuit: The circuit with the rotation applied.
        """
        # Recursive stop condition.
        if qubit >= circuit.num_qubits:
            return circuit

        # Apply controlled inverse rotations first.
        # 'qubit' is the target. 'control_qubit' are qubits with lower indices.
        for control_qubit in range(qubit): # control_qubit from 0 to qubit-1
            circuit.cp(-pi / 2 ** (qubit - control_qubit), control_qubit, qubit)
        # Apply H gate to the current qubit.
        circuit.h(qubit)

        # Optional barrier for visualization
        if circuit.num_qubits > 1 and qubit < circuit.num_qubits -1:
            circuit.barrier()


        # Recursively apply the iQFT to the next qubit.
        return QuantumFourierTransform._iqft_append_circuit(circuit, qubit + 1)
    # (Inside the QuantumFourierTransform class)

    @staticmethod
    def get_full_simulation_circuit(state: int) -> QuantumCircuit:
        """Constructs the full circuit used in simulation
        (state preparation + QFT + iQFT + measurement).

        Parameters
        ----------
            state (int): The state to prepare for the circuit.

        Returns
        -------
            QuantumCircuit: The constructed quantum circuit.
        """
        # Get the number of qubits.
        qubit_count = state.bit_length()
        if qubit_count == 0 and state == 0: # Handle the case for state = 0
            qubit_count = 1

        # Create the circuit.
        circuit = QuantumCircuit(qubit_count, qubit_count)

        # Apply the initial state.
        initial_state_label = f"Init |{state:0{qubit_count}b}>" # Binary representation
        for qubit in range(qubit_count):
            if state & (1 << qubit):
                circuit.x(qubit)
        circuit.barrier(label=initial_state_label)


        # Apply the QFT.
        circuit = QuantumFourierTransform.qft(circuit)
        circuit.barrier(label="QFT") # Add barrier after full QFT for clarity

        # Apply the inverse QFT.
        circuit = QuantumFourierTransform.iqft(circuit)
        # The iQFT method itself might add barriers.
        # You can add another one here if needed: circuit.barrier(label="iQFT complete")


        # Append the measurement.
        circuit.measure(range(qubit_count), range(qubit_count))

        return circuit
    @staticmethod
    def _qft_append_swaps(
        circuit: QuantumCircuit, inverse: bool = False
    ) -> QuantumCircuit:
        """Apply swaps to a circuit to reverse qubit order.
           The 'inverse' flag is somewhat misleading here, as the swap sequence
           is its own inverse. The original code used it to change iteration direction,
           but for swapping (q_i, q_{n-1-i}), the direction doesn't change the final set of swaps.

        Parameters
        ----------
            circuit (QuantumCircuit): The circuit to apply the swaps to.
            inverse (bool): If True, iterates swaps in reverse order. For symmetric swaps, this has no effect on the set of swaps.

        Returns
        -------
            QuantumCircuit: The circuit with the swaps applied.
        """
        qubit_count = circuit.num_qubits
        # The iteration order (normal or reversed) for selecting pairs to swap
        # does not change the final state if all necessary pairs are swapped.
        # We need to swap qubit i with qubit (qubit_count - 1 - i)
        # for i from 0 to (qubit_count // 2) - 1.
        for qubit in range(qubit_count // 2):
            circuit.swap(qubit, qubit_count - qubit - 1)
        return circuit



if __name__ == "__main__":
    print("===================================")
    print("Quantum Fourier Transform Simulator")
    print("===================================")

    while True:
        try:
            # Get the input state as integer decimal.
            state_str = input("> Enter the state as decimal integer (or 'q' to quit): ")
            if state_str.lower() == 'q':
                break
            state_int = int(state_str)
            if state_int < 0:
                print("Please enter a non-negative integer.")
                continue

            # Run the algorithm.
            print(f"Simulating for state: {state_int}")
            result = QuantumFourierTransform.simulate(state_int)
            print(f"Input state: {state_int}, iQFT result (output state): {result['result']}")
            if result['result'] == state_int:
                print("SUCCESS: Input state matches output state.")
            else:
                print(f"MISMATCH: Expected {state_int}, got {result['result']}.")
            print("-----------------------------------")

        except ValueError:
            print("Invalid input. Please enter a decimal integer or 'q'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Example test cases to ensure QFT and iQFT logic
    # print("\nRunning internal tests...")
    # for n_qubits_test in range(1, 5): # Test for 1 to 4 qubits
    #     print(f"\nTesting QFT and iQFT for {n_qubits_test} qubits")
    #     qc_test_qft = QuantumFourierTransform.qft_circuit(n_qubits_test)
    #     # print("QFT circuit:")
    #     # print(qc_test_qft.draw(output='text'))

    #     qc_test_iqft = QuantumFourierTransform.iqft_circuit(n_qubits_test)
    #     # print("iQFT circuit:")
    #     # print(qc_test_iqft.draw(output='text'))
        
    #     # Test if QFT followed by iQFT is identity
    #     identity_test_circuit = QuantumCircuit(n_qubits_test, n_qubits_test)
    #     identity_test_circuit.compose(qc_test_qft, inplace=True)
    #     identity_test_circuit.compose(qc_test_iqft, inplace=True)
    #     # print("QFT . iQFT circuit (should be identity up to global phase):")
    #     # print(identity_test_circuit.draw(output='text'))


    # Test a specific simulation
    # state_to_test = 5 # Example: |101> for 3 qubits
    # num_q_test = state_to_test.bit_length()
    # if num_q_test == 0 and state_to_test == 0: num_q_test = 1

    # print(f"\nTesting simulation for state {state_to_test} ({num_q_test} qubits)")
    # test_circuit = QuantumCircuit(num_q_test, num_q_test)
    # for q in range(num_q_test):
    #     if (state_to_test >> q) & 1:
    #         test_circuit.x(q)
    # print("Initial state circuit:")
    # print(test_circuit.draw(output='text'))

    # test_circuit = QuantumFourierTransform.qft(test_circuit)
    # print("After QFT:")
    # print(test_circuit.draw(output='text'))

    # test_circuit = QuantumFourierTransform.iqft(test_circuit)
    # print("After iQFT:")
    # print(test_circuit.draw(output='text'))

    # test_circuit.measure_all() # Use measure_all for simplicity if measuring all to classical bits of same index
    # # print("Final circuit for simulation:")
    # # print(test_circuit.draw(output='text'))

    # sim = Aer.get_backend('aer_simulator')
    # t_circuit = transpile(test_circuit, sim)
    # sim_counts = sim.run(t_circuit).result().get_counts()
    # print(f"Simulation counts for state {state_to_test}: {sim_counts}")
    # sim_result_int = int(list(sim_counts.keys())[0], 2)
    # print(f"Simulated output for state {state_to_test}: {sim_result_int}")
    # assert sim_result_int == state_to_test, f"Simulation failed for state {state_to_test}"
    # print("Internal tests passed.")