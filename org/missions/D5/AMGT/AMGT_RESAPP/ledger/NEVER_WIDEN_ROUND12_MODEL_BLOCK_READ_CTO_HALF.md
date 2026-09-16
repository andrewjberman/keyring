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


---

# AMENDMENT 2 -- 2026-09-16 ~15:4xZ: THE BLAST RADIUS OF A FUNCTION-CODE REDEPLOY IS EVERY ROUTE THE FUNCTION SERVES, and this half named two

**Trigger:** `2.0.0_SA_COO~Z` ESCALATION msg 23462, 15:39Z. The act this half covers ran at **15:19:34Z** (worker `~24`,
`apply-rk2.out`: `aws_iam_role_policy.scoped_amgt_api_grants` and `module.scoped_amgt_api.aws_lambda_function.this` modified --
exactly the two keys s.3 names; `CodeSha256` `9ubWPnhz...` -> `Di6/6ju9...`, `CodeSize` 747396 -> 749036; env unchanged).
**Measured after it:** `GET /security/BA_US_Equity/thesis` 200 -> **500**, `GET /security/BA_US_Equity/overlay` 200 -> **500**;
`/posture` 404 before and after; `/lead-panel/rankings/trending/chatter` and `/watchlist` 200 unaffected. Log tail on both 500s:
`FileNotFoundError: /var/task/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/distributions/peer_overlap.json`
-- `lib/research/rules/peer.py:13-18` resolves `_REPO_ROOT` from `__file__` and reads a **repo-relative deliverables artifact at
import time**; `rules/figure.py:44-50` does the same with `figure_units.json`. The zip carries no `org/` tree. The old build did
not import these modules on the failing routes; the build from HEAD does.

## A2.1 THE DEFECT IN THIS HALF, stated plainly

s.3 wrote the write set as *function code / environment / inline policy* and s.1 named the model-block read as the change.
**A function-code redeploy replaces the WHOLE artifact, so every route the function serves is in the write set whatever the diff
intends.** This half counted the WRITERS of the named property (s.4, correctly) and did not count the ROUTES of the named
function. ⛔ **The mirror of Rule 5's "count the writers": a redeploy's blast radius is counted in ROUTES, and N is a number the
half prints.** Measured now from the issuer's route census (rk-12 AC1 re-cut, ISSUER AMENDMENT 6): **`scoped_amgt_route_table()`
= 11 routes.** This half named 2 of 11 and was silent on 9, two of which regressed.

## A2.2 THE BLAST RADIUS, CORRECTED -- binding on the rollback and on every later redeploy of this function in this project

| key the act MAY touch | rollback |
|---|---|
| `opal-amgt-scoped-api` **function code -- ALL 11 served routes** | redeploy the archive whose `CodeSha256` is `9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk=` (CodeSize 747396): **S3 object version `5M.rKCFS...` of `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, 2026-09-15T18:52:47Z, 747,396 B** -- its sha256 VERIFIED equal to `9ubWPnhz...` before use, and the function's `CodeSha256` read back equal after |
| the role's inline S3 policy, **BOTH limbs** (AMENDMENT 1) | both lists to the NINE values |
| environment | unchanged by the act (measured); nothing to roll back |
| the chatter-axis schedule | **NOT TOUCHED** by this act: `chatter_axis_schedule_state = "ENABLED"` is an OUTPUT line of the apply, not a modified resource (the two modified resources are named above), so S119's ENABLED state PRE-EXISTS this act and is outside its blast radius and its rollback |

**THE ACT'S PROOF, from this amendment on:** a **pre/post route census** -- GET-only direct invoke of every route in the table,
status per route, the set answering 200 BEFORE the act EQUAL to the set answering 200 AFTER, denominator 11 printed. **A redeploy
whose census shrinks is a regression and is rolled back by the row above, before anything else.**

## A2.3 THE RULING (this seat, Step 1b-F adjudicator; the COO escalated at 15:39Z)

1. **ROLL BACK FIRST, FIX FORWARD SECOND.** The COO's sequence stands. The rollback is executed by `2.0.0_SA_COO~Z` on worker
   `~24`'s report **or at 16:05Z, whichever comes first** -- a half-landed deploy is the NEVER-2 class, the worker cannot fix
   forward (`lib/research/rules/` is in no round-12 grant), and the only reason to wait is that two actors on one function is
   the collision; the bound ends the wait. Rollback = the row above, both IAM limbs, sha verified before and read back after,
   the census after. The `org/critical_paths/change_management/` entry is OPENED at the start of the rollback and CLOSED at its
   completion, and it records that the original 15:19Z act ran with NO entry (the face ordered one; the grant never carried the
   path -- the issuer's own defect, owned in 23462). No person is served by these routes today (the page is on no DEV/PROD
   branch, CARD 3), so the harm is to the round's evidence and to this half's blast radius; it is rolled back all the same.
2. **THE FIX-FORWARD IS PACKAGING, NOT A POOL READ.** The two distribution files are **build inputs** -- read once at import,
   never at run time -- and the pool is for artifacts consumers read at run time. So: (i) each reader resolves its file relative
   to its OWN module (`__file__`), never to a repo root, and reads LAZILY or guarded, so an absent file yields a classed error on
   that rule and never an import-time crash of the whole function; (ii) the two JSON files are committed under
   `lib/research/rules/data/` with their provenance (the `~8` deliverables path and sha256) recorded beside them, and the build
   packages that directory; (iii) rk-2's grant WIDENS by `lib/research/rules/` and by `org/critical_paths/change_management/` (an
   issuer widening; the COO's census reads no other round-12 writer of `rules/`); (iv) **the class is censused, not the
   instance**: every import-time repo-relative read in the adapter's import closure is enumerated (a walk of the modules the
   adapter imports for `_REPO_ROOT` / `org/missions` resolutions, denominator printed) and each is packaged or named out of
   scope -- two readers of one store was S117's lesson; N readers of repo paths is this one. No IAM change, no pool write, no
   second store of served data.
3. **rk-2 IS RE-CUT** (issuer amendment, before `~24`'s successor is spawned): **AC7 non-regression** -- the pre/post route
   census above, GET-only, every route printed, MET when the 200 sets are equal and the denominator is the route table's;
   **AC8 packaging** -- the import-closure census reads 0 unresolved repo-relative reads and the zip listing contains every
   packaged data file; the deploy leg of the proof instance cites the change-management entry id. rk-2's redeploy cannot pass
   while any served route regresses.
4. **S127 (rk-7 AC5 needs `BA_US_Equity`'s filings document regenerated under rk-15's producer):** the discriminator is whether
   the re-run makes a VENDOR CALL. If the producer re-renders from the stored analysis with no vendor call, the re-run is the
   issuer's to order. If it calls the vendor, it is under CARD 2 as a ONE-NAME pilot re-run (~USD 1.1) stated on the card.
   `2.0.0_SA_COO~Z` measures the producer's egress (its call graph or `comp-pipescript io`) and states which; until measured it
   is not run.
5. **S119, closed for this act:** the schedule was not changed by the apply (A2.2); its ENABLED state pre-exists; a ranking
   schedule over already-collected metrics is not collection. Whether it should be enabled at all is carried to the round-12
   L10 as a bounds question, not this act's.

**COST of this amendment:** one route census per redeploy of this function. **NON-APPLICATION:** an act that changes only the
policy or only the environment (its write set is what it names), and a function that serves one route.
Push state: LOCAL on SITEZ.
