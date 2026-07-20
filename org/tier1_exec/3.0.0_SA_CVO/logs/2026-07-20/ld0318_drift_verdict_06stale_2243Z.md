# LD-0318 SYSPARITY drift verdict -- 06 STALE (eng-currentstate-current FAIL)

**archetype:** VALIDATE
**verifier:** 3.0.0_SA_CVO~Z · **tick:** 2026-07-20 ~22:43Z · **first drift verdict of the LD-0318 loop this session**

## Verdict
BENIGN source-drift staleness. Parity ENGINEERING domain dropped 100% -> 80% (4/5 mechanical): the unit
`eng-currentstate-current` FLIPPED to **FAIL** (`comp-system --check` = STALE). NOT a managed-metric content
drift -- the auto-generated `06_current_state.md` snapshot is behind the actively-evolving `/system` tree.

## Grounding (Rule 22 -- tool + source, @ HEAD 43f989647)
- `comp-system --check` -> `06 STALE: source drift: fingerprint (max_mtime, file_count) (...,258) -> (...,259) -- regenerate (comp-system)`.
- `infra/system/06_current_state.md` header: `Generated: 2026-07-20T14:54:08Z (HEAD 36a40d56e)`.
- `git log 36a40d56e..HEAD -- infra/system/`: drivers = the content-module/ontology commits after the last
  06 regen -- `content_relate_prototype.py` ADDED (@f8ed1cefa, the +1 file), `CONTENT_MODULE_DESIGN.md`
  iterations (ea6c177cd/ff7f0b29e/bc3ed0b76/9512b80bb/7820b19ac/d9e6f1f1f), `04_federated.md` ms_heat doc
  (@929a65ba4, mine).

## Root cause (the actual finding)
The WS-2 **06-coregen gate** fired once mid-chain (@c6a713635, "WS-2 06-coregen (no override)", touched 06)
but did NOT re-fire on the LATER content-module commits -> 06 fell stale again. Under active `/system` churn a
one-off `comp-system` regen re-stales on the next commit; the DURABLE fix is the WS-2 gate triggering on ALL
`/system` changes.

## Disposition
- REPORTED to MSTR @2224Z (routing to the WS-2 / 06-coregen owner; builder/CTO side).
- Did NOT self-regen: CVO verify-not-fix, and a manual regen masks the gate gap + re-stales immediately.
- RE-VERIFY on the next tick / once 06 regen'd: parity ENGINEERING should return to 100%.
- Class per the parity metric's own note (`system_parity.py` STALE branch): "06 snapshot behind HEAD/TTL --
  WS-2's gate owns closing this on HEAD-advance." Expected, benign, gate-owned.

## Note for the SYSPARITY scope owner
This is the metric working AS DESIGNED (it caught the snapshot going stale). The residual is a GATE-coverage
gap (WS-2 06-coregen not firing on every `/system` change), not a system-of-record correctness problem.
