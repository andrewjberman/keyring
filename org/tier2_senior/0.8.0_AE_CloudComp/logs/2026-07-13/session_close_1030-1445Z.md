# 0.8.0_AE_CloudComp -- session close 1030-1445Z: P0-A schema split + Andrew's value-axis guard; and the INF chain's real lock (a bad deploy nobody knew was load-bearing)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE

---

## Summary

Two threads, both ending in the same lesson.

**INF (not my lane -- diagnosed, escalated, touched NOTHING).** Answered COO's RAVC2
(*"nobody has read the actual chain log"*). **The INF gold chain aborts at STEP ZERO** --
`sync_scripts()` basename collision on `build_assets_dim.py` (`code/gold` vs `code/silver`,
different content, deployed 2026-07-10T23:37Z) -- **it never reaches a pull.** Every mechanism
the fabric believed was holding the line was falsified, **including my own**. *We were being
protected by an accidental bad deploy* = **DOOR 5**, which the guard's own FATAL prints a
one-line remedy for and which the hold did not mention.

**OPAL_ASSETS P0-A (my lane -- shipped).** Pointed AC5's own falsifier at my own served
artifact: **RED on 18/19 partitions.** 162 rows served `fresh, staleness=0` over a 49F book 4
trading days stale, carrying an `as_of` no source ever reported. Split the overloaded `state`
enum into two canonical axes, then **Andrew broke every control I own with one sentence** and
I shipped his guard instead.

---

## Work Completed

### 1. INF -- the last unknown, discharged (READ-ONLY; zero writes, zero applies)
- **Trigger recon:** THREE EventBridge rules invoke `inf-gold-trigger`, not one.
  `inf-canonical-prices-daily` was **ENABLED**, `cron(47 14 * * ? *)`, target id
  `InfGoldTriggerFallback`, payload **`{"mode":"full"}`** -- byte-identical to the trap.
  **The rule's NAME says "prices"; its PAYLOAD runs the full gold chain.** A census by rule-name
  never finds it. The planned one-rule disarm was a **PLACEBO**.
- **`inf-gold-trigger` has NO data-state guard at all** (source-confirmed, sha-matched to live;
  there is a DECOY copy at `infra/aws/lambda/inf-gold-trigger/` -- NOT deployed). It starts a
  stopped EC2 and SSM-dispatches `--chain full`. It invoked **3x/day, 0 errors, every day of the
  "freeze"**.
- **THE ANSWER (chain logs, `s3://opal-data-inf/gold/logs/`, denominator 4,922 objects):**
  07-11 and 07-12 have **NO `chain_full_*` log at all** (07-10 has a 3.6MB one). Both carry the
  identical `FATAL: sync_scripts() basename collision`. **Deterministic. Still live in S3.**
- **Falsified, including my own claim:** *"repairing bronze fires the chain"* (it never reaches
  the pull); *"Orion recovering on its own is a CLOCK"* -- **MY claim at `105022Z`, RETRACTED**.
- **Instrument findings:** `SSM Success rc=0` is a **LAUNCH RECEIPT** (`--bg` detaches);
  **`ChainFailed` has NO datapoint because the chain dies BEFORE the metric is armed.** Both
  chain-health instruments are blind in the same window.
- **Sequencing catch:** flagged the chokepoint as **APPLIED-but-UNEXERCISED**, and that the
  **safe window to exercise it expires the moment anyone clears the collision** (today a failed
  chokepoint is harmless -- the collision still kills the chain at step 0). 0.7.0 exercised it
  (`5697cc340`): `held:true, dispatched:false`, lock untouched, EC2 stopped. **Closed by
  exercise, not assertion.**
- **Verified the disarm on the LIVE primitive** (a TF 0-diff is a DESIRED-state claim): armed a
  Monitor that caught both rules flip to `DISABLED` at 11:39Z + would have alarmed at 14:00Z if
  they had not. Guarded the one failure nobody covered: **CTO~B dying mid-apply** (MSTR ran ~70
  min dead this morning).

### 2. OPAL_ASSETS P0-A -- schema split, shipped and served-verified
- **Refused CTO~B's order to close P0-A.** He had declared it COMPLETE off **three independent
  live-AWS groundings**. He retracted. **All three of us asked the SAME question** -- *does the
  table exist and have rows?* **None asked whether the rows were RIGHT.**
  >> **INDEPENDENCE OF VERIFIERS IS NOT INDEPENDENCE OF QUESTIONS.** (to base CTO for the rulebook)
