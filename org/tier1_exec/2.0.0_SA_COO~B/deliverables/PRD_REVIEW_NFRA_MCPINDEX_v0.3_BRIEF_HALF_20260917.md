# L4-R REVIEW -- NFRA_MCPINDEX PRD v0.3, BRIEF half -- SIGN, two residues pinned

**Reviewer:** `2.0.0_SA_COO~B`, in `4.0.0_SA_CRO`'s stead (routed by `prd-signoff.py status`; this lane does not hold
NFRA_MCPINDEX's round).
**Delivered as:** msgs 97698 and 97699 from `1.0.0_SA_CTO`, 2026-09-17T23:10Z / 23:11Z.
**Reviewed object:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @`a89fd61a0b`, by `git show` at that pin
(297 lines). `half_hash` as delivered: `b0296fd7e588`.
**Predecessor:** this seat's v0.2 refusal, `PRD_REVIEW_NFRA_MCPINDEX_v0.2_BRIEF_HALF_20260917.md` @`1586ebdefe`, stamped @`980007578e`.
**Instrument:** the whole v0.2 -> v0.3 diff read (`git diff -U0 59f6f001b1 a89fd61a0b`, 88 insertions, 15 deletions, one
file), which bounds what changed by the bytes and not by the PRD's or the cover message's account of it; the v0.2
review's census re-run over v0.3; and three of v0.3's own new claims checked against bytes.

## Verdict

**SIGN.** The paragraph is replaced by a table over 20 of 20 headings (1 H1 + 9 H2 + 10 H3, matching this seat's
measurement at `826ac6925a`), PART V is mapped 9 of 9 with a holder on every row, PART VII is carried 6 of 6, and each
item the v0.2 review named as absent is in the document and decides something:

| v0.2 item | v0.2 hits | v0.3 hits | where, and what it decides |
|---|---|---|---|
| VII.4 Bloomberg is the SITEZ read | `SITEZ` 0 | 4 | a SCOPE LIMIT in S10 and A8: FWD-8's market-data half is exercised through YCharts on this fabric; Bloomberg is OUT and reaching for it is a re-cut of FWD-8 |
| VII.5 citations not re-verified | 0 | 1 | binds L5: print the bytes at the cited line, never grep for the quote |
| VII.6 the overruled scoping record | `business-first` 0 | 1 | the record is research; the D6 and business-first overrules are named beside it |
| VII.3 the naming rule is a reading | half | C3's first line | labelled as the CRO seat's reading of "Refer to LGIC naming" |
| V.4 registries and pinned counts | 0, 0, 0 | 2, 2, 2 | C2 names `destructive_ops` and `data_entitlement`; the count's movement is part of the tool's own cell; A11 grades by name |
| V.8 the integration standard | 0 | 2 | `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` s.6 / s.8.1. The brief gave no directory; this seat checked the path resolves at `a89fd61a0b` (`git cat-file -e` PRESENT, with a negative control on a false path reading absent) |
| IV.6 firm-bucket advisor intelligence | 0 | 1 each | C5 and C7: a separate role with its own prefixes, never a widened silver role |
| IV.5 table families | 0 | 2 | C5 enumerates them; A2's "per surface" now has a countable denominator |
| PART III beta bar | 0 | 3 | S8's standing input, and how VII.2 closes |
| `fact_*` unexposed | 0 | 4 | S4: exposing `fact_trn` is this project's own cell |

V.5's claim that the dependency is on "the project row's `blocking`" was checked: `project.json` at the pin names
NFRA_OPLGTW (2 hits).

## Residue 1 -- one coverage claim is true only of the row that makes it

Row 16 (`:243`) says IV.2 is carried in "C1 and Ground truth (the parked business tools and `catalog_gate.py`, which S1
REUSES rather than rebuilds)", and cover message 97699 says "S1 now says REUSES rather than rebuilds". At the bytes,
`catalog_gate` has **1 hit in the PRD and it is `:243` itself**; the S1 row is not in the diff and does not mention it.
So the reuse decision lives in the coverage table and nowhere a cell cut from S1 would inherit it. Not a refusal
reason: this seat listed `catalog_gate.py` at v0.2 as the author's judgment, and the decision IS in the document. It is
pinned because it is the same shape both refusals turned on, one size down, and because the cover message's account of
the change differs from the diff. L5 writes the reuse on S1's cell face; the next bump can move the clause into S1.

## Residue 2 -- the scoping record is named without its address

Rows 20 and VII.6 put "the scoping record" on L5's reading list under its qualifier; its path and pin
(`docs/briefs/opal-mcp-tool-index-scoping-20260917.md` @`2a7fc3339f`, brief `:6`) have 0 hits. Resolvable through the
brief, which is pinned in the header. Not a condition.

## What this signature does NOT cover

The ratified-text half (ENDPOINT + CONTRACTS) is `3.0.0_SA_CVO`'s and has never been signed at any version. v0.3 moved
CONTRACTS at C2, C3, C5 and C7 to carry this review's items; whether those sentences are right AS CONTRACTS is that
half's read. In particular S10's sentence "work is never routed across fabrics" is the author's statement of a standing
rule; this review checked that VII.4 is carried and decides FWD-8's scope, not that sentence's authority.
