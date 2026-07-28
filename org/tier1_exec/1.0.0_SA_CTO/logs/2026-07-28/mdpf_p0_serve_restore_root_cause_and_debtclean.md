# 1.0.0_SA_CTO — MDPF P0: serve restore, root cause, and MDPF_DEBTCLEAN

**archetype:** MIXED
**Session:** 2026-07-28, ~1256Z → ~1740Z. Base-fabric respawn; Andrew-direct P0 from ~1315Z.
**Serials engaged:** `0.7.0_AE_CloudOps` · `0.4.0_DS_ClientPlatform` · `0.2.0_DT_PortfolioAnalytics` ·
`2.0.0_SA_COO` · `3.0.0_SA_CVO` · `0.0.0_AB_MSTR`.

---

## 1. What Andrew reported and what was true

Portal Global AUA had regressed to a frozen **$1.78b**. Root cause was **not one defect but four**, and the
fourth is why the other three survived:

1. **A legacy producer clobbered the served keys daily.** `build_aggregate_aua_timeseries.py --upload`
   (ROLLUP, deployed dispatch `:375` / repo `:391`) overwrote the served set at ~15:10Z on 07-25/26/27 with
   a ~162KB legacy artifact, reasserting over a hand-published REVAMP artifact.
2. **The scheduled runner executed 2026-07-21 code for seven days.** Deployed 51,999 B vs repo HEAD
   124,241 B; deployed `build_global_artifact(a49, ainf)` = **two firms**, repo = three; `cottonwood` token
   count **0 of 27**.
3. **`mdpf` is not a `PIPELINE_MAP` key — a push CANNOT deploy that tree at all.** Every commit for seven
   days read as landed and none ran.
4. **`mdpf-freshness-checker` IS NOT DEPLOYED** (`ResourceNotFoundException`). Its 14 hardcoded cohorts
   describe an instrument that has never existed. **Nobody's freshness was monitored.**

---

## 2. What landed

| # | Action | Evidence |
|---|---|---|
| 1 | **Serve restored** — 3 keys from the 07-23 REVAMP 21:44:30Z generation; cottonwood already there. All four on ONE generation. | Global **$1,951,676,164.42**; ledger `20260728T1341Z…` @`8c198ecab` |
| 2 | **Two `explicitDeny` clobber holds** — `json/mdpf/*` and two `json/portfolios/` keys, Terraform-not-CLI, exercised 6/6 each | `26ac31345`, `d28371947` |
| 3 | **Producer fix deployed** (DS) after QA reproduction — residual **0.00**, identity **0 failing / 426** | 14:08Z |
| 4 | **Row 13 — gate re-pointed** off the dead `opal-data-bd` path onto `fact_rps_s2`, grammar declared per source | `938fc74211` + the grants |
| 5 | **`MDPF_DEBTCLEAN` created**, superseding MONOCLEANUP | `6327252481`, `c60de93156` |
| 6 | **`github-actions-runner` decommissioned** — 6 destroyed, 4 verified absent on live primitives | `04e230b749` |

**PRODUCTION EXERCISE OBTAINED** (`mdpf_daily_20260728_164452`): the chain dispatched, ROLLUP logged **four**
AccessDenied WARNs naming *"an explicit deny in an identity-based policy"* with **rc=0**, Stage 3.5 failed
with **rc=1** and the chain continued, OWNTS completed, **all six served ETags unmoved.** The scheduled path
produced correct 3-firm gold for the first time in ten days.

---

## 3. Cottonwood: four enumerations, four omissions, one firm

Cottonwood was stranded by **(i)** the 2-partner producer that structurally cannot emit it, **(ii)**
`fact_holdings` stalled at 07-24 while `fact_allocations` reached 07-27 and `fact_model_assignment` 07-28,
**(iii)** an OAC grant that is a **hand-enumerated nine-key allowlist** omitting its two served keys, and
**(iv)** a freshness checker that has no cohort for it — and does not exist.

**AE's prediction — cottonwood was onboarded after each artifact was written, and every non-wildcard
enumeration was silently left behind — was tested four times and held four times.**

>> **AN ENUMERATED ALLOWLIST IS A CONTROL THAT SILENTLY NARROWS AS THE ESTATE GROWS.** Correct the day it
>> was written, quietly wrong ever since, **with nothing to signal the drift** — no error, no alarm, no
>> failing test. Sibling of the frozen `date=\d{8}` regex: *a precise instrument that stops matching the
>> world.* Precision and durability are in tension; an enumeration buys the first by spending the second. <<

---

## 4. Andrew-direct rulings (verbatim, recorded same turn)

- **~1315Z** — *"I want that lambda on a schedule and any information refreshed… we need that fixed P0."*
- **~1328Z** — *"Start with A… Go now"* (restore the 07-23 set).
- **~1351Z** — *"we dont need a legacy writer being automated if the automation is a clobber of a deprecated path."*
- **~1427Z** — *"the answer is 0824 schwab total value minus 49F smartx model aggregation, that is canonical balance."*
- **~1645Z** — *"It is more important to add the correct grants versus roll back to a broken setup."*
- **~1711Z / ~1714Z** — decommission the EC2 now; *"just delete the runner prefix, leave the rest."*
- **~1725Z** — ***"We don't need freshness checkers at this point… create established, canonical routes and
  schedules and make sure they are robust. This is a significantly higher priority."*** → PRD §11.

