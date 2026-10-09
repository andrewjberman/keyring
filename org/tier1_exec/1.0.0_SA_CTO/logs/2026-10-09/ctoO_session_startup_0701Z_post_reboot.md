# 1.0.0_SA_CTO~O -- post-reboot startup, 2026-10-09 07:01Z-07:2xZ

**archetype:** COORDINATE

## Startup

- Site Z rebooted at 06:58Z (`LastBootUpTime`). The wind-down ask (msg 32449) no longer applies.
- `/watcher` steps:
  - Registered at PID 5572.
  - Monitor `bh4px6hv1`, script pid 7296. One row only.
  - Six unread messages read and acked (32427, 32435, 32436, 32447, 32449, 32476).
- `org/XXX.md` A.1-E: done. 102 of 102 comp-tools resolve bare. `to-check --all --assignee` reads 0 TOs held.
- Crons: zero armed at launch, per the launch order. The `LIVE_ARMS.md` row for the `~O` `/self-drive 30m` is still
  live; re-arming it is Andrew's call. `1.0.0_SA_CTO~Z`'s 60m row now names NFRA_MCPORTAL, NFRA_OPALAI and
  NFRA_MCPINDEX too, so the scopes overlap on those three.

## Acts

1. **NFRA_OPLGTW r29: CTO half SIGNED @d3f04813df.**
   - Signed against ANNOUNCE @368e48e533, release sha 91811b648a.
   - The diff was read at the sha: asker SAFE, the SendGate race, and `calendar_months` with one rule at read and
     write.
   - Two observations, not conditions:
     - the 13-month window is inclusive at both ends;
     - `schwab_list_files` keeps its pre-existing 30-day per-call span.
   - The CVO~Z half is still owed. The window opens 11:00Z.
2. **NFRA_MCPINDEX v0.8 @0eff9e0e6d: FWD-19, the operations lead's trade rec and billing readers.**
   - This meets condition (a) of the dell2 relay.
   - The ratified-text half was asked of `3.0.0_SA_CVO~Z`. The brief half reads SIGNED (auto).
3. **NFRA_MCPORTAL CP2 (msg 32427):** answered by Andrew's approval (msg 32447 @3cb48a4ca7). No ruling owed.

## Open calls

None at Andrew from this seat.

## Next step

- Wait for the CVO~Z halves: OPLGTW r29 Half 3, and MCPINDEX v0.8 ratified text.
- Then the COO~O applier order inside 11:00-23:00Z, and MI's round 9 cut.

## Compiler Tools

- `comp-which`: the forwarder exercise ran.
- `to-check.py --all --assignee`: 0 held.
- `prd-signoff.py status NFRA_MCPINDEX`: ratified-text STALE, owed by CVO~Z.
- `safe-commit.sh` x2: LANDED.
- Gap: `audit-archive-invoker` prints INTEGRITY findings (NON-APPEND-EDIT on three logs, baselines missing). These
  are owned by the audit-archive lane and are not re-filed here.
