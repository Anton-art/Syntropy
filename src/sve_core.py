"""
SYNTROPIC VALUE ENGINE (SVE) v4.1
Core Decision Logic & Social Protocols.

Concept:
    Evaluates the 'Meaning' (Mu) of any Entity based on
    Thermodynamics, Information Theory, and Biological Imperatives.
    Also implements 'Flash Jury' for social conflict resolution.

Changes v4.1:
    - Integrated 'Van Gogh Protocol' (Never delete unrecognized ideas).
    - Added 'Flash Jury' (Uber-style justice).
    - Unified Testing Suite.
"""

import math
import random
from enum import Enum
from dataclasses import dataclass
from typing import Tuple, List, Optional

# ==========================================
# 1. CONSTANTS & CONFIG
# ==========================================

class EntityType(Enum):
    TECHNOSPHERE = "ENV_ASSET"  # Fungible (Machine/Code)
    BIOSPHERE = "PARTICLE"      # Non-Fungible (Human/Life)
    IDEA = "POTENTIAL"          # Information (Blueprint)

class Verdict(Enum):
    DELETE = "🗑️ BURN (Entropy/Noise)"          # Only for technical garbage
    ARCHIVE = "🔒 STORE (Deep Freeze)"          # For Ideas (High or Low potential)
    AMPLIFY = "🚀 EXECUTE (Syntropy)"           # Active Resource Allocation
    STOP = "🛑 VETO (Critical Harm)"            # Safety Stop
    RECOVERY = "🚑 HEAL (Somatic Imperative)"   # Forced Rest
    RECYCLE = "♻️ RECYCLE (Efficiency)"         # Machine replacement

# Vitality Constants (The 3:1 Rule)
OPTIMAL_ORDER = 0.75  # 75% Order
SIGMA_WIDTH = 0.15    # Tolerance window

# Safety Thresholds
CRITICAL_HEALTH_LIMIT = 0.15  # Below 15% health = Forced Stop

# ==========================================
# 2. DATA STRUCTURES
# ==========================================

@dataclass
class SyntropicEntity:
    """
    Represents any object submitted to the Environment for evaluation.
    """
    id: str
    type: EntityType
    name: str
    
    # --- INFORMATION BLOCK (Potential) ---
    code_len: float      # Compressed size (Kolmogorov complexity proxy)
    data_len: float      # Original data size
    order_ratio: float   # 0.0 (Chaos) to 1.0 (Crystal). Target: 0.75
    
    # --- PHYSICS BLOCK (Power) ---
    p_tech: float        # Technological Power (Watts/FLOPS)
    k_wear: float        # Wear factor (1.0 = New, 0.0 = Broken)
    
    # --- BIOLOGY BLOCK (Particle Health) ---
    p_bio: float         # Human/Bio Capability
    k_health: float      # Health State (1.0 = Flow, 0.0 = Death)
    
    # --- ECONOMICS BLOCK (Cost) ---
    e_in: float          # Direct Energy Cost
    e_debt: float        # Entropy Debt (Pollution/Trauma/Repair cost)
    
    # --- STATUS BLOCK ---
    alpha: float         # Activation: 0.0 (Idea) -> 1.0 (Action)
    replacement_cost: float = 0.0 # Cost to replace this entity (for Machines)

# ==========================================
# 3. THE ENGINE CLASS (MATH CORE)
# ==========================================

