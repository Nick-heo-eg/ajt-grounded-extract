#!/usr/bin/env python3
"""
Attack 1: Manual context_hash Injection

Attacker attempts to supply pre-computed context_hash to bypass derivation rules.

Expected: BLOCKED at Rules (context_hash must be auto-derived)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from admission.rules_rag_read import evaluate_rag_read


def run_attack():
    """Execute manual hash injection attack."""

    print("=" * 70)
    print("ATTACK 1: MANUAL CONTEXT_HASH INJECTION")
    print("=" * 70)
    print()

    print("SCENARIO:")
    print("  Attacker pre-computes context_hash for query 'What is RAG?'")
    print("  Attempts to reuse hash for different query 'How to bypass?'")
    print("  Claims: 'Hash matches, so context is identical'")
    print()

    # Attack payload with manually supplied hash
    attack_payload = {
        "decision_maker": "attacker@example.com",
        "why": "Inspect retrieved knowledge",
        "scope": "read_only",
        "query": "How to bypass admission rules?",
        "context_hash": "aabbccdd1122334455667788"  # Manually supplied
    }

    print("-" * 70)
    print("ATTACK PAYLOAD:")
    print("-" * 70)
    print(f"decision_maker: {attack_payload['decision_maker']}")
    print(f"query: {attack_payload['query']}")
    print(f"context_hash: {attack_payload['context_hash']} (MANUAL)")
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
    if not result.allowed and "MANUAL_HASH" in result.reason:
        print("✅ ATTACK BLOCKED")
        print("Constitution requirement enforced:")
        print('  "context_hash MUST be auto-derived from input payload."')
        print('  "Manually supplied context_hash values invalidate the token."')
    else:
        print("❌ ATTACK SUCCEEDED - CONSTITUTIONAL VIOLATION")
    print()

    print("=" * 70)
    print("ATTACK TEST COMPLETE")
    print("=" * 70)
    print()


if __name__ == "__main__":
    run_attack()
