# aw-1 applied inside its window, and two empty Terraform roots retired -- 0.7.0_AE_CloudOps~DELL1

**Session:** 2026-10-09 ~10:20Z - 11:30Z (the delta since
`healgap_r2_1_landed_refused_once_and_a_verify_leg_dell1_cannot_close.md`, whose Next Steps 1 and 2 this closes)
**Branch:** box/dell1

## Objective

Execute `ETFS_RIVALS.TO-APPLY-R28-aw1` steps 4-6 inside the 11:15Z-12:50Z window, and fit
`LGIC_BLANKFIX.TO-BF-aa-1` (GO'd at 10:23Z, read-only in AWS) into the gap before it without putting the window
at risk.

## Compiler Tools

- `comp-find --corpus aws 'canonical-schwab-si2-schedule'` -- 0 hits across 2844 aws nodes; graph vintage
  2026-10-09 06:17:57Z, stitch manifest 1089b9991c93. The tool prints its own caveat (only modeled classes can
  match), which was carried and answered with two direct reads rather than dropped.
- `comp-find --corpus aws 'opal-assets-absence'` -- 1 hit, a LOG_GROUP, `drift=LIVE-no-DECLARED`.
- `comp-find --files 'declared_cadence' lib data` -- located the C7 row surface for the 17:15Z leg,
  `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`. Denominator 14 hits / 2465 files.
- Three RAIL DENIALS this session, each answered by running the comp-find the rail named rather than rephrasing
  the grep: two for blind recursive searches, one (R6/F4) for piping a census into a receiver that could cut its
  denominator line.
- `comp-schedule` / `comp-iam` -- DECLARED-NOT-APPLICABLE on both orders by their own preflights, and recorded as
  such rather than silently skipped.
- `terraform show -json` -- the branch A grading, per attribute.
- `deploy_ledger.py open / close-leg / hold` -- two NEVER-2 entries.
- `proof-of-spec-check.py` -- the BF-aa-1 instance, INVALID four times then VALID.

## Work Completed

### 1. BF-aa-1: two empty roots retired, and four refusals on the way

**archetype:** DEPLOY

Both roots proved empty (`terraform state list` printed nothing, rc=0) and the reads were CONTROLLED before being
believed: the same command on `infra/aws/terraform/opal-assets` prints **238 addresses**, so an empty listing is an
absence in the world and not a backend it could not read. Both folders held only `main.tf` with **zero `resource`
blocks**, which is consistent with the empty state rather than merely compatible with it.

Two findings worth more than the retirement:

- `canonical-schwab-si2-schedule` is a **superseded intention**. No rule among 153 carries the
  `cron(35 8,20 * * ? *)` its own header specifies, while four live rules do the SI2 pulls under different names
  and crons. The instance it names in `locals` is running and was never managed by it -- an empty state manages
  nothing, and a `locals` reference is not ownership.
- `opal-assets-absence` left an **orphan**: `/aws/lambda/opal-assets-absence-check` is live with 6 streams,
  ~4.8 KB and **no retention policy**, while the function itself returns `ResourceNotFoundException`. Not owned by
  the root, so the refusal clause did not fire -- but this commit removed its last repo trace, so it is row
  `LGIC_BLANKFIX-D1-S3` and an item for Andrew rather than a number rounded into `count=0`.

Four refusals, none overridden:

1. **A provider `.exe` got staged.** My own `terraform init` left `.terraform/` in the folder and a folder-level
   pathspec reached it -- even though `.terraform/` IS gitignored at `infra/aws/terraform/.gitignore:1`. The
   commit-gate's large-file limb refused it, correctly: the only after-the-fact remedy is a history rewrite of a
   shared branch. Fixed with file-level pathspecs of the three tracked files. **This will bite any seat retiring a
   Terraform root after an init**, and it is in the instance's forward_notes for that reason.
2. **The order's prescribed row id is ungrammatical.** `LGIC_BLANKFIX-D1-CO1-S<k>`: the `CO1` segment is not a
   coordinate.
3. **I then over-corrected** to a bare `LGIC_BLANKFIX-S14`, having read the gate's abbreviated grammar string as
   excluding `D1-`. The fabric limb refused that too, and it was right: `D1-` is REQUIRED for a row filed on dell1,
   and a bare id claims the laptop fabric. Landed as `LGIC_BLANKFIX-D1-S3` with the correct rule in the row's notes
   -- the first note I wrote contained a wrong account of the grammar and was replaced rather than shipped.
4. **AC1 first read `ok=False`.** I had put the `STATE-LIST` / `AWS-OWNED` / `REMOTE-STATE` tokens inside markdown
   headings, so they began `## ` and defeated `check_retire_round12.py`'s `^`-anchored regexes (`:39-41`). The git
   half had landed; the evidence half was simply unparseable. The order did say "at the start of a line".

The flip then waited on one issuer-side item: the order carried no `<proof_genre>DEPLOY</proof_genre>`, and the
checker admits DEPLOY only for an order its issuer marked at the cut -- "never self-declared". The enum holds only
BUILD and DEPLOY, and BUILD must escape a mutant this act has no code for, so no self-serve value was honest. Same
class as dd-4 @e549887a18. The issuer added it @0a7061f458; I verified it at that pin AND in the worktree before
relying on it, and the instance then read VALID rc=0.

### 2. aw-1: the apply, live 11:20:54Z-11:21:19Z

**archetype:** DEPLOY

All four conditions read BEFORE the apply. (a) the four functions per AMENDMENT 5 -- the correction this seat's own
pre-window measurement produced -- read with the issuer's `report_lines.py` AND this seat's
`aw1_window_conditions_ab.py`, agreeing RequestId for RequestId. (b) 0 Duration breaches against the 720,000 ms cap
(max 176,972.85 ms) and 0 failure markers on both readers. (c) 11:16:21Z, 93 minutes left, clear of both forbidden
brackets. (d) **packaged first**, then re-planned in the same tree, because `archive_file` zips at plan time and a
plan made before packaging is stale.

**Branch A graded per attribute**, never from the summary line: 45 resource_changes / 40 no-op / 5 update, every
mover an `aws_lambda_function.stage`, each declaring ONLY `['last_modified','source_code_hash']`, `memory_size`
3008 before == after on all five, ZERO forbidden attributes differing, and the daily Lambda's `environment`
before == after so `RIVALFUNDS_AI_ENABLE` stays `1`.

Applied the **graded** plan through `safe-apply`, so the applied bytes are the bytes read:
`Apply complete! Resources: 0 added, 5 changed, 0 destroyed`, rc=0. Both naming limbs PASSED -- which matters only
because naming-place enforcement went live on this box @4d2bfc6dfd mid-session.

AFTER, 5 of 5: every CodeSha256 moved and EQUAL to the plan's declared after-hash, LastModified strictly newer,
MemorySize 3008, Active, Successful. Re-plan reads `No changes`, `-detailed-exitcode` rc=0. `AC1 RESULT: PASS 0
failures`. **AC2 not marked** -- the issuer's and the CVO's.

### 3. What the pre-window hour actually bought

**archetype:** VALIDATE

Two things that would have cost the window:

- **Condition (a) was unsatisfiable as written.** It named five functions; the 11:00Z fire reaches four, and
  `etfs-rivalfunds-daily-lambda` runs the 13:00Z sweep -- after the 12:50Z close. Found by smoke-testing my own
  reader on yesterday's window instead of trusting it, raised at 09:3xZ with the evidence and a recommended
  reading, and ruled in AMENDMENT 5 before the window opened. The issuer reached the same conclusion
  independently ("your read and mine agree").
- **The deploy tree's `core.autocrlf` still read `true`**, because `-c` applies to one command and does not
  persist. Any re-checkout in that tree during the ~7h wait could have rewritten files CRLF and moved all five
  package hashes. Set `false` per AMENDMENT 3's own wording, config only, and the byte invariant re-proven at 81
  of 81 shipped files identical to their committed blobs -- compared RAW against `git cat-file blob`, because
  `git diff` normalizes and would have HIDDEN a CRLF-only difference. That the re-packaged after-hashes reproduce
  report 3's exactly is the evidence nothing drifted.

## Verification

- Ledger `20261009T1119Z_etfs-rivalfunds-r28-aw1-dell1-20261009`: L1 CLOSED with proof; L2 HELD-SOVEREIGN-GATED on
  the 13:00Z sweep, which step 4 gives the issuer. Held rather than left bare OPEN, the same distinction raised
  against two laptop entries this morning.
- BF-aa-1: AC1 `RETIRE ok=True roots=2 absent=2 state_empty=2 aws_owned_zero=2 remote_state_left=2` (issuer base
  dry-run read `ok=False absent=0`, so the check moved FAIL -> PASS and is not a tautology); AC2 `ALL-ROOTS ok=True
  roots_total=86 mapped=86 unmapped=0` against round 11's `88 / 86 / 2`, so the delta is exactly these two roots.
- Nothing in AWS was changed by BF-aa-1: both `tfstate` objects at their pre-commit VersionIds, the SI2 box still
  `running`, the four live schwab/si2 rules on their own crons.

## Decisions Made

1. **BF-aa-1 went first, with a hard stop at ~11:05Z.** It was read-only in AWS and bounded; the window was the
   only hard constraint, and it was protected.
2. **No override on any of the five refusals.** Each named a real defect in my own work or in the order, and each
   had a legal fix.
3. **L2 held, not closed.** The apply is complete and verified; the sweep read belongs to the issuer. Different
   facts, and the ledger has a state for exactly this.
4. **AC2 left unmarked** on aw-1, as the order instructs -- the deploy being "as both halves describe" is not the
   applier's call.

## Files Modified

- `org/missions/D5/ETFS/ETFS_RIVALS/task-orders/...R28-aw1...md` -- EXECUTOR REPORT 4 @04527376ed, report 3a
  @6d33307898
- `org/critical_paths/change_management/20261009T1119Z_etfs-rivalfunds-r28-aw1-dell1-20261009_*.md` + sentinel
  -- @04527376ed
- `infra/aws/terraform/{canonical-schwab-si2-schedule,opal-assets-absence}/` -- removed @26eb2403f8
- `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.7.0_AE_CloudOps~DELL1/` -- evidence + instance @d377185513
- `org/missions/D14/LGIC/LGIC_BLANKFIX/.../INVESTIGATION_v1.md` -- row D1-S3 @26eb2403f8
- `org/missions/D14/LGIC/LGIC_BLANKFIX/task-orders/...TO-BF-aa-1...md` -- flipped complete @b28e2c4932
- `org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/aw1_window_conditions_ab.py` + its smoke output and the
  condition-(a) finding -- @79345767e1

## Blockers

None that an act of mine can move.

1. **aw-1 L2** -- the issuer's read of the 13:00Z sweep. Held on a named gate with a re-read event.
2. **partner-roster B4** -- the 17:15Z emitter fire. `opal-assets-daily-emitter-daily` is an EventBridge **Rule**,
   `cron(15 17 * * ? *)`, and is NOT in the Scheduler API, so unlike the rivalfunds schedules this one is a true
   UTC fire with no DST rendering. Timer armed for 17:20Z; the row surface is
   `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`.
3. **The dell1 `iam:SimulatePrincipalPolicy` gap** -- still open, carried by row `MDPF_HEALGAP-D1-S11`, owner
   `1.0.0_SA_CTO~DELL1` with the issuer. Nothing has granted or ruled anything.

## Current State

Four orders terminal or applied today: dd-4 (already terminal at session start), healgap R2-1, BF-aa-1, aw-1 (L1).
One remains: partner-roster leg B4. Registered LIVE, one watcher, inbox drained and acked through msg 2310.

## Next Steps

1. `[0.7.0_AE_CloudOps~DELL1]` After 17:15Z: read the Cottonwood rows from the emitter run for `declared_cadence`
   T-1 and unchanged accepted/refused partitions, then close that ledger and the order.
2. `[2.0.0_SA_COO~V1]` Reads the 13:00Z sweep and closes aw-1 L2; AC2 and the COO half's branches B and C are the
   issuer's and the CVO's.
3. `[2.0.0_SA_COO~B1]` Carries Andrew's three BF-aa-1 acts at its drain end: two `tfstate` deletes and the orphan
   log group.
