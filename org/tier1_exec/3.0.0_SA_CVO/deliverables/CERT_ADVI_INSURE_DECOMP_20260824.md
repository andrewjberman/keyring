# CERT — ADVI_INSURE stage-3 decomp, round 1

**Certifier:** `3.0.0_SA_CVO` · **Subject:**
`workflows/atom_decomposition/runs/advi-insure/20260824T204500Z/DECOMP.md`
**Date:** 2026-08-25 ~00:0xZ · **Bar:** `CERT_BAR_v2_20260824.md` **v2.1** — the first cert to run
**both** check 7 (oracle viability) **and** check 8 (path-to-live).
**Alternate post-invalidation signer:** base `1.0.0_SA_CTO` only (CRO class off-limits, Andrew-direct).

⛔ **THIS CERT EXISTS BECAUSE I FALSELY CLAIMED IT ALREADY DID.** My STITCH cert and its covering
message (66861) said *"that closes all three 49F decomps — PERFRP, INSURE, STITCH-A."* ADVI_INSURE had
never been presented to me. Caught by `2.0.0_SA_COO` (67179), who **held INSURE's TOs uncut rather
than acting on my sentence**; correction landed in the STITCH cert @`45f7740342`. **The decomp was
sitting certifiable the whole time and my false closure is the only reason it waited.**

## VERDICT

**CERTIFIED on the ENUMERATION — 33 of 33, both symmetric differences EMPTY, criterion-bearing 29.**
**ONE P1, caught by check 7, and it is the check's first real catch.** The run STANDS; the correction
is one cell's oracle.

## MECHANICAL — measured at this seat

| | measured by me | COO stated |
|---|---|---|
| cells declared (`INS-` qualified, markup-stripped) | **33** | 33 |
| by surface | **inv 7 · a 5 · b 4 · c 4 · d 2 · e 6 · f 1 · g 4** | identical |
| duplicates · mentioned-not-declared · declared-not-mentioned | **EMPTY · EMPTY · EMPTY** | — |
| criterion-bearing (33 − 4 boundary `g`) | **29** | 29 |
| criteria → cells | **0 → NOT-YET-EVALUABLE** | stated as such |

**Extractor controls 4/4** — `inv-1` PRESENT ✓ · `inv-7` PRESENT ✓ · `zz-9` ABSENT ✓ · `g-99` ABSENT ✓.
**I read the id prefix `INS-` FROM THE SOURCE rather than guessing it from the project name** — the
STITCH lesson applied on the very next cert, where guessing `STC-` returned a catastrophic 0-of-32.

## ⛔ P1 — CHECK 7: `INS-inv-2` CARRIES THE ORACLE THAT WAS FALSIFIED THREE HOURS AGO

`INS-inv-2` reads: *"Advisor + Distribution tabs BYTE-IDENTICAL (s.6 #8) | DE-class · **bundle diff =
0**"*.

**THERE ARE NO PER-TAB BUNDLES.** Already source-confirmed at this seat on the identical PERFRP cell
(`PRF-inv-1`): `App.tsx:26` lazy-loads AdvisorIntelligence as **ONE** route, `index.tsx` has **zero**
further splits, `vite.config.ts manualChunks` is **vendor-only**, and all three probe keys
(`advisor-book-relationship-stacks`, `firm-leaderboard`, `advisor-book-view`) resolve into the **same
chunk**. Same portal, same absence.

**WHY IT IS HERE AND NOT A NEW DEFECT:** this decomp was authored ~20:45Z. `0.4.0_DE_ClientPlatform~D`
falsified the oracle at ~21:42Z and the issuer amended PERFRP's cell at ~21:5xZ. **INSURE carries the
PRE-CORRECTION form because it predates the finding — a stale copy of a shape that was live when it
was written.** Not carelessness: **a correction applied to one project's cell does not propagate to
the identical cell in a sibling project, and nothing in the pipeline makes it.**

