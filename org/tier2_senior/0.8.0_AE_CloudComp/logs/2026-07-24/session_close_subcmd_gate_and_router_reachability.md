# Session close: subcommand-declaration gate + stage-2 fail-open fix + router-reachability (blocked) + contamination correction

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

Window 2026-07-23 ~22:16Z -> 2026-07-24 ~04:30Z, continuing `session_close_2056-2210Z.md` (@bb9add30a).
Serial `0.8.0_AE_CloudComp` (base). Stood down mid-window (Andrew-direct via CTO 213512Z on deploy_ledger;
CTO~Z re-confirmed), then acted on discrete P1 findings + the CTO~Z subcommand-gate GO before stand-down.

## My commits this window

| Commit | What |
|---|---|
| `a0209b3ef` | SUBCOMMAND-DECLARATION completeness invariant -- the router can't be blind to a registered tool's derivations. 3 approved constraints, 4-direction mutants |
| `6b260bb41` | targeted backfill: comp-iam +9 (incl simulate+reconcile), comp-pipescript +5 (incl postdeps) -- the LAW-MANDATED derivations, DECLARED in tools_index |
| `ebce50ce8` | stage-2 gate FAIL-OPEN fix (CVO~Z finding): a missing/moved rule bank silently disarmed the whole stage-2 axis; real-file move/rename mutant now REDDENS |
| `e78e006cb` | PENDING patch (NOT applied): router-reachability for the 3 law-mandated calls -- behavior-verified 4/4 rank-1, BLOCKED by an unevaluable self-route gate; preserved in-lane |
| `550d8b265` | retire the comp-routes false-secure blind_spot ~A's fix closed (+ inadvertently swept ~A's uncommitted R2 contract hunks -- contamination, corrected on the record) |

## THE SUBCOMMAND-DECLARATION GATE + ITS FINDING (the window's headline)

~B's LATENCY census needed the derivation surface (tool x subcommand). I measured before answering:
tools_index `subcommands:` is populated on 65/65 tools and gated on NONE -- perfect camouflage, a field
present on every row and enforced on none READS complete while it drifts. Drift 16/24 apples-to-apples.
THE FINDING THAT MATTERS MORE THAN THE COUNT (verified by me, not relayed): the omissions include
derivations CLAUDE.md MANDATES -- comp-iam `simulate` (Rule 22a's spine) + `reconcile` (the only
APPLIED-plane overlay), comp-pipescript `postdeps`. THE ROUTER CANNOT ROUTE TO THE CALLS THE LAW REQUIRES
-- the registration invariant's own reasoning one grain down.

GATE built + arch-gated (CTO~Z 220731Z), 3 constraints: (1) pinned wrappers don't false-positive;
(2) declared-side grammar (the field mixes subcommands with flags/usage-forms); (3) UNKNOWN never FAIL where
the surface is not establishable (37 tools). SCOPE: blocks only on a registration THIS COMMIT touches, so
the gate lands AHEAD of the backfill without freezing the fabric on 13 known-drifted tools. Static
extraction only -- for the auto-refresh family the measurement instrument would itself be a mutation.

## THE DEEPER FINDING (CTO~Z, source-confirmed): DECLARATION != REACHABILITY

My backfill @6b260bb41 closed a DECLARATION gap in a surface NO CONSUMER READS. comp-which ranks TOOLS off
a CURATED VOCABULARY TABLE in .tools/comp-which and NEVER reads tools_index (:1006-1010). So all 3
law-mandated calls were DECLARED AND STILL UNROUTABLE -- the program's own defect class occurring inside its
own remediation pass. My FIRST reachability attempt (entries[] rows) ALSO failed -- I re-ran CTO~Z's four
queries and nothing surfaced. Behavior-verification is the only reason that didn't ship. The WORKING fix
(three curated tuples) takes all 4 intents ABSENT -> RANK-1, but it edits .tools/comp-which (the router
binary), which makes the self-route completeness member evaluate all 68 tools -> 68 comp-which subprocess
spawns -> HANG. Preserved @e78e006cb; NOT landed.

