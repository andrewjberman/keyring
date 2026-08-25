# OPAL_GLDRNS -- twr_daily D-1 mirror remedy, surfaces (a)(b)(c)(d) -- 0.4.0_DS_ClientPlatform~H

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Window:** 2026-08-25T02:00Z -> 03:03Z (session start to now; first log of this session)
**Lane:** `0.4.0_DS_ClientPlatform~H` (no lane folder exists; logged under the base folder per the standard)
**Project:** OPAL_GLDRNS -- the twr_daily D-1 MIRROR REMEDY. ONE project, per spawn brief.
**Decomp:** `workflows/atom_decomposition/runs/gldrns-twr-d1-mirror/20260825T015000Z/DECOMP.md`

---

## What this session did

Landed surfaces (a) MIRROR POPULATION, (b) TRADING CALENDAR, (c) REFUSAL INTEGRITY and
(d) DISCLOSURE of the 26-cell decomp -- 21 owned cells. Surface (e) BACKFILL was held out
deliberately (Rule 24(iv)) and is untouched. Surface (f) ACCEPTANCE remains open at the
deploy and the scheduled fire.

**Commit: `b9a665364f` -- LANDED LOCAL, RIDES INTEGRATION. Not pushed, not deployed.**
4 files, 388 insertions, 7 deletions. commit-gate clean. `[msg-verify] MATCH len=5863`.

### The mechanism (source-confirmed, then measured)

Every one of the 15 stages in `chain_49f_entrypoint._stage_list` passes exactly ONE date
expression -- the chain's `D` (AST-derived, 15/15). So `b00` writes only `date=D` into the
mirror; `c02`'s `prev_path` at `date=D-1` never exists; every row takes the
`REFUSED-NO-BMV` branch (a 5-key dict) instead of the OK branch (9-key); and `c02:98`
`pd.DataFrame(rows)` derives the column set FROM THE ROWS. That is the entire 13-vs-9
signature. **The columns were not dropped -- they were never derivable.**

### Cell-by-cell

| cell | disposition | evidence |
|---|---|---|
| `GLD-a-1` | DISCHARGED -- **measured, was inference** | isolated dry-run (own workdir, own mutex parent) `--date 2026-08-21` rc=0 212.8s: mirror at c02 time = 7 tables x exactly 1 distinct date; `canonical_valuation` held `date=2026-08-21` ONLY; c02 printed `{'REFUSED-NO-BMV': 7335}`, matching the live scheduled manifest exactly |
| `GLD-a-2` | LANDED | `_pull_prev_valuation_into_mirror()`, invoked immediately before c02, keyed on c02's own stage NAME so a future list reorder cannot detach the pull from its consumer |
| `GLD-a-3` | RULED, with reason on the record | CHOSE S3 pull (reuses `_pull_canonical_for_c04`, Build Ladder rung 2). REJECTED re-running `b00 --date {prev}`: recomputes a stored object and makes a SECOND PRODUCER of the same partition. It would also have moved the stage count to 17; the pull is a helper step and does not |
| `GLD-a-4` | DISCHARGED -- both arms, live S3 | `date=2026-08-18` -> prev `2026-08-17` is a real gap in the 530 partitions -> `ABSENT-IN-S3`, no empty dir left behind. Positive control `2026-08-19` -> `PULLED`, 2 objects. Chain does NOT abort: a genuinely absent D-1 is legitimate |
| `GLD-b-1` | LANDED | prev read from a04's `dim_calendar` via the SAME `prev_map` c02 builds. No second calendar source, no wall-clock arithmetic |
| `GLD-b-2` | DISCHARGED -- exercised over the live 534-day calendar | `prev_trading_day` == the immediately preceding trading day on 533/533. A WALL-CLOCK D-1 would resolve the WRONG partition on **118/533 = 22.1%** of runs (102 Mondays + 16 post-holiday) |
| `GLD-b-3` | LANDED + tested | `NO-PRIOR-TRADING-DAY` preserved as permanently correct at a series' first partition; helper never asks S3 for a partition that cannot exist |
| `GLD-c-1` | LANDED + tested | three refusal statuses stay distinct; census is per-status |
| `GLD-c-2` | DISCHARGED -- **mutant run in BOTH directions** | defaulting the refusal dicts -> 3 tests FAIL naming the operand; revert -> byte-identical `md5 86c9c812...` and 12 pass |
| `GLD-c-3` | CROSS-CHECKED, not touched | DS~G's contract. Disarm landed `2e87c580b2`, re-ratification `428a2c88bb`. I edited nothing of theirs |
| `GLD-d-1` | DISCHARGED -- was measurably FALSE on production | the live scheduled manifest `date=2026-08-21` read `"ABSENT -- exercise mode, all rows refused"` on a PRODUCTION fire. Now states the partition used, or WHICH absence |
| `GLD-d-2` | ALREADY SATISFIED at HEAD -- verified, NOT rebuilt | `status_census` was already carried into the manifest and `runner_common.emit` already ships it. Build Ladder rung 1 |
| `GLD-d-3` | DISCHARGED -- asserted on a run | `stages=16` was hand-typed with no `len()`. Now derived. **The literal was ALSO already wrong on every dry-run** (which skips c04): dry-run now prints 15, upload prints 16 |
| `GLD-inv-1..6` | HONORED | refusal path intact and never defaulted; no date literal; no new schedule/trigger/alarm/monitor; no served output moved; no shadow path or comparator; evidence at named refs |
| `GLD-inv-7` | VERIFIED DISCHARGED at the APPLIED layer (COO had it open) | see below |
| `GLD-e-1..3` | HELD OUT -- untouched | Rule 24(iv). The 6 partitions remain UNCLASSIFIED by status |
| `GLD-f-1..3` | OPEN | need the scheduled fire, the deployed bytes, and a deploy ledger entry |

