# CI-R4 — CLOSURE ROW 4: THE SEVER-A-CHANNEL EXERCISE — CVO VERDICT

    verifier:      3.0.0_SA_CVO
    TO:            MDPF_CHANNEL_INDEPENDENCE.CI-R4 @f5dd6c4940
    PRD:           docs/architecture/MDPF_CHANNEL_INDEPENDENCE_PRD.md @eaa8433547 §3a row 4
    row 4:         "No cross-partner gate exists ANYWHERE between vendor and served artifact"
    commit-ishes pinned (RAVC 3a):
                   producer  infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py @ed415e2682
                   deployed  mdpf-daily-trigger LastModified 2026-07-10T00:17:02Z,
                             CodeSha256 Y5py4xQ3Ar4CoIy13LuGpt1gF0Oa1qQRS1jjFCKVzMU=, GATE_ENFORCE=1
                   repo HEAD at verification: 48f590d26a

    VERDICT:       **NOT-EXERCISABLE-YET**
                   — reached on my own grounding, and on a DIFFERENT BASIS than the one I was given.

---

## 0. WHY THE BASIS MATTERS MORE THAN THE VERDICT

COO predicted NOT-EXERCISABLE-YET and then **withdrew the prediction unprompted** ("a verifier told to
expect NOT-EXERCISABLE-YET is a verifier primed to accept it"). That was the right call, and I had
already refused to inherit it. I grounded all three legs of the premise independently. **Two held, one
did not, and the one that did not is the leg the original reasoning rested on.**

| leg | claim as given | my finding |
|---|---|---|
| 1 | C1/C2/C3 not landed | **TRUE** |
| 2 | Actions billing-block prevents landing | **FALSE as a reason** — the outage took a CONTROL, not a route |
| 3 | current architecture has the cross-partner gate | **TRUE — but not the gate the PRD describes** |

**The verdict survives on leg 1 alone: the contracts do not exist yet, so the architecture row 4
verifies does not exist yet. Nothing can sever a channel in an architecture that has not been built.**

---

## 1. LEG 1 — C1/C2/C3 ARE NOT LANDED (verdict basis)

Every `MDPF_CHANNEL_INDEPENDENCE` commit at HEAD is a **PRD or a TO**. No contract implementation:

    86f58473d6  13:07Z  CTO  prd(...) partner-channel independence
    567221883e  13:09Z  CTO  prd(...) broaden to a CLOSURE definition + 12-row closure set
    eaa8433547  13:11Z  CTO  prd(...) s3.1/3.2 DATA-AS-OF vs PROCESS TIME
    00b36eac9e  13:23Z  COO  to(...) decomposition -- first two TOs
    f5dd6c4940  13:30Z  COO  to(... -> CVO) CI-R4  <- this TO
    b9b6b6b262  13:37Z  COO  to(...) final three TOs
    f642948889  13:38Z  CTO  prd(...) s2.6 AMENDED

**Denominator: 8 commits matching the project at HEAD `48f590d26a`; contract implementations among
them: 0.** Row 4 verifies the FIXED architecture. It is not built. **That is the whole verdict.**

## 2. LEG 2 — THE DEPLOY-BLOCKED REASONING IS WRONG, AND I CONFIRMED IT MYSELF

`gh run list` (read-only; **I dispatched nothing** — a dispatch is an action with side effects and is
not mine to take) shows `lambda-deploy.yml` and `ec2-deploy.yml` at `conclusion: failure`, repeatedly,
17:26–17:39Z. **The runs do fail. The inference drawn from it was wrong.**

`.github/workflows/lambda-deploy.yml:1` is `name: Lambda Drift Check`, and `:8` states verbatim:
*"Reports drift but does NOT deploy — all deploys go through terraform apply."* Terraform runs
**locally** via `safe-apply.sh` (CLAUDE.md Rule 1 / Rule 18).

**So the Actions outage did not block landing. It removed the DRIFT DETECTOR.** COO reached this
independently and told me before I asked; I verified it at source rather than accept the correction.

>> **AND THIS PRODUCES A CONSEQUENCE NOBODY HAS STATED, WHICH BEARS DIRECTLY ON ROW 4'S FUTURE
   VALIDITY.** If C1/C2/C3 land while drift detection is dark, then at exercise time **"the contracts
   are deployed" is itself an unverified claim.** My exercise would be severing a channel in an
   architecture I cannot confirm is the one that was built — and a row-4 PASS obtained against an
   unconfirmed deployment is exactly the class of result this PRD exists to prevent.
   **REQUIREMENT I AM IMPOSING ON MY OWN FUTURE VERDICT: before exercising row 4 I will ground each
   contract's DEPLOYED state on the live primitive** (`get-function-configuration` CodeSha256 /
   `describe-*` / event-source config), **not on the drift check and not on a builder's report.**

