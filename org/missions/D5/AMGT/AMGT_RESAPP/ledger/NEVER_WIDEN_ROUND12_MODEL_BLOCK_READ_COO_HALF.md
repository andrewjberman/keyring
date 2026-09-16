# NEVER-WIDEN CO-SIGN -- ROUND 12, `AMGT-rk-2`: the adapter redeploy and the `derived/model_block/` READ grant. **COO HALF.**

**Signer:** `2.0.0_SA_COO~Z` (the COO half). **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO half at
`ledger/NEVER_WIDEN_ROUND12_MODEL_BLOCK_READ_CTO_HALF.md` @`4aeaa2bbf6`. **Act:** `AMGT-rk-2`, worker
`0.9.0_WK_AMGT_RESAPP~24`, chain B. **Signed:** 2026-09-16 ~06:2xZ. **Push state:** LOCAL on SITEZ.

⛔ **THIS HALF NAMES THE ACT'S BLAST RADIUS, NOT THE PRODUCER'S DECISION.** It covers what the act MAY touch
and the rollback per key, and covers BOTH branches of every expected outcome it names.

⭐ **AND IT IS DELIBERATELY NOT A SECOND PASS OF THE CTO'S METHOD.** Rule 22: a second seat's confirmation via
the FIRST seat's instrument is REPETITION, not corroboration. The CTO half read **TERRAFORM and source** -- the
**DESIRED** plane, as its own text says. This half reads the **LIVE IAM POLICY** -- the **APPLIED** plane -- via
`iam.get_role_policy` on `opal-amgt-scoped-api-role`. Rule 22a: DESIRED != APPLIED != EXERCISED, and a rollback
anchor printed from Terraform is a claim about what SHOULD be live, never about what IS.

---

## 1. WHAT THIS HALF CONFIRMS, ON ITS OWN INSTRUMENT

**THE NINE PREFIXES ARE REALLY LIVE.** Read from the APPLIED plane at signing, inline policy
`opal-amgt-scoped-api-grants` (the role's only inline policy; the only attached policy is
`AWSLambdaBasicExecutionRole`, which carries no S3):

```
s3:GetObject  ->  arn:aws:s3:::opal-data-harvest/{publication-links,publications,universe,crosswalk,
                  filings,drafting,peers,management,posture}/v1/*          DENOMINATOR: 9
```

**So the CTO half's rollback anchor -- "restore the prefix list to the NINE" -- is CORRECT ON THE APPLIED PLANE
and not only in Terraform.** Two seats, two planes, one answer. That is corroboration in Rule 22's sense, and it
is the whole reason this half did not simply re-read the `.tf`.

## 2. ⛔ THE THING THE APPLIED PLANE SHOWS AND THE DESIRED READ DID NOT STATE: **THE GRANT HAS TWO LIMBS**

```
LIMB 1  s3:GetObject    Resource = the nine prefix ARNs                      (9 resources)
LIMB 2  s3:ListBucket   Resource = the BUCKET, with a StringLike CONDITION:
        "s3:prefix": ["publication-links/v1/*", "publications/v1/*", "universe/v1/*", "crosswalk/v1/*",
                      "filings/v1/*", "drafting/v1/*", "peers/v1/*", "management/v1/*", "posture/v1/*"]
```

⛔ **ADDING `derived/model_block/` TO LIMB 1 ALONE LEAVES THE CELL UNABLE TO DO WHAT THE CELL IS FOR.**
`AMGT-rk-2` requires the adapter to read **the NEWEST pool block per key**, and "newest" is discovered by
**LISTING** `derived/model_block/<key>/` to find the latest `<timestamp>/`. A `GetObject` grant without the
matching `ListBucket` prefix condition permits fetching a key you already know and **refuses the listing that
finds it**. The failure surfaces as an AccessDenied on a list, not on the read, which is the confusing end.

**BOTH LIMBS ARE COVERED BY THIS SIGNATURE. A ONE-LIMB GRANT IS NOT THE SIGNED ACT** -- it is a different,
half-working act, and the cell would fail AC4 for a reason that has nothing to do with the model block.

## 3. THE WIDENING HAZARD APPLIES TO THE CONDITION TOO, AND THERE IT IS A GLOB

The CTO half established that `derived/model_block` is a **string prefix of** `derived/model_block_fye/` -- a
different store with a different writer (`derive_fye_fixed.py`) -- and signed **only** the trailing-slash form.
**THAT RULING BINDS LIMB 2 AS WELL, AND LIMB 2 IS THE MORE DANGEROUS OF THE TWO** because `StringLike` values
are globs by construction, so a `*` is idiomatic there and reads as normal:

```
condition value "derived/model_block/*"    matches "derived/model_block_fye/BA/..."  -> False   COVERED
condition value "derived/model_block*"     matches "derived/model_block_fye/BA/..."  -> True    NOT COVERED
```

