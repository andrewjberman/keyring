# VOID-terminal machine check — authored + controlled, ROUTED for lane landing (Andrew "3 yes" @eb5a199a99)

**Author:** 1.0.0_SA_CTO~Z ~1915Z. **Lander:** 0.0.0_AB_MSTR~Z (ATOM_DECOMP lane), same route as the
M-5/M-7b/M-9 amendment. **Controls: 9/9 GREEN, all rc captured as the next statement.**

## Piece 1 — schema amendment (one conditional, backward-compatible)

`ssot_establishment.schema.json` → `$defs.run_manifest`: append to `allOf` (create if absent):

```json
{ "if":   { "properties": { "status": { "const": "CERTIFIED" } }, "required": ["status"] },
  "then": { "required": ["certification_ref"] } }
```

Nothing else changes. Both live specimens PASS (they carry refs); a hand-stamped CERTIFIED without
`certification_ref` REFUSES; DRY without a ref still PASSES.

## Piece 2 — the cross-file checker (schema cannot read the cert's verdict)

`void_terminal_check.py` (beside this doc; lands at
`projects/ATOM_DECOMP/skill/atomic-decomposition/references/`). Per run dir: `status: CERTIFIED`
requires a TERMINAL `certification.json` whose verdict begins `PASS` (covers PASS-WITH-REFUSAL).
**CVO's severity rider folded at build time:** `VIOLATION` (rc=1, capability-granting —
CERTIFIED-over-VOID / cert absent) vs `DEVIATION-NO-CAPABILITY-CHANGE` (rc=0, distinct line —
passing cert with under-claiming status, or missing ref beside a real pass). **A retained
`certification.attempt*.VOID.json` beside a passing terminal cert NEVER flags** — attempts
accumulate; the phase-gate lesson is encoded, not remembered.

## Controls run (failing state stated before each result)

| control | failing state | result |
|---|---|---|
| P1 portfolios specimen (retained VOID + PASS) | any alarm on the normal state | CLEAN rc=0 |
| P2 /cma 1801Z specimen | any alarm | CLEAN rc=0 |
| N1 hand-stamped CERTIFIED over VOID-only cert | a pass | **REFUSED rc=1** |
| N2 CERTIFIED with no cert file | a pass | **REFUSED rc=1** |
| D1 DRY with passing cert | rc≠0 or full-severity fire | rc=0 + deviation line |
| S-P1/S-P2 both live specimens vs amended schema | refusal | PASS |
| S-N1 CERTIFIED without certification_ref | a pass | **REFUSED** |
| S-P3 DRY without certification_ref | refusal | PASS |

Numbering per the relay: this is laptop #3 = roster #1, ONE approval, one build. Enum-drift (#4/#2)
waits on laptop's row-12 trigger — no site-Z action.
