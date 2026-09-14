# CTO ADJUDICATION -- `LGIC_NAMING` -- row S10: legacy membership is DATA, so the grade stays a function of `(name, type)`; and a legacy root `code/` key's verdict

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-14 ~11:3xZ

**Class:** the L4 follow-on to this seat's own ruling @`7bd4ef6f27`. That record is
`CTO_ADJUDICATION_LGIC_NAMING_20260914T103xZ_S6_S7_S8_ENTITY_PARTITION_CODE_TIER_LEGACY_SERVED_PATHS.md`.

**Authority:** Andrew-direct 2026-09-03 ~05:2xZ, the same authority as that record.

## Why

`2.0.0_SA_COO~G` filed row `LGIC_NAMING-S10` @`1765c4d16f` while re-reading the decomposition against v1.3. The row is
right about this seat's own ruling.
- **v1.3's `key.legacy_served_path` makes a platinum key's verdict turn on whether it is legacy.** A snake_case leaf,
  or a bare entity-id segment, is CONFORMANT when legacy and OUT-OF-PATTERN when new.
- **Legacy-ness is not a property of `(name, type)`,** which is the grade's ratified signature (CONTRACTS row 2,
  SIGNED; data `grade.signature`). And no field of v1.3 lists the legacy set.
- **So two hand graders can disagree on the same key, and so can `grade()` and a grader.** That is FWD-5's failure.
  Decomposition v2 closed it for the round by having LN-g-1's written rule enumerate the set. The contract question
  the row names as this seat's was still open: where the set lives, and how `grade()` consumes it.
- **A second, smaller gap:** a legacy root `code/` key "stays until its pipeline moves", but v1.3 gives it no verdict.

**No round is live.** LGIC_NAMING is at DECOMP v2, drained @`e902f6be00`, and L6 is not issued (blocking item 5).

## OPEN CALLS -- `LGIC_NAMING` -- 2 calls, adjudicated

```
+-- CALL 1 of 2 -- LGIC_NAMING-S10 -------------------------------------+
  **Where does legacy-served membership live: as DATA the grade reads,
  or as a new input to grade()'s signature?**
  v1.3 makes the verdict turn on it, and neither (name, type) nor any
  field of the data file carries it.
  --------------------------------------------------------------------
  **REC --** (a) DATA. The set is a CLOSED list: the portal is frozen, so
  it adds no request. Closed enumerations are what the data file holds
  (CONTRACTS row 1, unchanged). It lives at
  org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json,
  written by cell LN-g-1, which already enumerates the set in decomp v2.
  The list carries the portal vintage it read and a printed denominator.
  NAMING_SCHEMA.json names that home, so the standards file stays L4's
  and no worker writes it. grade() reads the list at run time as it reads
  every other enumeration, and its signature stays (name, type) over
  this file.
  Until the list lands, a key whose verdict turns on membership RAISES:
  "a defect in this file, fixed there" (grade.unplaceable). It is never
  guessed CONFORMANT or OUT-OF-PATTERN, and its absence is a stated claim.
  (b), adding the set to grade()'s signature, changes CONTRACTS row 2
  (ratified text) and LGIC_ENFORCE's counterpart, and hands every caller
  a list to carry.
  --------------------------------------------------------------------
  RULING -- (a), because it keeps the signed contract, keeps one owner
  per enumeration, and puts the measurement in the cell that already
  makes it.
+---------------------------------------------------------------------+

+-- CALL 2 of 2 -- LGIC_NAMING-S10, second instance --------------------+
  **What does a legacy root code/ key grade?**
  v1.3 says legacy root code/ homes "stay until their pipelines move",
  and says nothing about their verdict.
  --------------------------------------------------------------------
  **REC --** OUT-OF-PATTERN, with the code-tier key as its canonical_form
  (for example code/gold/x.py in opal-data-bd reads
  advi/49financial/code/gold/x.py). It is a remediation target like any
  other. A verdict is not a mandate to move: MDPF_CANON's frozen rollback
  objects (its DEC-14) keep the verdict and stay where they are.
  --------------------------------------------------------------------
  RULING -- as the REC, because the grade reports the grammar and the
  PRDs decide the moves, and giving it a fourth verdict or an exemption
  class would break "three verdicts and no fourth".
+---------------------------------------------------------------------+
```

## What changes

| surface | change | half / owner |
|---|---|---|
| `NAMING_SCHEMA.json` v1.3 -> v1.4 | `key.legacy_served_path` gains the membership sentence. New `key.legacy_served_paths`: its home, producer and claim ("absent until LN-g-1 lands it"), and the RAISE until then. `key.code` gains the legacy-root verdict. The changelog records it | the data file; `LGIC_NAMING`'s author |
| `LGIC_NAMING_PRD.md` v1.3 -> v1.4, S1 | one clause citing `key.legacy_served_paths` and the RAISE. ENDPOINT and CONTRACTS are byte-unchanged | the brief half re-opens (`4.0.0_SA_CRO`) |
| the tree row | phase, blocking (1) and lineage | this seat |
| decomposition v2 -> v3 | LN-g-1 gains a second write surface, `deliverables/LEGACY_SERVED_PATHS.json`, with its vintage and denominator; rectangle row 6 stays "unchanged" for the standards file | `2.0.0_SA_COO~G` at L5 |

**Not changed:**
- the grade's signature, and its three verdicts;
- CONTRACTS, on either project;
- any served byte;
- the D8 PRDs. They keep legacy names byte-for-byte already, and the list only makes their grade decidable.