- **The defect:** `_partner_state` fell back to the ARTIFACT-level `as_of_date` (a CROSS-PARTNER
  value), stamped it into a PER-COHORT `as_of` -- fabricating a vintage no source reported, in
  violation of PRD s3d, **the very rule the emitter exists to enforce** -- then derived
  `"fresh" if as_of_date == run_date`, which held on **5 of 5** partitions where that branch
  fires. **A CONTROL THAT CANNOT FAIL IS NOT A CONTROL.**
- **The split:** `vintage_state` {fresh|rolled_forward|missing} + `coverage_state`
  {complete|incomplete|unknown}, canonical. `state` = a pure derived view, then **CUT** (Andrew:
  *"i likely would never read that"*).
- **The dry-run caught TWO defects INSIDE the fix:** CTO~B's condition 1 would have **ERASED the
  08335338 undercount disclosure** on 18 rows (he struck his own condition); and
  `_total__etf_fund` **hardcoded `state="fresh"` while computing `staleness=4`**.

### 3. >> ANDREW BROKE EVERY CONTROL I OWN, AND THAT IS THE FINDING <<
Andrew, verbatim: *"it's only ambiguous on weekends/holidays. otherwise there is no way that
we're going to be displaying the same number twice."* **He does not read our labels** -- he
infers staleness from **whether the NUMBER MOVED**. Measured on the served table: **16
trading-day repeats were labelled `fresh`. He predicted zero. Every one was a defect.**

Six were mine: `_total__etf_fund` took its vintage from mdpf's ARTIFACT `as_of_date` (which
describes the **PARTNER** data) for a row whose CONTENT is **ETF** data, and served `fresh` over
feeders a **WEEK** stale.

>> **MY AC5 FALSIFIER REPORTED GREEN ON 532 ROWS WHILE THAT WAS LIVE.** `vintage_state` and
   `staleness` BOTH derive from the source's `as_of` -- a lying `as_of` makes them corroborate
   each other **perfectly**. <<
>> ## **A CONSISTENCY CHECK CANNOT CATCH A WRONG INPUT.** <<
**His crude heuristic beat every formal control in the package because it grounds on the VALUE
and every control I built grounds on the LABELS.** I landed the "independence of questions" rule
this morning and proved it against myself four hours later.

**Andrew chose option A** (of A/B/C): *don't change the number -- fix the SOURCE and automate the
check I was doing by eye.* Shipped.

### 4. Deliverables shipped (all TF safe-apply, 0-diff, sha-matched, served-verified)
| # | Thing | Note |
|---|---|---|
| 1 | vintage/coverage split; `state` CUT | 0/532 rows carry `state`; `derive_state()` survives as a pure fn nothing writes |
| 2 | **Andrew's value-repeat guard** | trading-day repeat + claims `fresh` -> **withhold the FRESHNESS CLAIM, KEEP THE VALUE** + CloudWatch ALARM line |
| 3 | `_stamp_state` write-gate | RAISES `VintageContradiction` on any row claiming `fresh` while its own as_of puts it behind |
| 4 | AST anti-drift lint | `state`/`staleness` writable ONLY by `_stamp_state`; carries its OWN positive + negative controls |
| 5 | AC5 falsifier + 5 mutants | GREEN after; **still RED-capable** |
| 6 | `staleness` residual disclosed | on **532/532 served rows**, not just a commit message |

**THE VALUE IS KEPT, deliberately:** these are ADDITIVE cohorts -- withholding one breaks
`sum(additive)==carried total`, AC7 fails, and the **ENTIRE PARTITION** is refused. *A guard that
takes out a day of data on a heuristic is a bigger defect than the one it catches.*

---

## Deployment Sequence + Verification (AE role requirement -- ACTUAL output)

```
package -> upload (--metadata content-sha256) -> READ-BACK VERIFY -> plan -> safe-apply -> 0-diff
         -> APPLIED sha == built sha -> re-emit 19 partitions CHRONOLOGICALLY -> SERVED verify
```
**Upload-verify gate (my own shim lesson, carried forward): `aws s3 cp` rc=0 is NOT the oracle.**
Verified by reading the bytes back and comparing sha256 -- and controlled that both sides were
real 64-char hex, not a shared error sentinel (the `HEAD_FAILED`-vs-`HEAD_FAILED` trap).
**Gotcha banked:** an S3 overwrite REPLACES metadata; a plain `cp` stripped `content-sha256` and
Terraform **failed closed** rather than deploy something it could not hash.

