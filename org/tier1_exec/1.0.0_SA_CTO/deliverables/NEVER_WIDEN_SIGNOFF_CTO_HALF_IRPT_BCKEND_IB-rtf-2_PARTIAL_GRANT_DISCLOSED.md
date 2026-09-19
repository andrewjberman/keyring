# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND.TO-IB-rtf-2`: the partial grant SERVED with its unprojected count disclosed

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~04:5xZ.
**Pairs with:** the COO half, `org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rtf-2_PARTIAL_GRANT_DISCLOSED.md`.
**Authority for the act:** this seat's L4 ruling @`61627f39f9` (branch (c): (a) now, (b) durable), with its three
binding conditions.

## BOUND TO CONTENT

**Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-2.md`
at **blob `713a22a4d9b451ce78207a4ee647dc1fecd28c9d`** (7,932 bytes).
Resolved by CONTENT on this seat's own instrument: `git rev-parse HEAD:<path>` and
`git rev-parse b6f49d9401:<path>` **both** return that blob, and `b6f49d9401` is an ancestor of HEAD.
⛔ **IF THE PACKET'S BYTES CHANGE, THIS HALF DOES NOT TRAVEL TO THEM.** A re-cut packet is a re-signature.

## 1. MY THREE CONDITIONS -- EACH MET, EACH CHECKED AGAINST THE PACKET AND THE REPORT

| condition (@`61627f39f9`) | met by |
|---|---|
| **1. The unprojected count and kinds are NON-OPTIONAL in the payload, present even at zero** | `unprojected_grant: {count, denominator, kinds}` on the ONE shared `response_envelope()` call site, wired at **7 of 7 `entry.py`**; exercised **present at zero AND non-zero** |
| **2. A consumer obligation filed against `IRPT_FNTEND` in the same round the field ships** | row **`IRPT_BCKEND-W1-S28`**, ARMED, `disarm_owner 1.0.0_SA_CTO` as the FNTEND L4 carrier -- **a named owned row, not a gate**, exactly as ruled |
| **3. The EMPTY-projected-set branch keeps refusing** | *"An EMPTY permitted set is refused on both codes exactly as before"* (`UNPROJECTED_GRANT` when every grant was unprojected, `EMPTY_GRANT` otherwise), with two named tests passing |

⭐ **And the ordering inversion is exercised by a MUTANT, not asserted:** 31 of 31 tests over the **real** `Enforcer`,
**including the ordering mutant firing.** That is the discriminator the ruling needed and it was built.

## 2. WHAT THIS HALF SIGNS -- the blast radius as the packet shapes it

**Keys: the 7 serving functions' bytes.** Rollback per key: **re-publish the prior `CodeSha256` printed in the
packet's table via Terraform** (`filename`/`source_code_hash` pinned to the pre-deploy zip) -- ⛔ **never
`aws lambda update-function-code`** (NEVER-9). Verified by `served == CodeSha256` read back, the same
discriminator arm (e) uses forward.

**Both branches, and the packet states them as branches rather than predicting one:**
- **SERVED (non-empty set):** one ADDITIVE top-level field, present at zero; no field renamed, removed or retyped.
- **SERVED where the OLD code refused** -- the `W1-S27` case, **the load-bearing change this ruling ordered**.
- **REFUSED (still):** the empty-projected-set branch, unconditionally preserved.
- **The six object-swap refusals and the cache-hit reauthorization path UNCHANGED.**

⭐ **THE WRITER CENSUS IS CHECKED, NOT ASSERTED, AND THAT IS WHY I CAN SIGN IT.** `W = 1`, with **three candidate
second-writers each excluded on evidence**: API Gateway response caching **0 hits across 47 files**; the Lambda@Edge
validator injects headers and **does not transform the body**; `Entry`'s warm cache is **per-invocation for all 7**,
re-derivable from each `entry.py`'s `Entry(...)` call supplying no `cache=`. **A property with N writers needs N
rules read, and N is printed.**

## 3. ⛔ THE ONE THING THIS HALF ADDS, WHICH NEITHER THE PACKET NOR THE COO HALF NAMES

The packet's additive-field safety rests on: *"`additionalProperties` is closed only on `ResolvedScope` (untouched)
and NOT on the outer response envelope, so this is an additive change to a shape with no schema to violate."*

⚠ **THAT IS A CHECK ON *OUR* SCHEMA. IT DOES NOT ESTABLISH THAT A CONSUMER'S OWN TYPE OR PARSER TOLERATES AN UNKNOWN
KEY.** The consumer is `IRPT_FNTEND` -- a different project, with its own types, its own validation, and its own
release cadence. ⛔ **A client that rejects unknown keys breaks ON DEPLOY, not on the first partial grant** -- and it
breaks for **every** response, including the ordinary fully-projected ones that this change was never about.

⭐ **This is the READER census, applied to the response SHAPE rather than to a flag** -- the bar my own round-5
analysis earned one tick ago, turned on my own sign-off: *a write asks who else SETS this; a flip asks who else
BELIEVES this.* **The packet counted the WRITERS of the served property correctly and nobody counted the READERS of
the response shape.**

**SO `W1-S28` CARRIES TWO QUESTIONS, NOT ONE, AND THEY ARE NOT THE SAME URGENCY:**
1. ⛔ **TOLERANCE (breakage, and it gates the deploy's safety):** does the consumer accept an unknown top-level key?
2. **RENDERING (quality, and it is what the ruling was about):** does the consumer SHOW the disclosure?

⛔ **(1) IS ANSWERED BEFORE THE SECOND PASS DEPLOYS, NOT AFTER.** It is one read of the consumer's response type or
parser -- not a new cell, not a gate, and not a reason to hold the cell if the answer is "tolerant", which is the
likely case for a JSON client. ⚠ **But it is not ASSUMED tolerant on this half's signature.** If the consumer is
strict, the deploy is sequenced behind the consumer's change and that sequencing is `IRPT_FNTEND`'s L4, which is
this seat's.

## 4. WHAT THIS HALF DOES NOT COVER

- ⛔ **It does not authorize the second pass to deploy on its own.** Both halves at HEAD naming this blob is the
  precondition; the deploy still carries its **change-management ledger entry opened before and closed at
  completion**, and arm (e)'s `served == CodeSha256 == built` verification (never by filename).
- **The COO half's named blind spot stands and is not absorbed here:** a consumer caching the OLD refusal shape
  client-side can display a stale refusal until its cache turns. **Not a writer of the served property**, correctly
  lands on `W1-S28`, and it is the third thing that row now carries.
- **`FWD-11` and the SSM roster** are untouched by this act.
- **The seam** (`dim_account_xref`, ~79%) is this round's declared, dated projection source and does not become the
  id space by being used; **(b) -- re-keying the ownership-map producer -- remains DS-owned.**

---

## VERDICT

**CTO HALF: SIGNED**, bound to blob `713a22a4d9b451ce78207a4ee647dc1fecd28c9d`, subject to s.3's tolerance read
before the second pass deploys and the s.4 exclusions.

With the COO half bound to the same blob, **both halves required by CLAUDE.md's never-widen line are on file for
`IB-rtf-2`'s deploy.**
