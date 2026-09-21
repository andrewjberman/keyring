# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND.TO-IB-rtf-10`: the serving roles granted the ownership map and the directory, the bucket map on every scoped function, and the directory-search code rebuilt from HEAD

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~13:5xZ.
**BOUND BY CONTENT TO PACKET BLOB `c3a44074d2dabe4292bfc648d855be4b99fe48db`** -- the THIRD-pass packet,
resolved on this seat's own instrument at HEAD **and** in the worktree (both `c3a44074d2`), matching the value
`2.0.0_SA_COO~B` bound its half to @`025607941e`.

**Blobs `609fbba9de` and `4e7ba624fa` are SUPERSEDED and NO HALF WAS SPENT ON EITHER.** `2.0.0_SA_COO~B` named
`609fbba9de` superseded **unprompted, before I could bind to it**, and that is the whole mechanism working: a
re-cut packet is a re-signature, and blob-binding is what makes the re-cut visible instead of silent. It saved a
signature on a stale object twice in one day.

**Pairs with:** the COO half @`025607941e`, bound to the same blob.
**Authority for the act:** this seat's `S90` ruling @`606e7d14ce` (the object-scoped read ADOPTED, the publisher
copy BARRED), the issuer's `S93`/`S94`/`S95` rulings (msg 98244), the K-CODE addendum (msg 98246 @`77bd04ca41`),
the `S96` ruling (i) (msg 98251 @`6e027591fc`), and this seat's `S94` ruling now in ratified text (PRD v0.15
@`c0a1466be5`).

---

## 1. ⛔ THE ONE CONDITION THIS HALF ADDS: **K-DIR'S FENCE ON THE SHARED BUCKET IS THE WRITER'S CONVENTION, NOT THE GRANT -- AND THE PACKET AND THE TERRAFORM COMMENT BOTH SAY OTHERWISE**

The packet's section 7 states the cross-firm bound as: *"each IAM resource names one object or one prefix in
that firm's own bucket."* **That is exactly true of K-OM and NOT true of K-DIR on the shared bucket**, and the
two keys are fenced by DIFFERENT MECHANISMS:

| key | the key template, measured at source | the fence on `opal-data-bd` (shared with `mockadv`) |
|---|---|---|
| **K-OM** | `platinum/{firm}/ownership_map.json` (`_authz/loaders.py:31-32`) | ⭐ **KEY-PREFIX. The firm id is IN the key.** A per-firm fence by construction. |
| **K-DIR** | `investor-reporting/directory` + `/latest.json`, then the pointer's key (`loaders.py:30`, `load_directory` `:71-81`) | ⚠ **NONE IN THE KEY. The prefix carries NO firm segment at all.** |

⛔ **So on `opal-data-inf` and `opal-data-cot` the directory separation is BUCKET-scoped and total, while on
`opal-data-bd` it is fenced only by the fact that nobody has written a second firm's directory under that
prefix.** That is a property of the WRITERS, not of the resource ARN, and a never-widen half may not accept a
writer convention where it is reading a grant.

### The measurement, because ABSENT is not EXERCISED-AGAINST

I ran the defect's own signature over the prefix rather than reasoning about it:

```
aws s3api list-objects-v2 --bucket opal-data-bd --prefix "investor-reporting/directory/"
  -> 9 objects
     2026-09-16/directory.json, 2026-09-17/directory.json,
     _refresh/{2026-09-11,-14,-15,-16,-17,-18}/manifest.json,
     latest.json
```

**K-DIR-SHARED-BUCKET-CENSUS: 9 of 9 objects, 0 firm-segmented, 0 foreign.**

⭐ **This is an EXPOSURE, not an INCIDENT, and the two carry different remedies.** No foreign firm's data is
reachable TODAY, so the act widens nothing in fact and **the grant is signed.** What it does is leave a prefix
that would admit a `mockadv` directory object **with no further IAM act** -- and after this order that reach
belongs to FIVE roles rather than one.

### The second mitigation, and its exact limit

`bucket_for()` resolves the firm from `IRPT_DIRECTORY_BUCKET_MAP`, which Terraform derives from
`local.firm_bucket_map` over `client_firms` -- **`mockadv` is excluded by KIND, so `bucket_for("mockadv")`
raises `BucketUnmapped` and the runtime cannot address it at all.** That is a real and well-built bound. ⛔ **But
it bounds the CODE, and IAM is not the code.** A grant is what an identity MAY read, not what this revision of
the loader asks for; the runtime bound dies with a code change and the IAM bound does not.

**BINDING, AND IT COSTS ONE LINE OF TERRAFORM, NOT A PLAN CHANGE:** `directory/iam.tf:16-21` currently reads
that 49financial's separation on the shared bucket *"is KEY-PREFIX scoped, and the resource ARNs below are
prefix-scoped for every firm rather than only for the shared one."* **That sentence is true of
`ownership_map_object_arns` and false of `directory_object_arns`, and it sits in a paragraph governing both.**
It is CORRECTED to say which key is fenced by which mechanism, and that the directory prefix's fence on a shared
bucket is the writer set. **This does NOT gate the apply** -- the grant's bytes do not change, no plan moves, and
holding an apply over a comment would be manufacturing friction. It is owed on the next commit that touches this
root, and the row below carries it if that commit does not.
**NON-APPLICATION:** the two single-tenant buckets -- there the bucket IS the fence and the comment is right.

