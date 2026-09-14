# PRD REVIEW -- LGIC_NAMING v1.2 @d6e0c3b74a -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** `1.0.0_SA_CTO`, msg 96436. It was sent by hand because the notifier's requests do not land as inbox files (`LGIC_NAMING-S1`).
**Prior:** v1.1 SIGNED (sign-off `68ccb95f57`; review @`48eab96ed5`, whose addendum @`9a0cbd6bc9` revised correction 1).

**Read, UTC 2026-09-13 ~23:5xZ:**
- The PRD @`d6e0c3b74a`. The working copy is identical to the pin.
- A section-by-section diff against v1.1 @`b75a62552d`, run through `.tools/prd_signoff_lib.py`'s own `top_sections` parser -- the same sections the stamp hashes.
- `org/standards/NAMING_SCHEMA.json` @`d6e0c3b74a` against @`b75a62552d`, both parsed.

**Half hash reviewed:** ratified-text `2f54ae7edbee09c9ad4a1bb561043e5903998d6aad9b7ce546d2c43c9bf6b81f`. The stamp is pinned to
it with `--expect-half-hash`.

## VERDICT: SIGN -- both corrections landed as asked, and nothing else in the half moved

## THE WHOLE DIFF OF THIS HALF, v1.1 -> v1.2 (three lines)

| section | line | v1.1 | v1.2 | answers |
|---|---|---|---|---|
| ENDPOINT | FWD-5 SOURCE | `brief Part I O5; bar Part III O5` | `brief Part I O5` | correction 1, as revised @`9a0cbd6bc9` |
| ENDPOINT | FWD-6 SOURCE | `brief Part I O6; bar Part III O6` | `brief Part I O6` | correction 1, as revised |
| CONTRACTS | row 4 | `{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}` | the ruled `{source}/{scope}/{tier}/{table}/{partition}` verbatim, with the bucket named as the key's CONTAINER (never a segment) and `{object}` as the LEAF under `{partition}`, pointing at `key.container` and `key.leaf` | correction 2 |

**Nothing else in the half moved:**
- The endpoint's deviation qualifiers were NOT restored. That is correct, because the spine (`CANONICAL_FABRIC_WORKFLOW_20260901.md:165`) keeps history out of the section.
- The SOURCE lines of FWD-1 through FWD-4 are unchanged.
- The TITLE, DONE WHEN and ACCEPT lines are untouched, so v1.1's finding carries: 6 of 6 outcomes verbatim against the endpoint @`e2210bf34c`.
- CONTRACTS rows 1-3 are unchanged.

The ruled five-segment string appears verbatim in CONTRACTS. It is Andrew's ruling @`998b3f0105`, card 1.

## THE DATA FILE ROW 4 NOW POINTS AT

This file is in neither half. It was checked only because row 4 names two of its fields.

`NAMING_SCHEMA.json` at v1.2:

| field | value |
|---|---|
| `key.grammar` | the five ruled segments |
| `key.ruled` | cites the ~03:2xZ card 1 |
| `key.container` | *"{bucket} -- the bucket that holds the key; NEVER a segment of the key"* |
| `key.leaf` | *"{object} -- the file under {partition}; not part of the ruled string"* |
| `key.full_address` | `s3://{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}` |

The top-level keys that changed are `changelog`, `key`, `ratified_by` and `version`, and nothing else. `LGIC_ENFORCE`'s `key()`
builder now has a field to read the container and the leaf from -- the exposure correction 2 named.

## CARRIED FROM v1.1, UNCHANGED

- **The counterpart is NOT EVALUATED:** `LGIC_ENFORCE`'s PRD does not exist.
- **CONTRACTS row 2 is NOT EVALUATED:** N2, the grading rule, is not yet written.

## NOT CLAIMED

- **The brief half.** Its S1 changed; it is `4.0.0_SA_CRO~D`'s to re-sign.
