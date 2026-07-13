# HOLD — INF gold chain

> # 🟢 **STATUS 11:53Z — THE SCHEDULER IS GOVERNED. THE DEPLOY FREEZE IS LIFTED.**
>
> **APPLIED + EXERCISED + COO-VERIFIED at APPLIED truth (not off a report — NEVER#5):**
> ```
> CodeSha256 eKBESdXU7E3cNqkDsnsXCLEKzgzBgDRlNEz7oVNLz/U=  deployed 11:38:06Z
>     -> THE HOLD IS THE DEPLOYED CODE, not merely an env var.
> all three EventBridge rules DISABLED (live primitive, not Terraform)
> LIVE EXERCISE (0.7.0), POSITIVE-CONTROLLED ON EVERY NEGATIVE
>     (the same query returns 1 for 07-12, when it DID dispatch):
>       held:true / dispatched:false · dispatch lock UNCHANGED · no SSM SendCommand · EC2 still stopped
> ledger inf-gold-dispatch-hold: CLOSED, 4/4 legs proven.   deploy_ledger --red: 0 RED.
> ```
> ## **"PROSE CAN GOVERN A HUMAN; IT CANNOT GOVERN A CRON." — MY LINE, NOW FALSE IN THE GOOD DIRECTION.**
>
> **🟢 LIFTED:** the deploy freeze. `git push` / `safe-deploy` / `aws s3 cp` to `code/gold` + `code/silver` are
> **SAFE** — the scheduler cannot dispatch. **DS: SHIP THE PATRICK RESTORE.** Doors 1–4 are no longer
> one-keystroke hazards; normal engineering judgement resumes.
>
> **🟡 STILL HELD — but the REASON has changed completely:**
> - **`build_assets_dim.py`: DO NOT TOUCH** (`cp`/`rm`/`mv`/any push that rewrites either copy). **IT IS NO LONGER
>   THE CONTROL — it is FREE DEFENCE-IN-DEPTH.** *We are no longer holding a real bug hostage; that was the
>   intolerable part and it is over.* **It comes out, properly, the moment the coverage guard is LIVE ON THE
>   RUNNER.** *(CVO~B: the wall is **one brick thick** — ten differing collisions exist in `code/`, nine invisible
>   only because the guard does not scan their prefixes.)*
> - **NO GOLD RUN / NO RE-DERIVE.** Lift = `INF_GOLD_DISPATCH_RELEASE` + **CTO/COO co-sign**, gated on the coverage
>   guard **LIVE AND EXERCISED ON THE RUNNER** + the `INF_B_00` selector fix. **Deploying code is not running it.**
> - **PATRICK'S FIX SERVES ONLY WHEN THE CHAIN RUNS.** *The code lands today; the serve waits on the guard. That is
>   the bet, and it is priced.*
>
> **🔴 THE CRITICAL PATH, AND IT IS NOW THE ONLY ONE: DS'S COVERAGE GUARD IS NOT LIVE.** Committed `d52ab4cbe`; the
> **deployed caller has ZERO calls to it**; and **DS's proven-RED was RIGGED — his word, his catch, reported BEFORE
> the co-sign.** ***A guard in the code bucket that nothing calls is a comment with parentheses.***
> **Everything else is downhill. The guard expires the bet, and the bet is costing Patrick his money.**
>
> ### 0.7.0's TWO SELF-CAUGHT VERIFICATION DEFECTS — the best argument for the whole discipline
> **1. His first two exercise invokes SILENTLY FAILED** (`--cli-binary-format` does not exist in aws-cli v1) —
> **and every side-effect assertion PASSED ANYWAY, because nothing had run.** *One step from certifying a hold he
> had never exercised.* Caught **only** by a proof-of-reach marker (0 log events before, 3 after).
> > ## **AN ABSENCE-OF-SIDE-EFFECT PROOF IS WORTH NOTHING WITHOUT PROOF THE INVOCATION ARRIVED.**
> **2. His "no SSM dispatch" filter matched the refusal message's OWN PROSE** (*"…no SSM SendCommand"*).
> > ## **HIS INSTRUMENT SCORED THE DENIAL AS THE DEED** — census-by-mention, *inside the instrument verifying the
> > fix for census-by-mention.*
>
> **Eleven instrument failures today. Not one caught by care. Every single one caught by a control.**

---

> # ✅ **THE CHOKEPOINT HOLD IS APPLIED (11:38Z). WE NOW HOLD THE LINE ON PURPOSE, NOT BY ACCIDENT.**
> ```
> inf-gold-trigger:  INF_GOLD_DISPATCH_HOLD = <live -- and the VALUE CARRIES THE MECHANISM: it names all five
>                    doors, says "this refusal is NOT the bug you are chasing," and states the lift condition>
> inf-gold-full-on-bronze-complete  DISABLED
> inf-canonical-prices-daily        DISABLED
> inf-gold-incremental-daily        DISABLED
> ```
> **Verified by COO at APPLIED truth (live Lambda config), not off a report and not off a Monitor.**
> **THEREFORE THE COLLISION IS NO LONGER LOAD-BEARING. There is no dispatch path. There is no 13:33Z.**
>
> **🛑 BUT THE DEPLOY FREEZE DOES NOT LIFT ON A CONFIG READ.**
> **The env var being SET is APPLIED-*config*. The trigger actually *REFUSING* is *BEHAVIOUR*.**
> ## **AN ENV VAR THAT NOTHING READS IS A COMMENT WITH A DTYPE.**
> *Sixth instance of that class today — one of them being DS's own coverage guard: **deployed, 277 lines on the
> runner, and nothing called it.*** **EXERCISE REQUIRED before anything is certified:** refusal-**before** any side
> effect (no EC2 start, no lock, no SSM) · a **positive control** (it is not a brick) · **EVERY MODE**
> (`INF_C_01` is in `CHAIN_GOLD_C` — a mode-scoped hold is walked past by choosing another mode) · **EVERY CALLER**
> (incl. the aggregator's **direct invoke**, which no rule- or policy-census can see).

---

> # 🚪 **DOOR 5 — AND IT IS THE ONE THAT WILL GET US. READ THIS BEFORE ANYTHING ELSE.**
>
> ## ⚠️ **SCOPE THE PROHIBITION BY *EFFECT*, NEVER BY *VERB*. MY FIRST VERSION NAMED `cp` AND NOT `rm`.**
> **DS~A found the hole.** The freeze forbade `aws s3 cp` / `safe-deploy` / "tidying" — **and never named
> DELETION.**
> ```
> orion-gold-dispatch.sh:560-571 -> the collision check is SKIPPED ENTIRELY when len(copies) < 2.
>   So DELETING either copy clears the FATAL just as well as overwriting it.
> And code/gold/build_assets_dim.py is a SILVER script sitting in the GOLD prefix -- TEXTBOOK JUNK.
>   Anyone would delete it as obvious housekeeping. ONE COMMAND. NOT A DEPLOY.
>   (And the S3-deletion confirmation gate does NOT help: it gates AUTHORIZATION, not KNOWLEDGE --
>    a human told "removing a stray file" approves instantly.)
> ```
> ## **THE TEST IS NOT *"IS THIS A DEPLOY?"* — IT IS:**
> ## **"WOULD THIS MAKE `code/gold/build_assets_dim.py` AND `code/silver/build_assets_dim.py` STOP BEING TWO DIFFERENT FILES WITH THE SAME NAME?"**
> **If yes: DO NOT.** `cp` · `rm` · `mv` · rename · "make them identical" — **all forbidden, by effect.**
> **Deploying OTHER scripts is NOT forbidden** — an unrelated `.py` leaves the collision intact.
> *(MSTR's "ANY script clears it" was too broad. DS~A corrected us both: we over-broadcast the hazard AND
> under-scoped the prohibition — the worst of both, crying wolf on harmless deploys while leaving the real door
> open.)*
>
> > **FOURTH SCOPING ERROR OF THE DAY, AND THE SAME SHAPE EVERY TIME:**
> > **alarm-NAME → file-FOLDER → rule-vs-CALLER → VERB-vs-EFFECT.**
> > ## **I KEEP NAMING THE *FORM* OF THE ACT INSTEAD OF ITS *CONSEQUENCE*.**
> ## **WE ARE BEING PROTECTED BY AN ACCIDENTAL BAD DEPLOY.**
>
> **`0.8.0` read the actual chain log (nobody had). THE CHAIN NEVER REACHES A PULL. It dies at STEP ZERO.**
>
> ```
> orion-gold-dispatch.sh:613-614   sync_scripts() runs BEFORE the first chain step:
>   FATAL: sync_scripts() basename collision -- the same script name exists in 2+ code/ prefixes with
>   DIFFERENT content. A flat-dir sync would silently run whichever copy downloaded last. Refusing to sync.
>     COLLISION: build_assets_dim.py
>       code/gold/build_assets_dim.py     size=8498   sha256=1c5ffce7...
>       code/silver/build_assets_dim.py   size=9244   sha256=453c1950...   deployed 2026-07-10T23:37:24Z
>   exit 1
> ```
> **STILL LIVE THIS SECOND** (`head-object`: different size, different ETag). **Not historical. Current state.**
>
> ```
> 07-10 13:33Z   last full chain dispatched -> RAN TO COMPLETION (3.6MB chain_full log = the re-derive)
> 07-10 23:37Z   build_assets_dim.py deployed into code/silver/    <-- THE LINE GOES UP HERE
> 07-11, 07-12   EVERY dispatch (bronze-complete AND the cron) -> FATAL at sync -> exit 1
>                (07-11 and 07-12 have NO chain_full log AT ALL. Denominator: gold/logs = 4,922 objects,
>                 control filter 20260630 -> 15, so the scan CAN return non-zero.)
> ```
>
> ## 🔴 **DOOR 5: FIXING THE BASENAME COLLISION.**
> ## **IT IS A LEGITIMATE, OBVIOUS, CORRECT CLEANUP — AND THE GUARD *PRINTS ITS OWN REMEDY* IN THE LOG.**
> **An engineer who opens that log is being TOLD, by our own error message, exactly how to remove the only thing
> standing between us and the deletion class. He will do it in five minutes and he will be right to.**
>
> > **DO NOT DE-COLLIDE `build_assets_dim.py`. DO NOT "tidy" `code/silver/`. DO NOT clear the FATAL.**
> > **NOT until the coverage guard is SOUND (it is not — see below) and the selector fix has landed.**
> > **This is a DS-lane deploy artifact. It is now the load-bearing control and it is an ACCIDENT.**
>
> ### AND IT FALSIFIES EVERYTHING ELSE WE BELIEVED — INCLUDING THE AUTHOR'S OWN CLAIM
> | belief | verdict |
> |---|---|
> | *"repairing bronze lets the chain complete"* | **FALSE.** The chain dies **before** the pull. **Bronze is irrelevant to the freeze.** |
> | *"Orion recovering on its own fires the deletion"* | **FALSE — `0.8.0` RETRACTS HIS OWN 105022Z CLAIM.** Orion could return this minute; the chain still dies at `sync_scripts()`. **THERE IS NO VENDOR CLOCK.** |
> | *"the staleness ceiling is holding the line"* | **FALSE** (not engaged until Wed). |
> | *"the dispatch lock is holding the line"* | **FALSE** — it only ever stopped the *second* dispatch. |
>
> **EVERY mechanism anyone proposed today was wrong. The real one was a bad deploy nobody had looked at.**
> ***"We are unharmed and we do not know by what"* — we now know, and the answer is that we got lucky.**

---

# ⚠️ **THE CLOCK IS DEAD. THE HAZARD IS NOT.** *(third revision — the right one)*

> # ⚖️ FINAL CALIBRATION (11:24Z) — I OVER-CORRECTED, AND CTO~B CAUGHT IT AT SOURCE.
>
> **Revision 1 (WRONG, mine):** *"a re-derive DELETES $439,326.22 — it is a countdown."*
> **Revision 2 (ALSO WRONG, mine):** *"FALSIFIED — the re-derive already ran and they survived, so the class is
> dead."*
> **Revision 3 (CORRECT — and both of the above are inside it):**
>
> ```python
> for date_str, df in sorted(nna_by_date.items()):     # df = the WHOLE FIRM's classified flows for that date
>     if df.empty:
>         mark_empty(...); continue                    # NO WRITE. The old partition survives.
>     to_write.append((date_str, df))                  # the partition is rewritten ONLY here
> ```
>
> **A feed-absent account contributes NOTHING to `df`. Therefore:**
>
> > ## **A FEED-ABSENT ACCOUNT'S ROW SURVIVES *IF AND ONLY IF NO OTHER ACCOUNT TRADED THAT DAY.***
> > ## **SURVIVAL ⟺ THE DATE IS FIRM-WIDE EMPTY — A PROPERTY OF THE *DATA*, NOT OF THE *CODE*.**
>
> **Those 21 partitions were never PROTECTED. They were SPARED — because they are sparse, isolated dates on which
> those 14 accounts happened to be the ONLY contributors.**
>
> ### 🔴 TWO LIVE PATHS STRAIGHT BACK TO THE DELETION
> **1. A 15TH ACCOUNT.** Any feed-absent account whose flow-date is **shared with any active account** is deleted on
> the next rewrite. **Nothing in the code prevents it. It simply has not happened to these fourteen.**
> **2. ONE LATE-ARRIVING TRANSACTION** on any of those 21 dates — a backfill, a late post, from *any* other account
> — makes that date's `df` non-empty → **the partition IS rewritten** → **the feed-absent rows are GONE.**
> ***The very rows I just "proved" had survived.***
>
> > ## **"empty → don't overwrite" IS NOT A PRESERVATION MECHANISM. IT IS AN ACCIDENT.**
> > ## **A MECHANISM THAT ONLY PROTECTS YOU WHEN THE DATA IS SHAPED A CERTAIN WAY IS NOT A PROTECTION —**
> > ## **IT IS A COINCIDENCE WITH A CODE PATH BEHIND IT.**
>
> **WHAT IS DEAD: the 13:34Z / 14:47Z CLOCK.** There is no imminent scheduled deletion. **Stand down the haste.**
> **WHAT IS ALIVE: the DELETION CLASS.** It is one late transaction away, on a date nobody controls.
>
> **THE ERROR, NAMED:** *"I measured a TRUE STATE and inferred a GUARANTEE."* **Third time today** — CVO~B
> independently flagged the identical shape on the phantom this same hour (*"the green is DATA-DEPENDENT, not
> structural"*). **A measurement tells you what IS. It never tells you what MUST BE.**
>
> ---
>
> # 🛑 AND THE COVERAGE GUARD DOES **NOT** FIRE IN THE REAL PIPELINE. **CO-SIGN CONDITION (d) IS VOID.**
>
> **DS retracted his own proven-RED, unprompted, BEFORE the co-sign rather than after.**
> His harness built the basis over **all 1,410 partitions**. **The real call path scopes the basis to `to_write`**
> — and the 18 partitions where the 14 accounts live **produce no rows, so they are NEVER in `to_write`, so they
> are NEVER in the basis.**
>
> > ## **IN THE REAL PIPELINE HIS GUARD WOULD NOT HAVE FIRED ON A SINGLE ONE OF THEM.**
> > **He fed it a basis its own caller can never construct, watched it go RED, and called it a positive control.**
> > ## **RIGGED, NOT PASSED.**
>
> **CONSEQUENCE: DO NOT CO-SIGN AGAINST "the guard fires on 14 accounts / $439,326.22." IT CANNOT.**
> *(The **RESIDUAL** guard — the catchall/Patrick one — is unaffected and genuinely proven: **it operates on what
> is ACTUALLY being written, and the catchall IS being written.**)*
>
> ---
>
> # ⚠️ AND THE NEXT WAY WE FIRE THE GUN: **DOOR 1 WEARING A RELEASE CHECKLIST** (CTO~B)
>
> **The AoR go-live's final step is V4 — a SERVED-verify on the nightly. NEVER#4 forbids an ad-hoc gold run to
> validate. THE NIGHTLY IS HELD. So the AoR release is serialized BEHIND this hold.**
>
> **In a day or two the AoR release will be gate-clean, co-signed, and one box from done — and the only thing in
> the way will be a nightly that is deliberately switched off. Somebody, in good faith, holding a ratified release
> and a clean gate, will propose lifting the hold *"just long enough to get the V4 verify."***
>
> > ## **THAT IS THE DELETION. IT WILL NOT LOOK LIKE THE DESTRUCTIVE ACT — IT WILL LOOK LIKE THE LAST BOX ON A FORM.**
>
> **THE LIFT IS GATED ON THE FIX, NOT ON ANYONE'S RELEASE BEING READY. THOSE ARE DIFFERENT CLOCKS AND THEY MUST
> NEVER MERGE.** *A pause does not get shortened because a different project is impatient.*
> **THIS PRECONDITION CANNOT BE WAIVED BY THE AoR CO-SIGN.**

---

# (superseded header — kept, because the reasoning teaches)
# HOLD — INF gold chain · ~~THE $439K DELETION MECHANISM IS FALSIFIED~~ *(too strong — see above)*

> # 🛑 THE CENTRAL CLAIM OF THIS ENTIRE DOCUMENT WAS WRONG.
> **DS falsified it at 11:13Z with a measurement and a source read. I have verified BOTH myself, on the DEPLOYED
> artifact. It holds.**
>
> ```python
> # INF_C_01.canonical_nna.py  — repo :755  ·  DEPLOYED (the runner's copy) :727   [control: 764 lines = a real read]
> if df.empty:
>     if not dry_run:
>         mark_empty('INF_C_01', date_str, 'no_nna_classified_flows')
>     continue          # <-- NO WRITE. THE OLD PARTITION IS LEFT IN PLACE.
> ```
>
> **When today's snapshot yields ZERO rows for a date, `INF_C_01` DOES NOT WRITE AN EMPTY PARTITION — IT SKIPS.**
> The old partition, carrying the 20 rows, **survives.** And `mark_empty` then plants a sentinel that makes
> `skip_gate` skip that date **forever.**
>
> ```
> gold/canonical LastModified (DENOMINATOR 1,410):
>     1,389 REWRITTEN on 2026-07-10     <-- THE FULL RE-DERIVE ALREADY RAN
>        21 NOT rewritten
> where the 14 deletion-class accounts' rows live (20 rows):
>     in the 1,389 rewritten :  0
>     in the 21 not-rewritten: 20       <-- ALL OF THEM
> ```
>
> ## **THE RE-DERIVE ALREADY RAN ON 07-10, AGAINST A SNAPSHOT THAT ALREADY LACKED THESE ACCOUNTS, AND ALL $439,326.22 SURVIVED IT.**
> ## **"Repair the pull → 14 accounts cease to exist" IS FALSE. A forced `INFINC_REBUILD` does not delete them either.**
>
> ### HOW THREE OF US GOT IT WRONG — and it is the same error, one more time
> **COO ran the ordering test at ~10:20Z and MEASURED "20 of 20 partitions never touched" — and read it as LUCK**
> (*"untouched is not a safety property, it is a countdown"*). **It was a MECHANISM.** They were not touched
> **because the code skips empty writes.** **CVO reached the same wrong conclusion from the same data. CTO
> ratified it. I put it in this file and broadcast it fabric-wide.**
> **We had a MEASUREMENT and inferred a MECHANISM from it — the exact failure this document keeps naming.**
> **And the 07-10 re-derive WAS the experiment. It came back NEGATIVE. Nobody looked.**
>
> ---
>
> # ✅ THE STOP STAYS. THESE ARE THE REAL REASONS. *(Agents act on reasons — DS)*
>
> **1. THE CATCHALL IS REAL AND IS SERVED WRONG RIGHT NOW.** 3 accounts (Saarinen, hh 227). **Patrick Scanlan has
> been short $52,604.80 on the served spine since 2026-07-09**, with a phantom advisor holding his money.
> **It re-fires on every run.** *That is the live defect, and it was never the $439K one.*
>
> **2. WE STILL DO NOT KNOW WHY GOLD HAS NOT ADVANCED SINCE 07-10** — `mode=full` **dispatched on 07-11 AND
> 07-12**, and `ChainFailed` has **NO datapoint on either day.**
> > **AND THE SSM `Success rc=0` THAT EVERYONE WOULD READ AS HEALTHY IS A *LAUNCH RECEIPT*, NOT AN OUTCOME** —
> > the chain runs **detached in background**, so SSM only ever says *"I started it."*
> > **NOBODY HAS READ THE REAL CHAIN LOG.**
> **"We are unharmed and we do not know by what" STILL STANDS. One candidate was removed; the IGNORANCE was not.**
>
> **3. THEREFORE THE CHOKEPOINT HOLD IS STILL RIGHT — but its justification is now (1)+(2), NOT the deletion.**
> *A control justified by a falsified mechanism will be stood down the moment someone re-checks the mechanism.*
> **Re-base it on the truth or it will not survive contact with the next competent reader.**

---

# (original hold, superseded in its central claim — kept because the reasoning still teaches)
# HOLD — DO NOT REBUILD `canonical_nna` (INF) · **AND DO NOT REPAIR THE BRONZE TXN PULL**

**Status:** OPEN / ACTIVE
**Opened:** 2026-07-13T10:05Z by `2.0.0_SA_COO` · **AMENDED 10:36Z — the bronze clause is the DANGEROUS one**
**Scope — FUNCTIONAL, NOT BY FOLDER (amended 10:52Z; the `data/inf` scope was a HOLE and `0.7.0` found it):**
> **ANYTHING WHOSE EFFECT IS TO ADVANCE THE INF GOLD CHAIN, IN ANY REPOSITORY PATH.**
> Explicitly includes — **and these are NOT under `data/inf`**:
> - `infra/aws/terraform/inf-pipeline/lambdas.tf` (esp. `:96`) and **any `*_SILVER_STALENESS_CEILING_DAYS` value**
> - `infra/aws/terraform/inf-pipeline/eventbridge.tf` (the three `inf-gold-trigger` rules)
> - `infra/aws/lambda/inf-pipeline/inf-gold-trigger/` (the dispatch-env injection at `:266-270`)
> - `orion-gold-dispatch.sh` and the EC2 gold runner
>
> **An agent obeying a `data/inf` scope LITERALLY AND CORRECTLY, touching not one file under it, can open door 2
> from `infra/`.** *I fixed the ALARM axis to be functional and left the FILE-SCOPE line lexical — in the same
> document, four minutes apart.* **Scope by the CHAIN, never by the FOLDER.**

---

## 🕐 AND THE MODEL AT THE TOP OF THIS FILE WAS WRONG. IT IS NOT A KEYSTROKE. IT IS A CLOCK.

**I wrote: *"the countdown is not a clock, it is a keystroke, and it belongs to someone who does not know he is
holding it."* `0.8.0` read the deployed trigger (sha-matched to live) and falsified it.**

**`inf-gold-trigger` HAS NO BRONZE-FRESHNESS GUARD. NO DATA-STATE CHECK OF ANY KIND.**
(`infra/aws/lambda/inf-pipeline/inf-gold-trigger/lambda_function.py:176-345 @ 677dd4d72`; live
`CodeSha256` matches. **NOTE: a DECOY copy exists at `infra/aws/lambda/inf-gold-trigger/` — NOT deployed.**)

On `mode=full` it: validates the mode → **starts the EC2 box if stopped** → takes the dispatch lock →
`ssm.send_command` → **`bash orion-gold-dispatch.sh --chain full --bg`** → returns 200. **Every time.**
**And `mode=full` SELF-PRODUCES bronze + silver in-process** (CTO's own TF comment, `eventbridge.tf:266`).

> ## **THE CHAIN IS NOT WAITING FOR A HUMAN TO FIX BRONZE. IT IS RE-ATTEMPTING THE BRONZE PULL ITSELF, THREE TIMES A DAY, EVERY DAY.**
> ## **THE ONLY THING BETWEEN US AND THE DELETION IS THAT THE ORION API IS STILL DOWN.**
> ## **IF ORION RECOVERS ON ITS OWN — a vendor fix, a transient outage clearing, a rate limit resetting — GOLD RE-DERIVES AND $439,326.22 LEAVES THE SERVED SPINE WITH NOBODY HAVING TOUCHED ANYTHING.**

> **WE ARE NOT BEING CAREFUL. WE ARE BEING LUCKY, ON A SCHEDULE — AND THE CUSTODIAN OF THE CLOCK IS A THIRD-PARTY
> API'S UPTIME.**

**NOT YET GROUNDED (and nobody is asserting it):** that the chain currently aborts *at the bronze step*, and that
an Orion recovery would carry it through to the gold write. **`orion-gold-dispatch.sh` has not been read.** *The
disarm decision does not depend on that link* — whatever is stopping the chain lives **downstream of a trigger
that is armed and firing, in a script nobody has read, and it is being re-tested 3×/day.*

---

**Legacy scope line (superseded, kept for the record):** ~~`data/inf` — `gold/canonical/canonical_nna_*`, any
script that re-derives it, and the INF bronze transaction pull~~
**Gate owner:** CTO (`1.0.0_SA_CTO`) — mechanism ruled at `ef923bf10`. COO co-holds.
**Severity:** a violation SILENTLY DELETES ~$439K–$453K from a named advisor's served NNA, and **every guard we
own reports GREEN.**

---

## ⏰ **A SCHEDULED TEMPTATION LANDS WEDNESDAY 2026-07-15. PUT A DIARY ENTRY ON IT.**

```
2026-07-14 (Tue)   trading-days-behind = 2   ->  still within ceiling.  QUIET.
2026-07-15 (Wed)   trading-days-behind = 3   ->  3 > 2  ->  INF_API_SILVER_TXN *** BLOCKS. HARD. LOUD. ***
```

**On Wednesday the ceiling FINALLY ENGAGES, an alarm fires, and the obvious one-line fix is:**
```
TXN_SILVER_STALENESS_CEILING_DAYS = "10"      <- mirroring the PERF bump, green ledger, in infra/
```
**…which is DOOR 2, wearing a CTO-RATIFIED PRECEDENT (`20260706T1440Z_inf-perf-ceiling-bump`, CLOSED, GREEN).**

> ## **THE CONTROL WE ARE COUNTING ON BECOMES VISIBLE ON THE EXACT DAY IT BECOMES TEMPTING TO REMOVE.**

**CTO has REVOKED his own 07-06 ratification for TXN.** **DOOR 2 STAYS SEALED — any value, any lane, no
exceptions — and it is MORE important on Wednesday than it is today, not less.**

---

## 📏 THE NUMBERS ARE IN DIFFERENT UNITS. DO NOT RECONCILE THEM BY ADJUSTING ONE.

| number | unit | meaning |
|---|---|---|
| **$439,326.22** | **all 14 accounts (full Class B)** | ***the amount that LEAVES on a re-derive.*** **This is the at-risk total.** |
| $453,179.39 | the 9-account SUBTOTAL | larger than the 14-account total **only because the 5 extras net NEGATIVE (−$13,853.17)** |
| $52,604.80 | 3 accounts, 07-09 cohort | Patrick's phantom — the *served* misattribution, a different defect |

**All three are correct in their own unit.** *Reconciling two counts by adjusting one until they agree is how a
census stops measuring anything.*

---

## 🔬 "EVERY GUARD REPORTS GREEN" IS NOT RHETORIC. IT IS **MEASURED** (CVO, `3a1459644`, exercised).

```
BEFORE (served today)      sum(advisors) = $133,107,667.64   firm_total = $133,107,667.64   TIES.  GREEN.
AFTER  (Class-B deleted)   sum(advisors) = $132,668,341.42   firm_total = $132,668,341.42   TIES.  GREEN.

VANISHED: $439,326.22 from THREE NAMED ADVISORS
          peter_lee -$328,965.68 · patrick_scanlan -$84,213.71 · inflection_wealth_management -$26,146.83
```

> ## **A CONSERVATION INVARIANT CANNOT DETECT A CONSERVED LOSS.**
> **`sum(parts) == whole` catches REDISTRIBUTION and is STRUCTURALLY INCAPABLE of catching DELETION.**
> ## **A GUARD THAT TIES IS NOT A GUARD THAT SAW.**

**Every value-based, sum-based, or reconciliation-based guard in the estate is blind to this BY CONSTRUCTION.**
**Only a COVERAGE check can see it** — *"every account carrying NNA history yesterday still carries it today"* —
because **COVERAGE IS THE ONE PROPERTY DELETION CANNOT PRESERVE.**

**That detector is F7 — the one DELETED on a *"the coverage axis is owned elsewhere"* hand-off.** So:
> **DS's F7 coverage guard is the PRECONDITION for the hold-lift, NOT a parallel workstream.** Until it lands and
> is EXERCISED, **there is no instrument in the estate that can go RED on this class** — which means lifting the
> hold without it is not *"risk-managed,"* it is ***UNOBSERVABLE.***

**AND THE CONFIRMING EXPERIMENT IS RE-POINTED AT THE GUARD, NOT AT A RE-DERIVE (CVO struck her own proposal):**
> *"The thing I was predicting — the rows vanish — **IS THE HARM.** I would have been running the incident in
> order to verify the incident. **An experiment whose positive result IS the harm is not an experiment; it is the
> incident with a hypothesis attached.**"*

### 🛑 **THE ORIGINAL WORDING OF THIS CRITERION FAILED *OPEN*, AND IT WOULD PASS RIGHT NOW. REPLACED.**

**It read: *"the coverage guard (F7) LANDS and is EXERCISED first."*** **BOTH ARE ALREADY TRUE:**
- **It HAS landed** — `d52ab4cbe`.
- **It HAS been exercised** — 21/21 with proven-RED fixtures, **and it FIRES on the live data at 14 accounts /
  $439,326.22**, reproducing CVO's figure to the cent, derived independently.

> ## **SO A CAREFUL AGENT CHECKS (d), FINDS IT SATISFIED, AND LIFTS THE HOLD — ON A GUARD THAT CANNOT FIRE IN PRODUCTION.**

```
DEPLOYED (the runner's copies, read on the artifact -- not source, not a commit):
  code/gold/lib/nna_coverage_guard.py   277 lines   deployed 2026-07-13T10:55:02Z   <- the GUARD, live today
  code/gold/INF_C_01.canonical_nna.py   764 lines   deployed 2026-07-10T22:02:32Z   <- the CALLER, 3 DAYS STALE
      calls to the guard in the DEPLOYED caller:  *** ZERO ***
RETRIEVAL CONTROL: the caller is 764 real lines and `canonical_nna` appears 5x -> the read is SOUND,
      so the ZERO is a REAL ABSENCE, not a failed read.  (`grep -c` on an error message also returns 0.)
DISCRIMINATOR: the LOCAL source calls the guard once. THE WIRING EXISTS AND IS NOT DEPLOYED.
                                 -> A **DEPLOY** GAP, NOT A WIRING GAP.
```

> ## **LANDING IS NOT THE PROPERTY THAT MATTERS. *REACHABILITY FROM THE RUNNER* IS.**
> **A COMMIT HASH IS A STATEMENT ABOUT A *REPO*. THIS HOLD IS A STATEMENT ABOUT *PRODUCTION*.**
> *(CVO authored the criterion and called it her own hole. That is the standard.)*

### 🛑🛑 **AND THE REPLACEMENT WAS *STILL* TOO WEAK. IT WOULD PASS ON A GUARD THAT CANNOT LOAD.** (DS, 12:00Z)

**I wrote (d)(i) as: *"the deployed `INF_C_01` contains > 0 calls to the coverage guard, with a RETRIEVAL CONTROL
(a real line count)."*** **THAT IS A `grep`. AND A LINE COUNT IS NOT A LOAD.**

**DS downloaded the DEPLOYED objects and tried to IMPORT them:**
```
deployed lib/inflection_rep_scope.py : 359 lines   KNOWN_ADVISOR_KEYS defined = 0     (repo: 791 lines)
deployed lib/nna_coverage_guard.py   : imports KNOWN_ADVISOR_KEYS from it
EXERCISED (both deployed objects downloaded and imported):        *** ImportError ***
```

> ## **THE GUARD DEPLOYED THIS MORNING CANNOT LOAD.**
> **It was NOT "a guard nothing calls." IT WAS A GUARD THAT COULD NOT HAVE WORKED IF IT HAD BEEN CALLED —**
> **and if anything HAD imported it, THE CHAIN WOULD HAVE DIED.**
> **And the unit suite was GREEN throughout — because A UNIT SUITE IMPORTS THE REPO, NOT THE BUCKET.**

> # **A PRESENT FILE IS NOT A LOADABLE ONE, AND A GREEN SUITE IS NEITHER.**

**THIS INVALIDATES EVERY "DEPLOYED" VERIFICATION IN THIS DOCUMENT AND IN MY DAY** — `head-object`, a file listing,
a line count, a `grep`, a deploy log. **I used *"764 lines, therefore the file is real"* as a retrieval control.
It proved I had READ the file. IT PROVED NOTHING ABOUT WHETHER IT RUNS.**

> ## **`DEPLOYED` NOW MEANS: DOWNLOADED **AND IMPORTED**. Nothing less counts, anywhere, on any deploy.**
> *(DS's finding. Routed to CTO for the rulebook under his name. CTO~B has made it a condition on every deploy in
> his gate.)*

**FINAL (d) — VERIFIED AT *LOADED*, NOT AT APPLIED, AND NEVER AT HEAD:**
```
(d)(i)   DOWNLOAD the deployed objects (INF_C_01 + every lib it imports) and *** IMPORT THEM ***.
             They must LOAD. An ImportError is a FAILED DEPLOY, however green the suite was.
(d)(ii)  the deployed INF_C_01 contains > 0 calls to the coverage guard.  (necessary, NOT sufficient)
(d)(iii) the guard is EXERCISED THROUGH THE REAL RUNNER -- not through its own fixture, and not through the repo.
(d)(iv)  it FIRES on a basis its REAL CALLER CAN CONSTRUCT.
             *** NOT "14 accounts / $439,326.22" -- THAT NUMBER IS VOID. *** The real path scopes the basis to
             `to_write`, and those partitions produce no rows, so they are NEVER in it. DS proved this and
             RETRACTED HIS OWN PROVEN-RED before the co-sign.
         The exercised RED case (DS, a233b84f5): a REAL partition (canonical_nna_2026-01-15), a REAL account (47,
             -$3,500.00) made feed-absent, with 31 REAL co-tenants still trading so the partition IS rewritten
             WITHOUT it -> RED, naming the account, the amount AND the partition.
         OVER-CONDEMNATION ARMS WATCHED TOO: a faithful rewrite PASSES; an empty frame PASSES.
             *A fail-closed fix that fires on a legitimate zero is the disease it was sent to cure.*
         >> THE RAISE IS ON THE **DROP**. THE REGISTER IS ON THE **RISK**. << (DS's split; better than the spec.)
Scratch prefix. Never prod. Zero risk.
```

---

## ⛔ THE CLAUSE THAT WILL ACTUALLY BITE YOU — READ THIS ONE FIRST

> ## **NOBODY REPAIRS, RESTARTS, RE-RUNS, OR "KICKS" THE INF BRONZE TRANSACTION PULL.**

### 🚨 **THERE IS A FOURTH DOOR, AND NO CENSUS BY RULE OR POLICY CAN SEE IT** (CTO~B, 11:03Z)

> **THE SILVER AGGREGATOR INVOKES `inf-gold-trigger` *DIRECTLY* — NOT VIA ANY EVENTBRIDGE RULE — AND IT FIRES
> `{"mode":"full"}` EVERY DAY AT 13:47Z.**

```
aws events list-rule-names-by-target   -> BLIND (it lists RULES; this is not a rule)
aws lambda get-policy                  -> BLIND (it lists SERVICE principals; an IAM-ROLE caller
                                                 needs no resource-policy statement at all)
THE LOGS CAUGHT IT. NOT A RE-READ. BOTH CENSUS INSTRUMENTS RETURNED CLEAN.
```

**SO THE TWO-RULE EVENTBRIDGE DISARM — THE THING I ASKED FOR AND CTO RATIFIED — IS *ITSELF* A PLACEBO.** *A fourth
caller walks straight past it.* **Third time today a disarm/census has been scoped by the wrong axis.**

> ## **THEREFORE THE LOAD-BEARING CONTROL IS A HOLD AT THE *CHOKEPOINT*, NOT AT THE DOORS:**
> ## **`INF_GOLD_DISPATCH_HOLD` on `inf-gold-trigger` itself — refusing EVERY dispatch BEFORE any side effect**
> ## **(no EC2 start, no lock, no SSM).**
>
> **Every path must traverse that function — the aggregator, both rules, and DOORS THAT DO NOT EXIST YET.**
> **And it holds EVERY MODE, not just `full`:** `INF_C_01` is in `CHAIN_GOLD_C`, so a `gold-c` run re-derives the
> protected artifact. ***A mode-scoped hold is walked past by choosing another mode.***
>
> The two rule-disarms ride along as **defence-in-depth in the same apply.**

**STATUS: AUTHORED, GATE-BLOCKED (correctly), NOT APPLIED.** `owned-paths` refused CTO~B's commit (`infra/aws` is
AE-lane). **He did not force it.** Routed to `0.7.0_AE_CloudOps` for SoD: adversarial review → `safe-commit` →
build-and-upload → `safe-apply` → 0-diff → **EXERCISE**. *With hours of margin there is no excuse for bypassing
SoD; **a wrong control is worse than a late one.***

---

### AND THE THREE DOORS BELOW ARE STILL SHUT — but they are the SYMPTOMS, not the chokepoint.

### THERE ARE **THREE DOORS** INTO THE SAME KEYSTROKE. GUARDING ONE IS GUARDING NONE.

| # | The door | Who walks through it |
|---|---|---|
| **1** | **Repair / restart / re-run `INF_API_PULL_TXN`** (bronze, dead since 07-10) | an AE clearing an obvious 3-day-stale P1 |
| **2** | **Clear, raise, or bypass the silver staleness BLOCK** — `convert_transactions_to_silver.py:128`, `STALENESS_CEILING_TRADING_DAYS = 2`, already breached and escalating to FAIL-LOUD-BLOCK | an engineer "unblocking" a blocked converter |
| **3** | **"Fix" the frozen mdpf / OPAL_ASSETS daily bucket** — a *different project*, with a *sovereign mandate*, that **never touches an INF file** | an agent on Andrew's own commissioned work |

> ### 🛑 **STRUCK 10:57Z — "THE SILVER STALENESS BLOCK IS THE SAFETY CATCH" IS FALSE. I WROTE IT; IT IS WRONG.**
> ```
> bronze/transactions last pull : 2026-07-10  = FRIDAY
> today                         : 2026-07-13  = MONDAY
> TRADING days behind           : 1           (Sat + Sun are not trading days)
> ceiling (:128)                : 2           ->  1 <= 2  ->  WARN. *** IT DOES NOT BLOCK. ***
> ```
> **THE CEILING IS NOT ENGAGED. IT IS NOT HOLDING ANYTHING.** `0.8.0` asserted it, **CTO RATIFIED IT AND SENT
> IT TO TWO AGENTS AS A RULING**, I put it in this file as a load-bearing safety claim — **and none of the three
> of us did three lines of arithmetic.** *Fifth symptom-promoted-to-mechanism of the day, and the first one
> laundered into a ruling other agents were told to act on.*
>
> **DO NOT RAISE THE CEILING ANYWAY. DO NOT ADD A BYPASS FLAG.** It is still a door (see door 2) — **it is just
> not currently the thing keeping us alive.** *Do not relax it on the strength of this correction; relax nothing.*

---

## ☠️ **WE DO NOT KNOW WHAT IS HOLDING THE LINE.**

**Measured, we know four things that are NOT holding it:**

| candidate | verdict |
|---|---|
| the trigger (`inf-gold-trigger`) | **NOT a guard** — no data-state check of any kind; fires 3×/day, 0 errors |
| the EC2 runner being stopped | **NOT a guard** — the trigger calls `start_instances()` on a stopped box |
| the silver staleness ceiling | **NOT ENGAGED** — 1 trading day behind, ceiling 2 → WARN, not BLOCK |
| the 14:47Z cron being "blocked" | **NOT a control** — it merely LOSES A RACE to a dispatch lock, **by 16 minutes.** *Luck with a TTL.* |

**And `bronze-complete` ITSELF dispatched `{"mode":"full"}` on 07-10, 07-11 AND 07-12** — the `_BRONZE_COMPLETE.json`
marker is still written even though the pull is dead. **THE CHAIN IS BEING DISPATCHED DAILY. GOLD IS NOT ADVANCING.
SOMETHING ELSE ABORTS IT AND NOBODY HAS READ IT.**

> ## **WE ARE NOT PROTECTED. WE ARE UNHARMED, AND WE DO NOT KNOW BY WHAT.**

**THEREFORE THE EVENTBRIDGE DISARM IS NOT DEFENCE-IN-DEPTH — IT IS THE ONLY CONTROL, AND IT IS RIGHT *BECAUSE* WE
ARE IGNORANT.** *You cannot rely on a guard you cannot name.* Every door works by letting the CHAIN PROCEED, and
the chain only runs if the trigger DISPATCHES. **Kill the dispatch and it does not matter what we failed to
understand.**

> ## **AND THE ACTOR IS NOT A HUMAN.**
> **The pulls are `tolerate`, not fail-fast. NO HUMAN IS REQUIRED. If Orion simply comes back up on its own, the
> chain proceeds and the deletion lands WHILE WE SLEEP.**
> **PROSE CAN GOVERN A HUMAN. IT CANNOT GOVERN A CRON.**
> **Every instrument shipped today — this hold, the broadcast, the door-2 seal — addresses an AGENT. The actor is
> a SCHEDULER. A HOLD IS NOT A CONTROL WHEN THE ACTOR CANNOT READ.**

## ⚠️ AND THE COVERAGE GUARD IS **NOT LIVE** — DO NOT READ DS'S COMMIT AS CLEARANCE

DS built it, it is **21/21 tested with proven-RED fixtures**, and it **fires RED on live data** (14 accounts /
**$439,326.22**, reproducing CTO's and MSTR's numbers **to the cent**, derived independently). **It is committed
(`d52ab4cbe`).** **AND IT IS NOT PROTECTING ANYTHING:**

```
safe-deploy on push:
  SERVE-HELD: INF_C_01.canonical_nna.py   -- committed but NOT served (AoR sentinel)
  DEPLOYED  : lib/nna_coverage_guard.py   -- the LIB only

s3://opal-data-inf/code/gold/INF_C_01.canonical_nna.py -> guard calls = 0
  (control on the retrieval: wc -l = 764 -> the file is REAL, so the ZERO is a REAL ABSENCE)
```

> **A GUARD IN THE CODE BUCKET THAT NOTHING CALLS IS A COMMENT WITH PARENTHESES.**
> DS: *"I tested the SOURCE and shipped the DEPLOYMENT."* His structural test asserts the call site exists **in
> the repo** — it cannot see that the repo file **never reaches the runner.**

**THE COLLISION (two CORRECT mechanisms):** the `DEPLOY-SERVE-HELD` sentinel that keeps the AoR fold off the
served path is now **HOLDING THE SAFETY GUARD HOSTAGE.** Both are right. **CTO ruling required** — nobody touches
the sentinel unilaterally (NEVER#2 / CTO~B gate).

**And every instrument an engineer owns is currently screaming at him to walk through door 1:** a dead pull, a
`ChainStepDegraded=1` metric firing nightly, a breached staleness ceiling escalating to FAIL-LOUD-BLOCK.
> **Every one of those instruments is RIGHT about the symptom and WRONG about the remedy.**
> *A bare "don't touch it" will lose that argument — and it will lose it to a competent, conscientious engineer
> doing exactly his job.* **That is why this file leads with the mechanism and not with the order.**

```
bronze/transactions          DEAD since 2026-07-10 09:43   <-- reads as an obvious, correct, urgent P1
silver/transactions          DEAD (starved by bronze)
gold/canonical               has not run since 2026-07-10 10:44
silver/api_dims/accounts_v2  STILL ADVANCING DAILY          <-- the roster feed is HEALTHY
```

**`inf-gold-full-on-bronze-complete` is EVENT-DRIVEN on bronze-complete.** Gold has not re-derived for exactly one
reason: **bronze never completes.**

> ### **THEREFORE THE REPAIR IS THE TRIGGER.**
> Fix the bronze pull and gold **immediately re-derives 1,389 of 1,410 partitions back to 2020**, against a silver
> snapshot that has **ZERO ROWS** for 14 accounts carrying **$439,326.22 of currently-served NNA**. Those rows do
> not move to a catchall — **they cease to exist** — and `sum(advisors) == firm_total` **still ties perfectly**,
> because the money leaves the advisor side and the firm side at the same instant.

> ## **THE GOOD FIX AND THE DESTRUCTIVE ACT ARE THE SAME KEYSTROKE.**
> **Nobody looks at a stale-data P1 and thinks "I must first check whether repairing this deletes an advisor's
> book."** That is why this clause is at the top of the file.

**INF STALENESS IS NOW A DELIBERATE STATE, NOT A DEFECT TO BE CLEARED.**

**AND THE FRESHNESS ALARMS ARE ACTIVELY DANGEROUS — THEY ARE INSTRUCTING AGENTS TO PULL THE TRIGGER.**
> *An alarm that instructs an engineer to perform the destructive act is worse than no alarm.*

### ⚠ SCOPE THE STOP BY **WHAT THE ALARM POINTS AT**, NEVER BY WHAT IT IS **CALLED** (0.8.0, 10:36Z)

**The first version of this order said "ignore all INF freshness alarms." THAT WAS A CENSUS-BY-MENTION BUG IN A
SAFETY ORDER, and `0.8.0` caught it inside four minutes — live, exercised:**

```
12 of 14  mdpf-cohort-freshness-stale-*  ARE IN ALARM RIGHT NOW
          incl. ...-inflection_models AND all nine 49f_* cohorts   (only etf_pfde / etf_pfoe are OK)
NONE of them has "inf" in its name.
```

**`mdpf-cohort-freshness-stale-inflection_models` IS an INF freshness alarm wearing a different prefix.** It fires
*because* of this freeze and it points its reader at the same repair. **An agent obeying the old STOP LITERALLY AND
CORRECTLY could still page on `mdpf-*`, conclude mdpf is broken, and go unblock the chain.**

> ## **THE RULE IS FUNCTIONAL, NOT LEXICAL:**
> ## **ANY alarm whose remedy is "refresh / unblock / repair / re-run the INF chain — OR ANYTHING DOWNSTREAM OF IT" IS UNDER THIS STOP, WHATEVER IT IS NAMED.**
> **Do not ask "does the alarm say INF?" Ask "would obeying it advance the INF chain?"** If yes: **DO NOTHING.**

**Named instances (NOT exhaustive — the functional rule above governs):**
`inf-gold-freshness-check-trigger` (18:30Z) · the NNA partition check (19:30Z) · **all 14
`mdpf-cohort-freshness-stale-*`** · **any OPAL_ASSETS "daily AUM bucket has not advanced" alarm.**

### AND THE HAZARD REACHES INTO PROJECTS THAT NEVER TOUCH AN INF FILE

**OPAL_ASSETS' daily emitter is FROZEN at `run_date=2026-07-10`** (`lambda_function.py:842,844 @ 677dd4d72` —
`run_date` comes from the SOURCE FILENAME, never the emit date). mdpf cannot advance past a gold that last wrote
07-10. **So from the OPAL_ASSETS lane the symptom presents as *"the Andrew-commissioned DAILY AUM bucket has not
advanced in 3 days"* — a clean, urgent, entirely legitimate P1 with a sovereign mandate behind it — and its repair
path runs straight into the $439,326.22 deletion.**

> **AN AGENT WORKING OPAL_ASSETS, IN GOOD FAITH, WOULD FIX THIS AND NEVER TOUCH AN INF FILE TO DO IT.**
> The blast radius of the "obvious repair" is **WIDER THAN THE INF LANE**. Scope this hold by the CHAIN, not by
> the folder.

**`0.8.0` is deliberately NOT building the obvious missing control** — a "daily AUM bucket has not advanced in N
days" staleness alarm — **because under this freeze that alarm has exactly one function: to page a future agent
into the destructive repair, with a green-looking justification and a sovereign mandate behind it.** *A loaded gun
with a helpful label.* **It ships when the hold lifts, WITH a `frozen-by-deliberate-hold` discriminator so it can
never again mean two things.** *That is the correct call and it is recorded as such.*

**THE REAL CONTROL, REQUESTED OF CTO (`103534Z`), NOT YET LANDED: DISARM `inf-gold-full-on-bronze-complete`.**
The trigger is **already effectively dead** (bronze never completes), so **disabling it is a NO-OP TODAY and a
REAL CONTROL TOMORROW** — zero behavioural change, fails safe, trivially reversible, and it lets an AE repair
bronze *correctly* without holding a loaded gun. **Then this bronze clause can be LIFTED.** *We should not have to
keep a pipeline broken to keep the data safe.* **Until it lands, prose is the only thing holding this — and prose
is what we watched fail all day.**

---

## THE REBUILD HOLD

> **NOBODY RUNS A FULL REBUILD, A BACKFILL, OR A DATE-RANGE RE-DERIVE OF `gold/canonical/canonical_nna_*`
> UNTIL THE SILVER `rep_id` NULL IS FIXED AND A COVERAGE ASSERTION IS IN PLACE.**

This includes: `INF_C_01.canonical_nna.py` run over any historical range, `_rebuild/` sweeps, "re-run the chain
from date X", and any repair that re-derives an old partition. **A normal forward nightly on TODAY's partition is
not what this hold is about — but if you are about to re-derive a PAST date, STOP.**

An ad-hoc gold run to "validate" or "just refresh" the numbers is the exact action this hold forbids
(and NEVER#4 already forbids ad-hoc gold runs for validation).

## WHY — MEASURED, NOT INFERRED

`INF_C_01:444-464` derives `advisor_key` by mapping **`rep_id` on the TRANSACTION ROW** (`:375-380` map:
`3`→firm, `6`→joe, `11`→patrick_scanlan, `12`→peter_lee). **Roster presence plays NO part in the derivation**
(the 2026-07-13 "roster departure" mechanism was ruled and then FALSIFIED — see `ef923bf10`).

Twelve accounts are absent from today's roster and carry NNA. Per-row census over **1,410 partitions,
124/124 rows classified**, S3 `LastModified` read in **Z**:

```
silver/transactions/2026-07-10.parquet   written 13:44:22Z   <- 3 accts present w/ rep_id=<NA>; 9 accts ZERO rows
gold canonical_nna partitions            written 14:41:xxZ   <- ~1 hour LATER

PHANTOM(3)  560/703/1225   rebuilt_after_silver = TRUE   113/113 rows   -> stamped inflection_unmapped_rep
SURVIVOR(9) 77/100/302/…   rebuilt_after_silver = FALSE   11/11 rows    -> still stamped with the REAL advisor
                                                                            (partitions last written 05-13/06-02/06-29)
```

**PERFECT SEPARATION. The discriminator is not the account, not the advisor, not the roster — it is WHETHER THE
REBUILD TOUCHED THE PARTITION.**

> **RE-DERIVATION IS THE ACT THAT DESTROYS THE ATTRIBUTION.**
> **The 9 survive ONLY because nothing has re-derived them yet. "Untouched" is not a safety property — it is a
> countdown.** The defect is PROGRESSIVE and advances one partition at a time.

## AND THE FAILURE MODE FOR THE 9 IS DELETION, NOT MISATTRIBUTION

- The **3** ARE in silver with `rep_id = <NA>` → they produce a row → `.fillna()` → **catchall**. The money stays
  in the firm total, visibly wrong. **This is the recoverable case.**
- The **9** are **NOT IN SILVER AT ALL — 0 rows.** A re-derive of their partitions produces **NO ROW**.
  → **Peter Lee's $368,965.68 and Patrick Scanlan's other $84,213.71 do not move. THEY CEASE TO EXIST.**

## >> AND THE RECONCILIATION CANNOT SEE IT <<

`sum(advisors) == firm_total == raw gold` currently ties to **0.00**. That is TRUE and it is **NOT reassurance.**

**A deleted row leaves the ADVISOR side and the FIRM side AT THE SAME INSTANT.** Both totals shrink together, so:

```
sum(advisors) == firm_total     -- STILL TRUE. STILL 0.00. FOREVER.
```

> **A RECONCILIATION THAT TIES BOTH SIDES OF THE SAME OMISSION IS NOT A RECONCILIATION.**

The co-signed invariant (`sum(advisors) + unattributed == firm_total`) is **blind to this by construction** — it
was built to catch money moving *between* buckets. **This is money leaving the building, and every bucket agrees
it was never there.** *An invariant that only ever compares the artifact to itself will certify any consistent lie.*

**The only instrument that can see it compares the served total against a PRIOR VINTAGE of itself, or against a
source the pipeline does not derive from.**

## ⚑ PRE-REGISTERED PREDICTION — WRITE THE NUMBER DOWN **BEFORE** THE RE-DERIVE RUNS (CVO, `5be383519`)

> ## **A PREDICTED NUMBER-MOVE IS A VERIFICATION. AN UNPREDICTED ONE IS AN INCIDENT.**

The re-derive that LIFTS this hold will do **two correct things at once**, in **opposite directions**, and only
one of them is the one everybody is watching for.

### 🛑 THE FIRST VERSION OF THIS PREDICTION WAS WRONG BY 30× AND IN THE WRONG DIRECTION. IT IS REPLACED.

**I committed `+$13,853.17 / peter_lee +$40,000` here at 10:47Z. CVO falsified it at 10:50Z by measuring, and
`REPLACED IT HERSELF`. If you are reading a cached copy of that number, DISCARD IT.** *Checking a correct rebuild
against the old number would have HALTED IT as a regression — a false FAIL with a destructive remedy, which is the
class we spent the entire day on.*

**WHY IT WAS WRONG — and it kills my own claim, not just hers:** I told CTO *"the 9 survivors SURVIVED a
post-silver re-derive."* **CVO measured the `LastModified` of EVERY partition carrying EVERY one of the 14:**
```
COO's 9  -> partitions in the 07-10 rebuild: 0     never touched: 11
CVO's 5  -> partitions in the 07-10 rebuild: 0     never touched:  9
                                                   ------------------
                                                   20 of 20 NEVER TOUCHED
```
> **"THE 9 SURVIVED THE REBUILD" IS FALSE. THEY DID NOT SURVIVE ANYTHING — NOTHING EVER RE-DERIVED THEM.**
> **That claim was the ONLY evidence anyone had that a re-derive does NOT delete a feed-absent account.**
> **IT IS GONE. NOTHING NOW CONTRADICTS THE DELETION MECHANISM.**

**AND THE 14 ARE ONE POPULATION, NOT TWO.** COO's 9 + CVO's 5 were the same class found through two different
doors. All 14 are **roster-absent AND feed-absent.**

**CORRECTED EXPECTED DELTA — ACCEPTANCE CRITERION:**

```
THE RE-DERIVE DELETES ALL FOURTEEN.

    NET CHANGE TO SERVED NNA HISTORY:   -$439,326.22
    peter_lee:                          -$328,965.68
```

**WHY:** those 5 accounts' entire served NNA lives in **8 partitions the 07-10 rebuild never touched**
(all written 2026-05-13 06:52Z; 8 of 8). They have **ZERO rows** in the canonical snapshot `INF_C_01` derives from
(`:306` — single-snapshot source-selection, over ALL of history). **When the re-derive reaches those partitions,
those rows cease to exist — and that is CORRECT: a number the source cannot produce should not be served.**

> **BOTH OUTCOMES ARE RIGHT. THAT IS EXACTLY WHY IT IS DANGEROUS.**
> The same delta lands on the same night either way. The only variable is whether it reads as
> *"the re-derive did what CVO said it would, to the cent"* — or as
> ***"peter_lee's historical NNA moved $40,000 and nobody knows why."***
> **We have spent this entire day on numbers that moved without an owner.**

**IF THE DELTA IS ANYTHING OTHER THAN THE ABOVE, *THAT* IS THE ALARM.** Halt and restore from the backup.

**AND THIS MAKES THE PREDICTION FALSIFIABLE FOR FREE.** CTO wanted a dry re-derive of one untouched partition and
said it needed an owner. **The hold-lift re-derive IS that exercise, at zero extra cost** — provided someone reads
the result against a number written down **in advance**. *It stops being a prediction and becomes a measurement.*
**Safe:** 8,805 gold objects backed up + ETag-verified (0 missing / 0 mismatched), so a wrong prediction is
recoverable.

> **THE GENERAL SHAPE (CVO):** *"F2 × F7 taught us that per-finding triage is structurally blind to COMPOSITION.
> This is the same thing between two findings of MINE, in two different scripts, filed an hour apart, that I never
> held up against each other. Individually: 'a collapse to repair' and 'some stale rows.' Jointly: a single
> re-derive that changes served advisor numbers in TWO DIRECTIONS AT ONCE, one of which nobody is expecting."*
> **ENUMERATE THE INTERACTION, NOT JUST THE FINDINGS.**

---

## TO LIFT THIS HOLD

1. **Ground and fix the upstream defect: WHY is `rep_id` NULL in `silver/transactions` for accounts 560/703/1225?**
   (3,283 rows between them, NULL on every row, re-firing nightly.) The silver converter has NOT been read by
   anyone as of this writing — **do not guess it.**
2. **A COVERAGE assertion, not just a key-validity assertion.** A *vanished* account has no key to be invalid.
   Assert: *every account with NNA history yesterday still has it today* — and RAISE. **This is F7**, currently
   SERVE-HELD with the AoR bundle. **F7 would have caught both the 07-09 phantom AND this deletion class.**
3. **A vintage comparison on the served spine** (today's `advisor_nna_canonical.json` vs yesterday's), because the
   internal reconciliation provably cannot.

## NOTE

**INF gold has been STALLED since 2026-07-10** (platinum last written 07-10; `data_as_of` 07-09). **That stall is
currently the only thing holding this line — AND A STALL IS NOT A CONTROL.** It will end, and when it does this
hold is the only thing standing between us and a silent half-million-dollar deletion.

*Filed by COO after a reconciliation run to CONFIRM a claim instead refused to tie. Mechanism ruled by CTO
(`ef923bf10`) after he opened the script none of the four of us had read.*

---

# AMEND 15 (2026-07-13T13:30Z, COO) — THE ANDREW-APPROVED SPEC CITES A FUNCTION THAT THE FIX FOR THE DEFECT DELETED

## THE FINDING

CTO's **TIME-LOCK NNA** spec (12:47Z, Andrew-approved — the fix this entire hold exists to enable) says at step 3:

> *"`INF_B_00.accounts_v2_key_for_snap` **ALREADY DOES EXACTLY THIS — USE IT. Do not write a second one.**
> (Two paths to one fact is how we got here.)"*

```
grep -rn "accounts_v2_key_for_snap" --include=*.py .        ->  0 REFS
  RETRIEVAL POSITIVE CONTROL: _INF_REP_ID_TO_ADVISOR_KEY    ->  6 files.  The grep works.
git log --all -S "accounts_v2_key_for_snap"                 ->  12 commits. IT EXISTED.
  DELETED BY:  c23988cdf  "fix(INF_B_00 SEV): WALK BACK OVER THE 0-ROW ROSTER"
               0.4.0_DS_ClientPlatform~A  ·  2026-07-13T10:58Z  ·  PUSHED to origin/CLOUD
```

> ## **THE SPEC WAS WRITTEN AT 12:47Z. THE FUNCTION DIED AT 10:58Z. IT WAS CITED 1h49m AFTER THE GROUND MOVED.**

## AND THE DEAD NAME IS NOT MERELY STALE — IT ENCODES THE BROKEN CONTRACT

The replacement, at `data/inf/scripts/gold/INF_B_00.canonical_holdings.py` @ `c23988cdf`:
```
:211  accounts_v2_candidates_for_snap(snap, available) -> list[str]    # a LIST
:240  resolve_accounts_v2_for_snap(snap, available)    -> DataFrame    # walks back over EMPTY *and* UNREADABLE
```
**It returns a LIST *because a single key IS the defect*.** `..._key_for_snap` — **singular** — promises exactly
the one-key selector that walked into the 0-row 2026-05-08 partition, NaN'd every `representative_name`, and
served **all $202,062,830 to one advisor with three real advisors zeroed.**

> ## **DS GREPS THE NAME → GETS ZERO → HIS ONLY OPTIONS ARE STALL OR *WRITE A SECOND ONE* — TO THE CONTRACT THE DEAD NAME IMPLIES.**
> ## **THE SPEC'S OWN CITATION WOULD HAVE CAUSED THE EXACT DEFECT THE SPEC'S OWN PARENTHETICAL FORBIDS.**

## THIS IS THE DAY'S OWN DOCTRINE, LANDING ON THE DAY'S MOST IMPORTANT SPEC

> *"**THE MOST DANGEROUS COMMENT IS NOT A FALSE ONE — IT IS A TRUE ONE THAT THE GROUND MOVED UNDER.**"*
> *"**A LINE CITATION WITHOUT A VINTAGE IS NOT A CITATION.**"*

The citation was **TRUE WHEN CTO LEARNED IT.** It reads authoritatively, in the codebase's own voice, and argues
persuasively for the harm it would now cause. **Nobody was careless.** *A fix can outlive the defect it fixed and
reverse polarity — and so can a citation.*

**AND IT WAS NOT CAUGHT BY CARE. It was caught because the grep returned ZERO and the rule says: WHEN THE ANSWER
IS ZERO, OPEN THE FILE.** *A zero is the one result a pattern produces for reasons that have nothing to do with
the estate.* **CONTROLS OVER CARE — ninth instrument-catch of the day, and the first one aimed at a spec rather
than at code.**

**ROUTED:** DS (build against the real names) + CTO (correct the spec AT SOURCE — a verbal patch in an inbox does
not survive; the spec is what DS builds from). **The spec's INTENT is correct and unchanged** — the at-or-before
walk-back IS the right instrument and it EXISTS. Only the name was a ghost.

## >> AND A HYPOTHESIS I RAISED AND *FALSIFIED* BEFORE SENDING IT — RECORDED BECAUSE THE NEGATIVE IS THE POINT

I suspected the spec reused a selector with a **live 0-row hole** (2026-05-08 is an empty roster; a vintage-correct
at-or-before walk would land on it). **FALSE — already closed.** `resolve_accounts_v2_for_snap` walks back over
EMPTY *and* UNREADABLE partitions and **discriminates the two** (Rule 22a F4: *an instrument that cannot observe
must say so; one that observed nothing should say that instead*). **No alarm was sent.** *A hypothesis that dies
on contact with the source is the system working; a hypothesis that gets DISPATCHED is how a COO invents a defect.*

---

# AMEND 15b — **A TRUE-THEN-FALSE-NOW SENTENCE IN *THIS* DOCUMENT. MINE.**

The **NOTE** closing the section above this one says:

> *"That stall is currently the only thing holding this line — **AND A STALL IS NOT A CONTROL**."*

> ## **THAT WAS TRUE WHEN I WROTE IT. IT IS FALSE NOW, AND I AM THE ONE WHO MADE IT FALSE.**

```
INF_GOLD_DISPATCH_HOLD  on `inf-gold-trigger`        APPLIED   [live read, this cycle]
  inf-gold-full-on-bronze-complete                   DISABLED
  inf-canonical-prices-daily                         DISABLED
  inf-gold-incremental-daily                         DISABLED
EXERCISED live by 0.7.0 (5697cc340), mode=gold-c -- the mode that carries INF_C_01 -- held:true, dispatched:false,
  dispatch-lock object UNCHANGED, EC2 still stopped.  THE HOLD IS PROVEN MODE-AGNOSTIC ON THE DEPLOYED CODE.
```
**The line is now held ON PURPOSE, by an applied and exercised control — not by a stall, and not by prose.**
*I struck the sentence rather than deleting it, because the correction is the record.* **I amended this document
fourteen times today and never re-read its own closing paragraph. When you change what is canonical, re-read every
rationale that predates the move — INCLUDING YOUR OWN.**

*(MSTR removed the INF prose block from `org/XXX.md` this hour for exactly this reason, and named it better than I
did: "it only ever existed because prose was the sole control; once the chokepoint was applied and exercised it
should have been deleted the same hour." **A gate replacing a paragraph is the whole objective.**)*

---

# AMEND 16 (2026-07-13T13:40Z, COO) — **THE TWO GUARDS COVER DISJOINT CLASSES, AND WE KEPT DESCRIBING THEM AS ONE WALL**

**CTO, directly:** *"We built the guard for a deletion class that turned out not to exist, and the defect that IS
real needs a different fix. **Do not let anyone spend the guard as if it covered it. Put that in the hold
document.**"* — done, and here is the grounding, verified at source by me rather than asserted:

```
nna_coverage_guard.py:191   prior_by_date = {date_str: {account_id: net_nna}}
                                                        ^^^^^^^^^^^^^^^^^^^^
                                            *** advisor_key IS NOT IN THE BASIS ***
```

| class | what happens | the instrument | state |
|---|---|---|---|
| **DELETION** | an account **VANISHES** from the partition | `nna_coverage_guard` | **LIVE** |
| **COLLAPSE** | every account **STAYS**; `advisor_key` flips to one | `INF_B_00` selector | **NOT ON THE RUNNER** |

> ## **IN A COLLAPSE NOTHING VANISHES. Every account is present, every `net_nna` intact — only `advisor_key` flips to the firm catchall. THE COVERAGE GUARD HAS NO COLUMN TO NOTICE WITH. It passes, silently, at full confidence.**
> ## **NEITHER GUARD CATCHES THE OTHER'S CLASS.**

**This is the 2026-05-08 mechanism: $202,062,830 onto ONE advisor, three real advisors zeroed, `advisor_key`
carrying ZERO nulls.** *Not a null — a **WRONG VALUE that looks exactly like an advisor and carries real money**.*
**A re-derive today would re-preserve it, and every guard we shipped would report GREEN.**

## CONSEQUENCE FOR THIS HOLD — AND IT IS A TIGHTENING, NOT A LOOSENING

**`INF_B_00`'s selector is not tidy-up. It is the ONLY instrument that catches the collapse class, and it is the
critical path to the lift.** *(COO co-signed its arming under NEVER#2 at 13:33Z on exactly this ground — DELTA-0:
the chain is HELD, nothing serves. CTO~B holds the arch-gate.)*

**CTO~B annotated his own lift-ledger `[x] 1. COVERS DELETION ONLY` and called the error correctly:**
> ## ***"A CHECKLIST WHOSE ITEMS ARE INDIVIDUALLY TRUE AND JOINTLY MISLEADING IS HOW A FABRIC TALKS ITSELF INTO A LIFT."***
> *Per-item triage is structurally blind to composition — that rule landed in CLAUDE.md today, and the lift-ledger
> violated it eight hours later.*

## AND THE SAME SHAPE, SAME HOUR, IN THE SILVER CENSUS — *both agents were right and the estate was still open*

`0.7.0`: *"It was never one of five. It is **ONE OF TWO**. Two live writers of `accounts_v2`. **Both are now
guarded. Tonight's hole is closed on both doors.**"* — **TRUE.**
`DS~A` (by EXECUTION, live partitions as proof the writer RAN): **`inf-api-reps` wrote `representatives` AND
`household_rep_mapping` TODAY, unguarded. `inf-api-positions` writes `positions_mv` — the holdings book — unguarded.**

> **`0.7.0` counted **PATHS TO ONE DIM**. `DS~A` counted **COPIES OF THE WRITER**. Neither number was wrong; neither
> adjusted his number to match the other. The unit at which the verdict is rendered is `(dim x writer)` —**
> ## **AND ON THAT UNIT IT IS 3 OF 6 STILL OPEN.**
> *"Tonight's hole is closed on both doors" is TRUE about `accounts_v2` and MISLEADING about the estate.* **Escalated
> P1 to `0.7.0` at 13:32Z: close it at the WRITE BOUNDARY (`write_silver_api_dim_parquet`), not by pasting a fourth,
> fifth and sixth call-site guard.** *A guard that must be pasted into N places is a guard with N failure modes —
> and we are now watching that prediction come true in real time.*

---

# AMEND 17 (2026-07-13T14:00Z, COO) — **"THE CHAIN IS HELD" DOES NOT MEAN "NOTHING CAN WRITE." THE CHOKEPOINT COVERS *DISPATCH*, NOT THE *WRITERS*.**

**CTO~B found it; I confirmed it at APPLIED truth with a working positive control:**
```
inf-api-reps-daily       ENABLED  cron(17 13 * * ? *)  -> inf-api-reps        <- FIRED TODAY
inf-api-positions-daily  ENABLED  cron(37 13 * * ? *)  -> inf-api-positions   <- FIRED TODAY
POSITIVE CONTROL: inf-gold-full-on-bronze-complete -> DISABLED   (the probe CAN read DISABLED)
Both wrote snapshot_date=2026-07-13.
```
**These fire on their OWN EventBridge rules, target the SILVER API lambdas, and DO NOT pass through
`inf-gold-trigger`. The chokepoint does not touch them.** And per DS~A's deployed-package census, **`inf-api-reps`
and `inf-api-positions` have been deployed since 2026-05-13 with ZERO guards of any kind.**

> ## **A 0-ROW ROSTER CAN LAND IN SILVER AT 13:17Z TOMORROW WITH THE GOLD CHAIN PERFECTLY HELD — AND IT WOULD SIT THERE, IN AN APPEND-ONLY STORE, WAITING FOR THE DAY WE LIFT.**
> *A poison pill planted under a hold. The hold does not protect the bucket; it protects the **dispatch**.*

## >> THE PATTERN, AND IT IS THE ONE THAT NEARLY LIFTED THIS HOLD THIS MORNING (CTO~B) <<
```
"the coverage guard is live"  =/=  "a re-derive is safe"      (it covers DELETION; blind to COLLAPSE)
"both gates are clear"        =/=  "go-live is safe"          (V4 is unrunnable while the chain is held)
"the chain is held"           =/=  "nothing can write"        (the silver writers are on their OWN crons)
```
> ## **EVERY ONE IS INDIVIDUALLY TRUE AND JOINTLY MISLEADING. THREE TIMES IN ONE DAY WE TOOK A *SPECIFIC* CONTROL AND READ IT AS *GENERAL SAFETY*.**
*A control is a statement about the path it sits on. It says NOTHING about the paths it does not.*
**Ask of every control: WHAT, EXACTLY, DOES THIS ONE SIT IN FRONT OF?**

## THE DEADLINE + THE PRE-AUTHORIZED FALLBACK (so nobody improvises it under time pressure)

**`0.7.0` holds the P1 — and it is a DEPLOY, not a code change: his lib fix is in the REPO and *0 of 5 deployed
packages carry it* (DS~A, verified on the downloaded packages).**

> **DEADLINE: guarded lib DEPLOYED + DOWNLOAD-VERIFIED on `inf-api-reps` + `inf-api-positions` by 2026-07-14T12:00Z**
> (77 min before the 13:17Z fire).
> **IF NOT VERIFIED BY 12:00Z -> COO DISABLES BOTH RULES.** *Pre-authorized 2026-07-13T14:00Z, in writing.*

**The fallback was PRICED, not assumed:** every gold consumer of `positions_mv`/`representatives` sits in the
**HELD** chain (`INF_B_00`, `INF_D_00`, `partition_provenance`, `skip_gate`) — **one stale silver day costs
essentially nothing downstream today.** *A cheap reversible control beats a hope.* **Not fired now** — the feed is
legitimate, it produces real data, and 23h is ample runway for the real fix. *Prevent what you can, detect what you
cannot, and NAME THE GAP IN THE TEXT.*

## AND ITEM 5 IS CLOSED — COO CO-SIGN GIVEN on `ccabfb3de`, **ON THE NEIGHBOUR CONTROL, NOT ON THE CONSERVATION**
```
IWM  $202,062,830.31 -> $252,714.37   |   peter +$164,606,300.62  patrick +$20,815,558.09  joe +$16,388,257.23
firm BEFORE == AFTER == $202,062,830.31        DRIFT $0.00
```
**`DRIFT $0.00` says no money entered or left. IT SAYS NOTHING ABOUT WHOSE IT IS — conservation is invariant under a
swap (CVO~B, proven RED this morning).** *If that were the only evidence I would not have signed.*
> **What earns the signature is DS~A's OUT-OF-SAMPLE control: the repaired day lands BETWEEN its two healthy
> neighbours (05-07 / 05-09) — A CONTROL THE FIX WAS NOT FITTED TO. That is an assertion a swap cannot pass.**

**LIFT LEDGER: 4 of 7.** Item 4 (CVO~B, **by exercise**) is the critical path. **Nothing lifts today.**

---

# AMEND 18 (2026-07-13T14:10Z, COO) — **THE WHOLE FIRM CAN COLLAPSE ONTO ONE *VALID* KEY WITH EVERY DETECTOR GREEN. THE LEDGER GROWS 7 -> 9.**

## THE FINDING (CVO~B, EXERCISED — item 4 verification, `a2ff8d8ce`, 9/9)
```
D1   Guard A (coverage) PASSES a total advisor COLLAPSE.
     Basis = {date: {account_id: net_nna}} (:191).  advisor_key IS NOT IN IT.  No column to notice with.

D1b  *** THE RESIDUAL-ADVISOR GUARD IS *ALSO* BLIND -- and nobody had said this out loud. ***
     A collapse flips every key to `inflection_wealth_management`, WHICH IS A LEGITIMATE ROSTER MEMBER.
     So it is NOT a residual, and the guard CORRECTLY stays quiet.
     EXERCISED: assert_no_residual_advisor({inflection_wealth_management: $202,062,830.31}) -> PASSED

D1c  CONTROL: the residual guard DOES fire on a real residual (inflection_unmapped_rep).
     >> Its silence on the catchall is a REAL READING, not a dead instrument. <<
```
> ## **THE ENTIRE FIRM CAN COLLAPSE ONTO ONE VALID KEY AND EVERY DOWNSTREAM DETECTOR STAYS GREEN.**
> ## **THE COLLAPSE CLASS IS PREVENTED AT SOURCE AND DETECTED BY NOTHING.**
> ## **`INF_B_00`'s SELECTOR IS NOT DEFENCE-IN-DEPTH. IT IS THE ONLY THING.**

**D1c is what makes D1b believable:** *a guard silent because it is DEAD and a guard silent because the input is
legitimately CLEAN are byte-identical until you make it FIRE.* **She made it fire.**

**And the raw 05-08 partition is `0 rows / 45 COLUMNS`** — a **perfect schema on an empty roster**, which is exactly
why a column-level guard passed it. > ## **A SCHEMA CHECK IS NOT A CONTENT CHECK.**

## THE RULING (CTO~B) — **HE GREW THE DENOMINATOR WHEN HE WAS ONE ITEM FROM A CLEAN BOARD**
> ***"We have spent all day condemning single-point prevention with no detection. I am not going to accept it in my
> own lift because everything else is finished."*** · ***"THE DENOMINATOR GREW BECAUSE WE LEARNED SOMETHING.
> SHRINKING A CHECKLIST TO FEEL FINISHED IS THE DISEASE."***

**This morning he predicted the hazard would arrive looking like *"the last box on a form."* It did — and the person
who refused it was HIM, about HIS OWN FORM.** **RATIFIED, both items, without amendment.**

- **ITEM 8 — THE COLLAPSE DETECTOR** (DS~A's concentration guard): a roster is usable only if **non-empty AND
  < 50% firm-catchall — RAISE, never silently skip.** **Proven-RED required on BOTH 05-08 (0 rows) AND 04-28
  (818/850 = 96.2%)**, *plus* an **over-condemnation arm on a legitimately concentrated day.** *A threshold that
  fires on a real concentration is the disease it was sent to cure.* **No hardcoded skip-list — the next poisoned
  partition will not announce itself.**
- **ITEM 9 — REMOVING THE SELECTOR MUST BREAK THE BUILD.** **AST-asserted (DEFINED *and* CALLED), never grep** — *a
  mention is not an implementation, and a symbol-gate is walked past by inlining the call.* **If one function is the
  only thing between us and a silent $202M collapse, deleting it must be LOUD.**

## OPEN QUESTION POSED (may become item 10)
**Item 9 protects the selector from being REMOVED. It does not protect it from being BYPASSED.** *What stops a
DIFFERENT script from reading `accounts_v2` by date-key and deriving an advisor without it?* **Census BY FUNCTION,
print the denominator — routed to DS~A.**

## AND THE SILVER POISON-PILL WINDOW (AMEND 17) IS **CLOSED — 22h EARLY**
`0.7.0` deployed the write-boundary guard to **all four live writers**. **I verified it MYSELF on the deployed
bytes — IMPORTED, not grepped:**
```
inf-api-reps / inf-api-positions   IMPORT OK (16,560B)   EmptyDimWriteError=True   registry=dict
   representatives / household_rep_mapping / positions_mv -> allows_empty=False -> RAISE
   billing -> allows_empty=True -> WRITES            (the over-condemnation control, INTACT)
RETRIEVAL CONTROL  6 .py files/package (a 0 would be a REAL absence, not a failed download)
NEGATIVE CONTROL   inf-api-txn -> 0/0.  *** THE CHECK DISCRIMINATES. ***
```
**The 12:00Z fallback is STOOD DOWN; the rules stay ENABLED.** *Two verifications asking DIFFERENT questions — his
"does it RAISE" (25 arms, over-condemnation control), mine "is it LOADABLE and CORRECTLY CONFIGURED."*

**RESIDUAL, grounded and DELIBERATELY NOT FIXED:** `inf-api-txn` carries a **WEAKENED AUA SANITY BAND** —
`50M–400M` vs the canonical `150M–300M` — **and I confirmed in the deployed bytes that IT IS READ (3 refs). It is
not dead code.** *A live Lambda would accept AUA values every other copy in the estate rejects.* **Nobody tightens
it on an ungrounded basis** (the `INF_B_00`-in-the-F2-blast hazard: a blanket fix that BREAKS a working script).
**It is a FINDING with an owner, not a chore.** *The commit gate's refusal is the only reason it is visible.*

## LIFT LEDGER: **5 of 9**
```
[x] 1 coverage assertion LIVE      DELETION ONLY -- blind to collapse (exercised: D1)
[x] 2 silver rep_id NULL GROUNDED
[x] 3 INF_B_00 selector LIVE       the ONLY collapse instrument
[x] 4 CVO~B independent verification, BY EXERCISE      a2ff8d8ce, 9/9, both guards
[x] 5 co-sign on the PRE-REGISTERED delta              CTO + COO, both GIVEN on ccabfb3de
[ ] 6 the collision -- DELETE the orphan               SOVEREIGN (Andrew); deliberately LAST
[ ] 7 the first re-derive WATCHED against the delta, revertible from the 8,805 backups
[ ] 8 *** NEW: THE COLLAPSE DETECTOR ***               DS~A
[ ] 9 *** NEW: removing the selector BREAKS THE BUILD *** DS~A
```
**Nothing lifts today — and now for two more reasons than it had an hour ago.**

---

# AMEND 19 (2026-07-13T14:15Z, COO) — **A NAMED↔NAMED SWAP IS INVISIBLE TO ANY SUM** + **ITEM 10: THE BYPASS. THE LEDGER MAY GROW A THIRD TIME.**

## 1. THE DEEPEST FINDING OF THE DAY — CVO~B, INSIDE HER OWN REPAIR OF THE CONSERVATION TRAP
> ## ***"A NAMED↔NAMED SWAP IS INVISIBLE TO ANY SUM."***
> *joe −55,600 / peter +55,600 **nets to zero**. Every aggregate formulation — "the named deltas must sum to minus
> the IWM delta", "conservation within the window" — **is satisfied by the very swap I am trying to catch. It is the
> same conservation trap, ONE LEVEL DOWN, INSIDE MY OWN REPAIR. I nearly shipped it."*

**She built the fix FOR the conservation trap and the fix HAD the conservation trap in it.** *Knowing a failure mode
by name does not immunize you against writing it — and the only thing that has ever caught it is a control.*

> ## **RULED, AS A GENERAL LAW: IF YOU CAN BE WRONG ABOUT AN ACCOUNT, THE ACCOUNT IS THE UNIT. AN AGGREGATE OVER ADVISORS CANNOT ANSWER A QUESTION ABOUT *WHOSE* ACCOUNT IT IS.**
*Fourth instance of one family — **count at the unit at which the verdict is rendered** · **control on the defect
LINE, not the FILE** · **assert the ROW, not the COLUMN**. **THE GRAIN IS ALWAYS THE GRAIN OF THE HARM.***

## 2. SHE DISCLOSED THAT HER OWN BAR VOTED ON AN OPEN RULING — **BEFORE THE RULING**
> ***"T1 as written RATIFIES THE FORWARD BRANCH, and I would have been the one blocking a good ruling with a
> green-looking instrument."***

**A bar that silently encodes one branch of an open question does not VERIFY the fix — it VOTES on the ruling, in
the dark, wearing a green tick.** *Same class as a pre-signed co-sign: an artifact asserting a state of the world
that has not been decided yet.* **RATIFIED:**
```
T1a  [FORK-NEUTRAL · HARD · PROVEN-RED · ACCOUNT GRAIN]  both branches agree on a NAMED advisor
     -> covers ALL 16 named<->named transfers = THE ENTIRE PROVEN-RED CASE. Nothing lost by neutrality.
T1b  [FORK-DEPENDENT -> CANNOT-EVALUATE UNTIL RULED]     quarantined (incl. acct 4273, the 17th)
     BOTH branches pre-registered. Verdict rendered the moment Andrew rules -- EITHER WAY.
```
**LOAD-BEARING FACT, measured: TODAY'S CORRUPTION INVOLVES *ZERO* CATCHALL MOVEMENT** (IWM delta = `0.00` in BOTH
closed windows; it is entirely named↔named plus named→phantom). > **THE FORK IS ORTHOGONAL TO THE LIVE DEFECT** —
which is why the bar can be made fork-neutral without weakening it, **and why the fork, though genuinely open, does
NOT block the repair.**

**And her reframing of the sovereign ask, which I am carrying up as she put it:** *"The two treatments are not an
inconsistency to be tidied — **they are two different questions being asked of one symbol that cannot answer
either.** The durable fix is to STOP OVERLOADING THE SYMBOL, not to pick a branch."*

## 3. *** ITEM 10 — THE BYPASS. MY QUESTION; CTO~B FOUND IT REAL AND THEN DECLARED HIS INSTRUMENT INCAPABLE. ***
**Item 9 protects the selector from being REMOVED. It does not protect it from being BYPASSED** — *a symbol-gate is
walked past by INLINING the call (the C_07 lesson, landed today).*
```
gold scripts (denominator)                          49
scripts referencing accounts_v2                     19
raw date-key pattern AND no safe-path reference      5   <- *** CANDIDATES ONLY. NOT FINDINGS. ***
    INF_C_09.fee_status_audit
    INF_D_00.portal_aggregates        <<< SERVED -- FEEDS THE PORTAL
    INF_D_04.client_portal_summary    <<< SERVED
    INF_D_08.nmec_nmnc_nna            <<< SERVED
    INF_E_00.eclipse_model_portfolios
```
> **THREE OF FIVE ARE ON SERVED SURFACES.** *If any derives an advisor from a raw date-keyed roster, `INF_B_00`'s
> selector does not protect it — and a 0-row roster day collapses THAT surface too, silently, with a perfect schema.*

**AND CTO~B REFUSED TO REPORT IT:**
> ***"That screen is a SYMBOL CENSUS... It CANNOT answer the question you actually asked, which is a DATA-FLOW
> question. 5 candidates, 0 findings. I am not reporting a number I cannot stand behind, and I am not sending an
> engineer to fix five scripts off a grep."***

**ROUTED TO DS~A, AND I HAVE ORDERED IT *AHEAD* OF ITEMS 8 AND 9:** *8 and 9 protect the FUTURE; **10 asks whether we
are ALREADY EXPOSED.** A discovery question about current live exposure outranks two future-protection items.*
**Binding: print the denominator at every step · if the answer is ZERO, OPEN THE FILES · keep `INF_C_01` in the
census as the PROVEN-RED case (an instrument that does not score IT red is broken) · if the instrument cannot answer
it, SAY SO and ship a smaller honest thing.**

## 4. THE COUNT, CORRECTED WITH ITS *CAUSE* — 5 of 9 (+1 open)
CTO~B's header said `4 of 9` while his table carried five `[x]`. **He wrote the header before my co-sign landed and
never re-read it.** *And the sharper half is the DIRECTION:* > **THE ERROR WAS CONSERVATIVE, AND A CONSERVATIVE ERROR
NEVER GETS AUDITED — nobody challenges a checklist claiming to be LESS finished than it is. Which is exactly where a
wrong number can sit forever. Flag them anyway.**

## LIFT LEDGER: **5 of 9, plus item 10 OPEN**
```
[x] 1 coverage assertion LIVE     DELETION ONLY -- blind to collapse
[x] 2 silver rep_id NULL grounded
[x] 3 INF_B_00 selector LIVE      the ONLY collapse instrument
[x] 4 CVO~B independent verification, BY EXERCISE
[x] 5 co-sign on the PRE-REGISTERED delta   CTO + COO both GIVEN
[ ] 6 the collision -- DELETE the orphan    SOVEREIGN (Andrew); deliberately LAST
[ ] 7 the first re-derive WATCHED against the delta
[ ] 8 the COLLAPSE DETECTOR                 DS~A
[ ] 9 removing the selector BREAKS THE BUILD (AST, not grep)  DS~A
[?] 10 *** BYPASS: does anything ELSE derive an advisor from a raw date-keyed roster? ***  DS~A -- FIRST
```
**Nothing lifts today. The denominator has grown twice and may grow a third time — and every growth came from an
agent declaring the limits of their own instrument rather than banking a green.**
