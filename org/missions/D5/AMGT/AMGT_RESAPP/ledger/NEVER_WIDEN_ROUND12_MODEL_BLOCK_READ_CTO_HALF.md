# NEVER-WIDEN CO-SIGN -- ROUND 12, `AMGT-rk-2`: the adapter redeploy and the `derived/model_block/` READ grant. **CTO HALF.**

**Signer:** `1.0.0_SA_CTO~Z` (the CTO half). **Counterpart:** `2.0.0_SA_COO~Z` writes the COO half; `AMGT-rk-2`
AC1 asserts `halves 2` and the cell cannot pass on one. **Act:** `AMGT-rk-2`, worker
`0.9.0_WK_AMGT_RESAPP~24`, chain B. **Signed:** 2026-09-16 ~06:1xZ. **Push state:** LOCAL on SITEZ.

⛔ **THIS HALF NAMES THE ACT'S BLAST RADIUS, NOT THE PRODUCER'S DECISION.** It covers what the act MAY touch
and the rollback per key, and it covers BOTH branches of every expected outcome it names.

---

## 1. THE ACT, in two limbs

1. **REDEPLOY** `opal-amgt-scoped-api` from HEAD, so the adapter's `read_posture` and model-block read reach the
   live plane. The deployed bytes are older than the code that works.
2. **GRANT** the adapter's role `s3:GetObject` + prefix-conditioned `s3:ListBucket` on **`derived/model_block/`**,
   a TENTH prefix beside the nine already co-signed at `@e1c3cf0cb3`.

## 2. PRE-ACT STATE -- the rollback anchor, read from the live plane at signing

| field | value at signing |
|---|---|
| `FunctionName` | `opal-amgt-scoped-api` |
| `LastModified` | **`2026-09-15T19:01:10.000+0000`** |
| `CodeSha256` | **`9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk=`** |
| `CodeSize` | `747396` |
| `Role` | `arn:aws:iam::313476888478:role/opal-amgt-scoped-api-role` |
| env keys | `['HARVEST_ARTICLES_TABLE', 'HARVEST_METRICS_TABLE']` -- **`AMGT_MODEL_BLOCK_ROOT` ABSENT** |

Read by `get_function_configuration` at signing, not carried from the order.

## 3. THE BLAST RADIUS -- the write set this act MAY touch, and the rollback FOR EACH KEY

⭐ **THE ACT WRITES NOTHING TO THE POOL.** It changes Lambda code, Lambda configuration and one IAM policy. The
grant it adds is **READ-ONLY**. No pool object is created, modified or deleted by this act, so no pool key needs
a rollback.

| key the act MAY touch | rollback |
|---|---|
| `opal-amgt-scoped-api` **function code** | redeploy the archive whose `CodeSha256` is `9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk=` (CodeSize `747396`), the bytes live at signing |
| `opal-amgt-scoped-api` **environment** | restore the env to exactly `HARVEST_ARTICLES_TABLE` + `HARVEST_METRICS_TABLE`; if `AMGT_MODEL_BLOCK_ROOT` is added, **REMOVING it is the rollback** and it was ABSENT at signing |
| the role's **inline S3 policy** | restore the prefix list to the NINE co-signed at `@e1c3cf0cb3`: `publication-links/v1/`, `publications/v1/`, `universe/v1/`, `crosswalk/v1/`, `filings/v1/`, `drafting/v1/`, `peers/v1/`, `management/v1/`, `posture/v1/` -- printed here so the rollback needs no second lookup |
| **nothing in `s3://opal-data-harvest`** | not applicable -- the act has no write path to the pool |

⛔ **OUTSIDE THIS HALF, and therefore NOT COVERED:** any pool write; any DynamoDB grant change; any change to the
NINE existing prefixes; any wildcard or `Scan` grant; any second function; any portal act; enabling a schedule.
An act reaching any of those is not covered by this signature and must not proceed on it.

## 4. THE WRITER CENSUS -- **N is printed, per named property**

⛔ **A property with N writers needs N rules read, and N is a number this half PRINTS.** Measured at signing by
reading the source, not by trusting `comp-iam`.

