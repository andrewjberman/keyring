# WSE_COTMDL -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-25 on the first surfaced item for this project. Executing seats surface; the CVO files. Items are schema-validated against `../schemas/investigation_item.schema.json`.

```json
[
 {
  "id": "WSE_COTMDL-S1",
  "surfaced_by": "0.7.0_AE_CloudOps~H -- APPLIED AND LANDED THE AUTHORISED WORK FIRST so the surfacing is not a hold; re-derived the TO's own headline number from today's artifacts rather than accepting it",
  "surfaced_at": "2026-08-25T10:05Z",
  "one_line": "The TO's and decomp's '30 of 64' COUNTS TWO DIFFERENT POPULATIONS -- 30 is detail files landed, of which only 22 are ON the roster and 8 are transitive children NOT on it. TRUE ROSTER COVERAGE IS 22 OF 64, so the gap is 42 models and not 34; and AC3 asks for exactly the comparison the TO's face number cannot support.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "re-derived from today's own 06:00Z artifacts, not from the TO: roster (rebalancer_models page_000 totalResultCount) = 64; detail files landed = 30; ON the roster = 22; NOT on roster (transitive children) = 8",
    "_is_opal seeds on roster = 22, ALL 22 pulled -- and 22 + 8 = 30 RECONCILES EXACTLY",
    "CONTROLS RUN BOTH WAYS: casefold control (8 still absent), positive control (a known roster id resolves), negative control (bogus id -> False)",
    "the authorised change is APPLIED and LANDED before surfacing: MODEL_DETAIL_SCOPE=all live per get-function-configuration, LastModified 2026-08-25T09:50:45+0000, ledger cotmdl-model-detail-scope-all CLOSED, 3 legs proven"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "THE ISSUER of WSE_COTMDL's TO (routing per Rule 27; 1.0.0_SA_CTO / 2.0.0_SA_COO to confirm which holds it) -- the remedy is a CODE change and the surfacing seat's TO explicitly is not one. ⛔ ARMED WITH A NAMED MATERIALISATION: 2026-08-26T06:00Z, the next scheduled run.",
  "notes": "⛔ THE DEFECT IS WORSE THAN THE TO STATES, WHICH STRENGTHENS THE AUTHORISATION RATHER THAN WEAKENING IT -- the surfacing seat says so explicitly, against the natural incentive to let a favourable-looking number stand. The gap is 42, not 34. || WHY IT IS A GRAIN MISMATCH AND NOT AN ARITHMETIC ERROR: '30' counts DETAIL FILES LANDED and '64' counts ROSTER MODELS. Both numbers are true of their own population and the RATIO IS TRUE OF NEITHER. Rule 24(ii), same-grain, violated across the numerator and denominator of a single quoted fraction -- and a fraction is exactly the shape that hides it, because it presents as one measurement. || AND AC3 ASKS FOR THE COMPARISON THE FACE NUMBER CANNOT SUPPORT, so the criterion is currently discharged by quoting a figure that does not mean what the criterion needs. That is the acceptance-surface class this fabric has hit repeatedly: a criterion satisfiable by a true statement about the wrong population. || SECOND LIMB, SAME ITEM: scope=all ALSO DROPS 8 SUB-MODELS -- the transitive children that are not on the roster. So the two populations are not merely mis-ratioed, they are each incomplete in a different direction. || METHOD NOTE WORTH KEEPING: the surfacing seat LANDED THE AUTHORISED WORK FIRST AND THEN SURFACED, so no work was held while the finding was written. Rule 27 permits surfacing without holding, and this is the specimen of doing both correctly in one turn."
 },
 {
  "id": "WSE_COTMDL-S2",
  "project": "WSE_COTMDL",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps",
  "surfaced_at": "2026-09-11T00:52Z",
  "one_line": "cot-rebalancer-runner HAS FAILED 100% OF ITS INVOCATIONS FOR ELEVEN CONSECUTIVE DAYS and nothing reports it: its own fail-closed count-reconcile self-gate refuses the pull because strategy 'Core | Satellite 60' has 14 accounts on the roster and the pull observes 13, so rebalancer_model_detail/ has been stale since 2026-08-28 while every other Cottonwood bronze feed is fresh today.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "CloudWatch AWS/Lambda, FunctionName=cot-rebalancer-runner, period 86400 over 12 days: Invocations EQUAL Errors on every day from 2026-08-31 through 2026-09-10 (3 per day = 1 fire + 2 async retries; 4 per day on two days). 2026-08-30 reads 1 invocation and 0 errors, so the series HAS a clean day and the instrument can distinguish pass from fail -- the all-error run is a measurement, not a blind metric.",
    "the actual error text, read from the logs rather than inferred: 'RuntimeError: COUNT-RECONCILE SELF-GATE FAILED (Sec.5, fail-closed) -- the account pull does not reproduce the roster assignment counts (wrong/truncated pull). mismatches=[{\"strategy\": \"Core | Satellite 60\", \"roster\": 14, \"observed\": 13}] orphans=[]' at lambda_function.py:344 via :378 via :424, on the 2026-09-10T06:00:42Z, 06:01:48Z and 06:03:54Z invocations",
    "s3api list-objects-v2 on opal-data-assets prefix blackdiamond/cottonwood/bronze/: rebalancer_model_detail/ newest object is 2026-08-28T06:00:58Z, while holdings, allocations, transactions, realized, unrealized and account_attributes were ALL written 2026-09-10T11:45Z. So this is ONE dataset stale, NOT a firm-wide Cottonwood outage, and the scope is stated narrowly on purpose.",
    "rebalancer_models/2026-09-10/page_000.json EXISTS at 2026-09-10T06:03:56Z -- the runner reaches the roster write and then dies on the gate, which is why the failure leaves a partial footprint that looks like progress",
    "CLAUDE.md NEVER#4 (resolve the trading calendar before calling anything stale) is SATISFIED WITHOUT LEANING ON FILE DATES: the oracle here is eleven days of 100%-error invocations, not an object's age. A weekend or holiday cannot produce a daily ERROR metric.",
    "WS-5's own infra is APPLIED and is NOT the fault: events describe-rule cot-rebalancer-runner-daily returns State=ENABLED, ScheduleExpression=cron(0 6 * * ? *); lambda get-function-configuration returns State=Active, LastModified 2026-08-25T10:38:32Z. The function fires, authenticates and pulls -- the refusal is downstream of everything this seat owns."
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.6.2_AE_PartnerETL (WS-1, the producer and roster owner) with 2.0.0_SA_COO as issuer routing it -- the remedy is the PULL or the ROSTER, both WS-1's code, and WS-5's grant is infra only. ⛔ ARMED WITH A NAMED MATERIALISATION: the next scheduled run, 2026-09-11T06:00Z, will fail the same way and make it twelve days. ⚠ 0.6.2_AE_PartnerETL IS NOT LIVE at surfacing time, so this row is the carrier and no broker message can substitute for it.",
  "spec_asserts": "WSE_COTMDL.WS5 reads <status>pending</status>, describes its own work as 'infra scaffolding' to 'stand up' a scoped role and EventBridge schedule, and names the function as opal-assets-bd-rebalancer-daily-pull with dependencies 'ready'.",
  "world_is": "The infra is already BUILT AND APPLIED -- by this same seat on 2026-07-21 at ab268cb900 and b2add5091b -- the function was RENAMED to cot-rebalancer-runner in that same reconcile so the TO names a function that no longer exists, and the live schedule it describes as something to stand up has been ENABLED and firing into a 100% failure for eleven days. The order's status field and its text are both wrong, in opposite directions.",
  "notes": "HOW IT WAS FOUND: while grounding WS-5, which is this seat's OWN task order, before writing anything. The order reads <status>pending</status> and describes infra to stand up, so the live plane was measured first -- which is the only reason this was found at all. No work was held to write this row. || METHOD NOTE ON THIS FIELD: `surfaced_by` carries the BARE SERIAL and nothing else, because .tools/surprise-row-gate.py's FOREIGN-ROW SWEEP compares that field to the committing serial and a trailing prose clause makes it read as a foreign row. It refused this row once for exactly that, with the serial sitting in plain sight at the front of the string. Pre-existing rows on this channel carry prose there and were never graded -- the gate grades NEW rows only -- so the existing rows are not evidence that prose is allowed. The prose moved here rather than being forced through with the audited override. || ⛔ THE THING THAT MAKES THIS WORTH A BLOCKING ROW IS NOT THE FAILURE, IT IS THE SILENCE. Eleven days of a daily scheduled job failing every fire, and the only reason anyone knows is that a seat happened to ground its own task order before building. CLAUDE.md's standing alarm moratorium means there is no monitor here BY DESIGN, so the detection path for this class is a human or a seat looking -- and for eleven days nobody did. This row is NOT a request to build a monitor; the moratorium is Andrew's and stands. It is a request that the remedy owner know. || THE SELF-GATE IS WORKING CORRECTLY AND MUST NOT BE 'FIXED' BY LOOSENING IT. Sec.5 fail-closed is doing exactly its job: it caught a truncated pull and refused to write it to bronze. A 14-vs-13 count mismatch written through would have put a silently incomplete rebalancer dataset into the served chain. The defect is UPSTREAM -- either the pull drops one account in 'Core | Satellite 60', or the roster claims an account the pull cannot legitimately see. Whoever takes it should establish WHICH before touching either, because those two causes have opposite remedies and the gate cannot tell them apart. || WHY 2026-08-31 DID NOT CATCH IT, which is its own small lesson: 1.0.0_SA_CTO DID see this runner fail at 06:00Z on 2026-08-31 and asked this seat to measure the cot session refresh cadence, hypothesising a TIMING cause (fires 06:00Z, session refreshes ~11:33Z). That ask was then STOOD DOWN two hours later as belonging to 0.6.2's TF. Both messages sat UNREAD IN THIS SEAT'S INBOX FOR TEN DAYS across the 2026-09-05 crash. The stand-down was correct about ownership and the timing hypothesis was WRONG about cause -- the logs say count-reconcile, not session -- so a correct routing decision and an incorrect cause theory together produced ten days of nobody looking. || THE OTHER FEEDS BEING FRESH IS THE LOAD-BEARING CONTROL and the reason this row does not claim a Cottonwood outage: six sibling bronze datasets landed today at 11:45Z from a different producer. Quoting '13 days stale' without that control would have manufactured a far larger defect than the real one. || SEPARATE AND SMALLER, recorded so it is not lost: the schedule is still the PLACEHOLDER cron(0 6) that the TF comment flags as awaiting chain-timing confirm, and 06:00Z is 5.75 h before the sibling feeds land. That is a real open question about whether 06:00Z is the right hour at all, but it is NOT this failure's cause and 1.0.0_SA_CTO has already ruled the cadence belongs to 0.6.2's cot-pipeline TF, so it is named here and not chased."
 }
]
```