### End-to-end exercise (ad-hoc QA -- explicitly NOT production evidence)

Real chain, `--date 2026-08-19`, rc=0, 247.0s:
```
prev valuation pull: 2 object(s) for date=2026-08-18 (D-1 of 2026-08-19) -> mirror canonical/canonical_valuation/
backfill mode (D-1 2026-08-18 loaded): {'OK': 6393, 'UNCOMPUTABLE-ZERO-BMV': 922, 'REFUSED-NO-BMV': 17}
CHAIN OK date=2026-08-19 wall=247.0s
```
Manifest: `bmv_source "canonical_valuation date=2026-08-18"`, cols 9 -> 13.
Was 100% `REFUSED-NO-BMV`. `GLD-f-1` still requires the SCHEDULED run; an ad-hoc run is a QA
instrument and never production evidence.

---

## The ARMED item I raised against my OWN remedy (filed `ADVI_PERFRP-S12`)

Before building, I surfaced that this remedy CREATES MIXED PARTITIONS, which have never
existed. Exercised against `c02:98`'s own construction: all-refused -> 5 cols, all-OK -> 9,
MIXED -> 9 with the refused rows reading `bmv=NaN, r_net=NaN`. A mixed partition presents
in the FULL shape while containing refused rows whose operands are **PRESENT-AS-NaN, not
ABSENT.** That is `GLD-inv-1`'s harm reached by a route inv-1 cannot see: inv-1 forbids
DEFAULTING the refusal dicts, nobody defaults them, and pandas' own column union does it.

Consequences it produced across the fabric:
- COO added `GLD-inv-7` (decomp 25 -> 26): the consumer disarm lands and is DEPLOYED before
  the first mixed emission. A DEPENDENCY, not a gate.
- CVO retracted the STRUCTURAL form of its own ratified claim (co-extensivity is
  state-dependent, not a signature) and issued a re-ratification `@f29554053f`.
- DS~G found the hazard was **LIVE, not hypothetical**: `link_returns` tested
  `v is not None`, and a NaN is not None, so it returned `(nan, "COMPUTED", coverage 1.0)`
  -- a NaN LABELLED COMPUTED with full coverage. Fixed `2e87c580b2`.

I did not pull surface (e) in, and I declined the contract's `refused_dates` tuple: it names
the 6 dates but not which of the three statuses each carries, so they remain unclassified.

## `GLD-inv-7` -- I verified the DEPLOY half COO had left open

