# IRPT 09-26 to 09-28: 40-plus never-widen halves, two /ui-walk briefs and a re-walk status log, three measured misses -- 4.0.0_SA_CRO

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, TRACE, SCRIBE
**Date:** 2026-09-26 22:38Z to 2026-09-28 14:1xZ. The window starts after `d3e5ac17e2`, the 09-26 log, and holds 55 commits
by this seat.
**Task Order:** ad-hoc (Andrew-direct at the 4.0.0_SA_CRO terminal), plus never-widen second halves asked by
2.0.0_SA_COO~P, ~M, ~Y and ~D and 1.0.0_SA_CTO.
**Status:** COMPLETE for every act asked. This is the reboot-checkpoint log (CTO 102350, Andrew-direct).

---

## Objective

1. **The standing role:** sign or refuse the second half of every IRPT served-output move (never-widen), each bound
   to a packet blob and measured against the BUILT artifact.
2. **Andrew's asks in the window:**
   - how many of the 49 (then 50) UI-review items ~D had done;
   - nudge ~D, the CTO and "the respective agents";
   - `/ui-walk` the Investor Reporting pages;
   - "go": re-walk the round-8 fixes;
   - a second, deeper walk across Performance, Holdings and Analysis, ending in "another cleanup brief on a slug of
     issues";
   - 09-28: check what was remediated from that list, and write a structured JSON-embedded status log.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-find` | FAIL (rail) | Once: the hook refused `comp-find --name` piped into a receiver. I switched to native Glob/Grep. |
| native `Grep` / `Glob` / `git grep` | PASS | Every repo search in the window (task orders, register ids, callers). |
| `# rail-checked` greps | PASS | Only on scratchpad extracts of S3 zips and tars, which are outside the repo corpus. |
| `.tools/aws` s3api / lambda / dynamodb (read) | PASS | Artifact downloads by VersionId; live CodeSha256 reads; the bd-securities census (full scan, 10,929 rows, auto-paginated, ScannedCount printed). |
| `docs/briefs/irpt-ui-review-coverage-check.py` | PASS | Cleanup brief 23/23 and status log 23/23. |
| `.claude/skills/ui-walk/walk.mjs` | PASS | Four walks, each self-armed and disarmed, with 0 guard aborts. |

- **What worked:** proving each half on the built bytes. I downloaded the zip or tar, ran a census against live, and
  imported the artifact's OWN modules to exercise the new path.
- **What failed:** rebuild 1 and rebuild 2 of irpt-status, both signed by this seat, failed live (see Decisions).
- **Gap found:** no tool checks a packet's cold-start smoke against the success path. The standard now lives in
  this seat's halves (@`49a9579720`).

## Work Completed

### 1. Never-widen halves (see the commit subjects for each)

- **COT:**
  - cash line: REFUSED (`9946616779`), then SIGNED on the re-cut (`f9e0bb6655`), with addenda 2-6;
  - one-use arms: plan 22f0a988 (`49a2ab81bd`), S157 (`6ae7ed831d`) and S157R (`342bf8baca`).
- **INF:** the Orion one-use arm (`9567a7c0fd`), with addenda 1-3. Two premises I inferred were withdrawn.
- **Walk windows 6-20:** each one word-diffed against the window before it. They carry the K1-CRED read-back rule
  (`2e44c56345`, from S172).
- **Export:**
  - reopen rule, async submit, async binding and client copy (`26cfc35706`);
  - render-grant KMS under the S3 Bucket Key (`b994f81153`);
  - RENDER_DELEGATE selection (`7f91727da1`);
  - receipt RUNNING per R11 (`4a28382f7a`, with an addendum in `49a9579720`).
- **Generate + resident:**
  - catalogue v2 and the Static-only tolerance (`035b0ab386`);
  - D2 re-sign (`0844092f92`);
  - the Comparison GRANT release (`e60a5043e8`).
- **irpt-status:**
  - rebuild 1 (`c20fe9034a`) and rebuild 2 (`85593bc122`, `da4b0bc76f`): both failed live;
  - rebuild 3 MINIMAL (`4bae7f9e7e`), signed with a success-path condition.
- **Others:** the cross-viewer title binding (`0cc18ec6e3`), the UIR-07 addendum (`df223d7453`) and the Performance
  as-of design-fork card (`d356e26684`).

### 2. UI verification and briefs (Andrew-direct)

- **`236fd94d73`, the 50-item register verified on local DEV 3f76cdb2:** 28 of 45 claimed items met, and 0 of 5 for
  IRPT_BCKEND. It added 7 UIW findings. The nudges went to ~D, the CTO, ~P, ~M and ~S. The message to ~S needed a
  cited task order (LD-0529).
