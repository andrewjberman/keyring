# ANDREW-DIRECT 2026-08-25 ~01:1xZ — PERFRP: BUILD IT OUT, DEV ONLY, NO PROD PROMOTE UNTIL VERIFIED END TO END

**Received at:** `0.7.0_AE_CloudOps~G` terminal (this seat, directly — he was answering my
`/open-calls` CALL 1 and the `/next-steps` set).
**Recorded:** 2026-08-25T011327Z. **Broadcast:** same turn, to COO + CTO + MSTR + the two peer
PERFRP lanes.
**Channel:** direct at this terminal. **Not a relay** — I am the receiving seat.

---

## VERBATIM

> "Yeah we do want to build this out but it needs to stay on the DEV branch not promoted to PROD
> until we know the data pipeline and all underlying data is verified end to end."

**Quoted exactly. Not paraphrased. The phrasing is the ruling.**

---

## WHAT PROMPTED IT

My `/open-calls` CALL 1 (00:22Z, restated 01:08Z): *ship PERFRP round 1 with two of the five v1
cards non-functional — (a) proceed as ruled, or (b) hold round-1 serving until the inputs land?*

- Transactions: no data source in round 1 (serving deferred; his own s.11 #6 forbids the round-1
  entity-keyed map form — *"per-relationship, PAGED, never a firm-wide dump"*).
- Performance: computes nothing for 100% of accounts on current data — `twr_daily`'s refused
  partitions carry **9 columns not 13**, with `bmv/emv/cf_net/cf_gross` absent, so the returns are
  not merely null but unrecomputable downstream.
- And, surfaced with the restatement: **nobody owns the `twr_daily` fix** — CVO declined it as out
  of scope (*"I read artifacts, not c02"*), DS~G called it upstream.

My REC was **(a) proceed**, conditioned on the ownership gap being routed.

---

## WHAT IT BINDS — SURFACED, NOT ADJUDICATED

**Three things are plain on the face of his words. I am not narrowing or widening them.**

1. **BUILD IT OUT.** *"we do want to build this out"* — CALL 1 is ANSWERED as **(a) proceed**. The
   two non-functional cards do not stop round 1. Work continues.
2. **DEV ONLY.** *"it needs to stay on the DEV branch not promoted to PROD"* — a PROD-promote hold
   on this work, stated by him, at this terminal.
3. **THE LIFT CONDITION IS NAMED.** *"until we know the data pipeline and all underlying data is
   verified end to end."* The hold lifts on that condition and no other.

⛔ **THIS IS HIS GATE, NOT A MANUFACTURED ONE.** CLAUDE.md's no-inferred-gates rule bans an agent
creating an approval step from precedent, prudence or process symmetry. This is the opposite case:
the sovereign stated the hold himself, in his own words, unprompted by any proposal of mine. It is
recorded because it binds, not because it was inferred.

## WHAT I AM DELIBERATELY NOT DECIDING

**The scope of "this" and of "verified end to end" is HIS, and I am not resolving either.**

- **How wide is "this"?** He said it answering a PERFRP question, so PERFRP is certainly in. Whether
  it reaches the wider 49F ADVI serving surface is **not stated** and I am not extending it. If a
  lane needs that answer, ask him — do not infer it from this record.
- **What counts as "verified end to end"?** Not defined here, and I am not defining it. It plainly
  concerns *"the data pipeline and all underlying data."* Whether the `twr_daily` BMV gap alone
  satisfies it, or whether it wants a broader chain-to-card verification, is his call or the PRD
  author's on his behalf. **A seat that decides this on its own has adjudicated a sovereign
  condition.**
- **Relationship to the existing 49F switch hold.** My TO's authority section already says PROD
  exposure rides the 49F switch promote, and that switch is separately HELD on Mike at 49 Financial
  (Andrew-direct 2026-08-24 ~15:2xZ). **Whether these are one hold or two independent ones is not
  stated.** Treat them as independent until he or CTO says otherwise: satisfying one does not
  release the other.

## WHAT DOES NOT CHANGE

- **Rule 19 stands unchanged** — the portal main worktree lives on `DEV` always; this is not a new
  mechanism, it is a hold on the promote act.
- **PROD promotes are a DT lane** (`/prod-deploy`). This was never my act to perform, which is
  exactly why the record and the broadcast are the whole of my obligation here.
- **My TO's scope guard is untouched:** no new schedule, no new trigger, no alarm/SNS/monitor, no
  shadow prefix, no comparator.
- **The round-1 rulings stand:** one object per family (no fan-out), 11 registry entries with 10
  emitting, Transactions carrying `deferred` honored by construction, the projection staged AFTER
  the c04 battery (fail-closed).

## WHAT I DID THIS TURN

1. Recorded this file verbatim and committed it under my own author line.
2. Broadcast to `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR`, and the two peer PERFRP lanes
   (`0.4.0_DS_ClientPlatform~G`, `0.4.0_DE_ClientPlatform~D`) — the promote path crosses their work,
   and DT owns the act.
3. Routed the `twr_daily` ownership ask to COO — **as a route, explicitly NOT as a hold.** He said
   build it out; the ownership gap is a thing to assign in parallel, and treating my own
   recommendation's condition as a gate on his instruction would be the exact inversion the
   no-inferred-gates rule forbids.

## STATUS OF MY OWN CELL, UNCHANGED BY THIS

Start condition (DS~G's first local PERFRP leaf emission) still UNMET. AC5 PASS, proof instance
VALID rc=0. Nothing built, no criterion flipped, no infrastructure touched.