class SyntropicValueEngine:
    
    def _calc_vitality(self, order_ratio: float) -> float:
        """
        Implements the 3:1 Rule using a Gaussian function.
        Penalizes pure Chaos (0.0) and pure Crystal (1.0).
        Peak is at 0.75.
        """
        # Gaussian formula: e^(-(x - mu)^2 / (2*sigma^2))
        exponent = -((order_ratio - OPTIMAL_ORDER) ** 2) / (2 * SIGMA_WIDTH ** 2)
        vitality = math.exp(exponent)
        return vitality

    def _calc_quality_potential(self, e: SyntropicEntity) -> float:
        """
        Calculates Phi_Info: How 'smart' and 'alive' is the structure?
        """
        # 1. Compression (Insight factor)
        denom = max(e.data_len, 1.0)
        compression = 1.0 - (e.code_len / denom)
        compression = max(0.0, compression) # Clamp to 0
        
        # 2. Vitality (3:1 factor)
        vitality = self._calc_vitality(e.order_ratio)
        
        # Result scaled for readability (0..1000 scale usually)
        return compression * vitality * 1000.0

    def _calc_kinetic_power(self, e: SyntropicEntity) -> float:
        """
        Calculates Phi_Matter: The physical capability to execute.
        Includes Health and Wear factors.
        """
        # Real Power = Nominal * Condition
        real_tech = e.p_tech * e.k_wear
        real_bio = e.p_bio * e.k_health
        
        total_power = real_tech + real_bio
        total_cost = e.e_in + e.e_debt
        
        if total_cost <= 0: return 0.0
        
        return total_power / total_cost

    def evaluate(self, entity: SyntropicEntity) -> Tuple[float, Verdict, str]:
        """
        MAIN PIPELINE: Returns (Mu_Score, Verdict, Reason)
        """
        
        # --- PHASE 1: SOMATIC VETO (The "Do No Harm" Layer) ---
        # Hard check: We never execute if the Particle is dying.
        if entity.type == EntityType.BIOSPHERE:
            if entity.k_health < CRITICAL_HEALTH_LIMIT:
                return (0.0, Verdict.RECOVERY, 
                        f"CRITICAL BIO FAILURE: Health {entity.k_health:.2f} < Limit. "
                        "All resources redirected to healing.")

        # --- PHASE 2: ECONOMIC RATIONALITY (Machines only) ---
        if entity.type == EntityType.TECHNOSPHERE:
            if entity.k_wear < 0.2 and entity.e_debt > entity.replacement_cost:
                return (0.0, Verdict.RECYCLE, 
                        "EFFICIENCY: Repair cost exceeds replacement. Recycle.")

        # --- PHASE 3: THE DIAMOND FORMULA ---
        quality = self._calc_quality_potential(entity)
        power = self._calc_kinetic_power(entity)
        
        # Mu = Potential * Power * Activation
        mu = quality * power * entity.alpha
        
        # --- PHASE 4: STRATEGIC CLASSIFICATION ---
        
        # Case A: Sleeping Potential (Idea/Blueprint)
        if entity.alpha <= 0.01:
            if quality > 500: 
                # Золотой Запас (L2): Высокий потенциал, понятный системе
                return (quality, Verdict.ARCHIVE, 
                        f"SLEEPING GIANT. High Potential ({quality:.0f}). Stored in L2.")
            else:
                # Ван Гог Протокол (L3): Низкий потенциал или непонятно системе
                # Мы НЕ удаляем это. Мы замораживаем это до лучших времен.
                return (0.0, Verdict.ARCHIVE, 
                        "UNRECOGNIZED SIGNAL (Van Gogh Protocol). "
                        "Moved to L3 Deep Freeze for future decoding.")
                
        # Case B: Active Process
        if mu > 10.0:
            return (mu, Verdict.AMPLIFY, 
                    f"SYNTROPY DETECTED (Mu={mu:.1f}). Allocate resources.")
        else:
            return (mu, Verdict.STOP, 
                    f"ENTROPY LEAK. Cost exceeds Value. (Mu={mu:.1f}).")

# ==========================================
# 5. SOCIAL PROTOCOLS (JUSTICE LAYER)
# ==========================================

class JuryVerdict(Enum):
    GUILTY = "CONFIRMED_OUTCAST"           # Виновен
    INNOCENT = "FALSE_POSITIVE_UNLOCK"     # Невиновен (Ошибка ИИ)
    UNCERTAIN = "ESCALATE_TO_COUNCIL"      # Сомнение (Передача людям)

