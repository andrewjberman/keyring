# 0.7.0_AE_CloudOps -- MDPF A-2 egress principal + cohort/consumer traces (2041-2156Z)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, TRACE

Fresh base session succeeding the context-exhausted predecessor. Launcher mission
PORTAL.MODEL_PORTFOLIOS; CTO dispatches. Window = whole session (first log of this session).

---

## Summary

Came up on-mission, found the dispatched item already in flight by another agent, escalated instead
of editing, and it was cancelled. Then executed CTO's queue: built + applied the A-2 egress
principal (staging-scoped after I surfaced a NEVER#3 blocker), delivered the ABSENT-vs-STALE cohort
census, and answered the severity gate with the DDB consumer trace.

**6 commits, all mine** (the 8 `0.7.0_AE_CloudOps~C` commits in this window are my LANE's, not this
session's -- separated by exact-author match, not the substring filter, which matches `~C` too).

---

## Work performed

### 1. Dispatched roster item -- ESCALATED, then CANCELLED (no edit made)

Launcher item: single-source the partner roster in `mdpf_aggregate_aua.py` at `:492-500`/`:1132`,
then enroll cottonwood. **I wrote nothing to that file.**

Two of my own probes straddled a live edit: at 20:44Z the roster was at `:492`/`:1132`; at 20:46:54Z
the same working tree returned `:555` (changed signature) and `:1213`, with `+102/-15` uncommitted,
mtime 20:45:31Z. The in-flight diff was doing my dispatched task and citing my authorization
(Andrew 203435Z). By 20:50:21Z the tree was CLEAN and the insertions were gone -- HEAD unmoved,
nothing in `git stash`.

Escalated to CTO (205114Z) rather than attributing or editing. **Resolution: it was `0.4.0_DS`
executing CTO's 203955Z GO, reverted at 204655Z in compliance with CTO's hold, and PRESERVED as a
patch** (`deliverables/HELD_20260728T2046Z_roster_single_source/`, all 3 artifacts verified present).
A double-dispatch CTO owns. **Item CANCELLED 205446Z** (reading 1, canonical-only; Ruling 1 intact).

Design work banked before cancellation -> `155de3ff41`. Key finding: **"enroll cottonwood" was a
misnomer** -- cottonwood has been a declared roster partner since 07-24; the script never ASKS. The
literal reading of the dispatch would have added a 4th string to a hardcoded list AND falsely
asserted cottonwood COUNT back to 05-28 against its own `unbackfillable_before: 2026-07-22`.

**DS accepted both my findings and landed `97a8814ed`** -- F-2 was worse than I reported (BOTH call
sites, not one) and DS fixed it harder than proposed, removing the defaults so under-specification
raises `TypeError`, plus an `inspect.signature` test that fails if a default returns.

### 2. A-2 SEPARATE EGRESS PRINCIPAL -- built, applied, verified, ledger closed

**The blocker I surfaced pre-build:** `opal-data-portal-v2`'s bucket policy has **ZERO Deny
statements** (2 statements, both Allow/GetObject for CloudFront). Both explicitDenys protecting the
frozen MDPF serve live on `mdpf-daily-runner-ec2-role` -- **principal-scoped, not resource-scoped.**
So a new principal writing `platinum/mdpf/*` would not be blocked by them, not weaken them, and not
be visible to them: a **second door** into a serve frozen by design and hand-published. That is
NEVER#3 (CTO+COO), which the A-2 ruling did not carry.

**CTO concurred** (he had written that principal-scoped warning himself at 202502Z), declined to
self-grant both halves, and rescoped the applied grant to a NON-SERVED staging prefix.

Landed `a11b8e2cc3` -> applied -> `d36ba22678` (ledger closed) -> `fe5c97c21c` (process miss).

### 3. Cohort census -- ABSENT vs STALE-BUT-PRESENT (`430ca6a55a`)

Own denominator: 32 rows @ `run_date=2026-07-28` (ScannedCount 35,078); 14 missing / 13
rolled_forward / 5 fresh -- independently reproducing COO's floor. COO's ~$522mm verified EXACTLY at
`$522,484,735.05`.

**The "13 stale" is three populations, not one** (resolved on `lib/trading_calendar.py`, never
wall-clock): 4 cohorts at T-16 (the defect), 7 at T-2 (4 of them cottonwood at its DECLARED D+2
cadence), and **2 at T-1 -- HEALTHY, the documented default.** Reporting all 13 as stalled would have
been a **false outage** (NEVER#1). CTO called this the most important line in the report.

**Mechanism: I got it wrong first and corrected before commit.** I concluded "the upstream source
stopped" from `opal-data-etfs/daily/49financial/` being stale since 07-06 -- positive-controlled
against `daily/cottonwood/`, which is current. Both measurements true, the inference false: I had
grounded **the artifact the producer's own `source_field` NAMED**. The emitter's ACTUAL input carried
`partner_held_etf: 2026-07-28` and `held 180,276,733.36`. **The fresh value was in the file it read.**
CTO banked this as a new doctrine class (§III-f): *a self-report used as a POINTER rather than as a
VALUE defeats every control you run -- my positive control REINFORCED the wrong conclusion.*

### 4. DDB consumer trace -- the severity gate (`2f6d16da64`)

**No live external consumer of the ETF cohorts on the DDB plane.** Six predicates, each with its
blind spot stated. CTO's "floor" consumer is **DORMANT**: `load_ddb_0824_custody_history()` is defined
and never invoked (`:822` comment "retained for that alignment harness"; `:823` calls
`load_rps_custody_history` instead). Corroborated on the applied plane: the host role has ZERO
dynamodb, `Scan -> implicitDeny` with a positive control returning `allowed`.

The one two-hop reader of this table is **the emitter itself** (`:900`), backing a value-repeat
guard -- so **`vintage_state` is EMITTER-DERIVED, not source-passthrough.**

**Explicitly NOT priced as harmless:** the same numbers exist as served S3 artifacts on DT's plane.

---

## Deployment Sequence + Verification (AE role requirement)

**Deploy:** MDPF A-2 egress principal, staging-scoped. Ledger opened 2123Z, closed 2126Z. NEVER#6
discharged in-session.

```
1. TF written        infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf (+ router_iam.tf census note)
2. fmt + validate    fmt -check rc=0 ; "Success! The configuration is valid."
3. commit BEFORE apply (Rule 2)   a11b8e2cc3 -> pushed
4. targeted plan     Plan: 3 to add, 0 to change, 0 to destroy
                     live-serve policy ABSENT from plan (count=0 held)
5. PRE-APPLY battery simulate-custom-policy (role did not exist yet -- simulate-principal-policy
                     structurally unavailable). Policy extracted FROM THE PLAN via
                     `terraform show -json`, NOT retyped.  7/7.
6. apply             .tools/safe-apply.sh apply -target=... (Rule 18; NOT bare terraform)
7. re-plan           "No changes. Your infrastructure matches the configuration."
8. APPLIED truth     live primitives, below
```

**ACTUAL verification output:**
```
$ aws iam get-role-policy --role-name opal-assets-mdpf-egress-publisher-role \
      --policy-name opal-assets-mdpf-egress-publisher-scoped
ReadPortalGoldMdpf   Allow   arn:aws:s3:::opal-data-assets/portal/gold/mdpf/*
WriteStagingMdpf     Allow   arn:aws:s3:::opal-data-portal-v2/platinum/_staging/mdpf/*
ListPortalGoldMdpf   Allow   arn:aws:s3:::opal-data-assets
ListStagingMdpf      Allow   arn:aws:s3:::opal-data-portal-v2

$ aws iam list-attached-role-policies --role-name opal-assets-mdpf-egress-publisher-role
AWSLambdaBasicExecutionRole                      <- NO FENCE, as designed

$ aws iam list-role-policies --role-name opal-assets-mdpf-egress-publisher-role
opal-assets-mdpf-egress-publisher-scoped         <- live-serve policy ABSENT, count=0 held
```

**APPLIED battery -- simulate-principal-policy against the LIVE role, 8/8**
(one `--resource-arns` per call; every control a SEPARATE invocation):
```
A1 PutObject platinum/_staging/mdpf/global/...            allowed        positive
A2 PutObject platinum/mdpf/global/...      (LIVE SERVED)  implicitDeny   THE BOUNDARY
A3 GetObject portal/gold/mdpf/...                         allowed
A4 GetObject opal-data-bd/bronze/...       (SOURCE)       implicitDeny
A5 PutObject opal-data-assets/...          (reads it)     implicitDeny
A6 ListBucket WITH --context-entries                      allowed
T8 GetObject opal-data-assets/schwab/08242234/silver/...  implicitDeny   read-side firm boundary
T9 GetObject opal-data-assets/blackdiamond/cottonwood/... implicitDeny   read-side firm boundary
```
A2 is discriminated from the nonexistent-action artifact by A1 returning `allowed` on the SAME
action string -- simulate does NOT validate action names, so a typo denies byte-identically.

**STOP CONDITION HELD: the serve did not widen.** Zero S3 objects written; no served ETag moved.

**PROCESS MISS, recorded `fe5c97c21c`:** CTO's apply-authorisation was conditional on T8/T9 running
**BEFORE** apply. That message landed while the apply was in flight and I applied without them. Both
pass, but a gate satisfied after the irreversible step is not the gate that was asked for. CTO
recorded it as a crossing rather than a violation; I recorded it as a miss either way.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `opal-assets-daily-aua` | PASS | Denominator for the consumer trace; surfaced 2 code-bearing refs vs many doc refs |
| `comp-which` rail (HUD gate) | fired twice on `infra/*` greps | PASS | Gate worked as designed; both proceeded with an audited `# rail-checked:` marker naming why no comp-tool fits (a bash-var literal; live managed-policy attachment count) |
| `.tools/terraform.exe fmt/validate/plan` | opal-assets root | PASS | fmt rc=0; "configuration is valid"; plan 3/0/0 with the gated resource correctly absent |
| `.tools/safe-apply.sh` | `apply -target=...` | PASS | Rule 18 wrapper. First invocation errored usefully -- it requires the `apply` subcommand explicitly, not just flags |
| `.tools/safe-commit.sh` | 6 commits, `-F` | PASS | `-F` throughout per the commit-message-is-an-execution-vector rule; `/tmp` is not writable here, scratchpad used |
| `lib/trading_calendar.py` | `trading_days_behind` | PASS | THE control that prevented a false outage: 07-27 = T-1 = healthy, not stale |
| `comp-iam` | not run for the new role | N/A -- deliberate | It models `(action)`, never `(action, resource)`, and fails GREEN. For a NEW principal on a bucket it has never touched, `simulate-*-policy` on exact ARNs is the only sufficient instrument (Rule 22a) |

**What worked:** extracting the policy document **from the plan** rather than retyping it -- a
hand-transcribed policy tests what you typed, not what will land. CTO called it the single most
valuable line in the report.

**What failed:** my own probes, three times -- see Gap.

**Gap found:** `comp-grep` is `.gitignore`+submodule-aware, so **it structurally cannot see the
portal** (the parent repo tracks 1 gitlink file). Any consumer census run with it must state that
bound or it silently under-reports.

---

## Blockers

**None of mine.** Gated at others, evidence-cited:
- **[1.0.0_SA_CTO + 2.0.0_SA_COO]** the NEVER#3 never-widen co-sign to flip
  `var.mdpf_egress_live_serve_write_cosigned`. CTO holds the CTO half and takes it to COO with
  verified-publisher evidence. **AE does not flip it.**
- **[0.2.0_DT_PortfolioAnalytics]** the S3-object-side consumer census. Severity of the $522mm T-16
  staleness cannot be fully priced until that lands; my DDB-plane answer closes only one path.

---

## Current State

- **`opal-assets-mdpf-egress-publisher-role` is LIVE** (`a11b8e2cc3` / `d36ba22678`). Reads
  `opal-data-assets/portal/gold/mdpf/*`, writes `opal-data-portal-v2/platinum/_staging/mdpf/*`,
  **not on the one-way-fan-in fence** (deliberate misclassification repair; rationale verbatim in
  the TF description). Cannot write anything served. Ledger CLOSED.
- **`var.mdpf_egress_live_serve_write_cosigned` = false.** The live-serve grant exists as reviewable
  code with `count = 0`; flipping it is the single irreversible step and needs CTO+COO.
- **`router_iam.tf`** now carries a census warning: TF declares 6 fence attachments, LIVE has 12
  (six silver roles via `for_each`). Ground the member census on `list-entities-for-policy`.
- **`mdpf_aggregate_aua.py` is UNTOUCHED** and byte-identical to HEAD. Item cancelled; DS's patch is
  preserved and re-appliable, with my quantity-blindness catch recorded against it.
- **Deliverables:** `MDPF_ROSTER_SINGLE_SOURCE_FINDINGS_20260728.md` (F-1..F-6),
  `MDPF_COHORT_ABSENT_VS_STALE_CENSUS_20260728.md`, `MDPF_DDB_CONSUMER_TRACE_20260728.md`.
- **MEMORY.md is at exactly 17408/17408 bytes -- ZERO headroom.** I amended entry 11 (its old
  "use explicit-`Z` forms" advice is what produced my forged-`Z` error) and kept it net +5, but the
  next agent to add an index line silently truncates the tail. **Needs an operator/MSTR compaction
  pass; not mine to do unilaterally to shared memory.**

---

## Next Steps

1. **[1.0.0_SA_CTO]** next queue item -- ④ the stale `public-data-router` fork, or question (3) on
   `_total__partner_aua`. I have a HYPOTHESIS on (3): the emitter already carries the right doctrine
   at `:1132` ("a total's vintage is the worst of its contributors', never the artifact's") and the
   ETF total implements it; the partner total appears not to. **I have not read that code path.**
2. **[1.0.0_SA_CTO + 2.0.0_SA_COO]** the never-widen co-sign decision.
3. **[0.2.0_DT_PortfolioAnalytics]** S3-object-side census -> completes the severity pricing.
4. **[0.0.0_AB_MSTR]** MEMORY.md compaction -- at the cap, zero headroom.
5. **[0.7.0_AE_CloudOps]** AE-lane, logged not solved: the roster must be PUBLISHED INTO
   `s3://opal-data-mdpf/code/scripts/` for any runner-executed gold script to consume it (measured
   ABSENT; `--delete` removes hand-placed copies). CTO ruled this a `CODE_TREES` entry, not a
   bespoke copy step -- `~C` notified.

---

## Corrections I made to my own work this session

Recorded because three of tonight's six fabric-wide near-misses were mine, all one root -- reading a
value without establishing what it is OF:

1. **Claimed `0.5.0_AE_OpalETL` was live and committing tonight** and derived "the broker roster
   can't be trusted." Those commits are **2026-07-09**. I ran `git log --date=format:'%H:%M:%SZ'` --
   discards the DATE, renders LOCAL -- with the `Z` **typed by me, not computed**. RETRACTED; the
   broker was right. CTO banked the lesson: *a fabricated marker is worse than an ambiguous one,
   because ambiguity prompts the check and a forged marker cancels it.*
2. **Labelled `staleness = 99` a MISMATCH** against the calendar's 16. It is a **documented
   sentinel**, deliberately shared with 14 live alarms "so row and alarm agree by construction."
   Had I "fixed" it I would have silently desynchronised 14 alarms from their rows.
3. **Read `held_by_partner[].held_value`, got `null` everywhere**, and was one step from reporting
   COO's figures as fabricated. **The field is `held`.** My null was my own query artifact.
4. **Counted two nonexistent directories as clean sweeps** (`portal/app`, `portal/lib`) -- discarded;
   they would have inflated one real sweep into three.
