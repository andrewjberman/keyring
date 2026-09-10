# NFRA_IAMROLES202609.TO-IAM-t-2 -- EXERCISE the permission-grain usage instrument, over a stated population and lookback

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R3.md</decomp_doc>
<owned_cells>IAM-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~8</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-2; the round-2 analysis calls this R3-B)

```
IAM-t-2. ACT: EXERCISE the permission-grain usage instrument across a stated role population over a
stated lookback, and NAME the unused permissions per role.

FWD-2's bar, verbatim: "real roles have been read and their unused permissions named, over a stated
lookback". Its DONE WHEN state is EXERCISED.

⛔⛔ THIS IS NOT A BUILD CELL AND IT IS NOT AN EXTEND CELL. THE INSTRUMENT ALREADY EXISTS AND ALREADY
ANSWERS THE PERMISSION AXIS. Measured at HEAD before this order was cut:

    .tools/comp-iam-usage permission-cold --role <ROLE> [--lookback DAYS] [--json]
      "PERMISSION grain: which of a role's GRANTED permissions were never used over a stated
       lookback (IAM Access Advisor ACTION_LEVEL, NOT Access Analyzer)"

    Its `self-test` passes and NAMES THIS OUTCOME BY NAME:
      "'unused over the stated lookback', FWD-2's own phrasing, not a claim the action was never
       called at any point in the account's history"
    and asserts, in its own words, that unobservable != never-used.

⛔ SO DO NOT WRITE A NEW TOOL, DO NOT FORK THIS ONE, AND DO NOT "IMPROVE" IT AS YOUR DELIVERABLE.
C-EXTEND-NOT-BUILD, and the build ladder puts "the estate already has it" ABOVE "extend". Round 1
BUILT this instrument and produced NO usage result; the gap this cell closes is EXERCISE, not
construction. If you find the tool genuinely cannot answer for some role, that is a FINDING and a
surprise ROW -- not a licence to rebuild it.

WHAT TO PRODUCE, at
    .../deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md

  (a) A STATED POPULATION with its DENOMINATOR. Which roles did you run against, how were they
      chosen, how many were attempted, and how many returned. "Real roles" is plural and the
      selection rule must be stated -- an unstated selection is a filtered census that confirms
      whatever it was filtered for.

  (b) A STATED LOOKBACK, in days, as a number, appearing in the deliverable. The tool defaults to 90;
      whatever you use, say it.

  (c) PER ROLE: the granted permissions the instrument reports as NEVER USED over that lookback.

  (d) ⛔ UNOBSERVABLE KEPT SEPARATE FROM NEVER-USED, as its own count. A service AWS does not track
      at action grain, or an action absent from AWS's own tracked-action list, renders UNOBSERVABLE --
      and unobservable is NOT clean. This is FWD-7's discipline one grain over and the tool already
      carries it; your deliverable must not collapse the two.

  (e) THE INSTRUMENT'S OWN LIMITS, quoted. `comp-iam-usage limits` prints a Rule-22a fix-or-carry
      statement naming three limits. Quote it and say which of them bound YOUR run.
```

## DEPENDENCIES

**NONE.** No cell of this round precedes it. **Six of the eight outcomes are downstream of this one
cell** -- FWD-1's posture number is a rollup of it and FWD-7's vocabulary is a rendering of it -- which
is why it is cut now and why FWD-5 and FWD-8 are deliberately NOT cut this round.

## BOUNDS -- what this cell may not cross

