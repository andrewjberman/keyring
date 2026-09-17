# `1.0.0_SA_CTO~Z` -- seating, the round-11 L10, PRD v0.9, and two cards at Andrew (04:40-05:20Z)

**archetype:** MIXED (COORDINATE + VALIDATE + SCRIBE)
**Seat:** `1.0.0_SA_CTO~Z`, site-Z fabric, branch SITEZ. **Project:** AMGT_RESAPP (D5) -- tonight's SOLE FOCUS.
**Authority:** Andrew-direct ~04:3xZ (`afc02ead18`) and ADDENDUM 1 ~04:5xZ (`c05a41c0f4`).

## Current state

Round 11 is ACCEPTED and answered. Round 12 is defined as **thirteen cells (A-M)** and is gated on ONE act:
`3.0.0_SA_CVO~Z`'s ratified-text signature on PRD **v0.9 @`44269d0515`** (half `88e330dea809`). `2.0.0_SA_COO~Z`
may run L5 now; only the ONE L6 issuance waits. **Two RESERVED cards sit at Andrew** and without them the
finished product is five names.

## What this session did

| act | artifact |
|---|---|
| `/watcher`, startup A-F, identity, delivery ledger | Monitor `bzg512yz1`; 4 OFFER-EXHAUSTED messages opened and acked |
| Found the round-11 slug **stranded off-tree**, measured the drain clean, routed it | msg 23366 -> drained by `3.0.0_SA_CVO~Z` @`d87181423c` |
| L10 ROUND_ANALYSIS + goal + Step 1b-F carrier row + `Z-S108` disarm | @`c708914c50` |
| ADDENDUM 1 -- four cells the analysis missed | @`1db70c8e87` |
| PRD v0.8 -> **v0.9**: `FWD-20` + five contracts | @`44269d0515` |
| ADDENDUM 2 -- three rulings corrected, cell M, two cards | @`06378dd3bd` |
| `/self-drive AMGT_RESAPP` armed, 30m | cron `6b00e98e` at `13,43` |

Rulings made as adjudicator: the continuity ruling (the `~Z` fabric drives AMGT_RESAPP from round 12), five
L10 contract calls, five A1.3 rulings, three self-corrections, and the owner reassignment of the 44 open remedy
rows by limb (39 -> COO, 5 -> CTO).

## THREE THINGS FOUND, each invisible to the instrument that should have caught it

1. **A limb's output can be COMPLETE, CORRECT and INVISIBLE.** `3.0.0_SA_CVO~W`'s whole round-11 adjudication
   -- slug, 250 dispositions, 70 rows, three stamps -- sat on an unmerged branch while `project.json` read
   ROUND_CLOSE, `prd-signoff` read ADMITTED and the packet was filed. **A lane going down does not surface its
   unmerged branches.** One `git branch --contains` on the dead lane's last artifact is the read.
2. **A round's own artifacts cannot enumerate what the round never looked at.** Eight cells were subtracted
   from the slug and the packet; `2.0.0_SA_COO~Z` differenced them (24/24, 15 shared) and the agreement read
   as corroboration. It was not -- they share the round-11 evidence base. `4.0.0_SA_CRO~Z`, pointed at the
   PRODUCT, found the page exists **only on a drain ref** and the print route **500s**, neither named anywhere
   in the round-11 record.
3. **Cells can repair the PLANE and never touch the POPULATION.** A-L would have left 10 of 19 outcomes ABSENT
   for any non-pilot name. One axis across ten outcomes, invisible per-outcome because every cell is correctly
   built -- Rule 22's shared-dependency blindness one level above the cells.

## Two defects caught against myself

- **R3 was wrong:** I ruled the pull consumer becomes an event-source-mapped Lambda. It calls the Bloomberg
  DAPI at `127.0.0.1:8194` **on this box**; a Lambda would fail every message. Corrected -- the consumer stays
  on the box and its cadence is a card.
- **The v0.9 change-note used a `##` heading**, making it a top-level section rather than preamble and moving
  the **brief** half (`0455fc3d1e95` -> `379799cfc644`) for text changing no requirement -- the exact trap the
  same paragraph was warning about. Caught by re-reading the half hashes **after** the write. Demoted to
  `###`; brief restored exactly. ⭐ **Measure the halves after the write, never only before.**

Also discarded rather than reported: a negative control using `origin/CLOUD`'s tip returned
`fatal: Not a valid object name` -- an error that reads like a clean negative. Replaced with `5d3a04cab6`,
confirmed present by `git cat-file -e` first.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-which` (A.3 exercise) | PASS | 104 of 104 comp-tools resolve bare; forwarder RAN |
| `prd-signoff.py status` | used x4 | the one read of what is owed; caught v0.9 WITHHELD + owed signer |
| `prd_signoff_lib.half_hashes` | used x6 | before AND after every PRD write; caught the `##` defect |
| `surprise-row-gate.py` | rc=0 | `Z-S108` graded as 1 new row of 251 |
| `to-pipeline-gate` / `missions-tree-check` | rc=0 | 0 violations on every commit |
| `audit-archive-invoker.py` | 14 findings | all KNOWN device-chain classes; NOT chased per `org/XXX.md` A.2 |
| `git merge-tree --write-tree` | rc=0 | measured the drain clean before routing it |

**Gap found:** none in the tools. The gap was in **which document I subtracted from**, and no tool grades that.

## Owed next

`3.0.0_SA_CVO~Z` the v0.9 signature; `2.0.0_SA_COO~Z` L5 then the ONE L6 issuance over A-M; **Andrew** the two
cards. This seat: adjudicate on the `13,43` tick, and answer the next slug.

Push state: **LOCAL on SITEZ** for every hash above. LD-0522 puts the push with `0.0.0_AB_MSTR~Z`; none requested.
