# NEVER-WIDEN CO-SIGN -- CTO HALVES. Round 14, chain I (identity). One section per co-signed cell.

**Signer:** `1.0.0_SA_CTO~Z`. **Counterpart:** `2.0.0_SA_COO~Z`'s COO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_I_COO_HALVES.md` (APPLIED/EXERCISED plane -- the live
keys, the writer census, the per-key rollback measured fresh). **This plane: DESIRED** -- the SOURCE DIFF and THE
PRODUCER'S OWN RULE, read from source at HEAD, never predicted from the input's shape. Neither half stands alone; the
worker reads BOTH before its first live act and STOPS with a BLOCKING row if either is absent.

A half names the act's BLAST RADIUS, never the producer's decision (CLAUDE.md s.5 NEVER-1). Where an expected outcome
below has two branches, both are covered or the half says which is not.

## `AMGT-rk-31` -- add-a-security entry writes a NEW dated crosswalk object (R14-I1; FWD-2, V1; `C-INSTANTIATION-ENTRY`)

**THE ACT.** `python -m lib.research.identity.add_security --bloomberg "<id>" --as-of <today> --write-pool` for exactly
the three validation names -- `CAT US`, `CSL AU`, `6861 JP` (`C-VALIDATION-NAMES`) -- and the corpus-folder form for the
same three. Agrees with the COO half word for word; no disagreement between the planes.

**THE SOURCE DIFF -- this cell WRITES ITS PRODUCER; it does not modify one.** `lib/research/identity/add_security.py`
**does not exist at HEAD** (measured: `lib/research/identity/` holds `build_universe.py`, `coverage_pass.py`,
`coverage_residue.py`, `crosswalk.py`, `crosswalk.schema.json`, `positioning_chain.py`, `resolver.py`, `self_test.py`,
`tests/`, and no `add_security.py`). That absence IS `C-INSTANTIATION-ENTRY`'s finding -- the entry point every downstream
stage waits on. So the DESIRED plane here is a NEW module bound by the rules below, not a diff against existing behaviour,
and the only pre-existing code it may write the pool through is `crosswalk.write_pool()`.

