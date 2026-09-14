# PRD REVIEW -- LGIC_ENFORCE v1.1 @78128f29ea -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier (msg 96513) and `1.0.0_SA_CTO` (msg 96515).
**Prior:** v1.0 REFUSED -- sign-off `bbfa9a28c8`, review @`06985bd8c0` (R1, R2 blocking; N1 non-blocking).

**Read, UTC 2026-09-14 ~06:0xZ:**
- The PRD @`78128f29ea`. The working copy is identical to the pin.
- A section-by-section diff against v1.0 @`1118c45aef`, run through `.tools/prd_signoff_lib.py`'s own `top_sections` parser.
- Every changed CONTRACTS line, read in full.
- Card 1 of Andrew's ~18:4xZ ruling record, for the conditions.

**Half hash reviewed:** ratified-text `8be10ad9c329ae3758e745f9dc82746ca79bd582c00dafa6d37b66a6d61bc6b0`, which matches the
hash 96515 states. The stamp is pinned to it with `--expect-half-hash`.

## VERDICT: SIGN -- R1, R2 and N1 are each answered, and nothing else in the half moved

## THE DIFF OF THIS HALF, v1.0 -> v1.1

**ENDPOINT is byte-unchanged,** so v1.0's finding carries: TITLE, DONE WHEN and ACCEPT are verbatim for 7 of 7
outcomes against the endpoint @`e2210bf34c`.

**CONTRACTS changed on four lines, and only those:**

| row | answers | v1.1 reads | against the source |
|---|---|---|---|
| the fence patterns | R1 | see the three clauses below | each condition is matched in the next table |
| the source-first key string | R2 | *"`key()` returns exactly it and nothing more, and `address()` composes the full address around it"* | the ruled five segments, verbatim |
| `lib/opal_naming.py` | R2 | `key(...)` returns exactly `{source}/{scope}/{tier}/{table}/{partition}`; `address(..., object=None)` returns `s3://{bucket}/{key}`, with the object as its leaf and the bucket from the tier home rule, never from an argument | one answer now, the same in both rows |
| `NAMING_SCHEMA.json` | N1 | the generator derives the registry-derived deny patterns from the schema, pointing to the fence row | agrees with `LGIC_NAMING` v1.2's row 1 |

**The fence row's three clauses:**
1. *"a Deny on every principal except two kinds: principals whose name carries that firm in its scope slot, and the principals the registry's exemption list names for that bucket. A principal whose name carries no firm is therefore denied unless it is named."*
2. *"The Deny lands only after every principal that reads or writes the bucket today holds a firm-scoped identity or a named exemption, under the never-widen sign-off."*
3. *"The exemption list, service principals included, is generated from the registry and never typed."*

**Card 1's three conditions against the row -- all present, none narrowed:**

| card 1 condition (verbatim) | where the row carries it | check |
|---|---|---|
| (1) *"decide explicitly what happens to roles that carry no firm token"* | clause 1: denied unless named | present, and decided |
| (2) *"every existing writer gets a firm-scoped identity or a named exemption before the new fence lands, under never-widen sign-off"* | clause 2 | present, and BROADER: it covers every principal that reads OR writes, not only writers |
| (3) *"the short list of AWS service exemptions is generated from the registry too"* | clause 3 | present, and it covers every exemption, service principals included |

The conditions sit in the CONTRACTS row, not in FWD-2's ACCEPT. v1.0's review offered that row as one of the two
places, and it keeps FWD-2's confirmed wording verbatim. They are stated in plain terms, with no history and no seat
name.

CONTRACTS rows 2 and 3, and the other produced rows, are unchanged.

## CARRIED, UNCHANGED

- **The counterpart:** `LGIC_NAMING` v1.2's rows 1-4 agree with this PRD's rows 1-4, with the intended direction flip on the registry rows.

## NOT CLAIMED

- **The brief half.** Its DEC-2, DEC-6, cells, paths, coverage and surface manifest moved in this bump; that half is `4.0.0_SA_CRO`'s.
- **DEC-4's mechanism,** which is not graded here.
