# /self-drive D2 & D3 — tick 13 (2026-08-28 17:51Z) — state: ARMED

Covers tick 13 (tick 12 logged @b1f5b48b9a). Cron bde882a4 (:07/:37; this tick ran on idle after
the 17:40Z word was executed). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA:
an Andrew-direct word answered the tick-12 card and moved a deploy vehicle; row 14 landed; the base
CVO is live again.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 28
(D2 21, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342, 0 claimed-not-member.

## Calls (§1-2)

**Zero.** The tick-12 RESERVED card (row 13) was ANSWERED by Andrew-direct at this terminal 17:40Z
(COO wrote row 13 `consumed` = ANSWERED). GATE A on PERFRP TO-R1-AE remains not-a-card (condition
half-unmet). `3.0.0_SA_CVO` (base) is LIVE (PID 15352, in startup) — the held reserved-claim review
is moot (answered by the sovereign), but the loop's round-bank classes (seven, ticks 10-12) and the
INS-a-5 decomp cert queue are routed to that seat this tick.

## Andrew-direct 17:40Z / 17:41Z — recorded, ruled, executing

VERBATIM (record `deliverables/ANDREW_DIRECT_20260828_1740Z_INSURE_PULL_IS_A_PIPELINE_FUNCTION_ON_THE_CANONICAL_BD_API_LAMBDA_ROUTE.md` @11d67876eb):
*"Yeah this would be a pipeline function, not an agent, we would need to build it in the same bd api
lambda route that is canonical in data/assets/docs/ or wherver"* · *"agents have egress to do
research and check it out"*.

**Row 14 (VERDICT, @11d67876eb) — the vehicle ruling, measured at source before ruling:** the
canonical route is the bd-pipeline 49F session chain (`BD_API_DESIGN.md` :29-51): per-target daily
cron → `bd-49f-session-trigger` {session-refresh, runner} → fresh cookie → `session-complete` →
`runner-run` → `_fire_runner(target)`; two targets today (`main` 00:00Z, `fees` 22:20Z). INSURE
becomes the **third runner target** `insurance` = `opal-assets-bd49f-reporting-pull` invoked with
`{"leg":"insurance"}`: cron `bd-49f-insurance-session-daily` 04:35Z (staggered ≥2h35m clear of
fees/main/cot), `_RUNNER_BY_TARGET` + marker vocab + a per-target payload map in the session-trigger
(main/fees keep the empty payload), the reporting-pull ARN added to the chain's invoke policy (**CTO
plan-gate** on that IAM diff), `INSURANCE_EGRESS` ON by his word. **Act (c) as designed — standalone
Scheduler + new scheduler role on the reporting-pull — CANCELLED**; COO's 78496 IAM ruling moot;
this seat's plan-gate on that role withdrawn. Not inside `bd-49f-runner`: it is firm-bound to
`opal-data-bd` only and the insurance mint is ruled at `opal-data-assets/…/49financial/`. The 08-25
agent grant stays research/QA per his second word. Acceptance = the first chain fire with
`runner=insurance` (both Lambdas' own logs + head-object; negative control = main's run did not
enter insurance); first fire 2026-08-29T04:35Z if the wiring lands today.

**Executed downstream (COO summary 17:5xZ + 0.6.0 78510):** TO-A3-AE superseded on the face
@fa5a2759fa; (c) HELD at 0.6.0, measured UNTOUCHED on DESIRED/APPLIED/RUNTIME (0 of 18 schedules
target the function); the one bounded AC4-QA invoke ran 17:43:19Z — **before** either hold, under
COO's standing 78445 — and validated the porting module against the real vendor: pages=2 rows=77
attested_total=77 measured-complete, reporting branch NOT run, head-object on both pages at the
grammar with attested-total/page metadata. The 08-27 page-short defect is closed against the vendor.
`0.7.0_AE_CloudOps~G` no longer live (COO released it) → the chain-wiring half needs a fresh
AE_CloudOps lane via COO's `/mstr-spawn`; 0.6.0 keeps the reporting-pull side. `0.4.0_DS_ClientPlatform~R`
RELEASED 17:48Z (AC1 PASS, silver-stage design + digest prep on the record).

## Other deltas absorbed

- **DE~D 78479/78491:** AC2 PASS @2813c8d8c4; Manage Table MOUNTED + PUBLISHED (origin/DEV 9957410e,
  CI SUCCESS); caller census delivered — the two zeros took OPPOSITE verdicts (PerfrpTable = real gap;
  PerfrpPeriodUnavailable = dead code, its behaviour served inline) and the census instrument's first
  run was wrong (excluding the defining module hid intra-module composition; recorded, not just
  fixed). AC8 re-read: reason retired, status HELD — the unmet clause is a **declared state no
  producer can emit** (`KNOWN-NOT-HELD`, 2 of 4 enum members reachable; MECE ≠ reachable). 7 artifact
  rows carried a push claim that had gone FALSE after the integrator pushed — corrected.
- **COO 78474 / DS~R 78485:** unmanifested-partition fork RULED (default SKIP-UNVERIFIABLE;
  `--backfill-manifest` once at the stage build's first act with a parquet byte-compare); first-mint
  = step 0 of the stage build (2 imports missing at the prefix); `safe-deploy.sh` header drift →
  obligations row 7 item (i).
- **MSTR:** SITEZ reconcile STOPPED at LEG-OUTSTANDING on Andrew's word; base CTO/COO not to be
  routed anything outside D2 & D3 (78428 verbatim, MSTR's record).

## Round-bank classes (seven, ticks 10-13) — routed to `3.0.0_SA_CVO` this tick

1. Member-list acceptance accepted PRESENCE where REACHABILITY from the configured entrypoint was
   the criterion. 2. Deployed object moved under a peer's measured hash. 3. An EXERCISED arm went
   stale when its subject moved. 4. A control read on ONE plane concluded about the gate; the relay
   inherited the grounding. 5. A relayed grant citation was wrong about its SCOPE. 6. A completeness
   signal measured then discarded by the producer. 7. Idempotence keyed on an output's existence
   proves only that something was converted. (+ DE~D's: a declared enum state no producer can emit;
   a push-state claim aging inside an artifact nobody re-reads.)

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope (row 13 answered).

state: ARMED · push state of this log: LOCAL (origin/CLOUD @f814126b59, ls-remote read 17:51Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · `get_live_agents` (14 live;
  CVO base LIVE) · ledger read (rows 13-14 consumption) · `git ls-remote`. The vehicle ruling's
  instruments are in row 14's grounding (Read-class on the design doc, the session-trigger source
  and the bd-pipeline `.tf`s; no `aws` inspection at this seat — the live handler binding and the
  schedule census were 0.6.0's and COO's measurements, cited).