## THE SELF-ROUTE GATE IS UNEVALUABLE (grounded, reassigned to ~B)

safe-commit BLOCKED on "self-route invariant could not be evaluated (... timed out after -5032.094 seconds)".
GROUNDED: `_run_comp_which` (:282-285) passes a FIXED timeout=60 -- there is NO timing arithmetic of ours,
so the -5032 is CPython's Popen._remaining_time on Windows: the call HUNG ~84 minutes past a 60s bound
before the check fired. THE BOUND DID NOT BOUND. ~B's inversion (confirmed by my grounding): an unreliable
bound may ALSO fail to fire on a real hang -- silent, strictly worse. Reframed step-1 from a clock-arithmetic
bug to an ENFORCEABILITY bug (subprocess.run timeout under capture_output on Windows). FIX FEASIBLE without
touching the denominator: comp-which exposes _score_rule/_manifest_matches, so a warm in-process route
collapses 68 spawns to one import -- caution: must reproduce ranked-list semantics EXACTLY, verdict-IDENTITY
on all 68 as the acceptance, not speed. Reassigned to ~B (owns LATENCY + the cost-driver diagnosis) with
this grounding verbatim + the redden-mutant + hang-timeout-mutant requirements.

## STAGE-2 FAIL-OPEN (CVO~Z finding, my defect, fixed @ebce50ce8)

My self-tests exercised only the ENFORCING path. The DISARM path was FAIL-OPEN: canon_vocab() swallowed a
read failure and returned {} BEFORE my fail-closed handler could fire, so a missing/moved rule bank
silently disarmed the whole stage-2 axis while printing a benign "DORMANT" line and PASSING. Docstring said
fail-closed; path was fail-open. WORSE: the dormancy rationale EXPIRED at canonization @5d1161d70 -- I wrote
"pre-canonization" 4h before ~C canonized type_tuple and never re-read it (stale-record-with-authority,
from the lane closing that class). FIX: canon_vocab_strict() RAISES on read failure; both empty-vocab
conditions BLOCK with distinct correctly-attributed messages; dormancy branch RETIRED. CTO~Z's required
mutant -- a REAL on-disk move/rename of the rule bank -- REDDENS (rc=1), restored clean, no artifact.

## COMP-ROUTES BLIND_SPOT + THE CONTAMINATION I TRIPPED

CVO~Z (self-initiated P1-false-secure): ~A's fix closed the origin_type false-secure defect but the
blind_spot at :288 still declared it LIVE -- a security tool printing a correct auth-map + a line calling it
wrong. Verified both the fix (extract_routes.py:371,385) and the stale line myself; retired it, kept the
narrower REAL residual (CVO~Z later grounded it as latent, zero live triggers). BUT my safe-commit by
pathspec on that shared file SWEPT ~A's 3 uncommitted R2 contract hunks into @550d8b265 -- landing ~A's R2
contract WITHOUT ~A's R2 code = a false-clean at HEAD on a security tool. CTO~Z caught it HEAD-plane. I
corrected the MECHANISM (contamination via whole-file staging, NOT authorship -- git blame launders
authorship onto the sweeping commit, which CTO~Z banked as their own lesson). ~A committed R2 code
@b9f80e6da; false-clean CLOSED at HEAD (11 markers, was 0), verified independently by me + CVO~Z + CTO~Z.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-manifest-check | subcommand member (4 directions) + stage-2 member (2 disarm paths) | PASS/BLOCK as designed | new member; standing drift reported not blocking; drifted-registration blocks |
| comp-which | 4 behavioral queries x2 (entries[] fail, curated-tuple pass) | PASS after fix | ABSENT->RANK-1 all 4; the routing surface is the curated table, not tools_index |
| comp-which-routing-test | self-route member (via commit) | UNEVALUABLE | the 68-spawn hang; negative-timeout artifact; reassigned to ~B |
| argparse/static extraction | comp-iam/pipescript/transform declared-vs-actual | FINDING | third independent instrument agreeing with ~B + my earlier run |
| deploy_ledger | (prior window) | closed | crash/reader fixes accepted; stood down |
| comp-system | --check + regen x3 | CURRENT | fail-closed on each source touch |
| commit-gate/safe-commit | every commit | PASS | ruff caught 1 unused import; the same-file contamination guard-gap surfaced |
| pytest | test_output_contract (+ subcmd + stage-2 disarm fixtures) | 37/37 | real-file move mutant; both disarm paths; 4-direction subcmd mutants |

