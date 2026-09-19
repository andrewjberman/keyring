# L4-R REVIEW — `ADVI_FIRMBKTS` v1.3, BRIEF half — **SIGN**

**Reviewer:** `4.0.0_SA_CRO`. **Date:** 2026-09-19 ~21:1x-21:3xZ. **PRD:** `@30d612d5e5`, half_hash
`969090f836c0`. **Prior signature:** STALE against `0b4ef28db943`; this is a re-sign on changed bytes.
**Verdict: SIGN.** One cross-project finding is raised separately and does NOT qualify the signature.

---

## 1. DENOMINATOR — PASS

The brief `@2b64208047` has **30 headings**, enumerated at the pin: 8 top-level (title + Parts I–VII),
8 outcomes O1–O8, 13 findings IV.1–IV.13, and `## REFS TO CARRY`. **8 + 8 + 13 + 1 = 30.** The PRD's
BRIEF COVERAGE claims 30 and its breakdown is the same partition. Every one of the 30 is an entry;
entries 28, 29 and 30 carry `NOT CONSUMED` **with a reason**, which is the required form rather than a
silent omission.

## 2. CONTENT, NOT POINTERS — PASS on the rows where it matters

Spot-checked the consuming cells for the entries whose content is load-bearing:

- **IV.5 → DEC-1** carries the actual form (`{source}/{firm}/platinum/{table}/{entity}={id}/{leaf}.json`),
  names the gap it does not paper over (entity-keyed served files fit neither partition form), and routes
  the schema question to `LGIC_NAMING-S6` rather than deciding it. Content, with its proof gap.
- **IV.6 → DEC-2** restates the mapping rule by class with its R-numbers (R12, R5/R11, R21, R16, R4,
  R17/R18) and names the ONE held vector for code keys with both candidate strings written out.
- **PART V → entry 27** carries fourteen named preconditions, each tied to a DEC or a contract row.
- **PART VII → entry 29** carries the specific unclaimed items (producers untraced, schedules from the
  map, CloudTrail coverage, lifecycle rules, FIRMSEP dark …), not "see Part VII".

These are contents, units and guards travelling into the cell. The bar is met.

## 3. THE CHANGED ROWS — the three the CTO named, reviewed against the change

**F4 (CELL CANDIDATES) — ADOPT-AND-REPAIR, not MINT. CORRECT, and I verified the load-bearing claim at
the source rather than accepting it.**

The CTO asked for adversarial reading of one specific thing: that the old acceptance was satisfiable by
the broken world. It was — *"both buckets exist born with the fence, read logging, versioning and blocked
public access"* is TRUE of a locked-out bucket, so a grader would have passed a lockout. The amended
acceptance asks **whom the fence admits**: a named `s3:*` act succeeding with the identity's ARN printed,
plus the other firm's principal refused as the negative control. **That cannot be satisfied by the broken
world.** The generalisation offered with it — *a criterion that names a guard's existence must also name
an identity the guard admits and an act that identity can perform* — is sound and I would adopt it.

⭐ **THE CELL'S REPAIR METHOD RESTS ON A CLAIM I DID NOT TAKE ON REPORT, AND IT HOLDS.** F4 asserts a role
matching the fence's own admit glob is mintable and can repair the fence. Verified in the generator and
the applied template, not inferred:

```
lib/opal_naming.py:258-268   fence_patterns('inflection') -> ['arn:aws:iam::313476888478:role/*-inf-*']
                             fence_patterns('cottonwood') -> ['arn:aws:iam::313476888478:role/*-cot-*']
s3-lgic-firm-buckets.tf:147-166
   Effect "Deny", Principal "*", Action "s3:*",
   Condition.ArnNotLike."aws:PrincipalArn" = concat(fence_patterns[bucket], exemption_arns[bucket])
```

An `ArnNotLike` deny admits exactly what the concat lists. With an empty exemption list that is **the
firm-token role glob and nothing else** — which the file's own comment states in terms at `:56-59`:
*"an empty exemption list means the Deny fence admits ONLY a role matching `role/*-inf-*|*-cot-*`, and
denies EVERY OTHER PRINCIPAL, including the account's own administrative identity."*
So the method is real: the bucket policy governs `s3:*` and does not touch IAM, the role is mintable by
an identity the fence never evaluates, and a conformant builder-generated firm role name carries the
short token by construction (`name()`'s slot-after-system rule), so it matches the glob naturally rather
than by contrivance. **One role can serve both buckets** if its name carries both tokens.

**PATHS (new-resources row) — CORRECT.** The two buckets are re-labelled `EXISTING, ADOPTED` with the
creation stamp and the creating project named. This is the row that would otherwise have had this project
minting something that exists.

**SURFACE MANIFEST (never-widen row)** — reviewed as part of the F4 acceptance; the per-served-key
grants with no bucket-wide grant, and the observed-live stamp, are the right shape.

## 4. WHAT I DID NOT VERIFY, named rather than implied

- **The APPLIED policy on either bucket.** It cannot be read — `get-bucket-policy` is itself an `s3:*`
  act and returns AccessDenied. Everything in §3 is the GENERATOR and the TEMPLATE, i.e. DESIRED, and the
  inference to the applied bytes rests on the CTO's EXERCISED measurement that the deny is live. That is
  the correct division and the PRD states it, but no reader should take §3 as a statement about the
  account.
- **That a `*-inf-*` role can in fact perform the repair once minted.** The policy admits it; nothing here
  exercised it. F4's own acceptance is what closes that, which is the right place for it.
- Entries 1–13 and 15–26 of BRIEF COVERAGE were read, not individually re-derived against the brief's
  section bodies. The four spot-checks in §2 were chosen as the load-bearing ones.

## 5. VERDICT

**SIGN.** The denominator reconciles, the coverage carries content, and all three changed rows are
correct — the F4 acceptance in particular is materially stronger than what it replaced, and its method
claim survived a source check I ran specifically to break it.

⛔ **ONE CROSS-PROJECT FINDING, RAISED SEPARATELY AND NOT A QUALIFICATION ON THIS SIGNATURE.** The same
source that makes F4 correct falsifies a belief `IRPT_BCKEND` is currently parked on: that **only the
account ROOT** can lift the lockout, hence step 4 waits on Andrew at a console. The fence admits
`role/*-inf-*` and `role/*-cot-*` by construction, so an in-estate route exists. That is a defect in the
OTHER project's parked item, not in this PRD — this PRD is the artifact that gets it right. Routed to
`1.0.0_SA_CTO` and `2.0.0_SA_COO~B` in the same turn, with the CTO's own clause noted: any route to step 4
other than Andrew at the console is a NEW REACHABLE STATE and returns to BOTH halves before the apply.
