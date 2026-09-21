# WORK BRIEF -- REGISTRY ASSIGNING (the "1,055 placeholder rows")

**For:** Andrew, in office 2026-09-21.
**Written by:** `2.0.0_SA_COO~G`, 2026-09-21 ~01:3xZ, at his ask.

> **TWO THINGS ABOUT THIS DOCUMENT, BEFORE THE WORK.**
>
> **1. It is NOT an L1 commissioning brief and must not enter the canonical flow as one.** The two
> real D14 briefs on this shelf were authored by `4.0.0_SA_CRO~D` and commissioned by Andrew; L1 is
> the CRO's lane. This is an **operator task spec** -- a document for a person sitting down to do a
> job. If this work is ever to become a project, it gets a real brief from the CRO first.
>
> **2. Andrew asked for it as `lgic_canon_registry_assigning`. I have named it `lgic-enforce-...`
> deliberately, because THE WORK IS `LGIC_ENFORCE`, NOT `LGIC_CANON`.** The placeholder population,
> the checker that produces it, and the outcome it blocks (FWD-5) all live in ENFORCE. Filing it
> under CANON would send a later reader to the wrong project. He said "or something like that," so
> I took the latitude; the subject is what changed, not the ask.

---

## 1. THE JOB, IN ONE LINE

**Tell the registry what ~200 things are, so the naming checker can stop printing `{system}` and
start printing a real name.**

## 2. THE NUMBER IS NOT THE WORK

The figure in circulation is **1,055** (sometimes 1,298 or 1,303, depending on vintage -- they are
the same population measured at different moments). **It is a count of ROWS, not of DECISIONS**, and
the record has always said so: the register calls it *"1055 rows of UNMEASURED decision count"* with
an **upper bound** of ~1,056 decisions. Nobody had measured the real number.

**1,302 of the 1,303 rows carry the IDENTICAL reason:**

> *"no row of any of the 6 registry files under `infra/logic/registry/` ... resolves this"*

So it is not 1,303 puzzles. **It is one question asked 1,302 times -- "what does the registry say
this belongs to?" -- and the answer is "the registry was never told."**

## 3. THE FAMILIES -- MEASURED 2026-09-21, THE PASS THAT HAD NEVER BEEN RUN

Of the **1,119 rows needing a `{system}` answer**:

| family | rows | % | looks like | example |
|---|---|---|---|---|
| **A1 -- firm read as a system** (`bd`/`inf`/`cot`) | **217** | 19.4% | **ONE decision** | `bd-gold-qa-runner-forgotten` |
| **A3 -- AWS service name read as a system** | **175** | 15.6% | **ONE rule** | `cloudfront-high-error-rate` |
| **A2 -- log-group path** (`/aws/<svc>/...`) | **67** | 6.0% | **ONE rule** (grade the tail, not the prefix) | `/aws/lambda/access-anomaly-scanner` |
| **A4 -- `opal*` prefixed** | **10** | 0.9% | **ONE rule** | `opalinvest-auth-handler` |
| **A5 -- everything else** | **650** | 58.1% | **the actual work** | `semantic-clustering-lambda-build` |

**A1-A4 = 469 rows (42%) that plausibly collapse to FOUR rules.** A1 is already established as one
class, not 217 questions -- that collapse was done previously and is the evidence that this works.

**A5's 650 rows carry 155 distinct leading tokens**, and its head is itself clustered:

```
find 56 · cross 55 · invoke 24 · market 18 · historical 15 · consolidation 14
ec2 12 · exec 11 · gldinc 11 · CloudWatchLogs 11 · daily 10 · infrastructure 10 · github 10
```

Those read like real product and pipeline names. **A realistic guess is a few dozen genuine
decisions in A5, not 650** -- but that is a GUESS and sub-clustering A5 is the first hour of work.

## 4. RECOMMENDED ORDER OF WORK

1. **Confirm or reject the four family rules (A1-A4).** Four judgements, 469 rows. If they hold,
   42% of the population is answered before lunch.