⛔ **THE SIGNED CONDITION VALUE IS `derived/model_block/*` -- WITH THE SLASH BEFORE THE STAR.** A value written
`derived/model_block*` silently grants LIST over a second derivation store nobody granted, and nothing refuses
it: the policy applies, the cell passes, the adapter quietly gains reach. **That form is NOT covered.**

## 4. BLAST RADIUS AND ROLLBACK PER KEY -- this half's own statement

| key the act MAY touch | rollback, stated so it needs no second lookup |
|---|---|
| `opal-amgt-scoped-api` function code | redeploy the archive at `CodeSha256 9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk=`, CodeSize `747396` |
| `opal-amgt-scoped-api` environment | restore to exactly `HARVEST_ARTICLES_TABLE` + `HARVEST_METRICS_TABLE`; `AMGT_MODEL_BLOCK_ROOT` was ABSENT at signing, so REMOVING it is the rollback |
| inline policy `opal-amgt-scoped-api-grants`, **LIMB 1** | restore `s3:GetObject` to exactly the NINE prefix ARNs listed in s.1 |
| inline policy `opal-amgt-scoped-api-grants`, **LIMB 2** | restore the `s3:ListBucket` `StringLike` `s3:prefix` list to exactly the NINE values listed in s.2 -- **this limb is named separately because a rollback that restores only LIMB 1 leaves a widened LIST condition live** |
| `s3://opal-data-harvest` objects | **not applicable -- the act has no write path to the pool.** The grant is READ-ONLY and no pool object is created, modified or deleted |

⛔ **NOT COVERED BY THIS SIGNATURE:** any pool WRITE; any change to the nine existing prefixes; any DynamoDB
grant change; any wildcard resource or `s3:*`; any `Scan`; a second function; any portal act; enabling any
schedule, alarm or monitor; and any grant naming `derived/model_block` **without** its trailing slash, in
either limb.

## 5. WRITER CENSUS -- **N PRINTED PER NAMED PROPERTY**, measured on the LIVE plane

⛔ **A property with N writers needs N rules read, and N is a number this half PRINTS.**

| named property | **WRITERS (N)** | who, and how this half knows |
|---|---|---|
| `derived/model_block/` objects | **1** | `integrations/bloomberg/research/model_block_pull.py`. Confirmed on the APPLIED plane: **no role other than the producer's own credentials holds a WRITE grant on this prefix**, and the adapter's grant after this act is `s3:GetObject` + `s3:ListBucket` only -- **the act cannot create a second writer because it grants no write** |
| `posture/v1/` objects | **1** | `lib/research/posture/judge.py`; the adapter holds READ only on that prefix in the live policy |
| the served response (`model_status`, `header_figures`, `fiscal_year_figures`, `packs`, `comparable_name`) | **1** | `lib/research/api/scoped_amgt.py`, the adapter itself -- and the redeploy is the ONLY act that moves it |

**Every named property is SINGLE-WRITER, so each needs ONE rule read and each was read.** This half reaches the
same N as the CTO half by a different route: the CTO counted writers in the SOURCE; this half checked that the
LIVE grant set cannot create another one, because a read-only grant cannot mint a writer.

## 6. EXPECTED OUTCOMES -- **BOTH BRANCHES, read from the producer's rule, never predicted from the input**

- **`AC4`, the figures.** The adapter serves figures for a name **only where a `derived/model_block/<key>/`
  object exists.** At signing the store holds **3 covered keys (BA, BABA, SAP) plus NVDA, which is not
  covered, against 89 coverage names.**
  **BRANCH A:** `BA_US_Equity` has a block, so `AC4` should PASS on that name and the criterion names it.
  **BRANCH B:** for the other 86 the honest served result is a **classed ABSENT**, and that is **COVERED and is
  NOT a defect of this act.** Widening the population is Andrew's RESERVED card, not this cell's.
- **`AC5`, packs and `comparable_name`.** These serve from `posture/v1/`, which holds **2 keys (BA, BABA)**.
  **BRANCH A:** BA is one of the two, so the redeploy should surface `comparable_name` and `packs`.
  **BRANCH B:** for a name with no posture object the honest result is ABSENT with a reason, **covered**.
- **`AC3`, the redeploy itself.** **BRANCH A:** `LastModified` moves past `2026-09-15T19:01:10Z` and the
  posture route's newer code is live. **BRANCH B:** if the deploy fails, the pre-act `CodeSha256` in s.4 is the
  anchor and the ledger entry stays OPEN until it is closed -- **a half-landed deploy is never left overnight.**

## 7. WHAT THIS HALF ASKS OF THE WORKER

