# EXECUTION-RISK TRIAGE -- where the macro workflow actually breaks, and where the next tightening dollar goes (4.0.0_SA_CRO~A, 2026-08-19)

**Authority:** Andrew-direct at this terminal 2026-08-19 (~1430Z): *"I do want to tighten this, where
do you see the most execution risk here? I want to triage the process and identify where the highest
leverage work could go. Research the logs and processes and see what you can find."*
**Method:** grounded on (a) the 08-18/19 push window's own failure record (9 live specimens, every one
measured, commits cited), (b) a frequency census over the 1,037-file memory corpus (tight-pattern
filename clustering, denominators printed, first-pass over-match discarded), (c) the as-built process
artifacts (NFRA_DEPLOYCENSUS instance, R-WATCH TO, LD-0424, the cc-defect record). Rankings are
recurrence x blast-radius x (1 - current-coverage). CRO does not dispatch; owners are suggestions.

---

## 1. THE EVIDENCE BASE

### 1a. This week's live specimens (all inside ONE 24-hour window, all measured)

| # | specimen | class | cost |
|---|---|---|---|
| S1 | "cc CTO" written in a message BODY copies nobody -- CTO found the waiting 4b determination only via a roster read; several same-session body-ccs survivorship-masked (`feedback_broker_cc_is_a_body_line_that_copies_nobody.md`, COO-owned 08-19) | COMMS | DT freeze released late ("delivery-lost via broker-cc class", LD-0424 commit); a determination sat invisible |
| S2 | CTO seat git-live but broker-deaf ~16:05-17:05Z 08-18, ratify route queued (MSTR 163340Z) | COMMS | ~1h latency on a ratification path |
| S3 | Broker DOWN fabric-wide after the kill wave -- the port-7800 listener lived under a killed seat's process tree (LD-0424 finding 2) | COMMS/SPOF | spares' MCP clients orphaned until a register_agent restart; confirmations went filesystem-direct |
| S4 | kill-agent.ps1 single-serial path matches the serial ANYWHERE in a CommandLine, no self-exclusion -- first CVO kill killed MSTR's OWN MCP python + both Monitors (LD-0424 finding 1; the LD-0274 mention-is-not-identity class, now in the kill instrument) | IDENTITY/INSTRUMENT | near-decapitation of the coordinator during wind-down; 2 kills re-run direct-PID |
| S5 | MDPF_PROVENANCE T-B PB-1/PB-2 UNCOMPUTABLE: mdpf-gold-lambda bundled the OLD member (ce9c0284...) -- the deployed plane lagged the committed fix; AE rebuilt+applied same day (@1949f72b7b, @dded9d334b) | EXEC-PLANE | a dated TO's proof blocked on a plane nobody had re-read; the gated mdpf delete held |
| S6 | NFRA_DEPLOYCENSUS (@ its 08-18 instance, 6/6 PASS): **197 Lambdas = CURRENT 141 / HELD 11 / STALE-BY-NEGLECT 8 / TWO-HOMES-DIVERGED 16 / UNREAD 21**; EC2 staged = CURRENT 6 / STALE 6 / TWO-HOMES 3 / UNREAD 12. Positive control FOUND the known inf-silver-chain divergence (build_billing_dim.py sim 0.345) -- the producer behind the 08-12 served is_fee_earning defect | EXEC-PLANE | the class now has a fleet denominator: ~12% of read Lambdas diverge from built-from source |
| S7 | Schwab stopped publishing FAM for 08335338 after as_of 08-10 -- detected at SIX TRADING DAYS (AE fork verdict 130754Z; vendor-side confirmed) | VENDOR-DETECT | the flagship program's entire P2->P4 date chain re-dated to R (@f79760179a); fleet wound down |
| S8 | Wrong-bucket clean-zero near-miss: after the overnight GOLDHOME move, listing the OLD bucket with the NEW prefix returned a clean well-formed EMPTY -> a false "inputs vanished" read, falsified before acting (DS~B 08-19 log) | INSTRUMENT-LIES | caught by care, not by a control -- the exact class CONTROLS_OVER_CARE names |
| S9 | comp-state 08-19 default-env run: 634 of 2,487 governance records BEHIND/POST-CLOSE (advisory recall; mostly lexical noise, but the only drift instrument) | RECORD-DRIFT | reconciliation lag is chronic, now measurable |

