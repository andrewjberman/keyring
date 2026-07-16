# 0.7.0_AE_CloudOps~B -- delta 2: 122-HIGH decomposed (96% trash), NFRA_INFRPT_V2 drafted, F-A CLOSED + VERIFIED -- and Andrew's own 07-13 remedy found ROTTED into a false clean

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE, SCRIBE
**serial:** 0.7.0_AE_CloudOps~B (lane ~B; base folder) | **date:** 2026-07-16 | **window:** ~15:20Z -> ~18:05Z (delta since `6c41b330c`; ONGOING -- Andrew's session)

## Summary

1. **ANDREW REFRAMED THE WHOLE AUDIT (verbatim, recorded `e3aaec0b0`): SALVAGE, NOT REPAIR.** *"not necessarily
   'fixing' the calibrations if the calibrations are just wrong ... identify what is actually important, what
   are actually good ideas ... grab those and refine as needed, and throw out all the trash."* **This
   SUPERSEDED "noise vs real" as the unit of analysis** -- the verdict is on THE CHECK, not a line of output.
   KEEP / REFINE / DISCARD. **THE BLADE: "if this check fires, is there something a human would DO?" No ->
   trash REGARDLESS OF ACCURACY.** It corrected my own instinct AND MSTR's charter constraint: **suppressing a
   bad check KEEPS the bad check**; deletion is the remedy; suppression is only for a GOOD check whose findings
   are known/accepted. Broadcast to MSTR+COO; both folded it.
2. **SECURITY 122 HIGH -> ~5 REAL (~96% trash), decomposed on the raw report (denominator 122/122 parsed).**
   102 = AWS-MANAGED policies flagged for `Resource:*` (`AWSLambdaBasicExecutionRole` x53,
   `AmazonSSMManagedInstanceCore` x48, `AmazonECSTaskExecutionRolePolicy` x1) -- unactionable BY CONSTRUCTION.
   11 = DynamoDB "encryption not enabled" -- **FACTUALLY IMPOSSIBLE** (on by default since 2018, cannot be
   disabled; scanner reads `SSEDescription==null` and renders "not enabled"; **control: 11+ tables DO populate
   `SSEType: KMS`**, so the field works). **The metric is ANTI-CORRELATED WITH GOOD WORK: today's "+2 HIGH" is
   our OWN new `consolidation-gold-runner-role` flagged for carrying AWS's standard SSM policy.**
3. **THE LAST THREE SECTIONS WALKED (Andrew: "Finish these three").** `trade-parquet-batch-export`: REAL 3/3/3/3,
   but **the AI's fix is DANGEROUS** -- IAM is CORRECT (role holds Query on `opal-trade-submissions/index/*`);
   the Lambda queries **`trade-submissions`, a table that DOES NOT EXIST** (`config.py:8`, one missing `opal-`
   prefix; the writer `portfolio_excel_generator:49` has it right). **AccessDenied does NOT mean the resource
   exists** -- 3-way ambiguity the AI collapsed to one. **Caught ONLY because my positive control ALSO returned
   implicitDeny** (nonsense for a role named `trade-submission`) -> read the policy -> found the prefix.
   Right-size: `inf-gold-layer-runner` **RUNNING 14h past its job at 1.2% CPU** -- REAL, but "right-size
   candidate" prescribes DOWNSIZE when the fix is STOP (measure idle-hours-billed, not avg CPU); **my
   "batch box defamed by a 14d average" hypothesis was WRONG**. Deploy-drift: "stale artifact OR out-of-band
   deploy" is a compound verdict **CloudTrail resolves in ONE call** -- `UpdateFunctionCode` on
   `opal-partners-data`, 2026-06-03, `Andrew_Berman`. **The hand-fix exists ONLY in the deployed Lambda; the
   next `bd-pipeline` apply reverts it** (and that module currently `cannot-assess`, which is the only reason
   it hasn't).
4. **NFRA_INFRPT_V2 DRAFTED (Andrew-direct), on file, NOT ROUTED** -- `docs/briefs/NFRA_INFRPT_V2_PRD-draft-20260716.md`
   (`7aabb2da7` -> `d7dc6a706`). Andrew: *"just write a fucking brief and keep it on file, i will tell you when
   to send to CTO."* **ROOT CAUSE: V1 is a UNION of independent checks** (each observes alone, rates alone, top
   line = max()) -- every symptom falls out of that ONE property. **V2 = a PIPELINE:** REGISTER (action_on_fire
   REQUIRED or it does not ship -- would have killed 113/122 at birth) -> OBSERVE (UNKNOWN first-class) ->
   NORMALIZE (**no compound verdicts; a finding may not contain "or"**) -> CORRELATE (**the join V1 never does
   -- it held BOTH HALVES of 3 incidents and joined neither**; standing join EVERY CONTROL |x| ITS READER) ->
   SUPPRESS (owner+reason+**EXPIRY**) -> RANK (**BLIND > CONTROL-DEAD > REAL-NEW > REAL-CHRONIC > ACCEPTED**)
   -> RENDER ("nothing to do today" must be expressible) -> MEASURE (unactioned 30d -> deletion review, incl.
   itself). **AI layer scoped BY MEASUREMENT: diagnosis 3/3 falsified -> FORBID; prioritization correct -> KEEP.**
5. **F-A (RV-0050) TAKEN, MEASURED, RULED, LANDED, VERIFIED -- and it opened the day's biggest finding.** CTO
   assigned provisional ownership; I measured before proposing (**4,295 B / 25 lines / 2 months across all
   four** -- churn VERIFIED non-pathological, not assumed) and found **the mechanism of the blindness is ONE
   LINE: `.gitignore:68 *.log`**, identical for 4/4. A housekeeping glob **severed the estate's audit trail**;
   RV-0050's "2 of 13 walked" is its DOWNSTREAM SYMPTOM.
6. **THE FINDING OF THE DAY -- ANDREW'S OWN 07-13 REMEDY HAD ALREADY ROTTED, INTO A FALSE CLEAN.**
   `.owned-paths.yaml:52` records **Andrew-direct 2026-07-13 (RV-0049)**: the logs were untracked, *"erased by
   a fresh clone or a dead disk, with their ABSENCE INDISTINGUISHABLE FROM 'no overrides ever happened'."*
   Remedy = a snapshot archive. **It ran ONCE (`2026-07-13T144931Z`) and never again (comp-grep: ZERO
   invokers).** Six hours later `2.0.0_SA_COO~Z` overrode a sovereign `[STOP]` from MSTR **twice** --
   **neither entry was in ANY durable record.** The archived halt-gate log's only entry was the **TEST_SERIAL
   fixture**. **AND THE FALSE CLEAN WAS A COMPOSITION OF TWO CORRECT DECISIONS**: snapshot-not-track (sound:
   *"a log anyone may rewrite is not a log"*) + filter-TEST_SERIAL (sound: the fixture is contamination) =
   **"ZERO halt-gate overrides ever."** **Nobody erred. The COMPOSITION is the defect** -- which is why it
   survived two reviews, a ruling and RV-0050. **CURED**: CTO landed `d8b34eaf3` (path rules, GOVERNANCE_AUDIT
   lane) + `.gitignore` un-ignores + `:52` reconciliation, tracked at `b150952ba`, pushed `b06048dd5`.
   **I VERIFIED IT MYSELF, not his self-report: `git cat-file -e origin/CLOUD:` 4/4 PASS; the durable log now
   carries 3 entries, 2 REAL. The two sovereign-STOP overrides are safe.**

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-grep | x4 (`accounts_dim`, `silver/accounts_dim`, `trade-submissions`, `audit/archive`) | PASS | source-confirmed the ADVI_INFREF 06-30 repoint, the `config.py:8` prefix bug, and **ZERO invokers on the audit archive** |
| aws iam simulate-principal-policy | 2-arm battery on `trade-submission-lambda-role` (target GSI + base-table control, **ISOLATED calls**) | **BOTH implicitDeny** | **THE FAILED POSITIVE CONTROL IS WHAT CAUGHT THE REAL BUG.** Target-only would have CONFIRMED the AI's wrong fix |
| aws primitives (live) | cloudwatch x6, logs filter x5, dynamodb describe x4, ec2 describe/CPU, cloudtrail lookup-events, sns list-subs, events describe-rule/list-targets, s3 ls x6, lambda get-config/get-policy | PASS | APPLIED truth for every claim |
| git check-ignore -v / cat-file -e | 4/4 ignored-by `:68`; post-landing 4/4 on origin/CLOUD | PASS | **`cat-file -e origin/CLOUD:` = CVO's corrected durable criterion, adopted** |
| safe-commit.sh | x4 (2 landed, **2 BLOCKED by owned-paths**) | 2 PASS / 2 BLOCK | the gate fired correctly on `docs/architecture/` (ANY_CTO) and `.gitignore`+logs (BASE_EXEC/UNDEFINED). **Not overridden.** |
| python (stdlib parse) | 122/122 HIGH decomposed by rule + category | PASS | denominator printed; header-claim vs parsed-count reconciled |

**What worked:** grounding every report claim on the live primitive instead of arguing with the document --
each FALSE verdict came from one `aws s3 ls` its author never ran. **The failed positive control on
`trade-parquet` is the session's best instrument moment**: target-alone said implicitDeny and would have
confirmed the AI; the *control* returning implicitDeny for a role named `trade-submission` was nonsense, and
that nonsense drove me to the policy and the phantom table.

**What failed (MINE, all caught in-flight by a control, not by care):** (1) `--filter-pattern '[ERROR]'` --
CloudWatch parses `[..]` as a BRACKET PATTERN, not a literal; matched START/END/REPORT. (2)
`grep -c 'HALT-OVERRIDE'` -> 4 against 3 entries -- **the log's own header carries the format spec**. (3)
"bd producers have no scheduler" -- WRONG, `bd-allocation-pipeline-trigger` is ENABLED. (4) "the 14d-avg-CPU
axis defames batch boxes" -- WRONG here; the box is genuinely running 14h idle. **Four hypotheses, four
killed by live checks. Knowing the failure class did not immunize me against writing it.**

**Gaps found:** the freshness manifest has no invoker (D-2, mine); **the audit-archive snapshot has no invoker**
(escalated, ASK-1 granted to me); `safe-deploy-bypass-audit.log` records **actor=UNKNOWN on 3/3** (an audit log
that cannot name who bypassed -- and `halt-gate-override-audit.log` in the SAME estate gets `agent={serial}`
right); a **TEST_SERIAL fixture line in the production audit trail**; **a census over these logs has a
false-positive floor of 1** (the header matches the pattern).

## MCP traffic

~9 in / ~9 out. **Out:** the SALVAGE reframe record+broadcast (MSTR w/ the charter-constraint CORRECTION, COO);
F-A ACK+mechanism proposal; F-A BLOCKED report; the archive-rot URGENT (CVO + CTO); the verify + census-floor
catch; the census-poisoning + false-refutation synthesis; **a CORRECTION of a false credit in my own favour**.
**In:** CTO x4 (F-A assign / mechanism RULED / STOP-before-add + landed / ACK census-floor); CVO x4 (the ghost
URGENT / attribution accepted + `.owned-paths` lane / independent confirm + their own self-catch / clear);
COO (push discipline + salvage folded); MSTR (SCTY framing correction); base (allocations banked).

## Deployment Sequence + Verification (AE)

**Zero deploys, zero TF, zero mutations by me.** Read-only diagnostic by Andrew's design. **TWO safe-commits
BLOCKED by the owned-paths gate and NOT overridden** (`docs/architecture/` = ANY_CTO; `.gitignore` = BASE_EXEC;
3 of the 4 logs = **UNDEFINED**). CTO landed the F-A change under his own author line; I **independently
verified** it rather than accept his self-report: `git cat-file -e origin/CLOUD:` **4/4 PASS**, durable
halt-gate log = 3 entries / **2 REAL**, negative control (`comp-which-rail.log`) **absent** => the negation is
NARROW, and the big two correctly still untracked (split held).

## Blockers

**None.** Nothing half-landed; index restored to session-start state; tree clean.

## Current State (handoff, zero-prior-context)

- **Andrew's commission is COMPLETE**: the whole infra report is walked (freshness / automation / security /
  drift / SNS / cost / deploy-drift). **`docs/briefs/NFRA_INFRPT_V2_PRD-draft-20260716.md` (`d7dc6a706`) is ON
  FILE and NOT ROUTED -- Andrew reserves the send to CTO. Do not route it.**