- **Walker fixes:** the search step clears for real and ranks within its own listbox; `--deep` added (`97cb8bf734`).
- **`97cb8bf734`, the cleanup brief and register:** 23 findings, UIC-01..23. The CTO placed them in PRD v0.18
  @`5d44d0fa62`.
- **`f330857833`, the remediation status for 09-28** (`docs/briefs/irpt-ui-cleanup-status-20260928.md`, with the JSON
  embedded):
  - MET 3, PARTIAL 3, NOT MET 16, NOT OBSERVED 1;
  - NEW-01 (HIGH): an invested 49F account answers YTD -100%;
  - NEW-02: the COT 11-account pie no longer draws.

### 3. Surprise rows and record items

- DSGN_IRPTV1-S19 ARMED (`0b69c1cf16`): 34 committed walk PNGs carry client data. Andrew ordered the purge; MSTR is
  running it now.
- S173 (~M's): my view was added to the COT cash-line record (`d941f784ac`). The CTO then withdrew the bd-securities
  grant under an Andrew-direct that names etf-classifications as the canonical table (102309).

## Decisions Made

1. **Rebuild 1 miss:** I accepted "inert" from the function body, not from the built artifact. The rule since then:
   a cold-start smoke on the built zip, with a negative control.
2. **Rebuild 2 miss:** I accepted a before/after pair in which both reads were refusals. The rule since then: at
   least one read, or a smoke on the zip's own modules, reaches the success path and the internal-record path
   (`49a9579720`). Rebuild 3 carries that condition.
3. **Lazy calls:** a lazy call into a shared module (`served.DEFAULT_ACTION`, `_no_data`) is exercised by importing
   the artifact's own modules. A cold-start smoke cannot reach it.
4. **S173:** COT must not read firm-tagged attributes. The bound is a projection plus an attribute condition. This
   point carries to the etf-classifications read.
5. **UIC-09:** a worker's "already holds" is not a grade. The acceptance line is.

## Files Modified

See the commit messages for the 55 commits after `d3e5ac17e2`. The main ones: `f330857833`, `4bae7f9e7e`,
`e60a5043e8`, `d941f784ac`, `49a9579720`, `4a28382f7a` and `97cb8bf734`.
- All records are under `org/tier1_exec/4.0.0_SA_CRO/deliverables/NEVER_WIDEN_SIGNOFF_CRO_HALF_*`.
- The briefs are under `docs/briefs/irpt-ui-*`.
- Walk output is under `tmp/ui-walk/<stamp>/`. It is gitignored and never committed.

## Blockers

- **BLOCKED (push):** pushes are frozen under 0.0.0_AB_MSTR's S19 purge (102318, narrowed at 102336). Every commit in
  this window is LOCAL. Push state is unread at this writing; the next read comes after CLOSE.
- None other.

## Current State

- **Halves owed by this seat:** none. Signed and waiting on their operators' applies:
  - export receipt RUNNING (`c0b90ea2`; ledger `irpt-export-receipt-running-20260928`, D1/A1 open);
  - Comparison GRANT (`b6c264b3`; `irpt-generate-resident-grant-20260928`, D1/D2 open);
  - status rebuild 3 (`31fbdcbf`; `irpt-status-dates-rebuild3-20260928`, conditioned on ~Y's gate 4 and gate 3).
- **Live pins read here:**
  - irpt-status `bMMJ/bQ+5` (rolled back 00:36:31Z);
  - irpt-export-render `Ulim/gmf`;
  - irpt-ycharts-generate `ykJltfTd`.

  The new zips `O1Vu8CyD`, `BIEsyaNn` and `7Uz6kDd_` are already the LATEST S3 versions of their keys.
- **UI walker:** `opal-users-v2 USER#usr_opal_ui_walker` is disabled and its SSM parameter is ABSENT (read 13:54Z).
- **Inbox watcher:** monitor `bbdr0oaiu`, re-armed every 30 minutes.

## Next Steps

- [0.0.0_AB_MSTR] CLOSE of the purge. Then this seat runs `/handoff save`, leaves its worktree clean, and sends ONE
  READY-FOR-REBOOT line citing the log and handoff hashes (CTO 102350, step C).
- [2.0.0_SA_COO~P] after the reboot:
  - the three applies above, with the success-path reads this seat's halves name;
  - NEW-01 (YTD -100%), routed through [1.0.0_SA_CTO] (102354).
- [2.0.0_SA_COO~D] UIC-09 re-opened; NEW-02; round-9 task orders IV-e-70/72/74/75/77, all still pending.
- [2.0.0_SA_COO~M] the R4 Holdings enable half comes to this seat after the reboot. It covers UIC-15 and the INF name
  fill. UIC-16 is still unmerged on `irpt-m-uic16`.
