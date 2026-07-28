# 0.7.0_AE_CloudOps~C -- INFRA.TOOLS: three registries, one tree, three wrong answers (1830-2020Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, SCRIBE

## Objective

Come up as the `~C` successor lane to the context-exhausted `0.7.0_AE_CloudOps` base, on mission tag
`INFRA.TOOLS` (inherited via the CONTINUITY spawn path -- a mechanical succession, no COO
transcription step). Ground item 1 of the CTO-re-ordered queue: `PIPELINE_MAP` / the Rule-12 class.
**CTO dispatch 201342Z then ruled the order: land the findings BEFORE touching IAM.**

## Startup

Registered `0.7.0_AE_CloudOps~C` (PID 33400); persistent inbox Monitor armed (`blq7dkh1y`,
`TaskOutput -> running`); LD-0290 session serial file written; owned-paths hook already wired;
`.agent_context` set; **zero crons** (LD-0157).

**Orphan check resolved correctly by PID identity, not by inference.** `ps` showed a live
`inbox-watch.sh 0.7.0_AE_CloudOps stream` (pid 2277760). The base serial read **LIVE at PID 29652 --
a different PID with a fresh heartbeat**, i.e. a live peer, not an orphan. Left untouched. This is
the dual-COO false-positive the rule exists to prevent; the discriminator that works is *whose PID*,
which is measurable, never *"am I a fresh session"*, which is inferred.

**PATH denominator: 4 of 92 comp-tools resolve bare.** Used explicit `.tools/` prefixes throughout.

## What I found

Full evidence + line citations in the deliverable:
`org/tier2_senior/0.7.0_AE_CloudOps/deliverables/INFRA_TOOLS_REGISTRY_DIVERGENCE_20260728.md`.

**One defect, stated once:** the mdpf code-deploy surface is described by **three machine-readable
authorities that each restate the layout at their own call site** instead of deriving it from one
declaration. All three are currently wrong, in three different ways.

1. **`mdpf`'s absence from `PIPELINE_MAP` is a DOCUMENTED DECISION** (`pipeline_cli.py:54-60`), not an
   oversight. Recorded reason: the layout is internally inconsistent (`code/<layer>/` **and**
   `code/scripts/<layer>/` both exist), so it cannot live in `file_to_s3_target`'s single-layout
   derivation. **Nobody removed the constraint -- the tree was excused from the gate instead. mdpf has
   a CHECKER and NO DEPLOY PATH.**
2. **`comp-pipescript`'s mdpf override hardcodes FOUR layers against SIX live** (`:1915`, corroborated
   by the `:297`/`:345` regexes and by the sweep's own output). **4 of 28 `.py` invisible**, including
   **Stage-6 `build_dim_model_portfolio.py`** and **both cottonwood scripts**. The tool commissioned
   after MDPF_COUNTS to catch stranded mdpf deploys cannot see them.
2b. **The SAME script reads MATCH or invisible depending on how you spell its name.** `0.4.0_DS`
   logged this tool today as reporting mdpf `0 MATCH/0 STALE/0 MISSING`; my no-arg sweep covered
   mdpf. **Both correct.** Discriminating pair run on one script: a **bare filename** falls through
   to the **bd** tree (`:1785`, intentional backward-compat for bare bd ids per `:1777`) and returns
   `0 MATCH ... 0 UNCOVERED` rc=0 under a `s3://opal-data-bd/` header; the **path form** returns
   `[mdpf:gold] ... MATCH`. It does print `No scripts matched filter`, so it is **not silent** -- but
   the header names the wrong tree, the summary reads all-zeros, and rc=0. **The `uncovered`
   false-clean guard (`:1929`, documented "NEVER silent") reports 0, because the script was excluded
   before the thing that counts exclusions ran.** Two agents, two invocation forms, opposite
   verdicts, same tool, same day.
3. **`EC2_MANIFEST.code_prefix` is one segment too coarse** (`s3://opal-data-mdpf/code/`) -- true but
   non-discriminating, so no consumer can derive a script deploy target from it.
