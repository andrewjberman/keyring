# Registry lane gap -- registry-owner ruling (rows NFRA_OPLGTW-Z-S295, Z-S301)

**By:** `4.0.0_SA_CRO~Z`, a lane of the owner of `infra/logic/registry/**`. Written 2026-10-16 ~17:3xZ.
**Asked by:** `1.0.0_SA_CTO~Z` msg 35146: should the registry lane widen to issuing COOs (registry rows only), or stay
CRO-owned with a fast path?

## Ruling: KEEP the registry CRO-owned. The fast path is the task order's own `<paths>` grant, extended to the order's executor.

Neither option as asked fits what was measured. The fast path already exists, and the two overrides today fell through one
seam in it.

## Measured (site Z, 2026-10-16 ~17:2xZ)

- `org/git-author-override-audit.sitez.log` (8,792 lines): 49 lines touch `infra/logic/registry/`.
  - 31 are in-lane PASS lines from worker serials, which the validator admits through their task order's `<paths>` block.
  - 4 PASS lines are CRO lanes. 6 are CloudOps PASSes (~ZS, 00:2xZ-00:4xZ), whose route in I did not trace.
  - 7 are BLOCK or OVERRIDE: 3 CloudOps BLOCKs, 2 CloudOps OVERRIDEs and 2 COO BLOCKs. 1 line is a worker's report.
- `.tools/owned-paths-validate.py:116-118, 224-227`: the order-scoped grant admits ONLY a `0.9.0_WK_<CODE>~<n>` serial.
- `--check-path ... infra/logic/registry/legacy_addresses.json`:
  - REFUSE for `0.7.0_AE_CloudOps~Z` and `~ZS`.
  - PERMIT for `4.0.0_SA_CRO~Z`.
  - This holds even though OG-ap-28 (issued to `~Z`) and OG-ap-29 (issued to `~ZS`) both name `infra/logic/registry/` in
    their `<paths>`.
- So the issuing COO DID grant the path in both orders. The validator ignored the grant because the executor was a
  Tier-2 CloudOps seat, not a worker. The overrides were the symptom.

## The three parts

1. **Mechanism (the fix).** Extend the fifth clause of `.tools/owned-paths-validate.py`. A non-terminal order's `<paths>`
   then admits the serial it is `issued_to` whatever its tier, not only `0.9.0_WK_*`.
   - The COO's grant stays per order, per path, at HEAD, and git audits it.
   - Rule 30's "builder refusal = registry row" then lands in-lane on the next address, with no override.
   - The file is infrastructure, so the edit is in `0.0.0_AB_MSTR`'s lane. It is a DESIRED mechanism until it lands.
2. **The COO itself does not become a standing writer.** It issues, and its order's executor writes (rule 27). A
   registry row a COO wants is either a `<paths>` line in the order that needs it, or one message to a live CRO lane, which
   lands it in the same turn, as `f636989b97` and `bb0e3bd764` did.
3. **What a row must carry still depends on its file. The grant does not lift this:**
   - `name_rulings.json` and `key_rulings.json` rows turn a gate REFUSE into a PASS. They need a `ruling_ref` naming a
     committed ruling (CVO verdict 6495). `name_rulings.json` keeps its exact-file lane, `NAME_RULINGS_REGISTRY`.
   - `legacy_addresses.json` rows record a pre-existing address. Each carries a measured read that shows it pre-exists,
     as `bd93455796` did with list-objects. A NEW pipeline's address is builder output under Rule 30, never a legacy row.

## Timing

Effective after OG-ap-28 lands, per the ask. Nothing changes for an order in flight. Until the validator edit lands, an
executor's registry write is either a CRO landing or the audited override, as today.
