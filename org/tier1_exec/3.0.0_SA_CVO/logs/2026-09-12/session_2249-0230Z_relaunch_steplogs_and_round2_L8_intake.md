# Relaunch after the reboot: the two owed step logs, round-2 L8 intake, and an L4-R re-stamp — 3.0.0_SA_CVO
**archetype:** MIXED

**Date:** 2026-09-11 / 2026-09-12 (UTC)
**Task Order:** none — standing L8/L9/L10 responsibility on IRPT_BCKEND and IRPT_FNTEND, plus this seat's L4-R halves
**Status:** OPEN — both rounds still EXECUTING; nothing closed, no slug cut
**Seat:** `3.0.0_SA_CVO` (BASE, laptop, Claude harness, branch CLOUD)
**Window:** 2026-09-11T22:49Z (register) → 2026-09-12T02:30Z (this log)
**Prior seat log:** `logs/2026-09-11/session_close_0953-1739Z.md` @`b93df1e4a6`

## Objective

Resume after Andrew's reboot under his ~22:25Z direct (*"load up and get /canonical-flow driving for COO~B
(IRPT_BCKEND) and COO~F (IRPT_FNTEND)"*), clear the one paperwork gap this seat had recorded against itself,
and hold the L8 channel intake on both IRPT rounds while the two COO lanes drain.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| PATH rail | the A.3 resolve+exercise pair | 104 of 104 resolve; a forwarder RAN | scored on OUTPUT, not rc |
| `comp-read` | `surprise-watch.sh --enumerate 'STATE_FILE'` | 11 hits, 1 whole | found the absolute-path key at `:63`/`:287-291` |
| `comp-read` | `surprise-row-gate.py --for` (id forms per directory) | self-test `:1706` | decided row PLACEMENT; a C- row in `investigations/` is REFUSED |
| `comp-read` | spine `--for` (L8 output + watermark) | L8 section | gave the exact L8 output contract |
| `comp-find` | `--name 'STEP_LOG*' --files --limit 40` | 28 of 172,979 | located the schema + a CVO exemplar |
| `comp-find` | content mode, `'account\(s\) in scope'` | **TIMED OUT to background** | the known rc=124 trap; switched to native `Grep`, which Rule 21 does not gate |
| `prd-signoff.py` | `status` x3, `sign` x2 | ADMITTED x3 | the gate's own run, not an estimate |
| `safe-commit.sh` | 8 commits | all gated clean | one REFUSED correctly (see below) |
| `safe-merge.sh` | 1 drain | merged index graded, row gate OK | |

## Work completed

### 1. The two owed round-1 step logs — `f2f02e5829`
`STEP_LOG.3.0.0_SA_CVO.round1.json` for both IRPT projects, 14 rows each, 0 schema errors against
`org/standards/STEP_LOG.schema.json`. Written from committed evidence only; no round rerun, no battery
re-executed, and the stale round-1 scratch writer deliberately NOT invoked. `1.0.0_SA_CTO` re-derived both
with a different instrument and closed RAVC (96033).

**Two things the reconstruction measured rather than assumed, both now adopted as policy by the CTO:**
- **Neither L10 slug has a message id and neither can.** `codex-send` delivers OFF-LEDGER; the delivered files
  carry `Sender-unverified` and no `Msg-ID`. Cited as ARTIFACT carriers with the reason in the row. A READ ack
  for either slug is unsatisfiable *by the transport*.
- **Every `org/mcp/inbox/` carrier is untracked, so `@HEAD` on one is a FABRICATED VINTAGE.** The first draft
  carried `@HEAD` on twelve refs. Measured before committing (`.gitignore:248`; `git ls-files org/mcp/inbox` = 0)
  and rewrote all twelve. `git show` on such a path returns clean-empty rather than erroring, so a fabricated
  vintage reads as diligence and fails silently for every later reader.

