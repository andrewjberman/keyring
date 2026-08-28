# ISCK FREEZE LOG — registry-side prose for every freeze, OUTSIDE the bundle

**Why this file exists (R4-DT-10, 2026-08-28).** A freeze is a REGISTRY fact: `bundle_identity.py <pin>
--freeze --boundary <commit>` writes `frozen_at` + the boundary into `BUNDLE_LABELS.json`, and the
label's `contract_bundle_id` is a sha256 over the bundle's 14 members — DOCTRINE (`ISCK_CONTRACT.md`)
among them. The first freeze commit for `v0.3-candidate+27` (7a44b65f50) also wrote its own freeze
entry into `ISCK_CONTRACT.md` §8, and in doing so changed a member byte: the bundle derived AT the
freeze commit (`103cfd6c…`) was already not the bundle the label names (`87ed7080…`, derived at the
pin d0398b977d). Because `receipt_problem` binds a receipt's `run_commit` to the label by full-bundle
equality (R3-CRO-36 — "the run certified THESE bytes"), and the only commits deriving `87ed7080…`
predate the ledger code, no `run_commit` could ever satisfy the binding: the WP-3 certification
receipt was unobtainable by construction. Found by `0.4.0_DT_ClientPlatform~X` (77766) while
preparing AC8, reproduced independently by `2.0.0_SA_COO~X` (77769) and `3.0.0_SA_CVO~X` (121316Z).

**The repair (b′, issuer REC 77769, certifier concurrence 121355Z, owner's act):** `ISCK_CONTRACT.md`
restored byte-for-byte to the frozen blob at d0398b977d (`git show d0398b977d:… > …`, blob
`d52d6838…`), the §8 freeze entry relocated HERE verbatim, no rule changed, no history rewritten
(7a44b65f50 stands; this is a forward commit). `derive(HEAD)` returns to `87ed7080…`; the label holds;
every later build commit satisfies R3-CRO-36 unchanged.

**The convention this fixes forward:** a freeze's own record NEVER lives inside a member of the bundle
it freezes. `BUNDLE_LABELS.json` carries the registry facts; this file carries the prose;
`ISCK_CONTRACT.md` §8 carries CONTRACT changes only — and a contract change after a freeze derives a
new candidate, which is the design. `bundle_identity.py --freeze` now REFUSES when the working-tree
DOCTRINE differs from the DOCTRINE blob at the commit being frozen (the guard that would have caught
7a44b65f50).

**This file is NOT a bundle member** (`bundle_identity.py` member list: DOCTRINE, SCHEMA, VALIDATOR,
GATES ×8, VOCAB ×3 — read the script, never this sentence). Editing it moves no bundle id.

---

## v0.3-candidate+27 — SCHEMA-ONLY FREEZE (2026-08-28 06:40:18Z) — relocated verbatim from `ISCK_CONTRACT.md` §8 @7a44b65f50

The §8 changelog line for the fourth pin, as it stood at 7a44b65f50 (the appended clause after the
`nullified` sentence):

> (`nullified`, §3.21: VOID beside REPLACE — the only way a false transition is undone) → the fourth
> pin d0398b977d (`+27`, on top of DT~X's last probe repair: R4-CVO-4 the corrective-only race
> slot; R4-DT-2 the identity re-pin).

The freeze entry:

> **SCHEMA-ONLY FREEZE — `v0.3-candidate+27` FROZEN (2026-08-28 06:40:18Z):** `bundle_identity.py
> d0398b977d --freeze --boundary abcb491373` (the second cut, `BOUNDARY_ROUND4.md` §9) records
> `frozen_at` + the boundary in `BUNDLE_LABELS.json`; `BUNDLE_IDENTITY.json` reads `status: frozen`,
> `freeze_scope: schema-only`; `supersedes_bundle_id` → the frozen `+38`, which stays frozen and
> immutable beside it. **The three operational receipts stay null BY DEFINITION** — NOT
> operationally certified; each lands through the registry-side carrier (`--receipt`, structured and
> bound, R3-CRO-28/31/33/36). Naming debt, disclosed: `derive()`'s boundary field is spelled
> `round_3_boundary_commit` and carries the ROUND-4 boundary for this label — the value is right,
> the key name is the round-3 one; a rename is a script change (not a member) and is not made under
> the freeze. **The frozen label is immutable:** any member byte change derives a NEW candidate; the
> contract is never mutated under `+27`. The freeze lifts ledger CODE (both gates of self-drive D11
> ledger row 12 — the design is dry at the same hash); production population and the L3 cells stay
> HELD.

Provenance: original commit 7a44b65f50 (`1.0.0_SA_CTO~X`); relocated at R4-DT-10 by the same seat.
The `+38` freeze (dcbe214a44, 2026-08-28 04:14:06Z) wrote no §8 entry of its own and needs no relocation
(members differing dcbe214a44~1 → dcbe214a44: read the object database, never this line).
