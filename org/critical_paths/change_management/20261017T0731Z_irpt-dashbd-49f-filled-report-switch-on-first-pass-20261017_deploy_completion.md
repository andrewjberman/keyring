# Deploy Completion Record
**Date opened:** 2026-10-17T07:31:21.633859+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-328 (the 49F filled-report switch-on pair, round 150, IB-pr-551 hop 2): a new publish bundle (code only, 0/1/0), the one environment variable FILLED_REPORT_PASS (0/1/0), a dry run in seven shards, ONE canary, the mint leg and ~S2's V leg, the full pass in seven shards, the after-read. Gate 0(c): no open leg on the publish function, the reporting-publish root or the reporting prefix at the worktree census.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | function-map artifact_sha256 for irpt-49f-reporting-publish-lambda, the one lambda.tf environment line, plus this ledger sentinel and the receipt, committed with explicit paths | commit ids recorded |  | OPEN |
| L2 | s3-prefix | the publish artifact key: a NEW VERSION built == landed == the packet hash 4SF81dqn.. (17 members); the rollback version oXM0wQg8.. kept | new VersionId | built == landed == 4SF81dqnVu8rqP3xT0dWtQ8br1w9hvjQft/0knAtaic= (17 members); new version Nh.5z_OquDPiUL0VYa9CdkJqkQ0NqvZJ; rollback version oXM0wQg8.. kept | CLOSED 20261017T110809Z |
| L3 | tf-lambda | TWO safe-applies of reporting-publish, each exactly 0 add 1 change 0 destroy: the code attributes, then the one environment variable; each with a clean re-plan; the exact OFF probe between them | plan counts, replan No changes, probe_off | two safe-applies of reporting-publish, each plan 0 add 1 change 0 destroy (code attributes; then FILLED_REPORT_PASS=1), replans No changes; OFF probe exact between them; schedule inputs clean | CLOSED 20261017T110809Z |
| L4 | verify | the dry run in seven shards writes nothing (object count equal before and after) | shard table | dry run 28 shards: clients 4776, would-write 4012, not available 764, refused 0; peak 846 MB (line 900), longest 149 s (line 240); prefix 18257 objects before and after; the first 7-shard attempt (300 s, 847 MB) and two probes are in the notes | CLOSED 20261017T110809Z |
| L5 | s3-prefix | ONE canary written (a new object under client=<id>/filled_report.json) and ~S2's V leg graded; both synthetic rows removed and read ABSENT twice if minted | canary digest, grades | one canary (digest dde0e6ed7721) written once, validates, prefix +1, S2 step 1 PASS; V leg: nothing minted, steps 2 and 3 OWED (no viewer session pair), per CTO msg 10467 | CLOSED 20261017T110809Z |
| L6 | s3-prefix | the full pass in seven shards equal to the dry run's sums; the prefix gains exactly the would-be total minus 1 | full table | full pass 28 shards equal to the dry run's sums (4012 written, 764 not available, 0 refused); peak 838 MB, longest 150 s; the prefix gained 4011 | CLOSED 20261017T110810Z |
| L7 | verify | the after-read and the receipt: counts, function, policy, schedules | record and criteria | after-read and the receipt written; counts equal (series, summary, manifests), filled 4012; role policy and schedules unchanged | CLOSED 20261017T110810Z |

## Log

- 20261017T073121Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
- 20261017T110809Z LEG L2 closed: built == landed == 4SF81dqnVu8rqP3xT0dWtQ8br1w9hvjQft/0knAtaic= (17 members); new version Nh.5z_OquDPiUL0VYa9CdkJqkQ0Nqv
- 20261017T110809Z LEG L3 closed: two safe-applies of reporting-publish, each plan 0 add 1 change 0 destroy (code attributes; then FILLED_REPORT_PASS=1), 
- 20261017T110809Z LEG L4 closed: dry run 28 shards: clients 4776, would-write 4012, not available 764, refused 0; peak 846 MB (line 900), longest 149 s (
- 20261017T110809Z LEG L5 closed: one canary (digest dde0e6ed7721) written once, validates, prefix +1, S2 step 1 PASS; V leg: nothing minted, steps 2 and 
- 20261017T110810Z LEG L6 closed: full pass 28 shards equal to the dry run's sums (4012 written, 764 not available, 0 refused); peak 838 MB, longest 150 s
- 20261017T110810Z LEG L7 closed: after-read and the receipt written; counts equal (series, summary, manifests), filled 4012; role policy and schedules un