### 2. Round-2 L8 intake — standing, current
Both channels read in full as rows landed: **IRPT_BCKEND 159**, **IRPT_FNTEND `INVESTIGATION_v2` 38** at this
writing, all undispositioned, **0 ARMED without a `disarm_owner`** on either. Nothing sent — the CVO's one send
is the slug.

**One row named this seat and was discharged: `IRPT_FNTEND-S27` (ARMED, `disarm_owner: 3.0.0_SA_CVO`),
disposition `IRPT_FNTEND-C-S45` @`79561ebb71`.** Re-derived on a THIRD instrument (S27 read the rendered PNG,
`F16-AC8` greps a console line, this seat read SOURCE + FIXTURE) and the finding came out **stronger** than the
row stated: the performance wire payload carries **no `scope` block**, `accountIds` appears **zero times** in the
fixture, so `bundle.scope.accountIds` is defaulted to `[]` and `[].length` prints as a fact. Textbook silent zero
against the PRD's UNAVAILABLE rule — and it constrains the remedy, because there is no field on that route to
re-point the count at.

### 3. L4-R: both ratified-text halves moved onto the bytes — `d930d3c03a`, `ec7af20e09`
`prd_signoff_lib.py:198` falls back to comparing the VERSION STRING when a record has no `half_hash`. Both IRPT
records were on that fallback. Re-stamped; both now carry a `half_hash`.
⛔ **The control is the part worth keeping:** the two hashes DIFFER from each other and NEITHER is
`e3b0c44298fc…`, the sha256 of the empty string. A heading matcher that matches no sections returns that constant
for every half and still writes a record that READS BOUND — a record can be bound to nothing and pass every later
check. Byte-unchanged was verified by BLOB IDENTITY (a different instrument from a half-hash recomputation) with a
positive control from the v0.11-era pin that fires 8/4. `DSGN_REBRND` checked unasked and was already bound.

### 4. Governance: the mechanical-change carve-out — `276f728b68`, addendum `bd7bccfa64`
Position held for the L10 slug at the CTO's routing. A normalized-diff carve-out relocates *"does this change mean
anything"* into a normalizer sitting beneath every half of every PRD at once, and it cannot prove REFERENTIAL
equivalence — so it reads PROVABLY MECHANICAL on precisely the renames worth reviewing. **`1.0.0_SA_CTO` withdrew
the carve-out and adopted the sweep-signature shape** (96048). The slug carries BOTH, the rejected alternative
with its reason, because a record showing only the survivor cannot stop the next seat re-proposing the loser.

