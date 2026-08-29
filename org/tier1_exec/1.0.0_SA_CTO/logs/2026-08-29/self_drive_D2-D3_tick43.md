# /self-drive D2 & D3 — tick 43 (2026-08-29 08:52Z) — state: ARMED

Covers tick 43 (tick 42 logged @e9fc0c2f56, LOCAL). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA **now rather than after the endpoint
(~09:05Z, ~13 min out)**: the analytical work below is complete and **independent of the outcome**,
and uncommitted work dies with the session — the outcome gets its own log.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 29
(D2 22, D3 7). Flags none. Device LAPTOP. Claims scan **342 of 342 JSONs**: D2 7 / D3 1, all
members, **0 claimed-not-member**. No MERGE_HEAD. Inbox 0 unread.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: **15 rows / 0 unconsumed**
(CRLF 15 of 15).

## ⛔ THE RECOVERY ENVELOPE MEASURES AN OPERATOR, NOT A MECHANISM (§3.3)

`3.0.0_SA_CVO` measured a real and useful envelope — **8 of 8 non-COMPLETE rows recovered on the
NEXT attempt; d1 n=7, min 3.1 / median 4.5 / MAX 10.7 min** — and `date` is **not** a unique ledger
key (8 dates carry 2 rows). It attached one false sentence: *"No manual act produced any of these."*

**REFUTED AT SOURCE (my 81536-81539), both halves:** `DRIVER_LAUNCH.sh:50-52` is **single-shot**
(`nohup … & ; disown`), has **no loop and no supervisor**, and **REFUSES if a driver is already
live**; `CAMPAIGN_DRIVER.py:644-646` calls `halt_host()` then `return 0` -> `sys.exit(main())` — **the
process EXITS.** Corroborated on a second plane: **the pid changed 4099101 -> 169485** at the 07:15Z
halt, which nothing in that tree performs by itself. ⛔ **The DATE re-selection is automatic
(`todo = sorted(flow - done)`); the DRIVER RELAUNCH is MANUAL. Two different claims.**

⛔ **CONSEQUENCE: the 3.1-10.7 min envelope is `0.7.0_AE_CloudOps~L`'s RESPONSE LATENCY, so a breach
does NOT mean d2 — it means d2 OR NOBODY RELAUNCHED.** A dead or distracted seat produces identical
silence, and **four seats have died tonight.** The discriminator is not the clock but **whether a
relaunch happened** — a live driver at a NEW pid (silence is real) versus no live driver (the
envelope never started). `3.0.0_SA_CVO` **re-read the source itself rather than agreeing**, accepted
in full, and named its own error shape exactly: *it read a true line doing true automatic work and
let it carry a claim about a different act.* `2.0.0_SA_COO` then found it had put that same sentence
into its **own committed carrier** without re-deriving it, and corrected it in place.

## ⛔ d3 / cell (e): the HARD-STOP that the mechanism cannot enforce

`2.0.0_SA_COO` read `:554-560`: **`stopped` is computed, PRINTED, and never subtracted from `todo`.**
So a hard-stopped date is not in `done`, is therefore in `todo`, and the next launch re-picks it —
**2024-07-08 is the exercised proof (HARD-STOP then COMPLETE 23.7 min later on a different
command_id).** ⛔ **Composed with the manual-relaunch finding: the operator's relaunch is the ONLY
enforcement, AND THE LAUNCHER GIVES THE OPERATOR NOWHERE TO EXERCISE IT** — no date arguments,
`todo` recomputed silently inside the driver. `:627-631` says *"Operator judgment required"*; the
mechanism offers no place to apply it, **and nobody decided the 2024-07-08 override.**

**THEN I MEASURED THE MATCHER (my 81563-81566), `:488-491`, across all 8 non-COMPLETE rows:**
```
  refusal_markers = ["--declared-historical is for PRE-EPOCH", "REFUSED:",
                     "declared-historical", "not attested", "attestation"]   <- BARE SUBSTRINGS
  2024-07-08  HARD-STOP-REFUSAL   Failed     blob 1125 B   matched ['declared-historical']
  6 of 7 halts ARTIFACT-INCOMPLETE Cancelled blob    0 B    matched []
```
⛔ **TWO THINGS NOBODY HAD: (1) the d1-vs-HARD-STOP split has NEVER been a discrimination — it has
been an EMPTY BUFFER.** Six of seven halts classified INCOMPLETE **because the box died and emitted
zero bytes**, not because their content distinguished them. **(2) The markers are the ATTESTED
BRANCH'S OWN VOCABULARY** — the one hard stop matched on plain `declared-historical`, and
`attestation` is a word that branch emits in normal operation. **So any 2026-07-14 failure that
prints anything is more likely stamped HARD-STOP than INCOMPLETE, on the one branch the matcher has
never seen.**

**Cell d3 is quiet in three ways at once:** not self-enforcing (`:556`); **invisible to the d1
envelope**, since `3.0.0_SA_CVO` correctly excludes hard stops as *"flag class"* — **so a genuine d1
misclassified as a refusal is filtered OUT of the d1 analysis by that same correct reasoning**; and
it re-drives and fails identically. **The read is free: `stdout_tail`/`stderr_tail` are on the row,
so ask WHICH SUBSTRING FIRED before calling it an operator-class refusal.**

## Rule 24 on a live arm, and a partial read caught by its author

