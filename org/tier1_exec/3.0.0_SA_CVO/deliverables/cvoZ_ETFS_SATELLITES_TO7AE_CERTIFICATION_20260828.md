# CERTIFICATION — `ETFS_SATELLITES.TO-7-AE` (the scoped satellites route)

**Certifier of record:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T02:5xZ
**Executor:** `0.7.0_AE_CloudOps~S` · **Issuer:** `2.0.0_SA_COO~Z` · **Report:** msg 12286
**Instance (certified object):** `org/tier2_senior/0.7.0_AE_CloudOps~S/deliverables/ETFS_SATELLITES.TO-7-AE_PROOF_OF_SPEC.json` @`2795da3de9`

---

## VERDICT: **CERTIFIED. 7 of 7 PASS, and the coverage the checker could not assert is verified here.**

---

## 1. ⛔ THE CHECKER HANDED ME TWO THINGS IT EXPLICITLY CANNOT ASSERT, AND BOTH ARE THE CERT'S JOB

Run at this seat, `VALID`, 7 acceptance rows, **0 violations**. But it printed its own limits, unprompted:

> *"no `expected_criterion_ids` given — **COVERAGE UNCHECKED** (row quality only; **an omitted criterion is invisible to this run**). The cert consumer runs step-zero."*

> *"this closes the TO against ITSELF and against the decomp's id space. Whether the TO's declared set
> IS the decomp's complete criterion-bearing set is **a CVO cert judgment (enforcement layer 5), NOT
> asserted here**."*

**A tool that names the question it is not answering is worth more than one that returns a bare PASS** —
and the coverage limb is precisely where a certification goes hollow if nobody runs it.

### STEP-ZERO, RUN AT THIS SEAT
```
TO declares      T7AE-AC0 · AC0b · AC1 · AC2 · AC3 · AC4 · AC5     = 7
Instance files   T7AE-AC0 · AC0b · AC1 · AC2 · AC3 · AC4 · AC5     = 7, all PASS
                 IDS IDENTICAL, SET-FOR-SET. No omitted criterion.
```
**COVERAGE COMPLETE.**

### AND THE "2 OF 27" IS BY DESIGN, NOT A GAP
`alignment-forward-2` resolved **2/2** distinct cell_refs against a decomp id space of **27**. That is
correct: the TO's `<decomp_ref>` declares exactly **`SAT-a-4`** and **`SAT-c-2`** and states **"NO new
cell."** Its `<certification>` records that this seat's own lineage certified the decomp and that
`SAT-a-4` was **left explicitly open for the issuer to close** — which this TO does. Two of
twenty-seven is the declared scope, and I checked that rather than reading a low ratio as a shortfall.

## 2. ⚠ ONE PRECISION CORRECTION TO THE REPORT — the coverage holds, the citation did not

msg 12286 §1 states *"`expected_criteria` is 7; filed rows are 7."* **The instance's `expected_criteria`
field reads `None`** — which is exactly why the checker printed COVERAGE UNCHECKED.

The **claim is true** (the TO does declare 7) and the **citation is wrong** (it is not backed by the
field named). I verified the denominator from the TO itself, so nothing rests on the mis-citation.
⭐ Recording it because a true conclusion resting on a field that does not exist is the shape that
survives review — nobody re-checks a number that turned out right.

## 3. WHAT THE EXECUTION DID THAT I AM CERTIFYING AS METHOD

- **AC3's row is another seat's measurement and SAYS SO.** The APPLIED half is the executor's; the
  EXERCISED half is `0.4.0_DE_ClientPlatform~S`'s @`80f42be356`. **They did not re-run it** — *"re-running
  a peer's command is repetition, not corroboration, and the criterion is discharged by the measurement
  rather than by who typed it."* Rule 22 applied to **attribution**, which is the direction it is
  usually forgotten in.
- **AC4/AC5 argued by STRUCTURAL IMPOSSIBILITY, not by behaviour.** The router constructs statuses
  `['204','400','401','403','404']` — **no 200** — and contains no `books` / `as_of` / `schema_version`
  at all, so it *cannot* synthesise an empty set from a refusal nor strip an `as_of`. **Positive
  control:** the same probe finds `statusDescription` / `status` / `error` / `Not Found` / `401`, so the
  ABSENCE is a finding rather than a dead probe. A structural argument beats a passing test.
- **Two stale sentences corrected by AMENDMENT, not silent edit.** The ledger header and one evidence
  line said AC3's authenticated half was outstanding — true when written, false now. *"A ledger that
  silently rewrites its own history is worse than one that shows the correction."*
- **The other seat's finding carried AS THEIRS, with its bound verbatim:** the `opal-capital` 400 is
  **not evidence about the cottonwood path in either direction**. A measurement on one path is not
  evidence about a sibling path, and saying so in *both* directions is what keeps it honest.

## 4. WHAT THIS CERTIFICATION DOES NOT DO

- Does **NOT** close `ETFS_POSITIONING-Z-S16` — staff still see a pill that 400s. The remedy fork spans
  the router and the mode allowlist and is the issuer's.
- Does **NOT** close the **cottonwood rung**, which remains INFERRED FROM SOURCE ONLY. My 12277 ruling
  stands: a self-signed firm claim would test the boundary by circumventing it.
- Does **NOT** touch `TO-6-AE`, whose AC3 fires 07:00Z on its own trigger.
- Does **NOT** close D4. Its bar is Andrew's smoke test.

---

— `3.0.0_SA_CVO~Z`
