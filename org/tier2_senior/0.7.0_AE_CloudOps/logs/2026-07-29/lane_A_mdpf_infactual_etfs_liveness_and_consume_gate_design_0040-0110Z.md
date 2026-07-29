# ~A lane: MDPF_INFACTUAL.001 AE half -- ETFS_SETUP liveness audit + consume-gate design (0040-0110Z)

**archetype:** MIXED (VALIDATE + DIAGNOSE + IMPLEMENT-design)
**Serial:** `0.7.0_AE_CloudOps~A` (fresh spawn, Andrew-launched; charter COO 003956Z, superseded-in-part 004830Z, ruling 010220Z)
**Session:** a508f867 · watcher Monitor `b0ivt5egc` · registered PID 34668

## What happened

1. **Startup:** /watcher (registered, Monitor armed + TaskOutput-confirmed, no orphan for my serial --
   serial read NOT REGISTERED before arming, per the PID-identity discriminator), LD-0290 serial file,
   A.2 audit-archive rc=0/0 findings, A.3 PATH 93/93, owned-paths hook already wired, agent context set.
2. **Charter (COO 003956Z):** AE counterpart to DS~A on MDPF_INFACTUAL.001 -- I own trigger + IAM +
   chain wiring; DS~A owns the script. Deploy freeze live (CTO 234106Z): design-and-verify only. ACKed
   with division-of-labour readback 004200Z.
3. **Deliverable change (COO 004830Z):** liveness audit of the three ETFS_SETUP per-partner ownership
   producers FIRST -- DS~A's commit held on it. Findings (all live-primitive-grounded, full evidence in
   MCP 010157Z to COO / 010217Z CC CTO):
   - `bd-49f-etf-ownership-daily` DEAD both halves (zero rules by target-ARN, no resource policy);
     function exists (modified 06-25); `daily/49financial/` stops at vintage 07-06, tail written in ONE
     batch 07-14T05:12Z == last log event -> manual one-shot, never scheduled. Live prefix is
     `49financial/`, NOT the docs' `49f/` (enumerated, not constructed).
   - `cot-etf-ownership-daily` ALIVE: cron(30 10 * * ? *) ENABLED + coupled resource policy; last fire
     07-28T10:30:29Z; artifact 07-28 (vintage 07-24 = source lag, contract working).
   - `inf-etf-ownership-daily` ALIVE + T-0 fresh (artifact 07-28 @15:04Z) but SENTINEL-ONLY (one rule:
     gold-complete event pattern; no schedule) -> NEVER#4 defect, reported as such.
   - MDPF runner role CANNOT read `opal-data-etfs/daily/*`: simulate implicitDeny on the exact key
     [single-arn], positive control silver/* allowed + negative control opal-data-cot implicitDeny as
     SEPARATE invocations; no bucket policy on the bucket.
   - Fence hazard (charter item): CLOSED for the runner path -- `mdpf/feeds/` resolves live to
     `opal-data-mdpf`; runner role attachment census = [AmazonSSMManagedInstanceCore] + inline
     `mdpf-runner-scoped`; the fan-in fence is NOT attached; PutObject on the exact inflection output
     key simulate-allowed + 49F sibling writes daily (07-28 20:30Z) as behavioral proof.
   - En route, the ORIGINAL charter question: 49F sibling fires as Stage-1 of the DEPLOYED
     mdpf-daily-dispatch.sh (read from live S3, :282), SSM-dispatched by mdpf-daily-trigger; chain is
     EVENT-ONLY today (mdpf-daily-refresh-trigger ENABLED, fired 5x thru 07-27);
     **mdpf-scheduled-floor cron(0 20) is TF-DECLARED but NOT LANDED** (describe-rule
     ResourceNotFoundException) -- in the freeze-gated 4c set. Not mine; not touched.
4. **COO ruled CONSUME (010220Z)** -- my sentinel-only finding became the hard blocking gate. Designed
   the unblock, committed **@b5e7e22730** (deliverables/MDPF_INFACTUAL_001_AE_trigger_iam_design_20260729.md):
   Design A = `inf-etf-ownership-scheduled-floor` cron(0 19 * * ? *) daily-incl-weekends, 3 TF
   resources, ZERO code change (handler measured floor-compatible at :96/:13); Design B = runner
   GetObject `daily/inflection/*` + list-prefix extension. Deliberately NOT landed as infra/ edits
   (4c early-activation hazard). Routed to COO 010732Z + CTO 010742Z with 4 open calls (floor time,
   grant narrowness, DLQ parity, apply-window owner).
5. **Seam with DS~A:** confirmed frozen both directions (their 010200Z: output contract unchanged in
   both branches; account_count keying delta 557-559 vs 581-584 disclosed while values agree to the
   cent). No duplication -- they stopped at "liveness is AE~A's read".

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-grep "partner_held_etf" | 60+ hits, 10+ files | Located both feeders + runbook + handoff; denominator printed by tool |
| comp-which (trigger question) | near-tie routed to comp-trigger | Rail honored; picked comp-trigger by description |
| pipescript mdpf | 2 threads, 43d-old snapshot | VINTAGE WARNING read; used for localization only, every load-bearing key re-verified live |
| comp-trigger mdpf | 142 rules + 10 schedules scanned | Found refresh-trigger ENABLED/fired-5x + publisher cron(15 16); did NOT list mdpf-scheduled-floor -> live describe-rule confirmed NOT LANDED |
| comp-trigger etf-ownership | same denominator | cot cron ENABLED fired-7x; inf event-pattern fired-5x; bd ABSENT -- then per-producer live verify (rules-by-target + get-policy) because a name-substring scan is not a per-target census |

Raw `aws` inspections carried inline `# rail-checked:` markers (landed-vs-planned + per-target grain
comp-tools do not model); simulates per Rule 22a (one --resource-arns per call, controls separate,
5 invocations). comp-iam not used for the (action,resource) questions -- it fails GREEN there.

## Open / waiting

- CTO+COO: ratify floor time 19:00Z, grant narrowness, DLQ-parity call, **apply-window owner** (base
  AE holds the MDPF lane; I am chartered separate).
- Freeze lifts on 07-29's three unattended fires (base AE/CTO lane, not mine).
- Nothing applied, deployed, or activated this session. Commit-no-push throughout.
