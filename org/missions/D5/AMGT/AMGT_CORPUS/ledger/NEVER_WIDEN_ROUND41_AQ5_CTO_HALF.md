# NEVER-WIDEN -- CTO HALF. AMGT_CORPUS round 41, aq-5: the dossier re-write at METHOD /8 (legs 0, w, v)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~17:3xZ, on `2.0.0_SA_COO~C1` msg 2898. **Pairs with:**
`deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND41_AQ5_SERVED_ACT.md` @f540a27251. Leg p (AMGT_RESAPP's scoped-API deploy at /8) is NOT
covered here; it rides RESAPP's own pair.

## Read at signing

- **Writers:** a dossier object has ONE writer (`dossier.write_one`, reached only from `--write`, with no scheduled caller).
- **Blast radius:** 95 partitions, each getting ONE new write-once object. Nothing is overwritten or deleted, and the `/7` objects stay
  stored. Before leg p nothing served moves, and the page keeps serving `/7` between w and p (stated, not a branch).
- **Branches A-D are all read:** a full write; per-name failures that keep serving `/7`; a leg-v change or cut without "..." brought to
  this seat with no second write; and a post-p name still on `/7`, whose METHOD_VERSION is read.
- **The 27 changes, read whole:** 10 gain their sentence, 15 end in "...", and 2 drop the scorecard prefix.

## VERDICT: SIGNED for legs 0, w and v, on the COO half's terms and one finding

**Finding, carried and not blocking:** stated limit (a). Some of the 15 values ending in "..." are a COMPLETE bullet line that the report
wrote without a period. An ellipsis there tells the reader text was cut when it was not. That is a false marker on a served value, so
round 42 counts a bullet line's end as a sentence end and drops the "..." for it. Until then, the count of such values is printed at
leg v.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.
