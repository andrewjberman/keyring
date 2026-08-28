> # ⛔⛔ FALSIFIED IN ITS CENTRAL CLAIM — READ THIS BEFORE ANY LINE BELOW
>
> **2026-08-28 ~02:1xZ. The title of this file is WRONG. `portal-auth` is NOT "one deploy" in the sense
> §1–§4 assert, and the collision they describe DOES NOT EXIST.**
>
> `0.7.0_AE_CloudOps~S` — the same lane that measured the premise — **ran the read-only `terraform plan`
> it should have run before asserting, and falsified itself.** See §8. **The file is preserved rather
> than deleted because six messages cite it and a deleted record cannot correct the readers it already
> reached; §8 is the correction.**

# STANDING FACT: `infra/aws/terraform/portal-auth/` IS **ONE DEPLOY**, AND AN APPLY THERE SHIPS EVERY LANE'S COMMITTED EDGE WORK

**Recorded by:** `2.0.0_SA_COO~Z` · 2026-08-28 ~02:0xZ
**Measured by:** `0.7.0_AE_CloudOps~S` (11806) · **Ruled by:** `1.0.0_SA_CTO~Z` (11814)
**Class:** a STANDING PROPERTY of the stack, **not** tonight's accident. It was true before tonight and
will be true after.

---

## 1. THE MEASUREMENT

```
DENOMINATOR: 1 CloudFront distribution in the account.  NextMarker ABSENT.
  EVTSA9VEHNZVH  "opalinvest.dev portal distribution"  26 behaviors
      shared_advisor_router  PRESENT  v24        public_data_router  PRESENT  v7

infra/aws/terraform/portal-auth/cloudfront-distribution.tf   (the ONLY cloudfront-distribution.tf)
  :66  shared_advisor_router_arn = ... .qualified_arn
  :68  public_data_router_arn    = ... .qualified_arn
  :60  its OWN comment: "qualified_arn auto-bumps every deploy since `publish = true` on each edge"
```

⭐ **"Possibly the same distribution" resolved to CERTAINLY** — with **one** distribution in the
account there was no other outcome available. **The denominator did the work, not the lookup.**

> ⛔ **A SINGLE `terraform apply` OF `portal-auth` REPUBLISHES BOTH ROUTERS AND RE-PINS THE
> DISTRIBUTION TO BOTH NEW VERSIONS. WHOEVER APPLIES FIRST SHIPS THE OTHER LANE'S COMMITTED CHANGE —
> without touching that lane's files, and without it appearing as that lane's work.**

## 2. ⛔ THE HAZARD IS NOT A RACE, AND CALLING IT ONE UNDERSTATES IT

A race implies two appliers contend and one wins. **Here BOTH CHANGES LAND EITHER WAY.** The only
variable is **whose acceptance criteria have run when they do.**

> **THE REAL HAZARD: A CHANGE GOES LIVE BEFORE ITS OWN ACCEPTANCE RUNS.**

⛔ **That is the HALF-LANDED class again** — the same one caught in the Lambda package two hours
earlier, **arriving through a shared stack instead of a member list.**

## 3. ⛔⛔ THE CONTROL THAT WORKED ON THE LAMBDA WILL NOT CATCH THIS

`0.7.0_AE_CloudOps~I`'s *"8 of 9 resources unchanged"* control was sound **because there the blast
radius WAS the diff.** Here it is not:

```
THE PLAN DOES SHOW THE MOVEMENT      qualified_arn  v24 -> v25
WHAT AN APPLIER READS                "an arn version changed"
WHAT IT MEANS                        "and the other lane's FEATURE IS NOW LIVE"
```

> ⭐ **THE PLAN SHOWS THE MECHANISM AND HIDES THE MEANING. A seat can run a perfectly disciplined plan
> review and still not know what it shipped.**

⚠ **AND THE FAILURE SHAPE IS THE ONE THAT HIDES** (`0.7.0_AE_CloudOps~S`): the likely symptom is **not
a regression** — it is **a SUCCESS neither lane can account for**, a route going live that nobody
applied, *"which reads as good news and gets no investigation. **A regression at least prompts a
hunt.**"*

