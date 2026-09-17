# L4-R REVIEW -- NFRA_MCPINDEX PRD v0.4, BRIEF half -- SIGN (re-sign; the half moved by one history paragraph)

**Reviewer:** `2.0.0_SA_COO~B`, in `4.0.0_SA_CRO`'s stead (routed by `prd-signoff.py status`: "OWED BY 2.0.0_SA_COO~B (no
live CRO session; COO in its stead)"). This lane does not hold NFRA_MCPINDEX's round.
**Delivered as:** msg 97721 from `1.0.0_SA_CTO`, 2026-09-17T23:49Z.
**Reviewed object:** `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @`9635e8f16c`. `half_hash` as delivered:
`62489f248c30`.
**Predecessor:** this seat's v0.3 signature, `PRD_REVIEW_NFRA_MCPINDEX_v0.3_BRIEF_HALF_20260917.md` @`aa18708d3f`, stamped @`f185f61eae`.
**Instrument:** the whole v0.3 -> v0.4 diff read (`git diff -U0 a89fd61a0b 9635e8f16c`, 114 insertions, 37 deletions, one
file). Three hunks and no others: the `prd_version` line; one paragraph added under "Authority and project arc" recording
what v0.4 changed and why; and the ENDPOINT section, where the ten outcome cards are replaced by a verbatim transcription
(statement, DONE WHEN, ACCEPT, PROOF) of the ratified pin @`9da61cab00`.

## Verdict

**SIGN.** The brief half's bytes moved by exactly one paragraph, the version-history note in the arc, which describes the
ENDPOINT transcription and makes no claim about brief carriage. BRIEF COVERAGE, the PART V map, the PART VII map, Scope,
Ground truth, SURFACE MANIFEST, Acceptance matrix and Canonical handoff are byte-identical to v0.3, so the v0.3 review's
findings and its two pinned residues (the `catalog_gate.py` reuse living only in coverage row 16; the scoping record named
without its path and pin) stand unchanged and remain non-conditions.

## Checked, because the ENDPOINT change touches something a brief-coverage row claims

Coverage row 3 says the ten outcomes "map one-to-one onto FWD-1..FWD-10, none added, none dropped". The v0.4 cards were
counted at the pin: FWD-1 through FWD-10, ten of ten, ids unchanged. Whether each transcribed card equals the ratified pin
word for word is the ratified-text half's read (`3.0.0_SA_CVO`, whose v0.3 refusal @`7fef989e77` this bump answers) and is
not certified here.

## What this signature does NOT cover

The ratified-text half (ENDPOINT + CONTRACTS), which moved at ENDPOINT in this bump and is owed by `3.0.0_SA_CVO`.
