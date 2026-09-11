# ASSETCLASS_TAXONOMY PRD v0.1 — L4-R ENDPOINT SIGN-OFF REVIEW

**Reviewer:** `3.0.0_SA_CVO~Z` · 2026-09-11 ~03:55Z · **Verdict: SIGNED**
**Artifact:** `docs/architecture/ASSETCLASS_TAXONOMY_PRD.md` v0.1 @`a08aa0efe7` (ancestor of HEAD, verified)
**Author:** `1.0.0_SA_CTO~Z` · **Directive:** D4 (site Z) · **Notifier:** msg 21149 (L4 → L5)
**Scope of this sign-off:** the ENDPOINT section (Rule 27 L4-R: *"`3.0.0_SA_CVO` signs the ENDPOINT
section against the ratified pins"*). The CRO's coverage-map half is `4.0.0_SA_CRO`'s and is not signed here.

---

## VERDICT: SIGNED. The endpoint is sound and I am not holding the COO's decomposition.

Six outcomes, each with a DONE WHEN state and an ACCEPT bar, confirmed by Andrew at his reserved L2 step
(s.5, verbatim: *"Confirmed, just note that Philosophy/CMA are the same page now. Also this should likely
be heavily involved with ETFClassifier."*).

### What I checked, and what passed

| check | result |
|---|---|
| **NO FWD IS A WAIT** (Rule 27) — each outcome provable by an act a seat can take ON DEMAND | ✅ 6 of 6. None depends on an event nobody controls. |
| **DONE WHEN vs its ACCEPT bar** — the bar must grade what the state claims | ✅ no mismatch that changes a grade |
| **A REAL DISCRIMINATOR EXISTS** — could the evidence differ if the claim were false | ✅ FWD-5 is the strongest; see below |
| **MECE over the declared domain, BY SUBTRACTION** | ✅ s.7 carries 6 of 6 outcomes on exactly one surface row each (S1: FWD-1/2/5; S2: FWD-3/4; S3: FWD-6) = 3+2+1 = 6, 0 uncovered |
| **The pins the endpoint rests on are actually PINNED** | ✅ s.3 fixes all five classes, their canonical ORDER (1–5) and their COLORS in a table, bound by C-FIVE-CLASSES |
| **Named referents exist** | ✅ both C-ONE-SOURCE modules are tracked; `class ETFClassifier` is real at `_shared/etf_classifications_dynamodb.py:49` |

⭐ **FWD-5 IS THE BEST-BUILT OUTCOME IN THIS ENDPOINT AND IT CARRIES ITS OWN NEGATIVE CONTROL:** *"someone
changed where a class boundary sits in the single source, and every place reflected it **without being
edited itself**."* That last clause is what makes it a discriminator rather than a description — a
per-place hand-edit satisfies a naive "everywhere agrees" bar and fails this one. Likewise FWD-1's *"none
in two, and none left over"* tests BOTH directions of the partition rather than only over-coverage.

⭐ **AND THE PRD DECLINED TO PRE-JUDGE ITS OWN LOAD-BEARING QUESTION, WHICH IS WHY I CAN SIGN IT.**
C-ONE-SOURCE names the expected home and then says: *"FWD-5's FIRST L5 investigation confirms that is the
source, or finds where it truly lives — it is NOT hard-pre-judged here."* s.8 sequences that as S1's first
cell. A PRD that had asserted the single source instead of scoping the question would have been refused
here, because the measurement below would have contradicted it.

---

## ⛔ THE MEASUREMENT I AM HANDING THE FIRST L5 CELL — "ONE PLACE" IS CURRENTLY FALSE

Measured at HEAD by this seat, with printed denominators. **This does NOT change the verdict** — the PRD
scoped exactly this question to FWD-5 — but the first cell should start from a fact rather than a search.

### `etf_classification.py` — THREE copies, and ALL THREE DIVERGE

| sha256 (12) | bytes | path |
|---|---|---|
| `a83b439d57ad` | 52,964 | `infra/aws/lambda/v2_portal/_shared/etf_classification.py` |
| `46ff867cd035` | 46,247 | `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classification.py` |
| `591967f14bf3` | 26,406 | `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-etf-returns/etf_classification.py` |

**Three distinct contents over a denominator of 3.** The `_shared` copy is roughly TWICE the size of the
`yang-generate-etf-returns` copy, so these are not a formatting drift — they carry different logic.
⛔ **CONSEQUENCE, STATED PLAINLY: editing `_shared/etf_classification.py` TODAY PROPAGATES TO NOTHING.**
The other two lambdas carry their own, different classifier. So **FWD-5 as written would FAIL against the
current estate, and it would be CORRECT to fail** — that is the outcome doing its job, not a defect.

### `etf_classifications_dynamodb.py` — THREE copies, ALL IDENTICAL

| sha256 (12) | bytes | paths |
|---|---|---|
| `c677e8a5f699` | 14,027 | `_shared/`, `yang_pipeline/positioning/yang-generate-holdings-attribution/`, `yang_pipeline/positioning/yang-generate-positioning/` |

One content over a denominator of 3 — a vendored copy that is **in sync today**.

⚠ **THE IDENTICAL CASE IS THE MORE DANGEROUS OF THE TWO, AND THE ORDER OF DANGER IS NOT OBVIOUS.** Three
divergent files announce themselves on any diff. Three byte-identical files look like a single source and
are one unreviewed edit away from silently becoming the divergent case — with nothing failing at the
moment of divergence. A vendored copy that happens to agree is not a single source; it is a single source
that has not been tested yet.

### Why this bears on FWD-6 as well as FWD-5

FWD-6 grades that the **two** surfaces (C-TWO-SURFACES: Positioning, and the combined Philosophy/CMA)
agree on classes, order and colors. The **identical** module is the one the two POSITIONING lambdas share;
the **divergent** copies sit in `partners` and `yang-generate-etf-returns`. So if the two surfaces read
different classifier lineages, **FWD-6 can fail for an upstream CLASSIFICATION reason that has nothing to
do with rendering**, and a reader would look for the bug in the views. Worth knowing before S3 is cut.

---

## NON-BLOCKING OBSERVATIONS, recorded rather than raised as defects

1. **FWD-3 and FWD-4 grade at APPLIED while FWD-6 grades the same observable content at EXERCISED over
   both surfaces.** Not a MECE violation — each outcome sits on exactly one surface row — but it means
   **FWD-3/FWD-4 reading APPLIED does not imply FWD-6 will pass.** FWD-6 is the discriminating grade for
   order and color; the other two can be satisfied per-site while the two sites still disagree.
2. **The flat PRD home is disclosed, not an error.** s.1 notes the PRD is authored at `docs/architecture/`
   under the flat convention this project is registered with. I raise it only because the L4-R signoff
   and stamp lanes are written for the TREE path (`org/missions/*/*/*/prd/{signoff,stamps}/**`), so the
   sidecars for this project land wherever the tool derives them for a flat PRD rather than under a
   tree `prd/` — a mechanics note for whoever reads the ladder, not a scope objection.
3. **Out-of-scope is explicit and I agree with each exclusion** (s.6): edge membership rules deferred to
   L5 by C-MEMBERSHIP-AT-L5, surface content beyond the breakdown, and the TAX SMA Teams thread deferred
   on Andrew's *"the transcript is fine for now"*.

---

## WHAT THIS SIGN-OFF DOES AND DOES NOT CERTIFY

**CERTIFIES:** that the ENDPOINT section's six outcomes are outcome-shaped, non-waiting, MECE over the
declared domain, discriminating, and resting on pins that are actually pinned in the document.

**DOES NOT CERTIFY:** that the classification single-source exists — it does not, today, and the PRD says
that is FWD-5's first investigation. Nor the membership rules at the class edges (C-MEMBERSHIP-AT-L5).
Nor the CRO's coverage map, which is a different reviewer's half.

— `3.0.0_SA_CVO~Z`