**What worked:** measuring before answering (caught the 65/65-populated-0-gated camouflage); behavior-
verification over registry diff (caught that BOTH my reachability attempts didn't route); testing the
dispatch's premises (2 of 3 deploy_ledger legs already existed). **What I got wrong + surfaced:** the
stage-2 disarm path was my fail-open (CVO~Z caught it); I tripped the same-file contamination class
(corrected the mechanism, not just the symptom). **Gaps found + routed:** self-route gate enforceability
bug (->~B); safe-commit same-file contamination blind spot (->main CTO); the coupling-gate (contract-vs-code,
committed-state-keyed).

## Blockers

- ROUTER-REACHABILITY (a): BLOCKED, evidence-cited -- the self-route completeness member is UNEVALUABLE
  (68-spawn hang, negative-timeout). Patch preserved @e78e006cb; lands the moment ~B makes the gate
  evaluable. NOT an assumption-block: I reproduced the hang + grounded the mechanism.

## Current State (zero-prior-context handoff)

- LANDED + at HEAD: subcommand gate (a0209b3ef), tools_index law-mandated declarations (6b260bb41),
  stage-2 fail-open fix (ebce50ce8), comp-routes blind_spot (550d8b265). All pushed.
- comp-which ROUTING (the surface agents actually hit): the 3 law-mandated calls are DECLARED in tools_index
  but STILL UNROUTABLE via comp-which -- the curated-tuple fix that closes it is in the PENDING patch, not
  landed. Rule 22a discoverability hazard OPEN, held knowingly by CTO~Z (the control is inlined in the
  mandate; only the wrapper is unroutable).
- self-route completeness member: UNEVALUABLE at HEAD (blocks the registration surface for any UNBOUNDED
  change -- .tools/comp-which or entries[] edits). Bounded tools_index-entry edits still commit (they
  evaluate only changed tools).
- Two-stage output contract COMPLETE + stage-2 now fail-CLOSED. My owned surface: comp-output-contracts.yaml
  (20 declared), comp_output_contract.py, manifest_check_cli.py (9-member completeness family).

## Next Steps

- [0.8.0_AE_CloudComp~B] fix the self-route gate ENFORCEABILITY bug (explicit Popen + monotonic deadline +
  kill; in-process warm route; verdict-IDENTITY-on-68 acceptance; redden + hang-timeout mutants). THEN I
  land the reachability patch @e78e006cb.
- [1.0.0_SA_CTO] (routed by CTO~Z) safe-commit same-file contamination guard.
- [1.0.0_SA_CTO~Z] the coupling-gate (contract-vs-code, committed-state); the 11-tool subcommand sweep +
  whole-universe widen (atomic) once the gate is evaluable.
- [0.8.0_AE_CloudComp] land reachability on ~B's gate fix; the 2-regex latent comp-routes residual (queued,
  not urgent).

## MCP Traffic

~40 this window (20 in / 20 out). Significant: CTO gate-integrity dispatch -> deploy_ledger fixes ->
Andrew-direct STAND DOWN; ~B census asks -> subcommand finding -> CTO~Z arch-gate GO -> gate built + backfill;
CVO~Z stage-2 fail-open finding -> fix; CTO~Z reachability-not-met ruling -> curated fix (blocked); CVO~Z
comp-routes P1 -> blind_spot retire -> CTO~Z HEAD-plane false-clean catch -> contamination correction ->
~A R2 code lands -> closed. Three of my own defects surfaced + corrected this window.
