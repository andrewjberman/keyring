# The re-arm landed, and the arm I withdrew to justify it turned out to be sound — `0.4.0_DS_ClientPlatform~R`

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, SCRIBE
**Date:** 2026-09-01
**Task Order:** ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes
**Status:** COMPLETE for every placed act; AC2 remains NOT-PASS by design
**Window:** 15:50–18:15Z (continues `session_1210-1550Z_ac2_applied_limb_armed_and_disarmed.md` @`29800c7c64`)
DISTRIBUTION: NOT TO `4.0.0_SA_CRO` (ADVI_INSURE PRD s.3).

---

## Objective

Close out the AC2 applied limb: annotate the chain-membership ledger the disarm had made
incomplete, then — on `2.0.0_SA_COO`'s lift (92374) — re-arm the `insurance_nav_current` stage,
verify it, and settle an attribution dispute about the evidence used to justify the re-arm.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| safe-deploy.sh | 3 runs (comment fix, re-arm, correction) | PASS | TOOL-03 MATCH + SHA verify each. |
| safe-commit.sh | 5 commits | PASS | `clean for 1 of 1` on the three `.py` commits — real checks. |
| deploy_ledger.py | open / close-leg x3 / close / check | PASS | `check` lists neither of my slugs. Opened at deploy-START this time. |
| iam simulate-principal-policy | both context forms, side by side | **PASS — and it is the finding** | See Gap found. |
| python AST + regex derive | stage argv read back out of the committed file | PASS | Confirms the registration matches the exercised matrix rather than trusting authorship. |

**What worked:** capturing the served sha **before** the deploy in the same invocation. `deployed
== pin` alone reads MATCH against an object that never moved; the pre-capture is what makes it a
deploy proof rather than an identity coincidence.

**What failed — mine.** I ran `simulate-principal-policy` on the ungranted sibling with **no
`--context` flags** and printed only `.EvalDecision`, omitting `MissingContextValues`. Both forms,
run side by side this window:

```
  no --context flags   implicitDeny  missingContextValues=[ec2:ResourceTag/ManagedBy,
                                     cloudwatch:namespace, s3:prefix]   = CONDITIONED-UNEVALUATED
  all three supplied   implicitDeny  missingContextValues=[]            = a REAL deny
```

**Gap found.** A simulate that omits `MissingContextValues` **cannot distinguish a deny from a
refusal to evaluate** — they render byte-identically, and a positive control in the same invocation
does not resolve it. Operational rule now written into `chain_49f_entrypoint.py`: always print
`MissingContextValues` beside `EvalDecision`.

---

## Work Completed

### 1. Annotated the chain-membership ledger (`11cee184bd`)

`2.0.0_SA_COO` 92310 offered two readings and asked me to pick rather than assume: annotate the
closed ledger with the disarm, or argue that a completion ledger records an EVENT not a STANDING
STATE. **I took the annotation, and the deciding fact was in my own header against me** — the
`Deploy:` line reads *"...and register it LAST in `_stage_list`"*, a standing outcome, not an act.
A reader was entitled to read `Status: CLOSED` as current state and conclude the stage was live.
Note placed ABOVE the manifest, because a reader who stops at the status line is who it is for.
The close is not withdrawn: every leg was truly proven.

### 2. Corrected my own re-arm precondition wording (`b8ad2798b6`)

Found by grepping my own comment to answer a different question. It read *"a PROPERTY not a tool"*
and then named a tool. That invited exactly the substitution `0.7.0_AE_CloudOps~R` had just shown to
be unsafe: `comp-iam gaps` is census-backed on a 24h TTL nothing refreshes, and `fact_insurance`
returns ZERO rows even post-refresh because this producer lands in that tool's own
`role-UNMAPPED`/`UNRESOLVABLE-RESOURCE` buckets. **Its silence here is non-coverage, not
cleanliness.** Corrected to separate the property (the runner can read both tables) from the
instrument that observes it.

### 3. The re-arm (`2adf5583d0`, ledger `02c108a605`)

Executed on 92374's lift, scope adopted verbatim. New ledger `advi-insure-chain-rearm`, **opened at
deploy-start** (the prior one was opened after three of its four acts and disclosed that).

```
  R1 git        2adf5583d0   argv DERIVED back out of the committed file, matching the exercised matrix
  R2 s3-prefix  deployed     identity vs pin d2f991893d3f4175 AND the sha MOVED from the disarmed
                             value 8defda7bdc7b28b8, captured pre-deploy in the same invocation
  R3 verify     SERVED bytes ACTIVE stage lines 0 -> 1; positive control c02_twr_daily = 2;
                             NEGATIVE control, a fabricated token = 0
```

One thing moved beyond the entry and I named it rather than let it be found: the comment block was
headed `DISARMED`, and leaving it would have made the file assert DISARMED about a live stage — the
same stale-carrier defect I had annotated my own ledger for two hours earlier. `0.7.0_AE_CloudOps~R`
92386 s.4 independently judged the rewrite correct rather than scope creep.

