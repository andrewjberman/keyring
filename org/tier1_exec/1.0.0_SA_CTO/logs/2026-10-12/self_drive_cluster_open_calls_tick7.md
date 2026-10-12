# SELF-DRIVE cluster open calls -- tick 7 (2026-10-12 17:50Z, by hand; the 17:41Z cron fire did not arrive) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Ticks covered: 7. Last committed
log: tick 6 @843970c375 (16:56Z). Substantive-delta log.

## Measurements

- open rows: 11 (sitez 6, dell1 1, dell2 4, laptop 0), closed 87, unchanged since tick 3 (read at tick 6, 16:56Z; no row added
  by any box since -- every call this hour arrived by relay, not by the list).
- inbox: 0 unread at write; 8 read and acked this hour (108620, 108621, 108626, 108628, 108632, 108636, 108638 and ~ANL's
  108623). Watcher re-armed twice (tasks ba1gdlkve, b0i950jx8).
- dell2: `3.0.0_SA_CVO` and `1.0.0_SA_CTO~DELL2` up on the fresh account (receipt 108626, Opus 5.5 high); five parked COOs (~C2,
  ~G2, ~V2, ~Y2, ~O2) ENDED by the tree kill, respawn from files on Oct 17 or Andrew's word; three rounds moving to L8/L10.
- `3.0.0_SA_CVO~L`: INTERRUPTED at its terminal after writing the v0.28 review (MSTR peek 17:33Z, msg 108636); a human act, held
  by MSTR, who asked Andrew whether the stop was his. The v0.28 SIGNED stamp sits uncommitted; status reads STALE.

## Calls since the last log

- RULED by the driver: 3 relayed asks. (1) dell2 D2-S27 + D2-S32 owners @374118e5cd: comp-iam -> this seat (fixed @7222a6a131,
  live get-role after an index miss); the safe-apply CROSSBOX limb -> NFRA_CTLPLN, COO~C round-12 cell, the limb stays WARN
  until the ancestry filter and path-match reads land. (2) dell2 D2-S76 + D2-W282-S3 owners @f22faeace4: both this seat, fixed
  @c00bd7dbe8 (round-close-check: a foreign lane's untagged order is named, not counted) and @b2b7488660 (trading_calendar
  fallback announces once on stderr). (3) MSTR's tree-kill finding placed: rows NFRA_CTLPLN-S9117 @9ffd2daac5 and S9118
  @aa354a9928 (kill-agent.ps1 Stop-ProcessTree and kill-maint.ps1 taskkill /T cross seat boundaries), ARMED; interim disarm at
  MSTR (dry first; no kill when a target's tree holds another serial's claude.exe) adopted on dell1, dell2, laptop, site Z
  pending; permanent cell at COO~C round 12.
- DESIGN FORKS at CRO research: 0. GOVERNANCE FORKS: 0.
- ACTS ONLY ANDREW CAN DO: 15 unchanged, plus one HOLD that is his by its nature, not a new act: lift or confirm the terminal
  interrupt on `3.0.0_SA_CVO~L` (MSTR's question to him, 17:3xZ).

## Driver acts since the last log

fc10 addendum 1 @843970c375 (tick 6); S9117/S9118 rows; S27/S32 ruling; comp-iam fix; S76/W282-S3 ruling + two fixes; COO~C told
(read only) which three rows the round-12 recut carries. Push state at write: box/laptop LOCAL through f22faeace4; origin reads
828908f761 (ls-remote 17:50Z); MSTR's box-sync carries it.

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `check_inbox`; `get_agent_status`; `.tools/commit-gate.sh`;
`python .tools/round-close-check.py --selftest`; `python -m pytest lib/tests/test_trading_calendar*.py`; `safe-commit.sh`.