- **Brief sec 4b carries THREE laws EARNED after the draft** (all measured, not reasoned): **(1) "a cadence's
  corpse problem is not solved by adding a cadence, it is solved by ALARMING ON THE CADENCE'S DEATH"** --
  **1.0.0_SA_CTO's sentence, verbatim** (I corrected a misattribution of it to me); measured 3x (manifest 29d /
  archive 3d / CVO's index criterion). **(2) A file's header is a CENSUS-POISONING SURFACE** -- count ENTRIES
  anchored `^[0-9]{4}-`, never pattern hits; earned by **3 wrong counts over ONE 16-line file in one afternoon
  by the finder AND the validator, in OPPOSITE directions, same cause**. **(3) FALSE REFUTATION** -- an
  instrument error that kills a TRUE finding with a citation; CVO's `grep -vc` -> 12 (true 0) was aimed at my
  correct escalation and only the tail-vs-count mismatch stopped it. The estate has no name and no control for
  this direction.
- **NAMED, NOT HIDDEN, in the V2 design:** L0 gates checks one at a time; **nothing gates their COMPOSITION** --
  and the archive false-clean came from composing two correct decisions. That is V2's own next hole.
- **F-A CLOSED**: 4/4 durable on origin/CLOUD (`d8b34eaf3` rules / `b150952ba` tracking / `b06048dd5` push).
  CTO's GOVERNANCE_AUDIT lane over my ANY_EXEC_OR_AE instinct is right -- my read was **permission-correct and
  design-wrong**.
