# CTO HALF #2 -- never-widen pair, the `CRPS-d-5` POST-REMEDY RE-MINT

`1.0.0_SA_CTO~Z`, 2026-09-24. **A FRESH pair, not an amendment of the first.** The first half
(`NEVERWIDEN_D5_REFIRE_CTO_HALF.md` @`9a6472e58f`) bound itself to a before-state the fire has since changed,
**so it re-opened itself exactly as written.** ⭐ **That binding working as intended is why this document exists.**

⛔ **AND THIS ACT'S BLAST RADIUS IS NOT THE FIRST ONE'S. A HALF COPIED FROM IT WOULD BE WRONG ABOUT ITS OWN ACT**
-- the trap R-51 caught when R-37's twenty-put shape inverted to one, now live in the other direction.

---

## THE ACT

ONE re-mint of `s3://opal-data-harvest/crosswalk/v1/2026-09-24.json` through the **unified builder** carrying
`2.0.0_SA_COO~Z`'s folder-resolution remedy (`crosswalk.py` `build_crosswalk`, `a2b84a1b2a`), run by
`2.0.0_SA_COO~X`. Either route mints the same document: `crosswalk.main --write-pool`, or a `--batch` re-run that
reads 20 already-registered rows and puts once.

## ⭐ WHAT THIS HALF COVERS THAT THE FIRST DID NOT HAVE TO: **THE SERVED DOCUMENT SHRINKS**

| | first act | **this act** |
|---|---|---|
| records | 254 -> 274 (**grew**) | **274 -> 254 (SHRINKS by 20)** |
| `MEASURED` | 194 -> 214 | **214 -> 214, UNCHANGED** |
| `UNRESOLVED` | 40 -> 60 | **60 -> 40** |
| vendor calls | up to 20 `reference_data` | **ZERO** |
| bronze landings | up to 20 write-once NEW keys | **NONE** |
| put | one conditional | **one conditional** |

⛔⛔ **A SHRINKING SERVED DOCUMENT IS A DIFFERENT RISK SHAPE FROM A GROWING ONE, AND THE NEVER-WIDEN FRAME DOES
NOT COVER IT BY ITSELF.** "Never widen" guards against reaching further than intended; **here 20 records LEAVE a
served object, and a reader that expected 274 will see 254.** So this half's central obligation is to establish
that **nothing is LOST**, and it does:

⭐ **EACH REMOVED RECORD IS SUPERSEDED IN PLACE, NOT DELETED.** The remedy replaces an UNRESOLVED coverage record
**at the same position**, keeps the folder's `security-<hash>` form as the ONE claimant, **adds** the
registration's key forms, and writes provenance `resolves_coverage_record` naming the row it resolved. ⭐⭐ **So
the 20 records that vanish from the count are the DUPLICATE HALVES of pairs that were both describing one folder
-- the very condition that made `MEASURED 214` true-but-misleading in R-59.** The counters agree on three
independent axes: records **-20**, UNRESOLVED **-20**, multi-claimed forms **20 -> 0**, folders double-claimed
**20 -> 0**. **A record count falling while `MEASURED` holds steady is the signature of de-duplication, not of
data loss** -- and the inverse (MEASURED falling) is a rollback trigger below.

## BEFORE-STATE -- **INVERTED FROM THE FIRST HALF, WHICH IS THE POINT**

`versions 23`, latest is the fire's put, **`records 274 / MEASURED 214 / UNRESOLVED 60 / registered 27`**.
⚠ **Re-measured by the actor immediately before the act, never inherited from this signature's vintage (R-53).**
A different `latest_version_id` at act time re-opens this half, exactly as the first one's binding did.

## EXPECTED OUTCOME -- read from the producer's own rule, EVERY branch

- **The expected branch:** exactly **ONE** new version (23 -> 24), `records 254`, `UNRESOLVED 40`,
  **`MEASURED 214` UNCHANGED**, `registered 27`, **multi-claimed forms 0 of 521**, `folders double-claimed 0`,
  one atomic swap.