2. **Sub-cluster A5 by its 155 leading tokens into product/pipeline families.** This is the only
   genuinely unknown part and the only part that needs your knowledge of the business.
3. **Write the registry rows** for each family into `infra/logic/registry/` (which of the 6 files
   depends on the family -- `systems.json` for most).
4. **Re-run the checker and watch the number fall.** The population is re-derivable in one command
   (see §6), so progress is measurable after every batch rather than at the end.

## 5. THE 15 ROWS THAT ARE NOT THIS JOB AT ALL -- HAND THESE TO ENGINEERING

Separate from everything above, **15 rows carry a literal template variable that is sitting in the
REAL name**, written by application source code at **4 files / 5 sites** -- `{dim_name}`, `{snap}`,
`{firm}`, `{d}`, `{dc}`. The checker never produced these; something is shipping resource names with
an unexpanded placeholder in them.

**AND 5 OF THE 15 ARE GRADED `CONFORMANT`** -- the checker says they are fine while a brace is still
standing in the name. **Do not do these by hand at a desk.** It is a code fix, it is small, and it is
the only thing in this whole population that is an actual defect rather than a missing decision.

## 6. THE FILES, AND HOW TO RE-DERIVE ANY NUMBER HERE

```
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/
    PLACEHOLDER_RESOLUTION_R18.json      <- 1,303 rows, each with current / tokens / reason / owner
    PLACEHOLDER_POPULATION_R13.json      <- token counts, the 5 producers with file:line, the
                                            "one cause or several" verdict
    PLACEHOLDER_POPULATION_TABLE_R13.md  <- the human-readable table
    NAMING_CENSUS_REPORT.r13.md          <- the source census (3,264 judged rows)
infra/logic/registry/                    <- the 6 files that need the new rows
lib/opal_naming.py                       <- the grader; :1187 is where {system} is emitted
```

Current state: **all 1,303 rows are `CARDED`, `resolved = 0`**, every one owned by `1.0.0_SA_CTO`.
Nothing has been decided and nothing has been lost.

## 7. WHAT "DONE" LOOKS LIKE

This work exists to close **`LGIC_ENFORCE` FWD-5**, whose own words are:

> *"Anyone can run the check over the whole estate and get the complete ranked list of names and
> addresses that break the pattern, each with its fix ... DONE WHEN EXERCISED."*

Today the check runs and produces the list. **It just cannot say what the correct form IS for these
rows, because the registry has no opinion about them.** Done = the run produces a ranked list where
every row is paired with a real name instead of a placeholder, and the totals agree with the
hand-made ranking.

## 8. WHAT NOT TO DO

- **Do not work the 1,303 rows individually.** That is the trap this number has set since round 13.
- **Do not hand-fix the 15 template-variable rows** -- route them to code.
- **Do not trust the row count as a decision count** in either direction, including mine: §3 is a
  clustering by LEADING TOKEN, which is a PROXY for "one decision" and not a measurement of it. It
  is good enough to plan from and not good enough to report as a decision count.

## 9. DECISIONS ONLY YOU CAN MAKE

1. **Are `bd` / `inf` / `cot` a `{system}`, or a firm dimension that the grammar should handle
   separately?** 217 rows turn on this one answer.
2. **Should an AWS service name ever be a `{system}`?** 175 rows, and the answer is probably "no,
   and the grader should say so differently" -- which would be a grader change, not registry rows.
3. **For log-group paths, does the `/aws/<svc>/` prefix get graded at all, or only its tail?** 67 rows.
4. **A5's families** -- nobody but you can say what `find`, `cross`, `market` or `gldinc` are.

---

**Sequencing note:** Andrew ruled 2026-09-21 ~00:55Z that the project seating this work comes
**after** MDPF_TAXSMA and NFRA_MCPINDEX. This brief is the input for that seat when it exists, and
for his own desk work tomorrow in the meantime. It changes no sequence and asks for no seat.