```
⛔ C-NO-ACCESSDENIED (D5): NAMING an unused permission is not REMOVING it. This cell narrows nothing,
detaches nothing, applies nothing, and changes no policy, role or state. It REPORTS.

⛔ C-TWO-REMEDIES: this is the PERMISSIONS axis. Do not touch the governance disposition document, do
not assign an owner, and do not read a permissions finding as a governance answer.

⛔ C-ANALYZER-PRICED-FIRST + G-25: NO AWS ACCESS ANALYZER, not even to compare. permission-cold uses
IAM Access Advisor and says so. Pricing Access Analyzer is a VENDOR call RESERVED TO ANDREW and this
order does not and cannot authorise it.

⛔ AWS READS ONLY. get-role, list-role-policies, list-attached-role-policies, Access Advisor via the
tool. Anything that CHANGES AWS is out of this cell.

⛔ DO NOT MINT ANY ALERT, ALARM, MONITOR, SCHEDULE OR NOTIFICATION (G-21, ARMED, 25 gates). A
"freshness checker" or a recurring usage report is exactly what that moratorium forbids.

⚠ BOUND EVERY AWS READ. Each invocation runs under `timeout 120` and A TIMEOUT IS RECORDED AS THE
OUTPUT -- an unbounded sweep does not fail loudly, it produces a criterion whose evidence is the word
"timeout". Iterate role by role with a stated cap rather than sweeping the estate in one call.

⚠ A ROLE THE INSTRUMENT CANNOT SEE MUST NOT READ AS CLEAN. If a role returns nothing, say whether
that is "no unused permissions" or "no observation", and count them separately.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam-usage    BUILT, TRACKED, SELF-TESTING at HEAD. Subcommands: role-cold, who-can-reach,
                  reach-check, permission-cold, limits, self-test. Round 1's instrument-build cell
                  produced org/modules/graph/comp_iam_usage.py and .tools/comp-iam-usage and NO usage
                  result -- the instrument has never been exercised at population scale.

comp-iam (round-3 vintage, RUN as `bash .tools/comp-iam stats` FROM A CLEAN WORKTREE at f20bc65d71):
                  191 TF roles / 188 services / 1084 operations / 304 permission gaps.
                  ⛔ THE INVOCATION FORM IS PART OF THE FIGURE -- the bare name resolves through a
                  ~/bin forwarder to the MAIN checkout and reports 195, four of which are declarations
                  in untracked files that are in no commit. Use `bash .tools/comp-iam` from your own
                  worktree and state the form beside any number you quote.
                  ⚠ 304 gaps is a FLOOR on the DESIRED plane: wafv2:UNMODELED and UNMAPPED-METHOD
                  persist. Its NOTEs on reused role labels silently mis-linking inline policies
                  pre-fix are a reason to trust the ACCESS-plane read over a source parse here.

comp-find --corpus aws (vintage 2026-09-10 12:24:50 UTC): 219 IAM_ROLE nodes live, DECLARED=203.
                  219 is the LIVE role population and is the honest ceiling for "real roles"; the 191
                  is a Terraform-source count and the two are DIFFERENT POPULATIONS, not two readings
                  of one. Round 2 established that distinction and it binds your denominator.

comp-schedule (round-3 vintage, RUN to completion, 5 of 5 carriers, 13.5 s): GATES ARMED 25. G-21 and
                  G-25 bind this cell and are in BOUNDS.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/
org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R3.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/ledger/ROUND_ANALYSIS.round2.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-t-2.exercise-the-permission-grain-usage-instrument.md
</paths>

Your deliverable goes in `deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/`, inside the granted prefix.
`.tools/` is NOT in your write surface and MUST NOT BE MODIFIED -- you run the instrument, you do not
change it. AWS reads are operational and are not path-gated.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.
Your surprise row id is `NFRA_IAMROLES202609-Z-W8-S<k>`, `"fabric": "site-z"`. A BLOCKING row is read by the COO in your final report; an OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-t-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md && grep -c -i -E 'permission-cold' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md</invocation><expect>a count of 1 or greater -- the existing instrument was the one exercised and is cited by name; NO OUTPUT AT ALL means the deliverable is missing and the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-t-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md && grep -c -i -E 'lookback' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md</invocation><expect>a count of 1 or greater -- the lookback is STATED, which is half of FWD-2's bar in its own words; NO OUTPUT AT ALL means the deliverable is missing</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-t-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md && grep -c -i -E 'denominator' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md</invocation><expect>a count of 1 or greater -- the population carries its denominator: how many roles were attempted and how many returned, printed rather than implied</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-t-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md && grep -c -i -E 'unobservable' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md</invocation><expect>a count of 1 or greater -- unobservable is kept apart from never-used, which is the one distinction that decides whether this deliverable is honest; a role the instrument cannot see must not read as clean</expect></criterion>
  <criterion id="AC5" cell_refs="IAM-t-2"><invocation>test -f org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md && grep -c -i -E 'access.analyzer|put-role-policy|delete-role|detach-role-policy|terraform apply|safe-apply' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/PERMISSION_USAGE_EXERCISE.md</invocation><expect>a count of 0, printed -- NEGATIVE: no Access Analyzer was reached for (C-ANALYZER-PRICED-FIRST, a vendor call reserved to Andrew) and nothing was narrowed, detached or applied (C-NO-ACCESSDENIED). Naming an unused permission is not removing it</expect></criterion>
  <criterion id="AC6" cell_refs="IAM-t-2"><invocation>git hash-object .tools/comp-iam-usage org/modules/graph/comp_iam_usage.py</invocation><expect>exactly two lines, 5c7f03ba3702d5de5c0edf7a955a72dd20e596f5 then 8670fc5025694c942f8a7c725a19e2317cf63c20 -- NEGATIVE and structural: the instrument's BYTES are unchanged from the cut. A CONTENT PIN is used here deliberately rather than a git diff, because a diff against HEAD reads clean once a change has been committed and would pass whether or not the tool was rewritten; a blob hash cannot be satisfied by committing. Verified at the cut that appending one line moves the first hash to bcf2805c13, so the pin discriminates</expect></criterion>
  <criterion id="AC7" cell_refs="IAM-t-2" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the EXISTING instrument is what was exercised, cited by name.
- **AC2** (mechanical): the lookback is stated -- FWD-2's bar says "over a stated lookback" in terms.
- **AC3** (mechanical): the population carries its denominator rather than a bare list.
- **AC4** (mechanical): unobservable is kept apart from never-used. The single most load-bearing line in the deliverable.
- **AC5** (mechanical, NEGATIVE): no Access Analyzer, no mutation. Two constraints, one census, both about what must NOT appear.
- **AC6** (mechanical, NEGATIVE and STRUCTURAL): the tool was run, not rewritten -- pinned by BLOB HASH rather than by a diff, because a diff against HEAD goes clean the moment a change is committed and would have been a bar that cannot fail.
- **AC7** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): would a reviewer now be able to answer, for a real role, "which of its granted permissions are unused" WITH THE EVIDENCE ATTACHED -- and is the population large and well-chosen enough that the answer says something about the estate rather than about one convenient role? Round 1 exercised the instrument on ONE role; a deliverable that does the same at greater length has not moved this outcome.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output -- bound every AWS read.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>3</round>
<slot>~8</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 3) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2, amended at six sites @3cadaf52ca
**Authority chain:** round-2 slug @d076801ecf -> `ROUND_ANALYSIS.round2.md` @3cadaf52ca section 8 (R3-B) -> L5 round-3 decomp -> this issuance.
**Chain:** an independent chain of one.
**Provenance and THE ONE PLACE THIS ORDER DEPARTS FROM THE ANALYSIS:** section 8 frames R3-B as EXTENDING comp-iam-usage to the permission axis. This issuer measured at HEAD that the permission axis ALREADY EXISTS (`permission-cold`, self-test passing, naming FWD-2's own phrasing), and that round 1's instrument-build cell produced no usage result. The cell is therefore cut as an EXERCISE, which serves the ruling's own intent -- C-EXTEND-NOT-BUILD's ladder puts "the estate already has it" above "extend" -- and is recorded as a surprise ROW rather than settled silently. FWD-2's bar is EXERCISED; an extension would still have left it unexercised.
<preflight>
comp-iam-usage: INSPECTED at HEAD -- tracked, 20-line launcher over org/modules/graph/comp_iam_usage.py; `permission-cold` present with --role/--lookback/--json; `self-test` RUN and PASSING, asserting never-used!=cold, UNKNOWN-band, hold-aware, 22a limits NAMED, permission-grain unobservable!=never-used.
comp-iam: RUN at round-3 vintage from a CLEAN worktree via the explicit .tools/ path -- 191 TF roles / 188 services / 1084 operations / 304 gaps; bare-name form reports 195 against the main checkout.
comp-schedule: RUN to completion, 5 of 5 carriers, 13.5 s. GATES ARMED 25, none this project's.
comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16 at vintage 2026-09-10 12:24:50 UTC.
comp-adversary: RUN on the round-3 rectangle.
</preflight>

**Preflight disposition:** mandatory core RUN at the round-3 vintage. comp-blast DECLARED-NOT-APPLICABLE -- this cell changes no Terraform custody and applies nothing. The ACCESS plane is this cell's own instrument and is exercised by the cell rather than at preflight.
