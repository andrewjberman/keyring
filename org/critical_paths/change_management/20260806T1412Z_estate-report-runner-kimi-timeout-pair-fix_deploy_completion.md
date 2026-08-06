# Deploy-completion ledger: estate-report-runner KIMI_TIMEOUT PARAMETER-PAIR FIX (c176c3d9f)

**Opened:** 2026-08-06T14:12Z, AT DEPLOY START (not retroactive)
**Status: CLOSED 2026-08-06T14:22:18Z -- DEPLOYED, THEN ROLLED BACK ON AN ANDREW VETO. NOT LIVE.**

## ⛔ OUTCOME: DEPLOYED 14:12:43Z, VETOED, ROLLED BACK 14:22:18Z. NOTHING FROM THIS LEDGER IS LIVE.

**ANDREW-DIRECT at the CVO terminal ~1414Z, VERBATIM: *"No bridge, move to the subdivision now."***
Preceded by, verbatim: *"I thought we already established that this should be broken up into multiple
calls, where I would imagine that each call would have its prompt in a step function manner."*

**The timing, stated plainly because it is the whole lesson:** I deployed at **14:12:43Z**; CVO's
relay of the veto landed at **14:14:07Z** -- **84 seconds later.** I did not deploy in defiance of a
known ruling; I deployed into a window where the ruling existed and had not reached me. That is not
exoneration, it is the mechanism: **I held a sovereign approval (*"I approve on COOs behalf"*, ~1410Z)
and treated it as settling the substance, when it only settled WHO GATES. Andrew's later, more
specific word supersedes on substance -- latest and most restrictive binds.**

**AND THE DEEPER MISS IS MINE AND CVO's TOGETHER: we spent an hour hardening the call the approved
spec already retires.** SPEC @58505c291 subdivides this into Call 0 (deterministic) -> Call 1 NARRATE
-> Calls 2-5 DETECT -> Calls 6..N AUTHOR, each carrying only what its job needs. **A monolithic
72,344-char prompt is the thing that design eliminates, and we built a bigger socket for it.** The
root-cause analysis was correct and the remedy was aimed at an architecture already scheduled for
replacement. *Being right about the mechanism is not the same as being right about what to do.*

**Rollback executed and verified BOTH WAYS:**
`copy-object` from DEP3 VersionId `ybV1tlEZ4I3u9ZSIFljVK8_Zr8tK6RZ7` -> new VersionId
`zwAf4aAXNXV7uS9Nsp4mpBga5EtUYS.I`, ETag back to `"13b790058b8ed3ce4360dda654ee99df"` / 75,026 B.
POSITIVE: `KIMI_TIMEOUT_SECONDS = 300` / `KIMI_ATTEMPTS = 2` restored at :77-78.
NEGATIVE CONTROL: bridge markers `KIMI_RETRY_ON_TIMEOUT` / `KIMI_CALL` / `ai_call` all **0** on the
served bytes. `py_compile` PASS on the rolled-back served artifact.
**Live state == DEP3 == what ran this morning. The 2026-08-07 13:00Z fire will run DEP3 and will
very likely time out again; that AI-dark cost is accepted as the consequence of ruling out the
bridge, and is stated here so it is not discovered as a surprise.**

## ⚠ A CLAIM IN THE VETOED COMMIT IS TOO STRONG AND MUST NOT PROPAGATE

Andrew authorised the small-prompt probe; CVO ran it. Same endpoint, same model, same
`max_tokens=32000`, same 300s ceiling, 31-char prompt: **RETURNED in 3.4s**, HTTP 200,
finish_reason `stop`, prompt_tokens 92, completion_tokens 51, **reasoning_tokens 35**.
Two consequences:
1. **The endpoint is HEALTHY** -- vendor degradation is closed as a standing alternative, not merely
   made unlikely. (Honest limit: measured ~13:55Z, not 13:02Z; cannot exclude a transient at fire time.)
