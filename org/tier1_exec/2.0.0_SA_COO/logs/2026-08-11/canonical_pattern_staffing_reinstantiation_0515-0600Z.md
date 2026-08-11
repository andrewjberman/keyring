# Canonical-Pattern Program — COO Reinstantiation + Staffing Window (0515–0600Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE

## Window

Reinstantiated 2026-08-11 ~0515Z (Andrew-direct via MSTR). Boot payload =
`org/tier1_exec/1.0.0_SA_CTO/handoffs/2026-08-11_0503Z.md` @1a518b303f, COO half (SELF DO-FIRST
item 5: staffing + sequencing). Predecessor session read OFFLINE at a dead PID — genuine
reinstantiation, not a context-clear.

## Startup (XXX.md Step 1b)

`/watcher` armed once — Monitor `b4rtyvar5`, confirmed `running` via `TaskOutput`. **PID-identity
check run BEFORE any watcher action** (no `inbox-watch.sh` process existed for this serial; serial read
OFFLINE at PID 26144 ≠ mine) — so no orphan reap, no dual-COO collision risk. Registered PID 22976.
Serial file stamped. A.2 audit-archive rc=0, 0 findings. A.3: `PATH: 96 of 97 comp-tools resolve bare`
+ **forwarder EXERCISED** (banner produced), not merely resolved. `CronList` empty; **zero crons armed**
— Step 1b-F COO row carries no live scoped authorization (the 08-06 `/drive` re-arm was DISCHARGED
08-07), so `/drive` stays OFF.

## What I delivered

**`org/tier1_exec/2.0.0_SA_COO/deliverables/CANONICAL_PATTERN_STAFFING_AND_ROUTING_20260811.md`** —
the boot payload's COO half, ITEM_0 discipline (OWNER + TRIGGER + NAMED PRECONDITION per act) with a
13-row remediation register. Six commits across the window as state moved:
@014e7af672 → @9029676799 → @04c9d4b5f1 → @ad176c6e62 → @dbf69ccdc0 (+ the rename pass).

**Six acts dispatched, four already closed or landed:**

| act | state at log time |
|---|---|
| CPR-1 INF Sunday union-preserve (hard date 08-16) | ✅ **CLOSED** — DS landed @9b29609e42 / @9196959b53 / @76386cd21c, deployed to all 3 code prefixes, acceptance **exercised 13/13**, carry set 26,371 rows / 16 accounts EXACTLY matching CRO~A's independent oracle |
| CPR-4 D_04 residual → classification | **LANDED** @7341b27d50 (12/12 exercised); **both never-widen halves given**; serve choreography at DS |
| CPR-2 cot double-lag | in flight at DS |
| CPR-3 `ssm.tf` sweep order | with AE |
| X-iv delete 2 IAM-dead stages | AE working (live-primitive CURRENT-state verify first) |
| X-iii / X-ii / X-i | **staged and dispatched** — gate released by the CVO cert |

**Sequencing calls I owned:** adopted CTO's reverse-blast cutover order (iv→iii→ii→i); item-3 firm
order **inflection → 49F → cottonwood**; L5/L6 advi as **ONE sweep** post-archetype with two
preconditions (deployed-FE grounding; no RECON-5b wait); RECON-6 → CRO base; RECON-5a queued;
RECON-5 split into 5a endpoint-inventory (parallel) / 5b conformance (post-archetype).

## Findings I surfaced (none adjudicated by me)

1. **`C-n` NAMESPACE COLLISION, then a ruling conflict.** Three `C-n`/`R-n` namespaces live at once.
   CTO and CRO base ruled **opposite** conventions 15s apart. I did **not** adjudicate between two
   Tier-1 execs — surfaced both verbatim and ran a convention-independent interim protocol (descriptive
   reference + `file:line`), so **no worker was whiplashed and no dispatch needed re-issuing.** Settled
   on CRO's form (RECON-1..7 chapters; jam findings keep C-1/C-2/C-3). CTO adopted
   newest-namespace-moves as the standing tiebreak.
2. **I then committed the same defect.** My own act labels `R-1..R-4` collided with the 08-10 taxonomy
   rulings `R-1..R-5`. Renamed to `CPR-*` by CRO's own rule, with a mapping table to already-dispatched
   seats. Disclosed, not quietly fixed. The rename pass printed its own denominator and caught one
   leftover a line-wrap had hidden.
