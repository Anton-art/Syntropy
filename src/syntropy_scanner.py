```python
"""
SYNTROPIC SCANNER (MVP v1.1)
Tool for measuring the Thermodynamic Quality of Text.

Paradigm:
    Meaning is not just semantics. Meaning is Information Density + Vitality.
    We use Compression Algorithms (zlib) as a proxy for Kolmogorov Complexity.
    High-Novelty ideas trigger a Simulation Request.
"""

import zlib
import sys
import math

class SyntropyScanner:
    def __init__(self):
        # Calibration constants based on the 3:1 Rule
        self.OPTIMAL_DENSITY = 0.55  # Ideal compression ratio
        self.SIGMA_WIDTH = 0.15      # Tolerance window

    def analyze(self, text: str):
        if not text:
            return

        # 1. PHYSICS: Compression Analysis (Shannon Entropy)
        original_bytes = text.encode('utf-8')
        original_size = len(original_bytes)
        compressed_data = zlib.compress(original_bytes)
        compressed_size = len(compressed_data)
        
        # Density Ratio (0.0 = Pure Pattern, 1.0 = Pure Chaos)
        density = compressed_size / original_size

        # 2. VITALITY: The 3:1 Rule Calculation
        vitality = math.exp(-((density - self.OPTIMAL_DENSITY) ** 2) / (2 * self.SIGMA_WIDTH ** 2))

        # 3. SYNTROPY SCORE (Mu)
        length_log = math.log(original_size + 1) 
        mu_score = length_log * vitality * 10.0

        # 4. CLASSIFICATION & SIMULATION CHECK
        status = self._classify(density, vitality, text)

        self._report(mu_score, density, vitality, status, text)

    def _request_simulation(self, text, density):
        """
        Advanced Protocol for High-Novelty Ideas.
        If the idea is too chaotic (Density > 0.8) but structured enough not to be noise,
        we ask the AI to run a Thought Experiment.
        """
        if 0.8 < density < 0.95:
            return "🌪️ POTENTIAL DISRUPTION (Requires Simulation)"
        return None

    def _classify(self, density, vitality, text):
        # Check if we need a Simulation (High Novelty)
        sim_status = self._request_simulation(text, density)
        if sim_status:
            return sim_status

        if density < 0.4:
            return "🧊 STASIS (Bureaucracy/Repetition)"
        elif density > 0.95:
            return "🔥 CHAOS (Noise/Encryption)"
        elif vitality > 0.8:
            return "💎 CRYSTAL (High Meaning)"
        else:
            return "💧 LIQUID (Normal Text)"

    def _report(self, mu, density, vitality, status, text):
        preview = text[:50].replace("\n", " ") + "..." if len(text) > 50 else text
        print("-" * 60)
        print(f"INPUT:  {preview}")
        print(f"STATUS: {status}")
        
        if "DISRUPTION" in status:
            print(" [!] ALERT: High Novelty detected.")
            print(" [!] ACTION: Run a Multi-Agent Simulation to test viability.")
            
        print("-" * 60)
        print(f" > Info Density:   {density:.2f} (Target: {self.OPTIMAL_DENSITY})")
        print(f" > Vitality Index: {vitality:.2f}")
        print(f" > SYNTROPY (µ):   {mu:.2f}")
        print("-" * 60)
        print("\n")

if __name__ == "__main__":
    scanner = SyntropyScanner()
    print("=== SYNTROPY SCANNER SIMULATION ===\n")

    # TEST 1: Bureaucracy
    scanner.analyze("Process the process to process the process." * 5)
    
    # TEST 2: High Novelty (Disruption)
    # A complex, dense idea that might look like chaos to a simple filter
    disruption = "Abolish fiat currency. Replace with dynamic reputation tokens backed by energy credits and verified by zero-knowledge proofs."
    scanner.analyze(disruption)

    # TEST 3: Crystal (Syntropy)
    scanner.analyze("AI is the Environment. Human is the Particle. Together they form Reason.")
```
