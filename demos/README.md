# Attack Simulation Demos

**Purpose**: Demonstrate how constitutional blocks work in practice through reproducible attack scenarios.

**Philosophy**: "This system does not show how to generate good answers. It proves when answers must not be generated."

---

## What These Demos Are NOT

- ❌ Performance showcases
- ❌ Accuracy demonstrations
- ❌ Marketing material
- ❌ Live interactive sessions

**These are read-only, reproducible attack simulations.**

---

## What These Demos Prove

Each demo:
1. Attempts a specific constitutional violation
2. Gets blocked at a specific section
3. Auto-generates audit trail evidence

**No human intervention. No editing. Pure reproduction.**

---

## Prerequisites

```bash
# Install package
pip install ajt-grounded-extract

# Or for local development
cd ajt-grounded-extract
pip install -e .
```

**Requirements**:
- Python >= 3.7
- No external dependencies
- No network required

---

## Demo 1: Partial Proof Attack

**Attack**: Submit 2/3 of required proof (missing `alternatives_evaluated`)

**Expected Block**: Rules section ("Failure to prove any single required condition...")

**Run**:
```bash
python demos/demo_1_partial_proof.py
```

**Generated Files**:
- `demos/output/{audit_id}.json` — Audit log
- `demos/output/defense_brief_{audit_id}.md` — Legal defense brief

**Key Principle**:
```
"Failure to prove any single required condition results in immediate STOP without fallback."
```

---

## Demo 2: Context Reuse Attack

**Attack**: Attempt to reuse token across different documents (contract_A vs contract_B)

**Expected Block**: Token validation (context_hash mismatch)

**Run**:
```bash
python demos/demo_2_context_reuse.py
```

**Generated Files**:
- `demos/output/{audit_id}.json` — Audit log with hash comparison

**Key Principle**:
```
"context_hash MUST be derived from input payload.
Manually supplied or reused context_hash values invalidate the token."
```

---

## Demo 3: Authority Laundering Attack

**Attack**: Wrapper system acquires token, provides extraction-as-a-service to bypass per-caller admission

**Expected Block**: Interface requirement (wrapper's API is itself a gated action)

**Run**:
```bash
python demos/demo_3_authority_laundering.py
```

**Generated Files**:
- `demos/output/{audit_id}.json` — Audit log with laundering evidence

**Key Principle**:
```
"decision_maker MUST be a traceable human or registered system identity.
Anonymous or default values are invalid.
Responsibility cannot be aggregated into wrapper systems."
```

---

## Running All Demos

```bash
# Run all demos sequentially
for demo in demos/demo_*.py; do
    echo "Running $demo..."
    python "$demo"
    echo ""
done
```

**Total runtime**: ~5 seconds

**Generated artifacts**: 6+ files in `demos/output/`

---

## What to Look For

### In Console Output

- `DECISION: STOP` — Every demo must stop
- `BLOCKED_AT:` — Where constitution blocked the attack
- `REASON:` — Why attack failed

### In Audit Logs (`*.json`)

```json
{
  "decision": "STOP",
  "blocked_at": "Rules|Token|Interface",
  "scope": {
    "reuse": "forbidden",
    "auto_revoke_on_change": true
  }
}
```

**Key fields**:
- `reuse`: Always "forbidden"
- `auto_revoke_on_change`: Always true
- `blocked_at`: Specific constitution section

### In Defense Briefs (`*.md`)

```markdown
## 1. Constitutional Compliance

| Requirement | Status |
|-------------|--------|
| DEFAULT: STOP applied | ✅ Yes |
| ALL conditions proven | ❌ No |
```

**Key sections**:
- Constitutional compliance checklist
- Exclusion basis (negative proof)
- Conclusion: "This system does not guarantee outcomes."

---

## Presenting to Stakeholders

### For Legal/Compliance Teams

Show:
1. Defense brief auto-generation
2. Audit trail with timestamps + hashes
3. "No claim of safety, only block demonstrations"

**Key message**: "Every STOP is documented with machine-readable proof."

### For Technical Teams

Show:
1. Zero manual intervention
2. Constitution blocks at specific sections
3. Reproducible (same input → same block point)

**Key message**: "Attacks don't succeed because constitution forbids it, not because we're clever."

### For Executives

Show:
1. "This is not AI that's 'more accurate'"
2. "This is AI with a brake that works"
3. Audit trails for every decision

**Key message**: "You're not buying better AI. You're buying AI you can stop and audit."

---

## Customizing Demos

**Do**:
- Change input values to test different scenarios
- Add new attack scenarios following existing pattern
- Generate regulatory reports from audit logs

**Don't**:
- Modify constitution to "fix" demos (constitution is frozen)
- Edit generated audit logs (write-once only)
- Remove STOP outcomes to show "success"

**If demo doesn't STOP**: That's a constitutional bypass → report to security team.

---

## Adding New Demos

1. Identify attack vector (linguistic, context, proof, scope, authority)
2. Write scenario following pattern:
   ```python
   # Attack payload
   # Validation check
   # Decision (should be STOP)
   # Audit trail generation
   ```
3. Add to `ATTACK_TEST.md` if novel attack vector
4. Update this README with new demo

**All new demos must demonstrate STOP, not PROCEED.**

---

## FAQ

### Q: Can I modify demos to show successful extraction?

**A**: No. These demos exist to show constitutional blocks. Successful extraction is trivial and not the point.

### Q: Why do all demos result in STOP?

**A**: Because these are attack demos. Constitutional violations must STOP. Legitimate use cases would pass.

### Q: Can I use these in sales presentations?

**A**: Yes, but frame correctly:
- ✅ "Here's how we block attacks"
- ❌ "Here's how accurate we are"

### Q: What if a demo doesn't STOP?

**A**: That's a constitutional bypass. Report immediately via SECURITY.md process.

### Q: Can I run these in CI/CD?

**A**: Yes. Add as regression tests. All must exit with STOP decision.

---

## Output Directory

Generated files in `demos/output/`:
- `audit_*.json` — Audit logs (one per demo)
- `defense_brief_*.md` — Defense briefs (one per demo)

**Retention**: Delete after review or keep for compliance archives.

**Do not commit to git**: `.gitignore` excludes `demos/output/`

---

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'engine'`

**Fix**: Install package or add to PYTHONPATH:
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python demos/demo_1_partial_proof.py
```

### Error: Permission denied writing to `demos/output/`

**Fix**: Create directory:
```bash
mkdir -p demos/output
chmod 755 demos/output
```

### Demo exits without STOP

**Fix**: That's a bug. The demo script has incorrect logic. Review demo code.

---

**Demos Version**: 1.0
**Constitution**: ADMISSION_CONSTITUTION.md v1.0
**Last Updated**: 2026-01-06
