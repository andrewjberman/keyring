# 0.8.0_AE_CloudComp~Z -- NFRA_GRAPHFEED.W1 day one: TO-1 staged-to-apply, TO-3 LANDED+registered, TO-6 dispositioned, and the stranded-grant find that saved tonight's derive

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, COORDINATE, VALIDATE

---

## Summary (window: ~18:47Z -> ~21:2xZ; fresh session on the LD-0299 Andrew-direct GO)

Fresh ~Z session, wave NFRA_GRAPHFEED.W1 (6 TOs, Andrew: "Start with 1) ... proceed through all
6"). Day-one state: **TO-1 built-to-gate + CTO-ruled + staged on 0.7.0's apply batch** (maiden
03:30Z fire tonight IF 0.7.0 revives + tonight reads clean, else tomorrow); **TO-2 half-banked**
(flip verified APPLIED live; AFTER-verify time-gated to tomorrow ~04:05Z); **TO-3 comp-axes
LANDED end-to-end** (tool + registration + invariant PASS + routing rank-1 + frozen baseline
PASS; one AC open: the >=24h second snapshot row); **TO-6 (a)(b) dispositioned + fixed, (c)
facts sent**; TO-4 re-framed REVIEW-FIRST by an Andrew-direct (recorded verbatim + broadcast
same turn); TO-5 awaiting COO re-staff. **Plus the find of the day: tonight's 02:00Z derive fire
would have been DENIED** -- CTO's codeheat apply left the events-role RunTask grant on task-def
rev :4 while the live target fires :5; measured with isolated simulates (deny on :5, positive
control allowed on :4, SEPARATE invocations), escalated URGENT with ~6h runway; CTO accepted
whole + GO'd 0.7.0 same turn; COO deadline-tracked w/ 23:00Z backstop.

## Work completed

### TO-1 (standing CSE emitters) -- BUILT TO GATE, APPLY-STAGED
- Design doc (file:line-grounded): deliverables/NFRA_GRAPHFEED_TO1_CSE_EMITTERS_DESIGN_20260715.md.
  Root causes measured: cse_producer.tf is a never-built forward reference (cse_store.py:35);
  the marker's cse row is ERASED hourly by incremental_updater's 3-table stamp through
  _stamp_unconditional's wholesale replace (_provenance.py:242-268, measured 07-10); the writer
  has NO event_id dedup (cse_store.py:357-404) so idempotency had to be built as a filter layer.
- NEW infra/aws/globgrph/cse_producers_nightly.py (@ b0412f3d3): dedup-spine orchestrator --
  first graph_head fire IS the ~55k backfill, re-run adds 0 (AC-3 native); per-leg isolation;
  env-gated legs; AC-4 snapshot guard; TWIN_HEARTBEAT (last_run.json every run / last_append.json
  on landed rows). Self-test 8/8. Dockerfile +3 COPY-only lines. incremental_updater tuple 3->4
  (TO-1(c)); zip rebuilt (delta stated exactly: + current _provenance.py, CAS dormant).