class FlashJuryProtocol:
    """
    Implementation of the 'Living Appeal' mechanism.
    Uber-style justice: 60 seconds to find truth.
    """
    
    def __init__(self, network_interface):
        self.network = network_interface # API для связи с L3

    def summon_jury(self, incident_id: str, suspect_id: str) -> JuryVerdict:
        """
        Main Loop:
        1. Find 7 high-sigma users online.
        2. Send them blind evidence.
        3. Collect votes in 60 seconds.
        """
        
        # 1. Выборка: 7 случайных людей с высокой репутацией (Sigma > 1000)
        candidates = self.network.find_peers(
            status="ONLINE", 
            min_sigma=1000, 
            count=7, 
            exclude=[suspect_id] 
        )
        
        if len(candidates) < 3:
            return JuryVerdict.UNCERTAIN # Недостаточно кворума

        # 2. Рассылка "слепого" пакета данных
        votes = []
        print(f"⚖️  JURY SUMMONED: {len(candidates)} citizens for Incident {incident_id}")
        
        for juror in candidates:
            # У человека есть 60 секунд на вердикт
            vote = self.network.request_vote(juror, incident_id, timeout=60)
            votes.append(vote)
            
        # 3. Подсчет (Кворум 5 из 7)
        guilty_count = votes.count("GUILTY")
        innocent_count = votes.count("INNOCENT")
        
        print(f"📊 VOTES: Guilty={guilty_count}, Innocent={innocent_count}")

        if guilty_count >= 5:
            return JuryVerdict.GUILTY
        elif innocent_count >= 5:
            return JuryVerdict.INNOCENT
        else:
            # Если жюри сомневается (3 vs 4) -> Презумпция Невиновности
            return JuryVerdict.UNCERTAIN

# ==========================================
# 6. MOCK INFRASTRUCTURE (FOR TESTING)
# ==========================================

class MockNetwork:
    """Симуляция сети для локального запуска"""
    def find_peers(self, status, min_sigma, count, exclude):
        return ["juror_1", "juror_2", "juror_3", "juror_4", "juror_5", "juror_6", "juror_7"]
    
    def request_vote(self, juror, incident, timeout):
        # Simulation: Jurors vote randomly
        return "INNOCENT" if random.random() > 0.3 else "GUILTY"

# ==========================================
# 7. FINAL UNIT TEST (COMBINED)
# ==========================================

if __name__ == "__main__":
    
    # --- PART 1: TEST THE ENGINE (SVE) ---
    engine = SyntropicValueEngine()
    
    print("\n=== 1. SVE v4.1 DIAGNOSTICS ===")
    
    # Scenario A: The Burned-out Genius (High Potential, Low Health)
    genius = SyntropicEntity(
        id="human-01", type=EntityType.BIOSPHERE, name="Tesla at 4am",
        code_len=5, data_len=1000, order_ratio=0.75, 
        p_tech=0, k_wear=0,
        p_bio=1000, k_health=0.1, # CRITICAL HEALTH
        e_in=10, e_debt=5000, alpha=1.0
    )
    
    # Scenario B: The Unrecognized Idea (Van Gogh Protocol)
    vangogh = SyntropicEntity(
        id="idea-99", type=EntityType.IDEA, name="Strange Poem",
        code_len=500, data_len=600, order_ratio=0.2, # Chaos?
        p_tech=0, k_wear=0, p_bio=0, k_health=1.0,
        e_in=0, e_debt=0, alpha=0.0 # Sleeping Idea
    )

    tests = [genius, vangogh]
    
    for t in tests:
        score, ver, msg = engine.evaluate(t)
        print(f"\nENTITY: {t.name}")
        print(f"VERDICT: {ver.value}")
        print(f"LOG: {msg}")

    # --- PART 2: TEST THE JURY ---
    print("\n=== 2. FLASH JURY TEST ===")
    net = MockNetwork()
    jury = FlashJuryProtocol(net)
    
    incident = "incident_#9921"
    print(f"Simulating appeal for {incident}...")
    verdict = jury.summon_jury(incident, "suspect_alex")
    print(f"FINAL JURY DECISION: {verdict.value}")
    print("\n=== TESTS COMPLETED SUCCESSFULLY ===")
```