- **Live peers:** base `0.7.0_AE_CloudOps` (PID 25356) on today's timed reads; CTO/CVO/COO active on this thread.

## Next Steps

- **[Andrew, reserved]** the send of `NFRA_INFRPT_V2_PRD-draft-20260716.md` to CTO. **His call, not mine.**
- **[me, at Andrew's sequencing; CTO's gate]** (a) the **audit-archive snapshot INVOKER proposal** -- ASK-1
  granted, with CTO's binding constraint: **the invoker must carry its own FAILURE INSTRUMENT** (absence-registry
  row / freshness alarm on the newest `org/audit/archive/` timestamp), because **a cadence's corpse problem is
  not solved by adding a cadence**. Must carry **CVO's baseline-freshness as a FIRST-CLASS ALARM, not a note**
  ("a caveat with no instrument behind it is a hypothesis, and the estate reads hypotheses as clean" -- CVO on
  their own RV-0050 ratification, whose 36-override census reads off the frozen 07-13 baseline).
  (b) the **`safe-deploy-bypass` writer patch** (actor= field, copying halt-gate's working format).
- **[2.0.0_SA_COO, accepted, NOT yet fixed]** **`model_portfolios` producer frozen since 2026-07-12** (4 trading
  days, calendar-resolved; all 4 files wrote at 14:10:42 and stopped together) **AND `model_portfolios.headline`
  is an UNCONTRACTED SEV1** -- the surface nothing governs is the surface that is stale. **The one REAL data
  finding the report surfaced today, still unfixed.** Lead (INFERRED, not a cause): `yang-pipeline` sfn drift.
- **[0.7.0 base, banked]** the bd/49 allocations chain (Andrew: passive-care under the 49 refactor).
- **[open, INFERRED]** read the monitor's prefix-aging code to confirm/kill the **newest-mtime FALSE-CLEAN**
  mechanism (a backfill of an old partition may reset the freshness clock with no new data). **The most
  dangerous open item**: false-alarm costs credibility; false-clean costs the outage.
