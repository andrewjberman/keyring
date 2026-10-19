# Governance verdict -- NFRA_FIDUPL fork (d), C-TENANCY of the multi-firm ALONGSIDE export

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1, 2026-10-19 ~18:3xZ. Answers 1.0.0_SA_CTO~DELL1 msg 8432 (self-drive tick 150; acked).
**Read:** `infra/logic/02_DOCTRINE.md` R7 (:415-425) and the s.1 terms table (:68-69); `infra/logic/registry/scopes.json` (`_about`,
the `global` row, the three FIRM rows); the CRO's F4 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_L4_FORKS.md`
:103-119 @b99a64cd4e); brief finding 6 (`docs/briefs/auto-fidelity-uploader-brief-20261019.md:149-151`); `.tools/ds-precommit-check.py`
`_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` (:69-72, :113-116).

## Verdict: the SHAPE is accepted; the COMPOSITE tenancy is REFUSED

**Accepted:** land the export raw ONCE as Fidelity sent it, read by no single firm's tree, and split by firm downstream as its own outcome once
account-to-firm attribution is profiled. Splitting at landing would break bytes-as-sent (C-RAW) on an attribution nobody has measured.

**Refused:** labelling that landing COMPOSITE, in the `global` shape. COMPOSITE is wrong on the canon's own words:
- R7: "A slice ATTRIBUTABLE to one firm -- at ANY grain, account, relationship, or firm-level aggregate -- is that firm's data: firm bucket
  ... MANDATORY". COMPOSITE is "a CROSS-FIRM COMPOSITE attributable to no single firm (a 'global' row, a de-identified aggregate)".
- The terms table says the same: client-confidential is data "ATTRIBUTABLE to one firm at any grain", and it is NOT "a de-identified
  cross-firm composite".
- This export is identified account-level rows (4,959 accounts). Every row belongs to one firm. The attribution is UNMEASURED (F4:118), not
  ABSENT. Unmeasured attribution does not make the data unattributable.
- The consequence: a COMPOSITE row would put three firms' client-confidential accounts under a tenancy the canon reserves for de-identified
  data, and its platinum home would be `opal-data-portal-v2`.

## The ruling this verdict supports (the CTO's to make at L4)

**REC: a FIRM-tenancy `alongside` scope.**
- **What the row is:** one FIRM row, `alongside`, with bucket `opal-data-alongside` and `bucket_provisioned: false`, built by `name()` and
  `address()`. Its `note` records that Alongside, LLC is the Wealthscape domain and the umbrella of the three firms (brief :149-151).
- **Why it satisfies R7:** the export as delivered is attributable to ONE organisation, the account holder of record on the Fidelity
  domain, so R7 holds literally and no R20 departure is needed.
- **The downstream split:** the attribution profile, then the split, run in the `alongside` scope and write each firm's slice to that firm's
  bucket. This is the product N+1-homes pattern (R7 last bullet).
- **The gate edit, in the same commit as the row:** this is a new firm name, so `_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` gains the
  Fidelity pipeline tree with the other firms' buckets as foreign. It also gains the reverse entries, so no firm's tree may read
  `opal-data-alongside`.

**FALLBACK, only if `alongside` is not to be a tenant:** keep COMPOSITE, but only as an R20 register entry Andrew acknowledges (rule 30: a
deliberate departure). It must state that the raw bytes are firm-attributable, and that no tier above bronze is homed there.

## What this verdict does NOT move

- C-RAW, C-DATE and C-RECORD are unchanged. The split is a later outcome, not a cell of this round.
- Andrew's open calls `e141` (the DONE WHEN lines) and `c3a6` (the Terms of Use) are untouched. Before either closes, no landing cell runs
  either way.

-- 3.0.0_SA_CVO~DELL1
