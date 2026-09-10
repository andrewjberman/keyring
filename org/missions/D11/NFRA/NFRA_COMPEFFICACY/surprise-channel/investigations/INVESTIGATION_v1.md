# NFRA_COMPEFFICACY -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Assembled by:** `3.0.0_SA_CVO` (L8: the CVO assembles, any seat surfaces -- `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.4).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY` (Andrew-direct
2026-09-02 23:0xZ: the row gate is the control).
**Round 1 task orders:** ONE live -- `TO-CE-T-1` at `0.8.0_AE_CloudComp` (TO-CE-DISC-2 and TO-CE-TP-1 WITHDRAWN 02:25Z,
their decisions landed at L4 in PRD v0.4 @19bf1c7322). L10 routing waits on that TO's completion AND every row below
CVO-checked.
**Append-only during the round.** Denominator at this write: **42 rows** (S1-S36, S39, S40 -- S40 appended by `3.0.0_SA_CVO` 2026-09-10 ~01:2xZ at the round-7 L9 -- and W1-S1..W1-S4, the worker 0.9.0_WK_NFRA_COMPEFFICACY~1's, merged @8c3cadf936 without a restatement). The previous restatement: **37 rows** (S1-S36 and S39; S39 appended by `3.0.0_SA_CVO` 2026-09-04 06:5xZ at the round-6 L9; S34, S35 and S36 are the worker 0.9.0_WK_NFRA_COMPEFFICACY~2's, merged @46ff7f8c8a without a restatement; S37 and S38 are CVO rows in `../adjudications/` and are not items. The previous restatement: **33 rows** (S33 appended by `3.0.0_SA_CVO` 18:09Z, the round-6 tranche-1 L9: S23/S24/S25/S26/S27/S28/S30/S32 DISMISSED_WITH_REASON on this seat's reads; S29 and S31 wait for the stamp; S32 is a worker's adjudicating row on the CVO's item, a form note for the issuer).)
04:26:20Z, the disarm ack on S6: PID 25896 left untouched, the docstring residual confirmed already
fixed at S5's own commit. S6 appended by `3.0.0_SA_CVO` 04:2xZ, the L9 disposition and L10 stamp of the S2/S3/S5 item; S5 appended by `0.8.0_AE_CloudComp`
04:16:43Z -- the S3 disarm: grounds the BUDGET REACHED phenomenon as LOCAL via a live rebuild-process
citation, discharging the disarm-owner assignment S3 named. S3 + S4 appended by `3.0.0_SA_CVO` 04:0xZ --
the L9 adjudication in append-only form: S3 the recurrence of S2 measured at the CVO seat, S4 the closure
of S1; S2 appended by `0.8.0_AE_CloudComp` under the tree channel's lane-ANY worker-appends grant,
CLAUDE.md s.2 as corrected by Andrew-direct 2026-09-03 03:1xZ -- "a broker message is NEVER the carrier";
S1's own text and CVO attribution are UNCHANGED below).

## L8 read -- what the CVO checked on each row

- **S1** (surfaced by MCP 92943 at 02:55:51Z; no row existed on either root at the time -- the notifier's denominator was
  unchanged at 18 files / 191 rows, so this file is the row's first home). Grounding RESOLVES at this seat: commit
  `88e870b115` exists (author `0.8.0_AE_CloudComp`, 02:48:38Z; `.tools/comp-find` + `.tools/tests/test_comp_find_battery.py`,
  2 files, +138/-5), commit `19bf1c7322` exists (author `1.0.0_SA_CTO`, 02:51:16Z; PRD v0.4 + the answer-state enum), and
  TO-CE-T-1 :35-36 carries the Grammar clause verbatim as quoted. The world diverged from the TO's bound (a third file)
  and the ISSUER resolved it in-round (`2.0.0_SA_COO` 92960: bound AMENDED, `.tools/_compbudget.py` IN SCOPE under
  CE-t-1). Nothing to route; the owner's rework under the live TO is the disarm. Held `UNDER_INVESTIGATION` until that
  rework lands, because an ARMED item whose disarm has not yet landed is not written up as done -- DISARMED is not
  REMEDIATED, and neither has happened yet. Closing condition in `notes`.

- **S2** (surfaced directly by `0.8.0_AE_CloudComp`, the row's first home, per the CLAUDE.md s.2 correction --
  no MCP precursor for this one). While exercising T1-AC3's forced-ceiling control on the live `--corpus aws`
  backend, the SAME unscoped query that had completed in 7.4-8.2s across five separate measurements over the
  prior ~20 minutes (02:26Z-03:07Z) took >=90s (BUDGET REACHED, own internal ceiling) on three consecutive
  attempts 03:16Z-03:20Z, including one isolated, non-concurrent measurement that ran the full 90.25s with
  nothing else executing. The Kuzu DB file itself (`infra/aws/globgrph/kuzu_nessie_db`) was unchanged in size
  and mtime across the window (last write 2026-09-02T20:36Z, i.e. before this session), ruling out DB growth
  as the cause. Root cause NOT chased (this seat's own repeated `--mode inc` calls -- roughly 20 in the
  preceding 20 minutes -- are the leading, unconfirmed hypothesis: either local resource contention from rapid
  repeated Kuzu-native-library process launches, or AWS-side throttling on the CloudTrail-driven incremental
  refresh from that same call volume). By 03:25Z the SAME query completed in-budget again (battery re-run,
  19.68s wall total including all ten arms) -- self-resolved, transient, no code defect. Filed as OBSERVATION
  because CLAUDE.md Rule 22.2's "measure a feed's own cadence before calling it stale" / "clean metrics print
  above a failure verdict" class of trap applies to comp-kuzu's OWN latency exactly as it does to a pipeline's:
  a 90s ceiling could read as "comp-find is broken" to a future reader who does not know the backend, not the
  tool, moved. Rule T (this cell's own deliverable) is the reason nothing hung for 600s during the window --
  it degraded to an honest BUDGET REACHED both times, which is the feature working as designed under a real
  fault, not a simulated one.

## L9 adjudication -- 3.0.0_SA_CVO, 2026-09-03 04:0xZ (round 1: TO-CE-T-1 terminal @fc5ec7106c)

Rows are APPEND-ONLY as a control (`.tools/surprise-row-gate.py` `_mutation_violations`: an in-place edit of S1/S2 was
REFUSED at 04:04Z), so an adjudication is a NEW row citing the old id. A reader resolves a row's state from the newest
row that cites it.

| row | state after this write | carrier | L10 effect |
|---|---|---|---|
| S1 | **CLOSED -- DISMISSED_WITH_REASON** | S4 | closed |
| S2 | **OPEN -- checked, not closed** (its 'self-resolved' claim is falsified; mtime label note) | S3 | OPEN |
| S3 | **OPEN -- UNDER_INVESTIGATION**, CVO's own row: 3 of 3 default-budget aws pulls hit BUDGET REACHED at 90 s from this seat 03:53Z-03:58Z, no burst, no leftovers, DB unchanged; mechanism ungrounded | itself | OPEN -- ARMED, disarm owner `0.8.0_AE_CloudComp` NOW; graduates when the mechanism is grounded |
| S4 | closure row for S1 | itself | -- |

**L10 read from this seat:** every row CVO-CHECKED (4 of 4); 1 item closed (S1 via S4), 1 item open (S2/S3, one phenomenon),
0 graduated, 0 routed. Per protocol s.7 an open item is not a zero: round 1 does not route until S2/S3 terminate. The DISARM
(is the live AWS-corpus pull stalled locally or upstream?) is off-cadence and `0.8.0_AE_CloudComp`'s now; the REMEDIATION,
once the mechanism is grounded, re-enters at L5 as next round's input via a remediation row this seat writes. Rule T is not
the defect here: it is what turned a 600 s hang into a 90 s honest prefix, three times.

## L10 stamp -- 3.0.0_SA_CVO, round 1 of NFRA_COMPEFFICACY closes by the backward route

| item | rows | disposition (newest citing row) | route |
|---|---|---|---|
| the mid-round grammar landing | S1 | DISMISSED_WITH_REASON (S4) | none |
| the AWS-corpus pull under Rule T | S2, S3, S5 | **DECOMP_INVALIDATING** (S6): the budget kill orphans the rebuild, the orphan holds the mutex, every caller waits longer than the budget, the 900 s steal restarts the cycle | **L5**, owner `2.0.0_SA_COO`: add the cell for the freshness layer under a budgeted client; executor the comp-kuzu engine lane |

Precondition: every task order terminal; every row dispositioned; 0 graduated, 0 forward routes. Nothing is cut at L6
until L5 carries the cell.

## L10 stamp -- round 2 (3.0.0_SA_CVO, zero graduation: proceed to the next L6 dispatches)

| item | carrier | disposition | L10 |
|---|---|---|---|
| S1 | S8 (adjudicates S1; S4 gave the same closure in prose) | DISMISSED_WITH_REASON | closed |
| S2 / S3 / S5 | S9 (adjudicates all three) | DISMISSED_WITH_REASON -- REMEDIED by CE-g-5 @173dd335f4, TO-CE-G-5 complete with a VALID proof, exercised at this seat (WITHIN BUDGET, 14.34 s, 2,100 nodes) | closed |
| S4, S6, S7 | themselves | terminal on their own face | -- |

Precondition: 5 of 5 task orders terminal, the three complete ones with VALID proof instances whose surprises resolve;
every item dispositioned by its latest carrier. 0 graduated, 0 routed. The round's three in-deliverable findings are read
and not counted here (the audits' own content; the per-tool carrier is theirs). Next: L6, `2.0.0_SA_COO`; `ROUND_CLOSE`
on this stamp by the row owner; the close (completion report + grades) follows per the spine.

## L10 stamp -- round 3 (3.0.0_SA_CVO, zero graduation: proceed to the next L6 dispatches)

Precondition, read at this seat at HEAD `ee7c884f29` (07:4xZ-07:5xZ), never from the report (93305):

| half | read | result |
|---|---|---|
| task orders | 7 files' `<status>` tags | 5 `complete` (G-5, T-1, T-2, T-3, T-8), 2 `WITHDRAWN` (DISC-2, TP-1), 0 pending |
| proof instances (round 3) | `proof-of-spec-check.py` at this seat, checker vintage `e58250f261` | TO-CE-T-3 VALID rc 0, 6 of 6, surprises 0; TO-CE-T-8 VALID rc 0, 6 of 6, surprises 0 |
| rows | this file at HEAD | 9, none appended in round 3; every item dispositioned by its latest carrier (S8, S9) -- unchanged |

0 graduated, 0 routed. Next: L6, `2.0.0_SA_COO` (STAGE 2 / STAGE 3 per the decomposition's arc), or the close if the
COO reports the decomposition spent.

**Read and not counted** (the per-tool carrier; the `CE-pass` roll-up consumes every finding): T-3's F1-F4 and T-8's
F1-F5. Named for the L4 owner, `1.0.0_SA_CTO`: T-3 **F2** -- `comp-which` routes a syntactically valid, NON-EXISTENT
gold-script id with a forced curated score (shape validated, existence never) -- is the round's one finding ARMED for
normal operation; its remedy is in-chain (STAGE 2 "subject existence", CE-t-6 after CE-t-19, and the roll-up), so it
is not a row under the CTO's reading 93320. T-8 F4 (the enum's carrier census one entry stale) is an L4 residual.

**Cross-check at L8** -- a row on ANOTHER project's channel that touches this project's stamped remedy:
`NFRA_CLDGRPH-S4` (`0.7.0_AE_CloudOps~Q`, 07:29Z) reports two local rebuild residues (mkdir mutex 06:49:01Z and
07:05:32Z; WAL growth stopping ~38-39 s after each; no kuzu process alive at either observation) beside CE-g-5's
"no orphaned rebuild; serve-stale-immediately". Read here against S9:
(a) no orphaned PROCESS at either observation -- `_run_child_supervised` (job object, KILL_ON_JOB_CLOSE) took the child
with its parent, which is the half CE-g-5 promised;
(b) neither attempt wrote a fallback-sink line (`infra/aws/globgrph/kuzu_nessie_db.fallback.jsonl`: 06:47:28Z,
06:47:59Z, 06:48:52Z, then 07:26:35Z -- nothing between), so both PARENTS died before the serve-stale completion path
(`_canonical.py` `_incremental_or_serve_stale`, status + sink + `_rm_kuzu`) and before the `finally` lock release;
(c) the residue is the designed `ORPHAN_LOCK_S` 900 s backstop's domain, and at this seat's read (07:33:41Z) no lock,
tmp or WAL was on disk;
(d) an inc-mode caller meeting a held lock is served immediately (`wait_for_peer=False`), so no caller paid `MUTEX_WAIT_S`.
S9's REMEDIED stands. NOT established here: what killed the two parents (a client-side event -- a harness ceiling or a
seat kill; the discriminator is the killed client's own log, not the engine's). Not a row: no assertion of this
project's spec is contradicted.

**Observation carried to the CTO for placement, claim INFERRED** (no client log read; the sink census is MEASURED):
36 sink lines today, all `inc-served-labeled-stale`, delta 27133-27134 nodes, served vintage
`2026-09-03T00:36:15Z` unchanged from 02:26:26Z to 07:26:35Z -- every WINNING inc-mode call re-runs the incremental
child to the same large-delta exit before it is served stale (the sink cadence 06:47:28Z -> 06:47:59Z -> 06:48:52Z and
the two ~39 s WAL windows bound the child at ~30-50 s); the "~5 s" serve (`_canonical.py:562`) holds for a LOSER, the
winner pays the child's runtime. The claim that sentence tests is `NFRA_KUZUSPLIT`'s, not this project's; the full
refresh is `comp-kuzu-full` / MSTR startup by design (Andrew O-1), and today's has not run.

## L8 + L9 after the round-3 stamp -- S10 (the rollup's `adjudicates` blindness) and S11 (S6's machine closure)

Seen while reading the channel's own rollup beside the stamp @7ec9bf06dd: `comp-surprise --project NFRA_COMPEFFICACY`
lists S1, S2, S3, S5 and S6 as OPEN + ARMED; the row gate's census reads 0 undispositioned. The rollup reads each row's
own `disposition` and its source has no `adjudicates` (comp-read enumerate, 0 of 38 hits); estate-wide the only
`adjudicates` carriers are S8 and S9 (20 documents, 207 rows), so the phantom-open set is exactly those five, all here.
S10 carries the finding (ARMED; disarm owner `1.0.0_SA_CTO`, the tool's lane; remedy in place per 93320 limb (i), nothing
routes). S11 adjudicates S6 so the one fix leaves zero phantoms on this channel. Both are round-4 items, appended after
the round-3 precondition was read at `ee7c884f29`; neither blocks a task order.

## L9 -- S12 adjudicates S10: the rollup disarmed in place @2bc3679e0b and exercised here

`1.0.0_SA_CTO` (93349) resolved comp-surprise's dispositions by latest carrier, the row gate's own rule. Exercised at
this seat at 08:16:10Z: open = [S10], armed = [S10] (was five and five); `_latest` on S1 and S6 reads DISMISSED_WITH_REASON;
estate open 73 -> 70; NFRA_CLDGRPH's 8 genuinely open rows unchanged (the negative control). S12 closes S10. Nothing routes.

## L10 stamp -- round 4 (3.0.0_SA_CVO: TWO graduated, one to L6 and one to L2; the rest read and not counted)

Precondition, read at this seat at HEAD `c6d4eced8f` (09:1xZ-09:2xZ), never from the report (93421):

| half | read | result |
|---|---|---|
| task orders | 9 files' `<status>` tags | 7 `complete` (G-5, T-1, T-2, T-3, T-7, T-8, T-9), 2 `WITHDRAWN` (DISC-2, TP-1), 0 pending |
| proof instances (round 4) | `proof-of-spec-check.py` at this seat, checker vintage `7b649df39d` (clean; an earlier run at `7e78fe9171` + 6 uncommitted lines read the same, and those lines touched only multi-token `cell_refs`, which neither instance has) | TO-CE-T-9 VALID rc 0, 6 of 6, surprises 0, 1 artifact co-committed at `b1dab0b6a0`; TO-CE-T-7 VALID rc 0, 6 of 6, surprises 0, 2 co-committed at `803539f490` |
| rows | this file at HEAD | 12; every item dispositioned by its latest carrier (S12 closed S10); the rollup reads 0 open / 0 armed on the fixed instrument |

**Graduated, two** (the remediation document opens with this round):
- **S13** -- comp-trigger's T9-AC2: three of four planted cases byte-identical; the instance self-marks PASS; PRD s.4.3 says
  any two alike is FAIL and calls it FWD-2, the load-bearing test. `SPEC_ERROR` -> L6, owner `2.0.0_SA_COO` (a remediated
  order under CE-t-9). For the grade: T9-AC2 reads FAIL by the spec's own bar, honestly disclosed, wrongly marked.
- **S14** -- comp-dataflow's T7-F4: Rule T's form fixes rc 0 at expiry; a gate whose rc is its verdict then returns CLEAN
  from a partial sweep. The PRD names no outcome for a gate archetype at expiry. `SCOPE_CHANGE` (REQUIRES_UNNAMED_OUTCOME)
  -> L2, owner `1.0.0_SA_CTO`.

**Read and not counted** (the per-tool carrier; the `CE-pass` roll-up): T-9 F2 (a real crash on a tiny budget, FIXED in-cell
with a red-first arm) and F3 (the canonical opal-data-bd/-cot/-inf buckets absent from the single-account live graph's
28-bucket population -- account scope vs a real gap UNDETERMINED; named for `1.0.0_SA_CTO`'s placement, it is the graph's
coverage, `NFRA_CLDGRPH`-adjacent, not this project's spec); T-7 F1, F2, F3 (F2 named for the grade against s.4.3).

**Correction to the round-3 stamp, scoped to one clause:** that stamp placed T-3's F2 (comp-which validates a gold-script
id's shape, never its existence) "in-chain" under "STAGE 2 subject existence, CE-t-6 after CE-t-19". The decomposition's own
row :55 makes CE-t-6 comp-blast's cell (T-6), not a cross-tool home, so the placement was wrong; decomp v0.2.2 :52 inherited
it. F2's home is the `CE-pass` roll-up ("fixed" or "not fixing, and here is why") and the L4 owner's grade; it is not
graduated here because T3-AC2's four planted cases were distinguishable (F2 names a subject class the planted case did
not cover), unlike S13. `2.0.0_SA_COO` is told for v0.2.3. Everything else in the round-3 stamp stands.

Next: the two route owners act (annex s.8 'Who acts'); the COO's next L6 for the cells the routes do not touch (CE-t-19
RULED, then CE-t-6; STAGE 3) is not pre-empted by either route.

## L10 stamp -- round 5 (3.0.0_SA_CVO: ONE graduated, to L2; two routed items CLOSED on exercised disarms; one placed with its owning surface)

Precondition, read at this seat at HEAD `6cabd10827` (14:1xZ), never from the report (93626):

| half | read | result |
|---|---|---|
| task orders | 12 files' `<status>` tags at HEAD | 9 `complete` (G-5, T-1, T-2, T-3, T-7, T-8, T-9, T-9R, T-25), 3 `WITHDRAWN` (DISC-2, TP-1, T-19), 0 pending |
| proof instances (round 5) | `proof-of-spec-check.py` at this seat, checker vintage `7b649df39d` | TO-CE-T-9R VALID rc 0, 5 of 5, surprises 1 resolving; TO-CE-T-25 VALID rc 0, 5 of 5, surprises 2 resolving |
| rows | 17 at HEAD + S18 in the worker's worktree | open by the rollup: S15, S16, S17; armed: S13, S14, S15, S17 |

**Graduated, one:** **S17** -- R-4's condition ("comp-trace ... if so it should be retired") measured NOT MET on two
instruments the L4 owner's line-range cite did not use; the PRD's manifest row carries `claim=measured` on a strict-subset
claim the world contradicts. `SCOPE_CHANGE`, `CONTRADICTS_NAMED_OUTCOME`, `outcome_ref` FWD-5 (Andrew's written answer to
the subset question), -> L2, owner `1.0.0_SA_CTO`; the three honest options the lane named ride the remediation row, and the
choice is the L4 owner's and plausibly Andrew's, since it is his ruling's own condition that failed. TO-CE-T-19 stands
WITHDRAWN on its own gate; nothing was built or deleted; the carryable flag remainder is named for whichever cell the
sequencer places it in. CE-t-6 waits on this route by the decomposition's own dependency.

**Closed, two, on exercised disarms** (their remediation rows in `REMEDIATION_v1.md` carry `DISARMED`, `REMEDIATED`,
`closed`; the adjudicating rows S19 and S20 carry the exercise): S14 (comp-dataflow's gate returns rc 4 NOT-DECIDABLE at
expiry; run here) and S13 (comp-trigger's four states by token; three demonstrated live here, the fourth by fixture because
of S15). For the grade: T9R-AC3's disclosed partial stands as disclosed.

**Placed, one:** S15 (the empty TRIGGERS edge; a silent-zero in the graph engine's deriver) -- outside this project's chain,
handed to NFRA_CLDGRPH by the record committed with this slug (S21). Consequence for this project's close, stated: FWD-2's
comp-trigger limb is fixture-covered for one state until that surface derives the edge; the L4 owner grades it.

**Read and not counted:** T-25's F1 (the expiry rc form into the shared budget module -- the L4 owner's grain), T-9R's
disclosed partial (in S20 for the grade), T-19's flag table and carrier census (the deliverable @bfbff9dc14).

**Form notes for the issuer:** S18's author set its own disposition (the CVO's field); S18 was integrated into this commit
from the worker's worktree under the audited override because the round could not stamp around it -- authorship unchanged.
**Law changed between rounds:** annex v2.3 (12:02Z) gives a remedied-in-round item a REMEDIATED remediation row; S13 and S14
were routed before it and close on their own rows' clocks; read the two shapes as a law change, not an inconsistency.
**This seat's own defect** (S22): the packet aged about five ticks; CVO MODE of /drive is armed at 20 minutes from this stamp.

Next: `1.0.0_SA_CTO` acts on the S17 route; `2.0.0_SA_COO`'s next L6 for everything the route does not touch (STAGE 3 wide,
per the pitch 93644) is not pre-empted.

```json
[
  {
    "id": "NFRA_COMPEFFICACY-S1",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp",
    "surfaced_at": "2026-09-03T02:55:51Z",
    "one_line": "CE-t-1: PRD landed v0.4 s.4.4's canonical Rule T form (@19bf1c7322) mid-round; comp-find's already-committed fix (@88e870b115) used the T-16 interim shape per the TO's own words -- reworking to the landed form before reporting, named owner 0.8.0_AE_CloudComp",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 88e870b115 (0.8.0_AE_CloudComp, 2026-09-03T02:48:38Z): .tools/comp-find + .tools/tests/test_comp_find_battery.py, 2 files +138/-5 -- the interim T-16-shape fix; measured at 3.0.0_SA_CVO via git log/show",
        "commit 19bf1c7322 (1.0.0_SA_CTO, 2026-09-03T02:51:16Z): PRD NFRA_COMPEFFICACY v0.4 s.4.4 carries Rule T's FORM (--budget > COMP_BUDGET_S > 90 s default; WITHIN BUDGET / BUDGET REACHED; --cursor; one shared .tools/_compbudget.py); measured at 3.0.0_SA_CVO via git log",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-T-1.comp-find-s4-audit.md:35-36 @4d9cd02e40 -- 'Grammar: CE-tp-1's form (TO-CE-TP-1, at CVO) when it lands; until then the T-16 DEFERRED: N of M shape as the interim, stated as interim in the deliverable.'",
        "2.0.0_SA_COO 92960 (issuer's word, 02:58:38Z): reading AGREED; BOUNDS amended -- .tools/_compbudget.py IN SCOPE under CE-t-1; TO file to carry the amendment at the issuer's next commit"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CE-T-1 :35-36: 'Grammar: CE-tp-1's form when it lands; until then the T-16 DEFERRED shape as the interim'; BOUNDS: 'No new dependency, no new file outside the two named (the tool, its battery) plus the deliverable + proof instance.'",
    "world_is": "The form landed in PRD v0.4 s.4.4 @19bf1c7322 at 02:51:16Z, 2 min 38 s AFTER the interim-shape fix @88e870b115 (02:48:38Z) was committed; the form names --budget / COMP_BUDGET_S / 90 s / --cursor / one shared .tools/_compbudget.py, none of which the interim commit carries (it has --budget-s, DEFERRED-prefixed text, no cursor, no shared module) -- and the shared module is a third file outside the TO's two-file bound.",
    "notes": "CVO L8 check 03:0xZ: grounding resolves (both commits present locally; TO clause verbatim). Not routed: the TO's own Grammar clause anticipated the form landing mid-round, the issuer amended the bound in-round (92960), and the owner's rework under TO-CE-T-1 is both the disarm and the remedy. CLOSING CONDITION: flips to DISMISSED_WITH_REASON when 0.8.0_AE_CloudComp's reworked commit lands and the T1 deliverable report cites the s.4.4 form (T1-AC4 in the landed grammar); if the rework does not land before the TO's report, the item GRADUATES to a remediation row instead. No remediation row seeded now. Push state of every cited commit: LOCAL at this write (origin/CLOUD @96af269f47; 0.0.0_AB_MSTR window 92955 pushing)."
  },
  {
    "id": "NFRA_COMPEFFICACY-S2",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp",
    "surfaced_at": "2026-09-03T03:25:00Z",
    "one_line": "CE-t-1 T1-AC3 exercise: the live --corpus aws (comp-kuzu) backend degraded from a consistent ~8s per unscoped pull to >=90s (BUDGET REACHED) across three measurements 03:16Z-03:20Z, then self-resolved by 03:25Z -- transient live-infra latency, not a comp-find defect; Rule T's own ceiling is why nothing hung for 600s during the window.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Five successful unscoped `comp-find --corpus aws opal-gateway` measurements 02:26Z-03:07Z: 13.78s, 8.23s, 7.81s (--budget 0), and two scoped LAMBDA-unit measurements at 7.72s and 7.38s -- all completed well within any plausible budget",
        "Three degraded measurements 03:16Z-03:20Z: an isolated, non-concurrent run (nothing else executing) of the identical unscoped query ran the full 90.25s and hit BUDGET REACHED; a follow-up with --budget 30 also exhausted its budget without completing",
        "infra/aws/globgrph/kuzu_nessie_db: 82,661,376 bytes, mtime 2026-09-02T20:36Z (measured via `ls -la` at the time of the slow runs) -- unchanged across the whole session, ruling out DB-file growth as the cause",
        "Recovery: the full 10-arm battery (including F2/F3, which use a 150s budget + 170s wrapper timeout specifically to tolerate this) completed in 19.68s total at 03:25Z -- the backend was fast again"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.4 s.4.4.1's measured baseline and this seat's own T1 deliverable assume comp-find's --corpus aws pull completes in single-digit-to-low-teens seconds under normal conditions (the basis for a 90s default budget comfortably under the 120s outer ceiling).",
    "world_is": "For a ~4-9 minute window (approximately 03:16Z-03:24Z) the same query took >=90-120s+ instead, on a backend whose own DB file did not grow -- i.e. the LATENCY moved, not the DATA. Leading, UNCONFIRMED hypothesis (root cause NOT chased per CLAUDE.md s.2's speed governor): this seat's own ~20 `--mode inc` invocations in the preceding 20 minutes, either as local resource contention or AWS-side throttling on the CloudTrail-driven incremental refresh.",
    "notes": "Not routed as a spec/decomp/scope error -- nothing about the TO, the PRD, or the decomposition was wrong; the WORLD (a live backend's latency) moved and moved back on its own. Filed because a future reader of a BUDGET REACHED line during a bad window could mistake backend latency for a comp-find defect if this window is not on record, and because CLAUDE.md's own 'measure a feed's own cadence before calling it stale' / 'clean metrics print above a failure verdict' traps apply to comp-kuzu's latency the same way they apply to a pipeline's freshness. CLOSING CONDITION: CVO may close DISMISSED_WITH_REASON (self-resolved, no code defect, Rule T behaved correctly under the fault) at L8; no remediation owed to comp-find itself. If this recurs, the owner is comp-kuzu / infra/aws/globgrph, not this cell. Push state of every cited measurement: none of it is a commit; the CODE change it prompted (F2/F3's latency-tolerant redesign) rides commit 88e870b115's successor (this cell's rework), reported separately. No standing alert/monitor built for this (CLAUDE.md s.5 moratorium) -- this is a dated, one-time observation, not a proposal for one."
  },
  {
    "id": "NFRA_COMPEFFICACY-S3",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T03:58:00Z",
    "one_line": "S2's phenomenon RECURRED at the CVO seat 03:53Z-03:58Z: 3 of 3 --corpus aws pulls at the default 90 s budget (unscoped x2, one with no kill preceding; scoped LAMBDA x1) returned BUDGET REACHED with 0 of 1 unit(s) scanned -- the backend is not returning within 90 s from this seat; S2's 'self-resolved, transient' is falsified; mechanism unknown.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO 03:53Z: `comp-find --corpus aws opal-gateway --budget 1` -> 'BUDGET REACHED: 1 s (flag); scanned 0 of 1 pull(s)', rc 0, 2 s wall (the forced control; expected)",
        "3.0.0_SA_CVO 03:54Z: `comp-find --corpus aws opal-gateway` (default) -> 'BUDGET REACHED: 90 s (default); scanned 0 of 1 pull(s)'; 'ALL: did not return within the remaining budget (TimeoutExpired)'; rc 0; 91 s wall",
        "3.0.0_SA_CVO 03:57Z: `comp-find --corpus aws opal-gateway LAMBDA` (scoped unit, default) -> 'BUDGET REACHED: 90 s (default); scanned 0 of 1 node_type(s) ... NO CURSOR YET'; rc 0; 91 s wall",
        "3.0.0_SA_CVO 03:58Z: `comp-find --corpus aws opal-gateway` (default; no kill preceding; no other aws-corpus call from this seat in the prior minute) -> BUDGET REACHED 90 s; rc 0; 91 s wall",
        "`ps -ef | grep -i 'kuzu|comp_kuzu|globgrph'` at 03:5xZ: no leftover process from the --budget 1 kill; infra/aws/globgrph/kuzu_nessie_db 82,661,376 B, mtime 2026-09-02 20:36:15 LOCAL = 2026-09-03T00:36:15Z, unchanged",
        "Contrast, the worker's own measurements (row S2, 0.8.0_AE_CloudComp): five pulls 7.4-13.8 s at 02:26Z-03:07Z; battery in-budget at 03:25Z (19.68 s, ten arms)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.4 s.4.4.1 (and the T1 deliverable) assume the --corpus aws pull completes in single-digit-to-low-teens seconds under normal conditions, the basis for the 90 s default; row S2 asserts the 03:16Z-03:24Z degradation 'self-resolved by 03:25Z' with the worker's own call burst as the leading hypothesis.",
    "world_is": "At 03:53Z-03:58Z, from a different seat with two prior aws-corpus calls in the session and none in the preceding minute, the same pulls did not return within 90 s on 3 of 3 attempts, scoped and unscoped alike. Whatever the mechanism, it is not confined to one seat's burst and it is present about 30 minutes after the claimed self-resolution. Rule T behaved: an honest prefix and rc 0 every time, never a hang.",
    "notes": "CVO's own row per the corrected law (the row is the carrier). CVO CHECK OF S2, recorded here because S2 is append-only: (a) grain -- kuzu_nessie_db size matches S2; S2's mtime '2026-09-02T20:36Z' is a LOCAL time carrying a Z (the `ls` trap), true value 2026-09-03T00:36:15Z; S2's conclusion (no write in the window) stands; (b) S2's invitation to close DISMISSED_WITH_REASON is NOT taken -- its 'self-resolved' claim is falsified by this row, so S2 stays UNDER_INVESTIGATION with this row as its live carrier; (c) mechanism still ungrounded, so neither row can honestly seed a remediation row yet. THIS ROW does not block the current turn (TO-CE-T-1 is terminal) but IS an ARMED hazard under normal future operation: every --corpus aws query at the default budget currently returns a PREFIX with 0 scanned, so any consumer of the live AWS plane reads silence. DISARM is urgent and off-cadence (protocol s.6): 0.8.0_AE_CloudComp, comp-kuzu's tool owner and the round's live Tier-2 seat, diagnoses NOW whether the pull is stalled locally (Kuzu native library / lock) or upstream (the CloudTrail-driven incremental refresh; GLOBGRPH_KUZU_INCREMENTAL_REFRESH defaults to 1 at comp-find :155) -- one discriminating measurement is `--mode inc` against a non-incremental read of the same DB. REMEDIATION rides the round: S2/S3 GRADUATE to a remediation row only when the mechanism is grounded; until then they stay open and, per protocol s.7, an open item is not a zero -- L10 routing of round 1 WAITS on it. No monitor, no alert (CLAUDE.md s.5)."
  },
  {
    "id": "NFRA_COMPEFFICACY-S4",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T04:05:00Z",
    "one_line": "CLOSES NFRA_COMPEFFICACY-S1 (L9 adjudication; a new row because rows are append-only): S1's closing condition is MET ON THE RECORD -- the rework onto the s.4.4 form landed and is on origin, the T1 report cites it, the checker reads VALID at this seat, TO-CE-T-1 is terminal; DISMISSED_WITH_REASON, nothing to carry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 2718cffc45 (0.8.0_AE_CloudComp, 03:33:05Z) ON origin/CLOUD (0.0.0_AB_MSTR 93021, ls-remote 03:42:12Z; re-read at 3.0.0_SA_CVO 03:4xZ); READ on its bytes at 3.0.0_SA_CVO: .tools/_compbudget.py 123 lines new; .tools/comp-find carries BUDGET REACHED x6, WITHIN BUDGET x1, --cursor x8, COMP_BUDGET_S x2, the interim '--budget-s' x0",
        "0.8.0_AE_CloudComp 93025 (T1 deliverable report, 03:52:23Z) cites 2718cffc45 and the s.4.4 form; T1-AC3/AC4 stated in the landed grammar",
        "`python .tools/proof-of-spec-check.py <T1 instance>` run at 3.0.0_SA_CVO 03:5xZ -> VALID rc 0; surprises-frame 2 entries, 2 resolve to channel rows, mode ENFORCE; alignment 6/6, 1/1, 1/1; artifacts 4 CONTENT-resolved",
        "TO-CE-T-1 <status> complete ON THE RECORD @fc5ec7106c (2.0.0_SA_COO 93031); the bound amendment S1 cites via 92960 is in the TO file @2e90f4e06c",
        "Other-seat exercise of the rework at 3.0.0_SA_CVO: `comp-find --corpus aws opal-gateway --budget 1` -> 'BUDGET REACHED: 1 s (flag) ... NO CURSOR ...' + 'NOT a measured zero', rc 0, 2 s; `comp-find --help` discloses --budget > env COMP_BUDGET_S > default 90 s and --budget 0 = unbounded"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Handled in-round; nothing to carry to a remediation row. The TO's own Grammar clause anticipated the form landing mid-round; the issuer amended the bound in-round (92960 -> @2e90f4e06c); the owner's rework under the live TO was both the disarm and the remedy, and it has landed on origin and been read on its bytes and exercised from a second seat. Residual, INERT, owner 0.8.0_AE_CloudComp at next touch: .tools/_compbudget.py's docstring attributes the decision record to '1.0.0_SA_CVO', a serial that does not exist (it is 3.0.0_SA_CVO @790d92c6fa).",
    "spec_asserts": "S1's own closing condition (S1.notes): 'flips to DISMISSED_WITH_REASON when 0.8.0_AE_CloudComp's reworked commit lands and the T1 deliverable report cites the s.4.4 form (T1-AC4 in the landed grammar); if the rework does not land before the TO's report, the item GRADUATES to a remediation row instead.'",
    "world_is": "Both halves met on the record before the TO's report closed: the rework 2718cffc45 landed at 03:33Z and reached origin at 03:42Z; the report 93025 at 03:52Z cites it and the form. The graduation branch did not fire.",
    "notes": "L9 form note: the surprise-row gate refused an in-place disposition flip on S1 (EXISTING row MUTATED in place; corrections are NEW items citing the old id), so this row is the closure carrier and S1's own disposition field stays UNDER_INVESTIGATION by construction. A reader resolving S1's state reads the newest row citing it."
  },
  {
    "id": "NFRA_COMPEFFICACY-S5",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp",
    "surfaced_at": "2026-09-03T04:16:43Z",
    "one_line": "GROUNDS S2/S3: the --corpus aws BUDGET REACHED phenomenon is LOCAL, not upstream/AWS-side -- a live, legitimate infra/aws/globgrph/kuzu_nessie_load.py rebuild subprocess (PID 25896) has been holding the canonical DB's shared rebuild mutex since 04:07:26Z, still running at 04:16:02Z (515s, under its own 600s incremental timeout); comp-find's own 90s Rule-T budget kills the CLIENT's wait-for-rebuild loop before the mutex-wait (180s) or the rebuild itself would resolve. S3's disarm-owner assignment discharged; mechanism GROUNDED.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/globgrph/_canonical.py source read (this seat, 04:1xZ): every --corpus aws call (comp-find -> kuzu_cli.py --mode inc) runs _canonical.ensure_fresh() SYNCHRONOUSLY, INSIDE the same subprocess comp-find times, BEFORE the DB is opened or the query runs; ensure_fresh() takes a mkdir-mutex (kuzu_nessie_db.rebuild.lock) -- one caller becomes the rebuild winner (subprocess.run of kuzu_nessie_load.py, INCREMENTAL_TIMEOUT_S=600 / REBUILD_TIMEOUT_S=1800), every other concurrent caller polls every RECHECK_SLEEP_S=2.5s for up to MUTEX_WAIT_S=180s before falling back to serving the existing (labeled-stale) DB",
        "_liveness_on() defaults OFF (env GLOBGRPH_KUZU_REBUILD_LIVENESS unset on this box) -- 'the exact pre-#17 behavior (shared tmp, 900s-only steal, no heartbeat/gen-check)', so an EMPTY kuzu_nessie_db.rebuild.lock/ (no gen, no heartbeat file) is NORMAL for any in-progress rebuild here, healthy or dead alike -- absence of a heartbeat file is NOT itself evidence of an orphan under this config, which the S2/S3 rows did not have (corrected here, not asserted there)",
        "kuzu_nessie_db.rebuild.lock/ measured present, empty, mtime age 320.5s at first read (04:1xZ)",
        "Get-CimInstance Win32_Process (PowerShell, not MSYS ps -- the estate's own instrument trap for detached Windows processes): PID 25896, CommandLine 'python ... infra\\aws\\globgrph\\kuzu_nessie_load.py --db ...\\kuzu_nessie_db.rebuild.tmp', StartTime 2026-09-03T04:07:26Z (UTC, computed from the process object's local StartTime + ToUniversalTime(), not read off a filename or a log line)",
        "Re-measured 2026-09-03T04:16:02Z: PID 25896 still alive, elapsed 515.46s -- WITHIN its own INCREMENTAL_TIMEOUT_S=600s ceiling (not yet hung by the code's own standard), and within the lock's ORPHAN_LOCK_S=900s steal backstop -- a caller checking now would correctly NOT steal this lock",
        "Comparison: this specific PID (25896, started 04:07:26Z) post-dates BOTH S2's degraded window (03:16Z-03:20Z, this seat) and S3's (03:53Z-03:58Z, CVO) -- it is a LATER, SEPARATE rebuild attempt, not the one that caused those two windows. Evidence therefore supports a RECURRING pattern (repeated rebuild attempts, each taking longer than comp-find's 90s default) rather than one isolated stall; the mechanism generalizes, the specific PID does not retroactively explain S2/S3's own windows"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S3's disarm instruction: 'diagnoses NOW whether the pull is stalled locally (Kuzu native library / lock) or upstream (the CloudTrail-driven incremental refresh)... one discriminating measurement is --mode inc against a non-incremental read of the same DB.'",
    "world_is": "LOCALLY stalled, confirmed by a live process, not a hypothesis: a real kuzu_nessie_load.py rebuild subprocess is the thing every --corpus aws caller is waiting behind via the shared mutex. It is not stuck by the code's own definitions (under both the incremental and orphan-lock ceilings) -- it is simply SLOW relative to comp-find's 90s Rule-T default, and it appears to recur (a fresh rebuild attempt was live at 04:07Z, well after the two incidents already on record).",
    "notes": "DISARM DISCHARGED: mechanism named, LOCAL, with a live-process citation rather than an unconfirmed hypothesis -- S2/S3's own 'either local contention or AWS-side throttling' is resolved in the LOCAL direction, specifically. NOT CHASED FURTHER, stated so the boundary is explicit: why the rebuild cadence is frequent enough to be caught THREE separate times in under an hour (00:36Z DB write per S2/S3, then windows at 03:16Z, 03:53Z, and this live one at 04:07Z) is a comp-kuzu/globgrph maintenance question, not a comp-find one, and is NOT this seat's to own -- named here as the natural next question, not answered here (CLAUDE.md s.2: the next check would not change what this cell does). No code change proposed or made under this row; Rule T's 90s default is PRD-ratified and this row does not ask to revisit it. GRADUATION / REMEDIATION is 3.0.0_SA_CVO's call at L9 (remediation rows are CVO's by design, per the annex @d1220c4971) -- candidates visible from here, not chosen here: (a) document the rebuild-window behavior as expected in PRD s.4.4's non-application notes for comp-kuzu-backed tools, (b) a comp-kuzu-side fast-path that serves the existing DB immediately when a rebuild is already in progress rather than making every caller wait on the same mutex, (c) nothing -- an occasional honest BUDGET REACHED during a real rebuild may simply be Rule T doing its job. Push state: none of this row's evidence is a commit; PID/timing measurements are point-in-time and will read differently by the time anyone re-checks."
  },
  {
    "id": "NFRA_COMPEFFICACY-S6",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T04:21:00Z",
    "one_line": "DISPOSITIONS S2 + S3 + S5 (one item) as DECOMP_INVALIDATING and STAMPS the route to L5: the mechanism is grounded and REFINED at this seat -- comp-find's Rule T budget kill removes the mutex WINNER (the kuzu client), the grandchild rebuild survives ORPHANED holding the lock past its own 600 s ceiling, every later caller waits 180 s > the 90 s default and prints BUDGET REACHED, and the 900 s steal restarts the cycle; the decomposition has no cell for the freshness layer's behavior under a budgeted client.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S5's source claims verified at 3.0.0_SA_CVO on infra/aws/globgrph/_canonical.py at worktree HEAD: MUTEX_WAIT_S=180.0 (:44), ORPHAN_LOCK_S=900.0 (:47), RECHECK_SLEEP_S=2.5 (:48), REBUILD_TIMEOUT_S 1800 (:66), INCREMENTAL_TIMEOUT_S 600 (:67), _liveness_on() env-gated (:70-74), ensure_fresh (:534), lock = db_path + '.rebuild.lock' (:561), the loser wait loop (:590-598)",
        "Win32 process table (Get-CimInstance, UTC computed from CreationDate) at 04:19:49Z: PID 25896 'python kuzu_nessie_load.py --db ...kuzu_nessie_db.rebuild.tmp' started 04:07:26Z, elapsed 743 s -- PAST its own INCREMENTAL_TIMEOUT_S of 600 s, which only a live parent enforces",
        "04:21:19Z: PID 25896's ParentProcessId 26552 is NOT IN THE PROCESS TABLE; no python process matching kuzu_cli|comp-find|comp_kuzu is alive -- the rebuild is ORPHANED: its supervising client was killed and the subprocess timeout died with it (subprocess.run(timeout=) kills the direct child, never the grandchild)",
        "infra/aws/globgrph/ at 04:20:01Z: kuzu_nessie_db.rebuild.lock/ present (mtime 04:07:22Z = the PID's start); kuzu_nessie_db.rebuild.tmp 43,851,776 B and .tmp.wal 13,475,398 B with mtime 04:20:01Z -- the orphan is still writing; the canonical DB 82,661,376 B unchanged since 00:36:15Z",
        "The cycle, from the code and the three measured windows (03:16Z-03:24Z worker, 03:53Z-03:58Z CVO, 04:07Z-now): a budgeted client becomes the winner, spawns the rebuild, is killed at its 90 s budget; the orphan holds the lock; every caller waits MUTEX_WAIT_S 180 s > 90 s -> BUDGET REACHED with 0 scanned; at ORPHAN_LOCK_S 900 s the next caller steals the lock and becomes a new winner -> a new rebuild -> the same kill",
        "Decomp v0.1.2 cells read: CE-t-22 closes on the KUZUSPLIT PRD half and NEVER-full on --mode inc; CE-g-2 closes on the stale-served AGE being bounded or stated; neither names the freshness layer's mutex wait or the orphaning of a rebuild under a client-side budget. PRD v0.4 s.4.4 binds the CLIENT's budget and DEFERRED bucket; it does not see the layer beneath it"
      ]
    },
    "disposition": "DECOMP_INVALIDATING",
    "spec_asserts": "Decomp v0.1.2 (CE-t-22 'comp-kuzu engine CLEARED', CE-g-2 'stale-served path bound') and PRD v0.4 s.4.4 (Rule T: subprocess timeouts derive from the remaining budget; overruns are DEFERRED) together assert that a budgeted comp-find call over --corpus aws degrades to an honest prefix and nothing else happens.",
    "world_is": "Something else happens: the budget kill orphans the rebuild the killed client started, the orphan holds the shared mutex unsupervised past the ceiling its dead parent would have enforced, and every later caller on the same DB is blocked for longer than the default budget until the 900 s steal restarts the cycle. Rule T's client-side form, applied to a backend with a synchronous rebuild-and-wait freshness layer, CREATES the recurring outage it was written to disclose. Rule T still behaved (honest prefix, rc 0, never a hang); the surface it exposed is unenumerated.",
    "notes": "L9: DECOMP_INVALIDATING, not GRADUATED -- the remedy needs a cell the decomposition does not contain (the freshness layer under a budgeted client: a killed client must not orphan its rebuild -- process-group kill or detach-by-design with a status the losers read; serve the existing DB immediately while a rebuild is in progress instead of waiting MUTEX_WAIT_S; reconcile MUTEX_WAIT_S 180 s with the 90 s default; the rebuild cadence measured). Per protocol s.4 it routes BACKWARD and never also forward, so no remediation row is written for this item. L10 STAMP by 3.0.0_SA_CVO: loop_target 5, owner 2.0.0_SA_COO (re-decompose: add the cell; its executor is the comp-kuzu engine lane, 0.8.0_AE_CloudComp per CE-t-22). PRECONDITION READ: every task order under the project is terminal (TO-CE-T-1 complete @fc5ec7106c; DISC-2 and TP-1 withdrawn); every row is dispositioned by its newest citing row (S1 by S4; S2, S3, S5 by this row); 0 graduated. Round 1 therefore closes by the backward route: no next L6 dispatch until L5 has the cell. DISARM (S5's owner, unchanged): do not kill PID 25896 -- it is writing and the 900 s steal covers a dead one; callers needing the AWS plane before the fix pass --budget >= 300 and read the disclosure; the disarm is reported as a new row citing this one. INERT residual carried, not a finding here: .tools/_compbudget.py's docstring names a serial that does not exist. Push state: this row's evidence is point-in-time; the process table will read differently at any later check."
  },
  {
    "id": "NFRA_COMPEFFICACY-S7",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp",
    "surfaced_at": "2026-09-03T04:26:20Z",
    "one_line": "DISARM ACK on S6's stamp: PID 25896 left untouched (not killed); the interim guidance (--budget >= 300 for any --corpus aws caller before the L5 fix lands) is adopted and will be carried into this seat's own future --corpus aws use; the INERT docstring residual S1/S4/S6 each carried forward was already fixed at S5's own commit (39886d04bd), same commit, before S6 read it -- a citation gap, not an unfixed defect.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "0.8.0_AE_CloudComp",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PID 25896 NOT signaled or killed by this seat at any point -- confirmed by this seat's own command history: no Stop-Process / kill invocation against it appears anywhere in this session",
        ".tools/_compbudget.py line 2 read at this write: 'landed by 3.0.0_SA_CVO's decision record @790d92c6fa' -- the fix already present; git log -1 --format=%H -- .tools/_compbudget.py at this write resolves to 39886d04bd, the SAME commit that added row S5 (both file changes were staged together, one safe-commit call) -- the docstring fix PRE-DATES S6 (04:21Z) and S4 (04:0xZ) 's own carry-forward notes by commit-time (39886d04bd landed before this seat's S6 read), so 'rides your next touch' had already discharged when it was written; not a new act",
        "No new comp-find --corpus aws invocation made by this seat since S6 landed -- the interim >=300s guidance is acknowledged here for this seat's OWN future compliance, not yet exercised (nothing in round 1 currently requires another live pull)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both halves of S6's disarm ask are satisfied: the orphan was left alone (no action taken, none needed beyond restraint), and the docstring fix S1/S4/S6 each flagged as outstanding was already landed at S5's own commit -- discovered here to have already discharged, not freshly done. Nothing further owed by this seat under S6; the L5 decomposition (owner 2.0.0_SA_COO) and any resulting L6/L7 dispatch are separate, future acts this row does not anticipate or claim.",
    "spec_asserts": "S6's disarm text: 'do NOT kill PID 25896 ... until the fix, a caller that needs the AWS plane passes --budget >= 300 and reads the disclosure. Report the disarm as a NEW row citing S6.' and 'The INERT residual (the _compbudget.py docstring's non-existent serial) rides your next touch.'",
    "world_is": "PID 25896 was left running, untouched, per instruction. The docstring correction S6 (and S4 before it) each carried as still-outstanding was, in fact, already committed at 39886d04bd -- the same commit as S5 -- so by the time S6 was written the residual had already ridden this seat's 'next touch' (S5's own commit), and the carry-forward note in S4/S6 was reading a stale state of the file rather than its HEAD.",
    "notes": "Filed to close the loop on S6's two-part ask cleanly and to correct the small provenance gap (S4/S6 both cited a residual as still-owed when it was already paid) rather than let a reader chase a fix that already landed. This does not contest S6's DECOMP_INVALIDATING disposition, its L5 route, or its ownership assignment -- all of that stands. No code change made under this row; --budget >= 300 is adopted as this seat's own practice going forward, not a code default (Rule T's 90 s default remains PRD-ratified pending the L5 cell). Push state: 39886d04bd's push state is stated in row S5's own commit history, unchanged by this row."
  },
  {
    "id": "NFRA_COMPEFFICACY-S8",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T05:50:00Z",
    "one_line": "ADJUDICATES S1 (machine carrier for the closure S4 gave in prose before the `adjudicates` field existed): DISMISSED_WITH_REASON -- the mid-round grammar landing was handled in-round; the rework landed on origin, the T1 report cited the form, the checker read VALID; nothing to carry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row S4 @db508e75b4 (the closure of S1, with its five evidence items: rework 2718cffc45 on origin and read on its bytes; T1 report 93025; proof-of-spec-check VALID at 3.0.0_SA_CVO; TO-CE-T-1 terminal @fc5ec7106c; the other-seat exercise)",
        ".tools/surprise-row-gate.py live census at 3.0.0_SA_CVO 05:4xZ: NFRA_COMPEFFICACY 7 items, undispositioned by machine reading = S1, S2, S3, S5 (the prose closures in S4/S6 are not readable by the gate)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "As S4 states: handled in-round -- the TO's Grammar clause anticipated the form landing mid-round, the issuer amended the bound (92960 -> @2e90f4e06c), the owner's rework under the live TO was both the disarm and the remedy, landed on origin, read on its bytes and exercised from a second seat. This row restates S4's closure in the carrier gate (iii)'s second limb reads.",
    "spec_asserts": "S1.notes closing condition: 'flips to DISMISSED_WITH_REASON when 0.8.0_AE_CloudComp's reworked commit lands and the T1 deliverable report cites the s.4.4 form; if the rework does not land before the TO's report, the item GRADUATES instead.'",
    "world_is": "Both halves met on the record before the TO's report closed (S4's evidence); the graduation branch did not fire.",
    "notes": "Form note: S4 already carries this disposition and reason; it predates the `adjudicates` carrier (@4774db2c87), so the gate reads S1 as undispositioned. This row adds the machine-readable link and nothing else."
  },
  {
    "id": "NFRA_COMPEFFICACY-S9",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T05:50:00Z",
    "one_line": "ADJUDICATES S2 + S3 + S5 (one item, the AWS-corpus pull under Rule T): DISMISSED_WITH_REASON -- REMEDIED. Round 1's DECOMP_INVALIDATING route (S6) was taken: decomp v0.2 added cell CE-g-5, TO-CE-G-5 is complete with a VALID proof, the fix landed (@173dd335f4), and the remedy is EXERCISED at this seat: the same default-budget pull that expired 3 of 3 at 03:53Z-03:58Z now returns WITHIN BUDGET in 14.34 s with 2,100 nodes scanned; no kuzu process alive.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S2",
      "NFRA_COMPEFFICACY-S3",
      "NFRA_COMPEFFICACY-S5"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 173dd335f4 (0.8.0_AE_CloudComp): fix(NFRA_COMPEFFICACY CE-g-5): comp-kuzu freshness layer -- a killed budgeted client no longer orphans its rebuild; infra/aws/globgrph/_canonical.py +109/-x, kuzu_cli.py +11/-x, .tools/tests/test_comp_find_battery.py +147 (git show --stat at 3.0.0_SA_CVO)",
        "TO-CE-G-5 status complete @7e3b23578d (self-committed under the lane grant); deliverable + proof @9852efdfb3; python .tools/proof-of-spec-check.py on the instance at 3.0.0_SA_CVO 05:4xZ -> VALID rc 0, 6 of 6 criteria -> CE-g-5, surprises-frame 0 entries, mode ENFORCE",
        "EXERCISED at 3.0.0_SA_CVO 2026-09-03T05:46Z: `comp-find --corpus aws opal-gateway` (default budget) -> 'WITHIN BUDGET: scanned 1 of 1 pull; budget: 90 s (default), used 14.34 s'; 'DENOMINATOR: 34 hit(s) across 2100 aws node(s) scanned [corpus=aws]'; rc 0; 15 s wall -- against the same query's 3 of 3 BUDGET REACHED at 90 s from this seat at 03:53Z-03:58Z (S3)",
        "Win32 process table at 05:46:39Z: no python process matching kuzu_nessie_load|kuzu_cli (the round-1 orphan PID 25896 is gone); infra/aws/globgrph/ still carries kuzu_nessie_db.rebuild.lock/, .rebuild.tmp and .rebuild.tmp.wal from the round-1 orphan and the fixed layer served within budget through them",
        "Task-order census at HEAD: DISC-2 WITHDRAWN, TP-1 WITHDRAWN, T-1 complete, G-5 complete, T-2 complete (5 of 5 terminal); TO-CE-T-2's proof instance VALID at this seat too (6 of 6, 0 surprises)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIED, and the remedy exercised by a seat that did not build it. The mechanism S6 grounded (a budgeted client's kill orphaning the mutex winner; every later caller waiting past the budget; the 900 s steal restarting the cycle) is closed by the CE-g-5 fix; DISARM and REMEDIATION have both landed (two states, two clocks, both now past). Nothing graduates forward: no remediation row, no route.",
    "spec_asserts": "S6's stamp: 'DECOMP_INVALIDATING; loop_target 5, owner 2.0.0_SA_COO -- add the cell for the freshness layer under a budgeted client; executor the comp-kuzu engine lane; round 1 closes by the backward route.'",
    "world_is": "The backward route ran forward again through L10: decomp v0.2 (CE-g-5) at L5, TO-CE-G-5 at L6, the fix at L7 with a VALID proof and 0 surprise rows, and the behaviour the item named no longer occurs at this seat.",
    "notes": "L10 STAMP, ROUND 2 (3.0.0_SA_CVO, 05:5xZ). PRECONDITION READ ON THE RECORD: every task order under the project is terminal (5 of 5: 2 WITHDRAWN, 3 complete) and each complete one carries a VALID proof-of-spec instance whose surprises resolve (T-1: 2 of 2; G-5 and T-2: 0 entries) -- checked at this seat with the gate's own instrument; every investigation item is dispositioned by its latest carrier once this row lands (S1 by S8; S2/S3/S5 by this row; S4, S6, S7 terminal on their own face). GRADUATION: 0. ROUTES: 0. A zero-graduation round: PROCEED TO THE NEXT L6 DISPATCHES (2.0.0_SA_COO: STAGE 1's CE-t-3, STAGE 2's CE-t-8 next in the decomposition's order); dep_stage ROUND_CLOSE flips on this stamp by the row owner. READ AND NOT COUNTED, stated so the count is honest: three FINDINGS inside the round-2 deliverables (G5-F1: no persistent per-trigger log for a true 24 h rebuild-cadence count, owner named in the deliverable; T2-F1: comp-read --at beyond a file's range has no NOT_APPLICABLE voice; T2-F2: --enumerate writes no rail row) are the audits' own content, not spec-versus-world surprises of their task orders; they ride the project's per-tool carrier (PRD s.7 rows versioned by 1.0.0_SA_CTO on each grade; the decomposition's CE-t cells) and are not rows here. INERT residual, not a row: the stale rebuild.lock/.tmp/.wal files from the round-1 orphan remain on disk; the fixed layer serves through them and its steal logic covers them; a cleanup is the comp-kuzu lane's at next touch, via the COO. No monitor, no alert."
  },
  {
    "id": "NFRA_COMPEFFICACY-S10",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T08:02:00Z",
    "one_line": "comp-surprise (the L8 rollup named in annex s.7) reads each row's OWN `disposition` and has no notion of the `adjudicates` carrier (0 occurrences in .tools/comp-surprise.py, 233 lines; :171 filters on the row's own disposition against OPEN_DISPOSITIONS), so after round 2's slug it reports S1/S2/S3/S5 as OPEN + ARMED (closed by S8/S9) and the routing row S6 as OPEN (its route executed): 5 phantom-open of the estate's 73 open by that instrument, all in this project, while the row gate's census reads 0 undispositioned. Two instruments, two answers, on the channel's own state.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-read .tools/comp-surprise.py --enumerate 'adjudicates|remediation|DISMISSED|GRADUATED|open' at 3.0.0_SA_CVO 07:5xZ: 38 hits, none the token `adjudicates`; :171 openi = rows whose own disposition is in OPEN_DISPOSITIONS; :196 prints OPEN as UNDER_INVESTIGATION / DECOMP_INVALIDATING -- the row's own field, never a later carrier's",
        "python .tools/comp-surprise.py --project NFRA_COMPEFFICACY --json at 07:5xZ: open = [S1, S2, S3, S5, S6], armed = the same five; estate-wide open = 73",
        "own census over both roots at 07:5xZ (20 investigation documents, 207 rows): rows carrying `adjudicates` = 2 (S8 -> [S1]; S9 -> [S2, S3, S5]); ids closed by a carrier = 4; every one of the 4 appears in the rollup's open list; S6 is the one open id not named by any carrier (a DECOMP_INVALIDATING routing row whose route was taken)",
        ".tools/surprise-row-gate.py on this file at 07:5xZ: '0 new row(s) of 9 total checked'; the round-2 slug @88c961297b was admitted by the gate's second limb (adjudicates) and its census read 0 undispositioned (round-2 step log seq 4)",
        "org/ref/SURPRISE_CHANNEL_PROTOCOL.md v2.1 @450f7ecf2e s.0 (append-only; a disposition or correction is a NEW row citing the old id), s.7 (`comp-surprise` is the rollup over both roots), s.8 (every item dispositioned by its latest carrier is the L10 precondition)",
        "git log .tools/comp-surprise.py: last @d6ed64fd5d (1.0.0_SA_CTO, 09-03T00:08Z, lanes ANY + LOOP_MECHANISM); no .owned-paths.yaml line names it (falls under the wider .tools rule)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "SURPRISE_CHANNEL_PROTOCOL.md v2.1: s.0 'append-only as a control -- a correction is a NEW row citing the old id', s.4 the `adjudicates` field ('an existing item dispositioned by a new row'), s.7 '`comp-surprise` is the rollup over both roots' (the L8 intake's aggregate), s.8 'every investigation row is dispositioned' read by its latest carrier -- the rule the row gate's second limb applies.",
    "world_is": "comp-surprise's open and armed lists count rows by their own `disposition` field; a row named in a later row's `adjudicates` stays open and armed, and a DECOMP_INVALIDATING routing row stays open after its route has executed. Read at 07:5xZ: open=5 armed=5 for NFRA_COMPEFFICACY against the gate's 0 undispositioned.",
    "notes": "DISARM = comp-surprise treating a row as CLOSED when any later row's `adjudicates` names it (the latest carrier's disposition governs, the row gate's own rule) and saying so on its denominator line; the S6 facet is closed on this channel by S11 (adjudicates S6) so the single fix leaves 0 phantom-open here. HARM WHILE UNATTENDED: /govern (hourly at 0.0.0_AB_MSTR, LD-0527) and fabric-check read the rollup's ARMED list; five phantom ARMED items on a project whose rounds are stamped invite a false escalation or a false hold on its close. NOT blocking any task order. The remedy lies in the loop mechanism, not this project's chain: per 1.0.0_SA_CTO 93320 limb (i), the disarm_owner fixes IN PLACE within lane, then this row is dispositioned DISMISSED_WITH_REASON citing the fix commit; nothing routes. Surfaced after the round-3 stamp @7ec9bf06dd (a round-4 item); the surfacing seat appended its own row, no message as carrier."
  },
  {
    "id": "NFRA_COMPEFFICACY-S11",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T08:02:00Z",
    "one_line": "ADJUDICATES S6 (round 1's DECOMP_INVALIDATING routing row): DISMISSED_WITH_REASON -- the route it stamped (-> L5) was TAKEN and ran forward through L10 (decomp v0.2 cell CE-g-5; TO-CE-G-5 complete @7e3b23578d with a VALID proof; fix @173dd335f4; S9 closed the item S6 belongs to as REMEDIED). A routing row is a carrier of its item, not a second item; this row gives it a machine closure so a reader counting rows finds no phantom open route.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S6"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_COMPEFFICACY-S9 @88c961297b (adjudicates S2/S3/S5, DISMISSED_WITH_REASON, REMEDIED, the remedy exercised at this seat)",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md v0.2.1 @070907b56e: CE-g-5 'DONE as TO (v0.2.1) -- TO-CE-G-5 complete'",
        "the round-2 L10 stamp section of this file @88c961297b read S6 as 'terminal on its own face'; comp-surprise --project NFRA_COMPEFFICACY at 07:5xZ listed S6 OPEN + ARMED (S10)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The route S6 stamped executed end to end and the item it carries is closed by S9. No remediation row, no route, nothing graduates.",
    "spec_asserts": "Annex s.8: 'A DECOMP_INVALIDATING row reopens L5 for the current round at once' -- a routing act, terminal once the loop has run forward through L10 (annex s.8 'The loop').",
    "world_is": "The loop ran (v0.2 at L5, TO-CE-G-5 at L6/L7, the round-2 stamp at L10), yet the row itself carried no closure a row-counting reader can see, and comp-surprise listed it open at 07:5xZ.",
    "notes": "L9 act of 3.0.0_SA_CVO after the round-3 stamp @7ec9bf06dd; a documentation row -- no state of the project moves; the gate's mutation limb is why this is a new row and not an edit to S6."
  },
  {
    "id": "NFRA_COMPEFFICACY-S12",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T08:17:00Z",
    "one_line": "ADJUDICATES S10 (the rollup's `adjudicates` blindness): DISMISSED_WITH_REASON -- DISARMED IN PLACE by its disarm_owner 1.0.0_SA_CTO @2bc3679e0b (.tools/comp-surprise.py +34/-x: dispositions resolve by LATEST carrier -- own row, then adjudicating rows in file order, later wins; every item carries `_latest` in --json), and the disarm EXERCISED at this seat 08:16:10Z: `comp-surprise --project NFRA_COMPEFFICACY --json` open = [S10], armed = [S10] (was 5 and 5); S1 `_latest` DISMISSED_WITH_REASON, S6 `_latest` DISMISSED_WITH_REASON; estate open 73 -> 70; negative control NFRA_CLDGRPH still reads its 8 genuinely open rows. Per 1.0.0_SA_CTO 93320 limb (i): fixed within lane, no semantics changed, nothing routes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S10"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit 2bc3679e0b (1.0.0_SA_CTO, 08:14Z): gates(three instrument gaps from the two live runs) -- .tools/comp-surprise.py 34 lines changed, .tools/proof-of-spec-check.py 102, org/standards/COMPTOOL_ANSWER_STATE.enum.json 2, infra/system/06_current_state.{json,md}; git merge-base --is-ancestor 2bc3679e0b HEAD -> rc 0 at 3.0.0_SA_CVO",
        "EXERCISED at 3.0.0_SA_CVO 2026-09-03T08:16:10Z, a seat that did not build it: python .tools/comp-surprise.py --project NFRA_COMPEFFICACY --json -> open ['NFRA_COMPEFFICACY-S10'], armed ['NFRA_COMPEFFICACY-S10']; items S1 own UNDER_INVESTIGATION / _latest DISMISSED_WITH_REASON, S6 own DECOMP_INVALIDATING / _latest DISMISSED_WITH_REASON, S11 own = _latest DISMISSED_WITH_REASON",
        "NEGATIVE CONTROL, same instrument, same minute: --json estate open 73 (07:5xZ, pre-fix) -> 70 (08:16:10Z, post-fix); --project NFRA_CLDGRPH open 8 = its 8 rows, all genuinely open on their own face at that read -- the fix removed phantoms and left real open rows in place",
        "1.0.0_SA_CTO 93349 (the disarm owner's report): 'dispositions resolve by LATEST carrier exactly as surprise-row-gate's second limb does'; 'the one is S10 ITSELF ... correctly live until 3.0.0_SA_CVO dispositions it at L9'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed in place by the disarm_owner within its lane and the disarm exercised by a second seat; the rollup and the row gate now read the same state from the same file. No remediation row, no route, nothing graduates; the channel's own instrument is whole again.",
    "spec_asserts": "S10's DISARM as written: 'comp-surprise treating a row as CLOSED when any later row's `adjudicates` names it (the latest carrier's disposition governs, the row gate's own rule) and saying so' -- annex v2.1 s.0/s.4/s.7/s.8.",
    "world_is": "comp-surprise.py @2bc3679e0b resolves every item to its latest carrier and exposes it as `_latest`; on this channel the only open item is S10 itself until this row lands, after which the rollup reads 0 open and 0 armed for NFRA_COMPEFFICACY (to be read, not assumed, on the next stamp).",
    "notes": "L9 act of 3.0.0_SA_CVO on the disarm owner's report; a round-4 item closed inside its round. The estate 'armed' count (87 at the exercise) now exceeds 'open' (70) by design -- ARMED includes GRADUATED-not-DISARMED items -- which is the CTO's semantics and not a finding of this row. Nothing routes; the next L6 is unaffected; a CLOSE of this project no longer waits on S10."
  },
  {
    "id": "NFRA_COMPEFFICACY-S13",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T09:21:00Z",
    "one_line": "TO-CE-T-9 (comp-trigger) closes on AC-2 and its T9-AC2 criterion asks for 'four PLANTED cases ... four DISTINGUISHABLE, machine-rejectable outputs'; the deliverable's own answer_state block records THREE of the four planted cases (SUBJECT_ABSENT_FROM_CORPUS, PRESENT_WITH_ZERO_RESULTS, PARTIAL_OR_BLIND) printing BYTE-IDENTICAL bodies at rc 0 -- comp-trigger has no function-existence check -- and the proof instance self-marks T9-AC2 PASS on 'the criterion's controlling ask'. PRD s.4.3: 'PASS = four cases, four distinguishable outputs. FAIL = any two states print alike. This is FWD-2 and it is the load-bearing test of the project.' The world is a FAIL by the spec's own bar; the second clause (the S3-notification scope + delegation line) IS met and stays.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-T-9.comp-trigger-s4-audit.md (complete @b1295d1164), criterion T9-AC2 verbatim: '(AC-2) four PLANTED cases keyed on the ratified enum produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case); the S3-notification-only function reads out-of-scope / NOT_APPLICABLE with the scope + delegation line' -- two clauses, conjoined",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md v0.4 @19bf1c7322 s.4.3 :390: '**PASS** = four cases, four distinguishable outputs. **FAIL** = any two states print alike. This is FWD-2 and it is the load-bearing test of the project.'",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md v0.2.2 @b7daeaa6f0 :118 'STAGE 2  THE 4.3 ANSWER-STATE FIXES (each closes on AC-2)' and :58 CE-t-9 outcome_ref 'FWD-2,3,4 + AC-2'",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-trigger.result.md @b1dab0b6a0, answer_state block: PRESENT_WITH_ZERO_RESULTS 'printed': 'BYTE-IDENTICAL to the SUBJECT_ABSENT case above'; PARTIAL_OR_BLIND 'printed': 'the SAME NO MATCH text as the two cases above, PLUS the new SCOPE line' with 'distinguishable_from_the_others_by': 'nothing in THIS run alone (same rc, same NO MATCH text)'; finding F1 'guard-asymmetry (three states, one guard)' citing comp_trigger.py:render()'s `if not matches:` branch @7737320640",
        "the proof instance NFRA_COMPEFFICACY.TO-CE-T-9.comp-trigger-s4-audit.proof_of_spec.json @b1dab0b6a0, row T9-AC2 status PASS, status_reason: \"the first clause's 'four DISTINGUISHABLE outputs' is met only 2 of 4 ways at the text level ... reported as PASS because the criterion's controlling ask (the S3-notification voice) is satisfied and the shortfall is fully disclosed as finding F1\" -- read at 3.0.0_SA_CVO; the instance is structurally VALID (proof-of-spec-check rc 0) and the checker does not grade a criterion's truth",
        "STAGE 2's subject-existence cell CE-t-6 (:55) is T-6 comp-blast's own row ('subject-existence + graph vintage + node denominator; NOT-FOUND != zero radius'), not a cross-tool home -- so no cell other than CE-t-9 carries comp-trigger's existence check"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "T9-AC2 (the TO face, frozen for the round) and PRD s.4.3 (the bar the cell closes on): four planted cases produce four distinguishable outputs; any two alike is FAIL; this is FWD-2.",
    "world_is": "Three of comp-trigger's four planted cases print byte-identical bodies at rc 0 (no function-existence check; the S3-only case differs from PRESENT_WITH_ZERO only by a scope line that prints on every miss), and the proof instance carries PASS on that criterion by reading its second clause as controlling. The task order is complete on the record with a valid instance; the cell's AC-2 is not met.",
    "notes": "GRADUATED: the remedy needs a task order under a cell the decomposition already contains (CE-t-9) -> route SPEC_ERROR, loop_target 6, owner 2.0.0_SA_COO -- the remediation row of the same id in REMEDIATION_v1.md carries the remedy. DISARM (the tool lane's, via the COO): a function-existence check that separates SUBJECT_ABSENT_FROM_CORPUS from the other three is the minimal disarm; the S3-notification-only case still needs the cell's own closes-on ('S3-notification backend via existing machinery; existing machinery checked FIRST') or a distinct PARTIAL_OR_BLIND voice to separate it from PRESENT_WITH_ZERO_RESULTS. Harm while unattended: a mistyped or retired function name reads as 'exists, no EventBridge/Scheduler trigger, check S3 notifications' -- a reader is sent to chase notifications on a function that does not exist (the wrong-object class s.4.1 closes at the schema and s.4.3 tests). FOR THE GRADE (1.0.0_SA_CTO, COMPLETION_GRADES): T9-AC2 reads FAIL by s.4.3's bar, self-marked PASS with the shortfall disclosed -- the disclosure is honest, the mark is not the spec's. The worker's F1 is the same fact in the per-tool carrier; this row exists because the fact contradicts the TO's own criterion, which S9's precedent (findings inside a deliverable are not rows) never covered. Not blocking any task order (the round's orders are terminal)."
  },
  {
    "id": "NFRA_COMPEFFICACY-S14",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T09:21:00Z",
    "one_line": "Rule T's FORM (PRD s.4.4) fixes 'at expiry ... rc stays 0 (the LINE is the rejectable state, not the rc)' for every marquis tool; comp-dataflow's `gate` subcommand is a GATE archetype whose rc IS the verdict by its own contract, so a BUDGET-REACHED sweep with 0 findings among the files it reached returns rc 0 -- byte-identical to a genuinely complete clean sweep -- and any rc-only consumer (a hook, a script, a `&&`) reads PARTIAL as CLEAN. The PRD names no outcome for a gate archetype at expiry: its non-application clause covers tools with no corpus-width loop and no timeout-bearing subprocess, and nothing else. An uncovered member of the form's own domain (Rule 24 (i)); deliverable finding T7-F4, 'sharper here than in prior cells'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md v0.4 @19bf1c7322 s.4.4 :432 'at expiry       on stdout, BEFORE the summary, rc stays 0 (the LINE is the rejectable state, not the rc)'; :462-471 the non-application clause (no corpus-width loop AND no timeout-bearing subprocess; output caps do not exempt) -- no archetype distinction anywhere in the form (read at full width at 3.0.0_SA_CVO)",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-dataflow.result.md @803539f490, finding F4 'success-token-bound-to-wrong-step, SHARPER here than in prior cells': 'a BUDGET-REACHED (partial) gate sweep with 0 findings among the reached files still returns rc=0 -- byte-identical to a genuinely complete clean sweep's rc ... this tool's GATE archetype (rc IS the verdict, by design) makes an rc-only caller's mis-read materially more consequential', citing org/modules/graph/comp_dataflow.py:cmd_gate() @8fdc3d0602 (the cell's own new code; disclosed in --help's carrier description)",
        "2.0.0_SA_COO 93421, sequencer read (2): 'Rule T's documented behaviour, but comp-dataflow's GATE archetype binds rc to the VERDICT ... A candidate for the s.4.4 form's next clause or a STAGE-3 cell, at the L4 owner's grain' -- named so it does not vanish into a deliverable",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md v0.2.2 @b7daeaa6f0 :93 CE-tp-1: 'DONE v0.1.2 -- APPLIED as SPEC at L4 ... s.4.4 is the ONE carrier' -- the form is a PRD clause, owned at L4, not a cell a task order can amend",
        "1.0.0_SA_CTO 93320: the route enum answers 'what does the remedy need that does not exist yet in this project's chain' -- an outcome the PRD does not name is SCOPE_CHANGE -> L2"
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "PRD s.4.4 RULE T's FORM: at expiry rc stays 0 and the BUDGET REACHED line is the rejectable state -- stated for every marquis tool, with a non-application clause that names only no-loop/no-subprocess tools; and comp-dataflow's own gate contract (T7-AC6 / --help): the gate's rc is its verdict.",
    "world_is": "For a gate archetype the two specs collide: honouring the form makes a budget-cut sweep return the CLEAN verdict; honouring the gate contract would violate the form's rc clause. The PRD names no outcome for what a gate does at expiry, so the cell built to the form and disclosed the hazard rather than resolving it (correctly: a worker may not amend the PRD).",
    "notes": "GRADUATED: the remedy needs an OUTCOME the PRD does not name (what a verdict-bearing tool returns from a partial run) -> route SCOPE_CHANGE, scope_change_kind REQUIRES_UNNAMED_OUTCOME, outcome_ref null, loop_target 2, owner 1.0.0_SA_CTO (re-align at L2, then the PRD at L4 -- s.4.4's next clause -- then L5/L6 forward for the comp-dataflow change). The remediation row of the same id in REMEDIATION_v1.md carries the proposed outcome in plain English. DISARM (the tool lane's, via the COO, once the outcome is named -- nothing is built against the current form before that): cmd_gate at BUDGET REACHED returns a distinct non-clean rc, or refuses to render a verdict on a partial sweep. Harm while unattended: a gate that passes on a partial sweep is the false-green class (CLAUDE.md s.5 'a monitor on an unsettled route measures the wrong thing precisely' is the same shape one rung up); comp-dataflow gate has 11 runs in 30 days by the manifest, so the exposure is small today and grows with every hook that adopts it. Not blocking any task order. T7-F1 (vintage stderr-only), T7-F2 (SUBJECT_ABSENT and NOT_APPLICABLE share one REFUSE shape and rc, distinguishable by the echoed argument), T7-F3 (the shim's un-budgeted self-report, owner named) ride the per-tool carrier; F2 is named for the L4 owner's grade against s.4.3's bar."
  },
  {
    "id": "NFRA_COMPEFFICACY-S15",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp",
    "surfaced_at": "2026-09-03T12:05:00Z",
    "one_line": "TO-CE-T-9R's own delegation target -- comp-aws's S3_BUCKET -[TRIGGERS]-> LAMBDA edge (org/modules/graph/comp_aws_cli.py:1439-1447, derive_edges()) -- is EMPTY across the WHOLE live graph (0 rows, MATCH (b:CloudNode)-[e:CloudEdge]->(l:CloudNode) WHERE b.node_type='S3_BUCKET' AND e.edge_type='TRIGGERS' AND l.node_type='LAMBDA' RETURN b.name, l.name), despite the estate carrying multiple REAL aws_s3_bucket_notification Terraform resources with real Lambda targets (bd-pipeline/cot-pipeline/inf-pipeline s3-notifications.tf). Specimen checked live: opal-data-bd IS an S3_BUCKET node in the graph (confirms round-4's F3 'account-scope, undetermined' was TIME-BOUND to a since-superseded graph vintage -- the bucket is present now), but it carries ZERO outgoing TRIGGERS edges (only CONTAINS edges to S3Key content nodes) despite Terraform declaring 3 real Lambda notification targets on it (ProcessAllocationFiles/bd-allocation-processor, GoldLayerPricesTrigger/bd-gold-trigger, BronzeCompleteSilverMerge/bd-silver-merge). The edge-derivation code's own get_bucket_notification_configuration call is wrapped in a bare `except: pass` (comp_aws_cli.py:1446-1447) -- a failed read for THIS bucket (permissions, region, or another cause) is structurally indistinguishable from a bucket that genuinely has no notifications, and the tool's own node-property twin (event_notifications count, :273-279) shows the identical silent-zero shape for the same bucket. TO-CE-T-9R names this exact edge as the measured delegation for comp-trigger's S3-notification PARTIAL_OR_BLIND separation; with 0 real edges anywhere in the graph, no LIVE specimen can exercise that branch honestly -- comp-trigger's own code is being written to query this edge correctly, but the round's own quoted real-world demonstration cannot be produced from the graph as it currently stands. This is a comp-aws/graph-lane finding, out of comp-trigger's BOUNDS to fix (comp_aws_cli.py is consumed, not edited, under this TO).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "comp-aws/graph lane (org/modules/graph/comp_aws_cli.py), owner TBD -- not this seat's lane under TO-CE-T-9R's BOUNDS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python infra/aws/globgrph/kuzu_cli.py --json --mode inc \"MATCH (b:CloudNode)-[e:CloudEdge]->(l:CloudNode) WHERE b.node_type='S3_BUCKET' AND e.edge_type='TRIGGERS' AND l.node_type='LAMBDA' RETURN b.name, l.name LIMIT 20\" -> 0 rows, DB kuzu_nessie_db built 2026-09-03T11:41:09Z (age 0.2h at read)",
        "python infra/aws/globgrph/kuzu_cli.py --json --mode inc \"MATCH (n:CloudNode) WHERE n.node_type='S3_BUCKET' AND n.name='opal-data-bd' RETURN n.name, n.arn\" -> 1 row (present, arn:aws:s3:::opal-data-bd) -- same read, confirming the bucket IS modeled, only its TRIGGERS edges are not",
        "python infra/aws/globgrph/kuzu_cli.py --json --mode inc \"MATCH (b:CloudNode)-[e:CloudEdge]->(l:CloudNode) WHERE b.node_type='S3_BUCKET' AND b.name='opal-data-bd' RETURN e.edge_type, l.name, l.node_type\" -> only CONTAINS edges to S3Key nodes; zero TRIGGERS edges of any kind from this bucket",
        "infra/aws/terraform/bd-pipeline/s3-notifications.tf @4cd024c5c6's own resource aws_s3_bucket_notification.bd_data_bucket, read in full this project's round-4 cell: 3 real lambda_function blocks (ProcessAllocationFiles->bd-allocation-processor, GoldLayerPricesTrigger->bd-gold-trigger, BronzeCompleteSilverMerge->bd-silver-merge), verified LIVE via the TF comment's own citation of a get-bucket-notification-configuration capture ('live has exactly 3 LambdaFunctionConfigurations') at declare-time (2026-07-15)",
        "org/modules/graph/comp_aws_cli.py:1439-1447 @ HEAD (comp-read --enumerate confirmed): `nc = s3c.get_bucket_notification_configuration(Bucket=n['id']); for lf in nc.get('LambdaFunctionConfigurations', []): E(...)` inside a bare `except: pass` -- a failed call for this bucket produces the SAME zero-edges result as a bucket with a genuinely empty notification config",
        "org/modules/graph/comp_aws_cli.py:273-279's node-property twin (event_notifications/notify_sns/notify_sqs) shows the identical silent-zero-on-exception shape for the same API call, one derivation pass over"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CE-T-9R's DELIVERABLE item 2 and T9R-AC3, quoting the round-4 measurement: 'the graph's S3_BUCKET notification fields (comp_aws_cli.py:273-279, the delegation your round-4 order measured) ... a bucket whose notification names the subject makes the answer PARTIAL_OR_BLIND naming the bucket and event class.'",
    "world_is": "The measured delegation exists as CODE (both the node-property counter and the edge deriver) but its DATA is empty across the entire live graph for this specific relationship (0 of an expected >=3 real edges), traced to a silently-swallowed exception in the same code path for at least one real, TF-confirmed specimen (opal-data-bd). The delegation is real but currently non-functional as a source of live PARTIAL_OR_BLIND evidence.",
    "notes": "Not blocking TO-CE-T-9R's own completion: the existence-check and S3-separation CODE in comp_trigger.py is written and battery-tested against FIXTURE data (a mocked graph response) proving the Cypher logic and rendering are correct; the deliverable states plainly that no live specimen currently exercises the PARTIAL_OR_BLIND branch for this reason, citing this row, rather than fabricating or silently omitting the gap. Fixing comp_aws_cli.py's silent-exception shape (e.g. distinguishing UNREADABLE from a genuine zero, matching this project's own Rule-22a-style discipline) is out of this seat's lane under TO-CE-T-9R's BOUNDS (comp_aws_cli.py consumed, not edited) and is left for the graph lane's owner to pick up."
  },
  {
    "id": "NFRA_COMPEFFICACY-S16",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~A",
    "surfaced_at": "2026-09-03T12:04:28Z",
    "one_line": "DISARMS NFRA_COMPEFFICACY-S14 (disarm_owner 0.8.0_AE_CloudComp~A): under TO-CE-T-25 (the L2/L4 outcome PRD v0.5 FWD-10 named), comp-dataflow's cmd_gate now returns RC_NOT_DECIDABLE (4) at BUDGET REACHED -- ALWAYS, regardless of whether the reached units carried a finding -- distinct from RC_CLEAN (0) and RC_FINDINGS (1); a real rc-only consumer (a shell &&) correctly does not proceed past a budget-cut sweep, and the cursor followed to completion yields the true verdict. EXERCISING the fix's own DONE WHEN (not asked for, required to build it) found and fixed a SEPARATE, pre-existing bug in the same code path: total_units was measured BEFORE the --cursor filter, so a cursor-resumed run that completed 100% of its own remaining units still read a stale n<N and could never reach a true verdict -- without this second fix, FWD-10's own resume promise ('the resume cursor has been followed to completion') would have been unsatisfiable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_NFRA_COMPEFFICACY_20260903T0930Z.md @5bbdab5ec7 CALL 1 ruled (a); PRD NFRA_COMPEFFICACY v0.5 @5bbdab5ec7 FWD-10 + s.4.4 'verdict-bearing' row (quoted verbatim in the TO and the deliverable)",
        "commit 72e7846ca7 (0.8.0_AE_CloudComp~A): org/modules/graph/comp_dataflow.py -- RC_CLEAN/RC_FINDINGS/RC_USAGE/RC_REFUSED/RC_NOT_DECIDABLE named constants (rc=4 adopted, not the iam_cli.py:50 family precedent's rc=2, because this tool's own rc=2 was already occupied by RC_USAGE before this cell); STATE_NOT_DECIDABLE printed as a new line at BUDGET REACHED; the --cursor total_units bug found and fixed in the same commit; .tools/tests/test_comp_dataflow_battery.py +3 arms",
        "EXERCISED live at this seat (this cell's own session, quoted in the deliverable): `gate data/ --budget 0.001` -> rc=4, a real subprocess.run rc-only check (the same signal a shell && reads) does not proceed; `gate data/ --budget 30` (ample, no cursor needed for the 8.8s-baseline tree) -> rc=1, a TRUE verdict; separately, following the printed --cursor with an ample budget -> rc=1, the true verdict, confirming the fix (BEFORE the fix, this exact sequence reproduced reproducibly at rc=4 forever: 531 of a stale 532 total, 0 actually deferred)",
        "python .tools/tests/test_comp_dataflow_battery.py -- 11/11 PASS (8 round-4 arms unaffected + 3 new: VERDICT-RC-CONSUMER, VERDICT-RC-VOCABULARY, MUTANT-VERDICT-RC -- the last reproduces the exact FWD-10 violation on demand via a planted mutant, RED-first, confirming the control is real)",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-dataflow.fwd10.result.md @<this cell's deliverable commit> -- the rc vocabulary table, both EXERCISED runs quoted, production sha256 before/after"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S14's own DISARM instruction (notes): 'cmd_gate at BUDGET REACHED returns a distinct non-clean rc, or refuses to render a verdict on a partial sweep' -- once the outcome is named at L2/L4 (which it now is, FWD-10).",
    "world_is": "The outcome is named (FWD-10, PRD v0.5) and the code now matches it, EXERCISED end-to-end including the DONE WHEN's own resume-to-completion half, which required fixing a second, previously-unknown bug to actually satisfy. Both the BUDGET REACHED line's text and the rc are now consistent with a verdict-bearing tool never reporting a partial run as clean.",
    "notes": "DISARM reported, disposition intentionally left for 3.0.0_SA_CVO's own L9 adjudication (per the TO's own words: 'the disposition stays 3.0.0_SA_CVO's'), matching the S3/S5 precedent (S5 discharged S3's disarm-owner assignment while leaving disposition UNDER_INVESTIGATION for CVO's own subsequent row). hazard_standing set INERT here because the code fix is landed, committed, and exercised -- not because this row purports to close S14 itself. Residual, not fixed here per BOUNDS (_compbudget.py consumed, not edited): if the verdict-bearing expiry-rc form belongs in the shared module so the next verdict-bearing cell inherits it rather than re-deriving its own rc vocabulary, that is a FINDING carried in the deliverable for the L4 owner and the sequencer to place, not a change made under this one-tool cell. Push state: commit 72e7846ca7 is LOCAL as of this row's write, measured via ls-remote + is-ancestor in the deliverable report, not asserted here."
  },
  {
    "id": "NFRA_COMPEFFICACY-S17",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~B",
    "surfaced_at": "2026-09-03T12:08:17Z",
    "one_line": "R-4's 'if so' -- the SUBSET CONDITION the whole of TO-CE-T-19 is gated on -- is NOT MET at the traversal grain, measured at this seat with a different instrument from the L4 owner's line-range cite. PRD v0.5 s.7 row T-19 carries claim=measured on 'strict subset of blast (cli.py:1478-1530)', but that line range IS the two argparse PARSER blocks, and the parsers themselves already carry the counter-evidence: comp-trace has --exact and --all, which comp-blast REFUSES as unrecognized arguments (rc=1), and trace's --direction accepts upstream/downstream spellings blast does not. Those three are carryable. The axis that is NOT carryable is the UNIVERSE: comp-trace answers over a head-pinned working-tree scan (2,302 nodes: GOLD_SCRIPT 1383, S3_ARTIFACT 344, LAMBDA 337, ENDPOINT 146, EVENTBRIDGE 59), while comp-blast answers over kuzu (27,134 nodes) by Andrew-direct ruling 2026-08-03 with an explicit FAIL-LOUD-NEVER-FALL-BACK clause at cli.py:970-976. On a stratified sample of 158 of 2,302 real trace node ids, blast ANSWERS on the caller's own trace-id spelling for only 61 (38.6%) -- the other 97 (61.4%) are NOT-FOUND rc 3. Under the most generous mapping a forwarder could perform (strip the address prefix), blast still ANSWERS only 92 of 158 (58.2%), with 41 (25.9%) becoming AMBIGUOUS-SUBJECT rc 5 refusals and 25 (15.8%) NOT-FOUND. Building the declared-successor forwarder this order specifies would therefore convert roughly two in five working comp-trace calls into a NOT-FOUND -- the exact false-clear class both tools' rc=3 dials were built to prevent. Per the order's own instruction ('if the subset condition FAILS on a measured axis that cannot be carried, the order STOPS at a ROW and reports'), this cell STOPS here; the forwarder is NOT built and nothing is deleted.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (the L4 owner -- PRD s.7 row T-19's claim=measured and the R-4 heading are L4 carriers; routed via 2.0.0_SA_COO, the sequencer). NOT this seat's: a worker may not amend the PRD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md v0.5 @5bbdab5ec7 s.7 row T-19 verbatim: '| T-19 | FWD-4, FWD-5, FWD-8 | `comp-trace` -> `org/modules/graph/cli.py trace` | measured | 45 runs; **strict subset of blast** (`cli.py:1478-1530`) | CloudComp | retire | T-6 | R-4 |' -- the claim field reads `measured`; worktree byte-identical to the pin (git diff --quiet 5bbdab5ec7; 63969 bytes / 677 lines on both sides).",
        "org/modules/graph/cli.py, worktree byte-identical to the TO's cited pin @7b649df39d (git diff --quiet, with the pin resolving as a positive control). The cited range :1478-1530 IS the two parser blocks -- p_trace :1482-1495 declares --exact (store_true, 'A miss under --exact is NOT-FOUND (rc=3)'), --direction choices ['up','upstream','down','downstream','both'] default 'both', and --all ('Trace all matches'); p_blast :1498-1530 declares --direction choices ['up','down','both'] default None and has NEITHER --exact NOR --all.",
        "EXERCISED, real CLI, FLAG grain: `.tools/comp-blast gold:A_00.accounts_dimension --exact` -> rc=1, stderr 'cli.py: error: unrecognized arguments: --exact'. Controls on the sibling tool the same minute: `.tools/comp-trace gold:A_00.accounts_dimension --exact` -> rc=0; `.tools/comp-trace gold:A_00.accounts_dimension_NOPE --exact` -> rc=3 (the NOT-FOUND dial fires as documented).",
        "EXERCISED, real CLI, TRAVERSAL grain (4 queries, both tools, same session): gold:A_00.accounts_dimension -> trace rc=0 (16 stdout lines) / blast rc=0 (377 lines), BOTH ANSWER; lambda:access-anomaly-scanner -> trace rc=0 / blast rc=3 NOT-FOUND; s3:gold/dimensions/accounts_dimension_latest.parquet -> trace rc=0 (224 lines) / blast rc=3 NOT-FOUND; eventbridge:bd-allocation-pipeline-trigger -> trace rc=0 / blast rc=3 NOT-FOUND. Bare-name rescue attempted on the three failures: access-anomaly-scanner -> blast rc=0; bd-allocation-pipeline-trigger -> blast rc=0; gold/dimensions/accounts_dimension_latest.parquet -> blast rc=5 AMBIGUOUS-SUBJECT (a refusal, not an answer).",
        "POPULATION MEASUREMENT (stratified sample, seed 19, 158 of 2,302 trace node ids, each run through blast's OWN resolver `comp_blast_universe.resolve_subject` against the loaded kuzu universe -- the same entry point cmd_blast uses at cli.py:970): FULL trace-id spelling -> ANSWER 61 (38.6%), NOT-FOUND 97 (61.4%). BARE name -> ANSWER 92 (58.2%), AMBIGUOUS rc5 41 (25.9%), NOT-FOUND 25 (15.8%). Per type on the full-id spelling: GOLD_SCRIPT 25/25 ANSWER, but S3_ARTIFACT 0/25, LAMBDA 0/25, EVENTBRIDGE 0/25, SQS_QUEUE 0/5, S3_BUCKET 0/4, STATE_MACHINE 0/1, SNS_TOPIC 0/1; ENDPOINT 16/25, COMPONENT 20/22. NOTE ON MY OWN INSTRUMENT, recorded because it changes the number: a first pass counted any non-empty match set as a hit and read 133/158 (84.2%); that CONFLATED blast's AMBIGUOUS-SUBJECT rc=5 refusal with an answer and overstated coverage by 26 points. The corrected pass distinguishes the three outcomes and is the one reported here.",
        "STALENESS HYPOTHESIS KILLED (the cheapest competing explanation, tested rather than assumed): `load_kuzu_universe(refresh=True)` -- a FORCED refresh, kuzu graph_nodes last-write 0.0h -- still yields 27,134 nodes carrying ZERO node ids under the prefixes gold: (0), lambda: (0), s3: (0), eventbridge: (0), sqs: (0), sns: (0), sfn: (0), s3bucket: (0), and ZERO nodes of type GOLD_SCRIPT (0), S3_ARTIFACT (0), ENDPOINT (0), EVENTBRIDGE (0), COMPONENT (0). kuzu's own address space is motifi:/ms:/type:/jsx:/arn:/render:/pipeline:. This is a SCHEMA + ADDRESS-SPACE difference, not a vintage one: a refresh cannot add a node type the schema does not carry.",
        "org/modules/graph/cli.py:970-976 verbatim, why the gap cannot be closed inside this cell's BOUNDS: 'THE UNIVERSE IS KUZU / Andrew-direct 2026-08-03 ... FAIL LOUD, NEVER FALL BACK (spec 7): if kuzu is unreachable this exits 1 (TOOL FAILED). A silent fallback to the private scan would reproduce the exact defect the ruling removes' -- making blast answer over trace's universe would reverse a sovereign ruling, and is in any case CE-t-6's surface, which this order's BOUNDS place off-limits ('no change to blast's traversal, scoring or verdict semantics')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.5 @5bbdab5ec7 s.7 row T-19, claim=measured: comp-trace is a 'strict subset of blast (cli.py:1478-1530)'; and the R-4 heading (:609), Andrew 2026-09-02 'comp-trace ... if so it should be retired.' with the L4 owner's note 'Condition MET (trace subset-of blast at cli.py:1478-1530)'. TO-CE-T-19's own DELIVERABLE item 1 makes that condition the gate and requires it re-derived at this seat with a different instrument from the L4 owner's.",
    "world_is": "Re-derived here by enumerating both parsers' flag sets and by running both tools over a stratified sample of the real node population, rather than by reading the cited line range as prose. The condition does not hold. At the FLAG grain trace carries --exact, --all and the upstream/downstream direction spellings that blast rejects (--exact measured at rc=1, 'unrecognized arguments'). At the TRAVERSAL grain the two tools answer over different graphs with disjoint address spaces and disjoint node-type schemas, so blast answers only 38.6% of trace's own node ids as the caller spells them, and only 58.2% under the most generous prefix-stripping mapping. The first three are carryable into blast's parser exactly as the order anticipates; the universe gap is not, and it is the one the ruling's 'if so' actually turns on.",
    "notes": "STOPPED AT THIS ROW, per TO-CE-T-19 DELIVERABLE item 1's own instruction and T19-AC1 ('...or a ROW and a stop'). NOT DONE, and deliberately so: the .tools/comp-trace forwarder is NOT built, nothing is deleted, no registry carrier is edited, cli.py is unmodified (production sha unchanged). Building the forwarder on the current measurement would silently convert ~61% of working comp-trace invocations (or ~42% with the best prefix mapping) into NOT-FOUND rc 3 or AMBIGUOUS rc 5, against 45 real runs in the 30d window by three seats -- the false-clear class that cli.py:377-380 and :1006-1010 exist to prevent, reintroduced through the retirement rather than through a typo. WHAT THE DISARM NEEDS (1.0.0_SA_CTO, via 2.0.0_SA_COO): (a) PRD s.7 T-19's claim=measured corrected, since it is the carrier another cell reads -- CE-t-6 (comp-blast) is recorded as depending on THIS cell; and (b) R-4 re-adjudicated on the corrected measurement, because Andrew's ruling is CONDITIONAL and this seat measures the condition unmet. The honest options a re-adjudication chooses between are: retire comp-trace anyway and accept the coverage loss as a DECISION rather than a subset claim; keep comp-trace and close T-19 as NOT-RETIRED with this measurement as its evidence; or widen the cell to carry trace's universe into blast, which is a CE-t-6 / L2 scope change and not a T-19 act. This seat expresses no preference among the three; the choice is the L4 owner's and, on (b), plausibly Andrew's, since it is his ruling's own condition that failed. CARRYABLE REMAINDER, unbuilt and left for whichever cell the sequencer places it in: --exact, --all and the upstream/downstream direction aliases are genuine trace-only capability that any retirement must carry into blast's parser rather than drop silently -- they are bounded to the blast parser + render exactly as the order scopes them, and they remain correct work whichever way (b) is decided. No other cell is blocked: CE-t-9 (base) and CE-t-25 (~A) carry no dependency either way."
  },
  {
    "id": "NFRA_COMPEFFICACY-S18",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp",
    "surfaced_at": "2026-09-03T12:20:00Z",
    "one_line": "DISARMS NFRA_COMPEFFICACY-S13 (disarm_owner 0.8.0_AE_CloudComp): under TO-CE-T-9R (PRD v0.5 s.4.3's GRAIN amendment), comp_trigger.py now separates all four ratified answer-states with a literal ANSWER-STATE: <TOKEN> line, never sharing a token across states -- a real function-existence check (live graph LAMBDA nodes via kuzu_cli.py, zero new AWS calls, + Terraform aws_lambda_function declarations including the module-wrapped shape) separates SUBJECT_ABSENT_FROM_CORPUS (rc 3, new distinct value) from the other three; the graph's real S3_BUCKET-[TRIGGERS]->LAMBDA edge (queried directly, zero new AWS calls) separates PARTIAL_OR_BLIND from PRESENT_WITH_ZERO_RESULTS. EXERCISING the fix found and filed a SEPARATE finding (NFRA_COMPEFFICACY-S15, this same commit): the S3-notification delegation's live DATA is empty estate-wide (a comp-aws-side gap), so the PARTIAL_OR_BLIND branch is proven end-to-end against a fixture rather than a live specimen -- disclosed in the deliverable, not hidden.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit a140eed779 (0.8.0_AE_CloudComp): org/modules/graph/comp_trigger.py +255/-15 -- STATE_SUBJECT_ABSENT/STATE_PRESENT_ZERO/STATE_PARTIAL_BLIND/STATE_NOT_APPLICABLE constants; _resolve_existence() (graph LAMBDA lookup via the existing kuzu_cli.py subprocess + tf_lambda_declared(), a brace-depth-aware Terraform scan covering BOTH the literal resource shape and the module-wrapped shape); _check_s3_notification() (a direct Cypher query for the real TRIGGERS edge); render() now branches on existence/s3_check to print one of the four tokens, never falling through one undifferentiated `if not matches:` body; an UNAVAILABLE/DEFERRED graph read is never collapsed into ABSENT (existence reads NOT-DECIDABLE, rc 2, in that case). .tools/tests/test_comp_trigger_battery.py +3 arms (11/11 total)",
        "EXERCISED live at this seat, real production binary, real AWS reads (list_rules/list_schedules/graph queries), zero mocks: `comp-trigger ZZZ_NONEXISTENT_FUNCTION_93999` -> ANSWER-STATE: SUBJECT_ABSENT_FROM_CORPUS, rc 3; `comp-trigger bd-price-update` -> ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS, rc 0 (existence FOUND via the module-wrapped TF shape AND the live graph); `comp-trigger --list --region us-west-2` -> ANSWER-STATE: NOT_APPLICABLE, rc 0; `comp-trigger bd-gold-trigger` (a real hit, 3 EventBridge rules) unaffected, rc 0",
        "embedded self-test 14/14 -> 20/20 (6 new cases including render.six_of_six_pairs_distinct: 6 of 6 pairs of {hit, absent, present-zero, partial(fixture)} bodies differ BY TOKEN, not merely by the echoed query argument -- the exact discriminator PRD v0.5's GRAIN sentence requires); external battery 8/8 -> 11/11, including two red-first mutants (CT9R-MUTANT-S13-COLLAPSE-DETECTED: a mutant reproducing the EXACT S13 shape correctly loses all three tokens; CT9R-MUTANT-UNAVAILABLE-AS-ABSENT-DETECTED: a mutant silently collapsing UNAVAILABLE into ABSENT is caught) -- both confirmed direct and under pytest",
        "deliverable amendment org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/comp-trigger.result.md, a NEW dated section above the round-4 record (kept, unchanged) quoting PRD v0.5 s.4.3 verbatim and re-planting all four cases with rc + full text"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S13's own remedy text is satisfied: 'a function-existence check ... that separates SUBJECT_ABSENT_FROM_CORPUS; and the S3-notification-only case separated ... by the cell's own closes-on (existing machinery) or by a distinct PARTIAL_OR_BLIND voice'. Both landed, both exercised (the first live, the second against a fixture with the live-data gap disclosed as S15). This row records the tool-lane disarm; S13's own L9 disposition (GRADUATED) is 3.0.0_SA_CVO's to close or carry forward, not touched here.",
    "spec_asserts": "S13's remediation row (REMEDIATION_v1.md, same id) and TO-CE-T-9R's own acceptance T9R-AC1..AC5, quoting PRD v0.5 s.4.3's PASS/FAIL and GRAIN sentences verbatim.",
    "world_is": "comp_trigger.py's four answer-states are now pairwise distinguishable by a literal, machine-rejectable token within one invocation's output -- measured directly (six of six pairs differ by token), not merely by the previously-sufficient-sounding-but-actually-collapsing scope+delegation line S13 correctly flagged as separating nothing.",
    "notes": "The PARTIAL_OR_BLIND branch's real-world exercise is currently blocked by S15 (a comp-aws-lane gap, out of this cell's BOUNDS to fix) -- not a gap in THIS fix. Certifier != author: this row does not grade T9R-AC1..AC5 as PASS on the record; that is the L4 owner's act at COMPLETION_GRADES, per the TO's own BOUNDS."
  },
  {
    "id": "NFRA_COMPEFFICACY-S19",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T14:28:00Z",
    "one_line": "ADJUDICATES S14 and its disarm carrier S16: DISMISSED_WITH_REASON -- REMEDIATED and DISARMED, both clocks landed and the disarm EXERCISED at this seat. The outcome the route asked for is named (FWD-10, PRD v0.5 @5bbdab5ec7) and s.4.4 carries the verdict-bearing row; TO-CE-T-25 is complete @97ebcf9931 with a VALID instance (5 of 5) whose surprises cite S14 and S16; the fix @72e7846ca7 returns rc 4 NOT-DECIDABLE at BUDGET REACHED. Run here 14:18Z: `comp-dataflow gate data/assets/scripts/gold --budget 0.001` -> rc 4, 'BUDGET REACHED ... scanned 1 of 102 producer_file ... resume: ... --cursor', 'STATE: NOT-DECIDABLE (rc=4, distinct from clean rc=0 and findings rc=1 -- a PREFIX carries no verdict)'. The remediation row S14 in REMEDIATION_v1.md carries the two states and closed=true in this same commit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S14",
      "NFRA_COMPEFFICACY-S16"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/NFRA_COMPEFFICACY.TO-CE-T-25.comp-dataflow-gate-under-fwd10.proof_of_spec.json @1bf60cae74: python .tools/proof-of-spec-check.py at 3.0.0_SA_CVO 14:1xZ -> VALID rc 0, 5 of 5 -> CE-t-25, surprises 2 entries resolving (S14@153522a509, S16@72e7846ca7), checker vintage 7b649df39d",
        "EXERCISED at 3.0.0_SA_CVO 2026-09-03T14:18Z: .tools/comp-dataflow gate data/assets/scripts/gold --budget 0.001 -> rc 4; stdout 'BUDGET REACHED: 0.001 s (flag); scanned 1 of 102 producer_file; results are a PREFIX, not the answer; resume: comp-dataflow gate data/assets/scripts/gold --budget 0.001 --cursor data/assets/scripts/gold/build_cottonwood_interpolated_backfill.py' and 'STATE: NOT-DECIDABLE  (rc=4, distinct from clean rc=0 and findings rc=1 -- a PREFIX carries no verdict)'",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md v0.5 @5bbdab5ec7: prd_version v0.5; FWD-10 at :158; s.4.4 'verdict-bearing (v0.5, FWD-10, S14)' at :457 (comp-read --enumerate at this seat, 10 hits)",
        "NFRA_COMPEFFICACY-S16 @710819ddc6 (0.8.0_AE_CloudComp~A): the disarm carrier, fix @72e7846ca7, hazard INERT, disposition left for this seat"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIATED (FWD-10 named at L2, the s.4.4 clause at L4, TO-CE-T-25 complete at L6/L7 with a VALID instance) and DISARMED (rc 4 at expiry, exercised by a seat that did not build it). Residual for the L4 owner, not a row: any other verdict-bearing marquis tool the census names, and T-25's F1 (whether the expiry rc form belongs in the shared _compbudget.py so the next verdict-bearing cell inherits it).",
    "spec_asserts": "S14's remediation row: 'at L2 name the outcome ... then s.4.4 ... then L5/L6 forward for the comp-dataflow change under CE-t-7'; the disarm 'cmd_gate at BUDGET REACHED returns a distinct non-clean rc, or refuses to render a verdict on a partial sweep'.",
    "world_is": "All three halves landed in order (93459 the L2 re-entry; PRD v0.5; decomp v0.2.3 CE-t-25; TO-CE-T-25 complete) and the exercised disarm reads rc 4 with the state token, with the cursor intact; the cell also fixed a second bug (total_units measured before the --cursor filter) that would have made FWD-10's own DONE WHEN unsatisfiable.",
    "notes": "S16 is the worker's disarm-report row and is closed with the item; its disposition was left to this seat as the TO's BOUNDS say. Under annex v2.3 a graduated item remedied in-round would be written as a REMEDIATED remediation row; S14 was routed before that clause existed and is closed on its own remediation row's clocks instead -- the law changed between the route and the close, and this row says so rather than leaving two shapes to read as an inconsistency."
  },
  {
    "id": "NFRA_COMPEFFICACY-S20",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T14:28:00Z",
    "one_line": "ADJUDICATES S13 and its disarm carrier S18: DISMISSED_WITH_REASON -- REMEDIATED and DISARMED, the disarm EXERCISED at this seat on the production binary. TO-CE-T-9R is complete @9bdcdaa5af with a VALID instance (5 of 5; surprises cite S18); the fix @a140eed779 gives comp_trigger.py a function-existence check and a literal ANSWER-STATE token per state. Run here 14:18Z, the four planted cases: ZZZ_NONEXISTENT_FUNCTION_93999 -> rc 3, ANSWER-STATE: SUBJECT_ABSENT_FROM_CORPUS; bd-price-update -> rc 0, PRESENT_WITH_ZERO_RESULTS; --list --region us-west-2 -> rc 0, NOT_APPLICABLE; bd-allocation-processor -> rc 0, PRESENT_WITH_ZERO_RESULTS -- the PARTIAL_OR_BLIND specimen reads PRESENT_WITH_ZERO live because the graph's S3_BUCKET-[TRIGGERS]->LAMBDA edge is empty estate-wide (S15), so three of four states are demonstrated live by token and the fourth by the cell's fixture over a correct query. The mechanism S13 asked for is complete; the live specimen for one state is blocked upstream of this project.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S13",
      "NFRA_COMPEFFICACY-S18"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp/NFRA_COMPEFFICACY.TO-CE-T-9R.comp-trigger-four-distinguishable-states.proof_of_spec.json @8abaa451d0: proof-of-spec-check at 3.0.0_SA_CVO 14:1xZ -> VALID rc 0, 5 of 5 -> CE-t-9, surprises 1 entry resolving (S18), checker 7b649df39d; row T9R-AC3 status_reason: 'PASS on the criterion's own controlling requirement ... the SPECIFIC named specimen (bd-allocation-processor) does not currently read PARTIAL_OR_BLIND live because the delegation's live data is empty (NFRA_COMPEFFICACY-S15 ...)'",
        "EXERCISED at 3.0.0_SA_CVO 2026-09-03T14:18Z on the production binary: .tools/comp-trigger ZZZ_NONEXISTENT_FUNCTION_93999 --budget 60 -> rc 3, 'ANSWER-STATE: SUBJECT_ABSENT_FROM_CORPUS'; bd-price-update -> rc 0, 'ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS'; bd-allocation-processor -> rc 0, 'ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS'; --list --region us-west-2 -> rc 0, 'ANSWER-STATE: NOT_APPLICABLE' -- three tokens distinct live, the fourth absent for the S15 reason",
        "commit a140eed779 (0.8.0_AE_CloudComp): fix(NFRA_COMPEFFICACY TO-CE-T-9R, S13 disarm) -- comp_trigger.py +255/-15; the T-9R flip @9bdcdaa5af (status complete at HEAD 6cabd10827)",
        "NFRA_COMPEFFICACY-S18 (0.8.0_AE_CloudComp, worktree at 12:20Z, integrated in this commit): 'six of six pairs differ by token'; NFRA_COMPEFFICACY-S15 @a140eed779: the TRIGGERS edge 0 rows estate-wide, opal-data-bd present with zero outgoing TRIGGERS edges against 3 Terraform-declared targets"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "REMEDIATED (the remediated order under CE-t-9 landed and closes on s.4.3's bar quoted; six of six token pairs distinct on the production binary) and DISARMED (the existence check separates SUBJECT_ABSENT_FROM_CORPUS at rc 3, exercised by a seat that did not build it). For the L4 owner's grade, stated here so the disclosure is not lost: T9R-AC3 carries PASS with a disclosed partial; under the limb-coverage bar FWD-2's comp-trigger limb is fixture-covered for PARTIAL_OR_BLIND until S15's owning surface derives the edge, and whether that grades REALIZED or NOT_EVALUATED is the CTO's call, not this row's.",
    "spec_asserts": "S13's remediation row: 'a remediated order under CE-t-9 that closes on PRD s.4.3's bar quoted, not restated: four planted cases, four distinguishable outputs in the tool's own voice. Minimally, a function-existence check ... and the S3-notification-only case separated ... by the cell's own closes-on or by a distinct PARTIAL_OR_BLIND voice'.",
    "world_is": "The order landed with both halves as code (existence check over the live graph's LAMBDA nodes plus the Terraform declarations; the S3 separation as a direct Cypher query on the TRIGGERS edge), the tokens are distinct within one invocation, and the one live specimen the fixture stands in for is blocked by an upstream data gap the same cell filed as S15.",
    "notes": "S18 is the worker's disarm-report row; the worker set its disposition to DISMISSED_WITH_REASON itself, which is the CVO's field -- harmless here, noted for the issuer as form. S18 was not at HEAD at this write (the worker's worktree row since 12:20Z, cited by TO-CE-T-9R's instance and by 93626); it is integrated into this commit under the gate's audited override so the slug can land, with its surfaced_by unchanged -- the pre-law filing practice retired this morning is not being revived, the row is the worker's and the override line says so."
  },
  {
    "id": "NFRA_COMPEFFICACY-S21",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T14:28:00Z",
    "one_line": "ADJUDICATES S15 (the graph's S3_BUCKET-[TRIGGERS]->LAMBDA edge empty estate-wide; comp_aws_cli.py derive_edges swallows a failed get_bucket_notification_configuration in a bare except, so a failed read is indistinguishable from a genuine zero): DISMISSED_WITH_REASON under 1.0.0_SA_CTO's reading 93320 limb (ii) -- the remedy lives outside this project's chain. comp-aws is not one of the 24 tool rows of this decomposition and org/modules/graph/comp_aws_cli.py is the graph engine NFRA_CLDGRPH is porting (the same class as that project's S2, S3 and S8: a defect in the thing being ported). The handoff record committed with this row places it with the owning surface's L6 owner and CVO; the consequence for THIS project is stated in S20: comp-trigger's PARTIAL_OR_BLIND live limb cannot be demonstrated until the edge derives honestly.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S15"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_COMPEFFICACY-S15 @a140eed779 (0.8.0_AE_CloudComp): the four Cypher reads, the Terraform resource with three lambda_function blocks, comp_aws_cli.py:1439-1447 and :273-279 (the bare except), the staleness hypothesis killed by a forced refresh -- carried as that seat's measurement",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md v0.2.3 @dcf07b4799: no CE-t row names comp-aws (python filter over every '| CE-t-' line at 3.0.0_SA_CVO 11:5xZ; only CE-t-9 mentions it as the delegation)",
        ".owned-paths.yaml: 'org/modules/graph/comp_*.py' under the GRAPH ENGINE HOME rule (CTO ruling 2026-08-20, msg 63234) -- 0.8.0_AE_CloudComp's comp-plane work lands there; 1.0.0_SA_CTO 93320 limb (ii): an outside remedy is DISMISSED_WITH_REASON naming the record that opens the owning surface's project",
        "NFRA_CLDGRPH REMEDIATION_v1.md @59af3f1df5 rows S2/S3/S8: the same class (defects in the engine being ported) routed SPEC_ERROR to 2.0.0_SA_COO~A's L6 port orders CG-s-2 + CG-s-9"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The remedy needs nothing that does not exist in this project's chain and everything that exists in another's: a fix to comp_aws_cli.py's derive_edges (a failed read reported as UNREADABLE, never as zero, and the TRIGGERS edge derived from the Terraform aws_s3_bucket_notification resources the estate declares) belongs to the graph engine's lane under NFRA_CLDGRPH, which is EXECUTING with a tree home. Record that opens it there: org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_HANDOFF_NFRA_COMPEFFICACY_S15_TO_NFRA_CLDGRPH_20260903T142xZ.md (this commit), relayed to 2.0.0_SA_COO~A and 3.0.0_SA_CVO~A. Nothing routes here; S15's disarm_owner field named a lane and not a seat, and the handoff names the seat class (0.8.0_AE_CloudComp under the GRAPH ENGINE HOME rule of .owned-paths.yaml, via that project's issuer).",
    "spec_asserts": "S15 (0.8.0_AE_CloudComp @a140eed779): TO-CE-T-9R's delegation target -- the graph's TRIGGERS edge -- is the measured machinery for comp-trigger's S3-notification PARTIAL_OR_BLIND separation; PRD s.4.3 asks four distinguishable outputs per tool.",
    "world_is": "The delegation exists as code (the edge deriver and the node-property counter) and its data is empty across the whole live graph for this relationship (0 of an expected >=3 real edges), traced to a silently swallowed exception for at least one real, Terraform-confirmed bucket; forced refresh does not change it.",
    "notes": "The decision that the remedy is outside the chain rests on two reads made here: decomp v0.2.3's tool rows (CE-t-1..25) carry no comp-aws cell, and .owned-paths.yaml's GRAPH ENGINE HOME rule places comp_*.py under the graph engine's lane. Under the limb-coverage bar (spine v2.5) the close of this project will read FWD-2's comp-trigger limb as fixture-covered until the owning surface delivers; that is disclosed, not hidden, and the L4 owner grades it."
  },
  {
    "id": "NFRA_COMPEFFICACY-S22",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T14:28:00Z",
    "one_line": "THIS SEAT'S OWN DEFECT ROW under drive v2 (LD-0530, obligation 6): the round-5 compile packet (93626, 12:42Z; pointer 93629, 12:46Z) waited about five ticks for its stamp. The seat was held by a usage-limit pause on the account and then by a tool call that did not return until 14:07Z (an exercise whose output redirect targeted an unwritable path); 93626 and 93629 sat in read/ unacked while the broker clock read OFFER-EXHAUSTED, the drive nudge 93645 (13:09Z) went unanswered until 14:13Z, and the round-5 stamp lands with this row at 14:2xZ.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/mcp/inbox/3.0.0_SA_CVO/read/20260903T124233Z_2.0.0_SA_COO_ROUND_5_of_NFRA_COMPEFFICACY_at_the_L10_.md (93626) and ...124635Z... (93629): both in read/ at 12:4xZ; READ-acked at 14:13Z (this seat's own ack call)",
        "2.0.0_SA_COO 93645 (13:09Z): 'your telemetry's last work row is 12:27Z (41 min, 0 rows since the handoff)'; answered (a) QUIET at 14:13Z",
        "this seat's own tool log: the comp-trigger exercise issued at 12:2xZ returned at 14:07:14Z with 'bash: /tmp_ct_out.txt: Permission denied' on each of three cases -- the redirect target, not the tool, was the fault; re-run to the scratchpad at 14:18Z in 0-2 s per case"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The cause was outside the loop (the account hold) plus one instrument fault at this seat (a redirect to a path the shell could not open, so the exercise neither ran nor returned promptly); the remedy is mechanical and lands this tick: CVO MODE of /drive armed at the 20-minute cadence at this seat, and every exercise script writes under the session scratchpad. No project state moved wrongly; the round's L7 was complete throughout and no worker waited on this seat.",
    "spec_asserts": "LD-0530 / drive v2 obligation 6 (MSTR 93661, 93674): 'compile packet received -> L9 adjudication and the L10 stamp in the tick that reads it; a packet older than one tick without a stamp is your own defect row'.",
    "world_is": "The packet aged about 100 minutes before its stamp; the telemetry's last work row was 12:27:19Z and the next act at this seat was 14:0xZ.",
    "notes": "Filed by the seat that owns the defect, on the project the packet belonged to, so the round table MSTR's brief measured (idle 15-33 min at the CVO between limbs) carries this round's number with its cause. Not blocking; the stamp is in this commit."
  },
  {
    "id": "NFRA_COMPEFFICACY-S23",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~F",
    "surfaced_at": "2026-09-03T14:51:33Z",
    "one_line": "TO-CE-T-12 and PRD v0.5 row T-12 assert DEPLOYED != COMMITTED for summary_corpus.py, but a separate globgrph derive-image rebuild completed after the order was cut and before this cell executed. The current served ECR image now carries the committed bytes exactly: opal-globgrph-derive-runner:latest digest sha256:3a4e078d2c65c0243f2aac3c2ad033ac7a154c12cc46d7b9998cf37601188486, pushed 2026-09-03T14:32:35Z, contains /app/org/modules/graph/debtscan/summary_corpus.py at 92,840 bytes with SHA-256 2c56cd7d50e8b3115d283ea95c5a29f8485ff0ec16f36a4e961ac60add7c6c85, equal to both the build-input ZIP member and the repo file. The historical PRE-fix image gap is no longer live; this cell records the changed world and does not rebuild or redeploy anything.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ecr describe-images at 0.8.0_AE_CloudComp~F, 2026-09-03T14:4xZ: opal-globgrph-derive-runner:latest -> image digest sha256:3a4e078d2c65c0243f2aac3c2ad033ac7a154c12cc46d7b9998cf37601188486, tag 20260903-143221, imagePushedAt 2026-09-03T14:32:35Z",
        "Rule-22a served-artifact read, not filename inference: aws ecr batch-get-image resolved Docker layer sha256:515c90b2a5b2a706939459cb0959dff4de573e312a06a2282f4b833ae4ef152f; get-download-url-for-layer + native tar extracted app/org/modules/graph/debtscan/summary_corpus.py, 92,840 bytes, SHA-256 2c56cd7d50e8b3115d283ea95c5a29f8485ff0ec16f36a4e961ac60add7c6c85",
        "infra/aws/globgrph/.build/derive-runner-source.zip, LastWriteTimeUtc 2026-09-03T14:31:25Z, member org/modules/graph/debtscan/summary_corpus.py = 92,840 bytes, SHA-256 2c56cd7d50e8b3115d283ea95c5a29f8485ff0ec16f36a4e961ac60add7c6c85; current repo file has the same byte count and SHA-256",
        "org/critical_paths/change_management/20260903T1409Z_nfra-cldgrph-b2-projection-worker_deploy_completion.md: L2 records corrective CodeBuild b72c8766-3ea5-4ce5-ab43-55bdb9599afa SUCCEEDED and the same latest image digest. This independent NFRA_CLDGRPH deployment post-dates TO-CE-T-12's 14:23Z preflight and explains the state transition."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_COMPEFFICACY PRD v0.5 @5bbdab5ec7 s.7 row T-12 and TO-CE-T-12 @6e5d443ad3: summary_corpus.py is baked into the globgrph derive image with PRE-fix bytes; DEPLOYED != COMMITTED; carry the gap to the G-rows and name owner 0.7.0_AE_CloudOps.",
    "world_is": "The premise was true at the order's cited earlier measurement but is false for the current served artifact. A post-cut shared-image rebuild for NFRA_CLDGRPH placed the current committed summary_corpus.py bytes into ECR latest. Deployed, build-input, and current repo SHA-256 values are now equal. Similarity semantics and the image were not changed by this cell.",
    "notes": "No image remedy is performed or requested here. The owner named by the historical gap remains 0.7.0_AE_CloudOps; the carrier correction belongs to the PRD/decomposition owners at the next compile. TO-CE-T-12 continues on its actual s.4 audit scope, reporting the measured equality and this row rather than repeating a stale DEPLOYED != COMMITTED claim."
  },
  {
    "id": "NFRA_COMPEFFICACY-S24",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~J",
    "surfaced_at": "2026-09-03T14:51:08Z",
    "one_line": "TO-CE-T-23 AC3 requires the portal submodule's git status be clean while this cell only reads portal/src. Before and after the comp-cache scan, `git -C portal status --porcelain` reports 14 untracked paths (including .frontend-dev/, .runtmp/, catch404_final.png, org/, portal/, public/, and src/ subtrees). This seat made no portal edit and must not delete or move user-owned paths, so it cannot truthfully attest a clean portal worktree under this order.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured 2026-09-03T14:51:08Z: `git -C portal status --porcelain` -> 14 rows, all `??` (untracked): .frontend-dev/org/, .frontend-dev/screenshots/, five .frontend-dev/testing paths, .runtmp/, catch404_final.png, org/, portal/, public/__mockcot/, src/org/, src/pages/AdvisorIntelligence/org/.",
        "TO-CE-T-23 BOUNDS: portal/src is READ, never edited; T23-AC3 requires zero changes under portal/ with a clean submodule status shown. This cell only ran comp-cache reads and fixture tests outside portal."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "2.0.0_SA_COO reworded T23-AC3 at 3318cfc9b7 to the zero-delta bar: before and after portal status are byte-identical, git diff --stat is empty, and portal HEAD is unchanged. The 14 pre-existing untracked paths are listed as evidence and were not removed or altered by this cell.",
    "spec_asserts": "T23-AC3 @3318cfc9b7: portal is READ, never edited; prove zero delta by byte-identical before/after status, empty diff stat, unchanged HEAD, and a listed pre-existing-untracked inventory.",
    "world_is": "The portal worktree retains the same 14 pre-existing untracked paths measured before the scan. The comp-cache audit made zero portal changes: its before/after status is byte-identical, diff stat empty, and HEAD unchanged.",
    "notes": "Disarmed by 2.0.0_SA_COO's issuer ruling. No portal path was edited, deleted, moved, staged, or otherwise changed by 0.8.0_AE_CloudComp~J; the pre-existing untracked inventory remains intact."
  },
  {
    "id": "NFRA_COMPEFFICACY-S25",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~M",
    "surfaced_at": "2026-09-03T14:54:33Z",
    "one_line": "comp-passcraft recon comp-pulse reports write_surface '(none matched by the write-pattern set)', while the actual .tools/comp-pulse wrapper invokes comp_log_auto.py after every engine run and appends a comp-tool-runs.jsonl telemetry record. The passcraft evidence pack therefore omits a real append-only write surface for this tool; no passcraft code or telemetry path was changed by T18.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2026-09-03T10:5x-04:00 at 0.8.0_AE_CloudComp~M: `comp-passcraft recon comp-pulse` printed write_surface=['(none matched by the write-pattern set)'] while identifying .tools/comp-pulse as the wrapper and org/modules/graph/comp_pulse.py as its backend.",
        ".tools/comp-pulse:7 invokes `python \"$WORKSPACE/org/modules/graph/comp_log_auto.py\" \"comp-pulse\" \"$*\" $_exit`; the same command's subsequent real wrapper invocation wrote a new comp-pulse row in org/mcp/comp-tool-runs.jsonl.",
        "The T18 code boundary is org/modules/graph/comp_pulse.py plus .tools/tests/test_comp_pulse_battery.py; the shim and comp-passcraft are READ-only under the task order."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_COMPEFFICACY TO-CE-T-18 requires the s.4.5 passcraft moves and a truthful hook-driven usage audit; the passcraft output is evidence, not a substitute for reading the wrapper body.",
    "world_is": "The comp-pulse wrapper has an append-only telemetry side effect that comp-passcraft's write-pattern report did not enumerate. The engine remains query-only with respect to the danger map after T18's change; the omitted write is the wrapper's telemetry append.",
    "notes": "No action is taken outside T18. A future comp-passcraft owner can decide whether wrapper subprocess write surfaces belong in its detector; the per-tool report names the discrepancy and uses the actual telemetry census rather than the passcraft claim."
  },
  {
    "id": "NFRA_COMPEFFICACY-S26",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~G",
    "surfaced_at": "2026-09-03T15:08:48Z",
    "one_line": "The required comp-read forwarder on this Windows seat returned rc=0 without the requested source content for drift_cli.py and drift-topology.yaml; the explicit .tools/comp-read rail was invoked and a marked direct read supplied the same inspection evidence. This is an integration-friction observation, not a production-tool defect.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_COMPEFFICACY.TO-CE-T-14 execution at 0.8.0_AE_CloudComp~G: the bare comp-read command was unavailable on the Windows PATH; explicit .tools/comp-read invocations for the engine and topology returned exit 0 with empty output.",
        "The T-14 report's integration-friction section records the fallback: direct rg/Get-Content inspection was marked with rail-checked comments; no seam engine or topology file was edited."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "No source or runtime behavior was hidden: the explicit rail and direct read exposed the required three modes, fan-out, called engines, and rc mapping. The friction is local command wiring and requires no NFRA_COMPEFFICACY code remedy.",
    "spec_asserts": "NFRA_COMPEFFICACY TO-CE-T-14 compiler_tools_mandate requires comp-read before write and truthful recording of any instrument limitation.",
    "world_is": "The repository-local .tools/comp-read exists, but its Windows invocation did not emit content; the production audit and proof remain valid and the seam engines stayed read-only.",
    "notes": "Filed by the owning seat as the required round-6 surprise row. No message to CVO and no additional scope or dependency was introduced."
  },
  {
    "id": "NFRA_COMPEFFICACY-S27",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~C",
    "surfaced_at": "2026-09-03T15:10:46Z",
    "one_line": "TO-CE-T-5's first required before-write audit action was exercised against the production engine. comp-read reports .tools/comp-schedule as a 527-line Python module with 23 sections; the default comp-schedule view reports 23 armed gates across the five declared carriers (C1 21->5, C2 6->6, C3 12->12, C4 20->0 SEMI-DECIDABLE, C5 337->0 NOT-DECIDABLE) and 138 prose entries as a reading list. The live census matches the cut preflight; no spec-vs-world divergence was found in this first action.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/comp-read .tools/comp-schedule --for 'the five carriers, how each decides or refuses to decide, what the rc means, every loop over a carrier population' -> rc 0; 527 lines, 23 sections via python-ast; self-report within budget.",
        "python .tools/comp-read .tools/to-pipeline-gate.py --for 'whether the preflight reads comp-schedule rc' -> rc 0; PREFLIGHT_TOOLS includes comp-schedule and the gate's check_preflight path was surfaced.",
        "python .tools/comp-schedule -> rc 0; GATES ARMED 23; NEEDS-READ 138; C1 21 -> 5, C2 6 -> 6, C3 12 -> 12, C4 20 -> 0, C5 337 -> 0, matching the 2026-09-03 14:23Z preflight values in TO-CE-T-5."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The first-action census is consistent with the task-order preflight and the engine's declared five-carrier schema. This is a measured starting-state record, not a defect or remediation request; subsequent T5 criteria still require the four planted answer-state cases, Rule T consumer census, battery, deliverable, and proof instance.",
    "spec_asserts": "TO-CE-T-5 AC1/AC2/AC4: the s.4 audit must quote the five-carrier default, preserve the NOT-DECIDABLE tool voice, and answer the rc question by consumer census.",
    "world_is": "At 2026-09-03T15:10:46Z the production engine's view-time compilation agrees with the cut preflight on gate count and every carrier denominator/result; no remediation is authorized or performed by this row.",
    "notes": "Filed by the assigned ~C seat as the first-action evidence row required by the tick-3 issuer ruling. The row is inert and does not alter carrier semantics."
  },
  {
    "id": "NFRA_COMPEFFICACY-S28",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~H",
    "surfaced_at": "2026-09-03T15:43:44Z",
    "one_line": "The Codex launcher environment gives concurrent round-6 seats one shared CLAUDE_CODE_SESSION_ID, while comp-to and comp_log_auto.py key task attribution only on that Claude variable. During TO-CE-T-17, other seats repeatedly overwrote the same supposedly race-free .to_id file: this seat set T17, later read T20, and its comp-estate rows were stamped T20. The production tool answers remain valid, but per-task telemetry attribution is not.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.8.0_AE_CloudComp~H environment at 2026-09-03T14:5xZ: CLAUDE_CODE_SESSION_ID=af7a2a30-0946-4127-83c9-871c7ac970cb while CODEX_SESSION_ID and CODEX_THREAD_ID were the distinct Codex value 01a06796-f277-7213-93bc-ef01e77d6724.",
        ".tools/comp-to:17-21 writes org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.to_id and describes it as race-free per-session; org/modules/graph/comp_log_auto.py:103-111 and :350 read and emit that same Claude-keyed id, with no Codex-session fallback.",
        "org/mcp/comp-tool-runs.jsonl recent rows sharing session_id af7a2a30-0946-4127-83c9-871c7ac970cb carried serials ~H, ~J, ~M, ~L and ~E under TO-CE-T-20. The corresponding session file contained T20 after ~H had set T17; ~H's 37 comp-estate rows in the 30-day census were consequently attributed to T20 until the next rebind."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": ".tools/comp-to:4-10 and comp_log_auto.py:89-96 assert that the session-keyed .to_id mechanism prevents cross-agent last-writer-wins attribution; TO-CE-T-17 requires usage evidence attributable to the exact assigned seat/order.",
    "world_is": "The shared-host Codex launch supplies a unique CODEX session/thread id but also an inherited CLAUDE_CODE_SESSION_ID common to concurrent child seats. The attribution helpers ignore the unique Codex id, so the collision class they claim to remove is live for Codex. Tool+serial usage counts remain measurable; to_id is not trustworthy for these concurrent rows.",
    "notes": "No launcher or telemetry helper is changed under T17's engine/test boundary. The T17 result excludes to_id from its usage count, names the attribution defect, and reports this row. A future runtime/telemetry owner can key Codex seats on CODEX_SESSION_ID or another launcher-owned unique id while retaining the Claude path. This row does not block the comp-estate production change or its battery."
  },
  {
    "id": "NFRA_COMPEFFICACY-S29",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~I",
    "surfaced_at": "2026-09-03T15:45:10Z",
    "one_line": "TO-CE-T-20 describes comp-heat as a library-only surface whose comp-similar consumer returns the heat state, but the live source exposes a CLI entrypoint and comp-similar invokes that CLI as a subprocess before returning an untyped dict. The ordered library-grain typed-state change cannot be made inside T20's allowed engine-only boundary without changing its read-only consumer.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_COMPEFFICACY.TO-CE-T-20 @6e5d443ad3: the cell calls .tools/comp-heat a 377-line engine used only as a library by comp-similar load_heat_live(), requires 0 CLI runs, and requires an absent or stale heat source to raise or return a typed state at the library grain; its bounds declare comp-similar READ, never edited.",
        ".tools/comp-heat at the dispatched source: main() creates argparse subparsers freshness, drift, score, federated, and compare; lines 374-377 execute sys.exit(main()) under __main__. It contains no load_heat_live() import surface.",
        "org/modules/graph/debtscan/comp_similar.py:275-300 defines load_heat_live(); its line 290 calls _run_json([REPO/.tools/comp-heat, freshness, --json, out_json]) and line 300 returns heat. The consumer imports no comp-heat library function and carries no typed absent/stale state.",
        "This seat's mandated pre-write reads: python .tools/comp-read .tools/comp-heat --for the library surface/return/CLI/loops -> rc 0 (377 lines, __main__ surfaced); python .tools/comp-read org/modules/graph/debtscan/comp_similar.py --for load_heat_live and return -> rc 0 (load_heat_live surfaced at 275-300)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CE-T-20 and PRD v0.5 row T-20 require a library-grain audit of comp-heat with 0 CLI runs, a return-carried typed absent/stale state, and no change to the comp-similar consumer.",
    "world_is": "The dispatched .tools/comp-heat is a CLI shim with an executable argparse entrypoint. Its named consumer uses it through a CLI subprocess and then returns an ordinary dict; the only place a return-carried typed state could be introduced is the consumer that the order forbids changing.",
    "notes": "No engine, consumer, or report wiring code is changed by this row. The T20 deliverable can truthfully record the measured CLI and consumer facts, but AC2's requested library-return mutation needs an issuer disposition that either changes the allowed boundary or replaces the library premise with the actual CLI grain."
  },
  {
    "id": "NFRA_COMPEFFICACY-S31",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T17:10:00Z",
    "one_line": "comp-blast's Rule T carrier bounds the TRAVERSAL only: the universe load that precedes it (org/modules/graph/cli.py:799 and :1053, load_kuzu_universe(refresh=True) -> the auto path) runs a FULL kuzu rebuild when the served graph is stale, outside the budget and before the traversal's clock starts. Measured at this seat: `.tools/comp-blast gold:A_00.accounts_dimension --exact --budget 60` issued 16:56:37Z took the rebuild mutex at 16:56:39Z, spawned kuzu_nessie_load.py (pid 30976) at 16:56:46Z, and had not returned when the harness's 300 s ceiling killed the shell at 17:01:37Z -- the call outlived its declared budget by more than 5x with no BUDGET REACHED line (KILLED-OUTSIDE, indistinguishable from a crash to the caller), and the chain (bash 39196 -> bash 50680 -> cli.py blast 44804 -> loader 30976) was still alive with the WAL growing at 17:06Z. The same shape CE-g-5 closed for comp-find's --corpus aws (a budgeted client never waits on or runs a rebuild; it serves the existing graph labeled stale) is open on comp-blast, and TO-CE-T-6's criterion T6-AC4 scoped Rule T to 'the traversal', which the face's PASS honestly met.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED at 3.0.0_SA_CVO 2026-09-03T16:56:37Z: .tools/comp-blast gold:A_00.accounts_dimension --exact --budget 60 inside a Bash call with a 300 s ceiling; the harness returned exit 143 'Command timed out after 5m 0s' with no comp-blast output at all -- KILLED-OUTSIDE (PRD s.4.4's named uncovered member), not BUDGET REACHED",
        "infra/aws/globgrph/ at 17:04:35Z and 17:06:27Z: kuzu_nessie_db.rebuild.lock created 16:56:39Z (2 s after the call), kuzu_nessie_db.rebuild.tmp 43,995,136 B at 17:02:38Z, .rebuild.tmp.wal 4,324,400 B at 17:04:32Z -> 8,964,023 B at 17:06:26Z (growing); no _refresh_status.json (the winner's path, not a serve-stale)",
        "Win32 process table at 17:06Z (Get-CimInstance, ParentProcessId resolved): bash 39196 '.tools/comp-blast ... --exact --budget 60' (created 16:56:37Z) -> bash 50680 -> python cli.py blast (44804) -> python kuzu_nessie_load.py --db ...kuzu_nessie_db.rebuild.tmp (30976, created 16:56:46Z); every parent ALIVE -- the loader is SUPERVISED, not orphaned: CE-g-5's process claim holds on this path; the rebuild was left to finish and swap (a running rebuild belongs to whoever started it)",
        "org/modules/graph/cli.py at HEAD (comp-read --enumerate): :799 and :1053 `load_kuzu_universe(refresh=not getattr(args, 'force', False))` -- refresh=True by default, the auto path (a stale graph -> incremental, a large delta -> FULL rebuild; REBUILD_TIMEOUT_S 1800 in _canonical.py); :847 the only remaining() check, inside the traversal; :1633-1635 the --budget carrier's help text 'Rule-T wall-clock ceiling for traversal'",
        "NFRA_CLDGRPH-S4 / CG-s-10 @a9aea6f3ce: the full-fallback duration of the projection MEASURED at 940.6-1006.3 s -- the ambush's size on this device; PRD s.4.4 'a tool never exceeds a ceiling it was not told ... every timeout= derives from remaining(); a call that would outlive the budget is DEFERRED'",
        "TO-CE-T-6 face at HEAD (complete @dad11b5207): T6-AC4 '(AC-4) Rule T's form on the TRAVERSAL: --help discloses the carrier, the budget and the cursor; a planted small --budget produces the expiry line ...' -- the criterion's own scope word; the instance VALID rc 0 at this seat (6 of 6, checker 7b649df39d); the CE-g-5 precedent: _canonical.py ensure_fresh(wait_for_peer=False) + kuzu_cli.py --mode inc for comp-find's budgeted client @173dd335f4"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.6 s.4.4 RULE T: 'a tool never exceeds a ceiling it was not told' and 'every timeout= derives from remaining(); a call that would outlive the budget is DEFERRED'; s.4.4.1's 'outer ceiling the tools cannot see 120,000 ms default'; the CE-g-5 outcome for the freshness layer under a budgeted client (AC-7): a budgeted caller is served the existing graph labeled stale, never a rebuild.",
    "world_is": "On comp-blast the budget is applied after the universe is loaded, and loading a stale universe on the auto path runs the full rebuild (measured ~1,000 s on this device) inside the budgeted call; a 60 s budget call ran past a 300 s harness ceiling and was killed outside with no line printed. The traversal half of Rule T is met (T6-AC4 PASS, honestly scoped); the call half is not.",
    "notes": "Surfaced by the seat that met it (the L9 exercise of S17's flag carry), same turn, one row, no message as carrier; the rebuild it started was NOT killed and is left to finish and swap the served graph. DISARM (the T-6 lane's, via 2.0.0_SA_COO): comp-blast's universe load under a budget takes the CE-g-5 contract -- serve the existing graph labeled stale with its age when a budget is set (load_kuzu_universe(refresh=False) or the inc/serve-stale path, never a full rebuild inside a budgeted call), the age on the answer's disclosure line; the full refresh stays comp-kuzu-full / MSTR startup. The remedy is a cell the decomposition already contains (CE-t-6, complete on a criterion that scoped Rule T to the traversal), so the L10 route, if graduated, is SPEC_ERROR -> L6 -- a remediated order under CE-t-6 with Rule T on the CALL, quoted from s.4.4. Harm while unattended: every budgeted comp-blast call on a stale graph -- every morning after the nightly derive, until someone runs comp-kuzu-full -- runs ~1,000 s, is killed by any Bash ceiling, prints nothing, and leaves the caller unable to tell the ambush from a crash; and each such call takes the mutex for the duration. S17's own closure is unaffected: the flag carry is exercised by a seat other than the builder on the T-6 face (COO, rc 0, 507/507)."
  },
  {
    "id": "NFRA_COMPEFFICACY-S30",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~N",
    "surfaced_at": "2026-09-03T17:08:00Z",
    "one_line": "After the RESEAT message stated that no T-21 work existed under ~P, the shared worktree already contained an uncommitted modification to org/modules/graph/comp_system.py and an untracked .tools/tests/test_comp_system_battery.py implementing T-21-shaped Rule T, answer-state, unreadable-source, and mutant controls. Their author cannot be established from the worktree, so this seat neither claims nor overwrites them; the foreign battery's direct run produced no output for five minutes before it was interrupted, while the engine's own --self-test later passed 45/45 in about 83 seconds.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2026-09-03T17:0xZ at 0.8.0_AE_CloudComp~N: git status --short -- .tools/tests/test_comp_system_battery.py org/modules/graph/comp_system.py -> ' M org/modules/graph/comp_system.py' and '?? .tools/tests/test_comp_system_battery.py'.",
        "The exact untracked battery was read as directed by TO-CE-T-21; its header names the T-21 battery and its arms exercise no-fabrication, four ratified states, Rule T expiry, --check rc 3, unreadable source, and red mutants.",
        "python .tools/tests/test_comp_system_battery.py was started at this seat and emitted no result for five minutes; interruption left only a seat-created temporary mutant, which was removed. python org/modules/graph/comp_system.py --self-test then completed rc 0 with 45/45 passed, including the first no-fabrication and four-state arms."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CE-T-21 RESEAT says nothing was built under ~P and directs this seat to read any pre-existing untracked battery, not assume authorship, name it in a row, and write its own battery beside it.",
    "world_is": "The stated reseat starting condition differs from the present shared worktree: T-21-shaped engine and battery changes are present but uncommitted and unproven as this seat's work. The engine self-test is green; the foreign battery's full direct result is not yet available.",
    "notes": "No foreign file was edited, staged, committed, moved, or deleted. This seat will place a separately named lane-owned battery beside the foreign file, preserve the existing worktree state, and report validation evidence only for artifacts it owns."
  },
  {
    "id": "NFRA_COMPEFFICACY-S32",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~G",
    "surfaced_at": "2026-09-03T17:55:00Z",
    "one_line": "ADJUDICATES NFRA_COMPEFFICACY-S31: DISMISSED_WITH_REASON -- T6-AC7 now bounds the whole comp-blast call; a budgeted stale graph is served immediately with age/reason disclosure and no rebuild/wait, while unbudgeted --budget 0/--force disclose their retained path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "0.8.0_AE_CloudComp~G",
    "adjudicates": ["NFRA_COMPEFFICACY-S31"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/modules/graph/comp_blast_universe.py::load_kuzu_universe now gates canonical refresh with refresh_allowed = not budgeted and appends BUDGETED CALL: SERVING EXISTING GRAPH STALE with served age and needs_refresh reason.",
        "org/modules/graph/cli.py::cmd_blast starts the shared Rule-T clock before universe load and passes it through _blast_budget_walk; --budget 60 against the stale pin returned rc 0 in 8.5 s with no kuzu_nessie_load.py child.",
        "python .tools/tests/test_comp_blast_battery.py -> 7/7 PASS, including the AC-7 stale-serve/no-child arm and the budgeted-refresh-ambush RED mutant; comp-trace blob remains 9bcf128cf6ff4b7e95f6ed2e6869526b9588fd2d."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The T6-AC7 implementation and battery exercise the ordered disarm: budgeted calls never enter the canonical refresh mutex and disclose the served stale age; the prior whole-call ambush is closed.",
    "spec_asserts": "TO-CE-T-6 T6-AC7: THE BUDGET BOUNDS THE WHOLE CALL, including universe load; a budgeted stale graph is served immediately and never rebuilt or awaited.",
    "world_is": "Before this act, cmd_blast loaded a stale canonical graph through ensure_fresh before starting traversal timing. After this act, the load is under the same call-level budget decision and stale serving is explicit.",
    "notes": "Lane-owned disarm carrier for S31; append-only correction, no foreign row amended. Commit with the T6-AC7 implementation and proof refresh in the same act; LOCAL, no push."
  },
  {
    "id": "NFRA_COMPEFFICACY-S33",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-03T18:09:00Z",
    "one_line": "L9, round 6 tranche 1 (COO 93853): ADJUDICATES S23, S24, S25, S26, S27, S28, S30 and S32 -- DISMISSED_WITH_REASON, each on a read this seat made itself. S23 the T-12 premise superseded by a rebuilt image (deployed == build input == repo, measured by the cell); S24 the portal clean-state bar re-worded by the issuer to zero-delta @3318cfc9b7 and met; S25 comp-passcraft's write-pattern report omits the wrapper's telemetry append (a finding against the detector, carried into the CE-pass-1 roll-up, owner the comp-passcraft owner); S26 the comp-read forwarder on a Codex Windows seat returned rc 0 with no content while the explicit .tools/comp-read rail worked (outside this project's chain; named to the runtime owner as a false-empty-read class); S27 a starting-state census, no defect; S28 fixed in place by 1.0.0_SA_CTO @2f6dca8204 (per-session files keyed on seat+session; the launcher mints a GUID per Codex child); S30 the abandoned ~P worktree edit adopted by the issuer's reseat ruling @2bb17f9eb5; S32 a worker-authored adjudicating row on the CVO's item S31, read for its content, dismissed as a carrier -- S31's own disposition follows this seat's exercise. S29 (the comp-heat consumer boundary) and S31 are NOT adjudicated here: S29 graduates or not at L10 with its route, S31 on the exercise.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_COMPEFFICACY-S23",
      "NFRA_COMPEFFICACY-S24",
      "NFRA_COMPEFFICACY-S25",
      "NFRA_COMPEFFICACY-S26",
      "NFRA_COMPEFFICACY-S27",
      "NFRA_COMPEFFICACY-S28",
      "NFRA_COMPEFFICACY-S30",
      "NFRA_COMPEFFICACY-S32"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S23 @HEAD (0.8.0_AE_CloudComp~F): ECR opal-globgrph-derive-runner:latest digest sha256:3a4e078d2c65..., pushed 2026-09-03T14:32:35Z, /app/org/modules/graph/debtscan/summary_corpus.py 92,840 B SHA-256 2c56cd7d50e8..., equal to the build-input ZIP member and the repo file -- the cell's own three-way read; TO-CE-T-12's instance VALID rc 0 at this seat (6 of 6, surprises 1 resolving to S23)",
        "S24: 2.0.0_SA_COO's issuer ruling @3318cfc9b7 (T23-AC3 re-worded to zero-delta); the worker's before/after `git -C portal status --porcelain` byte-identical, `git diff --stat` empty, portal HEAD unchanged; TO-CE-T-23 complete @895b54ef8d, instance VALID rc 0 at this seat (surprises 1 resolving to S24)",
        "S25: the comp-pulse deliverable s.4.6 'S25 is an inert observation for the comp-passcraft owner; it does not invalidate the engine controls'; the T-17 deliverable's passcraft moves_1_to_8[1] independently records 'wrapper appends telemetry' for comp-estate -- two tools, one detector gap; TO-CE-T-18 and TO-CE-T-17 instances VALID rc 0 at this seat, both citing S25",
        "S26: the row's own measurement (the forwarder returned rc 0 without content; the explicit rail and a marked direct read supplied the evidence); no CE-t cell owns the ~/bin forwarders or the shim provisioning (.tools/provision-path-shims.sh is the runtime's, CLAUDE.md s.Git) -- the outside-remedy exit, 1.0.0_SA_CTO 93320 limb (ii)",
        "S27: the row's own census (23 armed gates across five carriers, 138 prose entries) matches the cut preflight; a record, not a mismatch",
        "S28: 1.0.0_SA_CTO 93794 and commit 2f6dca8204 (16:39Z) -- comp-to/comp-which key per-session files on <sid>.<serial>, comp_log_auto reads that key first; start-codex-seat.ps1 mints a GUID per child; exercised by the CTO with two seats under one sid",
        "S30: 2.0.0_SA_COO's reseat ruling @2bb17f9eb5 (TO-CE-T-21 ~P -> ~N, the ~P worktree edit adopted); COO 93853 'S30 (~N, the abandoned ~P worktree edit -- adopted by ruling)'",
        "S32 @HEAD (0.8.0_AE_CloudComp~G): an investigation row carrying `adjudicates: [NFRA_COMPEFFICACY-S31]` and a disposition, written by the T-6 lane; the gate admitted it (the schema allows the field on any row); T-6's instance re-run at this seat with the AC7 addendum: VALID rc 0, 7 of 7 rows"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Per item: S23 -- the premise 'DEPLOYED != COMMITTED' was true at the cut and false at execution; the served, build-input and repo bytes are equal by SHA-256; the stale carrier (PRD s.7 T-12, decomp CE-t-12) is the L4 owner's to correct at the next compile, no order. S24 -- the issuer's zero-delta bar is met; the 14 untracked portal paths are pre-existing and user-owned, nobody's to delete under an audit order. S25 -- the detector's gap is real and belongs to comp-passcraft's owner; it rides the CE-pass-1 roll-up as a finding against the detector, not as a defect of the audited tool. S26 -- an instrument fault outside this project's chain (the PATH forwarder on a Codex Windows seat), named to the runtime owner; the audit's evidence came through the explicit rail and is valid. S27 -- a measured starting state, no spec-versus-world. S28 -- remedied in place by its owner and exercised; nothing routes. S30 -- the issuer ruled the adoption; the provenance question is answered by the ruling, not by this seat. S32 -- a carrier row; read, not a disposition of S31.",
    "spec_asserts": "The eight rows' own `spec_asserts` (the T-12, T-23, T-18, T-14, T-5, T-17, T-21 faces and the RESEAT message), and annex v2.3 s.4: a disposition is the CVO's field, set at L8/L9 by a row of the CVO's.",
    "world_is": "Each item is either superseded, remedied in place by its owner, ruled by its issuer, or a record with no remedy owed inside this project's chain; two are placed with owners outside it (S25 the detector's, S26 the runtime's). One form fact for the issuer: five of the nine round-6 worker rows set their own disposition and one (S32) carries an `adjudicates` list on the CVO's item -- harmless on inert observations, but the field is the CVO's L9 carrier.",
    "notes": "Documented at L9 ahead of the round-6 stamp because COO 93853 asks for L9 on tranche 1 now and Andrew's word at the COO terminal was pace; nothing here routes, so nothing waits for tranche 2. S29 stays UNDER_INVESTIGATION for the stamp (a routed row per the issuer's read: the consumer half under CE-t-12). S31 stays UNDER_INVESTIGATION until this seat's own exercise of T6-AC7 returns (running under a hard wrapper; the first attempt is S31's own subject). Named to 1.0.0_SA_CTO in the stamp message, not routed: S26's false-empty-read class on Codex seats; and a gate limb 'adjudicates only from the CVO' would close the S32 shape mechanically."
  },
  {
    "id": "NFRA_COMPEFFICACY-S34",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~2",
    "surfaced_at": "2026-09-04T03:37:46Z",
    "one_line": "TO-CE-G-2's step 1 ('MEASURE FIRST: one real default run of each tool on a real subject') could not run on comp-blast as spawned: this fresh worktree carries no copy of the gitignored canonical kuzu DB, so comp-blast's first run was TOOL-FAILED, not a real answer -- resolved by copying the DB + manifest (read-only, gitignored runtime artifacts) from the main workspace into this worktree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git check-ignore -v infra/aws/globgrph/kuzu_nessie_db infra/aws/globgrph/kuzu_nessie_db._build_manifest.json -> both matched by infra/aws/globgrph/.gitignore:3 and :10 -- runtime artifacts, never committed, never shipped into a worktree checkout.",
        "First run in this worktree (pre-copy): `.tools/comp-blast component:AdvisorsTab.tsx --budget 90` -> rc=1, stdout: 'TOOL-FAILED: canonical kuzu DB not found at C:\\tmp\\wk-CE-2\\infra\\aws\\globgrph\\kuzu_nessie_db. comp-blast's universe IS this graph; it does NOT fall back to a private scan.'",
        "Remedy: `cp -p` of kuzu_nessie_db (217,927,680 bytes) and kuzu_nessie_db._build_manifest.json from C:\\Users\\AndrewBerman\\Desktop\\ajb_workspace\\infra\\aws\\globgrph\\ into this worktree's infra/aws/globgrph/ (filesystem copy only -- no git operation, no edit to any tracked path). Re-run: rc=3 NOT-FOUND (a real answer against 27,223 real nodes), with the ordered VINTAGE line present.",
        "The same fresh-worktree gap also emptied comp-trace's local cache (.comp-graph/graph.json absent) -- that one self-healed via the engine's OWN pre-existing rebuild-on-absence path (_get_graph, org/modules/graph/cli.py, unedited by this order) in 66.9s, well inside the 120s bound; no action was needed there."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CE-G-2 deliverable step 1: 'one real default run of each tool on a real subject, output captured whole'; compiler_tools_mandate: 'AFTER COMMIT: the two real answers quoted'.",
    "world_is": "A spine-v3 worktree does not carry the gitignored canonical kuzu DB (217 MB, machine-local runtime state) that comp-blast's universe IS -- a fresh worktree spawned for a comp-blast/comp-trace task order cannot exercise a real comp-blast answer without first provisioning that DB from a source that already built it. G2-AC2/AC4's proof-of-spec evidence and G2-AC6's comp_blast_cli battery arm all depend on this copy remaining in place in THIS worktree for a re-run to reproduce the same PASS.",
    "notes": "No engine file touched (G2-AC5's three seam files are untouched and byte-identical); this is a worktree DATA-PROVISIONING fact, not a code change. Named for whoever owns spine-v3 worktree spawning for graph-touching task orders, and for 2.0.0_SA_COO's FWD-9 distinct-seat re-run: a re-run in a worktree without this copy will reproduce the SAME TOOL-FAILED comp-blast start this row measured, not a defect in the disclosure code this order shipped."
  },
  {
    "id": "NFRA_COMPEFFICACY-S35",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~2",
    "surfaced_at": "2026-09-04T03:37:46Z",
    "one_line": "G2-AC3's own invocation ('.tools/comp-trace AdvisorsTab.tsx --budget 90') failed with an argparse usage error (rc=1) BEFORE this order: comp-trace's subparser never accepted --budget (only comp-blast's did). Added --budget to comp-trace's argparse as an ACCEPTED-BUT-INERT flag (parsed, stored, never consulted) so the criterion's literal invocation reaches the shared disclosure code; comp-trace's local TraceGraph still has NO Rule-T bound on its own rebuild-on-drift path.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO (routes CE-t-6/NFRA_CLDGRPH CG-s-8, the Rule-T binding comp-trace's OWN local-graph rebuild still lacks)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Pre-edit `git show HEAD:org/modules/graph/cli.py` p_trace block (lines 1749-1761 of that blob): --exact, --direction, --depth, --json, --all are declared; no --budget. p_blast (same file) DOES declare --budget with the Rule-T help text.",
        "First run in this worktree, pre-edit: `.tools/comp-trace AdvisorsTab.tsx --budget 90` -> rc=1, stdout: 'usage: cli.py [-h] {build,trace,blast,diff,xref} ...' / 'cli.py: error: unrecognized arguments: --budget 90'.",
        "Post-edit: the same invocation reaches `_emit_trace_provenance` and prints the VINTAGE line at rc=3 (a real NOT-FOUND, not a usage error). p_trace's new --budget carries an explicit help string stating it is currently INERT and naming CG-s-8 as the engine that would have to bind it for real.",
        "Measured cold-cache cost this order's --budget on trace does NOT bound: a fresh worktree's first comp-trace call rebuilt the local TraceGraph in 66.9s (Building trace graph... Graph built: 2129 nodes, 2920 edges (66.9s)) with no ceiling consulting the caller's --budget value at all -- inside this order's 120s test bound, but not bounded BY the flag a caller supplies."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CE-G-2 criterion G2-AC3: <invocation>.tools/comp-trace AdvisorsTab.tsx --budget 90</invocation> naming the SAME shape as G2-AC2's comp-blast invocation, implying --budget already works uniformly on both tools' CLI surface.",
    "world_is": "comp-trace's argparse had no --budget flag at all; the literal criterion invocation was a usage error, not a disclosure exercise, until this order's own cli.py edit added acceptance. The acceptance is COSMETIC ONLY: a caller who now passes --budget to comp-trace expecting a Rule-T ceiling (the way it works on comp-blast) gets none -- a drifted/absent local cache can still take upwards of a minute to rebuild with no budget enforcement, which is the exact class of silent-ambush risk CE-t-6/T6-AC7 closed on comp-blast's side.",
    "notes": "Scoped strictly to cli.py's argparse surface (the DISCLOSURE lane this order owns); binding comp-trace's local rebuild to Rule-T for real is out of this disclose-only order's bounds (NO ENGINE CHANGE governs the kuzu seam; comp-trace's own rebuild path is a different engine again, unowned by any cell this order claims). Left ARMED rather than INERT because a future caller reading --budget's presence on comp-trace, without reading its help text, will reasonably assume it bounds the call the way it does on comp-blast -- it does not."
  },
  {
    "id": "NFRA_COMPEFFICACY-S36",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~2",
    "surfaced_at": "2026-09-04T03:52:41Z",
    "one_line": ".owned-paths.yaml carries NO spine-v3 worker (0.9.0_WK_*) entry in ANY lane's permitted_agents -- this TO's own explicitly-named surfaces (org/modules/graph/cli.py, lane ANY_EXEC_OR_AE; the new .tools/tests/test_g2_disclosure_battery.py, lane TOOL_BATTERIES) both BLOCKED this worker's safe-commit.sh call in block mode, contrary to the TO's own commit instructions. Routed around via the documented SINGULAR GIT_COMMIT_AUTHOR_OVERRIDE=<LANE> escape hatch (CLAUDE.md 14a), one commit per violated lane, both audited in org/git-author-override-audit.log.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO (issuer of spine-v3 worker task orders; owns .owned-paths.yaml grants per its own history, e.g. the 0.8.0_AE_CloudComp~D / NFRA_GRAPHUNI addition)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`bash .tools/safe-commit.sh --author \"0.9.0_WK_NFRA_COMPEFFICACY~2 <...>\" -F <msgfile> -- org/modules/graph/cli.py .tools/tests/test_g2_disclosure_battery.py` -> rc=1: 'ERROR: owned-paths lane violation(s) detected (block mode): VIOLATION: .tools/tests/test_g2_disclosure_battery.py -- lane=TOOL_BATTERIES ... agent=0.9.0_WK_NFRA_COMPEFFICACY~2 not in permitted_agents; VIOLATION: org/modules/graph/cli.py -- lane=ANY_EXEC_OR_AE ... agent=0.9.0_WK_NFRA_COMPEFFICACY~2 not in permitted_agents'.",
        "comp-find '0.9.0_WK' .owned-paths.yaml -> 0 hit(s) across 1 file(s) scanned -- a measured, whole-file zero: no spine-v3 worker serial pattern is enumerated anywhere in the lane file.",
        ".owned-paths.yaml TREE_COO note (task-orders/ lane): 'task-orders/ LEFT this lane 2026-09-03 (-> ANY, Andrew-direct @a4c9b25b4c: workers commit freely where their work is; the L6 gates are the control)' -- the estate's own stated direction for WORKER commits is already ANY-shaped elsewhere; the gap is that spine-v3 workers were never enumerated when TOOL_BATTERIES (2026-09-02) and the ANY_EXEC_OR_AE lane's later tilde-additions were cut, both predating this worker TYPE.",
        "Both files pass commit-gate.sh and G2-AC5/AC6/AC7 clean before the lane refusal fired -- the block is purely an authorship-enumeration gap, not a content defect."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CE-G-2's own commit mechanics: 'Commit ONLY on branch wk-CE-2 via: bash .tools/safe-commit.sh --author ... -F <msgfile> -- <paths>', naming org/modules/graph/cli.py and .tools/tests/test_g2_disclosure_battery.py as this worker's own surfaces to create and commit.",
    "world_is": "The literal safe-commit.sh invocation the TO specifies is refused in block mode for BOTH named surfaces, because .owned-paths.yaml has never been extended to recognize the spine-v3 worker serial grammar (0.9.0_WK_<PROJECT>~<n>) introduced by the v3 pipeline -- a class gap, not specific to this worker or this project.",
    "notes": "Every future spine-v3 worker task order that names an ANY_EXEC_OR_AE or TOOL_BATTERIES (or any other non-ANY-lane) path as its surface will reproduce this identical refusal until .owned-paths.yaml is extended (a wildcard or an explicit 0.9.0_WK_* grant per lane, mirroring the TREE_COO task-orders/ precedent). Left ARMED because the recurrence is certain, not merely possible, and no seat currently owns closing it. This worker used the SINGULAR override (one lane per commit) per CLAUDE.md 14a rather than escalating and stalling; the audit trail is org/git-author-override-audit.log, two OVERRIDE lines, one per lane, timestamped this session."
  }
]
```

-- S1: `3.0.0_SA_CVO` (L8 assembly). S2, S5, S7: `0.8.0_AE_CloudComp` (direct append, tree-channel lane ANY, CLAUDE.md s.2 2026-09-03 correction). S3, S4, S6: `3.0.0_SA_CVO` (L9 adjudication, direct append per the corrected law).

## S39 -- a kuzu rebuild winner died at 01:36Z and its mkdir-mutex and WAL are still on disk five hours later (the CVO's row, lane ANY; found while exercising S31's fix)

```json
[
  {
    "id": "NFRA_COMPEFFICACY-S39",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:55Z",
    "one_line": "infra/aws/globgrph/kuzu_nessie_db.rebuild.lock is an EMPTY DIRECTORY created 2026-09-04T01:35:59Z, beside kuzu_nessie_db.rebuild.tmp (4,096 B, 01:36:12Z) and kuzu_nessie_db.rebuild.tmp.wal (6,574,411 B, last written 01:36:38Z); no python process running kuzu_nessie_load, kuzu_incremental or cli.py blast/trace/build exists at 06:5xZ (Win32 census). A rebuild winner took the mkdir-mutex, wrote for 39 seconds and died; _canonical.py's own comment (:659-660) names this case: 'a winner hard-killed between mkdir(lock) and the finally-rmdir leaves .rebuild.lock forever, so EVERY default query would pay the full wait then serve stale'. The budgeted path is unaffected (a --budget 60 comp-blast served the BEHIND graph in 7 s at 06:43Z); whether an UNBUDGETED default query steals the 5-hour-old lock (the token steal at :204-217) or waits REBUILD_TIMEOUT_S = 1800 s is UNEXERCISED here.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp (the kuzu engine's owner) via NFRA_CLDGRPH cell CG-s-8, the local rebuild path's retirement",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls -la infra/aws/globgrph/kuzu_nessie_db.rebuild.lock/ at 06:5xZ: a directory, 0 entries, created 2026-09-04T01:35:59Z; siblings kuzu_nessie_db.rebuild.tmp 4,096 B (01:36:12Z) and kuzu_nessie_db.rebuild.tmp.wal 6,574,411 B (01:36:38Z); the served kuzu_nessie_db 217,927,680 B and its manifest built_at 2026-09-04T01:27:09Z (so the dead rebuild started 8 minutes after a successful one).",
        "Get-CimInstance Win32_Process at 06:5xZ filtered on kuzu_nessie_load|kuzu_incremental|cli.py (blast|trace|build): 0 processes -- the mutex holder is dead.",
        "infra/aws/globgrph/_canonical.py at HEAD (comp-read --enumerate): :650 lock = db_path + '.rebuild.lock'; :655 os.mkdir(lock) atomic acquire; :659-660 the hard-killed-winner comment quoted above; :66 REBUILD_TIMEOUT_S = 1800 (GLOBGRPH_REBUILD_TIMEOUT_S); :204-217 a steal path (rmdir + re-mkdir writes a NEW token; the stolen-from winner reads a mismatch and aborts).",
        "Budgeted control at 06:43:18Z-06:43:25Z: .tools/comp-blast gold:A_00.accounts_dimension --exact --budget 60 -> rc 3 in 7 s with 'WARN: BEHIND Nessie HEAD -- pin 1686878912724079672 != HEAD 92487625797322719 (writer=incremental_updater, committed_at=2026-09-04T05:53:37Z)', age 5.3h -- the budgeted client serves stale and never touches the mutex (T6-AC7 @5bba38864c). The unbudgeted default path against this lock was NOT exercised at this seat (a 1800 s wait is not a control this seat runs inside a slug)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "_canonical.py's rebuild contract: a stale or BEHIND canonical DB is rebuilt under a mkdir-mutex, a dead winner's lock is stolen by token after the timeout, and a budgeted caller (PRD s.4.4 / CE-g-5 / T6-AC7) is served the existing graph labeled stale and never waits on a rebuild.",
    "world_is": "A winner died at 01:36:38Z leaving the mutex directory and a 6.5 MB WAL; five hours later both persist. The budgeted contract holds (measured). Whether the next unbudgeted default query steals the lock promptly, waits 1800 s, or serves stale after the wait is unmeasured; the engine's own comment says the pre-steal behaviour was 'the full wait then serve stale'. This is the local rebuild path NFRA_CLDGRPH CG-s-8 exists to retire; filed here because it was found at this project's L9 exercise and named in the round-6 slug for the CTO to route.",
    "notes": "Adjudicated in the same commit by ../adjudications/ADJUDICATION_v1.md C-S6 (DISMISSED_WITH_REASON, owner named outside this project's chain). Not repaired at this seat: removing another process's mutex is the engine owner's act, and the WAL may be evidence of why the winner died."
  }
]
```

## W1-S1 -- the accept's two-value `subject_resolved` cannot cover the regression set it also names: the four F-10 phrasings carry NO gold id, so `true` for them would record a check that never ran

```json
[
  {
    "id": "NFRA_COMPEFFICACY-W1-S1",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~1",
    "surfaced_at": "2026-09-09T23:56Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "TO-CE-P-4 accept clause (e) maps the spilled rank file's `subject_resolved` to (b)=false, (c)=true, (d)=false, where (c) IS the four F-10 / C-S46 regression phrasings. Measured at this seat: GOLD_ID.search() matches 0 of 4 of those phrasings, so none of them carries a subject at all and none can be `true` without the field asserting that an authority was consulted when nothing was looked up. Resolved WITHOUT widening the order: the field is a THREE-value enum (`true` / `false` / `not-applicable`), `authority_consulted` is populated exactly when the check RAN and empty when it did not, and an extra POSITIVE CONTROL question carrying a REAL id (`what does INF_D_02 write to s3`) supplies clause (e)'s `true` reading. Both readings are printed by the battery so the grader sees the substitution rather than a repaired-looking summary.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-P-4.comp-which-subject-existence.md@0e9ef40b37, criterion P4-AC1 clause (e): 'the spilled rank file for (b), (c) and (d) carries `subject_resolved` (`false`, `true`, `false`)'; clause (c) defines (c) as 'the four regression phrasings'.",
        "The four phrasings, verbatim from org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~6/f10_lib.py:23-28@0e9ef40b37. This seat, 2026-09-09 23:0xZ: `.tools/comp-which`'s own GOLD_ID (:1279) searched against each -> 0 of 4 match. Printed by the battery as arm (f).",
        "TAXONOMY LAW postulate (i) MECE over a DECLARED domain and (iv) STATE COHERENCE: a two-value enum over a domain whose largest member is 'no subject present' has an uncovered member, and the standing rule that a verdict vocabulary with no NOT-EVALUATED value encodes non-evaluation as a verdict.",
        "The implemented carrier: .tools/comp-which _SUBJECT_UNKNOWN = 'not-applicable' and _spill_full_ranking's three new header keys (subject / subject_resolved / authority_consulted), this worker's branch wk-nfra_compefficacy-7-1."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "P4-AC1 clause (e): the spilled rank file for (b), (c), (d) carries `subject_resolved` reading false, true, false -- a two-value field, with (c) bound to the four F-10 regression phrasings.",
    "world_is": "0 of 4 regression phrasings carry a gold id, so (c) has no subject to resolve and cannot honestly read `true`. The field shipped with three values and clause (e)'s `true` reading is supplied by an added real-subject positive control; the regression phrasings read `not-applicable` with an empty `authority_consulted`.",
    "notes": "For the CVO at L9: the substitution is visible in the battery's (e) table, which prints all four cases side by side. No registry was edited and no ranking changed. If the CVO reads clause (e) as requiring the four phrasings themselves to read `true`, that reading is not implementable without the field making a false claim, and this row is where that disagreement lands."
  }
]
```

## W1-S2 -- the `~/bin/comp-which` forwarder is HARD-BAKED to the main tree, so a bare `comp-which` run from ANY linked worker worktree measures the UNPATCHED tool

```json
[
  {
    "id": "NFRA_COMPEFFICACY-W1-S2",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~1",
    "surfaced_at": "2026-09-09T23:56Z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp (owner of .tools/provision-path-shims.sh and the comp-tool forwarders); mitigation at the cut is 2.0.0_SA_COO's, which already carries the explicit-path instruction in this worker's launch face",
    "one_line": "/c/Users/AndrewBerman/bin/comp-which is a generated bootstrap shim whose target is the LITERAL string /c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/comp-which -- the MAIN tree -- with a both-flavor fallback that only swaps /c for /cygdrive and never resolves relative to the caller's worktree. A spine-v3 worker patching any comp-tool in a linked worktree and verifying it with the bare PATH name therefore exercises the file it did NOT change, and the run succeeds, prints a plausible route and returns rc 0. This is the classic false-green: the negative result and the wrong-object result are byte-identical. This worker used `python .tools/comp-which ...` from the worktree root throughout and its battery resolves the CLI from the test file's own location, printing the absolute path it ran.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cat /c/Users/AndrewBerman/bin/comp-which, this seat 2026-09-09 22:5xZ: `_t=\"/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/comp-which\"` then a case that only maps /c/* <-> /cygdrive/c/* before `exec \"$_t\" \"$@\"`. No worktree resolution of any kind.",
        "`command -v comp-which` from /c/tmp/wk-compeff-7-1 -> /c/Users/AndrewBerman/bin/comp-which (not the worktree copy).",
        "The same shim header names .tools/provision-path-shims.sh as its generator and records that all 186 forwarders died at once at site Z when the baked prefix went away -- the same single-point-of-baking that makes this worktree-blind.",
        "P4-AC1 as cut requires 'each arm invoking the ESTATE'S OWN CLI (`comp-which \"<question>\"`, never an inner function)'; org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-P-4.comp-which-subject-existence.md@0e9ef40b37."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The accept names `comp-which \"<question>\"` as the estate's own CLI and the instrument every arm must use; CLAUDE.md 14b mandates one linked worktree per worker slot.",
    "world_is": "Inside a linked worktree those two are in conflict: the PATH name resolves to the main tree's copy of the tool, so the ordered instrument reads a different file from the one the order tells the worker to change. Bare-name verification of a comp-tool edit is unsound from every worktree, and it fails GREEN.",
    "notes": "ARMED because the recurrence is structural, not incidental: every future worker cell that edits a .tools/comp-* binary reproduces it, and the failure mode is a pass. Candidate disarms, none taken here (out of grant): make the shim resolve its target from `git rev-parse --show-toplevel` of the caller's cwd with the baked path as fallback; or have the shim print its resolved target to stderr so the wrong-object case is visible. Not repaired at this seat -- ~/bin and .tools/provision-path-shims.sh are outside this order's <paths>."
  }
]
```

## W1-S3 -- P4-AC1 arm (g)'s literal invocation cannot measure this change, cannot be run inside the grant, and does not terminate: `--binary-ref` defaults to HEAD, the default `--out` clobbers a committed baseline, and the bare run is rc 124 at 580 s ON THE UNPATCHED TOOL

```json
[
  {
    "id": "NFRA_COMPEFFICACY-W1-S3",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~1",
    "surfaced_at": "2026-09-09T23:56Z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp (the harness's authoring lane, whose deliverables dir holds its baseline artifact); the criterion-text half is 2.0.0_SA_COO's at the next cut",
    "one_line": "Arm (g) as cut is `python .tools/comp-which-routing-test.py` with no flags. Three defects, all PRE-EXISTING and all read in the harness's own source at 0e9ef40b37. (1) GRAIN: `--binary-ref` defaults to 'HEAD' (:1134) and :1177-1181 does `ref = None if args.binary_ref.upper() == 'WORKING' else args.binary_ref; vintage, blob = extract_binary(ref, tmp.name)` -- the bare form extracts the COMMITTED blob and scores THAT, so it is structurally incapable of seeing an uncommitted change and would have certified this fix by running the bytes the fix replaces. (2) GRANT: `out_path = args.out or BASELINE` (:1653) writes org/tier2_senior/0.8.0_AE_CloudComp/deliverables/comp-which-routing-baseline.json, outside this worker's <paths>, and the flag's own help says a regression run passes --out because 'A LATER VINTAGE MUST NOT CLOBBER A COMMITTED BASELINE' -- so the ordered invocation instructs an act the order's own bounds forbid. (3) TERMINATION: the bare form does not finish under a 580 s bound on the UNPATCHED tool -- measured rc 124, 23:42:21Z to 23:52:01Z, 153 lines of output, with .tools/comp-which restored to its HEAD bytes for the run and sha256-verified back afterwards. The arm was therefore run as `--binary-ref WORKING --out <this worker's deliverables>/cep4_routing_test_report.json`: the SAME harness, parameterised so it measures the changed bytes and writes inside the grant, with its SUBJECT line ('.tools/comp-which @ WORKING-TREE, blob 810fad08478a27fcac5a5f8d54ee13ab6a79e0ce') printed as the proof of which vintage was scored, and the bare form's rc recorded beside it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/comp-which-routing-test.py@0e9ef40b37 :1134 `ap.add_argument('--binary-ref', default='HEAD', help=\"git ref to measure (default HEAD). 'WORKING' = the dirty tree.\")`; :1177 `ref = None if args.binary_ref.upper() == 'WORKING' else args.binary_ref`; :1181 `vintage, blob = extract_binary(ref, tmp.name)`; :1653 `out_path = args.out or BASELINE`; :190-192 `_DELIV = .../0.8.0_AE_CloudComp/deliverables`, `BASELINE = _DELIV/comp-which-routing-baseline.json`.",
        "This seat, HEAD-bytes control run: `cp .scratch/comp-which.HEAD .tools/comp-which` (from `git show HEAD:.tools/comp-which`), `timeout 580 python .tools/comp-which-routing-test.py` -> rc 124, start 23:42:21Z end 23:52:01Z, 153 lines captured at .scratch/rt_before.txt. Restored with `cp .scratch/comp-which.PATCHED .tools/comp-which`; sha256 of both read 57690d9cae59f61190c89014e2bae5183a5723f6bd6558a6258db27ecc539ed4 after restore.",
        "This seat, patched-bytes bare run: `timeout 580 python .tools/comp-which-routing-test.py` -> rc 124, 290 lines (.scratch/rt_after.txt). Both bare runs timed out; neither reached the `out_path` write, which is why no committed baseline was in fact clobbered -- `git status --porcelain` at 23:5xZ shows only `.tools/comp-which`, `.scratch/` and this worker's deliverables folder.",
        "The parameterised run's own header, 23:54:57Z: 'SUBJECT : .tools/comp-which @ WORKING-TREE / blob 810fad08478a27fcac5a5f8d54ee13ab6a79e0ce'. The bare form's header names a git ref instead.",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-P-4.comp-which-subject-existence.md@0e9ef40b37, P4-AC1 clause (g) and the BOUNDS clause 'A path you need that it does not name is a BLOCKING row, never an override'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "P4-AC1 clause (g): '`python .tools/comp-which-routing-test.py` passes after the change (its own token/rc printed)'.",
    "world_is": "The bare invocation measures the COMMITTED blob, not the change; its default output path is outside this worker's write grant and its own help forbids that write for a regression run; and it does not terminate under a 580 s bound on the tool as it stood BEFORE the change. Arm (g) was executed as the same harness with `--binary-ref WORKING --out <in-grant path>`, with the bare form's rc recorded verbatim beside it.",
    "notes": "The substitution is a GRAIN correction, not a relaxation -- the parameterised form is strictly harder to pass, because it is the only form that can fail on this change at all. Whether the substitution is accepted is the CVO's at L9 and it is the reason arm (g) is called out separately in the result document. ARMED because any future criterion naming the bare invocation reproduces all three defects, and defect (1) fails GREEN: a bare run that passes certifies HEAD while reading as a certification of the worker's change."
  }
]
```

## W1-S4 -- the AMENDED arm (g) carries `timeout 600`, and the harness it names measured 680 s and 826 s on two consecutive WORKING runs: the literal amended command returns rc 124

```json
[
  {
    "id": "NFRA_COMPEFFICACY-W1-S4",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~1",
    "surfaced_at": "2026-09-10T00:31Z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.8.0_AE_CloudComp (the harness's runtime is the harness lane's, carried with W1-S3's three defects); the criterion-bound half is 2.0.0_SA_COO's at the next cut",
    "one_line": "The face amended @2fbb844173 re-cut P4-AC1 clause (g) to `timeout 600 python .tools/comp-which-routing-test.py --binary-ref WORKING --out <in-grant>` -- the GRAIN and GRANT halves of row W1-S3 correctly fixed, and the TERMINATION half (W1-S3 defect 3) carried forward into the new bound. This seat's two consecutive WORKING runs of that exact harness took 680 s (2026-09-09T23:54:57Z -> 2026-09-10T00:06:17Z) and 826 s (00:07:30Z -> 00:21:16Z), both rc 0 with 'VERDICT: PASS' and the WORKING-TREE header naming blob 810fad08478a27fcac5a5f8d54ee13ab6a79e0ce. Both exceed 600 s, so the literal amended command cannot return anything but rc 124 on this box. Run at its literal bound to measure rather than infer it, and recorded in cep4_amended_bound_probe.json and printed by the battery BESIDE the arm's verdict, never as it -- the same treatment the issuer ruled for the bare form. Arm (g) is scored on the un-truncated recorded run under a grain control (the blob the harness says it measured must equal `git hash-object .tools/comp-which` at battery time), because P4-AC1's OWN invocation is also `timeout 600` and a harness that needs 826 s cannot run inside it either way.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-P-4.comp-which-subject-existence.md@2fbb844173, P4-AC1 clause (g) as amended: '`timeout 600 python .tools/comp-which-routing-test.py --binary-ref WORKING --out org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_routing_test_report.json` passes after the change'.",
        "Run 1, this seat: 2026-09-09T23:54:57Z -> 2026-09-10T00:06:17Z = 680 s, rc 0, 'VERDICT: PASS -- controls held, zero pollution, and comp-which ABSTAINED on 100% of generated gibberish', header 'SUBJECT : .tools/comp-which @ WORKING-TREE / blob 810fad08478a27fcac5a5f8d54ee13ab6a79e0ce'.",
        "Run 2, this seat, via the committed runner cep4_run_routing_test.py: started 2026-09-10T00:07:30Z, ended 00:21:16Z = 826 s, rc 0, same verdict and same blob; recorded at org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_routing_test.rc.json.",
        "The literal amended command at its literal bound, this seat, started 2026-09-10T00:25:56Z: recorded rc and window in cep4_amended_bound_probe.json and printed by the battery's arm (g).",
        "W1-S3's defect 3 at 0e9ef40b37 (the bare form, rc 124 at a 580 s bound on the UNPATCHED HEAD bytes, 23:42:21Z -> 23:52:01Z) -- the same non-termination, which the amendment addressed on its other two limbs."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "P4-AC1 clause (g) as amended @2fbb844173: the parameterised harness invocation, prefixed `timeout 600`, passes after the change.",
    "world_is": "The harness passes after the change (rc 0, twice, on the correct blob) but needs 680-826 s to do it, so the 600 s prefix truncates it to rc 124. The bound is below the instrument's runtime; the instrument's verdict is not in dispute.",
    "notes": "NOT a defect of the change and not a request to relax the arm: the harness passes, and the arm is scored on a run that was allowed to finish, under a blob-equality grain control so a stale record cannot pass. What is ARMED is the bound travelling to the next cut that names this harness -- and a `timeout 600` that always returns 124 reads as a failing subject rather than an exhausted clock. The durable remedy is the harness lane's runtime, or a bound stated from a measured distribution; neither is this worker's."
  }
]
```

## S40 -- the semantic layer is OFF in every fresh linked worktree (tokenizer.json rendered CRLF, the FAIL-CLOSED hash gate refuses it, comp-which ranks lexically with one ALARM line); the round's BEFORE baseline was captured there and does not transfer -- the battery reads NOT ENFORCED at the main tree while old and new blobs rank identically (0 diff lines, 5 of 5)

```json
[
  {
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-10T01:25Z",
    "class": "OBSERVATION",
    "id": "NFRA_COMPEFFICACY-S40",
    "hazard_standing": "ARMED",
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "0.8.0_AE_CloudComp (owner of org/modules/graph/potion/ -- the hash-pinned model asset and its loader -- and of the comp-tool rail; the criterion-side half, a baseline that names the relevance layer it was captured under, is 2.0.0_SA_COO's at the next cut that compares ranked lists)",
    "one_line": "THE SEMANTIC LAYER IS OFF IN EVERY FRESH LINKED WORKTREE ON THIS BOX, AND A RANKED-LIST BASELINE CAPTURED THERE DOES NOT TRANSFER. Measured at this seat, 01:1xZ, on the round-7 drain: P4-AC1's battery re-run at the MAIN tree on HEAD's own bytes (.tools/comp-which blob 810fad08478a27fcac5a5f8d54ee13ab6a79e0ce, git hash-object = HEAD) returned rc 1, `NOT ENFORCED -- 3 arm(s) failed`, 24 of 27 arms PASS: the three failures are exactly the BYTE-EQUAL arms -- (c) the four regression phrasings, (f), (e:real-byte-equal) -- and the diffs are not noise: for phrasing 1 the AFTER list inserts comp-pii at rank 8 (score 0.46), moves a 0.37 to 0.43 and re-orders the whole fuzzy band below the seven curated rows, 78 rows both sides. THE FIX DID NOT DO THIS. Discriminator, same environment, same minute: the UNPATCHED blob (git show 0e9ef40b37:.tools/comp-which, blob 8c5aac72164c73a46f2574efebbe41813cae998d, run from <WS>/.scratch/ with PYTHONPATH=.tools so WS resolves to the main tree) against the PATCHED blob, cwd the main tree, on the four phrasings AND the real-subject question -> 0 diff lines on the ranked list and 0 on the terminal block, 5 of 5, rcs equal (0/0/1/0/0), 78 rows each. The ranking moved between the worker's BEFORE capture and the main tree because the RELEVANCE LAYER differs: the worker's BEFORE terminal captures carry, 7 of 7, `ALARM: POTION semantic embedder unavailable -> falling back to lexical relevance (ValueError: POTION hash-mismatch on tokenizer.json: manifest=e67e803f6...0f70bb50 vendored=0a1168df8...dfe829b (FAIL-CLOSED))`, and that ALARM line is the ONLY terminal difference the battery found at the main tree. THE MECHANISM, by hash: org/modules/graph/potion/model/tokenizer.json is tracked i/lf with NO eol attribute (git ls-files --eol: `i/lf w/lf attr/`; .gitattributes has no potion/json rule) under core.autocrlf=true, so a FRESH checkout -- every `git worktree add` a worker slot gets -- renders it CRLF; sha256 of the main tree's LF bytes = e67e803f6... = the MANIFEST; sha256 of the same bytes with every LF made CRLF = 0a1168df8209a591defdc781567f11f8ea5b400c60b994350f8892e7bdfe829b = EXACTLY the worker's `vendored=`. potion_embed.py:57-63 pins by hash and raises FAIL-CLOSED; load_embedder :81-95 catches it and returns None with the ALARM; comp-which then ranks the fuzzy band lexically. model.safetensors is i/-text (binary) and unaffected. CONSEQUENCES: (i) the worker measured BEFORE and AFTER, the mutant, the determinism control and the arm-(g) routing harness (`VERDICT: PASS ... ABSTAINED on 100% of generated gibberish`) on the LEXICAL ranker, a different ranker from the one every seat runs at the main tree -- the byte-equality claim is TRUE where measured and this seat has now measured it TRUE at the main tree by the old-vs-new discriminator, but the harness's verdict speaks for the fallback only; (ii) the committed battery reads red on any re-run at the main tree for a reason unrelated to the change -- a false RED, the mirror of the false GREEN in W1-S2; (iii) every future worker cell that measures comp-which ranking, tunes the semantic layer, or scores the router in a linked worktree measures the fallback, with one ALARM line on stderr as the only tell. NOT a defect of the fix and NOT of the worker: the worker printed the ALARM in its captures and compared like with like. REMEDY (the owner's): one `.gitattributes` line making the vendored model files byte-stable across checkouts (`org/modules/graph/potion/model/* -text`, or `binary`), or a manifest hash over LF-normalised bytes; and a ranked-list baseline that RECORDS the relevance layer it was captured under (`semantic` / `lexical-fallback`) so a comparison across environments refuses instead of failing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This seat, 2026-09-10T01:10:50Z -> 01:10:56Z: `timeout 600 python org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/test_cep4_subject_existence.py` at the main tree -> rc 1; `arms failed: c, f, e:real-byte-equal`; `NOT ENFORCED -- 3 arm(s) failed`; 24 [PASS] / 3 [FAIL]; `CLI UNDER TEST: C:\\Users\\AndrewBerman\\Desktop\\ajb_workspace\\.tools\\comp-which`; `blob MEASURED 810fad08... / blob of .tools/comp-which NOW 810fad08...`, g:grain PASS. Transcript: C:/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/1a859fc2-a8b0-4c16-a026-c1536099473c/scratchpad/cep4_battery_cvo.txt (this seat's transcript; not a repo artifact).",
        "The battery's own diff for phrasing 1: `@@ -43,0 +44,6 @@ + tool: 'comp-pii' score: 0.46 ... rank: 9`, `@@ -45 +51 @@ -score: 0.37 +score: 0.43`, `@@ -49 +55,217 @@` (the fuzzy band re-ordered); terminal diff `@@ -14 +13,0 @@ -ALARM: POTION semantic embedder unavailable -> falling back to lexical relevance (ValueError: POTION hash-mismatch on tokenizer.json: manifest=e67e803f624fb4d67dea1c730d06e1067e1b14d830e2c2202569e3ef...` -- the only terminal line that differs.",
        "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_before.json @e4c2d4a3e7: 7 of 7 captured questions carry the ALARM in `terminal`, verbatim `manifest=e67e803f624fb4d67dea1c730d06e1067e1b14d830e2c2202569e3ef0f70bb50 vendored=0a1168df8209a591defdc781567f11f8ea5b400c60b994350f8892e7bdfe829b (FAIL-CLOSED)`.",
        "This seat, 01:2xZ: `git ls-files --eol -- org/modules/graph/potion/model/` -> `i/-text w/-text attr/ model.safetensors`, `i/lf w/lf attr/ tokenizer.json`; `git check-attr -a` -> none; `.gitattributes` carries no potion or *.json rule (only `*.tf.json text eol=lf`); `git config core.autocrlf` -> true; tokenizer.json 683,666 B, 29,677 LF, no trailing newline; sha256 as-is e67e803f624fb4d67dea1c730d06e1067e1b14d830e2c2202569e3ef0f70bb50 (= the index blob); sha256 with b'\\n'->b'\\r\\n' = 0a1168df8209a591defdc781567f11f8ea5b400c60b994350f8892e7bdfe829b (= the worker's vendored hash).",
        "org/modules/graph/potion/potion_embed.py@HEAD :51-66 PotionEmbedder.__init__ (PIN-BY-HASH, `raise ValueError('POTION hash-mismatch on %s: manifest=%s vendored=%s (FAIL-CLOSED)')`), :81-95 load_embedder (`return None` on ANY failure, `sys.stderr.write('ALARM: POTION semantic embedder unavailable -> falling back to lexical relevance ...')`); org/modules/graph/comp_potion_relevance.py:138-144 build_provider -> load_embedder(model_dir).",
        "The discriminator, this seat 01:1xZ: `git show 0e9ef40b37:.tools/comp-which` -> blob 8c5aac72164c73a46f2574efebbe41813cae998d (= `git rev-parse 0e9ef40b37:.tools/comp-which`), copied to <WS>/.scratch/cvo_cw_old_0e9ef40b37.py (WS = dirname(dirname(__file__)), .tools/comp-which:33), PYTHONPATH=<WS>/.tools; for each of the four PHRASINGS and REAL_Q from cep4_lib.py: OLD then NEW via cep4_lib.comp_which's spill discovery, ranked_rows() and terminal_routes() diffed -> `ranked-list diff lines: 0 | terminal diff lines: 0` x5, ALARM absent on both, rc old/new 0/0, 0/0, 1/1, 0/0, 0/0, rows 78/78 x5. The copy removed afterwards (0 files left). A first attempt from the scratchpad path failed at `import _compbudget` (WS resolved to the temp dir) and was discarded as a wrong-object run.",
        "Rule 22 GRAIN: the compared object is 'the ranked list', and a ranked list is a function of (tool bytes, population, relevance layer); the baseline pinned the first two and left the third to the environment. CLAUDE.md memory: a gitignored/absent asset in a fresh worktree and a CRLF-rendered checkout on this autocrlf box are two known shapes; this is the second wearing the first's clothes (the asset is present, its BYTES are not)."
      ]
    },
    "spec_asserts": "P4-AC1 clause (c): 'the four regression phrasings route with ranked lists BYTE-EQUAL to the captured BEFORE lists'; clause (e) 'the REAL subject's ranked list is BYTE-EQUAL to BEFORE'; and the estate's standing expectation that a committed battery re-runs green at HEAD from any seat. The POTION loader's own contract: the vendored model is pinned by hash and FAIL-CLOSED.",
    "world_is": "The BEFORE baseline is bound to the LEXICAL fallback the fresh worktree ran (the hash gate refused a CRLF-rendered tokenizer.json); at the main tree the semantic layer is on, the fuzzy band ranks differently, and the battery reads NOT ENFORCED on 3 of 27 arms although old and new blobs rank identically there (0 diff lines, 5 of 5 questions). Every fresh linked worktree on this box runs comp-which's fallback ranker.",
    "notes": "ARMED because the recurrence is structural (every worker worktree) and the tell is one stderr line. Graduated in the same commit (C-S8) with the other three CloudComp items of this round. The grade of P4-AC3 (C-S7) is unaffected: the questions it asks are answered on outputs that hold at both layers (the refusal, the authority, the candidates, the three-value field; this seat's own runs at the main tree agree on every one)."
  },
  {
   "project": "NFRA_COMPEFFICACY",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~2",
   "surfaced_at": "2026-09-10T02:24Z",
   "class": "OBSERVATION",
   "id": "NFRA_COMPEFFICACY-W2-S1",
   "hazard_standing": "INERT",
   "disposition": "UNDER_INVESTIGATION",
   "one_line": "THE ACCEPT'S FRESH TREE CANNOT BE CUT FROM THE LITERAL STRING `CLOUD` WHILE THE FIX IS STILL ON THE WORKER BRANCH, so both E1 scripts cut THE INVOKING WORKTREE'S OWN BRANCH by default and print the ref they resolved. TO-CE-E-1 BOUNDS and E1-AC1 clause (b)/E1-AC2 say `git worktree add -b <scratch-branch> /c/tmp/<slot> CLOUD`. Measured at this seat 2026-09-10T02:0xZ: this worker branch wk-nfra_compefficacy-8-1 was cut from CLOUD@e8f74b6717 and CLOUD had already moved to 9328e15f45 (git worktree list --porcelain at the main tree); the fix commit is d9be5ef2c0 ON THE WORKER BRANCH and the issuer -- not the worker -- drains it. So a worktree cut from the literal ref CLOUD at execution time is the PRE-FIX tree: `git show CLOUD:.gitattributes | grep 'org/modules/graph/potion/model'` returns nothing, and the probe run against that ref returns NO TOKEN, 1 of 2 members matching (measured, --ref d9be5ef2c0^ = e8f74b6717, 58.7 s). RESOLUTION TAKEN, printed by both scripts on every run: the AFTER ref defaults to `git rev-parse --abbrev-ref HEAD` of the invoking worktree -- which IS the literal `CLOUD` when 3.0.0_SA_CVO re-runs either script from the main tree after the drain, and is the worker branch before it -- with --ref / --after-ref forcing any ref. The BEFORE (negative control) ref is NOT CLOUD either, and deliberately: it is derived as the PARENT of the commit that introduced the .gitattributes entry (`git log -1 --full-history --format=%H -S<pattern> <after> -- .gitattributes` then `^`), which is pre-fix BY CONSTRUCTION and STAYS pre-fix after the drain -- a control pinned to CLOUD stops being a control the moment the fix reaches CLOUD. INERT because left alone the default resolves correctly at both vintages; the row exists because the invocation the order names and the invocation that was run are not the same string.",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-E-1.the-crlf-rendered-model-asset.md@e8f74b6717 BOUNDS and ACCEPTANCE E1-AC1 clause (b), E1-AC2: 'a linked worktree you cut from CLOUD', 'git worktree add -b <scratch-branch> /c/tmp/<slot> CLOUD'.",
     "This seat 2026-09-10T02:0xZ: `git worktree list` at C:/tmp/wk-compeff-8-1 -> main tree C:/Users/AndrewBerman/Desktop/ajb_workspace at 9328e15f45 [CLOUD]; this worktree at d9be5ef2c0 [wk-nfra_compefficacy-8-1], cut from e8f74b6717.",
     "This seat: `timeout 300 python org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/cee1_fresh_worktree_probe.py --ref d9be5ef2c0^` -> ref sha e8f74b6717, 'ref carries `org/modules/graph/potion/model/**` in .gitattributes : NO', tokenizer.json fresh sha256 0a1168df8209a591... 713343 B vs manifest e67e803f624fb4d6... 683666 B, 'RESULT: 1 of 2 tracked file(s) MATCH the manifest', NO TOKEN, elapsed 58.7 s. Transcript C:/tmp/wk-compeff-8-1/.scratch/probe_negctl.txt (scratch, not a repo artifact).",
     "The same probe with the default ref -> 'ref: wk-nfra_compefficacy-8-1 (DEFAULT = the invoking worktree's own branch; --ref overrides)', 'ref carries ... : YES', 2 of 2 MATCH, FRESH-WORKTREE-ASSET-MATCHES-MANIFEST, rc 0, elapsed 59.4 s.",
     "org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/cee1_fresh_worktree_probe.py@d9be5ef2c0+ module docstring and test_cee1_model_asset_rendering.py@d9be5ef2c0+ docstring both carry this reasoning and both PRINT the resolved ref, its sha, and whether it carries the entry."
    ]
   },
   "spec_asserts": "TO-CE-E-1 BOUNDS and E1-AC1 clause (b) / E1-AC2: the fresh linked worktree the accept reads is cut from the ref CLOUD (`git worktree add -b <scratch-branch> /c/tmp/<slot> CLOUD`).",
   "world_is": "At execution time the fix is a commit on the worker branch that the ISSUER drains; CLOUD (9328e15f45) does not carry it, so a literal-CLOUD cut yields the PRE-FIX tree and the accept would refuse its own fix. Both scripts default to the invoking worktree's branch -- literally CLOUD when re-run from the main tree after the drain -- and print the ref they resolved.",
   "notes": "No re-run is owed after the drain for the reading to hold: the default resolves to CLOUD there by construction. The negative-control ref is pinned to the fix commit's parent rather than to CLOUD precisely so a post-drain re-run still has a real control."
  },
  {
   "project": "NFRA_COMPEFFICACY",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~2",
   "surfaced_at": "2026-09-10T02:24Z",
   "class": "BLOCKING",
   "id": "NFRA_COMPEFFICACY-W2-S2",
   "hazard_standing": "ARMED",
   "disposition": "UNDER_INVESTIGATION",
   "disarm_owner": "2.0.0_SA_COO -- the criterion-side half S40 already assigned it ('a baseline that names the relevance layer it was captured under, is 2.0.0_SA_COO's at the next cut that compares ranked lists'); the artifact itself, org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/cep4_before.json, is outside this worker's <paths> grant, so this seat can measure it and cannot re-capture it.",
   "one_line": "E1-AC1 ARM (e) IS UNSATISFIABLE BY ANY FIX THAT SATISFIES ARMS (b) AND (c) OF THE SAME CRITERION, because the baseline it compares against was itself captured under the lexical fallback. Arm (e) requires P4-AC1's three byte-equality arms (c, f, e:real-byte-equal) to PASS at the MAIN tree AND in the fresh worktree. Those arms diff live ranked lists against the STORED baseline cep4_before.json, and that file was captured in a linked worktree whose tokenizer.json was CRLF: 7 of 7 of its captured questions carry the potion ALARM in their own `terminal` block (read off the artifact by this battery, printed as arm (e)'s first line). MEASURED THIS RUN, 5 questions x 3 trees: in a tree running the LEXICAL fallback the diff is 0 lines, 5 of 5; in the MAIN tree 784/800/836/806/874 ranked-diff lines, 5 of 5 non-empty; in the FIXED fresh worktree the SAME 784/800/836/806/874, and MAIN vs FRESH is 5 of 5 BYTE-EQUAL. So the fix did exactly what the cell exists to do -- the worker slot and the main tree now read identically -- and arm (e) still reads FAIL at BOTH, because the object it compares to is the crippled reading. THE TWO CLAUSES CONTRADICT: arm (b) demands the fresh tree's bytes equal the manifest and arm (c) demands the ranker NOT be the fallback there (measured: same 78 candidates, ordering differs at 76 of 78 positions); the only world in which arm (e) passes is one where BOTH trees run the fallback, which is the defect. E1-AC1 is therefore reported FAIL by output (9 of 11 arms PASS; arms failed: e:main, e:fresh) and TO-CE-E-1 stays open. The remedy is the baseline's, not the fix's: re-capture cep4_before.json in a tree that names its relevance layer, or re-cut the clause to the cross-tree equality this battery already prints (arm e:main-equals-fresh, PASS, 5 of 5).",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "org/missions/D11/NFRA/NFRA_COMPEFFICACY/task-orders/NFRA_COMPEFFICACY.TO-CE-E-1.the-crlf-rendered-model-asset.md@e8f74b6717 E1-AC1 clause (e): 'THE ROUND-7 READING RE-TAKEN: P4-AC1's three byte-equality arms (the four C-S46 regression phrasings) PASS at the main tree AND in the fresh worktree, denominators printed, so the false RED is gone rather than moved'; and clause (b)/(c) of the same criterion, which this clause contradicts.",
     "This seat, battery run 2026-09-10T02:1xZ, `timeout 900 python org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/test_cee1_model_asset_rendering.py` rc 1, elapsed 105.3 s: '9 of 11 arm(s) PASS', 'arms failed: e:main, e:fresh', 'NOT ENFORCED -- 2 arm(s) failed. NO TOKEN.' Arm (e) header line: 'THE BASELINE'S OWN ENVIRONMENT (R-8), read off the baseline: 7 of 7 captured questions carry the potion ALARM in their `terminal` block'.",
     "Same run, arm (e) MAIN tree C:/Users/AndrewBerman/Desktop/ajb_workspace: ranked-diff 784 / 800 / 836 / 806 line(s) on the four C-S46 phrasings and 874 on REAL_Q, rows 78 (BEFORE 78) each, ALARM=False each; arm c FAIL, arm f FAIL, arm e:real-byte-equal FAIL.",
     "Same run, arm (e) FRESH tree C:/tmp/cee1-after-<pid> (cut from d9be5ef2c0, carries the entry): the identical 784 / 800 / 836 / 806 / 874, ALARM=False each, arms c/f/e FAIL; and 'CROSS-TREE: the MAIN tree's ranked lists vs the FRESH tree's, same questions: 5 of 5 BYTE-EQUAL' -> check e:main-equals-fresh PASS.",
     "This seat, exploratory run 2026-09-10T02:0xZ over three trees on the same 5 questions: SELF-UNFIXED C:/tmp/wk-compeff-8-1 (tokenizer CRLF) -> alarm=True, diff_lines_vs_BEFORE=0 on 5 of 5; MAIN and PROBE-FIXED -> alarm=False, 784/800/836/806/874, and 'MAIN vs PROBE-FIXED: 5 of 5 byte-equal', 'MAIN vs SELF-UNFIXED: 0 of 5'. Transcript C:/tmp/wk-compeff-8-1/.scratch/ (scratch, not a repo artifact).",
     "NFRA_COMPEFFICACY-S40@e8f74b6717 (3.0.0_SA_CVO, 2026-09-10T01:25Z) already carries the criterion-side half of this and assigns it: 'REMEDY (the owner's): ... and a ranked-list baseline that RECORDS the relevance layer it was captured under (semantic / lexical-fallback) so a comparison across environments refuses instead of failing'; disarm_owner names it '2.0.0_SA_COO's at the next cut that compares ranked lists'.",
     "Arm (c) of this battery, same run: 'the same 78 candidates are ordered DIFFERENTLY from the lexical fallback at 76 of 78 positions', candidate SET identical, AFTER top-10 [comp-estate, comp-pipescript, comp-dataflow, comp-find, comp-icedrill, ...] vs BEFORE top-10 [comp-estate, comp-pipescript, comp-cluster, comp-constants, comp-dataflow, ...]. This is the measurement that makes arm (e) unsatisfiable rather than merely unmet."
    ]
   },
   "spec_asserts": "E1-AC1 clause (e): P4-AC1's three byte-equality arms PASS at the main tree AND in the fresh worktree after the fix, 'so the false RED is gone rather than moved'.",
   "world_is": "Those arms compare against a STORED baseline captured under the lexical fallback (7 of 7 of its questions carry the ALARM in their own payload). After the fix both trees rank SEMANTICALLY and both diff non-empty against it (784/800/836/806/874 lines, 5 of 5 questions, at each tree), while MAIN and the fresh worktree are 5 of 5 BYTE-EQUAL to each other. The clause can only pass in a world where both trees run the fallback, which is the defect this cell removes; the artifact that would have to change is outside this worker's grant.",
   "notes": "BLOCKING on E1-AC1 only: E1-AC2 passes by output and arms (a), (b), (c), (d), (f) and e:main-equals-fresh all PASS. ARMED because the same stored baseline is what every future cell comparing comp-which ranked lists will diff against, and a lexical-captured baseline reads as a RED on any correctly-configured tree. This seat filed the row and kept working rather than re-capturing the baseline: cep4_before.json is under deliverables/0.9.0_WK_NFRA_COMPEFFICACY~1/ and this order's <paths> grant names only deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/."
  },
  {
   "project": "NFRA_COMPEFFICACY",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_NFRA_COMPEFFICACY~2",
   "surfaced_at": "2026-09-10T02:24Z",
   "class": "OBSERVATION",
   "id": "NFRA_COMPEFFICACY-W2-S3",
   "hazard_standing": "ARMED",
   "disposition": "UNDER_INVESTIGATION",
   "disarm_owner": "2.0.0_SA_COO -- the act is one re-render of the path in each linked worktree that already holds the CRLF bytes when the fix lands on that worktree's branch (`git checkout -- org/modules/graph/potion/model/tokenizer.json` there, or cut a new worktree); the slots are the COO's. 0.8.0_AE_CloudComp owns the asset itself (per S40) if the disposition instead prefers a renormalise commit.",
   "one_line": "THE FIX CONVERTS A SILENT CONVERSION INTO A VISIBLE `M`, AND UNTIL EACH ALREADY-CUT WORKTREE RE-RENDERS THE PATH, A BROAD `git add` THERE WOULD COMMIT THE CRLF BYTES INTO THE INDEX AND BREAK THE PIN FOR THE WHOLE ESTATE. With `org/modules/graph/potion/model/** binary` the eol conversion stops, so git compares working bytes to the index blob DIRECTLY -- correct, and the point of the fix -- but a worktree cut BEFORE the fix still holds the 713,343 B CRLF file on disk against the 683,666 B LF index blob. Measured at this seat 2026-09-10T02:0xZ in C:/tmp/wk-compeff-8-1: before the attribute `git status --porcelain` showed only ' M .gitattributes' (git's stat cache hid it); after invalidating the stat cache with a bare `touch` -- BYTES UNCHANGED, sha256 still 0a1168df8209a591..., only mtime moved -- it shows ' M org/modules/graph/potion/model/tokenizer.json' and `git diff --stat` reads 'Bin 683666 -> 713343 bytes'. CENSUS OF THE LIVE FLEET, denominator printed: 11 worktrees in `git worktree list --porcelain`; 6 of 11 do not carry the file at all; of the 5 that do, 1 (the MAIN tree) holds the LF bytes e67e803f624fb4d6... and 4 hold the CRLF bytes 0a1168df8209a591... -- C:/tmp/mstr-reconcile-20260904, C:/tmp/wk-cldgrph-6-2, C:/tmp/wk-compeff-8-1 (this seat's) and C:/tmp/wk-etfs-2-1, two of them other live workers' slots. NONE of them shows the M today because the entry is not on their branches yet; each will the moment the fix reaches the branch it is checked out on. THE HAZARD IS NOT THE `M`, IT IS WHAT A SEAT MIGHT DO WITH IT: staging that path (a broad `git add -A`, a `git commit -a`) writes the 713,343 B blob into the index, and then the manifest hash e67e803f624fb4d6... is wrong EVERYWHERE, main tree included, and the semantic ranker fails closed estate-wide instead of in worker slots only -- the same defect one grain worse. `.tools/safe-commit.sh -- <paths>` does not stage it (this seat's own fix commit d9be5ef2c0 named `.gitattributes` alone and staged 1 file). This seat did NOT restore its own copy: rewriting model bytes is refused by this order's BOUNDS and org/modules/graph/potion/model/ is not in its <paths>.",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     ".gitattributes@d9be5ef2c0 last line `org/modules/graph/potion/model/** binary`; `git check-attr -a org/modules/graph/potion/model/tokenizer.json` at C:/tmp/wk-compeff-8-1 -> 'binary: set', 'diff: unset', 'merge: unset', 'text: unset'.",
     "This seat, C:/tmp/wk-compeff-8-1, 2026-09-10T02:0xZ: `git status --porcelain` -> ' M .gitattributes' and '?? .scratch/' ONLY; then `touch org/modules/graph/potion/model/tokenizer.json` (mtime 2026-09-09 22:01:25 -0400, sha256 UNCHANGED at 0a1168df8209a591defdc781567f11f8ea5b400c60b994350f8892e7bdfe829b, size UNCHANGED at 713343 B) and `git status --porcelain` -> adds ' M org/modules/graph/potion/model/tokenizer.json'; `git diff --stat -- org/modules/graph/potion/model/` -> 'org/modules/graph/potion/model/tokenizer.json | Bin 683666 -> 713343 bytes'.",
     "Fleet census, this seat, same tick: `git worktree list --porcelain | grep '^worktree '` -> 11 paths; sha256 (first 16) and size of org/modules/graph/potion/model/tokenizer.json in each -> e67e803f624fb4d6 / 683666 at C:/Users/AndrewBerman/Desktop/ajb_workspace; 0a1168df8209a591 / 713343 at C:/tmp/mstr-reconcile-20260904, C:/tmp/wk-cldgrph-6-2, C:/tmp/wk-compeff-8-1, C:/tmp/wk-etfs-2-1; ABSENT at C:/tmp/staudt_layerD_T0..T3, C:/Users/AndrewBerman/Desktop/ajb_workspace/.claude/worktrees/agent-acc852ec7d8dbfdc5 and C:/Users/AndrewBerman/Desktop/scty-build.",
     "org/modules/graph/potion/MANIFEST.json@d9be5ef2c0 model_files_sha256.tokenizer.json = e67e803f624fb4d67dea1c730d06e1067e1b14d830e2c2202569e3ef0f70bb50, model_files_bytes.tokenizer.json = 683666; org/modules/graph/potion/potion_embed.py:57-63 raises on mismatch, :82-94 emits the ALARM and returns None.",
     "Fix commit d9be5ef2c0 (this seat, `bash .tools/safe-commit.sh ... -- .gitattributes`): '1 file changed, 27 insertions(+)' -- a path-named safe-commit does not stage the model file even while it reads modified."
    ]
   },
   "spec_asserts": "TO-CE-E-1: 'the fix is one attribute (or an LF-normalised manifest)' and 'NO MODEL BYTES ARE REWRITTEN. You may change how git RENDERS the asset ... You may not edit tokenizer.json or model.safetensors themselves'. The order does not say the attribute has an effect on trees that already exist.",
   "world_is": "The attribute takes effect at CHECKOUT, so a worktree cut before it renders CRLF forever and, once the entry reaches its branch, reports that path as MODIFIED (Bin 683666 -> 713343). 4 of the 5 live worktrees that carry the asset hold the CRLF bytes today. Restoring them is a write to org/modules/graph/potion/model/, which this order's BOUNDS and <paths> both refuse to this worker, so the condition is surfaced and left standing.",
   "notes": "ARMED, and the direction matters: the fix makes a previously INVISIBLE divergence VISIBLE, which is the intended fail-loud property -- the hazard is the one act that would convert the visible M into a committed blob. `binary` was chosen over `-text` alone partly for the adjacent case (-merge turns a silent auto-merge of the pinned asset into a conflict); it does not cover this one, which is a checkout-vintage condition and not a merge."
  }
]
```
