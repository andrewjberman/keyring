# NEVER-WIDEN -- CTO HALF: `HVST-ch-5`, one version-2 DIVZ fund form (0 reports, an absent reason), round 93

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~04:0xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round93/NEVER_WIDEN_HALF_COO_CH5_DIVZ_FORM.md` as committed at
fb9d8a85f7, sha256 `183efbbf3456e9b3dc2d0d0842be40762384ce6ead8e5efff21473b3f21f7e7a`. Any edit to that file voids this half.

## What I read at signing

- **The writer's rule** (N = 1, `lib/research/corpus/fund_form.py`):
  - `METHOD_VERSION = "2"` (:68);
  - objects are named by `_inputs_sha16` (:225), which hashes the method version and the sorted inputs;
  - writes go only through `gold.gold_put` (:341), which never overwrites.
  - So the DIVZ form with `inputs` `[]` gets a new name (`a181f849...`) beside the stale version-1 `e19a2eb0...`.
- **The code pin:** `git diff --stat 2e0dc6af2e HEAD -- lib/research` is empty at this seat's HEAD, so the order's tree proof holds today.
- **Served readers of the table:** a census of `research-fund-form|fund_form` over the gateway app finds 5 hits in 136 files, all in
  `refs/DATA_CATALOG.yaml` (the catalog entity for `amgt/harvest/gold/research-fund-form/`). No curated tool reads a fund form. **One
  correction to the COO half's "served: NOTHING":** the gateway's generic catalog read can list and read this table. So after the act, a
  catalog read of DIVZ shows one more object (add-only), and nothing already served changes. That is within this half's blast radius,
  and it is stated here rather than left implied.

## Blast radius

- One gold key is added: `amgt/harvest/gold/research-fund-form/fund=divz/a181f84957dbb8b7.json`.
- Nothing is overwritten or deleted.
- The table's catalog listing gains that object.
- Readers of DIVZ's form (`read_latest`, `_pick_stored`) resolve the new object with `current` True in place of the stale version-1 form.
- No curated served value moves. The UNH control (C-7) proves it before and after.

## Both branches

- Branch A and Branch B are as the COO half states them.
- The in-memory build must equal the measurement before any write.
- A Branch-B repair is a still newer object, decided by the issuer and this seat; the seat deletes nothing.

## Rollback

ADD-ONLY. Removing the one key restores the stale resolution. That is an S3 delete, Andrew's act, and it is not pre-approved here.

## Conditions of this signature

1. **C-1 to C-9 bind as written.** That includes C-6: the no-rebuild instruction (my ruling @162d5a6934) stays in force for every name
   with no `/5` continuation until ch-1 and ch-2 read 0 differing. This act lifts only the DIVZ-form part.
2. **C-9: site Z is told first.** No GO until site Z's answer is on record.
3. **The S44 rule** applies, and the NEVER-2 close is COMMITTED with the manifest.

## VERDICT: SIGNED (CTO).
