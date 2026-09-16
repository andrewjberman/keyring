# POSN_ASTTAX v0.10 ratified-text review - SIGN

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO~W`. Deliveries: 22974 and reconciliation 22976, from `1.0.0_SA_CTO~Z`.
PRD: `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md@59113e257a576d2ecfe463f736ce1a9cb92e1258`.
Reviewed half hash: `809d97ea1596ac2b3affd00e7877b0b38a2562adbf600f56bef6aaba03a95ab9`.

## Verdict and disposition

SIGN. All three ratified-text corrections in this seat's v0.9 review (`POSN_ASTTAX_V09_RATIFIED_TEXT_REVIEW_20260915_W.md@654fac2062`, refusal stamp `27a54b7550`) are satisfied at this pin:

1. The provenance parenthetical formerly at v0.9 line 300 is absent from the entire ENDPOINT section. The complete section, from its heading through the separator before the next heading (v0.10 lines 290-354), was read. The addendum retains the provenance outside it; no new annotation or seat name remains inside.
2. FWD-6 DONE WHEN (lines 332-336) now states the operative presence rule: only the five canonical classes, common order and colour for classes shared across modes, and display only where a book in the view holds the class. This matches Andrew's recorded absence-of-class instruction at `ANDREW_DIRECT_20260915_021xZ_ZERO_CLASS_ROWS_HIDDEN_AND_SATELLITES_HOLDINGS_BREAKDOWN_EMPTY.md@65410eedaf`, read in the prior review. The v0.10 addendum explicitly supersedes the former brief-half grading gloss; no alternate DONE WHEN is needed outside the endpoint.
3. FWD-7 DONE WHEN and ACCEPT (lines 343-350) now define availability per measure and ticker. A priced holding no longer implies every measure exists. The addendum discloses Bloomberg `active`/`credit` NULLs, CASH NULLs, the return-rule difference, and the new GLD return path. The latest addendum governs the earlier GLD gap wording. These are source and method constraints for subsequent execution; this signature does not claim that the producer or UI has delivered them.

## Scope and checks

Read the complete v0.9-to-v0.10 file diff and v0.10 addendum, the complete bound ENDPOINT, the exact follow-up message, and the newly cited vendor-approval record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_030xZ_BBG_ETF_PULL_RETURN_FIELDS_VENDOR_CHANGE_APPROVED.md@365580f244`. The pinned original brief and the earlier ratification records were already read in this seat's v0.9 review and remain its basis; no unchanged historical section was re-adjudicated.

The new vendor record quotes Andrew, verbatim: "vendor change approved go get it". It is a record of a word received at CTO~Z, not a fresh instruction issued by this reviewer. The CTO's reconciliation 22976 names the resulting backfill evidence; that live delivery is not independently certified here.

Direct outcome-block comparison against `8eabf98d81` matches FWD-1 through FWD-5 (5/5, stripping only surrounding block whitespace). Only FWD-6 and FWD-7 change; both retain EXERCISED. All seven identifiers remain in order, with no additions or renumbering. FWD-3/FWD-4 remain APPLIED; no PROOF field is added or changed.

Canonical `prd_signoff_lib.top_sections` identifies one ratified section, ENDPOINT, and no CONTRACTS section. No counterpart contract obligation is introduced by this delta. `half_hashes` reproduces the full delivery hash above, which also matched HEAD at measurement. Stamp with `--expect-half-hash` so concurrent unreviewed changes are refused.

This is acceptance of the ratified-text half only. Brief coverage and the producer/import/schedule details remain the brief reviewer's half. Implementation grades, task issuance, deployment and promotion are separate acts. The v0.9 refusal remains an accurate record of the old bytes; this signature accepts the corrected bytes. Reconciliation 22976 assigns this half to the routed W reviewer, with the Z reviewer asked not to stamp concurrently.

## Compiler Tools

| Tool | Result |
|---|---|
| comp-which / comp-read | Routed and indexed exact message/PRD inspections; complete section and pinned diff reads supplied the evidence beyond the excerpts. |
| prd_signoff_lib | Reproduced reviewed/HEAD hash, 7 outcome identifiers, 5/5 unchanged blocks, one ratified section; removed annotation absent. |
| prd-signoff.py status | Initially v0.10 WITHHELD, both halves STALE; ratified-text owed by CVO~W. Final status is measured after stamping. |

## What you should have asked but did not

The new per-measure rule resolves the text contradiction without declaring every cell filled. Later acceptance must compare each cell with its actual source availability and disclosed method, including legitimate NULLs.

## Push state

LOCAL. No push. Measured origin/SITEZ: `6f09a06dc919bf21ef96b52aff5cd7e9608ccf85`.

-- 3.0.0_SA_CVO~W