**FINAL SERVED-ARTIFACT VERIFICATION (532 rows / 19 partitions):**
```
`state` on served rows          : 0 / 532           (CUT)
canonical axes present          : 532 / 532
ANDREW'S TEST (value axis)      : GREEN -- 0 trading-day repeats claim fresh   (16 -> 10 -> 0)
AC5 falsifier (label axis)      : GREEN -- 0 / 532  (RED-capable: it fired twice today)
guard-downgraded rows           : 10 (freshness withheld, VALUE KEPT)
POSITIVE CONTROL                : fired on EXACTLY the 10 rows measured bad BEFORE it was built
residual disclosed on the row   : 532 / 532
reconciles TO THE CENT          : 19 / 19 partitions (AC7 passed on every partition)
MONEY                           : $33,956,793,166.72 -- UNCHANGED across all 4 re-emits
tests                           : 49/49 green; commit-gate clean
IAM (new GSI Query)             : simulate-principal-policy `allowed`, positive control run as a
                                  SEPARATE invocation (never batched -- multi-ARN poisoning)
```
**Honest number:** the reconcile is **exactly zero on 11/19**, not 19/19 -- the rest carry a
**2E-8** float residue from `partner_model_sum`. Three orders inside AC7's $0.011 tolerance, so
it reconciles TO THE CENT as required. **Reported, not rounded away** -- writing "delta = 0.00"
is the exact laundering this change exists to stop. Decimal arithmetic queued; it touches VALUES
so it rides its own never-widen gate.

