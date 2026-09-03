# NFRA_COMPEFFICACY -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Assembled by:** `3.0.0_SA_CVO` (L8: the CVO assembles, any seat surfaces -- `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.4).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY` (Andrew-direct
2026-09-02 23:0xZ: the row gate is the control).
**Round 1 task orders:** ONE live -- `TO-CE-T-1` at `0.8.0_AE_CloudComp` (TO-CE-DISC-2 and TO-CE-TP-1 WITHDRAWN 02:25Z,
their decisions landed at L4 in PRD v0.4 @19bf1c7322). L10 routing waits on that TO's completion AND every row below
CVO-checked.
**Append-only during the round.** Denominator at this write: **4 rows** (S3 + S4 appended by `3.0.0_SA_CVO` 04:0xZ -- the L9 adjudication in append-only form: S3 the recurrence of S2 measured at the CVO seat, S4 the closure of S1; S2 appended by
`0.8.0_AE_CloudComp` under the tree channel's lane-ANY worker-appends grant, CLAUDE.md s.2 as
corrected by Andrew-direct 2026-09-03 03:1xZ -- "a broker message is NEVER the carrier"; S1's own
text and CVO attribution are UNCHANGED below).

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
  }
]
```

-- S1: `3.0.0_SA_CVO` (L8 assembly). S2: `0.8.0_AE_CloudComp` (direct append, tree-channel lane ANY, CLAUDE.md s.2 2026-09-03 correction).
