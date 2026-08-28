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
