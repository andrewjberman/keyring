# OPEN CALLS AT ANDREW — `2.0.0_SA_COO~Z` (5 calls, 2026-08-29 ~07:4xZ; cards 4-5 added ~08:1x-08:2xZ)

**Why this file exists and is not just a message:** the finding below was routed to
`1.0.0_SA_CTO~Z` + `0.0.0_AB_MSTR~Z` at 20260829T072xZ and lived ONLY in that message. Measured
tonight across three seats and three instruments: **a Msg-ID is per-recipient and resolves for
nobody but its holder**, and nothing indexes a message for `/open-calls` to find. A sovereign call
whose only carrier is an MCP send is a call that will not reach him.

⚠ **INTEREST DISCLOSED UP FRONT, because it colours cards 1 and 2:** my standing arm's
STOP-CONDITION is *"D1 + D4 read complete off the register."* **Closing these two projects moves my
own finish line.** That is exactly why I measured them and did NOT close them, and why the
recommendation is his to accept or refuse rather than mine to act on.

---

BLOCKING (nothing waits on the word operationally — but the register is wrong until it comes)

+-- CALL 1 of 5 ---------------------------------------------------------------+
  **`D1_NAMEDISCOVERY` is work-complete and register-open. Close it? (a) yes / (b) not yet.**
  All 3 TO faces read `COMPLETE — ROUND 1 ACCEPTED + CERTIFIED`; open TOs ZERO
  (`total=0, scanned=2172`, positive-controlled against `D1_CATVIEWS` -> `total=3`).
  -------------------------------------------------------------------------------
  **REC —** **(a) CLOSE.** Round 1 covered all 16 criterion-bearing decomp cells (the 4 boundary
  cells carry no criteria by declaration); the PRD's §8 exclusions are **refusals, not deferrals**;
  `blocking` reads *"Not blocked on any decision."* Round 1 was world-done on 08-27 — built,
  exercised, accepted, certified, pushed. ⛔ **I did not self-close because YOUR standing bar is
  unmet: *"I dont want to see comp-closure on the directives item until i smoke it and its
  DEFINITIVELY done."*** When I closed `ETFS_SATELLITES` (@`b8d7f50017`) both limbs were your own
  acts. Here neither is. **The close needs one smoke and one word, or (b) and I carry it.**
+-------------------------------------------------------------------------------+

+-- CALL 2 of 5 ---------------------------------------------------------------+
  **`ETFS_POSITIONING` is work-complete and register-open. Close it? (a) yes / (b) not yet.**
  All 9 TO faces terminal (complete / closed / superseded); open TOs ZERO, same control.
  Its round 2 was registered as its OWN project, `ETFS_INGEST` — so no round remains here.
  -------------------------------------------------------------------------------
  **REC —** **(a) CLOSE**, and this one is cleaner than call 1: the successor project is the
  explicit carrier of everything that follows, so closing this code loses nothing and strands
  nothing. Same bar, same reason I did not do it myself.
+-------------------------------------------------------------------------------+

CARRIED (answer whenever — nothing is blocked)

+-- CALL 3 of 5 ---------------------------------------------------------------+
  **The face-flip check: build it now, or does D1+D4 keep priority? (a) build / (b) hold.**
  YOU authorized it 2026-08-26 ~21:07Z (Card B) and routed it verbatim: *"the face-flip check
  enters Rule 27 as a build item — COO routes/seats it under the standing gates."* Spec exists
  (`0.4.0_DS_ClientPlatform~V/deliverables/FACE_FLIP_CHECK_SPEC_20260826.md`). **No tool, no TO.**
  -------------------------------------------------------------------------------
  **REC —** **(b) HOLD, and this card exists only because the fork is yours, not because I want it
  lifted.** Your 08-28 arm at this terminal is *"proceed through D1 and D4 TO completion. No
  distractions, pure execution"* — a record-lint is `D0`/`NFRA_TORECORD` class, so the later,
  narrower word governs and building it now would be me widening my own arm. ⚠ **But the cost of
  holding is real and measured:** the defect it detects — your words, *"the recorded state lying to
  the next dispatcher"* — has bitten at least three times since authorization, including **my own
  stale RESUME dispatch of the very `D1_NAMEDISCOVERY` TOs in call 1**, which
  `0.4.0_DS_ClientPlatform~Q` correctly refused to execute. ⚠ **And as specced it would NOT have
  caught calls 1–2:** it is TO-FACE level, and those TO faces are correct — it is the PROJECT
  STATUS that lies. **The project-level analogue is a gap in the spec, not a bug in it.**
+-------------------------------------------------------------------------------+

