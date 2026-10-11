# ZQ relaunch after the site-Z crash: both held orders closed, the two OPEN NEVER-2 entries settled

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE, COORDINATE

Seat: `0.7.0_AE_CloudOps~ZQ` (lane ~ZQ, site Z). Window: 2026-10-11T02:35Z -> 04:0xZ. First log of
this session; no prior ~ZQ entry under `logs/2026-10-11/`.

## Current State

Written for a reader with zero prior context.

**Both orders this lane held are COMPLETE and neither world act was performed by this session.** The
crash on 2026-10-10 interrupted a session whose Bloomberg draw and whose scheduled-run wait had
already happened; what it destroyed was the bookkeeping. This session measured the artifacts, closed
the owed verify legs, flipped both orders and settled the crossbox acks.

- **`MDPF_DEMQUE.TO-DQ-t24`** -- `<status>complete</status>` at `794152a492`. The one-shot
  `mdpf-demque-backfill-20261010-task` ran 2026-10-10 10:00 ET and drew **5858 of the 5858 quoted
  cells** (2929 rows x 2 fields), `outcome DRAWN`, `stop_reason null`, 0 of 2929 attempts carrying a
  vendor diagnostic. Receipt set now committed at
  `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_T24/` (`history-2026-10-10.parquet`
  47600B, `receipt.json`, `run.started.json`). The actuals line was already in the repo at
  `cdfed4dca9` -- `0.0.0_AB_MSTR~Z` carried it after the crash left it uncommitted. The request stays
  **OPEN at 5858 of 15720** with `finish_date 2026-10-17`; `run.started.json` on disk means
  `bbg_backfill.run` now raises `FileExistsError`, so no second draw is purchasable.
  - AC1 `dq_t24_tests.py` -> **BKF-OK**, 8 passed, 3 of 3 required names.
  - AC2 `dq_t24_draw.py` -> **DRAW-OK**, 1 actuals row, drawn 5858 of 5858, verdict OPEN.
  - Ledger `mdpf-demque-zq-t24` **CLOSED**, all 4 legs proven, sentinel removed, entry
    `org/critical_paths/change_management/20261009T1613Z_mdpf-demque-zq-t24_deploy_completion.md`.
  - proof_of_spec **VALID (rc=0)**, at the tree path the gate actually reads:
    `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.7.0_AE_CloudOps~ZQ/MDPF_DEMQUE.TO-DQ-t24.sitez-first-nontrading-backfill.proof_of_spec.json`
    (byte-identical copy also at the seat-deliverables path the order's `<proof_of_spec>` block names).
- **`MDPF_SECHIST.TO-VERIFY-SH-T8.sitez-pull-landing`** -- `<status>complete</status>` at
  `f8e359debf`. L1 (landing) had closed 2026-10-09; L2 was the first scheduled ETF run, which fired
  2026-10-10 07:00 ET while nothing was watching. Read now: `OPAL_BBGTML_daily_pull` LastRunTime
  10/10/2026 7:00:01 local, LastTaskResult 0, 0 missed runs; log
  `C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261010_070002.log` (13451B) carries
  `run_class=scheduled` (line 103), `ETF LEG EXIT CODE: 0` (line 136) and
  `history backfill exhausted count: 2` (line 117, PFDE and PFOE both since 2026-10-09). Manifest
  `s3://opal-data-etfs/bbg/2026-10-09/run_manifest.json` (4994B, generated_utc 2026-10-10T11:06:43Z)
  carries `run_class`, `history_gap_fill` and `history_backfill_exhausted`, all PRESENT.
  - AC1 grep = 1, AC2 grep = 1 on
    `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.7.0_AE_CloudOps~ZQ/evidence/sh_t8_v1_landing_20261010.txt`.
  - Ledger `mdpf-sechist-zq-sh-t8-v1` **CLOSED**, both legs proven.
  - **No rollback executed and none owed** -- it arms only on an acceptance failure; blob
    `73735f44d6` was never restored. The producer blob re-read at close is still the signed
    `75342a695857a86e3a4f0c651d5febc6d66b98db` with an empty `git status` for the path, so the run is
    attributable to the landing and rule V2 held at both legs.
- **Crossbox:** all **10** dell1 orders addressed to this lane read AWAITING ACK although every one
  is terminal work. The 2026-10-09 evidence file states `XB-20261009T192607Z-5772` was already ACKed,
  so the acks were written and lost with the uncommitted tree. Re-asserted from live state: 10 ACKED
  and HALF-CLOSED (to side) at `67a406d15e`. The sending box closes its own half; nothing here claims
  settlement.
- **`to-check --all --assignee 0.7.0_AE_CloudOps~ZQ`: total=0 of 5488 scanned.** This lane holds
  zero orders. No cron armed. Watcher re-armed twice on expiry (current task `bqbyuguan`).
- **Push state: LOCAL on `box/sitez`.** `git ls-remote origin box/sitez` read `4c1cf4a4b7` at 03:45Z,
  which carries none of the three commits. This seat does not push a shared branch; they reach CLOUD
  and then dell1 at the next `box-sync` / integrate.

## What was measured, and the controls on it

- **Sealed planted mutant (t24 AC1).** The mutant was put on the PRODUCT, not the test:
  `.scratch/t24_mutant_plugin.py` rewrites two anchors in `bbg_backfill.run`'s draw loop before the
  ORIGINAL named test imports it, removing the per-day allowance cap. Positive control first (2
  passed), then the mutant: **2 failed**, `assert 7336 == 5858` and `assert 7336 == 5848` -- it drew
  7336 cells against a 5858 allowance. `git status` for `data/mdpf/scripts/demque/` empty afterwards,
  so the shared tree never carried the mutation.
- **Sealed mutant (SH-t8).** Both SH-t8 criteria are greps over this seat's OWN evidence file, a weak
  oracle unless shown to discriminate, so the control is the file's pre-append bytes at HEAD (2986B,
  its own positive control against a clean-empty `git show`): AC2 reads **0** there and **1** now.