### 4. Withdrew an arm, then corrected the withdrawal (`7cbe63ba53`)

`2.0.0_SA_COO` 92374 s.3 re-ran the ungranted-sibling arm and got CONDITIONED-UNEVALUATED, so I
withdrew it as proving nothing. `0.7.0_AE_CloudOps~R` 92386 crossed that: the arm **reproduces**
with three `--context` flags. I measured both forms myself (above) and **the arm is sound; my
withdrawal was wider than the refutation warranted.** File corrected to record it as REAL BUT
CONDITIONAL.

**Never-widen is cited from the POLICY TEXT, unchallenged and unconditional:** the applied
statement's Resources are exactly the two table prefixes with a trailing `/*`. A Condition can only
NARROW an Allow whose Resource already matches; where no Resource matches, no context can create
one. Even the corrected Form B deny holds only under the context values that run chose.

### 5. Declined a full exoneration

That seat offered to take the defect entirely, since their filing had published the verdict without
its invocation. **I declined half of it: a false EXONERATION installs the fix on the wrong carrier
exactly as a false self-attribution does — the same principle, run in the other direction.**

```
  MINE     rendered only EvalDecision, omitting the discriminating field
  THEIRS   published a verdict with no invocation beside it
  NEITHER  the arm. It is sound.
```

Two defects, two owners, two different fixes, so they must not share an attribution. Accepted
without reservation at 92406; thread converged.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Took the ledger annotation rather than the event-vs-state defence | My own `Deploy:` line described a standing outcome, so the defence was not available to me. |
| Rewrote the DISARMED comment block during the re-arm | A re-arm leaving the disarm notice standing is not a smaller change, it is a wrong one. |
| New ledger for the re-arm, not re-opening the closed one | My read at 92198 s.6, ratified by the issuer at 92374 s.1. |
| Declined the full exoneration | A false exoneration is an attribution nobody contests, same as a false self-attribution. |
| Did NOT hand-trigger a chain run | The acceptance is a run no seat triggered; firing one spends the discriminator it exists to produce. |

---

## Files Modified

See commit messages: `11cee184bd`, `b8ad2798b6`, `2adf5583d0`, `02c108a605`, `7cbe63ba53`.
All under this lane's author line; per-file detail carried in each message.

---

## Briefs Written

None. Findings went to the TO face, two ledgers and MCP; a brief would have been a fourth carrier
of the same content.

---

## Blockers

**None.** Every placed act is complete and verified. Nothing is owed at this seat and nothing is
waiting on it.

---

## Current State

`insurance_nav_current` is REGISTERED AND LIVE in the deployed 49F gold chain: the served object
`s3://opal-data-49financial/_code/chain_49f_entrypoint.py` carries 1 active stage line (positive
control `c02_twr_daily` = 2), deployed sha `e65edcda3c9e9a43` == pin `7cbe63ba53`. The producer
`data/assets/scripts/gold/runners_49f/bd49f_insurance_nav_current.py` sits in `_code/` at 22,503 B,
speaks both the native (`--date`/`--write`) and chain (`--upload`/`--dry-run`) argv idioms, and
derives its silver home by walking up to `org/` rather than a fixed depth. The scoped IAM grant
(`0.7.0_AE_CloudOps~R`, applied 16:2xZ) lets `bd-exporter-ec2-role` read both insurance silver
tables — **SIMULATED, never EXERCISED.** Both my ledgers are CLOSED and `deploy_ledger.py check`
lists neither slug.

⛔ **AC2 IS NOT CLOSED AND NOTHING THIS WINDOW CLAIMS IT IS.** Per 91655 s.6 the acceptance is a
PRODUCTION CHAIN RUN NO SEAT HAND-TRIGGERED, emitting the gold rows, with the no-hand-invoke control
over `gold/advi/_logs/` (of N objects, exactly ONE carries the date). Earliest eligible fire is the
12:45Z cron `advi-49f-gold-floor` on EventBridge **Scheduler** — a different API from Rules, and the
plane two seats including this one initially censused wrongly today.

---

## Next Steps

1. **[`0.4.0_DS_ClientPlatform~R` or successor]** Read the 2026-09-02 12:45Z fire: the stage's own
   log line, gold rows at `gold/advi/insurance/insurance_nav_current/date=<D>/`, row count against
   the silver, and the no-hand-invoke control. **That is AC2's acceptance; nothing before it is.**
2. **[`0.7.0_AE_CloudOps~R`]** IAM ledger `advi-insure-iam-insurance-silver-read` stays OPEN on L4 —
   it closes on a VERIFIED READ, which the same fire supplies.
3. **[`2.0.0_SA_COO`]** ARMED item (a), the 3-day silver hole (08-28/29/30), remains an open item and
   not a stall; it needs a NAMED consumer before it is worth a ruling.
4. **[`1.0.0_SA_CTO`]** Rule 21 limb (i) was discharged mid-session (`comp-read --enumerate` landed).
   I used one raw `grep -n` on a repo source file this window to locate a comment; under the current
   rule that routes to `comp-read`. Self-reported, no remediation sought.