COO verified the SOURCE half at `428a2c88bb` and explicitly said "I have NOT verified the
DEPLOYED bytes". Because my commit is a deploy, I checked before committing:
```
s3://opal-data-49financial/_code/perfrp_contract.py  LastModified 2026-08-25T02:47:32Z
md5 DEPLOYED         = 9a2aa974d15467e5a0f30092c964d208
md5 repo @428a2c88bb = 9a2aa974d15467e5a0f30092c964d208   -> BYTE-IDENTICAL
deployed bytes carry SHAPE_IS_A_VALID_CLASSIFIER = False + STATE_CLASSIFIER_FIELD = "status" (:142-143)
and the retraction AT the shape declaration (:308, :313)
positive control TWR_DAILY_SHAPE_FULL = 2 hits; negative control = 0 hits. Both arms ran.
```
Consumer disarm is DEPLOYED; my producer change is not. Ordering is correct as of this log.

---

## Findings raised

1. **`GLD-b-2`'s own ORACLE WORDING is too strong.** It reads "A Monday run must pull FRIDAY,
   not Sunday" -- true 98 of 103 times. FIVE Mondays pull a **THURSDAY** because the Friday
   before was a market holiday: `2025-04-21, 2025-07-07, 2026-04-06, 2026-06-22, 2026-07-06`.
   The invariant is "the prior TRADING day"; Friday-on-Monday is its commonest instance, not
   the rule. A test author implementing the oracle literally ships a check that fails on
   those five. Both cases now pinned as tests asserted BY DATE VALUE.
2. **ARMED -- `c04_validation_battery` check 7 structurally cannot fire.**
   `c04_validation_battery.py:140` passes `twr_daily=None` HARDCODED while `integrity`,
   `ledger` and `positions` are each loaded via `_try(...)`. So `:86`'s guard is never true
   and the anomalous-return census has never evaluated a return. Its else-branch message
   ("single-partition exercise structurally yields zero computable rows") is ALSO falsified
   by this remedy. The chain's own `_pull_canonical_for_c04` already downloads `twr_daily`
   into the c04 mirror -- pulled, staged, then not passed. **I did NOT fix it:** arming a
   dormant grade inside a battery whose failure ABORTS the chain is a behaviour change to an
   acceptance instrument, not a cell in my 21. Routed to CVO + COO.
3. **Second-order, same file:** `_try` uses a bare `except Exception: return None`, so a READ
   FAILURE and an ABSENT TABLE are byte-identical to every downstream grade -- an instrument
   failure renders as a `PENDING-BACKFILL` verdict. Named once, not my lane.
4. **My own instrument failure, caught by a control.** My first static stage census used a
   regex over the `_stage_list` body and returned "4 of 4 stages" with total confidence --
   nested brackets broke it. The conclusion it supported happened to be right, which is
   exactly why it was dangerous. Discarded and re-derived with AST (15). Separately, a
   `tail -20` on a run log cut off the `CHAIN START` line and I briefly read that as the
   code not printing it. Both are the retrieval-control class.

## Blockers

**None.** Nothing is blocking this seat. `GLD-f-1/f-2/f-3` are not blockers -- they are open
cells owned at the deploy act and the scheduled fire, which are not mine.

**One question outstanding (not a blocker, work continues):** CVO 68162 says "REMEDIATION --
the mixed-partition consumer hardening -- remains OPEN and is DS~H's"; COO 68146 scopes
REMEDIATED as the census re-base plus `GLD-e-1`'s classification. Those name different work
and one names me. Asked COO (issuer) to rule rather than adopting either reading. Stated
explicitly in that ask: shape stabilisation (always emitting 13 columns) is NOT the answer --
it defaults the refusal path in substance, breaches `GLD-inv-1`, and my own `GLD-c-2` mutant
test fails on it by construction.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `--name 'perfrp_contract.py'` | PASS | DENOMINATOR 1 hit / 28,249 files scanned |
| `comp-find` | `-i 'stages='` | PASS | 5 hits / 26,303 files. Established NO machine consumer of the `stages=` line before changing its value -- source + docs + one evidence artifact only |
| `comp-find` | `-i 'twr_daily' data/assets/scripts/gold/runners_49f` | PASS | located `c04_validation_battery` as the only twr_daily consumer in the runner tree; led directly to finding 2 |
| `comp-which` | A.3 startup exercise probe | PASS | forwarder RAN (produced its own banner), not merely resolved |

**What worked:** `comp-find`'s BAND classification separated the `[SURFACED]` source hit from
`[DOC]` prose in one call, which is what made the "no machine consumer" call cheap and
defensible rather than a guess.
**What failed:** nothing at the tool layer. My own hand-rolled regex census failed (finding 4)
-- the lesson is that the on-rails tool would not have made that error, and I reached for a
regex because the question was about AST structure. AST was the right instrument and I got
there on the second try.
**Gap found:** none new. `comp-find` is case-sensitive by default and I used `-i` throughout
per Rule 21.

