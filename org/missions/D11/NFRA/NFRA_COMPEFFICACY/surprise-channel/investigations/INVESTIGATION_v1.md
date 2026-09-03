# NFRA_COMPEFFICACY -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Assembled by:** `3.0.0_SA_CVO` (L8: the CVO assembles, any seat surfaces -- `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.4).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY` (Andrew-direct
2026-09-02 23:0xZ: the row gate is the control).
**Round 1 task orders:** ONE live -- `TO-CE-T-1` at `0.8.0_AE_CloudComp` (TO-CE-DISC-2 and TO-CE-TP-1 WITHDRAWN 02:25Z,
their decisions landed at L4 in PRD v0.4 @19bf1c7322). L10 routing waits on that TO's completion AND every row below
CVO-checked.
**Append-only during the round.** Denominator at this write: **6 rows** (S6 appended by `3.0.0_SA_CVO` 04:2xZ, the L9 disposition and L10 stamp of the S2/S3/S5 item; S5 appended by `0.8.0_AE_CloudComp`
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
  }
]
```

-- S1: `3.0.0_SA_CVO` (L8 assembly). S2, S5: `0.8.0_AE_CloudComp` (direct append, tree-channel lane ANY, CLAUDE.md s.2 2026-09-03 correction). S3, S4: `3.0.0_SA_CVO` (L9 adjudication, direct append per the corrected law).
