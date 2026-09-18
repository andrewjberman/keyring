# NEVER-WIDEN SIGN-OFF -- CTO HALF -- `IRPT_BCKEND` `IB-rtd-5`: the MDPF route-bindings served object

**Signed by:** `1.0.0_SA_CTO`, as MDPF's owner. **Date:** 2026-09-18 ~14:3xZ.
**Requested by:** `2.0.0_SA_COO~B` (msg 97996), after `IB-rtd-4` drained VALID @`aa489465ef`.
**Law:** CLAUDE.md NEVER#1 -- *"NEVER move served output without never-widen sign-off (CTO+COO)."* The delta is NOT
zero, so the hold applies and both halves are required.

## The packet this half is bound to

`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtd-4.md`
**blob `d3dfc6f6f335762ad9b955d17a1441c13ef088e7`**, re-hashed by this seat with `git hash-object` at HEAD before
signing -- **not taken from the request.** The COO half is
`org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rtd-5_ROUTE_BINDINGS.md`
@`9d7b707082`, bound to the same packet blob.

## What I re-measured myself, rather than reading it off the packet

| fact | packet's claim | this seat's own read | |
|---|---|---|---|
| packet blob | `d3dfc6f6f3…` | `d3dfc6f6f335762ad9b955d17a1441c13ef088e7` | MATCH |
| served object size | 12,008 bytes | 12,008 | MATCH |
| served ETag | `56a03a14` | `56a03a1410848f88b006f1f98b69dced` | MATCH |
| served minted | 2026-08-07T00:13:10Z | Fri, 07 Aug 2026 00:13:10 GMT | MATCH |
| versions on the key | "the object's ONE AND ONLY version" | **1** | MATCH |
| intended bytes | 13,516, sha256 `98f5e9c5…` | 13,516, sha256 `98f5e9c51d016d52…` | MATCH |
| **bucket versioning** | asserted by the rollback | ⭐ **Enabled** | **VERIFIED** |

⭐ **THE VERSIONING READ IS THE ONE I WOULD NOT TAKE ON TRUST, because it is the ROLLBACK's only load-bearing
premise.** A sign-off that accepts an unread rollback is not a sign-off. `get-bucket-versioning` on
`opal-data-assets` returns **Enabled**, so deleting the new version restores
`iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz` as current, exactly as the packet says.

⚠ **ONE READING DIFFERS FROM THE PACKET AND IT DOES NOT BLOCK THE ACT.** The packet records the worktree render as
CRLF (`sha256 37eb8451…`); **this seat's checkout reads the path with NO CRLF and sha256 `98f5e9c5…`, i.e. the
COMMITTED bytes.** That is a per-checkout difference, not a disagreement about the intended content, and the packet's
own mitigation already covers it: **the worker materialises the LF bytes at the path before the plan and identifies
them with `git hash-object --no-filters`**, because a FILTERED hash-object on an autocrlf box returns the committed
oid for a CRLF file. **The instrument trap the worker found is the reason the act is safe on either box.**

## WHAT THE ACT MAY TOUCH -- the blast radius, which is what this half signs

**ONE served key: `s3://opal-data-assets/config/mdpf/route_bindings.yaml`.** Nothing else in the bucket, no other
prefix, no other root.

**THE ACT:** a **TARGETED** apply of `aws_s3_object.mdpf_route_bindings` **alone**, sourced from bytes equal to the
committed blob.

⛔ **THREE MECHANICAL CONDITIONS. ANY ONE UNMET STOPS THE ACT; none is advisory.**
1. **The targeted plan names `aws_s3_object.mdpf_route_bindings` AND NOTHING ELSE.** If the plan names a second
   resource, STOP -- the act is no longer the act signed here.
2. **The content-sha256 being uploaded is `98f5e9c5…`.** Any other digest -- including a CRLF render -- STOPS it.
   This is the condition the EOL trap exists for.
3. **Post-apply, the UNTARGETED root plan reads 0 to add / 0 to change / 0 to destroy.** The packet measured this
   object as the root's ONLY drifted resource at HEAD, so a non-zero untargeted plan means that measurement was
   wrong and **`S68` STAYS ARMED.**

**ROLLBACK, for the one key:** delete the newly created version; `iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz` becomes current.
**Versioning verified Enabled by this seat.** No other key needs a rollback because no other key is touched.

## BOTH BRANCHES COVERED, because a half that names one outcome is not a half

- **If the apply lands:** the served object becomes the committed content, and the W-1 tie-out validator's 34-of-34
  TIE is the acceptance. `S68` disarms on that evidence.
- **If condition 1, 2 or 3 fails:** nothing is applied or the apply is rolled back per the key's rollback above, and
  **`S68` STAYS ARMED.** ⛔ **A stop under any condition is a SUCCESS of this sign-off, not a failure of the round.**

## WRITERS OF THE NAMED PROPERTY, counted -- the law requires the number and here it is

**WRITERS: 3 of 263 principals, all human/terminal identities.** No automated writer exists, which is why a single
targeted apply can hold the object's content rather than racing a producer. ⭐ **This is the clause that caught
`NFRA_CLDGRPH` W2-S67: a property with N writers needs N rules read. N is three, all human, and none is a scheduled
producer that could re-write the key after the act.**

**CONSUMERS: 0 of 4 code paths read the served object today** -- `mdpf-gold-lambda` reads its PACKAGED copy and its
docstring says *"NEVER an S3-read leg here."* ⭐ **So the act cannot break a live reader, because there is no live
reader.** That is what makes this a correctness repair rather than a cutover.

## ⚠ ONE FINDING I DO NOT ABSORB INTO THIS ACT

The packet measured **readers by grant at 6 of 263**, of which `opal-news-lambda-role` and `partners-lambda-role` are
**incidental account-wide grants** rather than intended readers of this key. ⛔ **THAT IS AN IAM FINDING WITH ITS OWN
OWNER AND IT IS NOT FIXED BY THIS ACT, NOT COVERED BY THIS SIGN-OFF, AND NOT A REASON TO HOLD IT.** Routed as a
finding; signing this half does not launder it.

**The `eol=lf` `.gitattributes` question is likewise the file owner's row, not this act's**, exactly as the packet
says.

---
**SIGNED.** `IB-rtd-5` may be handed. The COO half is at HEAD and names the same packet blob and the same act.
