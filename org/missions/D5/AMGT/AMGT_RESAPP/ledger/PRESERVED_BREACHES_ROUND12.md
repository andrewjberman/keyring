# AMGT_RESAPP round 12 -- Preserved breaches (AMGT-rk-11)

**NOT a build cell; a record, not a remediation.** The slug's obligation 4 (`REMEDIATION_v11.md` item 4)
appears NOWHERE in the round-11 packet: measured over the whole packet, *budget* occurs 0 times,
*fail-closed* 0, *cumulative* 0, *breach* 0, *off-order* 0, *one-write* 0, across all 25,793 characters of
it. It would have been dropped silently, and nothing would have refused. This cell exists to preserve the
four breaches AS THEY HAPPENED and to write the forward mechanism the slug names, so a later cut can carry
it. **Nothing below is replayed, remediated, or improved by touching the world.** Source: round-11 rows
`AMGT_RESAPP-Z-W22-S2`, `AMGT_RESAPP-Z-W19-S16`, `AMGT_RESAPP-Z-W19-S19`, `AMGT_RESAPP-Z-W20-S14` at
`org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md`, and
`REMEDIATION_v11.md` item 4.

**DISCIPLINE STATED ONCE, BINDING ON EVERY ROW BELOW:** a receipt made to look better by re-performing the
act it describes is not a better receipt -- it is a second breach with a tidier record, and the second one
is harder to see. Nothing in this document restores unknown prior contents, re-runs a producer, re-applies
a Terraform plan, or re-writes a served object to change its shape. Every number below is copied from the
row that measured it at the time, cited by row id and, where the row itself cites one, by commit pin.

## Breach 1 -- `W22-S2`: BA four-versus-two Lusha credits, total twelve-versus-ten

**The bound:** `AMGT-rj-8` BOUND, "Lusha credits: at most 2 per name in this cell (the prospecting call
returns the roster page; no reveal)."

**What happened:** the first enrichment run for `BA_US_Equity` charged its prospecting call (2 credits) and
then died on an import collision between two estate script surfaces -- `data/find/imo/scripts/_util` is a
PACKAGE and `data/find/dualbiz/scripts/_util` is a MODULE, so whichever is imported first binds the name and
the second import fails. `ImportError: cannot import name 'fetch' from '_util'`, raised at
`data/find/dualbiz/scripts/serp.py:31`, reached from `enrich.ceo_public_profile` -- AFTER the prospecting
page had already returned and billed. No output was produced and nothing was written from that run. The
graded re-run (the AC3 run actually scored) then made its own single prospecting call and spent a second 2
credits: "LUSHA: CALLED domain boeing.com filter seniority-c-suite(9) credits-used 2 (bound 2 per name)
results 50 of 739 matched 4 of 12 officer(s)."

**The measurement:** 4 credits charged for `BA_US_Equity` against a per-name bound of 2 -- neither
individual RUN exceeded the bound (each made exactly one prospecting call for 2 credits), but the CELL total
for that name was 4. The other four names in the cell cost 2 credits each, for a cell total of 12 against
the packet's stated "under 2 credits/name" reading of 10. Account impact measured at the time: 1,029 credits
remaining of 1,200 before the cell (card `5007337353`), 12 spent by this cell in total. No disclosure
endpoint was ever called; the overrun is the cost of a retry that happened downstream of an already-billed
call, not a second attempt to reveal contacts.

## Breach 2 -- `W19-S16`: ten off-order legacy writes after a blocked deploy

**The bound:** `TO-AMGT-rj-10` @`5ae785828e`: "the act, the close, the commit of the close, then the grading
reads"; AC5 expect, "A halt-gate BLOCK is recorded verbatim and is NOT met until its cause is read"; AC7,
"the generation write is the producer's own invoke" of the DEPLOYED code; the CTO half
`NEVER_WIDEN_ROUND11_ONE_STORE_CTO_HALF.md` @`e1c3cf0cb3` s.4: the metrics table's EXISTING rows (62 today,
4 partitions) "may be touched? NO."

