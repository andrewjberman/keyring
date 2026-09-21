# ANDREW-DIRECT 2026-09-21 ~16:3xZ -- four /open-calls at 4.0.0_SA_CRO, ALL RECS APPROVED

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Channel:** Andrew at the 4.0.0_SA_CRO terminal, answering `/open-calls` run at this seat.
**Time:** ~16:3xZ 2026-09-21 (UTC read at record time: 2026-09-21T16:31:03Z).

## His word, VERBATIM AND ENTIRE

> "All recs approved"

## What he approved -- the four cards as printed to him (verbatim)

```
+-- CALL 1 of 4 -----------------------------------------------------+
  **AMGT R4 doctrine draft: (a) start it now, or (b) hold it until IRPT is done?**
  MSTR~Z relay 99081: AMGT_RESAPP rk-32 + chain P (5 cells) have been held 2.5 days
  on an R4 narrowing + tenancy change + R20 entry in infra/logic/**, which only laptop
  CRO lanes can write. Your ~12:37Z word: "Everything else can wait."
  --------------------------------------------------------------------
  **REC --** (a) draft now. The job is text only, uses no pipeline or worker time, and
  keeps nothing from IRPT. Nothing lands until you approve the exact wording on its
  own card.
+---------------------------------------------------------------------+

+-- CALL 2 of 4 -----------------------------------------------------+
  **Are `bd` / `inf` / `cot` a {system}, or a firm field handled separately? (217 rows)**
  From the registry-assigning brief s.9.1 (docs/briefs/lgic-enforce-registry-assigning-
  brief-20260921.md). This is the largest one-decision group among the 1,303 rows.
  --------------------------------------------------------------------
  **REC --** A firm field, not a {system}. A firm is already its own axis in the
  naming canon (firm-owned tiers live in the firm's bucket). Reading it as a system
  names one thing twice.
+---------------------------------------------------------------------+

+-- CALL 3 of 4 -----------------------------------------------------+
  **Should an AWS service name ever count as a {system}? (175 rows)**
  From brief s.9.2, e.g. `cloudfront-high-error-rate`. If the answer is no, the fix
  is a change to the checker (grader), not new registry rows.
  --------------------------------------------------------------------
  **REC --** No. The service name says what the resource runs on, not which business
  system it serves. The checker should give these their own verdict rather than
  failing them against the registry.
+---------------------------------------------------------------------+

+-- CALL 4 of 4 -----------------------------------------------------+
  **Log-group paths: check only the part after `/aws/<svc>/`? (67 rows)**
  From brief s.9.3, e.g. `/aws/lambda/access-anomaly-scanner`.
  --------------------------------------------------------------------
  **REC --** Yes, only the part after the prefix. AWS requires that prefix and we
  can't rename it, so checking it can only ever produce findings nobody can fix.
+---------------------------------------------------------------------+
```

## Rulings as they now stand

1. **AMGT R4 draft: (a) START NOW.** 4.0.0_SA_CRO drafts the R4 narrowing + new tiers.json tenancy + R20
   entry (relay 99081). **Landing is NOT approved by this word** -- the card said the exact wording comes
   back to him on its own card first. This is a narrow exception to his ~12:37Z IRPT-priority word for a
   text-only act, and it is scoped exactly to that; it moves no worker, seat or compute onto AMGT.
2. **`bd` / `inf` / `cot` are a FIRM field, not a `{system}`.** (217 rows, brief family A1.)
3. **An AWS service name is NEVER a `{system}`.** The checker gives these their own verdict instead of
   failing them against the registry -- a grader change, not registry rows. (175 rows, family A3.)
4. **Log-group paths: only the part after `/aws/<svc>/` is graded.** (67 rows, family A2.)

## Scope notes (surfaced, not adjudicated)

- Rulings 2-4 are NAMING LAW. The 98867 relay recorded "1.0.0_SA_CTO decides, 4.0.0_SA_CRO writes" for this
  population; Andrew has now decided these three himself, so the CTO does not re-decide them.
- The 98867 sequencing ruling (the project seating this work comes after MDPF_TAXSMA and NFRA_MCPINDEX)
  is NOT changed by this word. Andrew asked this seat directly to look into and remediate the
  population; that is desk work at this seat, not a seated COO project.
- Ruling 3 implies a change to `lib/opal_naming.py` (the grader), which is not in this seat's
  `infra/logic/**` lane. Who writes that change is not decided here.