**THE PRODUCER'S RULE, read at HEAD (`lib/research/identity/crosswalk.py:609-655`).** `write_pool(key, payload, bucket=
POOL_BUCKET, client=None)`:
- `POOL_BUCKET = "opal-data-harvest"` (`:67`), `CROSSWALK_PREFIX = "crosswalk/v1/"` (`:68`) -- the bucket is a MODULE
  CONSTANT, not an argument the cell chooses, so this act cannot land outside `opal-data-harvest` (Andrew ~21:45Z: the
  whole pipeline lives there; `opal-data-assets` is client data only).
- **Branch NEW KEY:** `head_object` raises 404 -> `head is None` -> the put carries `IfNoneMatch: "*"` (`:628`), so a key
  that appeared between the census and the put REFUSES rather than overwrites.
- **Branch SAME CONTENT:** an object already carrying the same `document-sha256` is **NOT rewritten** (`:627`) -- re-running
  mints nothing and moves no version.
- **Branch EXISTING KEY, CHANGED CONTENT:** `condition = {"IfMatch": head["ETag"]}` (`:628`) -- it OVERWRITES that key,
  conditional only on the object not having changed under it. ⛔ **THIS IS THE ONE PLACE THE TWO HALVES MUST NOT BE READ
  LOOSELY.** The COO half says *"`crosswalk/v1/2026-09-15.json` ... is NEVER modified: `write_pool()` writes only the
  `<as_of>` key it is handed"*. That is TRUE and its reason is exact: **the protection is the KEY ARGUMENT the caller
  passes, not a refusal inside `write_pool`.** Handed the 2026-09-15 key with different bytes, this function would
  overwrite the population of record. So this half binds the NEW module: **`add_security.py` derives its key from
  `--as-of` and REFUSES any `--as-of` that is not today (UTC) when `--write-pool` is given**, and the worker's proof
  carries that refusal as an exercised negative control, not as a claim.
- **Read-back is part of the producer's rule, not an extra check:** `head_object` after the put, `document-sha256` and
  `ContentLength` compared, `ValueError` on mismatch (`:638-649`). A silent partial write is therefore not a reachable
  state; a failed read-back is a loud failure with the object already landed, which the rollback below covers.
- **Branch UNRESOLVED (a Bloomberg call fails, the terminal is signed out, or a name fails the entity test):** the record
  is written UNRESOLVED with its reason and COUNTED. That is `C-ONE-IDENTITY`'s standing rule and `resolver.resolve()`
  already implements its read side -- *"A MISS returns resolution UNRESOLVED, security_key None and the RAW IDENTIFIER
  echoed -- never a guessed key, never a key made by appending 'US Equity' or stripping a suffix"* (`crosswalk.py:533-538`).
  The COO half covers this branch explicitly, and its rollback is unchanged on it.

**WRITER CENSUS CROSS-CHECK of the named property (`crosswalk/v1/<newest>`).** The COO half prints **N = 2** -- `crosswalk.py`'s
own `--as-of` path and, after this cell, `add_security.py` through the SAME `write_pool()`. Verified from source: `write_pool`
is defined once (`:609`) and `POOL_BUCKET`/`CROSSWALK_PREFIX` are module constants with no second assignment. ⚠ **One reader
the census should be read beside, because it is what makes the new key REACHABLE:** `_read_pool_latest()` (`:513-530`)
lists `crosswalk/v1/` and takes `sorted(keys)[-1]` -- the LEXICOGRAPHICALLY LAST key, which for ISO dates is the newest.
So the moment the new dated object lands, every route resolving through `load_crosswalk()` reads it, with no redeploy.
That is exactly why this cell is co-signed although it ships no code to a served surface, and it is why the rollback works
by DELETE alone: removing the new key restores the prior newest by the same rule. ⚠ It also means a key named with a
FUTURE date would win the sort -- a second reason `--as-of` is bound to today.

**WHAT THIS HALF DOES NOT COVER -- a new act needs a new pair.** Any write to a crosswalk key other than today's; any run
on a name outside the three validation names; any `--write-pool` over the 33 covered names (Andrew, verbatim: *"I dont
care about rerunning until the process is completely validated end to end"*); any change to `write_pool` itself, to
`_read_pool_latest`'s newest-key rule, or to the adapter; any redeploy of `opal-amgt-scoped-api`.

Signed `1.0.0_SA_CTO~Z`, 2026-09-18, against the COO halves at `9a6aa12da2` (this seat's concurrence that the pair is
OWED: `CTO_ADJUDICATION_AMGT_RESAPP_20260918T204xZ.md` @`44702e4e90`, call 3).

---

## STANDING CLAUSE -- BINDS EVERY CELL IN THIS CHAIN (added at signature, 2026-09-18 ~22:4xZ)

**THE WRITE ADDRESS COMES FROM THE BUILDER, AND A HAND-TYPED KEY IS NOT COVERED BY THIS HALF.** Every S3 address a cell in
this chain writes is `lib/opal_naming.py` `address()` output and every resource name is `name()` output (Rule 30), and the
worker's proof carries the builder's PRINTED address, never a typed one. - **The commit gate cannot catch the violation:**
measured by `4.0.0_SA_CRO~Z`, relayed by `0.0.0_AB_MSTR~Z`, the naming gate is ENFORCING (`org/mcp/naming-gate.enforce`
@`d181e0ac5a`, read at `safe-commit.sh:691` -- CLAUDE.md Rule 30's "WARN today" is stale), but its GRADER IS WIDER THAN THE
BUILDER: a hand-typed key of the shape `bloomberg/amgt/bronze/...` PASSES the commit gate while `address()` REFUSES the same
key. A worker that types an address therefore gets a GREEN commit and a key no reader resolves.
**Also measured, and the reason a builder call may REFUSE today:** AMGT has no `scopes.json` row at all (9 rows, none
`amgt`, `harvest` or `resapp`), so `address()` returns an `opal-data-harvest` address in 0 of 1350 scope x source x tier
combinations. A refusal is the EXPECTED state until the registry row lands: it is a BLOCKING row and a named refusal, never
a hand-typed workaround (Rule 30). Andrew-direct ~21:45Z: *"opal-data-assets is solely for client data ... the whole
pipeline will exist within opal-data-harvest"*.


## CTO SIGNATURE -- chain I

**SIGNED** for `AMGT-rk-31`, against the COO half at `9a6aa12da2`, with the today-only `--as-of` bound the issuer has since
applied to the order (its new AC8 plants a past AND a future date, both refusing -- `2.0.0_SA_COO~Z` @`68d899f8d6`).
Every citation in this half was read at source by this seat: `crosswalk.py:609-655` (the conditional put and the read-back),
`:513-530` (`sorted(keys)[-1]`), `:533-538` (the UNRESOLVED rule), `:67-68` (the bucket and prefix constants), and the
absence of `add_security.py` from `lib/research/identity/`.

Signed `1.0.0_SA_CTO~Z`, 2026-09-18, against the COO halves at `9a6aa12da2`.
