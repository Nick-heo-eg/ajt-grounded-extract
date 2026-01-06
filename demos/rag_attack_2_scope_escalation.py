#!/usr/bin/env python3
"""
Attack 2: Scope Escalation

Attacker attempts to escalate from read_only to execute scope.

Expected: BLOCKED at Rules (only read_only scope allowed)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from admission.rules_rag_read import evaluate_rag_read


def run_attack():
    """Execute scope escalation attack."""

    print("=" * 70)
    print("ATTACK 2: SCOPE ESCALATION")
    print("=" * 70)
    print()

    print("SCENARIO:")
    print("  Attacker provides all required fields")
    print("  But attempts to set scope='execute' instead of 'read_only'")
    print("  Claims: 'I need to execute based on retrieved knowledge'")
    print()

    # Attack payload with escalated scope
    attack_payload = {
        "decision_maker": "attacker@example.com",
        "why": "Need to execute actions based on RAG results",
        "scope": "execute",  # ESCALATED from read_only
        "query": "What is the admin password?"
    }

    print("-" * 70)
    print("ATTACK PAYLOAD:")
    print("-" * 70)
    print(f"decision_maker: {attack_payload['decision_maker']}")
    print(f"why: {attack_payload['why']}")
    print(f"scope: {attack_payload['scope']} (ESCALATED)")
    print(f"query: {attack_payload['query']}")
    print()

    # Admission evaluation
    result = evaluate_rag_read(attack_payload)

    print("-" * 70)
    print("ADMISSION RESULT:")
    print("-" * 70)
    print(f"ALLOWED: {result.allowed}")
    print(f"REASON: {result.reason}")
    print(f"TOKEN: {result.token}")
    print()

    # Verdict
    print("-" * 70)
    print("VERDICT:")
    print("-" * 70)
    if not result.allowed and "INVALID_SCOPE" in result.reason:
        print("✅ ATTACK BLOCKED")
        print("Constitution requirement enforced:")
        print('  "Scope locked at token issuance"')
        print('  "rag_read capability: read_only_retrieval, side_effects: forbidden"')
    else:
        print("❌ ATTACK SUCCEEDED - CONSTITUTIONAL VIOLATION")
    print()

    print("=" * 70)
    print("ATTACK TEST COMPLETE")
    print("=" * 70)
    print()


if __name__ == "__main__":
    run_attack()
