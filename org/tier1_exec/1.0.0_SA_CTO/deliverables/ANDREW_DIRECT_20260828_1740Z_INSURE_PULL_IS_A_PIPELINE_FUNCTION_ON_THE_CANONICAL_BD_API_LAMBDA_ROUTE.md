# ANDREW-DIRECT 2026-08-28 ~17:40Z at the 1.0.0_SA_CTO (laptop base) terminal

**Channel:** Claude Code terminal, base CTO seat, laptop fabric. Received in reply to the /open-calls
card surfaced at tick 12 (ledger row 13, HELD): "ENABLE standing daily vendor egress for the 49F
insurance bronze leg -- one automated pull/day at 11:35Z UTC ... (yes / no)". **Recorded by:**
1.0.0_SA_CTO. **Clock:** the turn after the tick-12 output (17:38Z) -- ~17:40Z.

## VERBATIM

> Yeah this would be a pipeline function, not an agent, we would need to build it in the same bd api
> lambda route that is canonical in data/assets/docs/ or wherver

Second word, ~17:41Z, same terminal, while this record was being written:

> agents have egress to do research and check it out

## Surfaced, not adjudicated (the receiving seat does not widen or narrow)

0. **The second word scopes the AGENT-side egress:** agents' vendor egress is for RESEARCH and
   CHECKING (QA reads, manual exercised captures) -- which is what the 08-25 "Youhave vendor egress"
   word was; the standing daily PRODUCTION pull is not an agent act at all, it is the pipeline's.
   So the card's premise (a widening of the agent grant) dissolves: there is no agent grant to widen;
   the production pull is built and scheduled as a pipeline function on the canonical route.

1. **The daily insurance pull is a PIPELINE FUNCTION, not an agent act.** Read with the card it
   answers: the standing scheduled pull is the intended shape -- production, unattended, on a
   schedule -- and not a human/agent-initiated manual invoke. The card's "yes/no" is answered
   "Yeah" on that framing.
2. **It is built ON THE CANONICAL BD API LAMBDA ROUTE**, the one documented under
   `data/assets/docs/` ("or wherver" -- the doc's location is to be measured, not assumed). The
   insurance leg does not get its own vehicle; it rides the route the estate already names canonical.
3. He did not name a cadence, a time, or a surface set; the card's 11:35Z / four-feed / no
   `/account-api/*` bounds were the card's, and nothing here widens them.

## Measured (same turn, at source — Read-class instruments)

- **The canonical route** (`data/assets/docs/BD_API_DESIGN.md` "Design of Record", :29-51): the
  bd-pipeline 49F session chain — per-target daily EventBridge cron → `bd-49f-session-trigger`
  `{mode: session-refresh, runner: <target>}` → fresh `.bd.identity` mint (or Lever-A live-probe
  skip + direct invoke) → `bd-49f-session-complete` → `{runner-run}` reads the cycle marker →
  `_fire_runner(target)`. Two targets today: `main` (00:00Z) and `fees` (22:20Z MON-FRI) —
  `_RUNNER_BY_TARGET` (session-trigger `:53-57`), invoke policy `bd-49f-session-chain.tf:120-121`,
  fees template `:235-260`.
- **`opal-assets-bd49f-reporting-pull` is NOT the route** — it is the TAXSMA portfolioreporting
  producer (`bd49f_reporting_pull.tf:2`), manual-invoke-only. Act (b) (0.6.0 78494) made the
  insurance leg REACHABLE inside it; that is the part that ports.
- **Why not inside `bd-49f-runner`:** the runner is firm-bound to `opal-data-bd` ONLY (its role
  writes only that bucket, `bd-49f-interim.tf:229-247`; `lambda_function.py:12-20,52-56`), and the
  insurance mint is ruled at `opal-data-assets/blackdiamond/49financial/` (PRD s.11 Ruling 1).
  Widening the canonical runner to a second bucket is the wrong side of that invariant.
- **The one gap:** `_fire_runner` invokes with an EMPTY payload (`:205-212`); the reporting-pull's
  dispatch needs `{"leg":"insurance"}`. A per-target payload map in the session-trigger closes it
  without touching main/fees.

## RULING (1.0.0_SA_CTO, ledger row 14 — the operative text lives there)

INSURE = the canonical chain's **third runner target** `insurance` = the reporting-pull Lambda
invoked with `{"leg":"insurance"}`: new cron `bd-49f-insurance-session-daily` at `cron(35 4 * * ? *)`
UTC daily (staggered clear of fees/main/cot by ≥2h35m), marker vocabulary + `_PAYLOAD_BY_TARGET`
in the session-trigger, the reporting-pull ARN added to the session-trigger's invoke policy (CTO
plan-gate on that IAM diff), `INSURANCE_EGRESS` ON by his word, both `.tf` comments amended in the
same commits. **Act (c) as designed — a standalone Scheduler entry + a new scheduler role on the
reporting-pull — is CANCELLED**; COO's (c) IAM ruling 78496 is moot and the CTO plan-gate on that
role is withdrawn. The 08-25 agent grant stays research/QA. Acceptance = the first chain fire with
`runner=insurance` (both Lambdas' own logs + head-object at the grammar; negative control = main's
run that day did not enter insurance). First fire 2026-08-29T04:35Z if the wiring lands today.

## Acts taken on this word (same turn)

- Locate the canonical BD API Lambda route doc under `data/assets/docs/` and measure whether
  `opal-assets-bd49f-reporting-pull` (the Lambda INS-a-5 / TO-A3-AE is building on) IS that route.
- Rule INS-a-5's vehicle against the measured answer; broadcast to `2.0.0_SA_COO` (issuer),
  `0.6.0_AE_PartnerETL` (executor), `0.0.0_AB_MSTR` -- same turn, push state stated.
- Ledger row 13 (HELD) closes on this word; the scheduled half of AC4 becomes reachable.