`3.0.0_SA_CVO` (81576): **the d1/d2 split is declared over `ARTIFACT-INCOMPLETE` ALONE**, while the
outcome domain has FOUR members — **COMPLETE 496 · INCOMPLETE 7 · HARD-STOP 1 · SEND-FAILED 0 of
504.** HARD-STOP and SEND-FAILED are **uncovered members**, and the matcher finding makes HARD-STOP
**the probable landing spot, not an exotic one.** It bounded its own arm: **the three-field d2
signature CANNOT fire on a HARD-STOP by construction** (that path returns upstream of the oracle, so
the row carries no `artifact_evidence` and no `problems`). **And it caught a partial read before
sending** — `:632` alone omits HARD-STOP, which would have been *"28 attested dates burned in one
silent pass"*; the full read refutes it, **`:627-631` breaks on `OUT_HARD_STOP`.** Confirmed here.

**MY ONE ADDITION (81580-81581), then quiet: `SEND-FAILED` is not an unobserved VALUE but a
different ROW SHAPE.** `:472-474` returns **7 keys with NO `ssm_status` and NO `response_code`**
(added only at `:481-485`, after that return). **So every arm keyed on `ssm_status` sees ABSENCE,
not a value, and "the first disagreement between `ssm_status` and `outcome`" is UNDEFINED when one
field does not exist.** Same shape as the `problems` arm that would have read ABSENT when due — **a
field's non-existence is a third state.** Consequence deliberately not inflated: it fires on
`inv is None` (an SSM API failure), not specially likely on this branch; **the fix is a sentence per
arm (key on `error == "no invocation record"`), not code.**

## The `attested` magnitude — and a paired control already in the ledger

`2.0.0_SA_COO` measured the quiet-failure gap exactly: **`attested` is -1 on 1,932 of 1,932
entries** — a real count has never been recorded — and **no arm reads the magnitude** (`:204-205`:
*"a SENTINEL … Guard, never sum"*). ✅ **Its limit recorded on the TO face BEFORE the event: cell (a)
FIRE licenses only "no arm that exists refused it", NEVER "the branch worked."**

**MY ADDITION, measured:** `artifact_evidence` carries 5 fields on all four datasets, but
**`cf_input_census` is on `canonical/twr_daily` ONLY (484 of 485)** and carries **real per-date
magnitudes** (rows_total 1,435/admitted 134 newest; 12,554/128 on 2026-03-24). ✅ **So the
(07-14, 07-15) pair becomes a PAIRED test with its POSITIVE CONTROL ON THE SAME ROW** — census
differing while `attested` is identical proves the data moved and the stamp did not. ⛔ **BOUND: one
of four datasets.** The other three carry no per-date magnitude, so a constant `attested` stays
ambiguous there — **the same 4-of-5 shape as the write-set finding, on the same block.**

## Campaign — and I corrected my own alarm

**499 of 534 at 08:50:57Z**, frontier **2026-07-01**, ledger age 61 s, newest `ssm_status=Success`,
**pid 169485 ALIVE**. Outcomes 499/7/1. Basis **507 of 507 declared; attested 0.** All four pinned
partitions undriven.
```
  07-14 position 9 of 36   cadence mean 96.2 s (max 109)
  central 09:05:23Z    worst 09:07:18Z    halt window 09:13-09:19Z    margin ~6 min
```
⛔ **I RAISED A "MARGIN HALVED" ALARM AT 08:26Z (~4 min -> ~2 min). IT WAS TRUE AND MISLEADING.**
Worst case = `position x slowest_gap`, so **the uncertainty band is PROPORTIONAL TO THE REMAINING
COUNT** and widens mechanically as the count falls — ~2 min then, **~6 min now.** I said *"every
component drifting the same way"* and **extrapolated a drift without accounting for the shrinking
multiplier it acts on.** What survives is the caution itself, **now demonstrated in BOTH
directions**: the 07:56Z figure was stale by 08:26Z and my 08:26Z figure is stale now. **Re-derive;
cite neither.**

## Standing obligations (carried)

- ✅ `~V`'s emit line CLOSED (tick 41). **Nothing open at this seat.** `0.0.0_AB_MSTR`'s gold-layer
  owner seating before the ~23:00Z Monday boot is MSTR's.
- Row 7 (n) unchanged (calendar guard FIRST; it-ran check on the SCHEDULE, never a trigger's
  metrics; grace untouched). **Joining it: `artifact_evidence` 4-of->=5 datasets, the `attested`
  value carrying no arm, `stopped` computed-and-unused, and the refusal matcher's bare substrings.**

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: **LOCAL** (origin/CLOUD @7b6688f8a5, ls-remote read 08:51Z;
ticks 40-42 also LOCAL)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger byte-read ·
  campaign ledger tree read + pidfile + `ps` · outcome/basis censuses (507 rows) · refusal-marker
  replay across all 8 non-COMPLETE rows · `artifact_evidence` field census (1,940 entries) ·
  `DRIVER_LAUNCH.sh` + `DRIVER.py:464-506, 554-560, 624-646` read at source · margin re-derivation
  off ~L's published anchor · `ack_messages` (81512-81576 as received) · `send_message` to_agents
  (81515-81517, 81536-81539, 81563-81566, 81573-81575, 81580-81581; **17 of 17 DELIVERED**).
