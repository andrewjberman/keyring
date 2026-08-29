# /self-drive D2 & D3 — tick 12 (2026-08-28 17:21Z → 17:36Z) — state: ARMED

Covers tick 12 (tick 11 logged @92e91fb4d4). Cron bde882a4 (:07 mark passed mid-act; tick ran on
idle at 17:21Z, held mid-tick by MSTR's leg-2 merge window). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO`
(:22/:52). Written on DELTA: one RESERVED card surfaced at Andrew, one HELD ledger row, row 12
consumed, a leg-2 merge landed across both fabrics, six lane reports absorbed.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs **28**
(D2 21 — +1 = ADVI_INSURE.TO-A3-AE; D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342,
0 claimed-not-member.

## Calls (§1-2)

**ONE RESERVED card, surfaced at this terminal (Andrew's) this tick — see the card below.**
Classification: RESERVED by citation (NEVER class — vendor egress beyond his stated word), not
adjudicable; COO REC = GRANT, CTO concurs. `3.0.0_SA_CVO` (base) NOT LIVE → the reserved-claim
review is HELD as ledger **row 13** (`state: HELD`), the artifact a respawned CVO reads; the base-CVO
spawn is COO's act. Zero ADJUDICABLE calls. The ALL-RESERVED tell fired on a queue of one and was
re-run: the citation test passes on the card's own record (verified at source this tick, below).

## Verdicts / rulings since tick 11 (§3)

- **Row 12 CONSUMED by COO — EXECUTED 3 of 3:** INS-a-5 issuer amendment + `ADVI_INSURE.TO-A3-AE`
  cut @80734ba4cf (5 ACs / 1 cell; **decomp cert PENDING on a dark CVO** — COO's "alt base CTO" would
  be this seat certifying a cell it ruled: refused on the verifier-is-not-the-do-er line; the fix is a
  live CVO); `0.6.0_AE_PartnerETL` SEATED 16:57:21Z; DS~R's silver-stage design (unblocks 3) filed.
- **0.6.0 FIRST REPORT 78431 (validated at COO):** act (a) @d0f9a8f7e4 LOCAL — 5/5 arms incl. a RED
  arm and a pre-fix control (KeyError at HEAD bytes); Rule-20 read on the graph plane corroborates
  the no-invoker finding independently (9 downstream IAM/S3/secret nodes, 0 invoker edges); the
  pagination defect was the LEG's (total measured then discarded, no consuming loop); **the run path
  did not exist** — `run_insurance_leg` built inside the TO by necessity (consistent with tick 11's
  seam). **Egress-citation CORRECTION, owned here:** row 12 cited the 07-17 reporting grant
  (`.tf:150-155`, "standing for production pulls", scoped "THIS 49F reporting producer only") as
  covering the insurance producer — it does not; the insurance surfaces are sanctioned by the LATER
  08-25 word (@a1e9fbcca7), which is BOUNDED on its own record. That correction produced the card.
- **COO issuer ruling 78446:** (b) GO (deploying the dispatch egresses nothing); (c) lands DISABLED +
  run path fail-closed by env flag (two arms), NEVER#6 ledger closed as a declared terminal state;
  AC4 splits QA-manual (one bounded human-initiated invoke under the 08-25 grant) + SCHEDULED
  (sovereign-gated). TO-A3-AE face amended by COO.
- **COO 78438 — silver-stage idempotence RULED** on this seat's input: keyed on the BRONZE partition's
  CONTENT DIGEST recorded in the silver manifest; same → skip, different → re-convert + supersede in
  place. DS~R BUILT the prep @b85abd66b5 (10 arms from different planted truths; 3 load-bearing
  orderings; pre-regime partitions default SKIP-UNVERIFIABLE with an explicit `--backfill-manifest`;
  dry-exercised live during the hold). DS~R's first-mint answer to MSTR: NOT yet — the deploy target
  resolves to `s3://opal-data-mdpf/code/scripts/silver/` where the script AND its two imports read 404
  (positive control fires); `safe-deploy.sh`'s header omits `assets` while its table maps it —
  declarative drift, flagged not fixed.
- **DS~R 78400/78471:** AC1=PASS transcribed @c833341bab (now ON origin); `commit-gate checked 0 of 2`
  honest-denominator note → obligations row 7 item (h).
- **DE~D:** AC2 discharged on a read render (portal 2b8f7987); Manage Table RULED (CTO 78389 = COO
  78392, one voice): mount on both rendered tables with an inline column list off the existing hook —
  executing the frozen spec, not amending it. **Portal DEV PUSHED by the integrator** (MSTR 78440):
  origin/DEV 57701d5c → 9957410e, DE~D's 9 commits published; workspace gitlink follows.
- **AE~G:** DONE, release (b) at COO's call; COO drained its inbox residue (dead-agent cleanup).
- **Leg-2 merge (MSTR 78401/78417):** origin/CLOUD → 8eec9f0b30 (merge cd412f47d1, 294 site-Z + 37
  laptop; XXX.md CTO row OURS incl. CTO~X's 60m cadence); 2 mdpf gold deployed (measured at S3), 3
  first-mint skips (DS~R's silver script among them — see above), 2 `.tf` incoming unapplied. MSTR
  banked its own instrument class (incoming set = `merge-base..THEIRS`). All six of this seat's
  commits ON origin (ancestry after fetch). A later window moved origin again (@f814126b59 per DS~R
  78471 — read at commit time below).
- **Campaign (~L 78419):** both ledger commits ON origin; **40 of 534** ARTIFACT-COMPLETE at
  17:18:37Z, 0 non-complete rows, driver pid 1168780, 37 dates in 72 min (ahead of plan); pushed
  vintage correct-and-behind by design.
- **Out of scope, recorded:** MSTR routed a comp-system 06 regen here (78425) then RETRACTED on
  Andrew-direct at the MSTR terminal, VERBATIM *"No base cto does not need to be dealing with
  comp-system work"* (78428) — MSTR's record; this seat's scope stays D2 & D3. `1.0.0_SA_CTO~D`
  appeared on the roster (Andrew-direct separate project, no fabric engagement).

## Round-bank classes banked this tick (to `3.0.0_SA_CVO` when live)

5. A relayed grant citation inherited by two rulings (row 12 → TO-A3-AE face) was wrong about its
   SCOPE; the executor read the grant at source and found coverage from a different, later, bounded
   authority. A relay of an authorization carries its scope or carries the caveat.
6. A completeness signal MEASURED and then DISCARDED by the producer (`_denominator_for` rendered the
   server's total into prose; nothing consumed it) — the datum was never missing, the consuming half
   was (the CLAUDE.md §4 "consuming half is the whole mechanism" class, on a pull).
7. Idempotence keyed on an OUTPUT's existence proves only that something was converted, never from
   what; key on the input's content digest and record it in the output's manifest.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

**1 (new this tick):** standing daily vendor egress for the 49F insurance bronze leg — card below;
ledger row 13 (HELD).

state: ARMED · push state of this log: LOCAL at write (origin/CLOUD read at commit time)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · `git show --name-only` +
  grep on the 08-25 record and `sed` on the `.tf` (Read-class, Rule 21 rail) · `git ls-remote` +
  `merge-base --is-ancestor` (six commits, after fetch) · ledger append with byte-prefix assertion ·
  `get_live_agents` (13 live; CVO base absent). Mechanics note: a `cd` in one Bash call persisted
  into the next and broke two relative reads (`.tf` "No such file") — returned to the root with an
  absolute `cd`; relative paths after any `cd` are a trap this seat now avoids.
