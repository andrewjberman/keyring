# FINDING: Cottonwood has ZERO representation in the MDPF freshness gate

**Status:** ACCEPTANCE BASELINE (CTO ruling 20260804T001415Z, via AE base 001607Z)
**Author:** `0.7.0_AE_CloudOps~B` · **Date:** 2026-08-04
**Addressed to:** `1.0.0_SA_CTO` (gate) · `0.7.0_AE_CloudOps` (trigger owner) · `2.0.0_SA_COO` (issuer)
**Method:** read-only measurement. **No file was edited.** Trigger file is base-lane surface.
**Origin:** surfaced while measuring row 13 for the CI-R7R8 row-7 gate; CTO ruled it
outranks the row-13 question and routed it as its own live finding (001131Z).

---

## 1. THE FINDING

**The MDPF daily freshness gate has no representation of Cottonwood at all.** It cannot
report Cottonwood as lagging, cannot flag it, and **would read healthy on the day that feed
breaks.** The partner roster knows three partners; this consumer knows two.

Sharpened by same-day context (CTO 001131Z): **Cottonwood is the partner in which both
served-integrity defects were found on 2026-08-03** -- a double-count and shell-degenerate
values reaching client surfaces. The gate that should notice that channel going wrong does
not know it exists.

---

## 2. THE MEASUREMENT (reproducible; every citation vintage-pinned)

**Surface:** `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py`
**Denominator:** 892 lines
**Repo vintage:** `@ebb6e5a3e4` (2026-07-28T18:40:04-04:00)
**Deployed:** `LastModified 2026-07-28T22:44:10Z`, `CodeSha256 e+UKa2C0AiQXOSm7aavHlzL9ixt+GQq6e+8VLr13nyU=`
-> deployed 4 minutes after the commit, so **REPO-TRUE == RUNTIME-TRUE**. This is not a
repo-only reading.

```
grep -c -i cottonwood  lambda_function.py   ->  0      <-- the finding
grep -c -i inflection  lambda_function.py   ->  5      <-- POSITIVE CONTROL
grep -c -i roster      lambda_function.py   ->  0
```

**The positive control is what makes the zero admissible.** `inflection` = 5 in the same
grep proves the file does hold partner names, so the cottonwood zero is a **real absence,
not a broken pattern**. Independently re-run by CTO before ruling (001131Z).

**Where the two-partner assumption is hardcoded:**

| Line | Content | Consequence |
|---|---|---|
| `:748` | `partners = {"49financial": bd}` | dict literal; membership is code, not data |
| `:757-763` | gate dict hardcodes `"inflection"` + `"49financial"` | third partner unrepresentable |
| `:726` | `bd = _check_schwab_rps(now) if custody_source == "schwab" else _check_bd_silver(now)` | two-branch, single-partner |

**Onboarding partner #4 at this address requires three code edits** (the `:748` dict, a new
`_check_*` function, new env vars) -- not a roster row. This is the direct negation of the
PRD:399 criterion *"onboarding a partner is a roster row, not a gate edit"*.

---

## 3. THE T2.C QUESTION: THE FLOOR **INHERITS** THE BLINDNESS (at today's vintage)

CTO's deciding question (001131Z): does the T2.C rework supersede this gate, or inherit it?

**At the code as committed/deployed today: INHERITS.**

- `infra/aws/terraform/mdpf-pipeline/scheduled-floor.tf:117` targets
  `module.mdpf_daily_trigger.function_arn` -- **the same Lambda**.
- `is_floor` (`:717`) gates **only** `run_date` (`:729-732`, own calendar frontier).
- The gate construction at `:726` / `:748` / `:757-763` is **common-path and unconditional**.

**Therefore a floor fire evaluates the identical two-partner gate.** The floor does not
re-implement freshness; it re-schedules the component that already cannot see Cottonwood --
moving the blindness from an event path onto a **clock**.

### VINTAGE RECONCILIATION (AE base 001607Z -- both records stand)

| Claim | Vintage | Status |
|---|---|---|
| `~B`: **INHERITS** | code as deployed/committed 2026-08-04 | TRUE at its vintage |
| AE base: **SUPERSEDES** | post-`:769`-change design | TRUE at its vintage |

Recorded explicitly so the two records **compose instead of contradict**. Neither is a
retraction.

---

## 4. DISPOSITION (ruled, not proposed)

**CTO ruling 001415Z**, on AE base's compound answer 001330Z: when the `:769` hard-DEFER
change cuts, **partner representation is fixed IN THE SAME CHANGE, roster-derived, at both
layers**:

1. the **floor path stops gating on partners entirely** -- delegating to the roster-driven
   participation schema, where Cottonwood is present at window 3;
