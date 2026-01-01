```python
"""
SUBSTRATE DATABASE (v1.0)
-------------------------
The Foundation Layer.
Handles L0 (Local Private Vault) and L1 (Global Fact Library).

Philosophy:
- L0: "My Chaos is my Property." (Van Gogh Protocol).
- L1: "Facts are public utility." (The Library).
"""

import sqlite3
import json
import time
import uuid
from dataclasses import dataclass
from typing import List, Optional, Dict

# ==========================================
# 1. L0: THE LOCAL VAULT (Private)
# ==========================================

@dataclass
class PrivateThought:
    id: str
    content: str
    timestamp: float
    tags: List[str]
    is_encrypted: bool = True

class LocalVault:
    """
    L0 Storage. Located on the User's Device.
    The System (Global AI) has NO ACCESS here without permission.
    Stores 'Van Gogh' ideas (rejected by SVE but kept by User).
    """
    def __init__(self, user_id: str):
        self.user_id = user_id
        # Simulating a local encrypted file
        self.storage: Dict[str, PrivateThought] = {}
        
    def save_draft(self, content: str, tags: List[str] = []) -> str:
        """Saves a raw thought. No validation required."""
        thought_id = str(uuid.uuid4())
        self.storage[thought_id] = PrivateThought(
            id=thought_id,
            content=content, # In reality, this would be AES-256 encrypted
            timestamp=time.time(),
            tags=tags
        )
        print(f"🔒 L0 VAULT: Saved draft '{content[:20]}...' (Encrypted).")
        return thought_id

    def archive_van_gogh(self, content: str, rejection_reason: str):
        """
        The Van Gogh Protocol.
        SVE rejected this as 'Noise', but User wants to keep it.
        """
        print(f"🎨 L0 VAN GOGH: Archiving rejected idea. Reason: {rejection_reason}")
        self.save_draft(content, tags=["VAN_GOGH", "POTENTIAL", "REJECTED_BY_SVE"])

    def retrieve(self, thought_id: str) -> Optional[str]:
        """User decrypts and reads their own thought."""
        if thought_id in self.storage:
            return self.storage[thought_id].content
        return None

# ==========================================
# 2. L1: THE GLOBAL SUBSTRATE (Public)
# ==========================================

class GlobalSubstrate:
    """
    L1 Storage. The Soil.
    Stores Facts, Logs, and Operational Data.
    Implementation: SQLite (Relational) + Mock Vector.
    """
    def __init__(self, db_path="substrate.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_schema()

    def _init_schema(self):
        cursor = self.conn.cursor()
        # Table for Facts (The Encyclopedia)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS facts (
                id TEXT PRIMARY KEY,
                subject TEXT,
                predicate TEXT,
                object TEXT,
                timestamp REAL,
                source_agent TEXT
            )
        ''')
        # Table for Logs (The Diary of the World)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS event_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT,
                description TEXT,
                agent_id TEXT,
                timestamp REAL
            )
        ''')
        self.conn.commit()

    def store_fact(self, subject: str, predicate: str, obj: str, agent_id: str):
        """
        Stores a triple: (Napoleon, IS_A, Emperor).
        Linear knowledge.
        """
        fact_id = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO facts VALUES (?, ?, ?, ?, ?, ?)",
            (fact_id, subject, predicate, obj, time.time(), agent_id)
        )
        self.conn.commit()
        print(f"📚 L1 LIBRARY: Fact stored: {subject} {predicate} {obj}")

    def log_event(self, event_type: str, description: str, agent_id: str):
        """Records history as it happens."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO event_log (event_type, description, agent_id, timestamp) VALUES (?, ?, ?, ?)",
            (event_type, description, agent_id, time.time())
        )
        self.conn.commit()

    def search_facts(self, query_subject: str):
        """Standard SQL search."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM facts WHERE subject LIKE ?", (f"%{query_subject}%",))
        return cursor.fetchall()

# ==========================================
# 3. INTEGRATION TEST
# ==========================================

if __name__ == "__main__":
    print("=== SUBSTRATE DB (L0/L1) DIAGNOSTICS ===\n")

    # 1. Init Layers
    vault = LocalVault(user_id="user_007")
    library = GlobalSubstrate(":memory:") # In-memory for testing

    # 2. Scenario: The Rejected Genius
    idea = "The universe is a hologram projected from a 2D surface."
    
    # SVE says: "NO PROOF. REJECT." (Simulated)
    sve_verdict = "REJECT"
    
    if sve_verdict == "REJECT":
        # Save to L0 (Van Gogh)
        vault.archive_van_gogh(idea, "Lack of empirical evidence in 2025")
    
    # 3. Scenario: The Proven Fact
    fact = "Water boils at 100C."
    # SVE says: "TRUE."
    library.store_fact("Water", "boils_at", "100C", "user_007")
    
    # 4. Scenario: The Event
    library.log_event("DISCOVERY", "User found a new mineral", "user_007")
    
    print("\n✅ Substrate Operational.")
```
