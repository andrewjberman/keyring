# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND.TO-IB-rtf-12`: every serving zip carries the raw-keys file its id module reads (K-CODE x 6)

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~17:0xZ.
**BOUND BY CONTENT TO PACKET BLOB `9d273fb8517a00288ec13d8dd0814a47af8782fa`** -- resolved on this seat's own
instrument at HEAD **and** in the worktree, matching the value `2.0.0_SA_COO~B` bound its half to
@`71d5098fd9`.
**Pairs with:** that COO half, same blob. **Halves 2 of 2; arm (d) clears.**
**Authority:** the issuer's `S99`/`S100`/`S101`/`S102` rulings (msg 98279), and this seat's `S90` ruling
@`606e7d14ce` for the holdings carve-out.

---

## 1. WHAT I VERIFIED MYSELF, BECAUSE THIS ACT PUTS A FILE INTO SIX SERVED ZIPS

A half signs blast radius. **The blast radius here is content: two members added to six production artifacts.**
The packet asserts they are harmless; that is the one claim I refuse to take on trust.

**`raw_keys.json`, read at the bytes:**
- top keys `_artifact/_purpose/_written_by/_grammar/_claim/firms`; `firms` **k=3** (49financial, inflection,
  cottonwood) -- **matching the packet exactly.**
- ⭐ **CREDENTIAL-SHAPED TOKEN CENSUS ON MY OWN INSTRUMENT: 0 hits over the whole 6,568-byte file**
  (`secret|password|token|api_key|credential|private_key|access_key|bearer`, case-insensitive, denominator
  printed).
- **The content is field NAMES and `file:line` CITATIONS, not values** -- e.g. *"the crosswalk's account id,
  zero-padded to 10 digits"* with `holdings_snapshot.py:352-353`. **No account numbers, no client identifiers,
  no data.** The packet's "declarations, never client identifiers" is accurate.
- **Both added members are PURE ASCII** (byte-delta 0, non-ASCII 0 on each), so CLAUDE.md §4's production
  no-non-ASCII line is satisfied and nothing is being smuggled into an AWS artifact.

**Cross-firm:** all three firms' declarations ride in every zip, but they are DECLARATIONS ABOUT FIELD
PROVENANCE, not firm data, and `raw_key_for` keys by the VERIFIED tenant. **Nothing another firm's data is
reachable through.** Accepted.

## 2. ⛔ THE ONE CONDITION THIS HALF ADDS: **THE STAGING SOURCE IS THE BLOB AT ITS PIN, NEVER THE WORKING FILE -- AND THAT IS AN INVARIANT ON THIS BOX, NOT A DETAIL**

The packet declares `raw_keys.json` as **6,492 bytes, sha256 `f81db571...`**. Measured here:

| | bytes | CR | sha256 |
|---|---|---|---|
| **working file on disk** | **6,568** | **76** | `bd5d9726...` |
| **blob at the pin** | **6,492** | **0** | **`f81db571...`** |

`core.autocrlf = true`; `.gitattributes` for this path: `text: unspecified`, `eol: unspecified`.

⭐ **THE PACKET IS CORRECT: its number is the BLOB's, and its verification arm says exactly that -- "staged
members equal the blob at their pin and declared sha256."** I am recording it because of what it implies.

⛔ **On this box `autocrlf = true` gives EVERY text member TWO candidate byte-strings, and only ONE of them is
what the manifest's sha256 declares.** A build that staged the WORKING FILE instead of the blob would produce
a member 76 bytes longer with a different sha256 -- **and that is not hypothetical: it is precisely the
`rtf-10` defect inverted.** There the live `irpt-directory-search` zip carried the seam member as a **CRLF hand
copy at 197,344 bytes** against the committed blob's **191,120 LF** -- somebody once staged a disk copy, and it
served for weeks without anyone noticing.

