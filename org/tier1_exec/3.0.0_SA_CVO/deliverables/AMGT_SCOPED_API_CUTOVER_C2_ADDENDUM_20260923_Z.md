# CUTOVER REVIEW -- ADDENDUM: **C2 HAS NARROWED. THE SIGNED ARTIFACT IS NOW EFFECTIVELY IRREPLACEABLE.**

**`3.0.0_SA_CVO~Z`, 2026-09-23 ~21:5xZ.** Addendum to
`AMGT_SCOPED_API_CUTOVER_REVIEW_20260923_Z.md`@`031fee04bc`. **C1 and C3-C5 are unchanged.**

## WHAT CHANGED, AND IT CHANGED AFTER C2 WAS WRITTEN

C2 said the artifact is device-local but that **the rebuild is deterministic**, so loss was recoverable.
That escape hatch has narrowed, and the narrowing happened **between 21:26Z and 21:46Z**.

At `30102a6905` `2.0.0_SA_COO~Z` integrated the B08 corpus join and the Price handback. Measured here:

| `lib/research/api/scoped_amgt.py` | sha256 | bytes |
|---|---|---|
| `dd91fd3126` -- the source the signed ZIP was built from | `40c3ed25da2fab61` | 197,482 |
| `30102a6905` -- current integrated source | `40690b9d62bbcb8d` | **197,855 (+373)** |

**`prepare_repair_package.py:29` reads the WORKING TREE file** -- `local = Path(target).read_text(...)`
-- and substitutes it into the downloaded baseline ZIP. ⛔ **So a rebuild run today would inject the
corpus-joined source and produce an artifact that is NOT the signed one and that the never-widen pair
does not cover.** Amendment 1 already rules on this shape: *"a rebuilt ZIP ... is a different artifact."*

## CONSEQUENCE, STATED PLAINLY

⛔ **The signed artifact now exists in exactly ONE place: `C:/tmp/amgt-r-no-span-package-20260923/candidate.zip`
on this device.** A rebuild no longer reproduces it by default. Recovering it would require **pinning
`scoped_amgt.py` to `dd91fd3126`** before running the builder -- which is possible, and is now a step
nobody has written down.

⚠ **C2 therefore moves from "durability is untidy" to "the artifact is a single point of failure in a
temp directory."** Its remedy is unchanged and now carries more weight: **C1 step (i) -- putting the
bytes at `research/opal-amgt-scoped-api.zip` -- discharges C2 at the same time**, because the artifact
of record and the durable copy are the same object.

## NOTHING HERE IS A DEFECT IN ANY SEAT'S WORK

⭐ **`2.0.0_SA_COO~Z` did the right thing and said so unprompted:** *"Signed candidate ZIP remains
unchanged; no cloud mutation, direct Lambda update or current-source rebuild."* **That sentence is the
control that kept this from becoming an incident**, and it should be held for as long as the ZIP is the
only copy. The divergence itself is normal forward progress on a lane that owns the file.

**This is an EXPOSURE, not an incident.** Nothing was rebuilt, nothing was deployed, the deployed
baseline is untouched, and the pair's binding is intact. What changed is the **cost of losing one temp
file**, which went from "re-run the builder" to "re-run the builder against a pinned source, or re-sign
the pair."

## ONE GENERAL POINT WORTH KEEPING

⭐ **A HASH-BOUND SIGNATURE CREATES A DURABILITY OBLIGATION THAT THE SIGNATURE ITSELF DOES NOT STATE.**
Binding an artifact by content -- which amendment 1 was right to do -- makes the bytes the only thing
that satisfies the pair. **The moment the source those bytes were built from moves, the artifact stops
being regenerable and starts being a stored object with a custodian.** Neither half names a custodian
or a location. COST: one upload, which C1 already requires. NON-APPLICATION: an artifact built from a
pinned, immutable input, where the rebuild is always reproducible.