- Brief family A4 (10 `opal*` rows) was in the brief's "four rules" and was NOT among these calls.
  Family A5 (650 rows) is the fifth decision and comes back as its own card after sub-clustering.

## Addendum ~17:2xZ -- second /open-calls round: CALLS 2 and 3 APPROVED, CALL 1 SENT BACK FOR DETAIL

Cards put to him (verbatim calls): CALL 1 *"Firm-pipeline resources (~300 rows ...): (a) name each one's system in
the registry, or (b) let a firm-scoped name drop the {system} slot entirely?"*; CALL 2 *"Approve the 19 system
groups in the recount's s.4 table as the owner mapping, including ~10 NEW system keys (news, market, cloudops, find,
...)?"*; CALL 3 *"Does ruling 3 also cover inline policy names (CloudWatchLogs, S3Access, invoke-*: 79 rows) and
library Lambda layers (pandas: 5)?"*

His answer, VERBATIM AND ENTIRE:

> "Im good with your rec on calls 2 and 3. Regarding call 1, need more detail exactly. I think you would need to
> include both vendor and firm in the nomenclature for these things, not picking one or the other."

**Reading, narrow:**
- CALL 2 APPROVED: the 19 families in `LGIC_PLACEHOLDER_RECOUNT_AND_A5_FAMILIES_20260921.md` s.4 as the owner
  mapping, the new system keys included; registry rows written in batches, census re-run after each.
- CALL 3 APPROVED: ruling 3 extends to inline/console policy names (79 rows) and library-named Lambda layers (5).
- CALL 1 OPEN: he wants more detail, and gives a direction -- the name carries BOTH vendor and firm. Not a ruling
  between (a) and (b); the card comes back to him.

## CORRECTION ~17:1xZ -- rulings 2 and 4 move ZERO rows; the cards that produced them were built wrong

**By 4.0.0_SA_CRO, against its own cards. The rulings STAND as his words; what was wrong is the row counts this
seat attached to them.** Measured at `lib/opal_naming.py` @`0f1caafb1d`, read at the bytes by this seat:

- **Ruling 4 (log groups graded after `/aws/<svc>/` only) is ALREADY the grader's behavior.** `_grade_log_group`
  `:1335-1341` strips `/aws/<service>/` and grades only the tail. The 67 rows carry `{system}` because the TAIL has
  none (`/aws/lambda/access-anomaly-scanner` -> `/aws/lambda/{system}-access-anomaly-scanner-lambda`). CALL 4 said
  "67 rows"; the ruling settles 0. Those rows fold into the other families by their tail.
- **Ruling 2 (bd / inf / cot are a firm field, not a {system}) is ALREADY the grader's behavior.** `:1210-1212` puts
  `bd` in the SCOPE slot; the 217 rows are `{system}` because nothing says WHICH SYSTEM a firm-pipeline resource
  belongs to (`bd-gold-qa-runner-forgotten` -> `{system}-49f-gold-qa-runner-forgotten-alarm`). CALL 2 said "217 rows
  turn on this one answer"; the ruling settles 0 of them.
- **Ruling 3 (an AWS service name is never a {system}) is the only one that moves rows as written** -- 174 at HEAD,
  and it needs a grader change plus a new verdict value (a schema change) outside this seat's lane.

**How it happened:** this seat carried the brief's s.9 framing onto the cards without reading the grader the brief
names. The brief put those questions as open; the code had answered two of them already. The recount
(`deliverables/LGIC_PLACEHOLDER_RECOUNT_AND_A5_FAMILIES_20260921.md`) found it; this seat then read `:1180-1214` and
`:1316-1345` itself before writing this correction.

## Addendum ~16:4xZ -- the R4 draft text APPROVED for landing

Card put to him (verbatim): *"Land the R4 draft as written @2d07cf1bcc: yes / no?"* -- the draft
`org/tier1_exec/4.0.0_SA_CRO/drafts/R4_NARROWING_GENERAL_TENANCY_DRAFT_20260921.md`, REC yes.

His answer, VERBATIM AND ENTIRE:

> "Yes do it"

**Reading, narrow:** land EDITS A-C of the draft as written (R4 narrowed + R8 + the pattern table in
`02_DOCTRINE.md`; the GENERAL tenancy in `tiers.json`; the `harvest` row in `scopes.json`), and no R20
entry (draft s.3). The draft's open questions -- whether `mdpf`/`etfs`/`global` bronze and silver are
custodial, and what "custodial" covers -- are NOT answered by this word.
