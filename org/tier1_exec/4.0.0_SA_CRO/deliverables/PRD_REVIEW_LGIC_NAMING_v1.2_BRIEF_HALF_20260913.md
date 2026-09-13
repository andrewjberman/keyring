# PRD REVIEW -- LGIC_NAMING v1.2 @d6e0c3b74a -- the BRIEF half (L4-R, spine v3.15) -- 4.0.0_SA_CRO~D

**archetype:** VALIDATE
**Reviewer:** `4.0.0_SA_CRO~D`. **Prior:** v1.1 SIGNED (`@98ff34e45f`); v1.0 REFUSED (`@1e4e3e10fd`).
**Read:** `git diff b75a62552d d6e0c3b74a` on the PRD (12 lines) and `org/standards/NAMING_SCHEMA.json` (13 lines) in full --
the diff, not the CTO's description. UTC 2026-09-13 ~23:5xZ.

## VERDICT: SIGN

### What moved in the brief half: S1 only, and it is a correction in the brief's favour
v1.1's S1 wrote the key as `{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}` -- one string with the
container and the leaf folded into it. That was my brief's own IV.2 line, carried forward. The ruling (~03:2xZ card 1)
was the FIVE segments `{source}/{scope}/{tier}/{table}/{partition}`, the same in every bucket; the bucket is where the
key lives, not part of it, and the object is the file under the partition. v1.2's S1 says exactly that, and the data
file separates `key.grammar` (the ruled five), `key.container`, `key.leaf`, `key.full_address`. **This is the right cut
for the consumer:** `LGIC_ENFORCE`'s `key()` must never write a bucket name INTO a key -- the fold I wrote would have
let it. The CVO's correction (its review `@48eab96ed5`) is taken; I concur.

### Everything else in the brief half: byte-identical to v1.1
S2-S13, PROJECT ARC, CELL CANDIDATES, PATHS, BRIEF COVERAGE, SURFACE MANIFEST -- per the diff, no line in them changed
(the two SOURCE-line edits and the CONTRACTS row 4 edit are the CVO's half). The signature at v1.1 carries to them.

### An L1 debt this surfaces on MY surfaces, not a condition of this signature
`docs/briefs/d14-naming-schema-brief-20260913.md` IV.2 and `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md`
IV.5 both write the folded seven-segment form. The PRD is now the authority and says which is the key; the briefs are
history and a later reader could copy the folded line. A one-line touch to each ("the ruled string is the five
segments; bucket = container, object = leaf; see LGIC_NAMING_PRD S1") is owed at L1 and is not blocking -- the PRD's
brief_ref pins `@1b42dbe758` and the endpoint's outcomes did not move.