3. **VENDOR-GRANT GRAIN, both directions, one root.** Flagged a possibly TOO-WIDE read (BD egress
   "granted" while the standing lift is cot-BD only and 49F **is** a Black Diamond firm) — CRO~A
   answered AT-REST-ONLY, no violation. Then found the MIRROR at CRO base: a TOO-NARROW read marking
   the 49F unlock "vendor-egress-gated" when SmartX is on the standing lift. **The too-narrow direction
   has no rule pointed at it and fails invisibly — it presents as a legitimate blocker.** CRO conceded
   and removed the false blocker @108277a347. The unlock then landed **at rest, zero egress spent.**
4. **IDENTIFIER FAMILIES** — measured off Andrew's naming ground truth: `blackdiamond/` holds **both**
   `49f/` and `cottonwood/`, so "bd" as a PIPELINE means 49 Financial while "BD" as a vendor spans two
   firms. CTO ruled the four-family clause @b59dbed2d7 + an L1 key-annotation rule. Produced a real
   correction: the "complete fact tables" claim was measured over `schwab/08335338`, not
   `blackdiamond/49f`.
5. **RULE-24 CHECK on Andrew's instruction-4 quality partition** — MECE is satisfied, but the risk sits
   in the **UNITS not the values**: "script / engine / subsystem" are three **nesting** grains, so a
   subsystem EXTRACT over three DISCARD children has no single side. Surfaced to CTO + CRO with the
   cheap fix (declare census unit grain, or state the rollup rule). Not adjudicated.
6. **SESSION-BOUNDED EGRESS recorded with its expiry.** Andrew ~0549Z @9e1fc54623: free egress *"for
   the remainder of this session."* Recorded the **bound** as the load-bearing half — a time-bounded
   grant that generates durable artifacts propagates an **expired authorization** into them. Every
   dispatch relying on it carries the bound inline; the register states plainly that a later reader does
   **not** have it. Surfaced the "whose session" ambiguity (Andrew's sitting vs an agent process that
   can outlive it) to CTO without blocking anything.

## Two register defects, both caught by DS executing

My CPR-1 dispatch named **one** deploy prefix; the script was **TRIPLE-HOMED**, and
`orion-gold-dispatch.sh sync_scripts()` fails loud on a differing-content basename collision — a
gold-only deploy would have **REFUSED the next chain sync (INF outage)**. My CPR-4 row said
`PRECONDITION: none`; there was a **live `DEPLOY-SERVE-HELD` sentinel**.
**Root: my preconditions were derived from specs and drafts; the DEPLOY MECHANISM's own preconditions
are only visible from the lane.** Routing being right does not make the mechanism checks mine to have
found — and a register that says "none" is more dangerous than one that says "unknown." Both folded
back as remediation rows (8 amended, 11/12/13 added).

## Self-corrections made in-window

- Retracted my own `~B` spawn ask ~30s after sending it — CRO base delivered RECON-4 before it arrived,
  so the premise ("both CRO seats occupied") was false. MSTR caught it **at the decision point**;
  LD-0392 committed as `status=reversed`. I had cautioned MSTR about stale capacity reads 90 seconds
  earlier in the same message and was then caught by the same condition: **any capacity claim is a
  snapshot; the remedy is re-checking the premise at the irreversible act, not more care at read time.**
- Corrected my cottonwood **reason** (Andrew @a4d5147211): not "no model feed exists" (measured absence)
  but **SOURCE-EXISTS-PIPELINE-ABSENT** — an ingest build. Conclusion unchanged, mechanism was false,
  corrected in place because a right conclusion on a wrong mechanism gets copied forward.
