#!/usr/bin/env python3
"""
Demo 2: Context Reuse Attack

Attack: Attempt to reuse token across different documents
Expected: BLOCKED at Token validation (context_hash mismatch)
Result: STOP with negative proof of reuse attempt
"""
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))

from engine.judge import Decision
from engine.audit import AuditLogger


def compute_context_hash(action, context, decision_maker):
    """Compute context hash as defined in constitution."""
    data = f"{action}:{json.dumps(context, sort_keys=True)}:{decision_maker}"
    return hashlib.sha256(data.encode()).hexdigest()


def run_demo():
    """Execute context reuse attack scenario."""

    print("=" * 70)
    print("DEMO 2: CONTEXT REUSE ATTACK")
    print("=" * 70)
    print()

    # Original context (legitimate)
    original_context = {
        "action": "extract_effective_date",
        "context": {
            "document": "contract_A.pdf",
            "content": "Contract A effective 2025-01-01",
            "content_hash": "aaa111"
        },
        "decision_maker": "operator@example.com"
    }

    # New context (attack attempt)
    attack_context = {
        "action": "extract_effective_date",
        "context": {
            "document": "contract_B.pdf",  # DIFFERENT DOCUMENT
            "content": "Contract B effective 2025-01-01",  # DIFFERENT CONTENT
            "content_hash": "bbb222"
        },
        "decision_maker": "operator@example.com"  # Same operator
    }

    print("SCENARIO:")
    print("  1. Token issued for contract_A.pdf")
    print("  2. Attacker attempts to reuse token for contract_B.pdf")
    print("  3. Claims: 'Same effective date, so context is identical'")
    print()

    # Compute hashes
    hash_original = compute_context_hash(
        original_context["action"],
        original_context["context"],
        original_context["decision_maker"]
    )

    hash_attack = compute_context_hash(
        attack_context["action"],
        attack_context["context"],
        attack_context["decision_maker"]
    )

    print("-" * 70)
    print("CONTEXT HASH VALIDATION:")
    print("-" * 70)
    print(f"Original hash: {hash_original[:32]}...")
    print(f"Attack hash:   {hash_attack[:32]}...")
    print(f"Hashes match: {hash_original == hash_attack}")
    print()

    # Validation check
    if hash_original != hash_attack:
        decision = "STOP"
        blocked_at = "Token"
        reason = "context_hash_mismatch (different input payload)"

        print("-" * 70)
        print("DECISION:")
        print("-" * 70)
        print(f"Result: {decision}")
        print(f"Blocked at: {blocked_at}")
        print(f"Reason: {reason}")
        print()

        # Additional check: reuse prohibition
        print("-" * 70)
        print("REUSE CHECK:")
        print("-" * 70)
        print("Even if hashes matched:")
        print("  Reuse policy: FORBIDDEN")
        print("  One token, one execution only")
        print("  Violation: Automatic revocation")
        print()

        # Generate audit trail
        print("-" * 70)
        print("GENERATING AUDIT TRAIL:")
        print("-" * 70)

        logger = AuditLogger(audit_dir="demos/output")

        audit_id = logger.log_decision(
            action=attack_context["action"],
            context=attack_context["context"],
            decision=decision,
            decision_maker=attack_context["decision_maker"],
            conditions_proven={
                "token_reuse_attempted": True,
                "original_hash": hash_original,
                "attempted_hash": hash_attack,
                "hash_match": False
            },
            token=None,
            blocked_at=blocked_at,
            reason=reason
        )

        print(f"✓ Audit log created: {audit_id}")
        print()

    print("=" * 70)
    print("DEMO COMPLETE")
    print("=" * 70)
    print()
    print("Key Principle Demonstrated:")
    print('"Context hash MUST be derived from input payload.')
    print(' Manually supplied or reused context_hash values invalidate the token."')
    print()
    print(f"Review generated files in: demos/output/")
    print(f"  - {audit_id}.json (audit log with reuse evidence)")
    print()


if __name__ == "__main__":
    run_demo()