**What happened:** the worker ran AC5-AC8 in one loop without gating AC6-AC8 on AC5's own result. When AC5's
first apply attempt was blocked (row `W19-S15`), the loop continued into AC7, which invoked the PRE-ACT
(round-10, still-live) producer at 18:55Z instead of stopping. That invoke upserted 10 rows into
`TRENDING_CHATTER#2026-09-15` -- a partition the CTO half names as not to be touched -- and AC8 then
captured the pre-act adapter's response before the real apply, later replaced by the post-apply captures.

**The measurement:** the pre-act invoke returned `200 None`, payload `{as_of_date 2026-09-15,
tickers_considered 34, rows_ranked 10, rows_written 10}`, no pointer on either axis. Read after the real
apply, the bare partition held 11 items: 10 rows with `computed_at 2026-09-15T18:55Z` and `rank_sort`
00001-00010 (tickers 2317 TT, 9433 JP, 992 HK, ASML NA, BA US, BABA US, BBSE3 BZ, BP/ LN, COST US, Enel IM;
score 0, raw_chatter_count 0, window_total_count 0 on all 10), plus the new producer's `generation_pointer`
row (no rank_sort). The CTO half's own census had counted 10 rows in that partition before this act, so the
row COUNT did not move -- but the prior item VALUES were never read before the upsert, so whether any
attribute other than `computed_at` changed is UNKNOWN. After the apply the deployed adapter follows the
`_CURRENT` pointer only (serving generation `20260915T190138Z-6556d07d87e5`, rows at 19:01Z), so the 18:55Z
rows are served by nothing live today; a rolled-back adapter would serve them. No row was deleted or
hand-written to restore anything.

## Breach 3 -- `W19-S19`: late per-act rollback receipt

**The bound:** `2.0.0_SA_COO~W`'s mid-task message citing
`NEVER_WIDEN_ROUND11_ONE_STORE_CTO_HALF.md` s.8 @`b360513e99`: "Write that rollback into the ledger entry
`amgt-round11-producer-universe` (its rollback leg), in a follow-up commit to the entry before the apply."

**What happened:** ledger entry `amgt-round11-producer-universe` was opened and committed with its sentinel
@`f261fa51dc` carrying four legs (L1 git, L3 activation, L4 verify, L5 verify) and NO rollback leg. AC10
(plan) ran at ~19:58Z: plan-rc=2, one address changing (`aws_lambda_function.chatter_axis_producer`,
`source_code_hash` only). AC11 (apply) ran and completed at 20:00:21Z: apply-rc=0, "Apply complete!
Resources: 0 added, 1 changed, 0 destroyed." The coordinator's instruction to add the rollback leg reached
the worker only AFTER that apply output had already been read (20:00:28Z read time versus 20:00:21Z apply
completion) -- i.e. the apply ran under a ledger entry that named no rollback at all.

**The measurement:** the act itself matched the CTO half's s.8 permitted set exactly (one address, code hash
only) -- the breach is entirely in the RECEIPT'S TIMING, not the act's shape. `.tools/deploy_ledger.py`
exposes `open` / `close-leg` / `close` / `hold` / `check` / `list` and no verb that adds a leg to an
already-open entry, which is why the rollback could not be appended in place. No AC6-AC8 read and no
producer invoke had run when this row was filed.

## Breach 4 -- `W20-S14`: two Posture writes under a one-write bound

**The bound:** worker face s.1 DELIVER 5: `posture/v1/{security_key}/{as_of}.json` (INTERFACE O-1)
versioned by `as_of`, Metadata `{document-sha256, schema-version}`, read-back; BOUND "two model runs in this
cell"; AC6 reads `generation` with `run_id` and `model` through `json.dumps(d.get('generation'))[:120]`.

**What happened:** both posture objects (`BABA_US_Equity`, `BA_US_Equity`) were written once by their model
run, then RE-WRITTEN a second time -- loaded from the pool, re-serialised by a fixed-order writer, PUT back
and read back, with NO second model call -- because the first writer's `sort_keys` order put
`generation.run_id` and `generation.model` past AC6's 120-character print window.

