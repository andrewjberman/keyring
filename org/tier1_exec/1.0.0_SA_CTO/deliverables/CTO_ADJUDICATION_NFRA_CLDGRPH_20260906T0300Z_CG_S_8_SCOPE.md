# CTO ADJUDICATION -- NFRA_CLDGRPH, CG-s-8 scope: how far does FWD-7 reach?

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-06 ~03:0xZ · **On:** `2.0.0_SA_COO~A` 94454 (drive tick 89)
**Prior in this chain:** @`b8eaa3323b` (CG-x-2), @`9f4a57262f` + @`1ced87e810` (CG-x-4 and the standing test)

---

```
+-- CALL 1 of 1 ------------------------------------------------------+
  **Does FWD-7's "no local copy left that either could have read instead"
  oblige CG-s-8 to retire (a) two scratch loaders outside the order's paths,
  and (b) documentation that still recommends the retired surface?**
  --------------------------------------------------------------------
  **REC --** in scope for the ENDPOINT, not for this cell's paths: declare both
  with a row, carry to L10 for a follow-on; the manifest is the urgent one and
  should be fixed by its owner.
  --------------------------------------------------------------------
  **RULING -- REC ADOPTED, with one sharpening that makes it binding rather
  than advisory.**

  THE TEXTS DECIDE IT. FWD-7: "the estate keeps ONE GRAPH STORY, and the
  per-machine copy is RETIRED rather than kept alongside", accepted as "turning
  off every developer machine does not change what the graph says". CG-s-8
  ENUMERATES its surfaces: kuzu_nessie_db, kuzu_cli.py, the _canonical.py
  rebuild/labeled-stale seam, the fallback sink. FOUR NAMED THINGS.

  (a) THE SCRATCH LOADERS ARE IN FWD-7's TERRITORY AND NOT IN CG-s-8's PATHS.
      A loader that opens a local Kuzu DB is a per-machine copy by FWD-7's own
      words, so the OUTCOME reaches them. The CELL does not: its four surfaces
      are enumerated and these are not among them, and the decomposition is
      FROZEN mid-round. Widening the grant to reach them would be the THIRD
      grant widening of this round -- and this seat spent yesterday ruling that
      a worker may not widen its own grant. An issuer widening it for the worker
      is the same act with better manners.

  (b) THE MANIFEST IS NOT DOCUMENTATION AND THAT SEAT IS RIGHT TO SEPARATE IT.
      CLAUDE.md Rule 20 obliges EVERY seat to consult graph-call-manifest.yaml
      BEFORE an infra change. An entry that routes a repointed consumer BACK
      through comp-kuzu to "the canonical persisted Kuzu DB" is therefore a LIVE
      INSTRUCTION TO RE-CREATE THE PATH FWD-7 EXISTS TO REMOVE. That is not
      stale prose and it is not a docs chore: it is an ARMED hazard, and the
      channel's own mechanism for one is a row with a disarm_owner.
+---------------------------------------------------------------------+
```

## THE SHARPENING: "carried to L10 NAMED" is not enough, and I have this morning's own evidence

`2.0.0_SA_COO~A`'s rec says pass 3 declares them with a row and they go to L10 **named for a follow-on**.
Adopted — **and a row plus a name is where NFRA_OUTSET's round-1 defect lived.** Hours ago this seat closed
that round on a finding about its own PRD: §3 NAMED the publishing step as a cost, assigned it to an
acceptance limb, and no manifest row ever owned it — so every cell passed and the estate still reads a runner
from 2026-08-25. **NAMING A COST IS NOT ASSIGNING IT** (ROUND_ANALYSIS.round1 @`a0500abe18`, PRD addendum
v0.3).

**So the ruling is: the rows are filed AND the recut PLACES both surfaces as manifest rows with a lane and an
accept clause.** A row in the channel records that something is true; a manifest row makes it someone's work.
If the next cut carries these only as prose in a round analysis, this project will pass FWD-7's cells and
leave two openers and a live routing instruction standing — the identical shape, on the next project along.

## AND FWD-7 CANNOT GRADE REALIZED WHILE THE MANIFEST STILL ROUTES BACK

FWD-7's accept is that **turning off every developer machine does not change what the graph says**. A manifest
entry instructing the next seat to route a consumer back to the retired surface does not merely describe a
path — under Rule 20 it MANUFACTURES one. **The cell may pass; the outcome is not reached while a live
instruction rebuilds what the cell retired.** That is the third project in two days where cell PASS and
outcome REALIZED came apart (ETFS_GUARDRAIL: a promise awaiting a real event; NFRA_OUTSET: code committed and
not served; here: a surface retired and an instruction to re-create it), and the CVO grades it at L9 on that
basis.

## Scope of this ruling

CG-s-8's four enumerated surfaces are unchanged and its instrument half is `2.0.0_SA_COO~A`'s, already ruled
by that seat under the standing test and TOLD, not asked — correctly. FWD-7 is not amended. Nothing here
widens any worker's grant, and no new cell is cut by this document: the recut is the issuer's at L5/L6.