| named property | files mentioning it | **WRITERS** | who |
|---|---|---|---|
| `derived/model_block/` objects (the grant's target) | 7 | **1** | `integrations/bloomberg/research/model_block_pull.py` |
| `posture/v1/` objects (AC5's `packs` / `comparable_name`) | 4 | **1** | `lib/research/posture/judge.py` |
| the **served response** (`model_status`, `header_figures`, `fiscal_year_figures`) | -- | **1** | `lib/research/api/scoped_amgt.py`, the adapter itself |

**Each is a SINGLE-WRITER property, so each needs ONE rule read and each rule was read.** The three candidate
files that carried a write call but are NOT writers of this prefix were discriminated and excluded:
`derive_fye_fixed.py` writes a DIFFERENT prefix (s.5), and `crosswalk.py` / `render_print.py` / the vintage test
carry only prose or fixtures naming the string.

⚠ **`comp-iam` IS BLIND EXACTLY HERE and this half does not rest on its silence:** `comp-iam service
opal-amgt-scoped-api` returns 3 operations, **ALL `UNRESOLVED-RESOURCE`, and NO S3 row at all**, and its own
banner says the list is a **FLOOR** and never a deletion warrant. The Terraform was read directly. **An absence
from a tool that declares itself a floor is not evidence of absence.**

## 5. ⛔ THE WIDENING HAZARD THIS CENSUS FOUND -- the one thing this half exists to catch

**A SECOND, ADJACENT PREFIX EXISTS: `derived/model_block_fye/`**, written by
`integrations/bloomberg/research/derive_fye_fixed.py` (`:12`), carrying the fiscal-year-end derivation identity.
It is a **DIFFERENT store with a DIFFERENT writer** and the adapter has no business reading it.

**`derived/model_block` is a STRING PREFIX OF `derived/model_block_fye`.** Measured at signing:

```
grant "derived/model_block/"   matches "derived/model_block_fye/"  -> False   (trailing slash EXCLUDES it)
glob  "derived/model_block*"   matches "derived/model_block_fye/"  -> True    (star SWEEPS IT IN)
```

⛔ **THE GRANT IS SIGNED ONLY IN ITS TRAILING-SLASH FORM, `derived/model_block/`.** A grant written as
`derived/model_block*`, or as `derived/model_block` without the slash, **silently widens the act to a second
store this half does not cover, and nothing would refuse it** -- the policy applies, the cell passes, and the
adapter quietly gains read on a derivation store nobody granted. **That form is NOT covered by this signature.**

⭐ A prefix grant is a string-prefix match, so **two stores whose names share a stem are one typo apart**. This
is the specific shape a writer census catches and a per-member check cannot: both stores are individually fine.

## 6. THE EXPECTED OUTCOMES -- **read from the producer's own rule, BOTH branches covered**

`AMGT-rk-2` asserts figures and packs reach the served plane. **This half does NOT predict that outcome from the
input's shape; it reads the producer's rule and covers both branches.**

- **`AC4` figures.** The adapter serves figures for a name **only where a `derived/model_block/<key>/` object
  exists.** At signing the pool holds **3 covered keys (BA, BABA, SAP) plus NVDA, which is not covered, against
  89 coverage names.** **BRANCH A:** BA has a block, so figures SHOULD appear and `AC4` should pass on
  `BA_US_Equity`. **BRANCH B:** for the other 86 the honest result is a classed ABSENT, and **that is covered
  and is NOT a defect of this act.** Widening the population is Andrew's card, not this cell's.
- **`AC5` packs / `comparable_name`.** The posture producer writes a pack **only for a pair it has judged**; at
  signing **2 objects exist (BA, BABA)**. **BRANCH A:** BA is judged, so the redeployed `read_posture` should
  serve `comparable_name` and `packs`. **BRANCH B:** a name with no judged pair serves ABSENT, covered.
- **`AC6` is a JUDGMENT criterion, graded at L9 by `3.0.0_SA_CVO~Z` and NEVER self-graded.** This half takes no
  view on its verdict and its signature does not anticipate one.

⛔ **NO MANUAL-CLOCK OVERRIDE IS COVERED.** Nothing here licenses running a scheduled producer off its own clock;
such an override creates a new reachable state this signature has not seen.

## 7. WHAT THIS HALF DOES NOT DO

It does not authorise a portal act (**PORTAL FROZEN: commit yes, promote no**), a shared-branch push
(**RESERVED**, LD-0367/0368), enabling collection (**RESERVED**, `@9db2a36cdc`), any alarm/monitor/freshness
machinery (**standing moratorium**), a vendor call, or widening the model-block **POPULATION** beyond the 3 keys
that exist -- that last is **CARD 1 at Andrew** and is not this act's to take.

**A DELTA=0 outcome needs no hold. This act is not DELTA=0: it moves served output, which is why both halves
exist.**

---

**SIGNED, CTO half:** `1.0.0_SA_CTO~Z`, 2026-09-16.
**Counterpart owed:** the COO half by `2.0.0_SA_COO~Z`. **This act proceeds on TWO halves, never one.**

---

# AMENDMENT 1 -- 2026-09-16 ~06:3xZ: THE GRANT HAS **TWO LIMBS**, and this half named only one. Corrected, and the exact signed string is pinned.

**Author:** `1.0.0_SA_CTO~Z`. **Trigger:** the COO half @`809df9d16b`, which read the **APPLIED** plane and found
what this half's **DESIRED** read did not surface. **The counterpart was right and this amendment adopts its
finding in full.**

## A1.1 WHAT THIS HALF GOT WRONG

s.3 wrote the rollback as *"restore the prefix list to the NINE"* -- **one list.** Measured on the applied
policy by this seat's own IAM read (`get_role_policy` on `opal-amgt-scoped-api-grants`, 4 statements), **there
are TWO:**

```
LIMB 1  s3:GetObject    Resource = 9 prefix ARNs        arn:aws:s3:::opal-data-harvest/<prefix>/v1/*
LIMB 2  s3:ListBucket   Resource = the BUCKET (1 ARN)   Condition StringLike s3:prefix = 9 values
```

⛔ **A ROLLBACK THAT RESTORES ONLY LIMB 1 LEAVES A WIDENED LIST CONDITION LIVE.** That is a real hole and it was
in this half. **Both limbs are covered by this signature; the rollback restores BOTH lists to their nine
values**, and a one-limb rollback is not the signed rollback.

⭐ **WHY THIS HALF MISSED IT, because the mechanism is the transferable part: I read the TERRAFORM and the
counterpart read the APPLIED POLICY.** Terraform is **DESIRED** state. s.4 of this half says, correctly, that
the Terraform was read directly rather than resting on `comp-iam`'s silence -- and that was the right call
against that instrument. **But DESIRED is not APPLIED, and a co-sign governs an act on the APPLIED plane.**
Rule 22's own ladder says so and I stopped one rung short. **The two halves caught it precisely because they
read different planes** -- which is what two halves are for, and the reason a single reviewer would not have
found this.

## A1.2 THE EXACT SIGNED STRING -- and s.5's wording, read literally into LIMB 2, WOULD MATCH NOTHING

s.5 signed the grant "**only in its trailing-slash form** `derived/model_block/`". For LIMB 1's Resource ARN
that is right. **For LIMB 2 it is wrong**, because `s3:prefix` values are `StringLike` patterns and the nine
existing ones all end in `*`. Measured, `fnmatch` over the two real key shapes:

| pattern | intended object | adjacent `_fye` store |
|---|---|---|
| **`derived/model_block/*`** | **MATCH** | **no** |
| `derived/model_block/` (no star) | **no** | no |
| `derived/model_block*` | MATCH | **MATCH** |

⛔ **`derived/model_block/` WITH NO STAR MATCHES NOTHING**, so a reader applying s.5's wording literally to
LIMB 2 would land a condition that permits no listing at all -- **silently disabling the very read the cell
exists to perform**, while the policy applies cleanly and nothing refuses.

**THE SIGNED FORMS, PINNED, ONE PER LIMB:**

```
LIMB 1  Resource ARN      arn:aws:s3:::opal-data-harvest/derived/model_block/*
LIMB 2  s3:prefix value   derived/model_block/*
```

⭐ **THE SLASH BEFORE THE STAR IS WHAT EXCLUDES THE ADJACENT STORE; THE STAR IS WHAT MAKES IT MATCH ANYTHING
AT ALL.** Both characters are load-bearing and they fail in opposite directions -- drop the star and the grant
is inert, drop the slash and it widens onto `derived/model_block_fye/`. s.5's hazard finding STANDS unchanged;
this amendment only states the form that satisfies it **and works**.

## A1.3 WHAT IS UNCHANGED

The blast radius (no pool write), the per-key rollback anchors (`CodeSha256` `9ubWPnhz...`, CodeSize `747396`,
env restored to two keys with `AMGT_MODEL_BLOCK_ROOT` absent), the writer census (`derived/model_block/` **1**,
`posture/v1/` **1**, the served response **1**), and both branches of every expected outcome. **Nothing here
widens the act.** The amendment makes the signature COMPLETE where it was partial, and EXECUTABLE where it was
literally inert.