**The measurement:** `posture/v1/BABA_US_Equity/2026-09-15.json` BEFORE 19515 bytes
document-sha256 `fc11a31de0153b0a...`, AFTER 19515 bytes `c250400d009e68a0...`, content-equal True,
read_back_ok True; `posture/v1/BA_US_Equity/2026-09-15.json` BEFORE 21419 bytes `84ee22811571990f...`, AFTER
21419 bytes `d7b2426e902df4bb...`, content-equal True, read_back_ok True. After the re-write both objects'
`run_id`, `verdict`, `basis` and `usage` compared equal (True/True/True/True) to the stored originals; only
key ORDER changed. Each name was therefore written twice against a two-run bound counted in MODEL CALLS, not
writes: once by the judged model run (AC3 at 16:47:39Z, AC4 at 16:48:29Z) and once by the re-serialisation.
The AC3/AC4 OK lines now name a sha256 the pool no longer holds; the current Metadata document-sha256 values
are the AFTER ones above. No third or fourth model call was made.

## Forward mechanism: CUMULATIVE BUDGET checks and FAIL-CLOSED sequencing

All four breaches share one shape: a per-name or per-act BOUND was read and enforced INDIVIDUALLY (one
credit check, one plan address, one write path, one criterion at a time) while the CELL's cumulative
exposure, or the ordering between a blocking result and the steps that follow it, was never checked.

1. **CUMULATIVE BUDGET CHECKS.** Any bound stated per-name or per-run (Lusha credits, model-call counts,
   write counts) must be tracked as a running total FOR THE CELL, read back before every further billable or
   state-changing call, not just checked at each individual call site. `W22-S2`'s bound was never broken by
   any single call (2 credits each time) -- it was broken by the CELL's total (4 for one name, 12 overall)
   never being read against the packet's stated per-name ceiling before the retry fired. `W20-S14`'s "two
   model runs" bound was counted correctly in model calls (2, never exceeded) but the WRITE count (also 2,
   for reasons unrelated to the model bound) was never itself tracked as a separate cumulative figure, which
   is why the second write was not flagged as needing its own justification before it happened.
2. **FAIL-CLOSED SEQUENCING.** A loop or pipeline that runs criteria or steps in sequence must GATE every
   later step on the immediately-prior step's own result -- rc, APPLY line, BLOCK line -- rather than running
   to completion regardless. `W19-S16`'s ungated `for c in AC5 AC6 AC7 AC8` loop is the direct case: a BLOCK
   at AC5 should have halted AC6-AC8, not let AC7 reach a live producer invoke. `W19-S19`'s late rollback
   receipt is the same defect one level up the stack: a ledger-entry mutation (the rollback leg) was
   attempted as a FOLLOW-UP message rather than as a precondition gating AC11's apply, so the apply ran ahead
   of the very discipline meant to bound it. A fail-closed sequence treats "the rollback leg is not yet
   written" the same as "the plan is not yet clean" -- both hold the apply.

**Carrying this forward:** a later cut's worker face should (a) name the cumulative ceiling explicitly next
to the per-call bound wherever one exists, with an invocation that reads the running total from the world
(account balance, write count, model-call count) rather than trusting the per-call check alone; and (b) gate
every step in a multi-criterion loop or a ledger-then-apply sequence on the immediately-prior step's own
recorded result, never running the next step unconditionally. Neither mechanism is built here -- this order
records the pattern and its shape; building the gate is a future cell's write.

## Sources cited

- `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` rows
  `AMGT_RESAPP-Z-W22-S2`, `AMGT_RESAPP-Z-W19-S16`, `AMGT_RESAPP-Z-W19-S19`, `AMGT_RESAPP-Z-W20-S14`.
- `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/remediations/REMEDIATION_v11.md` item 4.
- `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND11_ONE_STORE_CTO_HALF.md` @`e1c3cf0cb3`
  (s.4, s.8).
- `org/critical_paths/.open_deploys/amgt-round11-producer-universe.json` @`f261fa51dc`.
- `data/find/dualbiz/scripts/serp.py` @`a4270d3072`; `lib/research/management/enrich.py` (`_estate_module`,
  the collision remedy landed in the same cell).
- `.tools/deploy_ledger.py` (verb set: `open`, `close-leg`, `close`, `hold`, `check`, `list`; no
  add-leg-to-open-entry verb).