- Superseded my own CPR-4 constraint ("labelling/surfacing ONLY") after Andrew's ratification upgraded
  the act to the residual's retirement vehicle — **a faithful application of my original instruction
  would have made DS stop and flag it.** Corrected before the cycle was spent.

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-which` (A.3 exercise probe) | PASS — forwarder RAN, banner produced; 96/97 resolve bare |
| `comp-find` (C-2/C-3 grounding, `bd-gold-runner`, `DEPLOY-SERVE-HELD`) | PASS — denominators + BAND classification let me separate fixture hits from source hits in one call; the `DEPLOY-SERVE-HELD` run located the enforcement at `safe_deploy_core.py:203-207` |
| `aws s3 ls` (operational, off-rail) | PASS — the bucket/prefix topology that grounded the naming law and the ADVI archetype substrate (`08335338` has `gold/`, `08242234` does not; `blackdiamond/` spans two firms) |

**What worked:** `comp-find`'s denominator + band line was decisive twice — it separated a
fixture-string hit from a source hit without a second call, and it grounded the serve-gate mechanism at
source so I signed a never-widen half on measured code rather than on DS's report.
**What failed:** nothing at my seat.
**Gap found:** carried forward from the window, not newly mine — `comp-pipescript deployed` renders ONE
`aux:manual_api` row for a **triple-homed** script while reading MATCH (rows 1/2/12). A deploy-map
instrument that knows one home of three is the two-channel blindness one layer out.
Coordination seat: verification of leg evidence stayed with the owning seats' live primitives; I ran
comp-tools for my own grounding (naming, serve-gate, C-n) and refused to let a comp-tool carry an
applied-state claim.

## Blockers

**None at me.** At **CVO:** RECON-4's cert (queued; my TO decomposition proceeds on DELIVERED per the
matrix's own non-serving-design rule, cert noted pending). At **DS + CTO:** the CPR-4 serve-release
choreography (ledger → lift → deploy → **re-hold same window** → republish). At **AE:** X-iv close,
then X-iii/X-ii/X-i. At **CTO/CRO:** the instruction-4 unit-grain declaration.

## Current State

Program **fully seated** (CTO, CVO, AE, DS, CRO, CRO~A, MSTR). **Nothing waits on Andrew** — he ratified
the exception set + pattern spec v1.0 @d272021791. **Cutover gate RELEASED** — CVO CERTIFIED
@cc62267d89, zero cells refused. Integrator pushes landed @7f579d72b6 then @5e1d1c2c51 (zero
local-ahead; MSTR is sole shared-branch integrator per LD-0367 r2 / LD-0368).

**Two CVO riders are binding in my register:** (a) act X-ii must ground the staging producer IDENTITY
with one CloudTrail/CW read — the 08-09/08-10 ~13:00Z `_aggregate_aua` writes happened with the main
chain **dark**, so the producer is an INFERRED cell and re-homing an unidentified producer fails
silently; (b) remediation row 13, consolidator carry-forward on stale staging inputs
(process-ts-FRESH / data-as-of-STALE). CVO also corrected the clock-floor framing in a way that
**preserves** act X-i's deliverable: `mdpf-scheduled-floor` is live but in the SCHEDULER namespace
targeting the CONSOLIDATOR — **nothing clocks the EC2 chain.**

## Next Steps

1. **[2.0.0_SA_COO] The 13:30Z RP-W3 bar** — the ONLY item I hold. Face 12/12 on the ratified basis
   (@e82326bdb2), Amendment-III interpretation table pre-registered, ADDENDUM to
   `org/critical_paths/change_management/20260811T0150Z_mdpf-atomic-window.md` after the cycle.
   Non-cottonwood degradation = failure, loud. **NOTHING IS ARMED AGAINST IT AND NOTHING WILL BE**
   (moratorium; a watcher on an unattended bar measures the watcher).
   ⚠ **CONTINUITY: the bar is ~7.5h out and may outlive this session. A successor inherits it from the
   ledger + §3 of the register, not from recollection.**
2. **[0.4.0_DS_ClientPlatform]** CPR-4 serve choreography (all four steps in one window or roll back);
   CPR-2; then the two UNMEASURED residuals (14 on the 49F **map-side leg** of 5,715 distinct;
   11 of 561 inflection). ⛔ **CORRECTED post-log (CVO delta-cert @da62a742c5): the 49F join's
   END-TO-END rate is 99.65% = 7,205/7,230 with 25 feed allocations reaching no spine account. The
   99.8% (5,701/5,715) I carried is the MAP-SIDE LEG ONLY; feed→map is 99.86%. Any build TO carries
   the FULL-PATH denominator, never a leg's** — see the register §4g correction.
   **Sunday 08-16:** the chain log must show the UNION-PRESERVE line — zero-carry also passes; ABSENCE
   is the failure.
3. **[0.7.0_AE_CloudOps]** X-iv close → X-iii → X-ii (producer-identity read FIRST) → X-i (schedule
   floor lands here).
4. **[4.0.0_SA_CRO]** RECON-6 endpoint-delta census (critical path — the last input to run atom-8
   conformance at scale); RECON-5a behind it.
5. **[1.0.0_SA_CTO]** instruction-4 census unit grain; the `bd↔cot` gate OPEN CHECK
   (`comp-firmsep-sweep`); the three instrument gaps.
