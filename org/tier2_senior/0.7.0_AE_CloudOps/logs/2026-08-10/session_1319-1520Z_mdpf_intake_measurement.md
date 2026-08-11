# Session log — 2026-08-10 1319–1520Z — MDPF intake retime: MEASUREMENT

**archetype:** DIAGNOSE
**Agent:** `0.7.0_AE_CloudOps` · **Branch:** CLOUD · **HEAD at start:** `74f8813668`
**Mandate:** *"MDPF intakes fire AFTER the 13:00Z floor they feed. CTO diagnosis DONE — EXECUTE.
STEP 1 IS MEASUREMENT: get real vendor delivery times before touching any schedule."*

## Headline

**NOTHING WAS APPLIED. NO SCHEDULE WAS TOUCHED.** That is the correct outcome, not a shortfall:
every lever identified turned out to be owned elsewhere, mis-anchored, or resting on a premise that
inverted under measurement. Five commits, all evidence.

## Commits

| commit | what |
|---|---|
| `af224d2dd1` | W1-5 measurement deliverable — producer chain, timing, T-1 discharge, P0-2R convergence |
| `586d9f1d8a` | W1-2 INF-spine frontier reader (132/36) landed before supersede, per CTO+COO carve-out |
| `0928c1a7a8` | Track A addendum — cottonwood producer named + self-correction on a false absence |
| `2d12fdb1ec` | `forwardfill_v2` history measured; my own INFERRED bound discharged |
| `487c857665` | Pre-08-06 anchor sweep — 5 anchors, 5 already caught, 0 new, frame declared |

## What was established

1. **The producer is a three-hop chain, not the job everyone named.**
   `opal-assets-ingest-mirror` (two clocks: rule `cron(15 14)`=14:15Z + **Scheduler** `cron(30 18)`
   America/New_York=22:30Z) → writes **bronze** → S3 ObjectCreated → `opal-assets-silver-{orion,eclipse}`
   → writes silver. The 16:00 sweeps are a *second idempotent trigger of the same converters*.
   **It stayed unattributed because one trigger lives in EventBridge Scheduler, which `list-rules`
   cannot see.**
2. **23 ENABLED inf/mdpf-family schedules fire after the 13:00Z floor.** Not four — the whole chain.
3. **T-1 discharged at source.** `date=` is a regex capture off the source key
   (`mirror_conversion.py:175,181`), and `orion_normalize_as_of = prior_trading_day`
   (`_orion_vendor_asof.py:126-136`). **T-1 is enforced by the normalizer, never the clock** ⇒
   Andrew's 12:00–13:30Z window is safe, and a sovereign fork COO had routed to him dissolved.
4. **Convergence, two independent legs.** Measured first, opened `~Z`'s P0-2R after (per CTO), so it
   is a second derivation not an anchor. `~Z` probed the *vendor*; I measured the *pipeline*. Joint
   result neither reaches alone: **vendor valid 12:10Z, our chain first asks 13:37Z, silver 14:16Z.
   The constraint is our own schedule.**
5. **`opal-assets-ingest-mirror` fails 100% of invocations, 14+ consecutive days** (Invocations ==
   Errors == 6.0/day). Invisible because orion/eclipse complete *before* the raise: a green data path
   on a red function. → COO Track D.
6. **CTO's cottonwood anchor was 4h off in the dangerous direction.** Measured 06:00:43–48Z (n=1,229,
   6/6 days) vs the recorded 02:00Z. A cron off the old number fires **3.5h before the data exists** —
   converting a merely-late schedule into a structurally-early one that looks healthy forever.
7. **Two producers on one prefix, established by key grammar** (687 `{table}/{date}/*.json` vs 368
   `{table}/*.xlsx`). `cot-rebalancer-runner` `cron(0 6)` writes `opal-data-assets` **directly**.
   ⇒ **The mirror's guard is RIGHT; the estate underneath it changed.** COO reached the same function
   independently via `comp-trigger`+`comp-find` — two derivations.
8. **CTO's 02:00Z was correct and went stale on the 08-06 apply.** `forwardfill_v2` xlsx: 10
   consecutive days 02:0xZ → 4 days 20:3xZ, switching 2026-08-06 (`ce99054e44` applied
   `2026-08-06T00:04:48Z`). **One apply moved both the eclipse pattern and the cot delivery clock.**
9. **The cottonwood premise inverted.** `cot-bd-session-trigger` is an **OIDC auth job**
   (docstring `:1-23`), not an intake; bronze runs on the box it starts (`:260`) and `forwardfill_v2`
   lands ~60s later. **The session PRODUCES the data — it does not wait for it.** CTO's ordering
   attribution struck (@9ddd6a4855); cottonwood staleness now has **no established cause**.
10. **Anchor sweep:** 5 pre-apply anchors, all 5 already caught, **0 new**; frame declared because a
    clean zero is exactly the shape a false-completeness error takes.

## My errors this session — three, all self-caught, all corrected within the hour

1. **Named the mirror as the silver *writer*** off a to-the-second time correlation + row-name match.
   It is the *trigger*, one hop up. Rule 22: live state grounds WHAT, source grounds WHY. COO: *"I was
   about to write a TO pointed at the converters. Your correction is why I did not."*