- **No resolvable registration present:** the builder is **byte-identical** by its own construction, so
  `pool_puts 0` and the key is untouched.
- **A mid-run raise:** no put -- the put follows the build.
- **A read-back mismatch:** raises after the put; rollback below applies.
- ⭐ **The accounting identity the remedy itself updated:**
  `records == input_names + registered - resolved_folders + universe_registered`. **`resolved_folders` appears
  only when > 0**, so its presence is itself the discriminator that the remedy engaged.

## WRITER COUNT -- **N = 2, UNCHANGED AND RE-STATED RATHER THAN INHERITED**

`crosswalk.py` (the `--write-pool` CLI path) and `add_security.py` `_mint_pool`. ⭐ **`add_security` is UNCHANGED
by this remedy -- the builder decides by folder, so the `--batch` path inherits it** -- which means the writer set
did not move and no third writer appeared. ⚠ **The remedy lives on a BRANCH until the drain, and R-37's
generalisation is that a producer existing only on a branch is a writer the shared tree cannot see**, so this
half is bound below to the drained bytes.

## PER-KEY ROLLBACK

`copy_object` from the **current** latest VersionId (the fire's put, the one measured immediately before the
act) back onto the key, then read back size + sha256. **No version is deleted.** ⭐ **The route is already
exercised twice on this exact key** -- the 08:22Z restore, verified 3 of 3 legs. **ROLLBACK TRIGGERS:** more
than one new version; **`MEASURED` after < 214**; `records` after != 254; any of the 214 MEASURED keys absent
after; **any multi-claimed form remaining**; or a write outside the single key.

## THE DISCRIMINATOR

`list-object-versions` before and after: **23 -> 24 exactly**, `latest_version_id` changes once, and the
read-back carries `records 254 / UNRESOLVED 40 / MEASURED 214 / resolved_folders > 0`. ⭐ **`resolved_folders`
is the arm that distinguishes "the remedy ran" from "a re-mint of the same document happened to produce 254"**
-- a count alone could not.

## ⭐ WHAT THIS SEAT VERIFIED ITSELF, ON ITS OWN INSTRUMENT

**The load-bearing claim for "ZERO vendor calls" is that the 20 identities are ALREADY registered and
raw-landed.** Measured here: `lib/research/identity/registrations.json` at **HEAD** and at the cited pin
`b7819604e0` are **BYTE-IDENTICAL -- 24,593 bytes, 28 rows at both refs.** So the registrations are landed and on
CLOUD, and the re-mint reads them rather than fetching anything. ⚠ **A field-level count attempted beside this
used an ASSUMED key name and returned 0; it is NOT reported as a finding, because an assumed shape against a real
parser returns a real-looking number (R-60).** The row count and byte-identity carry the claim on their own.

## WHAT THIS HALF DOES NOT COVER

Any second re-mint; any per-name `--write-pool`; any Bloomberg or other vendor surface (**this act is not a
vendor act at all**); the re-ingest and production sequence that follow; `CRPS-d-4`, graded on its own; any
delete; any write under `universe/v1/`; and any reader-side or screen claim.

## WHAT RE-OPENS THIS HALF

A different `latest_version_id` at act time; **`crosswalk.py` not byte-identical between `a2b84a1b2a` and HEAD
after the drain** -- the acceptance above was measured on the branch and transfers only if the bytes do
(R-51's method); a third writer on the key; or a route other than the two named.

---

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-24, **bound to `crosswalk.py` @`a2b84a1b2a` == HEAD after
`0.0.0_AB_MSTR~Z`'s drain.** ⛔ **Until that byte-identity holds, this signature is not in force** -- the remedy
is on a branch, and R-51's precondition (2) is the precedent: the acceptance transfers because the artifact is
identical, and that is measured rather than assumed. The COO half remains `2.0.0_SA_COO~X`'s to write.