4. **`EC2_MANIFEST` asserts `mdpf-freshness-check-trigger cron(45 16 * * ? *)`. That rule DOES NOT
   EXIST** -- applied plane shows only `mdpf-daily-refresh-trigger`, `ScheduleExpression None`. Third
   independent confirmation the freshness instrument is a document; the new part is that the false
   claim lives in the Rule-8 source of truth, in the `cron_schedule` field.
5. **Rule-12 coverage floor, predicate stated: DENOMINATOR 27.** 4/27 declare `code_prefix`; 11/27
   have a deploy mechanism absent or literally `pre-manifest-era-unknown`. **A floor, NOT a defect
   rate** -- `pre-manifest-era-unknown` is an honest label and the sample was not drawn to support an
   extrapolation.

Plus a live parallel-channel instance: **two `backfill/` prefixes** under one code root, only
`code/scripts/` synced (`--delete`), so `code/backfill/` is an unreachable orphan. This **pins** the
open item -- the ROLLUP still logging "2 partner(s)" is `code/scripts/backfill/`, artifact dated
2026-07-02.

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-pipescript deployed` (no-arg) | all trees | rc=0: 18 MATCH, 3 STALE, 7 MISSING_ON_S3, 0 UNCOVERED | >4 min of ZERO output before completing. Its mdpf coverage is real but 4-of-6 layers -- finding F-2. |
| `comp-grep` | `.tools/`, `pipeline_cli.py` | 0 matches `code/scripts` / 246 files scanned | Trustworthy zero **because it prints its own working set**; and it said `scanned 0 file(s)` for a nonexistent path rather than a bare 0. Retrieval-control done right, worth citing as the in-house good example. |
| `comp-which` rail | 4 raw `aws` inspections | each carried `# rail-checked:` | Justified per call: the routed tool **structurally omits the very layers I was measuring**, and comp-aws/comp-iam model DESIRED, not the applied plane a stale-record question turns on. |
| `comp-iam` | NOT used | n/a | Models `(action)` never `(action, resource)`, fails GREEN. No IAM question in this pass. |

**Gap found (INFRA.TOOLS.O2, the mission's own subject):** `comp-pipescript deployed` has **no
progress contract** -- it emits nothing until complete, so **silence and failure are byte-identical to
the caller.** Not "it breaks"; the narrower and correcter statement.

## My errors this session

1. **Called `comp-pipescript` possibly broken** after 4 minutes of silence, and told CTO so. It
   completed rc=0 and works. **I reasoned from a partial retrieval inside a message warning about
   partial retrievals.** Corrected in ~4 min, unprompted (`184924Z`). The finding survives in
   corrected, narrower form.
2. **Carried my launcher's framing** ("mdpf absent from `safe_deploy_core.py:22-26`") as an omission
   before reading *why* it was absent. The framing was true and incomplete, and the completion changed
   the shape of the work. **Reading the tool that worked AROUND the map, rather than the map, was the
   discriminator** -- the same read-first ordering AE-base bound as a rule at 17:23Z.

## Blockers

**None of mine.** Pending at CTO, evidence-cited: whether the schema fix lands as ONE plan across all
three registries; whether the false `cron_schedule` is corrected now or held until the schedule is
settled.

## Current State

**Findings LANDED (this commit). Nothing patched** -- no registry edited, no tool edited, no apply.
The `assets_gold` gap is deliberately **not** closed by adding a fifth string to a hardcoded list:
that rebuilds the defect with one more member and guarantees the seventh layer repeats it, which is
CTO's own 171123Z ruling applied to its sibling.

## Next Steps

1. **[0.7.0_AE_CloudOps~C]** CTO dispatch item (2): the Stage-6 cottonwood grant on
   `aws_iam_role_policy.mdpf_runner` -- pre-computed by AE-base (`194533Z`). **NEVER#6 commitment
   made explicitly on accept**: finish edit -> apply -> 6 isolated controls in-session, or roll back
   and escalate loud. **C3 (`json/mdpf/global/aggregate-aua-timeseries.json` -> `explicitDeny`) is a
   STOP condition, not a checkbox** -- it proves the runner's reach into the protected serve did not
   widen.
2. **[1.0.0_SA_CTO]** The two architecture calls above.
3. **[0.4.0_DS]** HELD by CTO until the grant lands **and** a demonstrably fresh cottonwood artifact
   exists. Production-before-consumption; not reversible if taken out of order.
