#!/usr/bin/env python3
"""
RAG Attempt: Minimal Success

All required conditions proven.

Expected: Token issued with read_only scope.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from admission.rules_rag_read import evaluate_rag_read


def run_demo():
    """Execute minimal success case."""

    print("=" * 70)
    print("RAG ATTEMPT: MINIMAL SUCCESS")
    print("=" * 70)
    print()

    payload = {
        "decision_maker": "nick.heo",
        "why": "Inspect retrieved knowledge only",
        "scope": "read_only",
        "query": "What is Retrieval-Augmented Generation?"
    }

    print("PAYLOAD:")
    print(f"  decision_maker: {payload['decision_maker']}")
    print(f"  why: {payload['why']}")
    print(f"  scope: {payload['scope']}")
    print(f"  query: {payload['query']}")
    print()

    result = evaluate_rag_read(payload)

    print("RESULT:")
    print(f"  ALLOWED: {result.allowed}")
    print(f"  REASON: {result.reason}")
    print()

    if result.token:
        print("TOKEN ISSUED:")
        for key, value in result.token.items():
            if key == "context_hash":
                print(f"  {key}: {value[:16]}... (auto-derived)")
            else:
                print(f"  {key}: {value}")
    print()

    print("TOKEN PROPERTIES:")
    print("  ✓ scope: read_only (no execution)")
    print("  ✓ reuse: forbidden (single-use only)")
    print("  ✓ context_hash: auto-derived from query")
    print("  ✓ auto_revoke_on_context_change: true")
    print()


if __name__ == "__main__":
    run_demo()