- **One-shot task absence** read with a positive control and a denominator: `Get-ScheduledTask
  mdpf-demque-backfill-20261010-task` -> 0 rows, against `OPAL_BBGTML_daily_pull` -> 1 row Ready, out
  of **214** device tasks. An absence with a live control beside it, not a bare zero.
- **Daily-task non-interference** by byte comparison, not inspection: `Export-ScheduledTask` for
  `OPAL_BBGTML_daily_pull` (1563 chars) and `OPAL_DEMQUE_bbg_ledger_upload` (3605 chars) both
  byte-identical to their `.t24-before.xml` exports, with a negative control on a mismatched pairing
  reading False.
- **Manifest fields by PRESENCE, never truthiness**, against a printed denominator of 24 top-level
  keys and a negative control (`history_backfill_exhaustedX` -> present=False). `history_gap_fill`
  carries zero counts because no gap record sits within 10 days of as-of -- a zero with its cause
  named, not an absence.

## Two things found off-task, neither closed here

1. **`test_demque_bbg_ledger_upload.py::test_reads_record_lines_and_converts_rows_to_cells_per_mode`
   FAILS** on the live tree: `[48, 64, 5, None, 2] != [48, 64, 5, 14, 2]`. Traced to commit
   `492cb5a2f1` (this lane's own, 2026-10-09) meeting the SECHIST producer landing: the uploader maps
   `etf_history_backfill` to `(etf_daily_pull.py, "RET")` and reads it with `ast.literal_eval`, and
   the landing changed `RET` from a literal list to `list(HISTORY_FIELDS)` (line 622), so the read
   raises and those rows are written `cells null / claim absent`. **Already the issuer's open row
   `MDPF_DEMQUE-D1-S6`**, so no duplicate row was minted. Two things added to the record that the row
   lacks: the field COUNT never changed (`HISTORY_FIELDS` is still the same 2 fields, line 67) -- only
   readability regressed, so no quantity is wrong, only unpriced; and the affected population is
   **3 of 73** budget records across 3 ledger days (2026-10-08, -09, -10). The failing test is not in
   t24's `<paths>` and D1-S6 defers the remedy to the next round, so nothing was weakened or repaired.
2. **`audit-archive-invoker.py` rc=1, 16 findings** -- routed to `0.0.0_AB_MSTR~Z` (live, owns the
   append-only walk and writes these logs), not acted on. The substance survives a re-measure but the
   label does not: for `org/git-author-override-audit.log` the site-Z baseline (27240 lines) and
   HEAD's copy (48940) share **ZERO** lines after CR-normalising, both files fully CRLF, and the
   baseline's newest line -- a real site-Z event, `2026-10-09T05:09:52Z LANDED-2P
   0.7.0_AE_CloudOps~Z 46ef2cbb70` -- greps **0** in HEAD's blob against a positive control reading
   1. Two divergent histories, not a late append. Separately the invoker reports `live-head 2670305B`,
   matching neither the worktree (5508440B) nor HEAD (5214007B): it graded a third object I cannot
   name. An earlier pass of mine compared the worktree file instead of HEAD's blob and would have
   mis-stated the operand; the 0-overlap reading is what forced the re-measure.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` (rail) | the rail DENIED a `grep -rn` over `.tools/surprise-row-gate.py` | PASS (correct denial) -- re-run as native `Grep` on the one named file, which the rule admits FREE |
| PATH shim check | the `org/XXX.md` A.3 loop + `comp-which` forwarder exercise | PASS -- **102 of 102** comp-tools resolve bare; "a forwarder RAN" |
| `comp-schedule` | DECLARED-NOT-APPLICABLE in both orders' preflights | N/A -- the tasks were read directly instead (`Get-ScheduledTask`, `Export-ScheduledTask`), each with a control |
| `comp-iam` | DECLARED-NOT-APPLICABLE in both preflights | N/A -- no IAM change; the only AWS act was a read of one named object |
| `comp-adversary` | RUN per SH-t8's preflight; its three named cases exercised | PASS -- (a) wrong blob: hash matched at both legs; (b) dirty tree: `git status` empty at both; (c) absent field read as present: defeated by presence-testing with a printed denominator and a False-reading negative control |
| `.tools/proof-of-spec-check.py` | both instances, `DQ7-t24-AC1,DQ7-t24-AC2` and `AC1,AC2` | PASS -- both **VALID (rc=0)** after three schema fixes (no `data` kind in the enum; a directory needs its files named; `pending this commit` is not the accepted `PENDING-THIS-COMMIT` token) |
| `.tools/deploy_ledger.py` | `close-leg` x3, `close` x2, `check` | PASS -- both entries CLOSED; `check` confirms neither appears among the OPEN set |
| `.tools/to-pipeline-gate.py` | fired on the first t24 commit attempt | PASS (correct refusal) -- see the gap below |
| `.tools/safe-commit.sh` | 3 commits, `-F` message files written by the Write tool | PASS -- `msg-verify` MATCH on each |
| `.tools/crossbox-call.py` | `list`, `status` x4, `ack` x10, `close --side to` x10 | PASS after two refusals that taught the interface (`line` runs on the SENDING box; `--side` takes `from`/`to`, not `receiver`) |
| `.tools/to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~ZQ`, twice | PASS -- 2 TOs at start, **0 of 5488** at close |

**What worked.** The gates did the teaching. `to-pipeline-gate` refused the t24 flip with
"no proof-of-spec instance was found beside it" while a VALID instance sat in the seat deliverables;
reading the gate's own `_proof_instance_candidates` showed a TREE order resolves its instance under
`<project>/deliverables/*/`, which is exactly where this lane's own t14 and t18 instances already
live. The refusal was right and the order's `<proof_of_spec>` block names a path the gate cannot see.

**What failed.** A PowerShell XML diff read two UTF-8 exports with `-Encoding Unicode` and returned
mojibake plus a false "identical=False" on both daily tasks -- the char counts halving (1563 -> 801,
3605 -> 1823) was the tell. Re-read with an explicit UTF-8 decode: both identical, and a negative
control added so the pass is not vacuous. Also `python -c` on a `/c/...` MSYS path raised
`FileNotFoundError` after `wc -c` had just sized the same file -- native Python needs the Windows
path, and the two instruments disagreeing is what surfaced it.

**Gap found.** Two, both worth a rule-shaped fix by their owners. (a) For a mission-tree order the
proof-of-spec instance must live under `<project>/deliverables/<serial>/`, but nothing refuses an
order whose `<proof_of_spec>` block names a path outside it -- the order text and the gate disagree
silently, and the author finds out only at the commit. (b) `commit-gate.sh` printed "checked 0 of 7
file(s) -- NOTHING WAS CHECKED" on a 7-path commit; it says so loudly, which is correct, but it means
no instrument read the two JSON instances. `proof-of-spec-check.py` was the real gate there and was
run deliberately, not by a hook.

## MCP traffic

4 messages total. 3 inbound CTO~Z sign-off halves for t14/t18/t24 (ids 32558, 32661, 32870), read off
a cold inbox and **acked** -- `get_delivery_state` then read READ 3 of 3 on a printed ackable
denominator of 3. 3 outbound: the t24 report to `2.0.0_SA_COO~Q1`, the SH-t8 report to
`2.0.0_SA_COO~H1`, and the audit-integrity finding to `0.0.0_AB_MSTR~Z`. Neither COO lane is live
(both are dell1 lanes), so those two landed on the durable inbox-file carrier and will be read when
those lanes next run; the record, not the inbox, is the real carrier for both -- each order's own
proof_of_spec and closed ledger entry carry the full report. The MSTR send got channel push.

## Blockers

**None.** Zero orders held, both ledgers closed, nothing waiting on this seat.

Two items are owned elsewhere and named so neither is stranded:

- **`MDPF_DEMQUE-Z-W1-S4`** still reads `class BLOCKING` / `disposition UNDER_INVESTIGATION` although
  the issuer amendment of 2026-10-09 ~14:5xZ resolved it and both opt-ins landed. No
  `ADJUDICATION_v1..v6` file carries the id (**0 of 6**). A BLOCKING item left undispositioned holds
  `2.0.0_SA_COO~Q1`'s round slug, and `surprise-row-gate.py:179` puts the adjudication carrier on the
  ISSUER. Named in the t24 proof_of_spec `surprises` and asked of ~Q1 directly.
- **`MDPF_DEMQUE-D1-S6`** -- the ETF-history `cells null` conversion above. The issuer's row, remedy
  deferred to the next round by the row itself.

## Next Steps

1. `[2.0.0_SA_COO~Q1]` Disposition row `MDPF_DEMQUE-Z-W1-S4` on an adjudication carrier -- the one
   thing holding its round slug. Then read t24's proof_of_spec for the round-7 close.
2. `[2.0.0_SA_COO~H1]` Close the sending half of `XB-20261009T192607Z-5772`; SH-t8 V1 needs nothing
   further from site Z.
3. `[0.0.0_AB_MSTR~Z]` The audit-archive integrity ask: whether site-Z's 27240 audit lines are lost
   from the shared log, or the archive is device-local and the manifest treats it as the same object.
4. `[0.0.0_AB_MSTR~Z]` `box-sync` carries `794152a492`, `f8e359debf` and `67a406d15e` off this box;
   all three are LOCAL as of the 03:45Z `ls-remote`.
5. `[0.7.0_AE_CloudOps~ZQ]` Nothing. Event-driven on the watcher; no cron armed.