2. **c176c3d9f's in-source line *"300s could never have accommodated 32000"* is FALSIFIED** -- that
   exact pair returned in 3.4s. **`max_tokens` is a CEILING, not a TARGET.** The true and narrower
   statement: **300s cannot accommodate the generation that a 72k-char prompt INDUCES.** The strong
   form must not reach the subdivision's rationale: it would justify sizing each call's timeout
   against `max_tokens` in the abstract, when the thing to size against is the generation each call's
   own prompt induces -- which is the entire point of the step function.
3. **First real token data, and it bears on per-call sizing: 35 of 51 completion tokens were
   REASONING for a task whose answer was "OK" (~69% overhead on a trivial request).** Subdivided
   calls need genuine output headroom even when their job is small; sizing them tight because "this
   call only writes one field" would starve them the way 4000 starved the monolith.

## What survives

**(a) timeout 300 -> 1800 + terminal-no-retry: VETOED. Dies here. Do not resurrect.**
**(b) the KIMI_CALL/KIMI_ATTEMPT telemetry reaching the ARTIFACT and MANIFEST: ARCHITECTURE-
INDEPENDENT and carries FORWARD into the subdivision build** (CVO recommendation, adopted) -- N
subdivided calls need per-call elapsed/size/outcome MORE than the monolith did, because a failure in
call 4 of 7 has to be locatable from the manifest. Not deployed standalone.

---

*(Original pre-veto ledger body retained below verbatim -- it is the record of what was done and
verified, not a claim about live state.)*
**Authority:** **ANDREW-DIRECT, sovereign, 2026-08-06 ~1410Z at the CTO~B terminal. VERBATIM:**
*"I approve on COOs behalf, they should not be gating this."*
**DEP4** of this key. Siblings: `20260805T1456Z_…corpus-vintage` (DEP1, a254104b34) ·
`20260805T1645Z_…corpus-delivery` (DEP2, 9a1856bc03) ·
`20260805T2312Z_…budget-inversion` (DEP3, 1d95d25b1e).

## Authority handling -- and the gate I deliberately did NOT manufacture

I had requested COO GO (@140727Z) + CVO FRESH acceptance (@140821Z). Andrew's word discharges the
COO leg directly and rules that COO should not be gating this class.

**CVO acceptance was IN FLIGHT and I did NOT hold on it.** That is a deliberate call against the
standing law: converting a sovereign approval into "well, the OTHER reviewer still has to clear it"
would be an inferred gate of exactly the class CLAUDE.md names -- *"just because i tell an agent to
stop does not mean you of your own accord create a gate, this is why the kimi pipeline did not get
finished, because it was held up on a gate you interpreted without my approval."* **That rule was
written about THIS pipeline.** Andrew said ship; holding for a second reviewer I myself proposed
would be me re-imposing the gate he just removed, one seat over.
CVO's acceptance therefore lands as VERIFICATION-AFTER, not a precondition. Rollback is same-window
and all prior versions are retained, so the cost of being wrong is one `put-object`.