## Files Modified

See commit message `b9a665364f` -- it carries per-file reasoning. Summary:

| file | change |
|---|---|
| `chain_49f_entrypoint.py` | `+_pull_prev_valuation_into_mirror()`; wired before c02; `stages=16` literal -> derived |
| `c02_twr_engine.py` | `bmv_source` now names the artifact or WHICH absence, never the mode |
| `tests/test_c02_twr_engine.py` | +4 tests: the `GLD-inv-1` mutant guard, the all-refused shape, the mixed-partition shape, status distinctness |
| `tests/test_chain_49f_prev_pull.py` | NEW, 12 tests: weekend + holiday by date value, the c02 seam, ABSENT-IN-S3, no-prior-trading-day, null sentinels, fail-loud |

Tests: **24 passed** (12 c02 + 12 pull).

## MCP traffic

11 messages handled; 4 sent. Significant:
- IN: spawn brief (MSTR 67848); COO `GLD-inv-7` sequencing ruling (67986); COO
  moment-vs-mechanism class (68028); DS~G disarm + the live `link_returns` NaN bug (68049);
  CVO re-ratification issued (68062) and verified (68162); COO inv-7 source verified,
  deploy half open (68146).
- OUT: RAVC ack + `GLD-a-1` measured (to COO); the S12 ARMED item (CVO/COO/DS~G, 3 DELIVERED);
  the landed report incl. my inv-7 deploy-layer verification (COO/CVO/MSTR, 3 DELIVERED);
  the c04 ARMED item + scope question (CVO/COO, 2 DELIVERED).

## Current State

`OPAL_GLDRNS` twr D-1 mirror: surfaces (a)(b)(c)(d) COMPLETE and committed at
**`b9a665364f`, LOCAL on branch CLOUD, awaiting integration.** Nothing pushed by this seat.

**THE COMMIT IS A DEPLOY.** `_code/chain_49f_entrypoint.py` (LM 2026-08-20T16:24:36Z) and
`_code/c02_twr_engine.py` (LM 2026-08-19T19:01:22Z) both EXIST in
`s3://opal-data-49financial/_code/`, so both update on the integrator's push under the
key-exists guard. `_code/tests/` has KeyCount 0, so the two test files are a loud skip.

The production path, per the 08-21 change-management ledger
(`org/critical_paths/change_management/20260821T1520Z_advi-49f-canonical-0819-production-backfill.md`):
host `bd-gold-layer-runner i-01003b035d2988dfb`, SSM document `advi-49f-chain-dispatch`,
which HARDCODES `--production` and takes no date parameter. So the scheduled fire derives
T-1 and will pull D-1 through the new step.

**IAM:** the pull uses `list_objects_v2` + `GetObject` on
`gold/advi/canonical/canonical_valuation/` -- the same actions on the same prefix pattern
`_pull_canonical_for_c04` already performs on the production host. I expect no new
`(action, resource)` pair, but **I have NOT simulated it against the EC2 role** -- my live
exercise ran under user credentials, a different principal. Worth one check at deploy.

## Next Steps

1. **[2.0.0_SA_COO]** Rule what, if anything, remains mine under "REMEDIATION" (CVO 68162 vs
   COO 68146 name different work; one names me). Sent 68278.
2. **[3.0.0_SA_CVO / 2.0.0_SA_COO]** Disposition the `c04` check-7 ARMED item -- name a
   disarm owner. It is an acceptance-surface hazard: an inert check manufactures assurance.
3. **[0.0.0_AB_MSTR]** `b9a665364f` rides integration. This push IS a deploy of two
   runner scripts; `GLD-f-3` wants a deploy-completion ledger entry in
   `org/critical_paths/change_management/` opened AT DEPLOY-START. I did not open one
   because I am not the one pushing -- say the word and I will.
4. **[unassigned]** `GLD-f-1` closes only on the SCHEDULED chain's own emission with non-null
   `r_net` on a real population and its count printed. `GLD-f-2` needs the deployed bytes
   read back after the push.
5. **Surface (e)** stays held out. Its 6 partitions still need per-status classification
   (`GLD-e-1`) before any re-run is planned, and the re-emission is a separately authorized
   act on a versioned bucket (`GLD-e-3`).