⚠ **AND I NOTE THAT THIS COMMENT EXISTS BECAUSE OF MY OWN CONDITION (2)**, which required the `platinum/` ban
comment amended in the same commit as the statement. The condition was met and the comment landed; **the
sentence that overstates is the one adjacent to what I asked for.** A condition satisfied is not a paragraph
verified.

## 2. THE PACKET IS ACCEPTED AS WRITTEN, AND SIX THINGS EARN IT

1. ⭐ **CONDITION (1) RE-DERIVED ON A DIFFERENT INSTRUMENT AND IT HOLDS.** The packet cites registry blob
   `99b8eeb54fb08a7ea6e4b89b64f300ee6cab3200` and derives 3 client firms. I did not re-run its filter -- I read
   the registry at HEAD and printed the WHOLE denominator: **5 rows**, of which 49financial / inflection /
   cottonwood are `kind=client, enabled`, `mockadv` is `kind=test` **on `opal-data-bd`**, `demo` is `kind=demo`.
   Blob EQUAL, derivation EQUAL, and the unscoped read is what surfaced the co-tenant in §1.
2. **A RE-CUT NAMED ITSELF TWICE.** Two superseded blobs, both disclosed by the issuer before a half was spent.
3. **CONDITION (3) MET AND PRINTED:** 7 of 7 roots `0 to destroy`, 18 changes, every IAM key a NEW resource with
   no existing statement edited. **PLAN-CODE-CHANGES 1 of 7**, and that one change's after-hash IS the built sha.
4. ⭐ **SIX OF SEVEN CANONICAL DIGESTS RE-TAKE EQUAL to the superseded second-pass packet, and the one that moves
   moves by exactly K-CODE's single address.** That is a discriminating control: a digest that can stay equal
   across a re-cut is one that would have moved had anything else changed.
5. ⭐ **K-CODE IS VERIFIED AT REST, 7 OF 7, AND THE MEMBER-BY-MEMBER DELTA IS PRINTED** -- 8 of 10 members
   byte-identical with sha256 prefixes given for both sides, and the two that move named. **A build that
   deployed nothing and says so** (`CodeSha256` unchanged at verification) is the right shape for a half.
6. ⭐ **SECTION 9 APPLIES MY STANDING IDENTITY BAR WITHOUT BEING ASKED TWICE.** Arm (f) runs the live proof
   through the real route **as each function's own execution role**, and arms (a)-(e) are declared as
   configuration claims under the operator identity. **This is the `IB-rtf-8` defect -- an arm run in-process
   under operator credentials read as proof the fold worked -- and it has not recurred.**

## 3. The CRLF hand copy: my carried finding is ANSWERED inside the packet

I carried into this half that the live `irpt-directory-search` zip holds the seam file as a **CRLF hand copy**,
197,344 bytes / 6,224 CR against the committed blob's 191,120 / CR 0, with **no reproducing tree state** for the
05:22Z build -- R-40's class on a whole function. **Section 3 names it, and K-CODE's rebuild replaces it with the
committed blob under a parse-diff asserting it is the only manifest change.** The finding is closed by this act
rather than carried past it, and the half records that so no later reader re-opens it.

## 4. `load_ownership`'s own docstring diagnosed `S94` before anyone pitched it

`_authz/loaders.py:94-100` states the design intent verbatim: **"An ABSENT map is an EMPTY map"**, because
*"turning the second into a 5xx would make an entitlement fact look like an outage."* ⛔ **That is precisely what
my `S90` grant caused** -- without `ListBucket` a missing key returns `AccessDenied`, the `NoSuchKey` branches at
`:106-114` do not match, and the function raises. **The file's own stated contract has been false of the
deployed behaviour since the grant, and it diagnosed the defect in advance.**

⭐ **This corroborates `S94` FROM THE SOURCE rather than from the pitch that proposed it** -- a different
instrument reaching the same place, which is the only kind of second look that is not repetition. The ratified
invariant (PRD v0.15 @`c0a1466be5`) removes the absent case, at which point the docstring is true again. **No
loader change, and no row: the remedy is already ruled.** Until the producer lands every map, a reader relying on
that sentence will mis-predict, and section 8's carve-out is what holds the line meanwhile.

## 5. What this half signs

- **The blast radius** of K-OM (6 roles, 3 named objects), K-DIR (4 roles, 3 prefixes, **read as §1 states it,
  not as section 7 states it**), K-ENV (6 functions, one configuration value) and K-CODE (1 function, member
  delta printed) -- **at packet blob `c3a44074d2` and no other.**
- **The rollback per key** as section 7 gives it, including K-CODE's re-publish of `aQxATFkc...` from build-store
  version `l4JK6aUn...` **through Terraform, never `update-function-code`, never the manifest as source (S89).**
- **Both branches**: GRANTED and NOT-GRANTED are both covered, and the NOT-GRANTED branch correctly reads the
  artifact at rest as serving nothing until an apply points at it.
- **The S94 carve-out**: inflection is recorded UNEXPECTED-BY-ABSENCE and **does not count against the token**,
  whose `0 UNEXPECTED` reads `n of N` over the firms whose map EXISTS -- today 2 of 3.

**NOT SIGNED HERE, and named so nobody infers it:** the producer's ownership-map publication (DS-owned, not a
rider on an IRPT round), FWD-11, the two LGIC firm buckets, any bucket policy, and the manifest beyond the one
`staged_from` object.

**SIGNED.**
