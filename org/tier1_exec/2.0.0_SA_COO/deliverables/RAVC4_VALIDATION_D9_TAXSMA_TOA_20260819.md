# RAVC-4 VALIDATION — D9_TAXSMA.TO-A-SITEZ (state assessment)

**Validator:** `2.0.0_SA_COO` (issuing seat). **Delivered by:** `0.4.0_DS_ClientPlatform~Z` via the
MSTR ferry; artifacts on `origin/SITEZ` @1da46a1f43 + @3da5bcaee6, status @990cfc061b.
**Dispatch vintage:** @fac13ccc3a.

## VERDICT: ACCEPT — 7/7 criteria, coverage-checked, the load-bearing claim independently re-derived, one CITATION-QUALITY note (not a rework trigger)

---

## WHAT I DID NOT DO: TAKE rc=0 ON THEIR WORD

Their D9A-7 evidence cites *"rc=0 on this instance ... the checker's own stdout is the oracle."*
**I re-ran the checker myself** — a producer's self-report is not evidence.

**Then I ran a MUTANT control, which is where this got interesting:**

| Run | Result |
|---|---|
| Delivered instance, no expected-ids | `VALID rc=0`, 7 rows |
| **MUTANT** (D9A-5 row deleted), no expected-ids | ⚠ **`VALID rc=0`, 6 rows — THE MUTANT PASSED** |
| Delivered instance, WITH the 7 expected ids | `VALID rc=0` — **7/7 matched** |
| MUTANT, WITH the 7 expected ids | `INVALID rc=1` — *"criterion 'D9A-5' ... has NO instance row (silent omission)"* |

**The instrument is HONEST about its own blind spot** — it prints *"COVERAGE UNCHECKED ... an omitted
criterion is invisible to this run. The cert consumer runs step-zero."* **I am the cert consumer.
Step-zero is mine, and it passed 7/7.**

### THE CITATION-QUALITY NOTE (recorded because the next seat will copy this pattern)
**Their CLAIM is TRUE — their EVIDENCE AS CITED could not have established it.** D9A-7 asserts
*"VALID rc=0 POSITIONAL: ids D9A-1..D9A-7"*, but **a bare rc=0 does not check positional coverage at
all**: the same rc=0 comes back from an instance missing a criterion entirely. The instance is
genuinely complete — I verified it — but the cited oracle could not have shown that.

**Not a rework trigger and I am not requesting one.** It is the *instrument that could not have said
otherwise* class, caught at the validating seat exactly where it should be.
**CARRY FORWARD: an rc=0 citation for a POSITIONAL claim must name the expected-id set it ran against.**

---

## INDEPENDENT RE-DERIVATION OF THE LOAD-BEARING FINDING

D9A-5's **NEVER-SCHEDULED** verdict drives the whole assessment, so I read the APPLIED plane myself
rather than accepting three planes on their report.

| Probe | Their claim | My live read |
|---|---|---|
| `get-policy` on `opal-assets-bd49f-reporting-pull` | `ResourceNotFoundException` | CONFIRMED |
| `list-event-source-mappings` | `[]` | CONFIRMED |
| **POSITIVE CONTROL** (`mdpf-gold-lambda`) | — | returns a real policy carrying `AllowExecutionFromSchedulerFloor` |

**The positive control is the part that matters:** it proves the probe DISCRIMINATES, so the
`ResourceNotFoundException` is a **TRUE ABSENCE** — not a confident nothing from a blind instrument.
**NEVER-SCHEDULED holds, independently.**

---

## THE THREE FINDINGS I CARRY FORWARD AS COO

1. **NEVER-SCHEDULED IS A THIRD STATE** beyond never-launched/stopped, and it is worse than the rule's
   usual case: **no trigger at all, one lifetime invocation (2026-07-17).** Primary input to (c1),
   already cut and already gated on the guardrail set.
2. **BUSINESS OUTRAN PIPELINE:** the master xlsx carries **11 accounts / $27.71M / 5 traded 08-05**
   against the **3-account roster** the pipeline knows. **A SCOPE finding, not a staleness finding** —
   it re-sizes (c1) before (c1) is built.
3. **BUILT-IS-BUILT:** pt1 intake is alive but automation ran **ONCE (07-15)**, ~24 **TRADING DAYS**
   unfiled. The seat counted in trading days — applying the calendar rule rather than tripping it.

## ROUTED, NOT CLOSED HERE
- **H8 — `comp-pipescript`'s pipeline universe lacks the `data/assets` tree**, so the chain scripts are
  **unverdictable by the deploy instrument**. A **Rule-22 comp-tool COVERAGE DEFECT** (the comp-tooling
  is foundational, not additive — a gap is a defect). → CTO.
- **H5 — WS-4/WS-R5 IAM roles live since 2026-08-15T02:32Z** while every record reads them
  REMAINING-gated. Least-privilege verified; this is a **gate-SEQUENCING** finding. → CTO via MSTR.
- **#48** split-supersede recommendation is at Andrew (sitez console). **#42** correctly needed no
  recommendation — Andrew's supersession landed mid-pass and the seat cited rather than re-authored it.

## SEAT EVENT
TO-A was the seat's entire workstream and is delivered. **THIS VALIDATION IS THE SEAT-FREEING EVENT.**
Per COO~Z's 204548Z allocation call the freed slot goes to **CVO~Z** (unblock-in-flight beats
start-new); **D8 queues for the second slot**, package held @509deefdd4.
