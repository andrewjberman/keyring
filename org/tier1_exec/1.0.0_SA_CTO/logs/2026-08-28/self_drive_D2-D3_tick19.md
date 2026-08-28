# /self-drive D2 & D3 — tick 19 (2026-08-28 20:52Z) — state: ARMED

Covers tick 19 (tick 18 logged @2241d71c35). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: campaign HALT-CLASS #2 with its
discriminator read live; a CTO ruling on the journal read; the first PERFRP emission's own author
falsifying two of its claims and closing a question this seat held; the deploy gate's
working-tree residual routed; DE~D's first act refuting the re-seat record's cited site.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 claims / D3 1, all
already members, 0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged: arm-(a) serve word (served output, NEVER#1/#3)
askable after the campaign completes and P1.5 re-grades; the two other copies of the struck relay
(his own "no recording of my word" — his word on other seats' inbox copies). Ledger unchanged:
15 rows / 0 unconsumed.

## Verdicts / rulings / acts since tick 18 (§3)

- **CAMPAIGN HALT-CLASS #2 (COO 79027, measured 20:39-20:42Z):** runner i-01003b035d2988dfb
  STOPPED with `StateReason.Code=Client.InstanceInitiatedShutdown`, CloudTrail StopInstances since
  20:00Z = NONE -> OS-initiated from inside the guest, the pre-registered discriminator read LIVE
  before any restart (credit COO). SSM b3c8285e (2025-01-06) InProgress from 20:28:52Z; ledger last
  complete row 2025-01-03. **CVO 79047 added the uptime signature: halt #1 died 1h51m22s after its
  LaunchTime, halt #2 1h56m03s — both inside a ~5-min band around 1h54m, both right after a Success
  row; the chain code has NO shutdown path (entrypoint 0 hits; the dispatch document's only
  `shutdown -h +2` sits under a StartedByDispatcher clause every campaign send omits) -> the actor
  is OUTSIDE the bundle (AMI-level cron/timer/idle watchdog, user-data, or a leftover of the
  nightly's own boot).** Candidates excluded for #2: API stop, the document's self-halt, the chain.
  Executor liveness read on the ledger itself: ~L wrote the 2025-01-06 row `ARTIFACT-INCOMPLETE`
  (ssm_status Cancelled, wall 1072.8 s) at 20:46:44Z — the (b) HALTED-resume path in motion.
  Tree at 20:52Z: 129 lines / 126 complete dates of 534 (+1 incomplete), uncommitted since
  @0bc0e8e588. Slack: two incidents (~34 + ~20 min) against ~3.5-3.8 h before the 12:45Z fallback;
  the finish re-derives from the ledger after the resume, never from a projection.
- **CTO RULING (79039/79040/79041, COO's ask):** the OS-journal read is taken NOW, at the resume —
  bundle item (d) discharged early; the DocumentVersion pin, the StateReason code-path change and
  the card scope stay at completion. Physical correction to the ask: a STOPPED instance cannot be
  read (SSM needs the guest), so the sequence is start -> read the PRIOR boot -> only then re-drive
  2025-01-06; the "window rolls at restart" premise is wrong in both branches (persistent journald
  survives on EBS; volatile was destroyed at the stop) — what the restart costs is churn, hence
  read before the re-drive. Read set: journald branch first (`/var/log/journal` present?),
  `--list-boots` (both boot ids), `-b -1` tail, logind/ssm-agent units, `last -x`, `/var/log/
  messages` 20:28-20:40Z; timer census (crontab both users, cron.d, `list-timers --all`, atq,
  IMDSv2 user-data); halt row in the ruled vocabulary BEFORE the resume send.
- **PRF-b-3 / AC2 BUILT + QA-EMITTED (DS~V 79024 @1fa9d927e0; COO ACCEPT 79030):** `_allocation`
  took `level` and never used it (both grains byte-identical firm-wide) -> per-key at grain,
  allocation_of_level AND allocation_of_total, identity at emit on unrounded sums; ties to the RAW
  positions partition at 1,793,416,380.56 exactly; residue kept as TWO states (UNCLASSIFIED-LOUD =
  verdict, NO-CLASSIFICATION-ROW = coverage gap). Residue 15.0103% at as-of 2024-11-07 vs 2.2881%
  at 2026-08-27, and the SPLIT discriminates (coverage-gap state 14.04% -> 1.37%, verdict state
  flat) = a vintage-less classification table, a declared property now measured; recorded by the
  issuer, not fixed. **TWO SELF-FALSIFICATIONS by ~V, both with the method stated:** (1) the fee
  census — 534 of 534 partitions, 3,027,497 rows: FEE-MANAGEMENT on 121,564 rows / 488 partitions;
  on 2024-07-25 r_net == r_gross on 0 of 3,089 fee-bearing accounts (max gap 0.9672) -> **the
  question this seat held (78990) is CLOSED: PRF-inv-6 clause 1 "served return = net-of-fee TWR"
  HOLDS BY FACT, non-vacuously; no contract change; nothing to Andrew.** The two "net == gross in
  both vintages" reads sampled 2024-11-07 and 2025-06-02 — two of the 46 fee-free partitions — and
  CVO's 78980 confirmation re-read the same two dates: repetition, not corroboration (the CLAUDE.md
  §22 clause firing on a live pair; the fix was a denominator, not a sharper tool). (2) b-2's SI
  window demanded the plane's first day, which cannot carry a return (no prior-day BMV; the
  contract floors twr_daily at 2024-07-09), so expected 88 vs max 87 and COMPUTED was unreachable
  for all 4,665 -> re-emitted with `return_series_start` beside `window_start`: COMPUTED 3,381 /
  PARTIAL 689 / INPUTS_PRESENT 586 / INPUTS_ABSENT 9, plus a REACHABILITY arm. AC1 stays accepted
  with the defect on its record; the corrected re-emission is the next leaf before b-7/b-6.
- **DEPLOY GATE UPLOADS WORKING-TREE BYTES (CVO 79020, fabric item 11 @f6c92ea9d5; MSTR 79009's
  window-20 hold was the disarm):** `.tools/safe_deploy_core.py:545-566` md5s the working path,
  uploads it, and compares the ETag to the SAME working md5 — a mid-edit file self-certifies.
  Campaign residual CVO measured: every send syncs `_code/` onto the runner and the per-date chain
  runs `_run_perfrp_projection` (`chain_49f_entrypoint.py:322`) from it, so an uncommitted
  `runners_49f/` file executes inside the live backfill on its next date (a broken import =
  `CHAIN ABORT stage=perfrp_projection rc=2`). Disarm = the integrator's porcelain check on
  `runners_49f/` before every push for the campaign's DURATION; lane half = commit-or-stash.
  **CTO act (79042/79043/79044): routed to COO as obligations row 7 item (m)** with the text
  supplied — same class as (k) ("a working tree is not atomic; gates read a cited commit"), owner
  0.8.0_AE_CloudComp / DT at the sitting; remedy shape = deploy from `git show <ref>:<path>` or
  REFUSE on dirty. No gate manufactured.
- **DE~D FIRST ACT on TO-R1-DE (79050, portal HEAD 9957410e47, every citation at a commit):**
  proximate cause CONFIRMED in kind (no payload reaches the consumer; the leaves constant gates only
  gain_loss, 1 of 5) and **REFUTED AT GRAIN: `AdvisorBookView.tsx:868` is `PerfrpBookView` = the
  Book face = AC5 only; the L3/L4 grids are `PerfrpCardGrid` at :552/:617 and pass NO `payloads`
  prop at all** (optional, plural, `?? null` at :222). A `payload=` token census was true as a
  string census and could not see an OMITTED prop — a presence instrument cannot see an absence;
  the same sentence sits on three carriers (STEP0 :127, TO-R2-DS face :80, the re-seat record :51
  — CVO 78823 / my 78805) by inheritance. Consequence: an edit at :868 leaves L3/L4 unchanged;
  AC3/AC4 edit at :552/:617. Scope: AC3 + AC4 + L3/L4 of AC11 readable against b-2 NOW; AC5/AC6
  are genuine producer waits on b-6 (not emitted; carrier listed 7 of 7). Vintage re-measured:
  the on-disk pair is @1fa9d927e0 (relationship grain 2,279 / 316 / 474 / 6). OBSERVATION/INERT.
  **The re-seat record I co-signed carries the wrong site; correction is the issuer's (COO) at the
  face — noted here, not edited from this lane.**
- Also queued from tick 18's tail (acked, no act at this seat): COO 79002 routing of ~D's
  `test_pipescript_digest` RED to 0.8.0 at the sitting; CTO~D 78995 Rule 21 T1 (law @9ed33c473e,
  mechanism @32d5967277); exec-sum re-shape landed @e629f07a6f on Andrew's word.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope (arm-(a) becomes askable post-campaign; the relay copies are his own record).

state: ARMED · push state of this log: LOCAL (origin/CLOUD @2afd4ddd4e, ls-remote read 20:49Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs (prds[] dict-or-string) ·
  verdict ledger read (15 CRLF rows) · campaign ledger tree read (python, distinct dates +
  outcome of the last row) + `git log -1`/porcelain on it · `git ls-remote` + MERGE_HEAD ·
  `ack_messages` (79002, 79020, 79024, 79027, 79030, 79047, 79050) · `send_message` to_agents
  (79039-79044, 6 of 6 DELIVERED).