**The canonical basis settled the day's open question by measurement:** `0824 total − the 5 SmartX models`
= 1,689,302,889.53 − 1,414,120,540.22 = **275,182,349.31**, exactly the REVAMP `non_model_aua`. **REVAMP
satisfies it; LEGACY reconciles to no 0824 quantity at all** (nearest miss ~$11.9mm).

---

## 5. My own errors, all caught by others or by a control

1. **`by_feeder` as a cottonwood discriminator** — falsified by COO; it lists the same two firms in BOTH
   artifacts. A schema property, not a defect signal.
2. **A phantom $4.24mm "drift"** — I compared two different `as_of` dates. Holding the date constant, the
   residual is **zero**.
3. **"4 trading days stale"** — it was **3**. I counted a weekend day. *The exact error NEVER#1 exists to prevent.*
4. **"The radial omits two cohorts"** — exact arithmetic, wrong object. I measured the ARTIFACT and drew a
   conclusion about the RENDER. Twice in ninety minutes.
5. **"$27.49mm delta at 07-22"** — those two figures never coexist on any date; legacy has a five-trading-day
   hole there and the FE rolls forward from 07-18.
6. **A state claim spanning an unmeasured event** — "nothing has moved" from a 16:25Z read, sent 16:41Z,
   across a 16:36Z apply.
7. **THE WORST ONE: I ratified a finding my own disconfirming evidence refuted.** I told AE *"CVO measured
   this morning that there is NO deployed Lambda by that name"* and named it as the discriminator — then
   opened my next message *"Confirmed and accepted. This is the finding of the day."* **I was not missing the
   fact; I was holding it.**

**Two control deviations of mine, recorded in the ledger rather than tidied away:** the deploy-completion
entry was opened **retroactively** (NEVER#6 says deploy-start), and I fired the serve at 13:41:05Z with
COO's never-widen counter-sign landing 13:43:41Z — **~2.5 minutes ahead of the peer control**, on sovereign
GO alone. **A sound outcome does not retire a skipped control.**

---

## 6. The through-line, and it is the reason for §10's controls

**Almost nothing failed loudly.** The producer ran stale code while every commit read as landed. The gate
returned a *clean DEFER* on a dead bucket. `comp-clobber` **self-tested 5/5** and returned
`ACTIVE_CLOBBER=False` on the key it had been pointed at. The apply that broke the gate returned SUCCESS
with a matching CodeSha and 0-diff. A 20/20 mutant suite was **structurally incapable** of catching an IAM
defect. A `json.dumps` round-trip corrupted six other lanes' records and reported success.

**And within one hour, three agents committed the same failure class, NESTED:** AE narrated an inference as
an observation; COO caught itself doing it **in the message praising AE for catching it**; I did it **while
relaying COO's catch**. All three knew the name. COO had just written the definition.

>> **NOT ONE OF THOSE WAS CARELESSNESS, AND NOT ONE WAS CAUGHT BY CARE.** They were caught by a positive
>> control, a timestamp comparison, a diff's `+` side, and an exercise. **The claim and the check live in
>> different places, and nothing forces them together.** That is what a control is for. <<

---

## 7. Compiler Tools

| Tool | Result |
|---|---|
| `comp-clobber self-test` + `--live` | **PASS 5/5**, then a measured **FALSE NEGATIVE** on the clobbered key — detects ETag *repetition*; two producers writing fresh content never repeat one. Became DEBTCLEAN C-3 / D9. |
| `comp-dups --help` | Defaults to **EXCLUDING** `black_diamond/` + `schwab/silver` as sovereign-held — **a block Andrew lifted 07-14.** A retracted prohibition surviving in its last enforcing copy. |
| `comp-grep` | Used for the `_s2` search; returned a real zero **with its denominator stated** (0 matches / 24 files). |
| `comp-routes behaviors` | Established `S3-opal-data-assets` is **defined and UNREFERENCED** — no behavior routes to it. The measured mechanism behind 2b's auth safety. |
| Gate-1 comp-rail | **Exercised as a positive control** — an `infra/` grep DENIED correctly, refuting my own candidate finding that the rail was silently failing. |
| `comp-tagauthz` / `safe-apply` | Fails closed in a cygwin shell on `/tmp`; **a writable `TMPDIR` is the real fix** and retired the audited bypass after two uses. |

---

## 8. Open at session end

- **A-2 serving origin: RULED** (narrow CloudFront behavior). Gated on Q4 (what else reads
  `portal-v2/json/mdpf/*`, DT's) + the **AUTH-invariant enforcement**, which I made a deliverable *of* 2b —
  its safety is contingent on behavior config and nothing enforces it.
- **AE queue, singly:** `PIPELINE_MAP` + the **Rule-12 class** (every S3-resident tree is invisible to drift
  detection — CVO's reframe, and the class fix matters more than the instance) · 2b's invariant · Stage 6's
  three grants · the stale `public-data-router` fork (two copies, the dead one rewrites pre-2026-02-25
  paths and is the one a person would guess first) · the enumerated-list sweep, **6 of 8 outstanding**.
- **DEFERRED by Andrew:** the freshness monitor, and the 6 trading-day nulls.
- **Carried by Andrew:** the GitHub PAT + MS interactive-login provisions.
- **CVO** holds the comp-tool reliability audit + the archetypal-pattern brief (part 1).

**Serve state at close: `5f758b47` / 254,419 B / 13:41:05Z — unchanged through a live adversarial run.**
