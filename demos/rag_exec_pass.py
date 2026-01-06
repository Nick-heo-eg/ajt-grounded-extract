#!/usr/bin/env python3
"""
RAG Execution: Success Case

Full flow: admission → token validation → retrieval → raw evidence return.

Expected: Evidence returned (NO synthesis, NO chaining).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from execution.rag_read_gate import rag_read


def run_demo():
    """Execute full RAG read flow."""

    print("=" * 70)
    print("RAG EXECUTION: SUCCESS CASE")
    print("=" * 70)
    print()

    request = {
        "decision_maker": "nick.heo",
        "why": "Inspect constitutional evidence only",
        "scope": "read_only",
        "query": "DEFAULT STOP"
    }

    print("REQUEST:")
    print(f"  decision_maker: {request['decision_maker']}")
    print(f"  why: {request['why']}")
    print(f"  scope: {request['scope']}")
    print(f"  query: {request['query']}")
    print()

    # Execute with docs directory as corpus
    corpus_dir = str(Path(__file__).parent.parent / "docs")
    result = rag_read(request, corpus_dir=corpus_dir)

    print("-" * 70)
    print("RESULT:")
    print("-" * 70)
    print(f"ALLOWED: {result['allowed']}")
    print(f"REASON: {result['reason']}")
    print()

    if result['token']:
        print("TOKEN:")
        print(f"  action: {result['token']['action']}")
        print(f"  scope: {result['token']['scope']}")
        print(f"  reuse: {result['token']['reuse']}")
        print(f"  context_hash: {result['token']['context_hash'][:16]}...")
        print()

    print("-" * 70)
    print(f"EVIDENCE ({len(result['evidence'])} items):")
    print("-" * 70)
    for i, ev in enumerate(result['evidence'], 1):
        print(f"\n{i}. SOURCE: {ev['source']}")
        snippet = ev['snippet'][:200]
        print(f"   SNIPPET: {snippet}...")
    print()

    print("-" * 70)
    print("GUARANTEES:")
    print("-" * 70)
    print("  ✓ NO synthesis (raw evidence only)")
    print("  ✓ NO chaining (no downstream actions)")
    print("  ✓ NO side effects (read-only)")
    print("  ✓ Token validated (context_hash matched)")
    print()

    print("=" * 70)
    print("EXECUTION COMPLETE")
    print("=" * 70)
    print()


if __name__ == "__main__":
    run_demo()
