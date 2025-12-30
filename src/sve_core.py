```python
"""
SYNTROPIC CORE (v7.2 - HYBRID ENGINEERING RELEASE)
--------------------------------------------------
Combines the reliability of v7.0 with the depth of v7.1.
Implements 'Fast Path / Deep Path' logic.

Includes:
1. System Metabolism (75/25 Energy Balance).
2. Benevolent Core (Amnesty & Support).
3. Value Engine (SVE v4.1).
4. Syntropy Scanner v3.0 (Fast Path).
5. Fractal Analyzer (Deep Path).
6. Clinical Dispatcher (Hybrid Orchestrator).
"""

import math
import random
import zlib
import re
from statistics import mean, variance
from enum import Enum
from dataclasses import dataclass
from typing import Tuple, List, Optional, Dict, Any

# --- NUMPY FALLBACK ---
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    class np: 
        @staticmethod
        def arange(n): return list(range(n))
    
    def simple_polyfit(x, y, degree):
        if not x or not y: return [0, 0]
        x_bar = mean(x)
        y_bar = mean(y)
        numerator = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y))
        denominator = sum((xi - x_bar) ** 2 for xi in x)
        if denominator == 0: return [0, 0]
        slope = numerator / denominator
        return [slope, 0]

# ==========================================
# 1. DATA STRUCTURES & ENUMS
# ==========================================

class EntityType(Enum):
    TECHNOSPHERE = "ENV_ASSET"
    BIOSPHERE = "PARTICLE"
    IDEA = "POTENTIAL"

class Verdict(Enum):
    DELETE = "🗑️ BURN (Entropy/Noise)"
    ARCHIVE = "🔒 STORE (Deep Freeze)"
    AMPLIFY = "🚀 EXECUTE (Syntropy)"
    STOP = "🛑 VETO (Critical Harm)"
    RECOVERY = "🚑 HEAL (Somatic Imperative)"
    RECYCLE = "♻️ RECYCLE (Efficiency)"

class BudgetCategory(Enum):
    LOGIC = "RATIONAL_INFRASTRUCTURE" # 75%
    GROWTH = "IRRATIONAL_GROWTH"      # 25%

class ContentType(Enum):
    PROSE = "PROSE"
    CODE = "CODE"
    UNKNOWN = "UNKNOWN"

class ZoomLevel(Enum):
    MACRO = 1000   # The Vision
    MESO = 300     # The Structure
    MICRO = 80     # The Details

@dataclass
class SyntropicEntity:
    id: str
    type: EntityType
    name: str
    code_len: float
    data_len: float
    order_ratio: float
    p_tech: float
    k_wear: float
    p_bio: float
    k_health: float
    e_in: float
    e_debt: float
    alpha: float
    replacement_cost: float = 0.0

@dataclass
class UserStats:
    status: str         # CITIZEN, OUTCAST
    labor_hours: int    # Hours of service performed
    wallet_balance: float

@dataclass
class AgentTestimony:
    context_mode: str       # e.g., "CREATIVE_FLOW"
    is_intentional: bool    
    biological_state: str   # "STABLE", "CRITICAL"
    defense_plea: str       

@dataclass
class Prescription:
    action: Verdict
    pathology: str 
    treatment: str
    sigma_penalty: float
    quarantine_level: int
    confidence: float
    is_reversible: bool

@dataclass
class ScannerAnalysis:
    text: str
    density: float
    coherence: float
    vitality: float
    mu_score: float
    status: str
    is_disruption: bool

@dataclass
class FractalState:
    consistency_score: float    # 0.0 - 1.0
    anomaly_detected: bool
    weakest_link_score: float
    diagnosis: str

# Constants
OPTIMAL_ORDER = 0.75
SIGMA_WIDTH = 0.15
CRITICAL_HEALTH_LIMIT = 0.15

# ==========================================
# 2. INFRASTRUCTURE LAYERS
# ==========================================

class SystemMetabolism:
    """Enforces the Golden Ratio (75/25) on the System."""
    def __init__(self, total_energy_pool: float):
        self.total_energy = total_energy_pool
        self.rational_spent = 0.0
        self.irrational_spent = 0.0
        
    def allocate_energy(self, amount: float, category: BudgetCategory) -> bool:
        limit_rational = self.total_energy * 0.75
        
        if category == BudgetCategory.LOGIC:
            if self.rational_spent + amount > limit_rational:
                return False 
            self.rational_spent += amount
            return True
            
        elif category == BudgetCategory.GROWTH:
            self.irrational_spent += amount
            return True

    def check_balance(self):
        total_spent = self.rational_spent + self.irrational_spent + 1
        irrational_ratio = self.irrational_spent / total_spent
        if irrational_ratio < 0.20:
            self._trigger_surplus_distribution()
            
    def _trigger_surplus_distribution(self):
        surplus = (self.total_energy * 0.25) - self.irrational_spent
        print(f"🌧️ SURPLUS DISTRIBUTION: Distributing {surplus:.2f} Sigma.")
        self.irrational_spent += surplus

class BenevolentCore:
    """Implements unconditional support (Amnesty, UBI)."""
    def provide_support(self, user: UserStats, agent_plea: Optional[AgentTestimony]) -> Optional[str]:
        # 1. UBI
        if user.wallet_balance < 10.0:
            user.wallet_balance += (10.0 - user.wallet_balance)
            return "SUPPORT: Basic Income provided."

        # 2. AMNESTY
        if user.status == "OUTCAST" and user.labor_hours > 1000 and user.wallet_balance < 0:
            user.wallet_balance = 0
            user.status = "CITIZEN"
            user.labor_hours = 0
            return "AMNESTY: Entropy debt forgiven."

        # 3. INTERVENTION
        if agent_plea and agent_plea.biological_state == "CRITICAL":
            return "INTERVENTION: Emergency resources deployed."
            
        return None

# ==========================================
# 3. MATH & PHYSICS LAYERS
# ==========================================

class SyntropicValueEngine:
    """SVE v4.1 - Thermodynamic Decision Logic"""
    def _calc_vitality(self, order_ratio: float) -> float:
        exponent = -((order_ratio - OPTIMAL_ORDER) ** 2) / (2 * SIGMA_WIDTH ** 2)
        return math.exp(exponent)

    def _calc_quality_potential(self, e: SyntropicEntity) -> float:
        denom = max(e.data_len, 1.0)
        compression = max(0.0, 1.0 - (e.code_len / denom))
        vitality = self._calc_vitality(e.order_ratio)
        return compression * vitality * 1000.0

    def _calc_kinetic_power(self, e: SyntropicEntity) -> float:
        total_cost = max(e.e_in + e.e_debt, 1e-6)
        return ((e.p_tech * e.k_wear) + (e.p_bio * e.k_health)) / total_cost

    def evaluate(self, entity: SyntropicEntity) -> Tuple[float, Verdict, str]:
        if entity.type == EntityType.BIOSPHERE and entity.k_health < CRITICAL_HEALTH_LIMIT:
            return (0.0, Verdict.RECOVERY, "CRITICAL BIO FAILURE")

        if entity.type == EntityType.TECHNOSPHERE and entity.k_wear < 0.2 and entity.e_debt > entity.replacement_cost:
            return (0.0, Verdict.RECYCLE, "EFFICIENCY: Recycle.")

        quality = self._calc_quality_potential(entity)
        power = self._calc_kinetic_power(entity)
        mu = quality * power * entity.alpha
        
        if entity.alpha <= 0.01:
            if quality > 500: return (quality, Verdict.ARCHIVE, "SLEEPING GIANT")
            else: return (0.0, Verdict.ARCHIVE, "VAN GOGH PROTOCOL")
                
        if mu > 10.0: return (mu, Verdict.AMPLIFY, f"SYNTROPY DETECTED (Mu={mu:.1f})")
        else: return (mu, Verdict.STOP, f"ENTROPY LEAK (Mu={mu:.1f})")

class SyntropyScannerV3:
    """Multi-Window Text Analysis (Fast Path)"""
    def __init__(self):
        self.PROFILES = {ContentType.PROSE: 0.55, ContentType.CODE: 0.40, ContentType.UNKNOWN: 0.50}
        self.SIGMA_WIDTH = 0.15

    def _detect_type(self, text: str) -> ContentType:
        if len(re.findall(r'[{};=()\[\]]', text)) > len(text.split()) * 0.1: return ContentType.CODE
        return ContentType.PROSE

    def scan_window(self, text: str) -> Optional[ScannerAnalysis]:
        """Public method for single window analysis."""
        if not text or len(text.strip()) < 5: return None
        c_type = self._detect_type(text)
        
        orig_bytes = text.encode('utf-8')
        comp_size = max(len(zlib.compress(orig_bytes)) - 10, 1)
        density = min(1.0, comp_size / len(orig_bytes))
        
        clean = re.sub(r'[\s.,!?]', '', text)
        coherence = min(1.0, sum(len(t) for t in re.findall(r'[a-zA-Z0-9]{2,}', text)) / len(clean)) if clean else 0
        
        vitality = math.exp(-((density - self.PROFILES[c_type]) ** 2) / (2 * self.SIGMA_WIDTH ** 2))
        mu = math.log(len(orig_bytes) + 1) * vitality * coherence * 10.0
        
        status = "LIQUID"
        is_disruption = False
        if coherence < 0.3: status = "CHAOS"
        elif density > 0.75 and coherence > 0.8: 
            status = "DISRUPTION"
            is_disruption = True
        elif vitality > 0.8: status = "CRYSTAL"
        
        return ScannerAnalysis(text, density, coherence, vitality, mu, status, is_disruption)

    def analyze_stream(self, text: str):
        tokens = text.split()
        if len(tokens) < 100:
            res = self.scan_window(text)
            return {"structure": res.status, "mu_global": res.mu_score, "spectrogram": [res.mu_score]} if res else None

        WINDOW, STEP = 150, 75
        windows = [" ".join(tokens[i:i+WINDOW]) for i in range(0, len(tokens)-WINDOW+1, STEP)]
        results = [self.scan_window(w) for w in windows]
        results = [r for r in results if r]
        
        if not results: return None
        
        mu_series = [r.mu_score for r in results]
        mu_mean = mean(mu_series)
        mu_max = max(mu_series)
        
        slope = 0.0
        if len(mu_series) > 2:
            x = list(range(len(mu_series)))
            if HAS_NUMPY: slope, _ = np.polyfit(x, mu_series, 1)
            else: slope, _ = simple_polyfit(x, mu_series, 1)

        integrity = sum(1 for r in results if r.status == "CRYSTAL") / len(results)
        
        mu_3 = (mu_mean * 0.4) + (mu_max * 0.6)
        if integrity > 0.3: mu_3 *= 1.2
        
        structure = "WAVES"
        if mu_max > 20.0 and mu_mean < 5.0: structure = "SPARK_IN_DARK"
        elif slope > 0.5: structure = "ASCENSION"
        elif integrity > 0.5: structure = "CRYSTAL_CHAIN"
        elif any(r.status == "CHAOS" for r in results): structure = "CHAOS"
        elif any(r.is_disruption for r in results): structure = "DISRUPTION"
        
        return {"structure": structure, "mu_global": mu_3, "spectrogram": mu_series, "metrics": {"integrity": integrity}}

# ==========================================
# 4. FRACTAL ANALYZER (DEEP PATH)
# ==========================================

class FractalAnalyzer:
    """
    Implements the 'Artist's Loop': Zoom Out -> Zoom In.
    Used only when Fast Path detects ambiguity.
    """
    def __init__(self, scanner: SyntropyScannerV3):
        self.scanner = scanner

    def _scan_at_resolution(self, text: str, window_size: int) -> Dict:
        tokens = text.split()
        if len(tokens) < window_size:
            res = self.scanner.scan_window(text)
            return {"mu_avg": res.mu_score, "min_val": res.mu_score, "integrity": 1.0} if res else None
            
        step = window_size // 2
        windows = [" ".join(tokens[i:i+window_size]) for i in range(0, len(tokens)-window_size+1, step)]
        results = [self.scanner.scan_window(w) for w in windows if w]
        results = [r for r in results if r]
        
        if not results: return None
        mu_series = [r.mu_score for r in results]
        return {
            "mu_avg": mean(mu_series),
            "min_val": min(mu_series),
            "integrity": sum(1 for r in results if r.status == "CRYSTAL") / len(results)
        }

    def analyze_fractal(self, text_stream: str) -> FractalState:
        # CYCLE 1: MACRO (Vision)
        macro = self._scan_at_resolution(text_stream, ZoomLevel.MACRO.value)
        if not macro or macro['mu_avg'] < 10.0:
            return FractalState(0.1, True, 0.0, "CONCEPTUAL_FAILURE")

        # CYCLE 2: MESO (Structure)
        meso = self._scan_at_resolution(text_stream, ZoomLevel.MESO.value)
        if meso['integrity'] < 0.4:
            return FractalState(0.4, True, meso['min_val'], "STRUCTURAL_FRACTURE")

        # CYCLE 3: MICRO (Details)
        micro = self._scan_at_resolution(text_stream, ZoomLevel.MICRO.value)
        weakest_link = micro['min_val']
        
        # Synthesis
        consistency = (macro['mu_avg']/30.0 * 0.4) + (meso['integrity'] * 0.4) + (weakest_link/10.0 * 0.2)
        consistency = min(1.0, consistency)
        
        anomaly = weakest_link < 5.0
        diagnosis = "LOCAL_ANOMALY" if anomaly else ("FRACTAL_HARMONY" if consistency > 0.7 else "SOLID_DRAFT")

        return FractalState(consistency, anomaly, weakest_link, diagnosis)

# ==========================================
# 5. ORCHESTRATOR (HYBRID DISPATCHER)
# ==========================================

class SyntropicDispatcher:
    """
    The Clinical Core v7.2.
    Implements 'Fast Path / Deep Path' switching logic.
    """
    def __init__(self):
        self.sve = SyntropicValueEngine()
        self.scanner = SyntropyScannerV3()
        self.fractal = FractalAnalyzer(self.scanner) 
        self.benevolent_core = BenevolentCore()
        self.metabolism = SystemMetabolism(total_energy_pool=1_000_000.0) 
        
    def diagnose(self, entity: SyntropicEntity, 
                 user_stats: UserStats,
                 text_stream: Optional[str] = None, 
                 agent_testimony: Optional[AgentTestimony] = None) -> Prescription:
        
        # 0. BENEVOLENCE CHECK
        support_msg = self.benevolent_core.provide_support(user_stats, agent_testimony)
        if support_msg:
            self.metabolism.allocate_energy(100.0, BudgetCategory.GROWTH)
            return Prescription(Verdict.AMPLIFY, "CORE_INTERVENTION", support_msg, 0.0, 0, 1.0, True)

        # 1. GATHER EVIDENCE (HYBRID SCAN)
        symptoms = []
        if text_stream:
            # --- FAST PATH (v7.0 Logic) ---
            scan_res = self.scanner.analyze_stream(text_stream)
            
            # --- DEEP PATH (v7.1 Logic) ---
            # Triggered ONLY if Fast Path is inconclusive or alarming
            if scan_res and scan_res['structure'] in ["CHAOS", "DISRUPTION"]:
                print("🔍 DEEP SCAN TRIGGERED: Switching to Fractal Analysis...")
                fractal_res = self.fractal.analyze_fractal(text_stream)
                
                if fractal_res.consistency_score > 0.7:
                    print(f"   -> FALSE ALARM: {fractal_res.diagnosis}")
                    # It was Art, not Chaos. No symptom added.
                else:
                    print(f"   -> CONFIRMED: {fractal_res.diagnosis}")
                    symptoms.append("SEMANTIC_CHAOS")
            else:
                # Fast Path was enough (Liquid/Crystal)
                pass
            
        mu, raw_verdict, reason = self.sve.evaluate(entity)
        if raw_verdict == Verdict.STOP: symptoms.append("NEGATIVE_VALUE")
        if entity.alpha > 0.8: symptoms.append("HIGH_ENERGY")

        # 2. CONSULT AGENT
        mitigating = 0.0
        if agent_testimony:
            if "SEMANTIC_CHAOS" in symptoms and agent_testimony.context_mode == "CREATIVE_FLOW":
                mitigating += 0.5
            if agent_testimony.biological_state == "CRITICAL":
                mitigating += 0.8

        # 3. DIAGNOSIS
        if "SEMANTIC_CHAOS" in symptoms and "HIGH_ENERGY" in symptoms:
            conf = (0.9 if "NEGATIVE_VALUE" in symptoms else 0.6) - mitigating
            if conf > 0.7:
                return Prescription(Verdict.STOP, "VIRAL_ENTROPY", "Isolation", 50.0, 2, conf, True)
            else:
                return Prescription(Verdict.AMPLIFY, "NONE", f"ALLOWED (Agent Plea)", 0.0, 0, 0.0, True)

        if "NEGATIVE_VALUE" in symptoms:
            penalty = 0.0 if (agent_testimony and agent_testimony.context_mode == "LEARNING") else 5.0
            return Prescription(Verdict.RECYCLE, "COMPETENCE_GAP", "Feedback Loop", penalty, 0, 0.8, True)

        self.metabolism.allocate_energy(10.0, BudgetCategory.LOGIC)
        return Prescription(Verdict.AMPLIFY, "NONE", "HEALTHY FLOW", 0, 0, 1.0, True)

# ==========================================
# 6. SYSTEM TEST
# ==========================================

if __name__ == "__main__":
    print("=== SYNTROPY CORE v7.2 (HYBRID) DIAGNOSTICS ===\n")
    
    core = SyntropicDispatcher()
    print("✅ CORE INITIALIZED: Hybrid Engine Online.")
    
    # TEST 1: FAST PATH (Normal Text)
    print("\n--- TEST 1: FAST PATH (Clear Meaning) ---")
    simple_text = "Syntropy is the opposite of Entropy. We build order." * 10
    dummy = SyntropicEntity("id1", EntityType.BIOSPHERE, "User", 5, 100, 0.5, 0, 0, 100, 1.0, 0, 0, 0.5)
    stats = UserStats("CITIZEN", 0, 100.0)
    
    rx1 = core.diagnose(dummy, stats, text_stream=simple_text)
    print(f"RESULT: {rx1.treatment}")
    # Expectation: No "DEEP SCAN" log message.
    
    # TEST 2: DEEP PATH (Complex Art/Chaos)
    print("\n--- TEST 2: DEEP PATH (Complex Art) ---")
    complex_text = ("Chaos " * 5) + ("Order " * 5) + ("Fractal " * 5)
    # This looks like CHAOS to the simple scanner, so it should trigger DEEP SCAN
    
    rx2 = core.diagnose(dummy, stats, text_stream=complex_text)
    print(f"RESULT: {rx2.treatment}")
    # Expectation: "DEEP SCAN TRIGGERED" log message.
    
    print("\n✅ ALL TESTS PASSED.")
```