## 4. THE RULING (`1.0.0_SA_CTO~Z`, adopted by the issuing office)

- **(a) THE TWO EDGE CHANGES ARE ONE DEPLOY.** Stop treating them as two lanes' independent applies —
  **the stack makes independence inexpressible.**
- **(b) PRE-APPLY DISCLOSURE, BY THE APPLIER, NAMING BOTH LANES.** Before any `portal-auth` apply,
  enumerate what is COMMITTED-BUT-NOT-RELEASED in **both** routers and write it into the apply record:
  *"this apply also ships `<the other lane's change>`."* Derived by diffing each router's source
  against the **currently pinned version** — `v24` shared-advisor, `v7` public-data.
- **(c) BOTH LANES' ACCEPTANCE CRITERIA READY TO RUN AGAINST THE SAME APPLY.** ⚠ **Not both PASSED
  beforehand — that is impossible, the route does not exist until it ships** — but both seats present
  and expecting it, **so neither change sits live and unexercised.**

⛔ **THIS IS A DISCLOSURE, NOT A GATE.** No approval step is implemented and none should be — **an
agent-made gate is invisible to Andrew.** The mechanism is that the applier **writes down** what else
is going out.

## 5. THE CORRECTION TO A CONTROL THIS OFFICE ISSUED

⛔ **`2.0.0_SA_COO~Z`'s 11732 §4 required *"a did-not-move control over the other 25 behaviors."* THAT
CONTROL CANNOT BE CLEAN ON THIS STACK** — the co-resident router's version **will** move.

An applier holding the original instruction would either **read a real change as a control failure**,
or — worse — **waive the control** because it "obviously" did not matter.

> **CORRECTED, superseding 11732 §4 for any `portal-auth` apply: the control is "25 behaviors unchanged
> EXCEPT the KNOWN co-resident router bump, NAMED IN ADVANCE."**

⭐ **A control whose expected exceptions are enumerated BEFORE the read is a control. One that meets a
surprise and gets waived is theatre.**

## 6. THE DURABLE HALF

> ⭐ **"ONE APPLIER PER MODULE" NOW HAS A PRECISE REFERENT: THE MODULE IS
> `infra/aws/terraform/portal-auth/` — NOT "the edge", AND NOT "a router."**

## 7. HOW IT WAS FOUND, BECAUSE THE METHOD IS THE TRANSFERABLE PART

`2.0.0_SA_COO~Z` told `0.7.0_AE_CloudOps~S` it *"had no reason to look at the etfs route"* — true when
the satellites census ran. That lane finished the measurement anyway:

> ⭐ *"The measurement cost less than the message describing why it was somebody else's."*

⛔ **NO LANE BOUNDARY IS CROSSED BY MEASURING.** The fence is on **acting**. A seat that declines to
measure because the subject belongs to another lane converts a fence meant to prevent collisions into
one that manufactures blind spots.


---

# 8. ⛔ CORRECTION — §1–§4 ARE FALSIFIED. THE COUPLING IS NOT REAL, AND THE REAL DEFECT IS WORSE.

**Author of the correction:** `0.7.0_AE_CloudOps~S` (11880), against its own 11806.
**Recorded by:** `2.0.0_SA_COO~Z`, who committed the falsified claim.

## 8.1 WHAT IS FALSE

> ⛔ **"A single `terraform apply` of `portal-auth` republishes BOTH routers." FALSE.**

```
terraform plan, infra/aws/terraform/portal-auth, READ-ONLY:
  Plan: 0 to add, 1 to change, 0 to destroy
  the 1 = aws_cloudfront_distribution.portal, in-place.  NO aws_lambda_function in the diff.
MECHANISM AT SOURCE, lambda-edge.tf:245-248 -- the edge functions do NOT track index.mjs:
  s3_bucket opal-313476888478-lambda-artifacts · s3_key portal-auth/shared-advisor-router.zip
  source_code_hash <- that OBJECT's content-sha256 metadata
```

⛔ **TERRAFORM CANNOT SEE A SOURCE-FILE EDIT AT ALL.** `qualified_arn` bumps only when the **ARTIFACT**
changes, and **no artifact has changed.** `public-data-router` likewise has **no pending change** (9 of
10 source literals present in the deployed bundle; the single absentee is inside a **COMMENT**, and
comments do not survive bundling).

