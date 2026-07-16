# A4 Wave-3 executed L0/L1/L2/L5 + F-AMT defect chain + WP7 purpose amendment -- one window, three sovereign rulings folded live

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-16 12:46Z -> ~16:35Z
**Session:** reinstantiation off the 12:2xZ handoff; watcher re-armed clean (found pair was
/clear-carryover, identity-probed before kill); A4 cut received 131113Z, GO on receipt.

## Legs landed (commits pushed through b7dd2a231; two gate-bearing pushes + batched locals)

1. **L0** (7760bfcf5): casebook ENTRY 5 draft -- B_00 DELETED OUTRIGHT, full-source 1,355L,
   R1-R5, line-cited. Owned-paths gate correctly blocked my direct casebook write (ANY_CTO
   lane) -> WAVE3_SPEC precedent (lane drafts, CTO folds). CTO fold pending. Self-caught:
   the blocked attempt left the edit STAGED in the shared index -- unstaged before push.
2. **L1** (64c7fa7dd): C_00.account_gains -- G2 identity, daily-atomic re-grain, NNA core
   IMPORTED from c03 (never copied). ACCEPTED. Estate measured first: dim_position has no
   market_value; the column is market_value_settled_unsettled (refuse-loud).
3. **F-AMT** (95b966545): the dry-run discriminator caught ALL-ZERO flows on 1,166 rows ->
   grounded at feed: net_amount is TR-only; flow dollars live in gross_amount; direction is
   debit_credit (FI=100%cr / FO=100%db controls; TA/DV/FE run BOTH ways -- the seed's
   class-implied signs proven wrong). STOPPED on CTO's surprise clause; design approved;
   fix + both-branch fixtures + flows-nonzero-when-feed-nonzero guard in both runners;
   **C_03 07-15 RE-RUN in-place -- live nna now real** (nna_cash $882,990.60 ties feed to
   the cent; growth residual $2.93M -> $2.04M). CTO: machinery acceptance stood, data
   acceptance reopened + re-closed on the re-run.
4. **L2** (local -> rode b7dd2a231): C_02 w/ M1-AS-SIGNED IN CODE -- C_04 gate in-process at
   emit (skippable-gate refused), degenerate floor verbatim float(v)>0 no hold-last-good,
   cross-contract tie to the cent. Runner refuses until C_01 exists (exercised).
5. **L5/WP7** (708ff97f7 + amendment b7dd2a231): TEN converters (seven per TO + three dim
   builders the estate surfaced) re-pointed 01_raw -> monolith bronze; nested-zip
   double-unzip AT READ (measured: outer -> one inner zip -> one CRS text; one-member-or-
   REFUSE). Exercised: trn/20260715 = 1,166 rows ties monolith dim_transaction exactly.
   **Lineage grounded on bytes:** 01_raw == 0824 delivery exactly (two eras) -> store
   history 0824-fed, REPLACEMENT-not-continuation; seed-vs-port identity re-framed
   within-master. **Purpose amendment (Andrew via 0.6.2: 0833=ADVI / 0824=MP):**
   PURPOSE_MASTER map + master_for() refuse-on-unknown; DEFAULT MASTER DELETED from the
   lib; consumer-anchored purpose per converter (all ten ADVI->0833 via the A1-contract
   trace). COO gate CLOSED ("you made the defect impossible instead of currently-absent").
   0.5.0 deploy leg validated same-hour (13/13 imports, live dry-run from their box).

## Sovereign rulings folded (recorded verbatim + broadcast same turn, each)

- acabb3553: canonical-prices schema unnecessary on RPS holdings; transaction-based pricing
  DEPRECATED; transactions stay for NNA -> CTO amended A4 (d1ff2dfb0: L3 retired-with-
  replacement, L4 records retirements); M4-supersede committed for CTO @ a04bcbcd4 (md5 pin
  verified byte-exact first).
- 60fb1ad56: the A4 premise -- same D-input outputs (portal parity), refactored path on
  0833 facts, incremental-daily over full recompute.
- Push binding (15:43Z via COO): batch-and-push-at-package-close honored; both pushes this
  window were gate-bearing under the binding's own clause.

## Compiler Tools

comp-glob/comp-grep (casebook + consumer censuses, on-rails) | comp-pipescript io B_00 =
EMPTY manifest (dynamic keys; the Entry-5 review IS the manual review, A1 precedent) |
commit-gate 19 files PASS (1 ruff block fixed at source, 1 unused-import caught) | pytest
64/64 | rail-checked raw reads: partition schemas (pq.read_schema), sb/debit_credit value
censuses, zip member inspection, three-way lineage row-universe ties -- each marker states
why no comp-tool fits (parquet/zip value-level reads). Gap noted: no comp-tool reads
parquet schemas or zip members; recurring rail-checked class this window.

## Next (in lane)

L5b: conv-seven 0824 re-point (purpose=model_portfolios; kills the local-OneDrive TRN
quirk; bridge-retirement clock starts on its close) -> L4: C_01/G4 port + G->C casebook
map -> L3 spec lines -> seed-vs-port identity (within-master) + profiling to Andrew's
rust/polars cell. Partition watch armed (date=2026-07-16, alarm 10:15Z, expiry 12:00Z);
tomorrow ~09:46Z = daily runs + WP7 cycle-1 verdict.
