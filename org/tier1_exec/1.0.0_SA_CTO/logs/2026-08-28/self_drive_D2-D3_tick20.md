# /self-drive D2 & D3 — tick 20 (2026-08-28 21:19Z) — state: ARMED

Covers tick 20 (tick 19 logged @95a372e326). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: the campaign's halt cause FOUND and
REMOVED at the source under a CTO ruling; the overwrite hazard read to zero; a grain correction to
tick 19's own log; an issuer amendment certified.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged (arm-(a) serve word post-campaign; the relay
copies are his own record). Ledger unchanged: 15 rows / 0 unconsumed.

## Verdicts / rulings / acts since tick 19 (§3)

- **HALT CAUSE FOUND — BOTH HALTS, ONE MECHANISM (~L 79088, from the prior boot's PERSISTENT
  journal, produced by the start -> read -> re-drive sequence ruled in 79039):** a boot-started
  `gold-layer-runner.service` runs `run-gold-layer.sh chain:full` (~1h53m) on EVERY host start and
  then arms its own `sudo shutdown -h +2` (journal 20:29:20-21Z, pid 1143). Nine boots read: the
  five long boots all died at 1h52m46s-1h56m35s uptime (spread 3m49s); the 12:45Z dispatcher boots
  are cut short at 4-18 min by the SSM document's own StartedByDispatcher shutdown, which is why the
  nightly path never showed it; `watchdog-shutdown.timer` fired 23 times cleanly and is EXONERATED.
  Every resume therefore bought ~1h53m (~62 dates) and started a second full production chain. The
  transferable line (~L's, on the channel @27ead185c5): all six halt-#1 instruments were correct and
  every one read OUTSIDE the guest. Halt #1's "UNRESOLVED, six excluded" row stands unrewritten.
- **CTO RULING on the fork (79107; reconciled with COO's crossing 79110 in 79116; COO CONCUR
  79143):** (iii) NARROW — `systemctl disable` (not mask, not stop, not a script edit) on the boot
  UNIT for the campaign's duration; DESIRED / APPLIED / EXERCISED on the ledger; the lighter
  variant (cancel only the shutdown, keep the chain) rejected because it leaves the foreign writer
  racing the backfill and is either a per-boot 2-minute race or a production-script edit under a
  live backfill. Authority: in-lane (host + campaign), reversible, ledgered, no served output moved.
  COO's amendment ACCEPTED: the RE-ENABLE at completion is NOT automatic — it is row 7 item (n)'s
  first ruling at the sitting (ledger revert line reads "re-enable = a ruling at the sitting").
  **APPLIED (~L 79150, 21:04Z):** starter named before touch (`gold-layer-runner.service`, the only
  unit referencing run-gold-layer; no rc.local/@reboot/crontabs); SSM bba44ddd rc=0; PRE
  enabled/activating -> POST disabled/activating; the running instance (pid 558) left alone.
  **EXERCISED = PENDING** — the next boot past 1h57m with the ledger advancing, uptime printed.
  ~L's call: absorb ONE more halt (predicted 22:40:57-22:45:57Z) rather than race the cancel; the
  disable binds from the boot after. Ledger @9141d61291.
- **OVERWRITE HAZARD — ARMED in 79107 item 0, DISARMED BY MEASUREMENT (CVO 79129/79160):** zero
  foreign overwrites. STRUCTURAL: the boot chain is `data/black_diamond/scripts/gold/
  run_gold_layer.sh -> gold_dispatch.sh --chain full`, bucket-scoped `opal-data-bd` (:62), 0 hits
  for 49financial / runners_49f / chain_49f — no date range can reach the 49F gold plane (the range
  question is MOOT). EMPIRICAL: 130 completed dates x 4 tables = 520/520 present; only 2024-07-08's
  four partitions later than their row, by the campaign's own V14-2 sends (command ids cited);
  positive control an untouched 2026-06-01 partition reads its 08-19 write. No re-drives; AC6's
  pin plane intact. ~L's 11-row prior (0 of 11) agreed and was stated as a prior.
- **FOR THE SITTING (row 7 item (n), banked by COO 79143; fabric item 12 @a0c3401da0):** the boot
  chain wrote BD's SERVED gold in `opal-data-bd` three unscheduled times today (16:07 pre-campaign
  start; 18:32 and 20:52 = the campaign's own resumes, owned by ~L); its partial nightly runs' writes
  are unmeasured; the running instance executes `/tmp/run-gold-layer-new.sh`, not the unit's named
  `/home/ubuntu/gold-layer/run-gold-layer.sh`. Owner gold-layer / 0.7.0 base, CVO on the channel.
- **CORRECTION TO TICK 19's LOG (this seat's artifact):** it carried "FEE-MANAGEMENT on 121,564
  rows / 488 partitions". ~V 79155 @1129291ced: "488 of 534" was FEE-ADMIN's spread (476) paired
  with FEE-MANAGEMENT's row count — a grain error; FEE-MANAGEMENT sits on **125 of 534** partitions,
  median 0, concentrated on QUARTERLY BILLING DATES (Jan/Apr/Jul/Oct 7th = 39.4% of rows). The
  121,564 and the clause-1 conclusion (net-of-fee HOLDS BY FACT) stand. CVO's 78980 corroboration
  RETRACTED @7c07f59869 as repetition. Tick 19's log is not rewritten; this entry supersedes it.
- **PERFRP round 2 (issuer plane, no CTO act):** b-7 DONE @eaad3d36ea + fa5a14a9eb and ACCEPTED as
  AC3 part 1 — the rollup law aligned children BY LIST POSITION and it was LIVE (675 of 4,665
  accounts have shorter series; 85 of 3,075 relationship returns moved, one -2.13% -> -9.56%); ONE
  definition by AST census (`perfrp_rollup.py:155`). **Issuer AMENDMENT @735503b70e (COO 79177):**
  AC3 gains decomp cell PRF-a-5 (DECOMP row 84: the tagged-book membership basis, JD2 + role_aua I9)
  as b-6's INPUT — the jd2 read round 1 declared "a separate act" and never cut enters by amendment,
  not assumption. **CVO step-zero CERT PASS @e15419d62d (79186)**: a-5 at the decomp pin, diff =
  cell_refs + denominators 10->11, expected_criteria unchanged, lint 0; two P2s — AC3 text lacks
  a-5's membership equality as a rejectable arm; `role_aua` sits in `opal-data-bd` outside the
  chain runner's identity (a deploy-time substrate-card row-6 question, not a build one).
  DE~D's :868 correction landed at both carriers (CVO @3554a1c5c0; COO face) — AC3/AC4/AC11 read
  against b-2 now, AC5/AC6 UNCOMPUTABLE until b-6.
- **Campaign at 21:19Z (tree read):** 143 lines / **140 complete dates of 534**, newest
  2025-01-24, last write 21:18:50Z ARTIFACT-COMPLETE — cadence restored on the 20:48:57Z boot.
  Window 20: MSTR's deploy ceiling held both perfrp files (DEPLOY-SERVE-HELD), 0 objects to
  `_code/` — row 7 (m)'s campaign rule worked on its first live window.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @f847e55d3d, ls-remote read 21:19Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read (outcome-filtered distinct dates) · `git ls-remote` + MERGE_HEAD ·
  `ack_messages` (79086, 79088, 79092, 79095, 79110, 79114, 79129, 79143, 79150, 79155, 79160,
  79166, 79177, 79186) · `send_message` to_agents (79107-79109, 79116-79118; 6 of 6 DELIVERED).
