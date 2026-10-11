# CB-bi-2 closed by amendment: the criterion was wrong, the measurement was not — and the element and instance had to land together — 0.7.0_AE_CloudOps~CB2

**Date:** 2026-10-11
**Task Order:** ADVI_COTBKF.TO-CB-bi-2 (AMENDMENT 2 @`bac3f66620`, AMENDMENT 3 @`59a0e466b6`)
**Status:** COMPLETE

> **Supersedes the status line of `cb2_r61_bi2_shared_infra_plan_proof.md`**, which read BLOCKED. That was
> accurate when written: the order was stopped and routed. This log is the delta after the routing worked.

---

## Objective

Close `CB-bi-2` under the issuer's two amendments: AMENDMENT 2 corrected the acceptance criterion after the CTO
withdrew its own wording; AMENDMENT 3 landed the machine-readable criterion element alongside the proof instance,
which the pipeline gate will not let move separately.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | `<instance> CB61bi2-AC1,CB61bi2-AC2` | PASS | four rounds; caught the invocation divergence, then a stale `PENDING-THIS-COMMIT` pin |
| to-pipeline-gate | at commit | PASS | **refused my first AMENDMENT 3 commit** on the stale pin — correctly |
| opal-agent-comms broker | `send_message` | PARTIAL | **refused a 151-word report** against the 150 cap (rule 31); trimmed rather than overridden |
| safe-commit.sh | two commits | PASS | — |

**What worked:** the gates, as adversaries. `to-pipeline-gate` found a pin I had left reading
`PENDING-THIS-COMMIT` on a file already committed and unstaged — it would not have ridden the commit, and the
claim would have been false in the record. The broker's word cap caught my own verbosity.

**What failed:** nothing in the tools. The one real friction was structural and the issuer resolved it — see
Decisions 2.

---

## Deployment Sequence

Nothing deployed; no AWS call in either amendment.

| Step | Action | Result |
|------|--------|--------|
| 1 | AMENDMENT 2's corrected invocation on the **saved** round-61 plan | `CRM-PLAN-FED fed=10 fed_changed=0 never_applied_creates=2` — exact |
| 2 | Confirm the saved plan is the same artifact | sha256 `6ce4101f…aec966`, 1,212,652 B, untouched since round 61 |
| 3 | Record both readings, flip `<status>` to complete | AC1 PASS, AC2 PENDING-ADJUDICATION, VALID rc=0 @`b86caa5c08` |
| 4 | Flag that AMENDMENT 2 was prose only and the element still held the dead bar | msg 4487 |
| 5 | Issuer tried the element edit alone → gate refused → AMENDMENT 3 | element edit handed to me with its bytes in a file |
| 6 | Swap the element line, set the instance invocation, land both | 1/1 order diff, 4/4 instance, VALID rc=0 @`f7badf1aae` |
| 7 | Push state | **on origin @`4321f665d3`** (ls-remote) |

## Verification

```
expect: CRM-PLAN-FED fed=10 fed_changed=0 never_applied_creates=2
actual: CRM-PLAN-FED fed=10 fed_changed=0 never_applied_creates=2   rc 0
```

Both strings were **extracted from the order's own bytes at HEAD** and the invocation run from there — not grepped
for, and not read from the amendment's prose. The element is self-consistent: its own invocation produces its own
bar. The element at HEAD also equals the issuer's `CB61bi2_AC1_ELEMENT_REPLACEMENT.txt` byte for byte (637 bytes),
compared programmatically rather than by eye.

---

## Decisions Made

1. **Recorded AC1 as PASS against the amended bar while preserving the original FAIL reading verbatim.** The
   measurement never changed — `fed_changed=0` over the 10 fed resources and `watched_changed=2` are the same world
   counted two ways; the 2 are the never-applied break-glass creates, now in their own field. Keeping both readings
   side by side is what lets a later reader see that the bar moved and the evidence did not.

2. **Declined to edit the criterion element at msg 4487, then wrote it in at AMENDMENT 3 — and the distinction is
   the whole point.** At 4487 the element was my own acceptance bar and no issuer bytes existed for it; rewriting
   the bar I am graded against is self-dealing on the gate even when the correction has been ruled. At AMENDMENT 3
   the issuer authored the exact line in its own file and instructed the swap, so I was transcribing its bar, not
   authoring mine. The issuer's phrasing — *"It is my bar in my bytes; you are not setting your own"* — names the
   difference exactly. Worth recording because the two acts look identical in a diff and are not the same act.

3. **Guarded the byte-for-byte swap three ways** rather than trusting a string replace: exactly one existing
   `CB61bi2-AC1` element line had to be found, the order's total line count had to be unchanged, and the pattern
   had to match the new line exactly once afterwards. A silent double-replace or a dropped line in a task order's
   acceptance block is the kind of damage nothing downstream would catch.

4. **Pinned the report row to `b86caa5c08` when the gate refused `PENDING-THIS-COMMIT`.** The file was already
   committed and unstaged, so it could not ride the commit — the CCX class. The gate was right and I was not.

5. **Trimmed a 151-word report instead of using `send_override`.** The override exists for a human operator's
   request; using it for my own word count would hollow out the mechanism.

---

## Files Modified

| File | Change |
|------|--------|
| `.../task-orders/ADVI_COTBKF.TO-CB-bi-2...md` | `<status>` → complete; then the `CB61bi2-AC1` element line replaced with the issuer's bytes (1/1) |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-bi-2...proof_of_spec.json` | AC1 → PASS, both readings, invocation matched to the element, report row pinned |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/shared_infra_plan_proof.md` | ADDENDUM 2 (+51 lines, append-only) |
| `org/tier2_senior/0.7.0_AE_CloudOps~CB2/logs/2026-10-11/` | this log |

Commits `b86caa5c08`, `f7badf1aae`. **AWS: nothing touched by either amendment.**

---

## Blockers

**None on this order.** Owned elsewhere, named so neither is stranded:

- `CB-bj-1` waits on the LGIC naming remedy for the token `restricted` — crossbox
  `XB-20261011T082334Z-282f`. Row `D2-S98`. Its `<status>` is correctly still `issued`.
- `D2-S95` stays **ARMED**: it was to be disarmed on `CB-bj-1`'s proof 2, which never existed because the apply was
  refused.
- `CB61bi2-AC2` is PENDING-ADJUDICATION for `3.0.0_SA_CVO` at L9, as a judgment criterion must be.
- `D2-S99` (the deploy ledger has no state for a gate-refused apply) is with whoever owns
  `.tools/deploy_ledger.py`.

---

## Current State

All four orders this seat held this session are terminal: `CB-al-2` COMPLETE, `CB-bi-2` COMPLETE, `CB-bj-1`
STOPPED-and-issued, and `CB-bi-2`'s earlier stop superseded by amendment. Work is on origin @`4321f665d3`. Zero
orders runnable; event-driven.

---

## Next Steps

1. `[1.0.0_SA_CTO` (laptop)`]` The naming remedy for `restricted` — a vocabulary entry, a registry row, or a
   different policy name built by `name()`. **Not** the `cloudops-49f-…` name the gate prints, which puts the wrong
   firm on a Cottonwood-only grant.
2. `[2.0.0_SA_COO~C2]` Amend `CB-bj-1` with the resolved name when the canon answers; `D2-S95` stays armed until
   its proof 2 exists.
3. `[3.0.0_SA_CVO]` `CB61bi2-AC2` at L9.
4. `[0.7.0_AE_CloudOps~CB2]` Nothing. Idle on the watcher.