---

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-freshness` | `ddb opal-assets-daily-aua` | WARN | "No items found with PK prefix ''" -- it cannot enumerate a `(run_date, cohort_id)` table. **GAP.** |
| `comp-grep` | `opal-assets-daily-aua`, `state` consumers | PASS | on-rails, .gitignore+submodule-aware; surfaced the 972 sovereign-held exclusions rather than hiding them |
| `comp-glob` | `**/opal-assets/**/*.py`, `orion-gold-dispatch.sh` | PASS | found the deployed-vs-decoy split |
| `comp-which` | "which script writes daily ETF ownership to opal-data-etfs" | PARTIAL | routed to `comp-platinum`; did not identify the producer |
| `pipescript` | `--resource opal-data-etfs` | **FAIL** | **"no thread references 'opal-data-etfs'."** |
| `comp-iam` (+ `simulate-principal-policy`) | emitter role vs `cohort_history` GSI | PASS | `allowed`; positive control run SEPARATELY per Rule 22a |

**What worked:** `comp-grep`'s sovereign-hold disclosure (it says what it did NOT search --
*"not confirmed absent"* -- which is exactly the "an instrument that cannot observe must say so"
posture). `simulate-principal-policy` with a one-ARN-per-call + separate positive control.

**What failed:** `comp-freshness ddb` cannot read a composite-key table -- it reports WARN/no-items
on a healthy 532-row table. A freshness tool that cannot see the artifact reports the same thing
as a dead artifact.

**GAP FOUND (routed):** **`pipescript --resource opal-data-etfs` -> "no thread references it."**
**The producer of a bucket that feeds a SERVED artifact is absent from the dependency graph** --
a `comp-blast` on those producers would show ZERO downstream consumers, and OPAL_ASSETS is one.
Worth an NFRA ticket.

---

## MCP Traffic

~20 messages. Significant:
- **IN:** MSTR dispatch (P0-A + STOP b7bce51bd) · COO `[STOP]` (INF bronze) · MSTR `[STOP]`
  (deploy freeze, then CORRECTED to scope-by-EFFECT incl. DELETION) · CTO~B ruling (b) + his
  **retraction** of "P0-A COMPLETE" + his **retraction** of condition 1 · COO NEVER#2 co-sign ·
  COO RAVC2 (read the chain log) · 0.7.0 sequencing question.
- **OUT:** RAVC2 ANSWERED (the collision) · `[STOP]` escalation to CTO (the one-rule disarm is a
  placebo; the 14:47Z cron) · **`[STOP]` to DS** (do NOT resolve the collision -- door 5, the hold
  does not mention it) · never-widen co-sign request · source-fix routed to **0.5.0** via COO ·
  P0-A closure to CTO~B.
- **Corrections I issued to my own reports: 3.** One retraction was itself ungrounded and the
  MEASUREMENT restored the original claim. **A retraction is also a claim and needs the same
  grounding.**

---

## Blockers

**NONE.** Nothing of mine is blocked.

---

## Current State (handoff -- assume zero prior context)

- **`opal-assets-daily-aua`** (DynamoDB, PK=`run_date`, SK=`cohort_id`, GSI `cohort_history`):
  **532 rows / 19 partitions, all verified honest.** Canonical fields: `vintage_state`,
  `coverage_state`, `as_of`, `as_of_basis`, `staleness` (+`staleness_semantics` disclosing its
  dual purpose), `value`, `additive`, `basis`, `value_class`, `masters_present`, `source_masters`.
  **`state` no longer exists.**
- **`opal-assets-daily-emitter`** (Lambda, TF-managed via
  `infra/aws/terraform/opal-assets/`, artifact
  `s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-daily-emitter.zip`; the
  artifact **MUST** carry `content-sha256` metadata or `terraform plan` fails). Source:
  `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/lambda_function.py`. Schedule
  `opal-assets-daily-emitter-daily` ENABLED, `cron(15 17 * * ? *)`.
- **The emitter is FROZEN at `run_date=2026-07-10` BY DESIGN** -- `run_date` is the SOURCE
  partition's filename date, and mdpf cannot advance past a gold frozen by the INF hold.
  **IT IS NOT BROKEN. DO NOT "FIX" IT.** That is **door 3**, and it never touches an INF file.
- **The bucket-staleness alarm is STILL DELIBERATELY UNBUILT.** Under the hold its only function
  would be to page a future agent into the destructive INF repair. It ships when the hold lifts,
  and only WITH a `frozen-by-deliberate-hold` discriminator.
- **INF:** both gold-trigger EventBridge rules **DISABLED**; chokepoint applied AND exercised
  (`5697cc340`). **The `build_assets_dim.py` collision is STILL LIVE and is load-bearing** --
  nobody may change its collision state (scope by EFFECT: write, delete, rename, or making the
  two copies identical).
- Commits (mine, this window): `6e26febe7` `37716b187` `c99ab5bb3` `aa445d3f6` `69f3ffed7`
  `bf7269a1e` `f8fc44ecc`. Tests: `infra/aws/lambda/opal-assets/tests/` (49 green).

---

## Next Steps

1. **[0.5.0]** (routed via COO `142017Z`) -- **fix `source_as_of` in the per-partner ETF producer
   to stamp the DATA date, not the FILE date.** It writes a file every day including weekends and
   stamps its own run date, so a carried value always looks fresh. **ACCEPTANCE TEST: my guard
   goes quiet on those 10 rows -- they self-correct to `rolled_forward`.**
2. **[1.0.0_SA_CTO~B]** G5 remains gated on the per-source `as_of`-semantics census. **Today IS
   its first result: two of the six sources (mdpf, opal-data-etfs) have now been measured and
   BOTH conflate a WRITE date with a DATA date. That is the census's finding, not a coincidence.**
3. **[0.8.0_AE_CloudComp]** Decimal arithmetic for `partner_model_sum` (kills the 2E-8 residue).
   Touches VALUES -> rides its own never-widen gate.
4. **[NFRA / CTO]** `pipescript` has no thread for `opal-data-etfs`; `comp-freshness ddb` cannot
   read a composite-key table.

---

## The thing worth keeping

**KNOWING A FAILURE MODE BY NAME DOES NOT IMMUNIZE YOU AGAINST WRITING IT.** In one session I:
wrote an AST lint against census-by-mention, then **did census-by-mention on `.gitignore`**;
landed "independence of verifiers is not independence of questions", then **had Andrew prove it
against me**; fixed a hardcoded-`fresh` in two places and **reproduced it in a third**; and swept
`.pyc` into commits **three times, once immediately after committing a message about that exact
mistake**.

**Every one was caught by a control firing, not by being careful.** *Care is not a control; care
is what you have instead of one.*
