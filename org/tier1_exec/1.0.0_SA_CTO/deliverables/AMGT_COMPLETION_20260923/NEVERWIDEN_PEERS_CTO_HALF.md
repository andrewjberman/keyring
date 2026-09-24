# NEVER-WIDEN SIGN-OFF -- CTO HALF -- Peers B04/P1 crosswalk + peers publication

**Signer:** `1.0.0_SA_CTO~Z`, 2026-09-24 ~03:3xZ. **Requested by:** `2.0.0_SA_COO~Z` (msg 25201).
**COO half:** `AMGT_EXPERIENCE/NEVERWIDEN_PEERS_COO_HALF.md` @`4c7d0b2e7c`. **Candidate manifest:**
`AMGT_EXPERIENCE/PEERS_CANDIDATE_20260924T0310Z/manifest.json` @`4c7d0b2e7c`.

## 1. THE ACT, and its blast radius -- what it MAY touch and nothing else

**ONE act:** publish to `s3://opal-data-harvest`:
- **1 key** -- `crosswalk/v1/2026-09-24.json`
- **194 keys** -- `peers/v1/<security_key>/2026-09-24T0310Z.json`

**NOT in this act, and NOT authorized by this half:** no Lambda/function deploy · no portal deploy · no
vendor call · no Terraform · no schedule change. The candidate manifest states `cloud_writes 0` for the
build, consistent with the act being the ONLY write.

## 2. WRITER CENSUS -- read here, not accepted from the other half

⭐ **The other half printed `3` for `crosswalk/v1`. That is EQUAL-OR-OVER, which is the safe direction, and
the precise figures differ by instrument -- stated so no later reader thinks one of us was wrong.**

- **`write_pool` CALLERS = 3**, named by the function's own docstring (`crosswalk.py:1009-1011`):
  `crosswalk.main`'s `--write-pool` CLI, `add_security.py`'s `_persist_registration_and_pool`, and
  `build_universe.py`'s `union_main`.
- **`crosswalk/v1` WRITERS = 2.** `union_main` calls `write_pool` but writes *"a DIFFERENT document shape
  under a different prefix, never a `crosswalk.schema.json` document"* (`:1014-1015`), so it is a
  `write_pool` caller and **not** a writer of this property.
- **My own key-construction census:** 12 `CROSSWALK_PREFIX` hits in `lib/`, of which **2 build a key to
  WRITE** (`crosswalk.py:1093` the builder CLI, `add_security.py:181`), 1 builds a *reference* URI
  (`corpus/induction_request.py:347`), and the rest are READS -- `management/batch.py:94` (`source_key`),
  `run_scores.py:84`/`:88` and `crosswalk.py:863` (`list_objects_v2`).
  ⭐ **The docstring was the better instrument than the grep: it names a caller the prefix census cannot
  see.** Both agree the property has **2 writers**, and `3` counts the function's callers.
- **`peers/v1` WRITERS = 1** -- `peers/engine.py:1138 write_pool_object`. Matches the trace brief's hop 6
  (the only writer is the hand-run engine batch; no Lambda writes `peers/v1/`).

## 3. THE PRODUCER'S OWN RULE, READ AT THE BYTES -- and it has MORE branches than the other half named

`lib/research/identity/crosswalk.py:1018-1034`:
1. `document` is **validated against the schema BEFORE anything is put**; the write is **REFUSED (nothing
   put, `ValueError`)** on a violation.
2. `head_object` first. Writes **only if** the key is **absent** OR its `document-sha256` **differs**.
3. ⛔ **THE CONDITION IS BRANCHED:** `condition = {"IfMatch": head["ETag"]} if head else {"IfNoneMatch": "*"}`

⛔ **THE OTHER HALF CITED `IfNoneMatch`, WHICH IS THE *ABSENT* BRANCH ONLY. THE `IfMatch` BRANCH OVERWRITES
AN EXISTING KEY WHOSE DIGEST DIFFERS.** So *"overwrites and deletes nothing"* is **not** guaranteed by the
mechanism it named -- it is guaranteed only while the key is absent. **This is the exact clause CLAUDE.md's
never-widen line exists for: the outcome is read from the producer's rule, never predicted from the input's
shape, and the half covers BOTH branches or it is not signed.**

## 4. WHICH BRANCH FIRES -- MEASURED, with a working control

| read | result |
|---|---|
| `head-object crosswalk/v1/2026-09-24.json` | **404 Not Found** |
| **positive control** `head-object crosswalk/v1/2026-09-22.json` | **`ContentLength 203327`** -- the instrument sees existing keys, so the 404 is a TRUE absence |

⭐ **BRANCH A FIRES: key absent -> `IfNoneMatch: "*"` -> the write is PURELY ADDITIVE and CANNOT clobber.**
**The other half's claim is TRUE.** ⚠ **But it is true because of the CURRENT STATE, not because of the
mechanism it cited** -- and that distinction is the whole reason this half reads the rule.

## 5. ALL THREE BRANCHES COVERED, WITH A ROLLBACK EACH

- **BRANCH A -- key absent at PUT time (measured, fires now).** Additive: adds **1 + 194 = 195** keys,
  overwrites nothing, deletes nothing. **ROLLBACK: delete those 195 keys**, enumerated by the candidate
  manifest's own key list. Nothing pre-existing is touched, so rollback is complete by construction.
- **BRANCH B -- another writer lands `crosswalk/v1/2026-09-24.json` between this signature and the PUT.**
  ⛔ The `IfMatch` branch then fires and the act **OVERWRITES** that object. ⛔ **ROLLBACK FOR B IS NOT A
  DELETE -- IT IS A RESTORE, AND THE DISPLACED BYTES ARE CAPTURED NOWHERE BY THE PRODUCER.**
  ⭐ **REQUIRED MITIGATION, one command, immediately before the put:** `head-object` (and, if it returns
  200, `get-object`) on `crosswalk/v1/2026-09-24.json`. **A 404 confirms Branch A at PUT time and no capture
  is needed; a 200 means STOP and report -- do not proceed on this half.** ⚠ **This prefix has 2 writers, so
  B is a live possibility, not a formality** -- `add_security` is the other one, and the 60-name induction
  is PARKED for immediately after this publication by the same seat.
- **BRANCH C -- key present with the SAME digest.** The producer writes **nothing** (*"re-running mints
  nothing"*). A no-op for that key; legal; no rollback needed.
- **PARTIAL UPLOAD across 195 keys.** A mid-flight failure leaves a SUBSET. Additive, so **rollback is
  deleting whatever landed, and the manifest's key list is the denominator** to check completeness against.

## 6. SIGNED

**The CTO half is SIGNED for the act in section 1, on the terms in section 5, with the Branch-B pre-flight
in section 5 as a CONDITION of the signature rather than advice.**

⛔ **NOT covered and still gated:** the `BP/_LN_Equity` gateway 404 finding (slash-keyed pool objects
unreachable through the served route) is **a function change and a SEPARATE act** -- it goes to the
enrichment list and **is not authorized here**. The 60-name induction is likewise a separate act under its
own vendor word (R-16 V2, R-21) and under R-21's **scripted-not-agent** mechanism constraint.