## The act

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`. Transient box,
systemd oneshot pulls on boot -> re-uploading IS the deploy (`EC2_MANIFEST.json:571`).

| | value |
|---|---|
| deployed vintage | `c176c3d9f` (CTO~B, 2026-08-06) |
| tree-vs-vintage | `git diff c176c3d9f` on the file = 0 bytes; pin re-derived at deploy time, not inherited |
| Phase-2 local md5 | `590258a03396fd1429d4f516a0183d42` |
| local bytes | 83,688 |
| PRE | ETag `"13b790058b8ed3ce4360dda654ee99df"` / 75,026 B / 2026-08-05T23:12:53Z / VersionId `ybV1tlEZ4I3u9ZSIFljVK8_Zr8tK6RZ7` (= DEP3, unchanged -- nobody deployed in between) |
| Phase-3 head-object ETag | *(filled at L4)* |
| POST | *(filled at L4)* |
| read-back | *(filled at L5)* |
| rollback | DEP3 VersionId `ybV1tlEZ4I3u9ZSIFljVK8_Zr8tK6RZ7`; all prior versions retained |

## What it changes

**KIMI_TIMEOUT root-caused as a PARAMETER-PAIR inconsistency armed since 08-04 -- not a too-small
timeout.** `19ebb5f44d` derived timeout=300 when `max_tokens` was 4000; `95e1f0283f` (the 08-04
KIMI_EMPTY fix) raised `max_tokens` to 32000 and touched `KIMI_TIMEOUT_SECONDS`/`KIMI_ATTEMPTS`
**zero times** (verified on the diff). Since 08-04 the model was permitted to generate 32,000 tokens
while the socket waited 300s -- unsatisfiable. It did not bite until 08-06 because **the
corpus-delivery defect was accidentally protecting it**: a thin prompt gave the model little to say.
DEP3 removed that protection and the latent fault surfaced on its first fire. **DEP3 did not create
the fault; it revealed one already armed.**

1. `KIMI_MAX_TOKENS` / `KIMI_TIMEOUT_SECONDS` / `KIMI_ATTEMPTS` declared as ONE co-located coupled
   set (they lived 970 lines apart -- the structural reason nobody re-derived the pair).
2. Timeout 300 -> 1800, labelled in source as a **MEASUREMENT WINDOW, not a derived answer**.
   Worst case ~31 min against the 90-min dead-man ceiling.
3. Timeout is **TERMINAL** (`KIMI_RETRY_ON_TIMEOUT=False`); transient classes still retry.
4. **Timeout path INSTRUMENTED** -- CVO's coverage finding. `KIMI_TOKENS` reads `usage` off the
   response body, so it is response-conditional and goes dark on a timeout: the instrument built to
   replace judgement with a measurement was silent in exactly the failure where the judgement was
   contested. New `KIMI_CALL`/`KIMI_ATTEMPT` emission reaches the report JSON, the MANIFEST
   (`ai_call`) and the human-facing MD.

## Exercise (pre-deploy, build-time correctness)

`py_compile` PASS · `ruff` PASS (py39) · non-ASCII **0**.
Local battery, `urlopen` monkeypatched (**NO vendor egress**): **25/25**. Telemetry survives a
timeout; exactly ONE attempt on timeout; transient errors still spend BOTH (suppression not
over-broad); success path intact with usage folded in. **MUTANT CONTROL**: flipping
`KIMI_RETRY_ON_TIMEOUT` back to True takes attempts 1 -> 2, so the terminal-timeout check is
discriminating rather than vacuously green.

## Scope honesty

**Deployed != exercised.** Box is transient and stopped; nothing has RUN this. First execution is the
**2026-08-07 13:00Z** boot.
**Residual, NAMED, not waived:** zero token counts for 08-06 (a timeout returns no `usage` -- that IS
the defect being fixed). Prefill-vs-generation remains **INFERRED**. The discriminating control (a
small-prompt probe at the same endpoint) is **VENDOR EGRESS, no per-use word, UNRUN and staying
unrun**. Claim status: **STRONGLY INDICATED BY A CONTROLLED COMPARISON** (08-05 positive control:
nuggets 0->153 while git paths went 357->217 and every other budget went down). Reserved words
deliberately not used.
1800s may still truncate if the model wants all 32,000 -- that lands as `KIMI_LENGTH_STARVED`, loud,
discriminated, fully instrumented. Acceptable next state; a silent one would not be.
**Bound on value (CVO):** the corpus is STALE (newest source 07-31, before the window opened) until
B6 lands. Delivering 153 nuggets makes the model SEE them; it does not make them CURRENT.
No alert/alarm/SNS/SES/checker/monitor built.

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | authority | Andrew-direct verbatim above (supersedes the COO leg); CVO = verification-after, explicitly not a gate | DONE |
| L2 | pre-state | head-object = DEP3 artifact, unchanged | DONE |
| L3 | PutObject | one call, no `--quiet` | *pending* |
| L4 | ETag verify | ETag == Phase-2 md5, size/LastModified advance | *pending* |
| L5 | read-back | get-object -> md5 match, `cmp` identical, py_compile PASS, non-ASCII 0 | *pending* |
| L6 | independent verify | CVO at the served layer, WITH a negative control (superseded DEP3 md5 must DIFFER) | *pending* |
| L7 | emitted-artifact verify | **OPEN BY DESIGN** -- 2026-08-07 13:00Z boot. **DEP3's L7 closed UNPROVEN**; this one inherits the same claim plus "does the timeout hold" | OPEN by design |
