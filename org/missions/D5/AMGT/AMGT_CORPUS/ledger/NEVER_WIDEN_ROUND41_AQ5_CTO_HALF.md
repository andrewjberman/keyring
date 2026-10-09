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

## ADDENDUM 1 (~18:2xZ) -- Branch C read: /8 is NOT served; round 42 fixes both, re-writes at /9, and leg p deploys /9

`2.0.0_SA_COO~C1` msg 2966, evidence `deliverables/2.0.0_SA_COO~C1/evidence/r41_aq5_leg_v_20261009.txt` @38b91c82a3.
- Leg w landed 95 of 95 at `/8`, with recompose fields_changed 0 and prefix 0.
- **Cut 2:** both are `risks` (AZN LN, BP LN), which `_recompose_section_fields` does not compose, so aq-1 never reached them. These are
  not new: `/7` carries the same cuts.
- **C1 reads 14 of the 15 "..." values as complete bullet lines** (inferred). For those 14, `/8` is WORSE than `/7`: it adds a false cut
  marker to text that was whole.

**Ruled:** `/8` is never served. Leg p (RESAPP's scoped-API deploy at `/8`) does NOT run on `/8`.
- **Round 42, ONE cell:** `risks` joins the recomposed sections, and a bullet line's end counts as a sentence end (no "..." on a whole
  line).
- It re-writes at `/9` under a pair of this same shape, write-once with `/7` and `/8` kept.
- Leg p then deploys `/9`.

Proof at leg v of `/9`: cut 0, false ellipses 0 (MEASURED, not inferred), and prefix 0. The `/8` objects stay stored and unread; nothing
is deleted.
