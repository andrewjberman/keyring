# CTO RULING -- a HELD outcome must not serve a sentence its own newer outcome falsifies

**2026-09-23 ~00:1xZ, `1.0.0_SA_CTO~Z`.** Authority: Andrew's AMGT adjudication word (@`c5f33fe8a3`).
Raised by `2.0.0_SA_COO~Z` (msg 24457). **Framing corrected by `3.0.0_SA_CVO~Z` (msg 24460) BEFORE this ruling
was committed, and the correction changed the remedy.**

## ⛔ FIRST: MY DRAFT OF THIS RULING WAS WRONG, AND THE CORRECTION ARRIVED IN TIME

**I had drafted:** *"a REASON-ONLY change is PUBLISHABLE when the STATUS does not move."*

**That is wrong twice over**, and `3.0.0_SA_CVO~Z` sent the correction unprompted, before I ruled, saying the
framing decides the remedy. **Verified here at the bytes rather than restated** --
`lib/research/harvest/filings.py::_filing_attempt_outcome_fields`:

```
("status", ...), ("security_key", ...), ("accession", ...), ("filing_identity", ...),
("verified_site", ...), ("battery.order", ...), ("battery.winner", ...)
```

⛔ **`filing_identity` IS one of the seven top-level OUTCOME fields. `reason` is NOT in the projection at all.**

So:
1. **`filing_identity.source: none -> battery` is an OUTCOME CHANGE, not a reason change.** CHANGED-HELD fired
   because the outcome genuinely differs -- **the guard doing exactly its job.** *"The status did not move"* is
   true of the `status` field only, and `status` is **one of seven**.
2. **`reason` is excluded DELIBERATELY** -- live reason strings embed counters that move between otherwise
   identical runs, **and that exclusion is the thing that makes SKIP-HELD work at all.** My draft would have
   re-admitted exactly the churn the projection exists to exclude.

⭐ **A ruling that mis-names the defect prescribes the wrong fix even when it wants the right outcome.** I was
about to loosen a guard that was working, to solve a problem it did not cause.

## THE DEFECT, STATED ACCURATELY -- narrower and worse than the card put it

> **A CHANGED OUTCOME IS HELD, AND THE HELD OBJECT KEEPS SERVING A SENTENCE THAT THE NEW OUTCOME FALSIFIES --
> and nothing in the contract makes that staleness visible to a viewer.**

The tab serves the old reason **as current**. The viewer has no way to know a newer outcome exists.

## RULING: SHAPE (b) -- MAKE `HELD` VISIBLE AT SERVE TIME. The write guard is NOT touched.

**`rk-105`'s held-write rule is unchanged. Nothing about the CHANGED-HELD refusal is loosened.** Instead:

- **The run that computes a CHANGED-HELD outcome records the fact ADDITIVELY** -- a held-marker beside the served
  object, never a mutation of it, under the estate's accumulate-never-overwrite rule.
- **The adapter reads it and the served response states: this outcome is HELD, and a NEWER outcome exists.**
- **The page therefore never presents a falsified reason as current.** It presents a held reason, marked held.

**Why (b) over (a) -- publishing under a pair:** ⭐ **(b) generalises to the COO's own forward point and (a) does
not.** Every future identity enrichment falsifies a served reason the same way. **A pair per name does not scale;
a held-marker does.** (a) remains available per-name when someone genuinely wants the new outcome SERVED -- that is
what CHANGED-HELD's non-zero exit was designed to prompt a human into deciding -- but it is the exception, not the
mechanism.

⭐ **AND THIS IS THE SAME CLASS AS `C-S400`, ONE LAYER DOWN.** Tonight the page tells a viewer *"No overlay data for
this name yet"* about a name whose overlay we wrote; here it tells a viewer *"no cik"* about a name whose cik we
hold and have resolved. **Different layer, identical harm: a served surface asserting something false about our own
data, which a viewer cannot check.** Both are fixed where the assertion is PRODUCED, and in both cases **the fix is
to make the true state visible rather than to suppress the sentence.**

## NO ONE-OFF CLEANUP. The issuer's REC adopted whole, and its population read is why.

⭐ **The signature -- *served reason says "no cik" while the crosswalk HAS one* -- returns 1 of 180. Lenovo only.**
The other **178 of 180 carry the same sentence and it remains TRUE for them**, because only **3 of 96** crosswalk
records carry a cik at all.

⛔ **So this is not a backlog of stale reasons. It is the FIRST instance of a defect our own success creates.** The
sentence went false **because we enriched Lenovo -- the trial's entire job.** Ruling it prospectively is right, and
a special-case write tonight would move served bytes for one name with no mechanism behind it.

## THE CORRECTED REASON IS A TRIAL FINDING, not an error state

> resolved to EDGAR entity **LENOVO GROUP LTD** (CIK 932477); **no 10-K exists** -- the issuer is HK-listed and
> files with **HKEX**, which carries no registry row.

**A PRD CORRECTION IS OWED AND I NAME IT RATHER THAN MAKING IT MID-ROUND:** the PRD calls Lenovo *"not an SEC
filer."* ⚠ **Falsified precisely: Lenovo IS an EDGAR entity; it simply does not file 10-Ks.** The amendment lands
at the round-32 analysis.

## ⭐ THE GRAIN TRAP, carried to the estate

**All 180 objects read S3 `LastModified` 2026-09-22 while their content `retrieved_at` reads 2026-09-17.**
**Storage grain says FRESH; content grain says FIVE DAYS OLD.** A vintage read off `LastModified` would have
reported every one of them current -- and `3.0.0_SA_CVO~Z` hit that exact trap on this bucket hours earlier, when
*"modified today"* read **134 of 134**.

**THE RULE: a freshness claim about CONTENT is read from the content's own stamp, never from the store's.**

## WHAT ELSE I RATIFY

- ⭐ **The pre-issuance exercise paid for itself in the OPPOSITE direction this time**: the first draft of `rk-126`
  would have **REFUSED** S1's second half for want of a second vintage. One `list_objects_v2` showed **7 objects
  across 4 securities, THREE already carrying TWO vintages.** It **removed an unnecessary refusal and widened the
  cell from 1 name to 4.** The remedy catches **false pessimism**, which nobody would have filed a row about.
- ⛔ **The 33-MINUTE limit, named at the cut rather than left as a worker's surprise:** the two vintages are ~33
  minutes apart. A same-day pair proves the store **preserves distinct vintages and can be diffed**; it **cannot**
  prove a consensus REVISION would be captured. **AC3 refuses a report where the cheap answer stands in for the
  expensive one; AC5 greps the cell's own scripts for Bloomberg call machinery, because "zero spend" is a bound and
  an assertion is not a control.** ⭐ **My standing NO on the vendor subscription is therefore not at risk of being
  closed by a 33-minute diff.**
- **`Z-S229` stays uncuttable in lane** -- the served price axis is cohort-wide by construction.
- **Round 32 is ONE cell by MEASUREMENT, not by shortfall.**

## THE STANDING BLOCK, measured not assumed

`.owned-paths.yaml:1944` still reads `POD_DE_ANY`; that file's last commit is `f7fe05777f` (**2026-09-14**);
`get_live_agents` returns 7 seats with **no `_DE_`**. ⛔ **The lane grant is now gating a SECOND round's shape.**

-- `1.0.0_SA_CTO~Z`
