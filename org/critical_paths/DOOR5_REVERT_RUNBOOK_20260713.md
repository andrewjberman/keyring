# DOOR 5 -- PRE-STAGED REVERT RUNBOOK

**Author:** `0.7.0_AE_CloudOps` · **2026-07-13** · **NOTHING IN HERE HAS BEEN APPLIED.**
**Commissioned by COO:** *"Stage the revert now. If we cannot re-arm it, we do not open it."*

---

## >> READ THIS FIRST: THE PLAN AS BRIEFED CONTAINS A CONTRADICTION <<

The plan is: **open Door 5 (de-collide) -> the chain runs once -> CVO reads the served row -> RE-ARM.**

**"RE-ARM THE COLLISION" IS SPELLED "RE-KILL THE BRONZE FEED."**

They are the same object. The collision *is* the outage:

```
DE-COLLIDE  -> sync_scripts() succeeds -> the bronze runner lives -> transactions silver resumes
RE-COLLIDE  -> sync_scripts() FATALs   -> the bronze runner dies   -> transactions silver goes dark AGAIN
```

**And `silver/transactions` is the DIRECT INPUT TO NNA** -- the very number we would be opening the door to serve.
So the plan's final step restores the outage that motivated it, on the feed the served row is computed from.

> ## **YOU CANNOT FIX BRONZE AND KEEP THE COLLISION GUARD. THERE IS NO SEQUENCE IN WHICH BOTH ARE TRUE.**
> ### Once you de-collide, **the collision guard is SPENT, PERMANENTLY.** That may be acceptable -- but it must be
> decided KNOWINGLY, in advance, not discovered at re-arm time.

**AND THE QUICK FIX DOES NOT EXIST ANYWAY (COO):** there are **TWO** fatal collisions. De-colliding
`build_assets_dim.py` alone leaves the runner FATALing on `_orion_api_silver_lib.py`.

---

## >> AND THEREFORE THE QUESTION NOBODY HAS ASKED: DOES THE DOOR NEED TO OPEN AT ALL? <<

**CTO, ruling on the observe run:**
> *"The observe run is a **DIRECT script invocation** -- it does **not** go through `sync_scripts()`, so the
> collision is irrelevant to it."*

**If a direct invocation bypasses `sync_scripts()`, then the chain can be run WITHOUT DE-COLLIDING --**
**the collision stays armed, gold's step-zero guard stays intact, and Door 5 is never opened.**

*I have NOT grounded that the FULL gold chain can be driven this way (the observe run is two scripts; the chain is
63 steps, and `sync_scripts()` is how the code reaches the box in the first place). **It is a QUESTION, not a
finding.** But it is the cheapest possible answer and it must be killed or confirmed BEFORE anyone de-collides:*

> ## **IF THE CHAIN CAN RUN BY DIRECT INVOCATION, THE ENTIRE OPEN/RE-ARM DANCE IS UNNECESSARY AND WE KEEP THE ONE CONTROL THAT REQUIRES NOBODY'S COOPERATION.**

---

## ARM A -- THE CHOKEPOINT (the REAL control: designed, sentinel-gated, audited)

**Current state, verified on the LIVE primitive 2026-07-13:**
```
aws lambda get-function-configuration --function-name inf-gold-trigger --query 'Environment.Variables'
   INF_GOLD_DISPATCH_RELEASE : None            <- absent  => HELD
   INF_GOLD_DISPATCH_HOLD    : SET (1568 chars)
   POSITIVE CONTROL: 3 vars visible -> `None` is a REAL ABSENCE, not a read failure.
```

**A GO sets `INF_GOLD_DISPATCH_RELEASE = "RELEASED-BY-CTO-AND-COO-COSIGN"` in
`infra/aws/terraform/inf-pipeline/lambdas.tf`.**

### RE-ARM (revert)
```
1. Remove the INF_GOLD_DISPATCH_RELEASE line from lambdas.tf   (leave INF_GOLD_DISPATCH_HOLD in place)
2. .tools/safe-apply.sh                                        (Rule 18 -- NEVER bare `terraform apply`)
3. VERIFY ON THE LIVE PRIMITIVE, not on the plan:
     aws lambda get-function-configuration --function-name inf-gold-trigger \
       --query 'Environment.Variables.INF_GOLD_DISPATCH_RELEASE'
   MUST return `null`. A DESIRED-only (terraform) verdict is NOT a verification (Rule 22a).
```

> ## **THIS IS NOT A ONE-COMMAND RE-ARM. IT IS A TERRAFORM CYCLE.**
> **`aws lambda update-function-configuration` IS BANNED (Rule 1 -- Terraform is the ONLY Lambda deploy
> mechanism).** *COO has told Andrew the re-arm is "one command." For the SOUND path it is not, and the difference
> is minutes during which the chain is armed. Price that honestly before promising it.*

**AND `INF_GOLD_DISPATCH_HOLD` ALONE DOES NOT HOLD ANYTHING.** The control is two-variable and the polarity matters:
`released = (RELEASE is not None AND RELEASE == SENTINEL)`. **Leaving `HOLD` set while `RELEASE` carries the
sentinel is RELEASED.** The re-arm must remove `RELEASE`; editing `HOLD` is cosmetic.

---

## ARM B -- THE COLLISION (an ACCIDENT, not a designed control -- and re-arming it re-breaks bronze)

**BYTE-STATE SNAPSHOTTED 2026-07-13 (rc checked on every copy; sha256 independently MATCHES the hashes the
runner's own FATAL log printed):**
```
code/gold/build_assets_dim.py          8498 B   sha256=1c5ffce722037f4a
code/silver/build_assets_dim.py        9244 B   sha256=453c1950ee24b17a   <- the collider (07-10T23:37:24Z)
code/gold/_orion_api_silver_lib.py    21132 B   sha256=2ac284169dd54af1
code/silver/_orion_api_silver_lib.py  28694 B   sha256=89ddfda0fee78132   <- the collider (07-13T12:48:24Z, DS AoR)
```
Snapshots held at: `<scratchpad>/door5_revert/{gold,silver}__<file>`

**A de-collide is therefore REVERSIBLE.** *(An IRREVERSIBLE de-collide must never be attempted, GO or no GO.)*

### RE-ARM (only if the collision is deliberately chosen as the guard -- see the contradiction above)
```
aws s3 cp <snapshot>/silver__build_assets_dim.py \
          s3://opal-data-inf/code/silver/build_assets_dim.py
# then VERIFY the FATAL returns -- do not assume it:
#   the next runner boot must FATAL on the collision. An unexercised re-arm is a hypothesis.
```
> **AND UNDERSTAND WHAT YOU JUST DID: the bronze feed is dark again, and `silver/transactions` -- the direct
> input to NNA -- stops advancing. You have re-armed the guard by re-breaking the pipeline.**

---

## WHAT I AM NOT STAGING, AND WHY

- **I am not staging a bronze restart / kick.** Under the INF hold; the test is functional, not lexical:
  *would obeying this ADVANCE THE INF CHAIN? If yes: DO NOTHING.*
- **I am not staging a `code/silver/` tidy-up.** The tidy-up IS the door.
- **I am not staging an `aws lambda update-function-configuration` fast-path.** It is banned (Rule 1), and a
  banned-but-fast revert is exactly the thing that gets reached for at 2am.

## STANDING

**Nothing applied. Nothing de-collided. Nothing tidied. Nothing restarted. `code/silver/` untouched.**
**The FATAL stands, and it is still the only control in the stack that requires nobody's cooperation.**
