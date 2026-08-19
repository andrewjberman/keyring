# TIGHTENING INCORPORATION BRIEF -- the approved set, step by step (CTO, 2026-08-19 ~14:45Z; to COO for execution)

**Authority:** Andrew-direct at the CTO terminal, VERBATIM: *"I like all your recommendations,
write a brief on what we need to incorporate here step by step and hand it off to COO; they
should go get it done."* -- ratifying the CTO assessment of CRO~A's
`EXECUTION_RISK_TRIAGE_20260819.md` (Andrew-commissioned), including the Rank-2(b) assertion
IN THE STAMP-COMPARISON SHAPE ONLY (the recommendation his word attached to). This satisfies
the no-gates law's your-word requirement for T2b as scoped below -- no wider.
**Governing test (binds every item):** a fix must retire a class BY STRUCTURE (inexpressible, or
free-to-check at an existing moment) -- never add apparatus that watches the class. Anti-scope
lines are part of the ratified scope; exceeding them needs a new word.

---

## T1 -- BROKER DELIVERY SEMANTICS (three primitives, nothing else)

**What:** on `org/mcp/server.py` (opal-owned): (i) `send_message` accepts a recipient LIST and
returns PER-RECIPIENT delivery state -- cc becomes mechanism, the body-cc class becomes
inexpressible; (ii) a queryable delivery/ACK read (has serial X's agent-side ACK for message M
landed?) -- SENT-vs-READ becomes a measurable state; (iii) the listener runs DETACHED from any
seat's process tree -- the port-7800 SPOF dies.
**Steps:** (1) CTO design shape via the build ladder (owed, my arch queue -- notably rung 2:
what the existing broker + inbox-watch substrate already carries); (2) 0.8.0-class builds at
respawn, BEHIND their dated rows; (3) acceptance per the triage: 3-recipient send with one dead
seat returns 2 DELIVERED + 1 QUEUED never silent success; the S1 body-cc replay is DETECTABLE
via the receipt query; kill the listener's original parent seat -> listener survives.
**Anti-scope:** no retry/guaranteed-delivery layers, no delivery-failure alarms, no send-side
approval steps. Three primitives exactly.

## T2 -- EXECUTING-PLANE: STAMPS FIRST, THEN THE CHEAP ASSERTION

**T2a (convention + builder change, no gate):** generalize the `BUILD_MANIFEST.json` vintage
stamp AE landed 08-19 (source pin, zip sha, per-member shas, build time) into every bundling
build path (`build_package.py`-class builders; EC2 staged bundles at their next touch). A
package that carries its build-input stamp makes the 22a CODE-layer read a lookup, not a
byte-diff expedition.
**T2b (the worded assertion, stamp-comparison shape ONLY):** at the safe-apply/safe-deploy
chokepoint for code-carrying deploys, compare the artifact's stamp against built-from source
and PRINT the classification loudly: CURRENT / STALE-BY-NEGLECT / DELIBERATELY-HELD /
TWO-HOMES-DIVERGED / UNSTAMPED. Only STALE-BY-NEGLECT stops the actor -- and it stops with a
self-serve inline audited acknowledge marker (`# stamp-acknowledged: <reason>`, the
system-current-override pattern), NEVER a wait on another person. Everything else proceeds with
its class printed.
**Steps:** (1) T2a rides the T1 builder's window or owning-lane touches; (2) T2b builds ONLY
after stamps exist on the deploy paths it checks (an assertion over absent stamps would read
UNSTAMPED fleet-wide and teach everyone to ignore it); (3) acceptance: the S5 replay (rebuild
committed, apply skipped, redeploy attempted later) refuses-until-acknowledged with
class=STALE-BY-NEGLECT; a DELIBERATELY-HELD member proceeds with its class printed; census
re-run shows stamp coverage rising with each touched builder.
**Anti-scope:** no fleet-wide byte-diff on every apply; no blocking of HELD or TWO-HOMES
classes (those are surfaced, routed states, not stop states); no retro sweep to stamp all 197
Lambdas (stamps arrive as builders are touched -- neglect-proof because the assertion covers
whatever is stamped and honestly says UNSTAMPED otherwise).

## T3 -- VENDOR-CLOCK ANCHOR AUDIT (one pass, can start NOW)

**What:** today's bd49f retime, generalized once: enumerate EVERY vendor pull schedule
(~6: schwab SDD x2 masters, the bd49f trio [DONE 08-19 -- the exemplar], orion, eclipse, the
cot rebalancer bronze placeholder [06:00Z, marked unconfirmed by its own comment], smartx if
any live pull remains) and compare each cron against the vendor's known/observed publish time
(BD ~01:02 ET ruled; 0824 SDD observed ~08:37Z; others = read the landing history). Retime the
mismatches exactly as today (targeted plan, ledger, applied-plane verify); record each anchor +
its authority in the P2 timing map so no future schedule is minted clockless.
**Owner:** AE 0.7.0 -- live and idle NOW; this is read+retime work squarely in their lane, and
it front-runs the class instead of detecting it.
**Acceptance:** every vendor pull cron carries a recorded vendor-publish anchor with authority;
each retime has its ledger; zero pulls fire before their vendor's publish window.
**Anti-scope:** no freshness checkers, no monitors -- the frontier READER roster (COO's Rank-3
execution) is the standing eye and stays reader-only.

## T4 -- TWO-HOMES: DECLARE FIRST, CONSOLIDATE BY ROW

**What:** one fork-or-drift DECLARATION row per census two-homes member (16 Lambda + 3 EC2):
FORK-DELIBERATE (with the why) or DRIFT (with a consolidation owner). Declarations from the
census owner class (0.8.0, at respawn) confirmed by owning lanes; consolidations then run as
ordinary lane work BEHIND R per row -- never a sweep (some forks are intent).
**Acceptance:** every census two-homes row carries a declaration; census re-run after each
consolidation shows the count fall by exactly the consolidated set, 0 new.

## RIGHT-SIZED / DEFERRED (part of the ratified scope)

- Frontier reader roster: DONE (COO 08-19); stays a READER. Instrumenting it re-opens the
  moratorium's anti-pattern -- refuse.
- Rank-4 PRD->TO coverage: DEFERRED. Revisit trigger = fleet re-expansion or the seam's first
  incident, whichever first; then it is a rung-2 extension of proof-of-spec-check's coverage
  mode, not a new tool.

## SEQUENCE AT CURRENT ECONOMY (COO drives; CTO gates applies as usual)

1. **NOW:** T3 to AE (live, idle). T1 design note at CTO (my queue, next quiet stretch).
2. **At 0.8.0 respawn (Wave 1, behind their dated rows):** T1 build; T4 declarations.
3. **With/after T1's builder window:** T2a stamps; **then** T2b assertion (stamps-first order
   is load-bearing).
4. Consolidations (T4 rows) behind R at owning lanes.

-- 1.0.0_SA_CTO. Triage: `org/tier1_exec/4.0.0_SA_CRO~A/deliverables/EXECUTION_RISK_TRIAGE_20260819.md`.
   Assessment ratified in-session; this brief is the execution form.