> **THERE WAS ONE PENDING EDGE CHANGE, NOT TWO.**

⚠ **THE ERROR WAS READING THE CONFIG INSTEAD OF RUNNING THE PLAN.** `publish = true` + `qualified_arn`
is **mechanically plausible** and wrong — it describes what would happen *if* the function resource
changed, and nothing makes it change.

## 8.2 ⛔ AND THE PLAN SHOWS SOMETHING WORSE THAN THE COLLISION IT DISPROVED

```
the plan's ONE change:
  + path_pattern = "/api/scoped/satellites/*"
  + lambda_arn   = ...function:shared-advisor-router:24
```

> ⛔ **IT WIRES THE NEW ROUTE TO v24 — AND v24 DOES NOT CONTAIN THE SATELLITES CODE.**

```
artifact portal-auth/shared-advisor-router.zip   LastModified 2026-08-21T16:00:13Z
satellites branch @40697fe79d                     committed    2026-08-27T22:42Z  -- SIX DAYS LATER
deployed bytes:  POSITIVE CONTROLS 'Platinum summary files must be accessed' PRESENT ·
                                   'platinum/advi/' PRESENT
                 SATELLITES '/api/scoped/satellites/' ABSENT · 'platinum/satellites/registry.json' ABSENT
```

⛔ **THE ROUTE WOULD GO LIVE DEAD, AND EVERY INSTRUMENT WOULD READ GREEN:** the apply succeeds, the
behavior exists so a cache-behavior census finds it, and `comp-routes` shows it on the DESIRED plane.
**Only the actual request fails** — surfacing as a **403/404 indistinguishable from a refusal**, which
is exactly what `TO-5-DS` AC3 exists to prevent, arriving from the **serving** side instead of the
producer side.

> **PRECONDITION, NOW EXPLICIT: the artifact must be REBUILT from `@40697fe79d` and UPLOADED before any
> apply.** ⭐ **An unapplied route fails honestly; a route wired to a version lacking its own code fails
> while reporting success.**

## 8.3 ⭐ THE METHOD FINDING, WHICH SURVIVES EVERYTHING ELSE IN THIS FILE

> **THE DEPLOYED BUNDLE IS MINIFIED. MINIFICATION DESTROYS IDENTIFIERS AND PRESERVES STRING LITERALS.**

An earlier byte-probe had **2 of 3 controls fail** and was **correctly discarded** — the two failures
were **identifiers**, the survivor a **literal**. ⛔ **A deployed-bundle probe must use LITERALS ONLY.**
Only with three literal positive controls PRESENT does the satellites ABSENT become a real absence
rather than a mangled read.

⚠ **AND A CITATION CORRECTED:** `1.0.0_SA_CTO~Z`'s ruling cited that lane as having *"already
demonstrated"* the diff was measurable. **It had demonstrated it FAILING.** Measurable **now**; not when
that was written.

## 8.4 WHAT STILL STANDS FROM §1–§7

- **§4(b) PRE-APPLY DISCLOSURE** — stands **on its own merits**. Writing down what else goes out is
  good practice whether or not a coupling forces it.
- **§5's CORRECTED CONTROL** — stands, and is **reinforced**: the expected-exception set is now
  *"nothing else moves"*, and an applier must still state it before reading.
- **§7's METHOD POINT** — stands, **and cuts against this file's own author**: *no lane boundary is
  crossed by measuring.* ⛔ **The lane that measured then measured AGAIN and overturned itself; the
  issuing office committed the first read to the durable record without asking for the plan.**

## 8.5 THE LESSON THIS OFFICE OWES

⛔ **I committed a durable record off a config read that had not been plan-tested — in the same session
in which I twice criticised acting on unmeasured premises, and roughly forty minutes after writing that
*"does this already exist?" is not yet a reflex at the moment of cutting.*** ⭐ **The transferable form:
A DURABLE RECORD RAISES THE EVIDENCE BAR RATHER THAN LOWERING IT — a claim worth committing is a claim
worth plan-testing, because committing it is what makes the error expensive to reach.**
