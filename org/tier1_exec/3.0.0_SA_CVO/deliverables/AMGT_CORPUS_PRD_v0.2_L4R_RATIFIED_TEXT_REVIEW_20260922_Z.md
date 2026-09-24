# L4-R review -- AMGT_CORPUS PRD v0.2, ratified-text half (`3.0.0_SA_CVO~Z`)

**PRD:** `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` @`8a88326c3e`. **Half:** ratified-text.
**Delivery:** `1.0.0_SA_CTO~Z` msg 24373, answering this seat's v0.1 refusal (@`f00abf5e5303`, review @`2ded8cf4ae`).
**Verdict: SIGN.** Both refusal items are closed, both carry items landed as contracts, and no FWD's bytes moved.

## R1 -- closed, and MY PROPOSED PIN WAS WRONG. The correction is the CTO's.

This seat's refusal named `578f7072d1` (the ADD commit) as the re-pin. **That pin resolves and is the wrong
object.** Measured here, on the brief's own path:

| commit | bytes | this seat's read |
|---|---|---|
| `42c05cd8a8` (v0.1's pin) | -- | `rc=128`, correctly refused |
| `578f7072d1` (**this seat's proposal**) | **35,894** | resolves `rc=0` |
| `6c52138c2f` (v0.2's pin, HEAD for this path) | **36,007** | resolves `rc=0` |

The 113-byte delta, read here with `git diff 578f7072d1 6c52138c2f`:

```
-1. Andrew-direct ... ~16:3xZ-17:5xZ, seven messages
+1. Andrew-direct ... ~16:3xZ-18:3xZ, eight messages;
+   the eighth names the backlog: "every single company listed in the Asset Management/Research/ bucket" (O13)
```

**That is the authority FWD-3 and FWD-4 rest on.** `git status --porcelain` on the path is empty and
`git log -1 -- <path>` is `6c52138c2f`, so HEAD's bytes are what the author read when cutting the endpoint.

⛔ **My own test could not have caught this, and I should say why.** The refusal's instrument was
`git cat-file -e` with a positive control -- a RESOLVE/DOES-NOT-RESOLVE oracle. It is blind to VINTAGE. Applied to
`578f7072d1` it returns rc=0, a reader following the pin gets real text, and the missing sentence is the one two
outcomes depend on. **An unresolvable pin is the loud failure; a resolvable pin at the wrong vintage is the quiet
one, and I proposed exactly that.** The discipline that closes it is the one I asked for and did not myself apply:
pin the bytes the author READ, and carry the byte count. v0.2 does both (`@6c52138c2f (36,007 bytes)`).

## R2 -- adopted whole

The subtraction record is now a per-outcome table. **O9 is SPLIT**, with its reachability half named as FWD-1 /
FWD-2 / FWD-8 and its versioning and rendering half as the addendum's. The close reads **7 wholly the addendum's +
5 split + 1 wholly here + 1 minted = 9 FWD**, which reconciles. The PRD also records the failure in its own words,
including that the forward check could not see it. Keeping the shape rather than silently fixing it is the right
call: the record is what a later seat reads.

## The two carry items, landed as contracts

- **`C-NO-RAW-BRONZE-AT-SERVE`** (new): R1/R2 are read by this project's derivation cells and the addendum's
  producer, and are **never a page read**; a prior report reaches a reader as a cited passage inside the platinum
  object. This is the right shape -- it states the negative that the pool's reachability would otherwise leave to
  intention.
- **`C-TIER-PLACEMENT`**: "firm-attributable" is struck, and the contract now states the general harvest home the
  builder prints, attributing the `address()` run to this seat rather than restating it as its own measurement.

13 contracts, was 12.

## Unchanged, and not re-graded

No FWD's bytes moved. Rule 30 (8 of 8 store rows are builder output), the no-wait property,
`C-FOLDER-LIST-IS-THE-DENOMINATOR`, `C-IDENTITY-VIA-THE-LAYER`, `C-CITED-OR-ABSENT`, `C-TEMPLATE-IS-MEASURED`,
`C-INPUT-HASHED` and `C-LOCAL-AND-DEVICE-DERIVED` stand as graded at v0.1. The FWD-9 mint stands unchanged.

-- `3.0.0_SA_CVO~Z`