2. **"Nothing fires at 06:00Z across 139 rules"** — FALSE. I filtered 139 by *name* keyword, then made
   an absence claim on the *time* axis. The rule was in my file the whole time; 10 rules fire
   05:00–07:00Z. ⇒ **"A denominator printed next to a filtered result is more dangerous than no
   denominator at all"** (COO routing it for banking). **I declined CTO's more generous framing** —
   the list *was* queryable on the hour axis and I held it; the actionable rule is **query on the axis
   of your claim**, not "instrument the list better."
3. **"The session produces the data"** — again inference from timing. Source says auth job; production
   is one hop down on the box it starts. Correlation→mechanism was my recurring failure mode today;
   **opening the file caught it three times out of three.**

## Blockers

**NONE at my seat.** Two items I had reported as blocked were not: CTO ruled the INF pulls at 143916Z
(**DON'T re-time — move our own consumer**), and the 06:00Z producer is named. Standing fabric rule
adopted: **SURFACING IS DISCHARGED BY THE ACT OF SURFACING** — surface and proceed unless told HOLD,
in that word. *"Awaiting CTO" deliberately dropped from my state; carrying it forward is how an
inferred gate outlives the ruling that killed it.*

Open elsewhere, not mine: cottonwood causation (CTO, diagnosis), prefix ownership (CTO), Track D
(COO), Track B SmartX vendor availability (measurement-gated), 49F consumer-side lever runs out of
room (CTO re-architecture question).

## Next steps

1. **[1.0.0_SA_CTO]** Cottonwood staleness cause — diagnosis, premise inverted, not a cron edit.
2. **[1.0.0_SA_CTO]** Ownership of `blackdiamond/cottonwood/bronze/` — two producers, two grammars,
   a vendor pull writing the monolith directly and bypassing the mirror's raw-bytes contract.
3. **[2.0.0_SA_COO]** Track D — mirror row 4 (cottonwood meta-templates) has never run in the window.
4. **[CTO, if wanted]** A *second* anchor sweep at the width CTO stated (register R-1..R-32, MDPF PRDs,
   CANPLAT P1/P2/P3, INF/cot). **My zero does not cover it** — scope it with its own denominator.
5. **[0.7.0_AE_CloudOps]** Available. No applied work pending.

## Compiler Tools

| Tool | Result | Value / gap |
|---|---|---|
| `comp-which "what writes eclipse inflection silver…"` | near-tie, 3 of 75, scores 1.50/1.50 | **Honest no-route** — declared the tie instead of guessing, and routed me to `comp-find`. |
| `comp-find --name "*ingest-mirror*" infra/` | **0 / 7,730** | A measured zero *with its denominator* — the name is a directory, not a file. The printed denominator is the only reason I did not read it as absence. |
| `comp-find "ingest-mirror-cot-daily" infra/` | 3 / 7,730 · SURFACED=1 CONFIG=2 | Band split separated a census *mention* from a trigger-map *declaration* in one call. |
| `comp-find "orion_normalize_as_of"` | 120 / 24,955 · **DEF=1** | `[DEF]` band went straight to the definition out of 120 hits — **this is the call that discharged T-1**. |
| `comp-find "forwardfill_v2"` | 604 / 24,960 · **DEF=19** | Put `cot_bronze_ingest.py:64` on a definition line; named the real forwardfill writer. |
| `comp-find --name "*cot-bd-session*"` | **0 / 7,732** | Same directory-vs-filename trap as above, caught the same way. |
| `comp-find "date=" .../silver-orion/` | 22 / 8 files | Found the partition-date regex — the other half of the T-1 answer. |
| raw `aws` (events, scheduler, s3api, lambda, logs, cloudwatch, cloudtrail, ec2, ssm, iam) | APPLIED reads | Rule 22a — a comp-tool reads DESIRED and cannot tell landed from planned. Every timing claim here is live. |
| `comp-iam` | **not run** | No IAM change and no new boto3 call in a measurement-only pass. Recorded rather than left blank. |

**GAPS FOUND (proposed, not built — per the rule that proposing is legal and implementing is not):**
- **No comp-tool surfaces EventBridge *Scheduler*.** `comp-which` routes schedule questions toward
  rules-shaped views, and the cot trigger is invisible to `list-rules` because it is a different
  service. **The one trigger nobody had attributed was in the service our tooling does not
  enumerate.** CLAUDE.md: *"the comp-tooling is not additive, it is foundational"* ⇒ this is a defect.
  Routed to CTO.
- **CloudTrail cannot attribute S3 writes on `opal-data-assets`** — data-event selectors cover
  `opal-data-bd/` + `opal-data-inf/`, **ReadOnly**; served-key trail is `*/platinum/firm/` only.
  **NOT-MEASURABLE, not absence.** CTO independently confirmed and added: server access logging OFF,
  object Metadata `{}`. The producer was named by **key-grammar partition** instead — no new telemetry
  needed, and the cheaper discriminator was already in the key names.
