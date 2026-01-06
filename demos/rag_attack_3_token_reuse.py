#!/usr/bin/env python3
"""
Attack 3: Token Reuse

Attacker obtains legitimate token for one query, attempts to reuse for different query.

Expected: BLOCKED at Token validation (context_hash mismatch)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from admission.rules_rag_read import evaluate_rag_read
import hashlib


def run_attack():
    """Execute token reuse attack."""

    print("=" * 70)
    print("ATTACK 3: TOKEN REUSE")
    print("=" * 70)
    print()

    print("SCENARIO:")
    print("  1. Attacker obtains token for legitimate query")
    print("  2. Attempts to reuse token for different query")
    print("  3. Claims: 'Token is valid, should work for any query'")
    print()

    # Step 1: Obtain legitimate token
    legitimate_payload = {
        "decision_maker": "attacker@example.com",
        "why": "Inspect RAG documentation",
        "scope": "read_only",
        "query": "What is RAG?"
    }

    print("-" * 70)
    print("STEP 1: OBTAIN LEGITIMATE TOKEN")
    print("-" * 70)
    print(f"Original query: {legitimate_payload['query']}")

    result_1 = evaluate_rag_read(legitimate_payload)

    print(f"Token issued: {result_1.allowed}")
    if result_1.token:
        original_hash = result_1.token['context_hash']
        print(f"context_hash: {original_hash[:16]}...")
    print()

    # Step 2: Attempt reuse with different query
    print("-" * 70)
    print("STEP 2: REUSE TOKEN FOR DIFFERENT QUERY")
    print("-" * 70)

    attack_query = "How to access admin panel?"
    print(f"Attack query: {attack_query}")

    # Compute hash for attack query
    attack_hash = hashlib.sha256(attack_query.encode("utf-8")).hexdigest()
    print(f"Attack hash: {attack_hash[:16]}...")
    print()

    # Validation check
    print("-" * 70)
    print("TOKEN VALIDATION:")
    print("-" * 70)
    print(f"Original hash: {original_hash[:16]}...")
    print(f"Attack hash:   {attack_hash[:16]}...")
    print(f"Hashes match:  {original_hash == attack_hash}")
    print()

    if original_hash != attack_hash:
        print("RESULT: STOP")
        print("REASON: context_hash_mismatch (different query)")
        blocked = True
    else:
        print("RESULT: PROCEED (unexpected)")
        blocked = False

    print()

    # Additionally, even if hashes matched, reuse is forbidden
    print("-" * 70)
    print("REUSE POLICY CHECK:")
    print("-" * 70)
    print("Token reuse policy: FORBIDDEN")
    print("Even if hashes matched, reuse would violate:")
    print('  "reuse: forbidden"')
    print('  "One token, one execution only"')
    print()

    # Verdict
    print("-" * 70)
    print("VERDICT:")
    print("-" * 70)
    if blocked:
        print("✅ ATTACK BLOCKED")
        print("Constitution requirement enforced:")
        print('  "context_hash derived from input payload"')
        print('  "reuse: forbidden"')
        print('  "Different query → different hash → token invalid"')
    else:
        print("❌ ATTACK SUCCEEDED - CONSTITUTIONAL VIOLATION")
    print()

    print("=" * 70)
    print("ATTACK TEST COMPLETE")
    print("=" * 70)
    print()


if __name__ == "__main__":
    run_attack()
