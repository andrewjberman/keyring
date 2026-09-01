# /self-drive D2 — tick 103

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` (:07/:37) · **UTC:** 2026-09-01 ~07:2xZ
**Ticks covered:** 103 (first of the re-arm; 102 died with the 2026-08-30 session)
**Carrier:** `org/XXX.md` line 633, Step 1b-F clause @`e706f59f62`
**Paired:** `/drive` @ `2.0.0_SA_COO`, cron `b8ac5fba` — armed on the same Andrew word
**Authority:** Andrew-direct 06:5xZ, relayed verbatim by `0.0.0_AB_MSTR` msg 90895

---

## Scope

```
SELF-DRIVE SCOPE: D2 -> 1 directive -> 10 project(s)     device: laptop     open TOs: 22
  claims scan: 348 project JSONs -> 7 claims on D2_ADVI_49F_E2E_PRD.md, ALL already members
               0 member-set lag, 0 malformed
```

⛔ **SCOPE LIMB UNRESOLVED BY DESIGN.** Andrew named an order — D2 FIRST, then D8. **D3 was neither
named nor struck.** This driver does not strike it (narrowing on its own authority) and does not
silently keep it ahead of D8 (widening against his order). D3 stays in scope; **its order relative to
D8 is a card at Andrew.** D2 is first under every reading, so the tick proceeds unimpeded.

## Calls pitched

**4 ADJUDICABLE · 0 RESERVED** — pitched to `3.0.0_SA_CVO`, msg 90908.

⭐ **The ALL-RESERVED tell did NOT fire.** Stated explicitly because the §1 restructure exists for
the opposite failure: no call was costumed as a NEVER, and none carried a citable law line or
standing hold.

## Verdicts received and acts taken

All four RECs **ADOPTED**, three with amendments. Ledger 19 → 23 rows.

| Call | Verdict | Act taken |
|---|---|---|
| 1 — `ADVI_ROSTERCOLS` stage lags its own PRD | adopted | routed to register owner; **no self-advance by the PRD's author** |
| 2 — `OPAL_ADVIPOINTERS` null stage, ~9 open TOs | adopted + amended | routed; amendment recorded below |
| 3 — flow-ingestion defect unowned | adopted + amended | **card already at Andrew from the CVO terminal — NOT double-carded**; allocation to COO, acked |
| 4 — `name`/`owner` blocked on an unminted project | adopted + amended | **PRD amended this turn** |

### ⛔ Amendment on CALL 2 — sharper than the call it answers

The call said a null stage "degrades every status read." It does something more precise: **the
completion test's VERDICT stays sound — a null stage cannot be `complete` — but its MEMBER-LEVEL
resolution is unsound**, because one member's position is unknown by construction.

>> **The stop-condition is safe; the progress reporting is not. "8 active" must not be quoted as
   measured while one of the eight is unmeasured.** <<

### ⭐ Amendment on CALL 4 — and the driver was wrong about its own text

The boundary is **A VALUE REACHING A SERVED ARTIFACT**, not "a schema mentions the column."
Sourcing, identifying the field of record and internal typing are pre-disclosure. **Widening a
SERVED type so the field appears in a served object IS disclosure, even unpopulated — a field name
is itself a statement.**

⛔ **This closed a loophole between the PRD's own §3 and §5 that its author opened.** §3 tier 2
(`CONTRACT-ONLY` — a serving-contract widening with no new producer) reads as pre-disclosure work
*because* it adds no producer. **For `name` and `owner` it is not.**

⚠ **AND THE CALL AS PITCHED OVERSTATED ITS OWN PREMISE.** It described the clause as blocking
*sourcing*. **It never did** — the PRD already read "this project sources the columns; it does not
rule on what may be displayed." The driver mis-recalled text it had authored three hours earlier and
pitched a call against its own artifact without re-reading it. The real defect was not an over-broad
block but an **under-specified boundary a later reader could cross while believing they were inside
it** — which the adjudication found only because it read the artifact instead of the call.

## Completion test — READ, never declared

```
2 of 10 projects complete -> NOT DONE
  complete: ADVI_BDPLAT_RESTORE, ADVI_49FSRC
  active:   OPAL_ADVIPOINTERS*, ADVI_INSURE, ADVI_STITCH, ADVI_PERFRP,
            ADVI_COTKEY, ADVI_49F, ADVI_BDPARITY, ADVI_ROSTERCOLS
  * position UNMEASURED (null dep_stage) — see the CALL 2 amendment
```

## RESERVED cards still at Andrew

- **D3's order relative to D8** — the scope limb above.
- **Whether the flow-ingestion defect widens the ruled 22** — carried from the CVO terminal, not
  duplicated here.

## Compiler Tools

`directives-check.py --json` (scope + denominators, D2/D3/D8) · `comp-find` (carrier row location in
`XXX.md`; law-file scan across the 121-commit batch) · `comp-state --self-test` PASS 4/4 earlier this
session · a python claims scan over 348 project JSONs handling both `prds[]` shapes (the documented
bare-string crash) · `git ls-remote` for every push-state claim. No `head` on any census.

**State:** `ARMED` · next tick on the cron.
