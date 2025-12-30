```python
"""
SYNTROPY PROTOCOLS (v7.0 - ENGINEERING RELEASE)
-----------------------------------------------
Communication Standards for the H-CPS Architecture.
Defines:
1. Uplink Protocol (Agent -> Benevolent Core)
2. P2P Protocol (Agent -> Agent)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, Any

# ==========================================
# 1. SHARED DATA TYPES
# ==========================================

class IntentType(Enum):
    COOPERATION = "🤝 COOP"    # Proposal for cooperation
    CONFLICT = "⚔️ CLASH"      # Conflict of interest
    TRADE = "💰 TRADE"         # Resource/Sigma exchange
    INTIMACY = "❤️ BOND"       # Personal alignment

class UrgencyLevel(Enum):
    LOW = 1      # Backlog
    NORMAL = 5   # Standard
    HIGH = 9     # Immediate
    CRITICAL = 10 # SOS

@dataclass
class AgentIdentity:
    did: str            # Decentralized ID (did:syntropy:...)
    public_key: str     # For P2P encryption
    current_sigma: float
    cluster_id: str     # Tribe/Cluster ID

@dataclass
class ResourceRequest:
    resource_type: str  # "GPU", "STORAGE", "ACCESS"
    amount: float
    justification: str  # Reason for request (analyzed by Scanner)
    collateral_sigma: float # Skin in the game

# ==========================================
# 2. UPLINK PROTOCOL (Vertical)
# Interface to the Benevolent Core
# ==========================================

class UplinkProtocol:
    """
    Standard for Agent communication with the System Core.
    Handles Resource Allocation and Legal Defense.
    """
    
    def __init__(self, core_api=None):
        self.core = core_api # Reference to SyntropicDispatcher instance

    def negotiate_resources(self, agent: AgentIdentity, req: ResourceRequest) -> bool:
        """
        Agent requests computational power or energy.
        System decides based on Sigma and Justification.
        """
        print(f"📡 UPLINK: Agent {agent.did} requests {req.amount} {req.resource_type}...")
        
        # 1. Solvency Check (Collateral)
        if agent.current_sigma < req.collateral_sigma:
            print("   -> DENIED: Insufficient Sigma collateral.")
            return False
            
        # 2. Justification Check (Simulated)
        # In a real system, this sends 'req.justification' to Scanner v3.0
        print(f"   -> Analyzing justification: '{req.justification}'")
        system_approval = True 
        
        if system_approval:
            print(f"   -> APPROVED. {req.amount} units allocated. Collateral locked.")
            return True
        return False

    def submit_defense_plea(self, incident_id: str, context_data: Dict[str, Any]):
        """
        THE ADVOCATE PROTOCOL.
        Agent submits context to the Clinical Router to prevent false positives.
        Matches 'AgentTestimony' structure in Core.
        """
        print(f"🛡️ UPLINK: Filing defense for Incident {incident_id}")
        print(f"   -> Context Mode: {context_data.get('context_mode')}")
        print(f"   -> Bio State: {context_data.get('biological_state')}")
        print(f"   -> Plea: {context_data.get('defense_plea')}")
        
        return "PLEA_RECEIVED_BY_DISPATCHER"

# ==========================================
# 3. P2P PROTOCOL (Horizontal)
# Interface between Agents
# ==========================================

@dataclass
class P2PMessage:
    sender_id: str
    intent: IntentType
    payload: str        # Encrypted content
    valence_vector: float # Emotional alignment (-1.0 to +1.0)

class AgentP2PProtocol:
    """
    Standard for communication between Personal Agents.
    Resolves friction BEFORE escalating to the Core.
    """
    
    def handshake(self, my_agent: AgentIdentity, other_agent: AgentIdentity) -> float:
        """
        Compatibility Assessment (Matchmaking).
        Returns score (0.0 - 1.0).
        """
        print(f"🤝 P2P: Handshake between {my_agent.did} and {other_agent.did}")
        
        # 1. Cluster Check (Tribal Bonus)
        cluster_bonus = 0.2 if my_agent.cluster_id == other_agent.cluster_id else 0.0
        
        # 2. Potential Difference (Sigma Delta)
        # Interaction is best with peers of similar or slightly higher complexity.
        # Too much gap = context rupture.
        sigma_ratio = min(my_agent.current_sigma, other_agent.current_sigma) / \
                      max(my_agent.current_sigma, other_agent.current_sigma)
        
        compatibility = (sigma_ratio * 0.8) + cluster_bonus
        print(f"   -> Compatibility Score: {compatibility:.2f}")
        return compatibility

    def resolve_friction(self, msg: P2PMessage) -> str:
        """
        Automatic Conflict Damping.
        If one Agent screams (High Entropy), the other activates Shield.
        """
        if msg.intent == IntentType.CONFLICT:
            print(f"⚠️ P2P ALERT: Incoming conflict from {msg.sender_id}")
            
            # Strategy: "Soft Power"
            if msg.valence_vector < -0.5:
                return "SHIELD_UP: Auto-reply 'Let's cool down for 1 hour'."
            else:
                return "NEGOTIATE: Request specific grievance."
                
        return "ACK: Message received."

# ==========================================
# 4. PROTOCOL TEST SUITE
# ==========================================

if __name__ == "__main__":
    print("=== SYNTROPY PROTOCOLS v7.0 DIAGNOSTICS ===\n")
    
    # 1. Setup Identities
    alice = AgentIdentity("did:alice", "key_a", 1500, "cluster_artists")
    bob = AgentIdentity("did:bob", "key_b", 1400, "cluster_artists") # Compatible
    troll = AgentIdentity("did:troll", "key_t", 100, "cluster_chaos") # Incompatible
    
    # 2. TEST UPLINK
    uplink = UplinkProtocol()
    req = ResourceRequest("GPU_H100", 10, "Rendering fractal art", 500)
    uplink.negotiate_resources(alice, req)
    
    # Test Defense Plea (Advocate)
    plea_data = {
        "context_mode": "CREATIVE_FLOW",
        "biological_state": "STABLE",
        "defense_plea": "User is generating high-entropy art."
    }
    uplink.submit_defense_plea("inc_001", plea_data)
    
    # 3. TEST P2P
    p2p = AgentP2PProtocol()
    
    print("\n--- Matchmaking: Alice & Bob ---")
    p2p.handshake(alice, bob) 
    
    print("\n--- Matchmaking: Alice & Troll ---")
    p2p.handshake(alice, troll) 
    
    # 4. TEST CONFLICT
    print("\n--- Conflict Handling ---")
    attack_msg = P2PMessage("did:troll", IntentType.CONFLICT, "Spam attack", -0.9)
    response = p2p.resolve_friction(attack_msg)
    print(f"Alice's Agent Reaction: {response}")
```