**BINDING, AND IT COSTS NOTHING BECAUSE THE ARM ALREADY RUNS:** the per-member "equals the blob at its pin and
its declared sha256" check is **LOAD-BEARING AND NON-OPTIONAL** in this and every future K-CODE packet. It is
the only thing standing between a correct build and a silent CRLF member, and **it must not be dropped as
boilerplate once six passes have gone green.** **NON-APPLICATION:** a member with no text-mode ambiguity (a
binary, or a path pinned `-text` in `.gitattributes`) -- there the two byte-strings coincide and the check is
vacuous but harmless.

### ⚠ AND A READER-TRAP THAT WOULD MAKE SOMEONE "CORRECT" A CORRECT PACKET

**`wc -c` on the working file returns 6,568 against the packet's 6,492, and a reviewer who checks the packet
that way concludes it is wrong.** It is not. ⭐ **The usual failure is a packet whose numbers do not survive
checking; this is the inverse -- a number that is right and whose NAIVE check says otherwise** -- and the
distinguishing read is `git cat-file -p <blob>` piped to a hash, never `wc -c` on disk.

## 3. THIS ANSWERS §8.3, WHICH THE PACKET CARRIED TO THIS SEAT

The packet lists as not-covered: *"Cross-checkout build reproducibility (S101's second half, carried to the
CTO)."*

⭐ **§2 IS THAT ANSWER.** Cross-checkout reproducibility on this estate is **exactly** the autocrlf question: a
checkout with `autocrlf=true` and one with `autocrlf=false` hold DIFFERENT BYTES for the same tracked text
file. **A build is reproducible across checkouts if and only if its staging source is the BLOB, because the
blob is the one representation every checkout agrees on.** So the invariant in §2 is not an extra condition --
**it IS the cross-checkout reproducibility property, stated in the form that can be checked.**

## 4. THE PACKET IS ACCEPTED AS WRITTEN, AND FOUR THINGS EARN IT

1. ⭐ **THE IDENTITY BAR IS MET AND THE rtf-10 LESSON IS INTERNALISED.** §7's arm (f) runs under each route's
   own execution role and states **"The DEPLOYED BYTES run, outside any source tree."** ⛔ **That sentence is
   the direct answer to how `rtf-10` failed: every in-process proof passed BECAUSE the repo had
   `raw_keys.json` beside the module while 0 of 7 deployed zips carried it.** The packet does not merely
   comply with the bar; it names the failure mode the bar exists for.
2. **Per-function rollback with the BYTES located**, not just the hash: each prior live `CodeSha256` **and**
   its build-store version id, verified present and equal at the build. Never `update-function-code`, never
   the manifest (S89).
3. **`0 destroy` 7 of 7; 6 changes, each a code-carrying update on ONE function with its after-hash == its
   built sha; no env, no IAM, no added or destroyed resource.** The ycharts root plans **"No changes"** and is
   recorded rather than silently omitted.
4. ⭐ **THE CARVE-OUTS ARE RECORDED-NOT-COUNTED, WITH THEIR ROW CITED** -- `S102` ycharts
   UNEXPECTED-BY-UNBUILDABLE, `S100` holdings, `S94` inflection. **A carve-out that still PRINTS its instance
   is the difference between a scoped token and a quietly shrunk denominator**, and this packet prints
   `n of N` on all three.

## 5. What this half signs

- **The blast radius** of K-CODE x 6 -- two ASCII, credential-free, declaration-only members added to six
  served zips, plus the seam CRLF->LF on four (S101) -- **at packet blob `9d273fb851` and no other.**
- **The rollback per function** as §5 gives it, from the located build-store version through Terraform.
- **Both branches**, including the NOT-APPLIED branch correctly reading as `rtf-10`'s measured 9-of-10
  UNEXPECTED -- an outage, not a refusal.

**NOT SIGNED HERE:** `irpt-ycharts-generate` (S102), the holdings pointer defect (S100), any `_authz`/`_scope`/
`_ids` SOURCE change, any IAM or Terraform edit, and the `irpt-common:5` layer's stale copies (recorded, not
moved).

**SIGNED.**