## 3. LEG 3 — THE CROSS-PARTNER GATE EXISTS, AND IT IS **NOT** THE ONE THE PRD DESCRIBES

This is the leg nobody asked me to check, and it is where the substance is.

**The PRD §1 defect 2 says: "All-or-nothing partner gating — one stale partner defers everything."**
**That mechanism was REMOVED on 2026-07-09 and the removal is deployed.** At `@ed415e2682`:

    :520  partners = {"49financial": bd}   # inflection is the spine/DRIVER, not a skippable partner
    :535  "all_fresh": bool(inf["fresh"] and bd["fresh"]),  # retained for log continuity
    :541  if GATE_ENFORCE and not gate["spine_fresh"]:      # ONLY THE DRIVER HALTS

`:515-519` records why, quoting Andrew 2026-07-09: *"49 Financial should not hold up MDPF, that is
nonsensical."* **`all_fresh` is computed and logged but no longer decides anything.** Deployed
2026-07-10T00:17:02Z — so repo and runtime agree, and I checked rather than assumed.

**So what actually froze the product for six days?** I read the decision, not the narrative.
CloudWatch `/aws/lambda/mdpf-daily-trigger`, window 2026-07-24T14:55:00Z..15:15:00Z:

    DEFER: mdpf per-partner roll-source unavailable
      reason: "stale partner(s) with no readable roll-forward block: ROLL_SOURCE_UNREADABLE"
      unresolvable_partners: [{"partner":"49financial","as_of":"2026-07-15",
                               "reason":"ROLL_SOURCE_UNREADABLE"}]
      gate: inflection fresh=TRUE as_of 2026-07-24 · spine_fresh=TRUE
            49financial fresh=false, trading_days_behind=7 · all_fresh=false

**The spine was FRESH. The build deferred anyway.** Not via the all-or-nothing gate — via the
roll-source fail-safe at `:562-576`. **That IS a live cross-partner gate: a stale 49F stopped a healthy
Inflection from publishing. Row 4 is NOT satisfied today.** But it is satisfied-or-not by a
*conditional* gate, and the condition is the part that matters (§5).

---

## 4. THIRTEENTH ITEM — TO CTO'S GATE AS AN AMENDMENT, WITH EVIDENCE

**`ROLL_SOURCE_UNREADABLE` IS A MISDIAGNOSIS. THE TRUE CONDITION IS `ROLL_SOURCE_ABSENT`, AND THE
DISCRIMINATOR BUILT TO SEPARATE THEM IS DEFEATED BY S3'S OWN PERMISSION SEMANTICS.**

`_roll_source_exists` (`:338-370 @ed415e2682`) maps the HEAD result three ways, and its docstring is
explicit about why:

    ROLL_SOURCE_ABSENT     -- 404: genuinely not there. A DATA condition, expected.
    ROLL_SOURCE_UNREADABLE -- 403: the INSTRUMENT is broken (missing IAM grant). A CONFIG fault
                              that will NEVER clear on its own -- must be LOUD + distinctly named.

**Measured:**

| probe | result |
|---|---|
| `head-object opal-data-portal-v2 platinum/mdpf/aggregate_aua/2026-07-15.json` (my creds) | **404 Not Found** |
| the prefix's actual contents | 07-18, 07-17, 07-16, 07-10, 07-08 — **no 07-15** |
| trigger role inline policy `mdpf-trigger-scoped` | `s3:GetObject` on `.../aggregate_aua/*` — **and `s3:ListBucket` ONLY on `arn:aws:s3:::opal-data-bd`** |
| `simulate-principal-policy` `s3:ListBucket` on `arn:aws:s3:::opal-data-portal-v2` (single ARN) | **implicitDeny** |
| positive control, **separate invocation**, `s3:GetObject` on an existing key | **allowed** |

**MECHANISM, SOURCE-CONFIRMED AND EXERCISED:** S3 returns **403 rather than 404 for a missing key**
when the caller lacks `s3:ListBucket` on the bucket — it will not disclose existence. The role has
`GetObject` but no `ListBucket` on `opal-data-portal-v2`. **So a genuinely-ABSENT block returns 403,
and the gate classifies an expected DATA condition as a permanent CONFIG/IAM fault.**

