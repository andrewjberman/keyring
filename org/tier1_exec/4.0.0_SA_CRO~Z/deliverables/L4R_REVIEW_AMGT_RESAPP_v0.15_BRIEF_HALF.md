# L4-R REVIEW -- AMGT_RESAPP PRD v0.15, BRIEF HALF -- verdict: SIGN

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`437e219264`,
v0.15, brief half hash `8992039f7cbc` (msg 24003). **Brief:** `docs/briefs/amgt-resapp-security-analysis-20260910.md`
@`19ce7d5b4d`, unchanged. **Prior act of this seat:** REFUSED v0.14's brief half (`6f979062c8`, review
`L4R_REVIEW_AMGT_RESAPP_v0.14_BRIEF_HALF.md` @`d61c888552`).

**Independence limit:** this seat authored the specification section 11 cites. Graded here: whether section 11 is
faithful to it and whether v0.14's refusal is discharged. The CONTRACTS additions (`:830-868`) are in the
ratified-text half, which is `3.0.0_SA_CVO~Z`'s to sign; they are read below only to confirm the refusal is discharged.

## Scope

`git diff -U0 c09b35ee5a 437e219264 -- <PRD>` gives five hunks: the version header (`:8`), the v0.15 change note
(`:204-211`), the six contracts appended to CONTRACTS (`:830-868`), and section 11 rewritten (`:1743-1771`). **No BRIEF
COVERAGE entry and no brief pin moved**, so the coverage and heading denominator signed at v0.13 (review @`8a788d2eaf`)
stand.

## v0.14's refusal: discharged

The correction asked for three bronze forms. `C-BRONZE-AS-RECEIVED` now carries them verbatim: (a) entity, (b)
immutable document, (c) request. The binding clause now points the right way: section 11 `:1752` says the contracts bind
over the plan, and the contracts now agree with the plan's s.5 bronze addresses. Both clarifications are taken: the
first fetch of never-kept bronze is in `C-FORMAT-SEQUENCE`, and the Lusha silver exception is in the section 11 open
items.

## Section 11 against the specification

| item | check | result |
|---|---|---|
| spec pin | `:1750` cites the plan @`d61c888552` | correct; that is the corrected plan |
| builder output, one per bronze form plus silver (`:1755-1759`) | compared with plan s.5.1, s.5.2 | 4 of 4 verbatim |
| "59 of 60, controls unmoved" | plan s.1 item 6, s.2 | faithful |
| live registry still prints `opal-data-assets` | re-measured in this seat's plan run; no tiers.json change on SITEZ since | faithful |
| laptop tenancy `1675a8f631` "not readable here" (`:1766`) | `git cat-file -t 1675a8f631` after `git fetch origin CLOUD`: `Not a valid object name` | **faithful, measured** |
| open items: rows, Lusha, table retirement | plan s.8 calls 2, 5, 6 | faithful |

## Two notes, neither a ground for refusal

1. **Platinum departs from this seat's plan, and that is correctly placed.** The plan put platinum in
   `opal-data-harvest` on Andrew's 09-18 ~21:45Z words (*"the whole pipeline will exist within opal-data-harvest"*).
   v0.15 follows the canon's R6 general home, `opal-data-portal-v2`, and `1.0.0_SA_CTO~Z` states in msg 24005 that it
   is surfacing that departure to Andrew. This seat does not adjudicate it. It gates nothing: platinum comes after the
   backfill. **Andrew's answer is the one item that could re-open this half.**
2. **`C-FORMAT-SEQUENCE`'s same-window rule overrode this seat's plan, and the rule is right.** Plan s.7 carried the
   09-18 order: dual-write for one cycle, and old prefixes kept until a census reads zero. That leaves a standing
   duplicate output path, which the shadow-pipeline veto forbids. The plan is corrected in the commit carrying this
   review, and section 11's pin (`d61c888552`) is one commit older than the correction. The contracts bind where the
   two disagree, so nothing is misstated. Re-pinning on a later bump is `1.0.0_SA_CTO~Z`'s call, and this seat's signature does not depend
   on it.
