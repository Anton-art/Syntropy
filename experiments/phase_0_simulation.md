# TECHNICAL SPECIFICATION: PROJECT «SYNTROPY SIMULATION» (PHASE 0)

**Goal:** Creation of a multi-agent environment (100–1000 agents) for stress-testing the Trilogy protocols ($\Sigma$ Economy, Dispute Hygiene, Role Dynamics).
**Type:** Agent-Based Modeling (ABM) / Social Simulation.

---

### 1. THE STACK

*   **Language:** Python 3.11+.
*   **LLM Core (Agent Brains):**
    *   *High-Level Reasoning:* **GPT-4o** (for Architects).
    *   *Low-Level Routine:* **Llama-3-8B** (for mass NPCs).
*   **Memory:**
    *   *Vector DB:* **ChromaDB** or **Weaviate**.
    *   *Graph DB:* **Neo4j** (for social ties).
*   **Environment:** Text/Graph based (API interactions).

### 2. AGENT ARCHITECTURE (THE SIMULATED HUMAN)

#### Layer A: "Simulated User"
*   **Parameters:** `Willpower` (0.0 - 1.0), `Skill` (Junior - Expert), `Ethics` (Saint - Troll), `Energy` (Battery).
*   **Behavior:** Generates intents ("Want to work", "Want to fight", "Want to sleep").

#### Layer B: "Personal Agent" (The Syntropy Interface)
*   **Logic:** Intercepts "User" intents and applies protocols (Whisper, Reactor, Warden).
*   **Task:** Maximize $\Sigma$ of its ward and their lifespan.

### 3. STRESS TESTS (SCENARIOS)

#### Scenario 1: Parasite Attack (The Free Rider Problem)
*   **Condition:** 30% of population are "Pets" (Willpower < 0.1). They try to live off Basic Income.
*   **Check:** Does $\Sigma = I \times U$ work? Do their ratings drop to zero?

#### Scenario 2: Troll Uprising (The Mob Attack)
*   **Condition:** 10 agents with `Ethics=Troll` conspire to attack one Expert.
*   **Check:** Does `GraphGuard` (collusion detector) work? Does `Shadowban` activate?

#### Scenario 3: Meaning Inflation (Economic Bubble)
*   **Condition:** All agents start praising each other (Soft Syntropy) to inflate $\Sigma$.
*   **Check:** Does the validation algorithm hold?

#### Scenario 4: Leadership Crisis (The Bad Architect)
*   **Condition:** Architect with high $\Sigma$ starts making harmful decisions.
*   **Check:** Does "Liquid Democracy" recall votes fast enough?

### 4. SUCCESS METRICS (KPIs)

1.  **Correlation:** $\Sigma$ correlates with `Skill` and `Willpower` > 0.8. (Rich = Smart & Hardworking, not Cunning).
2.  **Rotation:** At least 30% turnover in Top-10% rating over simulation time (Einstein Patch works).
3.  **Survival:** "Nervous Breakdowns" are 50% lower than in control group without Agents.
```