- CTO RULINGS x3 (193201Z): 03:30Z APPROVED w/ two OPAL_STNDRD binds -- (a) EventBridge
  SCHEDULER not classic rule ({unit}-{function}-{cadence} grammar) -> aws_scheduler_schedule
  globgrph-cse-producer-nightly; (b) ABSENCE-CHECK TWIN -> 2 freshness_alarm.tf registry entries
  (last_run 26h dead-task mode; last_append 30h fires-but-lands-nothing mode; breach-until-first-
  fire disclosed-expected). OPTION B2 ratified (dedicated task role: warehouse RW mirror + audit/*
  read-only w/ prefix-conditioned ListBucket). Marker leg approved-to-gate (CAS dormancy to be
  SHOWN at evidence). TF @ 9369f7451; terraform validate PASS; plan 11/5/0 -- MINE=13 targeted
  (10 creates + 3 consequence-changes), 3 not-mine excluded.
- AMENDMENT (203412Z): apply TOMORROW -> TONIGHT post-clear (conditional); then 0.7.0 base killed
  by Andrew (CPU-save) -> tonight-apply conditional on their ~22:15Z revival, else reverts.
  Rebuild+apply payload staged to 0.7.0 (203658Z): exact COPY sources, 13-resource set, zip
  upload prereq, exclusions.

### THE URGENT FIND (during plan-drift classification)
- Live primitives: rule target fires globgrph-derive-runner:5; the ONLY policy on
  opal-globgrph-derive-runner-events grants RunTask on :4. simulate-principal-policy: :5
  implicitDeny / :4 allowed (one --resource-arns per call, positive control its OWN invocation).
  NEVER#5 stranded-leg class on CTO's codeheat apply. Escalated 194522Z (CTO) + 194545Z (COO
  record). CTO: "FINDING ACCEPTED whole... GO went to 0.7.0 same turn"; revision-closure lesson
  queued for STNDRD's TF protocol doc.

### TO-2 (codeheat flip verify) -- BEFORE banked, flip APPLIED
- BEFORE: comp-learns-status DATA VINTAGE 2026-07-08T18:45:51Z (BEHIND, binding=code_heat,
  lag=153.3h). APPLIED truth: derive task-def rev 5 carries GLOBGRPH_CODEHEAT_ENABLED=1 (live
  describe-task-definition). AFTER rides tomorrow's 02:00Z derive + 04:00Z comp_learns -- which
  itself depended on the grant fix above.

### TO-3 (comp-axes) -- LANDED + REGISTERED (@ c44200273)
- .tools/comp-axes: 8-axis DIRECTORY (per-row = the READER'S OWN vintage + top-3 + drill),
  append-only SNAPSHOT history (org/modules/graph/axes_history.jsonl + per-run S3 mirror
  warehouse/axes_history/rows/), per-axis DELTA (--since baselining). Honest-degrade: debt
  renders ABSENT (comp-debt designed, NFRA_COMPDEBT_PRD, but NO landed executable -- wave
  finding); self-test 8/8. EXERCISED LIVE x2 + delta exercised (nonzero on 7 axes, catching
  real estate motion). Live run 2 caught its own bug class: bare 'bash' from python subprocess
  = the System32 WSL relay (execvpe /bin/bash fails) -> _git_bash() explicit resolution +
  stderr-surfaced failure notes + rc checks.
- Registration (COMPCLOSE): manifest entries + tools_index + comp-tools.yaml + coverage-map +
  comp-which curated rule. comp-manifest-check completeness PASS (72 executables / tools_index
  58 / coverage-map 75). comp-which routes "estate overview by axis" + "what got hotter since
  last week" to comp-axes RANK-1; frozen routing baseline PASS (zero pollution, 100% gibberish
  abstention). Owned-paths ANY_EXEC lane override AUDITED citing the LD-0299 delegation.
- AC OPEN: two runs >=24h apart (second dated row lands tomorrow).

### TO-4 -- ANDREW-DIRECT re-frame (recorded + broadcast same turn)
- Verbatim record: deliverables/ANDREW_DIRECT_20260715_TO4_compwhich_review_first.md; broadcast
  COO 210859Z + CTO 210912Z + MSTR 210916Z. TO-4 opens with a current-state review; any touch to
  comp-which's description/top-k surface contingent on a measured gap.

### TO-6 (hygiene) -- (a) FIXED, (b) DISPOSITIONED, (c) SENT (@ 9ccf9fe70)
- (a) rc=2 RCA: the fallback is the DESIGNED daily ground-truth reset (CTO condition 2,
  _canonical.py:360-364; gate at kuzu_incremental_refresh.py:174-176); canonical DB built
  18:16:32Z inside MSTR's assessment window = their query paid the designed rebuild. Defect was
  the log line; fix = classification at the call site (designed-reset vs cold-start vs
  error-investigate). "Make incremental succeed" on that path REFUSED (would remove the reset).
- (b) graph_contracts 698.4h = STATIC-BY-DESIGN (derive_runner.py:196-206 CVO-authors-on-ratify;
  _provenance cadence dict deliberately omits it). No fix.
- (c) NFRA_MSGRAPH.json current-state facts to COO 211758Z (S2 live+guarded, 5,520 MS nodes,
  one-site-one-library by decision, S3 GO-condition met, C3 not built).

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-glob | cse_emit_*, Dockerfile*, *incremental*, *.tf, comp-*debt*, routing-test, coverage-map | PASS | located every substrate file; the debt NO-MATCH carried the honest 0-hits caveat |
| comp-grep | stamp_branch_head_marker/MARKER_TABLES, incremental_updater, bootstrap, scheduler precedents, comp-debt, graph_contracts | PASS | THE load-bearing calls: found the marker-erase mechanism + the never-built cse_producer.tf forward reference + the scheduler house shape |
| comp-fedobs | (bare) | PASS | TO-1 BEFORE state: cse_log_total=342, served vintage 04:30:38Z |
| comp-learns-status | (bare) | PASS | TO-2 BEFORE state: BEHIND binding=code_heat lag=153.3h |
| comp-kuzu | count query | PASS | pin==HEAD; built 18:16:32Z (the TO-6a evidence); header names incremental_updater as the cse non-stamper (TO-1c corroboration) |
| comp-which | axis-shaped questions x2 | PASS | comp-axes rank-1 both; the AC routing proof |
| comp-axes (NEW) | --self-test, directory x2, delta | PASS | 8/8 self-test; live x2; delta nonzero on 7 axes |
| comp-manifest-check | completeness x2 | PASS | pre: 71 accounted; post-commit: 72 accounted, comp-axes registered |
| comp-which-routing-test.py | full run | PASS | zero pollution, 100% gibberish abstention -- frozen baseline intact after the curated-rule add |
| commit-gate.sh | 5 files across 4 commits | PASS | caught the walrus-in-comprehension AST class in comp-axes (fixed) |
| terraform validate + plan -lock=false | globgrph module | PASS | 11/5/0; drift classification produced the URGENT find |
| aws (operational) | describe-task-definition, list-targets-by-rule, get-role-policy, list-role-policies, simulate-principal-policy x2 | PASS | the 22a battery: deny on :5, positive control on :4 in ISOLATED invocations |
| (raw greps) | rail-checked markers carried x6 | PASS | single-known-file API/shebang/flag lookups; registry-file shape reads |

**Gaps found:** (1) comp-debt: designed (NFRA_COMPDEBT_PRD) but NO landed executable -- comp-axes
carries it as an honest ABSENT row; routed in the TO-3/TO-6 close. (2) The WSL-relay bash
resolution class for python-subprocess tool wrappers -- fixed in comp-axes (_git_bash()); other
python callers of bash-shebang comp tools may share it (candidate sweep).

## MCP traffic

IN: MSTR GO (recovered at startup) - CTO RULINGS x3 (193201Z) - CTO URGENT-ACCEPTED + plan-shape
ACCEPTED (195107Z) - COO deadline-track ACK (194646Z) - CTO apply-amendment (203412Z) - CTO
0.7.0-down heads-up (205850Z) - 0.7.0~Z STNDRD registry coordination ask (193111Z).
OUT: MSTR wave ACK (185117Z) - CTO design RAVC (190814Z) - 0.7.0 staged rebuild heads-up
(190820Z) - 0.7.0~Z registry answer + trigger-map ask (193203Z) - URGENT stranded-grant to CTO
(194522Z) + COO record (194545Z) - 0.7.0 rebuild+apply payload (203658Z) - ANDREW-DIRECT
broadcast x3 (2109xxZ) - COO TO-6(c) facts (211758Z). Heartbeats throughout.

## Blockers

NONE hard. Gated/waiting: TO-1 apply rides 0.7.0 revival (~22:15Z Andrew call) else tomorrow;
TO-2 AFTER-verify = tomorrow ~04:05Z artifacts; TO-3 second snapshot row = tomorrow; TO-5 = COO
re-staff record; TO-4 = review-first, next in sequence.

## Next steps

1. **[event]** 0.7.0 revival -> tonight-apply (their lane) -> my first-fire + re-fire evidence
   pack (CAS dormancy SHOWN, SAFE_TOOLS enumeration, B2 negative control on the LANDED role,
   audit-read allowlist for CTO review). Else same pack on tomorrow's apply.
2. **[tomorrow ~04:05Z]** TO-2 AFTER verify (code_heat vintage <30h + BEHIND flag gone) --
   report the before/after pair. TO-3 second snapshot row + >=24h delta AC.
3. **[me, next in sequence]** TO-4 REVIEW-FIRST per the Andrew-direct: current top-3+rank-file
   state vs the COMPASSURANCE top-5 directive + the zero-result rate re-measure (full tally,
   denominator printed). Touch nothing absent a measured gap.
4. **[COO]** TO-5 re-staff record; TO-6(c) registry refresh confirmation.