### 1b. The corpus census (1,037 memory files; overlapping clusters; tight patterns; first-pass
over-match with generic tokens DISCARDED -- the honest run)

| class | recorded lessons | still growing? (newest-15 read) |
|---|---|---|
| COMMS-DELIVERY | **79** | YES -- 2 of the newest 15 (cc-copies-nobody 08-19, broker-PID oracle 08-11); the class grew a NEW MODE this week (WRITTEN != SENT), not just a new instance |
| INSTRUMENT-LIES | **68** | YES -- zero-access-oracle-plane (08-18), TF-plan-end-state (08-15), lens-wrong-referent (08-12), never-launched-third-state (08-11) all in the newest 15 |
| RECORD-DRIFT | ~55 | slowing -- the J1/J2 instruments landed this week |
| IDENTITY-LANE | ~47 | S4 added the kill instrument to the class this week |
| EXEC-PLANE | **46** | YES -- S5/S6 this week; the census turned anecdotes into a denominator |
| VENDOR-TIMING | ~23 | S7 is the costliest single instance to date |

**The reading:** the two biggest classes by recurrence (COMMS 79, INSTRUMENT 68) are also the two
still minting NEW FAILURE MODES. EXEC-PLANE is third by count but first by measured blast (served
client data wrong while every instrument read green -- the 08-12 defect). VENDOR-DETECT is smallest
by count and largest by single-instance program cost (S7 re-dated the whole push).

---

## 2. THE TRIAGE (ranked by leverage = recurrence x blast x coverage-gap x feasibility)

### RANK 1 -- THE COORDINATION PLANE HAS NO DELIVERY SEMANTICS (COMMS: 79 lessons, 3 new members this week)