2. the residual **accelerator** gate's `:748` dict and `:757-763` literals go **roster-derived**.

**No partner literal survives at either layer; onboarding becomes a roster row.**

**Timing:** the Lambda cut waits on DS dim edits (CTO schema-validated 000925Z) and Andrew's
word at the AE base terminal. **This finding adds no gate** -- it supplies the evidence the
existing gate is measured against.

---

## 5. THIS DOCUMENT IS THE ACCEPTANCE BASELINE

CTO amended T2.C acceptance to make the transition measurable **using this method**. Post-change,
re-run the same greps with a positive control:

```
roster refs                     > 0     (baseline today: 0)
hardcoded partner literals      = 0     (baseline today: :748 + :757-763)
every roster partner resolvable at BOTH layers
a known-present term printed beside EVERY zero    <-- the control is mandatory
```

**CTO also ruled the REFUSED row 7 becomes re-runnable on this change's verified landing,
with the post-change grep as its evidence.**

---

## 6. A FALSE POSITIVE I CAUGHT ON MYSELF -- recorded for calibration

My first measurement was `grep -c -i cottonwood` on **`scheduled-floor.tf` = 0**, and I had it
half-written as the headline finding. **It is not a defect.** That file is an
`aws_scheduler_schedule` + IAM role + `aws_lambda_permission`: **structurally there is nowhere
for a partner name to appear.** Nothing in that Terraform is implicated; its timing derivation,
DST anchoring and DLQ wiring are sound.

> **THE GENERALIZATION: a zero is evidence only when the container could have held a non-zero.**
>
> The cottonwood zero in `lambda_function.py` **is** evidence -- `inflection`=5 in the same grep
> proves the container holds partner names.
> The cottonwood zero in `scheduled-floor.tf` is evidence of **nothing**.
> **Same command, same word, same repo, opposite epistemic status** -- and only the file's
> STRUCTURE tells you which one you are holding.

Reporting a count off a file whose shape cannot hold the counted thing is the **same class** as
the row-13 error I was dispatched to measure. Had it gone out, it would have been a false alarm
against an author who had done nothing wrong.

**Related, from the same thread:** I also had *"the row-13 amendment was never landed"*
half-drafted -- a claim that the CTO's own ratification never happened -- before registering that
the PRD mtime `15:01 EDT` and the amendment at `19:00Z` are **the same instant**. The amendment is
landed at `docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md:399 @4f60111035`, 83 seconds after
COO's relay.

**Two near-false-claims in one measurement pass, both caught pre-send, both against senior
seats' own work.** Recorded because a seat that reports only its wins gives its readers no
calibration (CTO 001131Z).

---

## 7. THE DURABLE LESSON (CTO 001131Z, banked verbatim)

> **AN UNISSUED GATE VERDICT IS NOT A PAPERWORK GAP -- IT IS A DISABLED CONTROL.**

PRD:399's *"LANDS IN THE SAME CHANGE AS ROW 7"* clause **was** the control against exactly the
state measured here. It was enforceable only at the CTO gate. That verdict never issued, so
nobody was watching the coupling, and the 07-28 re-point landed four days later unchallenged.

**My corollary from this thread:** the control was disabled **silently**. Nothing in the estate
reports a gate as *owed-but-unissued*. The ten days were invisible until a fresh session happened
to read an `issued_to` field -- the same detection gap as the lane-folder/`issued_to` class COO
routed to CTO as a BUILD (`ADHOC.tocheck-issuedto-keying`, staged `@da4a6b51c1`).

---

## Compiler Tools

| Tool | Command | Result | Value |
|---|---|---|---|
| `comp-which` | routing check at load | forwarder RAN (own banner) | A.3 exercise half -- resolution is not execution |
| raw `grep -c` + positive control | partner-term census over 892 lines | 0 / 5 / 0 | the finding + its admissibility. `# rail-checked:` no comp-tool models per-partner representation inside one Lambda source file |
| `aws lambda get-function-configuration` | deployed sha/size/env | REPO-TRUE == RUNTIME-TRUE | operational read; establishes the liveness column CTO added |
| `aws ssm get-parameter` | `/mdpf/custody_source` = `schwab` | active branch confirmed | grounds which `:726` branch is live rather than trusting a 10-day-old log |
| `git log -1 --format` | vintage pins on every cited file | -- | Rule 22: a line citation without a vintage is not a citation |

**What worked:** the positive control, twice -- it made one zero admissible and exposed the other
as meaningless.
**What failed:** nothing tooling-side. Both near-misses were mine and were caught by structure
checks, not by tools.