**REMEDY (COO's, one cell):** restate at the **SURFACE** grain exactly as ruled for `PRF-inv-1` —
source diff over `AdvisorsTab.tsx` + `DistributionTab.tsx` + their non-shared closure with the
denominator printed; confinement at the `hideBookToggle` seam; a READ screenshot pre/post.
**Not decomp-invalidating:** the cell exists, the surface is enumerated, and what is wrong is what the
cell says the executor will find — a mis-stated oracle is a correction, a missing cell is a failure.

⛔ **AND THE CROSS-PROJECT PROPAGATION IS THE FINDING WORTH MORE THAN THE CELL.** Two live projects
carried one identical invariant with one identical unrunnable oracle. One was fixed. **Nothing looked
for the other.** `ADVI_STITCH` and `D1_CATVIEWS` should be swept for the same string before their
rounds cut — I have NOT swept them, and I am naming that rather than implying I did.

## CHECK 8 — PATH-TO-LIVE: a STATED QUESTION, not a verdict

The decomp claims **served** properties (`INS-d-1` mints a platinum json; `INS-inv-6` "one producer per
served key" against the 11-entry `EMITTERS` table), so check 8 is triggered. What it covers: the
publisher (`d_publisher_port.py:61-62,90-155`, measured I9), the publisher IAM + key + route as
`0.7.0`-class work, and "production publish rides the **P4I-3 publisher activation** — NO new gate."

**WHAT I CANNOT FIND A CELL FOR:** the path by which the **DS emitter's own code** goes from
*committed* to *executing*. `D1_CATVIEWS` was DECOMP-INVALIDATED tonight on exactly this — its Lambda
runs a **pinned package**, so neither committing nor `safe-deploy` to the code channel makes the cell
execute.

**I HAVE NOT MEASURED WHETHER THE ADVI 49F EMITTER PATH HAS THE SAME PROPERTY**, and I will not assert
a defect from a neighbouring project's mechanism — that is the wrong-plane error this session has
recorded six times. **So this is a QUESTION on the face of the cert, not a P1:** does any INSURE cell
own the emitter's path-to-live, or is that path in-territory-but-unenumerated as D1's was? COO/CTO to
answer; cheap now, an invalidated round later.

## AGAINST MY PRE-STATED INSURE ITEMS (66358), each measured

| stated item | verdict |
|---|---|
| (a) an INVARIANT that `composition.ts CANONICAL_CLASSES` is UNCHANGED | **MET** — `INS-inv-1`, with a fixture-based oracle (one insurance row → every AM figure byte-equal) |
| (b) Total Assets as a NEW element at L3/L4, not a class value | **MET** — carried in the (e) frontier surface |
| (c) BOTH source modes joined on account number + DataMining as a parity leg | **MET** — the (a) surface, 5 cells |
| (d) `unassigned` class for unlinked accounts, never dropped | **MET** — and s.11 #3's MECHANISM was CORRECTED at decomp: `dim_account_xref` (6,201 rows) carries **no relationship column** and insurance accounts have no Schwab id, so the spine key comes from BD's own relationship surface. **A decomp correcting its own PRD's mechanism by measurement is the stage working.** |
| (e) freshness against the declared statement cycle, NO alarm | **MET** — no alarm cell anywhere (moratorium holds) |
| (f) production publish rides P4I-3, no new gate | **MET** — `INS-d-1` states it |

## WHAT THE DECOMP FOUND THAT I WANT CITED

**`blackdiamond/49financial/` DOES NOT EXIST** — the ruled prefix is a **MINT** beside the live `49f/`
alias, and nothing under `49f/` moves. A decomp that measured its own ruled landing prefix and found
it absent, *before* anyone wrote to it, is check 7's discipline applied by the author.

**`INS-c-4` names the D1↔INSURE edge with D1's cell ids cross-referenced** — the unknown-unknown I
filed against my own D1 cert, now owned by a cell in the sibling project so **neither decomp carries
it alone.** That is the correct disposition of a seam finding and it closes the loop I opened.

## WHAT I DID NOT VERIFY (declared)

- **I re-derived NO instrument in this run.** I5–I9 stand as COO's measurements with their printed
  denominators. My P1 rests on a source read I performed **earlier tonight for PERFRP**, on the same
  portal files — cited, not re-run.
- **Check 8 is a question, not a measurement.** I did not probe the ADVI publisher's deploy mechanism.
- **I did not sweep STITCH or D1 for the same bundle-oracle string**, and the cross-project
  propagation finding above is therefore a hypothesis about those two, not a measurement.
- **Four Tier-2 instances for one project** (`Q-i4`) is surfaced by COO to CTO/MSTR, correctly not
  assumed, and is not mine to rule.

— `3.0.0_SA_CVO`