**The risk:** every joint of the macro workflow -- GO issuance, gate releases, determinations,
ratifications, halt words -- travels over a broker with **no sender auth as delivery proof, no
multi-recipient send, no cc mechanism, no delivery receipt, no read receipt, and a single listener
that dies with one seat's process tree** (S1/S2/S3). The estate's entire compensation is CONVENTION:
RAVC ack discipline, watcher protocol, "separate sends per seat." Convention is exactly where this
fabric's failures live (measured: cc-defect S1, 7h17m orphan-eaten mailbox, dual-COO collision,
1h26m unarmed-agentbus delay, the Kimi inferred-gate stall's delivery half). **The structural point:
every OTHER remedy in this triage is delivered over this plane. A tightened gate whose release
message is never delivered is a silent hold -- the exact invisible-approval-step class the no-gates
ruling exists to kill.**
**Coverage today:** conventions only. Zero mechanics. The class is still producing new MODES
(WRITTEN != SENT, 08-19) on a mechanism months old -- meaning discovery is not exhausted.
**Highest-leverage work (a ROUTE fix, not a monitor -- moratorium-clean; NOT a gate -- no approval
step on any work):** one deliverable on `org/mcp/server.py` (opal-owned):
 (i) `send_message` accepts a recipient LIST and returns PER-RECIPIENT delivery state -- making the
     cc a mechanism instead of prose (kills S1's whole class by construction);
 (ii) a queryable delivery/ACK read ("has serial X's agent-side ACK for message M landed?") -- making
     SENT-vs-READ a measurable state instead of a doctrine paragraph;
 (iii) broker as a detached process not parented to any seat (kills S3's SPOF).
**Owner (suggested):** the MCP/server lane (historically MSTR/CTO-adjacent; COO routes).
**Acceptance-that-fails-if-wrong:** a 3-recipient send with one dead seat returns 2 DELIVERED + 1
QUEUED (never a silent success); the S1 replay (body-cc only) is DETECTABLE by the receipt query;
kill the broker's original parent seat -> the listener survives.

### RANK 2 -- THE EXECUTING PLANE DIVERGES FROM SOURCE, AND THE GATE CANDIDATE'S PRECONDITION JUST COMPLETED (EXEC-PLANE: 46 lessons, fleet-measured 12%)

**The risk:** 24 of 197 read Lambdas run bytes diverging from their built-from source (8 neglect, 16
two-homes), +21 unread; EC2 staged 6 stale / 3 two-homes / 12 unread (S6). The class produced the
estate's worst measured incident shape -- served client data wrong while plan-0-diff, config reads,
and green runs all pass (Rule 22a's own record; the 08-12 is_fee_earning defect traces to exactly a
census-confirmed two-homes member). It bit a live dated TO again THIS WEEK (S5).
**Coverage today:** the census (one-shot, classify-don't-fix, DONE 08-18) + Rule 22a's per-use read
discipline (CONV, expensive, applied only when someone thinks of it). CLAUDE.md Rule 22a already
carries the remedy as a named gate candidate "sequenced AFTER the authorized census" -- **that
precondition is now satisfied; the candidate is unblocked by its own stated terms.**
**Highest-leverage work, two halves with different remedies (Rule 24(iv)):**
 (a) **The 16+3 TWO-HOMES consolidations** -- the ROOT: one logical producer, two independently
     editable homes; byte drift is only the symptom. Consolidation kills the class by construction
     (one-fact-one-home, applied to code). No gate needed; ordinary lane work off the census's named
     rows.
 (b) **The apply-time deployed-vs-built-from assertion** (classifying stale-by-neglect /
     deliberately-held / two-homes, per 22a's own spec, so the reflex is never blind "redeploy").
     ⛔ THIS IS A GATE -- proposing is legal, implementing needs YOUR word (no-gates rule). It is on
     the table now because its stated precondition (the census) completed.
**Owner (suggested):** (a) the owning lanes per census rows, COO sequences post-R; (b) CTO routes IF
worded.
**Acceptance:** (a) re-run the census instrument on consolidated members -> TWO-HOMES count falls by
exactly the consolidated set, 0 new; (b) the S5 replay (rebuild committed, apply skipped) REFUSES at
apply time with class=stale-by-neglect.

### RANK 3 -- VENDOR-FEED STOPPAGE IS DETECTED BY ACCIDENT (VENDOR-DETECT: smallest class, costliest instance)

**The risk:** S7 -- a vendor silently stopped one account's feed and the program consumed the stale
vintage for SIX TRADING DAYS before an unrelated fork investigation surfaced it. Cost: the flagship
push's whole date chain re-anchored; the fleet wound down. The moratorium (correctly) bars building
freshness checkers; NEVER#1 (correctly) bars wall-clock staleness panic. But between them sits an
uncovered middle: **nobody is ASSIGNED to read the existing sanctioned instrument on a cadence.**
**Coverage today:** R-WATCH (issued 08-19) -- ONE feed, ONE account, until R fires, human-read daily.
The instrument for the general case EXISTS: comp-freshness with `freshness_basis:
trading-day-frontier` (the NEVER#1-sanctioned form). The gap is a reader, not a builder.
**Highest-leverage work (an ASSIGNMENT, not a build; moratorium-clean by the same logic as R-WATCH's
own authority line: "this is a READER seat, one listing + one log read per day"):** generalize
R-WATCH's A1 shape to the vendor-feed roster (~5 feeds: schwab x2, orion, eclipse, blackdiamond x2)
-- one paginated frontier listing per feed folded into an existing seat's daily turn-top, verdict in
trading days, report-on-change only. Zero new infrastructure; one TO amendment.
**Owner (suggested):** DS base (already holds R-WATCH; same act, wider denominator) or rotate at COO
discretion.
**Acceptance:** a synthetic hole (yesterday's prefix absent on a trading day) surfaces in <=1 trading
day in the reader's log; a weekend/holiday correctly surfaces NOTHING (the NEVER#1 control).

### RANK 4 -- THE LAST UNCHECKED SEAM IN THE PROOF CHAIN: PRD -> TO COVERAGE (no measured incident yet -- and that is the point)

**The risk:** every downstream seam is now checked (TO->instance coverage: proof-of-spec-check
positional mode; instance->rows: schema + conditional rules; artifact->rows: the A_03 heuristic).
The TOP seam -- does the TO SET issued for a PRD actually span the PRD's acceptance battery? -- is
checked by nobody but the COO's eyes at decomposition. The A_03 zero-battery class (caught by
eyeball twice before mechanization) says this seam WILL produce its incident; the only question is
whether before or after we check it.
**Coverage today:** none mechanical. GROUND-TRUTH-AT-OUTSET (Andrew 08-14) gives the inputs: a PRD
package now carries its atom_decomp run, and TO expected-values derive from run rows -- the
derivation is exactly what a coverage read can check.
**Highest-leverage work:** extend proof-of-spec-check's coverage mode one level up: a PRD-side
declared criterion universe (the decomposition's own criterion-id mint, committed as an artifact) vs
the union of issued TOs' expected sets -- both directions, denominators printed. Read-only, advisory,
run by the issuer at decomposition close. Rung 2: the coverage_check function already exists; the
input is one new declared artifact.
**Owner (suggested):** COO (issuer-side) + the comp-tool lane for the mode.
**Acceptance:** a hand-withheld criterion (in the PRD mint, in no TO) prints as a MISSING row;
a TO criterion absent from the mint prints as UNEXPECTED.

### BELOW THE LINE (real, but lower marginal leverage NOW -- mostly riding momentum)

- **INSTRUMENT-LIES (68):** the remedy is already institutionalizing -- frame-printing instruments
  (comp-find, --proof-board, the census) keep replacing frameless reads; S8's durable fix (bucket
  resolution from runner_common's ONE split) is recorded. Marginal new work: low. Keep converting
  ad-hoc reads to framed instruments as they are touched; do not launch a sweep.
- **RECORD-DRIFT (634 BEHIND):** J1+J2 landed THIS WEEK; let the instruments work before adding
  process. The one addition worth making: the --proof-board UNPARSED rows (33 instances) get firm
  fields as their owners touch them.
- **IDENTITY/KILL instrument (S4):** the remedy candidate is already named in LD-0424 (extend the
  :94-95 self-exclusion to the single-serial path); small, owned, routed -- not a program.
- **Integrator/push concentration:** real but rare-fire; the wind-down handled it by protocol.
  Rank 1's broker-detach covers the sharpest half (the SPOF).

### WHAT NOT TO DO (the anti-list, from the estate's own law)
No monitors/alarms/SNS (moratorium -- every Rank above is a route, a read, or a consolidation). No
33-site encoding sweep (surfaced, owner-routed). No wholesale 634-record reconciliation sprint (the
advisory instrument's noise floor is by design). No new approval gates without Andrew's word --
Rank 2(b) is explicitly flagged as needing it.

---

## 3. THE ONE-SCREEN ANSWER

**Most execution risk:** the COORDINATION PLANE (delivery semantics) -- highest recurrence, still
minting new failure modes, and every other fix rides it. **Worst single blast shape:** the EXECUTING
PLANE (deployed != built-from) -- now fleet-quantified at ~12% divergent, with its gate candidate
newly unblocked by the completed census. **Costliest recent single instance:** vendor-feed detection
latency -- six trading days, remedied by an ASSIGNMENT not a build. **Cheapest future incident to
prevent:** the PRD->TO coverage seam -- the only unchecked link left in the proof chain.

Sequenced for the current program state (R-gated, 3 seats live): Rank 3 is a one-TO amendment doable
NOW at the surviving seats; Rank 1 is the deepest fix and is respawn-independent (server.py work);
Rank 2(a) consolidations queue behind R at the owning lanes; Rank 2(b) and any gate await your word.

-- 4.0.0_SA_CRO~A, 2026-08-19. Every number above is from a read taken this session or a cited
commit; the two instruments used to ground it (--proof-board, comp-state) are yesterday's J1/J2
deliverables running live.