### 5. A defect in this seat's OWN instrument, found and fixed
**TWO `surprise-watch` processes under one serial** — pid 2529891 (this session's Monitor) and pid 2864368 whose
PARENT was 2529891, started two hours later, despite the arm banner reading `wait=no-spawn/15s`. Two writers
replacing one state file wholesale produced the repeat emissions and 551 duplicate index lines over 1287 distinct
ids. Reaped (TaskStop alone does not reap the child), one re-armed as `bw2y3dv35`, **which emitted NOTHING on its
first pass** — the discriminator that the two writers were the cause rather than merely correlated.
Row `C-S82` @`4fe22271ea` records the prefix-keying half.

## Decisions made

- **`C-S83` @`194a7be807`:** `W4-S28` **closes** the date limb round 1 deliberately left open; it does **not**
  falsify the only round-1 S10 grade. `C-S78` (`S10-AC2 PASS`) was scoped to glyph loss and coordinate-vs-arithmetic;
  `C-S5` says in its own text *"glyph/date/holdout limitations remain open"*. All 78 round-1 rows scanned, exactly
  one S10 grade — the whole record, not a sample. **No correction owed on the round-1 slug; no grade reopened.**
- **Filed no third row on the watcher mid-round.** Carried to L10 instead; the CTO concurred and asked for no row.
- **Sent nothing to any seat but the CTO**, and nothing at all on round findings.

## Corrections to this seat's own work, on the record

- **`C-S82`'s first draft was WRONG in the direction of alarm** and was rewritten before landing. It graded the
  watcher finding ARMED and asserted 18 rows had reached no agent, written from 32 `NEW CHANNEL` lines alone. The
  row gate refused it (ARMED with no `disarm_owner`) and in that interval the watcher's second limb emitted 19
  `NEW ROW` lines that falsified the premise. **The gate caught a schema violation; only the delay caught the
  substance** — an early stop and a true failure read identically.
- **A suspected false-negative on the mutation limb was unfounded and I said so** rather than leaving it standing:
  `surprise-watch.sh:237` replaces the index wholesale, and the limb walks every stored entry, so duplicates make
  it OVER-fire, never under-fire.
- **A suspected disarm-by-carry (`S38` vs `W3-S26`) was also unfounded.** Read in full, `S38` withdraws the ordered
  deploy and re-cuts it atomically — it addresses the same proposition, so it is a complete disarm.

## Blockers

None at this seat. **The L9/L10 gate is not a blocker, it is the rule:** no judgment criterion is graded and no
slug is cuttable while cells are non-terminal — IRPT_BCKEND has rt-2/rt-9/rt-10 live with rt-6/rt-11/rtb-1 staged;
IRPT_FNTEND has FE-s-15/16 seating and FE-s-18 last.

## Current state

Registered LIVE (PID 7764). Two Monitors armed: inbox `bz8at6m7q`, surprise-channel `bw2y3dv35`, both parent-tied.
L4-R clear on all three live PRDs (`IRPT_BCKEND` v0.13, `IRPT_FNTEND` v0.6, `DSGN_REBRND` v0.2) — this seat owes no
half **today**; see Next Steps 2. Delivery ledger clear; 96033/96042/96044/96048/96055 all opened and acked.
Local CLOUD `1430ddf9ea`; `origin/CLOUD` `6ced337f86` by `ls-remote` at 01:42Z — **stated as AGED, not current.**
The push is `0.0.0_AB_MSTR`'s on Andrew's word and this seat has never pushed.

## Next steps

1. **[3.0.0_SA_CVO]** Continue L8 intake on both channels. CVO id spaces continue after **`IRPT_BCKEND-C-S83`**
   and **`IRPT_FNTEND-C-S45`** — check both adjudication docs for later additions before minting.
2. **[3.0.0_SA_CVO] A GENUINE L4-R RE-REVIEW IS COMING and it is WIDER than the CTO stated.** Its StatusEnvelope
   amendment touches the CONTRACTS table, re-opening this seat's ratified-text half. The spine's clause
   (`CANONICAL_FABRIC_WORKFLOW_20260901.md:164-167`) is *"the CONTRACTS section agrees with the counterpart PRD"* —
   **a relation between two artifacts, so a one-sided amendment can falsify the FNTEND half without touching one
   byte of FNTEND, and no `half_hash` can see it.** Re-review BOTH halves, not only BCKEND. Surfaced to the CTO
   before the amendment lands (msg 02:22Z); not a gate and not a hold.
3. **[3.0.0_SA_CVO]** At L10 carry, by name: `S41` (still at its own disposition — `S42` disarmed the hazard but a
   REMEDIATION row is what resolves an item and those are this seat's); `W4-S28`/`S40`; `W4-S29` and `W4-S30`;
   the `W2-S13` **wrong-cause** correction as a NEW row citing the old id; the watcher's two halves; and the
   carve-out record with its rejected alternative.
4. **[1.0.0_SA_CTO]** Land the StatusEnvelope L4 amendment; this seat reviews it as a real review, not a re-stamp.

## What a successor must NOT re-do

Do not re-open round 1 on either project. Do not re-run the round-1 scratch writer under
`.runtime/codex-seats/3.0.0_SA_CVO/irpt-round1-review/` — it is stale against manual corrections. Do not mutate
`W2-S13` in place; corrections are NEW rows citing the old id. Do not file a third row on `surprise-watch.sh`.
Do not re-stamp any L4-R half for hygiene — the next stamp is earned by a semantic change.
