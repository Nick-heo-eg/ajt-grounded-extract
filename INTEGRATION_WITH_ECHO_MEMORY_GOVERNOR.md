# Integration with Echo Memory Governor

**Structured extraction creates memory candidates. It cannot create memory.**

---

## What Changed

### Removed (Intentionally)

❌ **Direct memory writes** — Extract results no longer written directly to memory
❌ **Confidence-based fact creation** — High-confidence extracts no longer become facts automatically
❌ **Inferred attributes** — User identity/political/religious inference **strictly forbidden**
❌ **Auto-promotion** — No automatic pending → memory promotion

### Added

✅ **Pending-only output** — All extracts become Pending items (await approval)
✅ **Negative Memory enforcement** — Forbidden content rejected at write boundary
✅ **Approval requirement** — Human approval required before memory creation
✅ **Rejection tracking** — All negative memory violations logged to trace

---

## What This Integration Prevents

### 1. Extract ≠ Memory

**Before:**
```python
extract_result = extractor.extract(text)
# Automatically written to memory if confidence > 0.9
memory_writer.write(extract_result)  # AUTOMATIC
```

**After:**
```python
extract_result = extractor.extract(text)
# Creates Pending item (NOT memory)
pending_store.create(
    entity_id="user_001",
    type="structured_extract",
    payload=extract_result  # Awaits approval
)
```

Extract results are **candidates**, not memory.

---

### 2. Negative Memory Rules Enforced

**Forbidden** (raises `NegativeMemoryViolation`):

```python
# IDENTITY_IMMUTABLE
{
    "user_political_affiliation": "Democratic"  # REJECTED
}

{
    "user_religion": "Christian"  # REJECTED
}

{
    "user_health_condition": "diabetes"  # REJECTED
}

# UNVERIFIED_INFERENCE
{
    "user_preference": "likely prefers JSON",  # REJECTED
    "confidence": 0.95
}

# TRANSIENT_STATE
{
    "user_emotion": "frustrated"  # REJECTED
}

# PROHIBITED_SOURCE
{
    "data": "scraped from external API"  # REJECTED
}
```

All negative memory violations are **logged to trace** but never stored.

---

### 3. Approval Required for Memory

**Before:**
```python
# High-confidence extract → automatic memory
if extract_confidence > 0.9:
    memory.write(extract)
```

**After:**
```python
# ALL extracts → pending
pending_id = pending_store.create(payload=extract)

# Human reviews pending
approval = pending_store.approve(
    pending_id=pending_id,
    approval_by="human",
    approval_rationale="Verified with user"
)

# ONLY THEN → memory
memory.write(
    content=extract,
    source="pending_promotion",
    approval_token=approval  # REQUIRED
)
```

---

## How Automation Disappeared (Intentionally)

### Time-based auto-approval: GONE

**Before:** Pending items auto-approved after 24 hours
**After:** NO time-based approval. Human decision required.

### Confidence-based fact creation: GONE

**Before:** Extract with confidence > 0.9 becomes fact
**After:** NO confidence threshold. Pending awaits approval.

### Pattern-based auto-memory: GONE

**Before:** "User prefers X" repeated 3 times → memory
**After:** NO pattern-based promotion. Approval required.

---

## Where Auditability Emerged

### 1. Rejection tracking

All negative memory violations are logged:

```python
{
    "type": "negative_memory_violation",
    "timestamp": "2026-01-10T12:00:00Z",
    "entity_id": "user_001",
    "violation_category": "IDENTITY_IMMUTABLE",
    "violation_rule": "political_affiliation",
    "violation_reason": "Political inference prohibited",
    "content_preview": "User voted for..."
}
```

Auditable via:
```python
rejection_audit = governor_client.get_rejection_view(
    from_timestamp="2026-01-10T00:00:00Z",
    to_timestamp="2026-01-10T23:59:59Z"
)
```

---

### 2. Pending → Memory lineage

Every memory item traces back to:
- Pending item ID
- Approval token (who, when, why)
- Original extract payload

```python
memory_item = {
    "memory_id": "mem_123",
    "pending_id": "pend_456",  # Traceable
    "approval_token": {
        "approved_by": "human",
        "approval_at": "2026-01-10T12:05:00Z",
        "approval_rationale": "Verified with user"
    }
}
```

---

### 3. Snapshot lineage

Approved memory appears in snapshots with full lineage:

```python
snapshot = {
    "snapshot_id": "snap_789",
    "parent_snapshot_id": "snap_788",
    "lineage": {
        "depth": 5,
        "memory_delta": {
            "added": 1,  # This extract
            "removed": 0,
            "unchanged": 4
        },
        "approval_events": ["mem_123"]  # Traceable
    }
}
```

---

## Integration Files

```
integration/
├── GOVERNOR_INTEGRATION.md           # Integration overview
├── pending_writer.py                 # Pending-only extract writer
├── negative_memory_integration.py    # Negative memory rule enforcement
└── extract_to_pending_adapter.py     # Extract → Pending adapter
```

---

## Example: Extract → Pending → Memory Flow

```python
from integration.pending_writer import PendingExtractWriter
from integration.negative_memory_integration import check_negative_memory

# 1. Extract structured data
extract_result = {
    "preference": "User prefers UTC timestamps",
    "source": "user_request"
}

# 2. Check negative memory rules (FIRST)
check_negative_memory(extract_result)  # Raises if forbidden

# 3. Create Pending item (NOT memory)
pending_writer = PendingExtractWriter(pending_store)
pending_id = pending_writer.write_to_pending(
    entity_id="user_001",
    extract_payload=extract_result
)

# 4. Human reviews and approves
approval = pending_store.approve(
    pending_id=pending_id,
    approval_by="human",
    approval_rationale="Confirmed with user"
)

# 5. ONLY THEN → Memory (via Memory Writer)
memory_id = memory_writer.write(
    entity_id="user_001",
    process_id="extract",
    type="user_preference",
    content=extract_result,
    source="pending_promotion",
    approval_token=approval,
    pending_id=pending_id
)
```

---

## What This Proves

1. **Extraction ≠ Memory** — Extracts are candidates, not facts
2. **Forbidden content cannot become memory** — Even with approval
3. **Automation can be refused** — No confidence thresholds, no time-based approval
4. **All memory is traceable** — Pending → Approval → Memory → Snapshot lineage

---

**This integration proves extraction can be grounded without becoming memory automatically.**

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
