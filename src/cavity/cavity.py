from qutip import about, basis, destroy, mesolve, ptrace, qeye, tensor, wigner

class Cavity():
    
    def __init__(self, frequency: float, dissipation_rate: float, no_states: int, current_state: int) -> None:
        self.frequency = frequency
        self.dissipation_rate = dissipation_rate
        self.no_states = no_states
        self.state = basis(no_states, current_state)
    
    def __str__(self):
        data = []
        data.append(f"Cavity Frequency: {self.frequency}")
        data.append(f"Cavity Dissipation rate: {self.dissipation_rate}")
        data.append(f"Cavity no of states: {self.no_states}")
        data.append(f"Cavity state: {self.state}")

        return "\n".join(data)