+-- CALL 4 of 5 ---------------------------------------------------------------+
  **Five UNTRACKED alarm/monitor `.tf` files sit in the estate's terraform trees, 1,008
  lines, declaring 7 CloudWatch metric alarms. Commit, delete, or apply? (a) delete /
  (b) commit as held drafts / (c) something else.**
  Your standing moratorium: *never build an alert/alarm/SNS/SES-send/notification/
  freshness-checker/monitor unless Andrew explicitly asks.* Surfaced by
  `0.7.0_AE_CloudOps~Z`; measured independently by this seat.
  -------------------------------------------------------------------------------
  **REC —** **(a) DELETE, unless you asked for one of them.** Measured, not relayed:
  `freshness_alarm.tf` 348 · `inf-gold-freshness-guard.tf` 252 · `tool_activity_freshness.tf`
  200 · `item2d_freeze_monitor.tf` 150 · `freshguard_derive_watchdog.tf` 58 — **all five
  UNTRACKED**, declaring **7 `aws_cloudwatch_metric_alarm`, 1 `aws_cloudwatch_log_metric_filter`,
  4 event rules, 3 lambdas.** ✅ **NOTHING IS DEPLOYED — untracked AND never applied**, so this is
  exposure, not a live violation. ⚠ **But 1,008 lines of moratorium-class infrastructure exists as
  files, and untracked files on this shared checkout are one `git clean` from gone and one
  `safe-apply` from live.** ⛔ **`0.7.0_AE_CloudOps~Z` refused to commit OR delete them and was
  right — either way is a decision, not a tidy.** **Whichever you pick closes it; no answer leaves
  1,008 unowned lines in the terraform trees.**
+-------------------------------------------------------------------------------+


+-- CALL 5 of 5 ---------------------------------------------------------------+
  **`ADVI_49F` P14-VEHICLE V14-1's last open leg is an exercise whose FAILURE MODE STOPS AN
  EC2 HOST. Authorize it? (a) run it / (b) hold.** This seat is `ADVI_49F`'s `coo_lane`, so
  the word would normally be mine — **but CLAUDE.md reserves stopping EC2 to HUMAN
  confirmation, and that reservation binds me too.**
  -------------------------------------------------------------------------------
  **REC —** **(a) RUN IT, at `0.7.0_AE_CloudOps~Z`'s convenience.** The leg (`L4`) requires
  *">=2 consecutive direct ssm send-command with StartedByDispatcher OMITTED; host still
  running read from INSTANCE STATE, never send rc"* — it exists to prove a halt-trap does
  **NOT** exist. ⭐ **The EXPECTED outcome is the host keeps running; the host stopping is the
  FAILURE result, and that is precisely what makes it a reserved act.** ✅ **Everything else on
  that deploy is proven: L1/L2 verify CLOSED, L3 git CLOSED on measured evidence
  (`a8907bf114`, on origin/CLOUD). Its sibling entry closed fully at 08:20Z, taking the
  ledger from 2 BYPASS to 1.** ⛔ **The remaining alarm is CORRECT and should keep firing
  until this word — `0.7.0_AE_CloudOps~Z` declined to mark it closed and was right.**
  ⚠ **If (b), it stays open and alarming indefinitely; there is no third state that is honest.**
+-------------------------------------------------------------------------------+

---

## The measurement behind calls 1 and 2, so it does not have to be re-derived

```
  MEMBERS re-resolved from org/missions/DIRECTIVES.yaml (DENOMINATOR: 12 directives)
    D1  D1_CATVIEWS      active  3 open TOs
        D1_NAMEDISCOVERY active  ZERO           <- CALL 1
    D4  ETFS_CANON       scoping DEFERRED, out of the completion set by your 08-24 word
        ETFS_POSITIONING active  ZERO           <- CALL 2
        ETFS_INGEST      active  2 open TOs
        ETFS_SATELLITES  complete
```

⛔ **HOW THIS WAS MISSED FOR MANY TICKS, stated because it is the more useful half:** the arm says
*"members re-resolved EACH TICK, never a pinned list."* **I restated that clause every tick and
checked faces for the two projects I resolved on the first one.** Quoting a re-resolution clause is
not re-resolving. The first attempt to fix it printed `D1: NOT FOUND / D4: NOT FOUND` — a regex
expecting `- NAME` bullets against a file using inline `projects: [A, B]` sequences — and **a failed
parse and an empty directive read identically**, which is precisely when the remembered list feels
like a safe fallback.

**What is NOT claimed here:** that no further work will ever touch these surfaces. A closed project
is re-opened or a new one is cut, and neither is contradicted by closing today.

---

**raised:** `2.0.0_SA_COO~Z` · **2026-08-29 ~07:4xZ** · **status: calls 1–2 at your next terminal;
cards 3–5 whenever — cards 4 and 5 are not mine to close either way.** D1 has 3 open faces (`D1_CATVIEWS`), D4 has 2 (`ETFS_INGEST`), all on the
13:30Z / 13:00Z scheduled fires — verified ENABLED on both EventBridge planes this session.
