# Quantum Fourier Transform using Qiskit
The Quantum Fourier Transform (QFT) is a quantum algorithm for performing the discrete Fourier transform (DFT) of an n-dimensional complex vector. It is a fundamental quantum algorithm that is used as a subroutine in many other quantum algorithms, including Shor's algorithm for factoring integers and the Quantum Phase Estimation algorithm. 

The QFT algorithm has an exponential speedup over classical algorithms for DFT, with a time complexity of O(n log n) for n-dimensional input, compared to O(n^2) for classical algorithms. This makes it a powerful tool for solving problems in quantum computing, such as factoring large integers and simulating quantum systems.

## QFT Circuit Diagrams
The circuit diagram of the QFT is as follows for 3 qubit input:
```
                             ░                ░ ┌───┐ ░    
q_0: ───────────────■────────░───────■────────░─┤ H ├─░──X─
                    │        ░ ┌───┐ │P(π/2)  ░ └───┘ ░  │ 
q_1: ──────■────────┼────────░─┤ H ├─■────────░───────░──┼─
     ┌───┐ │P(π/2)  │P(π/4)  ░ └───┘          ░       ░  │ 
q_2: ┤ H ├─■────────■────────░────────────────░───────░──X─
     └───┘                   ░                ░       ░    
```

The circuit diagram of the inverse QFT is as follows for 3 qubit input:
```
         ░ ┌───┐ ░                 ░                           ░ 
q_0: ─X──░─┤ H ├─░──■──────────────░──■────────────────────────░─
      │  ░ └───┘ ░  │P(-π/2) ┌───┐ ░  │                        ░ 
q_1: ─┼──░───────░──■────────┤ H ├─░──┼─────────■──────────────░─
      │  ░       ░           └───┘ ░  │P(-π/4)  │P(-π/2) ┌───┐ ░ 
q_2: ─X──░───────░─────────────────░──■─────────■────────┤ H ├─░─
         ░       ░                 ░                     └───┘ ░ 
```

## Usage
It is recommended to use a virtual environment to run the program. To install the required dependencies, run the following command:
```bash
$ pip3 install -r requirements.txt
```

To run the program interface, simply run the following command:
```bash
$ python quantum_fourier.py
```

## Application Interface
```python
from quantum_fourier import QuantumFourierTransform

# No of qubits to be used.
n = 4

# Append the QFT to a already made circuit.
circuit = QuantumCircuit(n)
circuit = QuantumFourierTransform.qft(circuit)

# Append the QFT to a already made circuit.
circuit = QuantumCircuit(n)
circuit = QuantumFourierTransform.iqft(circuit)

# Directly create a QFT/iQFT circuit.
circuit = QuantumFourierTransform.qft_circuit(n)
circuit = QuantumFourierTransform.iqft_circuit(n)

# Do a simulation with QFT + iQFT.
state_as_int = 13
result = QuantumFourierTransform.simulate(state_as_int)
print(result["result"] == state_as_int)
```