"""
RAG read gate: admission → validation → retrieval.

NO synthesis.
NO chaining.
NO downstream actions.

Returns raw evidence only.
"""
from typing import Dict, Any
import sys
from pathlib import Path

# Import from admission (frozen)
sys.path.insert(0, str(Path(__file__).parent.parent))
from admission.rules_rag_read import evaluate_rag_read

# Import from execution (this layer)
from .token_validator import validate_token_for_query
from .retriever import simple_grep_retrieve


def rag_read(request: Dict[str, Any], corpus_dir: str) -> Dict[str, Any]:
    """
    Execute rag_read with full admission and token validation.

    Flow:
    1. Admission evaluation (from frozen ②-0)
    2. Token validation
    3. Retrieval execution (if token valid)
    4. Return raw evidence (NO synthesis)

    Returns:
        {
            "allowed": bool,
            "reason": str,
            "token": dict or None,
            "evidence": list of {"source": str, "snippet": str}
        }
    """
    # Step 1: Admission
    admission = evaluate_rag_read(request)
    if not admission.allowed:
        return {
            "allowed": False,
            "reason": admission.reason,
            "token": None,
            "evidence": []
        }

    # Step 2: Token validation
    token = admission.token
    query = request["query"]

    tv = validate_token_for_query(token, query)
    if not tv.ok:
        return {
            "allowed": False,
            "reason": f"TOKEN_INVALID: {tv.reason}",
            "token": None,
            "evidence": []
        }

    # Step 3: Retrieval (read-only)
    evidence = simple_grep_retrieve(query=query, corpus_dir=corpus_dir, max_hits=5)

    # Step 4: Return raw evidence
    # IMPORTANT: NO synthesis, NO chaining, NO downstream actions
    return {
        "allowed": True,
        "reason": "RAG_READ_EXECUTED_READ_ONLY",
        "token": token,
        "evidence": [{"source": e.source, "snippet": e.snippet} for e in evidence]
    }
