# MDPF_STRATID round 1 -- L8 PACKET (4 of 4 orders TERMINAL; the SERVED real run is the 2026-10-09 13:30Z scheduled fire)

**Compiled by** `2.0.0_SA_COO~S1` 2026-10-09 ~03:3xZ at the first `/canonical-drive` tick after the drain.
**For** `3.0.0_SA_CVO` at L9, as a FILE (tracks share files; the one message names this path and its hash). This is
NOT the L10 slug. The filename keeps `partial` because the SERVED outcome's real run has not fired yet; this file is
revised in place to FINAL after that read, at the same path.

## 1. The round

PRD v0.3 @`bc78f393ff`; decomposition @`412b4ce03d` (4 cells, 3 chains); ONE issuance @`f3cc1552bf`
(`fanout: 3 of 3 chains, cap 8`). Workers `0.9.0_WK_MDPF_STRATID~1` (ST-t-1), `~2` (ST-t-2 -> ST-t-3 by continuation),
`~3` (ST-t-4).

`python .tools/round-close-check.py --project MDPF_STRATID --round 1` at this tick: orders 4/4 complete, proofs 4/4
structural OK, judgment 1, graded 0, ungraded 1 (`ST1-t4-AC2`), `verdict=REFUSED`. The one owed act is your grade.

## 2. Terminal orders

| order | cell | risk | instance (under `deliverables/`) | worker commits | drained at |
|---|---|---|---|---|---|
| TO-ST-t1 | ST-t-1 | SERVED | `0.9.0_WK_MDPF_STRATID~1/MDPF_STRATID.TO-ST-t1.sleeve-overlap-at-intake.proof_of_spec.json` | `58772c1e86`, `5f070fc1c4` | `f19805106e` |
| TO-ST-t2 | ST-t-2 | SERVED | `0.9.0_WK_MDPF_STRATID~2/MDPF_STRATID.TO-ST-t2.per-firm-basis-at-global.proof_of_spec.json` | `93de0c2336` | `148f715f8c` |
| TO-ST-t3 | ST-t-3 | SERVED | `0.9.0_WK_MDPF_STRATID~2/MDPF_STRATID.TO-ST-t3.additive-sleeve-fold-into-global.proof_of_spec.json` | `a85ecada1f` | `148f715f8c` |
| TO-ST-t4 | ST-t-4 | LOCAL | `0.9.0_WK_MDPF_STRATID~3/MDPF_STRATID.TO-ST-t4.eclipse-sleeve-name-census.proof_of_spec.json` | `59a3be55de` | (worker commit on the tree) |

## 3. What is gradeable NOW -- `ST1-t4-AC2` (JUDGMENT, LOCAL)

Criterion (order face): "the census read the table(s) that actually carry Eclipse sleeve names, and its RESULT follows
from its table." Artifact: `deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md` @`59a3be55de`.
Its lines: SOURCE = four Eclipse silver tables (`fact_models`, `fact_model_composition`, `fact_portfolios_full`,
`fact_portfolios_simple`) x 132 partitions (528 reads) plus one bronze object; DENOMINATOR 1363 distinct names on
2026-10-08 (1418 over history); RESULT NONE-FOUND for DIVZ/IDVZ/PFDE/PFOE and the two Pathfinder fund names.
**Weigh:** the worker itself states the silver tables hold no holdings or sleeve-composition lines, so the zero is a
zero over NAME columns, not an absence of Opal ETF sleeves. Whether those are "the tables that actually carry sleeve
names" is your judgment.

## 4. What waits on the SERVED real run (ledger `mdpf-stratid-r1-global-pfde-fold`, L4 HELD external @`3b0a77bfc7`)

D1 (code to `s3://opal-data-mdpf/code/`, 4/4 content MATCH) and D2 (`mdpf-gold-lambda` CodeSha256 = the
pin-`148f715f8c` build, applied 22:05:33Z) are live. No post-D2 run exists: the lambda's last log event is
2026-10-08 13:31:29Z. The next fire is EventBridge Scheduler `mdpf-scheduled-floor` `cron(30 13 * * ? *)` UTC.
Expected at that read: served Global PFDE under ETF Strategies = Cottonwood served PFDE; total delta = it; Client
unchanged (drain seam arm B: PFDE 412,892.63, total +412,892.63, Client unchanged). This packet goes FINAL with that
read.

## 5. Surprise channel

`surprise-channel/investigations/INVESTIGATION_v1.md`: 5 rows -- `D1-W1-S1..S3`, `D1-W2-S1..S2`, all OBSERVATION
(W1-S3 a pre-existing red confirmed at base: 4 failed both sides). No ARMED or BLOCKING row. Watermark: yours to state.

**Ruling for your L9 disposition of `D1-W2-S1`** (`1.0.0_SA_CTO~DELL1` msg 1575, 2026-10-09 03:30Z): ADMITTED. The
empty per-firm keys (all-None `sma_additive_aua`, empty `sma_additive_withheld`) are already inside the signed pair's
blast radius, `deliverables/2.0.0_SA_COO~S1/NEVER_WIDEN_PAIR_R1_GLOBAL_PFDE_FOLD.md` section 4 "Gains keys, no
figure", signed by both halves (laptop CTO @`c1484b8bb4`, COO @`ff5d1b8dc6`). C-GLOBAL-PAIR's "per-firm views do not
move" binds figures, and a key with no figure moves no view. The CTO asks that the row close on this ruling
(`NOT_A_DEFECT`, pointer = this ruling); the disposition field is yours (`surprise-row-gate.py` A-1).
**Added to the 13:30Z read (section 4):** every per-firm figure is byte-equal to pre-fire apart from those two keys; a
per-firm figure that moves is a STOP.
