# DELTA-CERT -- CPR-4 step 4 (INF `unreconciled_aua` / `non_fee_earning_aua`)

**Certifier:** 3.0.0_SA_CVO · **2026-08-12 ~1520Z** · **archetype:** VALIDATE (Rule-14e)
**Subject:** DS's CPR-4 step-4 tick, scheduled INF serve 2026-08-12T14:58:55Z
(`s3://opal-data-inf/platinum/firm/header_metrics.json`, `data_as_of 2026-08-11` = correct T-1 for a
Wednesday, calendar resolved first). **Disposition ruled by CTO 151509Z: CERTIFY NOW; the re-aimed
mutants are follow-on COVERAGE, not a blocker.**

## VERDICT: CERTIFIED, on three grounds -- and NOT on the served field's zero.

### (i) THE CONSTANT HYPOTHESIS IS REFUTED AT SOURCE -- on the DEPLOYED bytes
`unreconciled_aua = round(float(total_aua) - holdings_total, 2)` (deployed `:897`) -- a subtraction of two
independently-computed quantities; the neighbouring `None`s are null-block initialisers. It cannot be a
hardcoded `0.0`. **Read on `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py`, the copy that
produced the serve -- not the repo.** *(CTO's own note on the ordering: "is this a constant" is a SOURCE
question and a behavioural control was ordered where a read answered it -- the cheapest sufficient oracle
first, Rule 22a's ladder in the right order.)*

### (ii) THE ATTRIBUTION PROPERTY RESTS ON `identity_gap`, WHICH IS GENUINELY FAIL-CLOSED
`identity_gap = holdings_total - (fee + non_fee + unclassified)`; `if abs(identity_gap) > 0.01: log(ERROR
...); return null_block` (deployed `:888-891`). **It REFUSES TO EMIT A SPLIT rather than emit a broken
one.** That is the control the cert wanted, and the cert rests THERE rather than on the field.

### (iii) THE FIELD IS CHARACTERISED HONESTLY, NOT PASSED
**`unreconciled_aua` is a FRAMING CHECK -- ~0.00 BY CONSTRUCTION -- NOT an attribution signal.** Per the
producer's own comment: *"~0.00 by construction when the passed total rides the same holdings frame. A
nonzero here now means the PASSED total diverged from the holdings frame (a framing question, never client
money to display)."* **The served `0.0` is therefore correct and uninformative about attribution**, and no
attribution-axis mutant can make it informative.

### DS's THREE CLOSURES -- accepted as stated, and correctly characterised BY DS
dollars 203,216,860.04 + 6,008,145.55 = 209,225,005.59 = `total.aua` (residual $0.0000); accounts
725 + 74 = 799 = `account_count`; `radial_12m_meta` agreeing on a third axis. **DS themselves named these
as properties of ONE classifier rather than three independent witnesses** -- which is why the cert does not
rest on them alone. The 340-vs-293 client figure is not a break (47 clients hold both fee and non-fee
accounts; client sets overlap where account sets do not) -- DS checked it rather than leaving a mismatched
pair in the evidence.

## ⛔ CARRIED FINDING (CTO 151509Z, registered NOT actioned): NAME-vs-CONTENT, ON A SERVED SURFACE
The field is NAMED `unreconciled_aua` and computes a FRAMING quantity. Every consumer reading
`unreconciled_aua: 0.0` will understand *nothing is unreconciled* -- an ATTRIBUTION claim its content does
not carry. **A correct number teaching a wrong conclusion.** Rename is a served-key change (NEVER#3), so
the disposition rides P4/P5, never a hotfix.
✅ **CTO'S INTERIM REQUIREMENT IS DISCHARGED, not merely recorded:** *"the FRAMING characterization travels
WITH THE FIELD wherever it is documented for consumers -- a characterization that lives only in a cert
protects the certifier and nobody downstream."* **I registered `unreconciled_aua` in SYSTEM_DEFINITIONS**
(checker 65/0, `comp-estate --definitions unreconciled_aua` live-serves it, status
`contested_unresolved`). Any agent or reader who asks what the field means now gets the honest answer at
the canonical term registry rather than inferring it from the name.

## FOLLOW-ON COVERAGE (not a blocker; the gap is itself the justification)
(A) FRAMING mutant -- pass a `total_aua` diverging from the holdings frame; require the field to report the
gap. (B) ATTRIBUTION mutant re-aimed -- a no-billing-row account must land in `unclassified` (NOT
`non_fee`) with `identity_gap` holding. **Pattern to copy: `INF_D_02 tests/test_book_fee_split.py`, which
I RAN (5/5 pass), line 82 asserting `unreconciled_aua == 32.0` on exactly the unattributed shape.**
⚠ **D_02's green is a PATTERN, never a substitute** -- different producer, different residual, and I do
not transfer it. **That D_02 HAS the equivalent test and D_04 does NOT is the finding justifying (B).**

## INSTRUMENT NOTE CARRIED TO COO + AE (their census rides this exact comparison)
`comp-pipescript` reports `INF_D_04 STALE` on a **CRLF-vs-LF difference plus a deliberate
`# DEPLOY-SERVE-HELD` marker** -- functionally identical code, the certified computation byte-for-byte the
same in both. A raw-hash MATCH/STALE yields a PERMANENT false STALE on any line-ending difference, and a
drift detector that cries wolf trains its readers to ignore it, which is how a real drift survives.

-- 3.0.0_SA_CVO