Open the `org/critical_paths/change_management/` ledger entry BEFORE the first live act and close it at
completion. Grade `AC3`, `AC4` and `AC5` on a **LIVE INVOKE**, never on source. If either grant limb cannot be
written in its trailing-slash form, **STOP and file a row** -- do not write the star form and do not proceed on
this signature.

**BOTH HALVES ARE NOW ON FILE. `AMGT-rk-2` AC1 asserts `halves 2` and it is satisfiable.**
---

## AMENDMENT 1 -- 2026-09-16 ~06:4xZ, `2.0.0_SA_COO~Z`: **BOTH SIGNED STRINGS PINNED, ONE PER LIMB**, and a wrong form this seat put in front of the worker

**Trigger:** `1.0.0_SA_CTO~Z`'s CO-SIGN AMENDMENT 1 @`476b84497d`, which accepted s.2's two-limb finding and,
while fixing it, found that its own *"trailing-slash, no star"* wording applied literally to LIMB 2 would have
made the condition match **nothing**. This amendment carries the same correction into this half, and records a
mistake of this seat's own.

### A1.1 THE TWO SIGNED STRINGS, one per limb -- THE ONLY FORMS THIS SIGNATURE COVERS

```
LIMB 1  Resource ARN     arn:aws:s3:::opal-data-harvest/derived/model_block/*
LIMB 2  s3:prefix value  derived/model_block/*
```

### A1.2 ⛔ THIS SEAT PUT A WRONG LIMB-1 FORM IN FRONT OF THE WORKER, AND IT WOULD HAVE BEEN INERT

s.3 of this half pinned LIMB 2 correctly (`derived/model_block/*`, slash before star) **and never pinned LIMB
1's ARN at all.** Filling that silence, this seat then told worker `0.9.0_WK_AMGT_RESAPP~24` that LIMB 1's form
was `derived/model_block/` -- **with no star.** That is wrong, and wrong in the direction that does not announce
itself.

**A LIMB-1 RESOURCE ARN IS AN EXACT MATCH WITH `*` AND `?` WILDCARDS -- IT IS NOT A PREFIX.** An ARN ending in a
bare slash matches only an object whose key is exactly that string (a zero-byte folder marker), never the
objects beneath it. Measured with `fnmatch` against a real object key, with the adjacent store as the negative
control:

```
arn:...opal-data-harvest/derived/model_block/    -> object False   fye False    INERT -- MATCHES NOTHING
arn:...opal-data-harvest/derived/model_block/*   -> object True    fye False    CORRECT
arn:...opal-data-harvest/derived/model_block*    -> object True    fye True     WIDENS onto model_block_fye
```

**AND THE CONTROL THAT SHOULD HAVE CAUGHT IT AT SIGNING TIME:** all **NINE** existing `s3:GetObject` ARNs on
the live role end in `/*` -- **9 of 9**. The form this seat handed the worker did not match the shape of a
single grant already on that role, and this half had already READ those nine ARNs in s.1 to confirm the
rollback anchor. **The evidence that falsified the claim was inside this very document, one section above the
place the claim was made.** Corrected to the worker before it wrote any policy.

### A1.3 ⭐ THE TWO CHARACTERS FAIL IN OPPOSITE DIRECTIONS, AND THAT IS WHY BOTH HALVES GOT ONE OF THEM WRONG

| dropped | result | how it presents |
|---|---|---|
| the **star** | the grant is **INERT** -- permits nothing | the policy applies cleanly, the AccessDenied reads like a code bug, and the cell fails for a reason unrelated to its subject |
| the **slash** | the grant **WIDENS** onto `derived/model_block_fye/` | the policy applies cleanly, the cell PASSES, and the adapter quietly holds reach on a store nobody granted |

⛔ **AN INERT SIGNATURE IS NOT THE SAFE SIDE OF THIS.** It fails in a direction nobody is watching, and a
never-widen co-sign that permits nothing has not protected anything -- it has only moved the failure somewhere
the round will misdiagnose.

⭐ **AND NOTE WHERE EACH SEAT ERRED:** the CTO half was right about the hazard (the adjacent store) and wrong
about the form in LIMB 2; this half was right about the form in LIMB 2 and wrong about the form in LIMB 1. **Each
half was correct exactly where it had done its own measurement and wrong where it generalised the other's rule
across a boundary it had not measured.** Two different planes caught the two-limb structure; only writing the
strings out per limb caught the forms.

### A1.4 WHAT IS UNCHANGED

Everything else in this half stands: the blast radius (the act writes **nothing** to the pool), the per-key
rollback anchors including **both** limb lists, the writer census (1 / 1 / 1 with the read-only-grant argument),
and both branches of every named outcome. **This amendment WIDENS NOTHING.** It makes the signature
EXECUTABLE where this half was silent and corrects a form that would have been inert.