**Why this is more than a mislabel:**
1. The code's own comment says UNREADABLE *"will NEVER clear on its own"* — so the condition is
   treated as permanent when it is in fact **transient and self-clearing** the moment a 07-15 block
   lands (or the stale partner advances).
2. `mdpf-freshness-checker` was designed to *"alarm on a CONFIG fault and never on ABSENT."* It has
   therefore been alarming — or routing — on the wrong class for six days.
3. **The remedy is inverted.** UNREADABLE points an operator at IAM. The actual missing thing is a
   served platinum block for 2026-07-15.

>> **THE SHAPE, BECAUSE IT IS THE THIRD TIME TODAY.** This discriminator was built specifically to fix
   *"'cannot read it' and 'it does not exist' print the same nothing"* (its own comment, citing the
   0.6.0 BLOCK). **It is defeated by the exact semantics it was written to disambiguate**, and it fails
   toward the more alarming, more permanent-sounding classification. Same family as this morning's grep
   binary-mode truncation and the opening-token census matcher: **an instrument that returns a
   confident, plausible, wrong answer, with nothing in its output marking it as wrong.**

**RECOMMENDED (CTO's call, not mine to design):** grant `s3:ListBucket` on `opal-data-portal-v2`
scoped to the `platinum/mdpf/aggregate_aua/*` prefix so 404 and 403 become distinguishable at all — the
discriminator cannot work without it. **Until then, every ABSENT reads as UNREADABLE and the two
branches are one branch wearing two names.** I am not proposing the policy text; I verify.

---

## 5. THE EXERCISE, DEFINED AND READY TO RUN (AC-3)

Row 4's exercise is **not** "sever anything and watch." The surviving gate is **conditional**, and a
naive exercise passes while leaving the real gate untested.

### 5.1 The trap that is specific to THIS architecture

    a stale partner WITH a readable roll-forward block  -> SKIP + roll forward -> others publish  (PASS)
    a stale partner WITHOUT one                         -> DEFER EVERYTHING              (CROSS-GATE)

**A sever that leaves the severed partner's roll-source block present takes the SKIP path and PASSES —
while the path that actually froze the product for six days is never exercised.** Any row-4 exercise
that does not control roll-source state is measuring the branch that already works.

**THEREFORE THE EXERCISE HAS TWO CASES AND BOTH MUST RUN:**
- **Case A — roll-source PRESENT.** Expect: severed channel skipped, other two publish. Tests the skip.
- **Case B — roll-source ABSENT.** Expect *today*: defer-everything (cross-gate confirmed). Expect
  under the fixed architecture: **the other two still publish.** **Case B is the real row 4.**

### 5.2 Subject selection — and why the obvious second choice is also wrong

- **COTTONWOOD — DISQUALIFIED.** Count feed permanently absent, vendor D+2 by design,
  `allocations`+`unrealized` unchanged since 07-17. Severing a channel that was not publishing cannot
  demonstrate that severing one *would* stop the others. (COO's named trap; I concur and record it
  rather than silently avoid it.)
- **INFLECTION — DISQUALIFIED UNDER THE CURRENT ARCHITECTURE, and this is my own finding.** `:520`
  makes Inflection **the spine/DRIVER, not a skippable partner**, and `:541` defers on a stale spine
  **by design**. Severing INF today would produce a defer-everything that looks exactly like
  CROSS-GATE-FOUND but is the driver halting as specified. **That would be a FALSE POSITIVE — a
  verifier reporting a cross-partner gate where the design intends a driver halt.**
- **49 FINANCIAL — THE ONLY VALID SUBJECT** under the current topology: a genuine skippable partner,
  currently producing.

>> **AND THE DESIGN CONSEQUENCE THAT FOLLOWS, WHICH I FLAG FOR CTO'S GATE:** **row 4 cannot pass while
   a "spine/DRIVER" exists at all.** A driver is definitionally a cross-partner gate — every other
   channel is a passenger on its liveness. If C1/C2/C3 preserve the driver concept, row 4 fails by
   construction no matter how the contracts behave. **§2.1's "channels are the unit" and `:520`'s
   spine/driver cannot both be true.**

### 5.3 Procedure — runnable the moment the contracts land

1. **PRE — establish the subject was ALIVE at severance** (not merely that artifacts exist). Record
   49F's silver latest partition + `count_provenance`, and the **served artifact ETag + explicit-Z
   LastModified** for all three channels. Pin the artifact **build**, not a cardinality — *my own
   finding today: two builds both reporting 429 covered different date sets.*
2. **PRE — ground DEPLOYED state** of C1/C2/C3 on live primitives (CodeSha256 / event-source config),
   **not the drift check** (down) and **not a builder's report** (the reason this row is mine).
3. **SEVER** — reversibly, without a deploy: suppress the 49F channel's bronze→silver event input for
   one cycle. **No producer edit, no IAM change, no code change.** Record method + exact `Z` time.
4. **RUN both cases** — A with the roll-source block present, B with it absent.
5. **LIMB 1 — the other two PUBLISHED AFTER severance.** New ETag **and** LastModified strictly greater
   than the severance timestamp. **Existence is not publication.**
6. **LIMB 2 — the severed channel's own output STOPPED.** Its ETag must be **unchanged** across the
   window. **Without limb 2 nothing was severed and limb 1 is vacuous.**
7. **REVERSE** — restore the input, confirm 49F republishes, confirm no residual manifest state.

### 5.4 What discriminates a real pass from a vacuous one

| vacuity | discriminator |
|---|---|
| nothing was going to publish anyway | establish a publish was **DUE** — the chain is event-driven with **no schedule of its own**, so a quiet window is indistinguishable from independence. **State the triggering event.** |
| artifacts merely exist | ETag **change** + LastModified strictly after severance, explicit-Z |
| nothing was actually severed | limb 2 — severed channel's ETag unchanged |
| the skip path passed and the defer path was never touched | **run Case B** |
| a hand-fired run read as production evidence | **NEVER#4 as amended @7d2b8cf6f: an ad-hoc run is never the production path and its artifacts are never production evidence.** If the exercise is ad-hoc-triggered, **the verdict must say so** — "the other two published" is a different claim when hand-fired. |
| the driver halted and it read as a cross-gate | do not sever the spine (§5.2) |

**Verdict vocabulary:** `INDEPENDENT` requires **both limbs in Case B**. Limb 1 alone, or Case A alone,
is `NOT-EXERCISABLE-YET` — never `INDEPENDENT`.

---

## 6. WHAT SHOULD HAVE BEEN ASKED BUT WAS NOT

**Row 4 is written as a property of the FIXED architecture, but nobody has asked what row 4 costs to
KEEP.** The exercise proves independence **once**, on the day it runs. Independence is a property that
decays silently: any future change that reintroduces a shared precondition — a roster lookup, a shared
manifest write, a common IAM grant, one more fail-safe like `:562` — re-couples the channels, and
**nothing in the closure set would notice.** The 07-09 fix removed the all-or-nothing gate and a
*different* cross-partner gate was live within the same file, six days later, undetected until Andrew
looked at a chart.

**The closure set has twelve rows and no row for "independence stays true tomorrow."** A one-time
exercise verifies a state; it does not install a control. **Recommend (P2, CTO's gate, not
gate-blocking for row 4): a standing per-channel publish-independence assertion** — each channel's
served artifact advances on its own cadence regardless of the others' state, checked continuously
rather than proven once. Otherwise row 4's PASS has the same lifetime as the next fail-safe someone
adds for a good reason.

---

## VERDICT

**NOT-EXERCISABLE-YET.** The contracts C1/C2/C3 are not built; the architecture row 4 verifies does not
exist at HEAD `48f590d26a`. **I did not construct a proxy exercise against the current architecture** —
that would measure the defect rather than the fix, and would have read as row 4 to every downstream
consumer.

**Reported anyway, because it is more useful than the verdict:**
1. **The current cross-partner gate is real, live, and is NOT the one the PRD describes.** The
   all-or-nothing gate was removed 07-09; the six-day freeze came from the roll-source fail-safe at
   `:562-576` while the spine read **fresh**.
2. **THIRTEENTH ITEM:** `ROLL_SOURCE_UNREADABLE` is a misdiagnosis of `ROLL_SOURCE_ABSENT`, caused by a
   missing `s3:ListBucket` grant; the three-way discriminator is defeated by the semantics it was
   written to disambiguate, and fails toward "permanent config fault."
3. **The exercise is defined and runnable** (§5), including two cases, the disqualification of both
   Cottonwood **and** Inflection as subjects, and the vacuity discriminators.
4. **Row 4 cannot pass while a spine/DRIVER exists** — flagged to CTO's gate as a design consequence.

**This verdict is not a failure to try. It is the third state, and it is the honest one.**

— 3.0.0_SA_CVO
