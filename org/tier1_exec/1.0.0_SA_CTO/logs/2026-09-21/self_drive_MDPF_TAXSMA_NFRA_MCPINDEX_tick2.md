# /self-drive tick 2 -- `MDPF_TAXSMA`, `NFRA_MCPINDEX`

**Seat:** `1.0.0_SA_CTO` · laptop · CLOUD · **UTC** 2026-09-21 ~02:3xZ
**Arming record:** `deliverables/ANDREW_DIRECT_20260921_005xZ_SELF_DRIVE_RESCOPED_MDPF_TAXSMA_NFRA_MCPINDEX.md` @`07b8a03ec3`
**State:** ARMED · cadence 30m · job `852cc1e2` (re-cut this tick, §6)

---

## 0. HEADER FIGURES -- EACH PRODUCED BY A CALL IN THIS TICK

| figure | value | the call, this tick |
|---|---|---|
| device | laptop | `agentbus-sqs.sh device` (basis: workspace path) |
| projects in scope | 2, both **PLACED stage 0** | `sequence-check --project` x2 |
| sequence flags in scope | **0** | same, `FLAGS (denominator 1 projects): none` x2 |
| live COO lanes / cap | **4 / 3 -- OVER CAP** (`~B ~M ~O ~T`) | `sequence-check` CAPACITY, off `liveness.json` |
| orders, `MDPF_TAXSMA` | **27** (25 non-terminal) | `git ls-files task-orders/` -- **hyphen**, §9.1 of tick 1 |
| orders, `NFRA_MCPINDEX` | **0** | same |
| positive control | **33** (`NFRA_OPLGTW`) | same call -- **a zero gets a control now** |
| my unread inbox | **0** | `ls` on my inbox slice top-level (⚠ §5) |

## 1. ⭐⭐ THE FINDING: A DISPOSITION THAT LIVES WHERE NO GOVERNANCE CARRIER CAN SEE IT

`3.0.0_SA_CVO` (`98909`) answered the question `98896` routed to it, and answered it well: **no CVO L9
adjudication of `OG-r-1` exists** -- `0 hits across 1952 files`, with a **101-hit positive control on the same
scope and instrument**, and its own bounds printed (4 binary + 55 ephemeral-floor files unread, not claimed).
It concluded `TX-r-2` stays held because AC10's adjudication "does not exist in any carrier, mine or yours."

**It does exist. Measured at HEAD, bold in the source:**

> `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md:252` --
> **"For the release currently live (`NFRA_OPLGTW.TO-OG-r-1`, deployed_commit `1764e54a16`): this release has
> NO VALID ROLLBACK under this section."**

**THE CHAIN, each link read:** R-56 item 2 (**my own** round analysis, `97864` @`853a37edd1`) ruled the
restorability standard → the order's grant amended **§7.2 only**, *"in the words R-56 item 2 requires"* → **the
amendment is at HEAD** → `NFRA_OPLGTW-W2-S7` stays ARMED for the residual.

⭐ **THE KEEPABLE: A DISPOSITION CAN LIVE IN THE OPERATOR'S OWN ARTIFACT RATHER THAN IN A RULING, A ROW OR A
PROOF -- and every governance carrier two seats searched is STRUCTURALLY BLIND TO IT.** The CVO searched its
deliverables tree; I read the proof instance and the surprise row. **The runbook is where the disposition does
its WORK, which is exactly why it was the last place either of us looked.** ⚠ And the criterion NAMED it the
whole time: AC10's own verbatim reads *"restorable by **the runbook's rollback section**"*.
**COST: one read of the artifact the criterion names. NON-APPLICATION: a criterion naming no external artifact.**

## 2. ⛔ TWO ERRORS OF MINE IN `98896`, CORRECTED AT `98910`

**(a) WRONG LOCUS.** I wrote the exclusions were *"adjudicated at L9 by `3.0.0_SA_CVO`, never self-graded."*
No such document exists and the CVO proved it. The adjudications are **R-56 items 2, 3 and 4 -- MINE, at L10.**
A read-back sent hunting a CVO L9 would have hunted a document never written, and a freshly-seated lane would
have burned a turn on it.

**(b) ⛔ OVERSTATED NOVELTY -- the worse one.** I called the rollback gap *"the most consequential thing in
this message"* in language that reads as UNDISCOVERED. **It was discovered, ruled on by me, disclosed in the
runbook and ARMED as a row, all on 2026-09-18.** The FACT was right; the FRAMING implied nobody knew, and it
would have had `2.0.0_SA_COO~O` re-discover finished work.

⭐ **THE TELL I HAD AND DID NOT USE: I was reading `declared_exclusions` -- a field whose ENTIRE PURPOSE is to
say "this was considered" -- and I treated its PRESENCE as evidence of a gap instead of reading what it
POINTED AT.** A field that exists to record a disposition is the worst possible thing to read as an omission.
**COST: one dereference. NON-APPLICATION: an exclusion whose pointer is empty.**

## 3. THE G-O GATE: INPUT NOW EXISTS; THE GRADE IS NOT MINE

The read-back is **producible with every disposition citable** -- `OG-r-1` complete @`be38a0f475` under the
order's own amended flip bound (R-58 item 1: terminality read from the PROOF,
`.tools/surprise-row-gate.py:820-824` `_proof_terminal`); AC4 FAIL disclosed (R-56 item 3, cause
`core.autocrlf` in the deploying worktree, residual ARMED as `W2-S8`); AC9 N/A-BY-CONSTRUCTION (R-56 item 4);
AC10 FAIL with the gap disclosed at `runbook:252` (R-56 item 2, residual ARMED as `W2-S7`).

⚠ **WHETHER THAT SATISFIES `TX-r-2` IS READ AT THE CELL BY `2.0.0_SA_COO~T`.** I state the gate's INPUT
exists; I do not grade the cell. AC10's failing leg is 1 of 5 checks (`restricted_profile_denial_present`
False); **the content-hash mechanism itself verified CLEAN** -- recorded == read-back at `1556d6e979`.

## 4. ⛔ MY ORDER CENSUS SAID 3 OPEN; THE CVO'S RESOLVER SAID 2. THE CVO IS RIGHT

`OG-r-2`'s `<status>` is **a ~300-word PARAGRAPH** beginning *"superseded -- CLOSED for round 1 by
`2.0.0_SA_COO~O` ..."*. My terminal-word test compares the whole field against a word list, so a terminal
order read as open. **A FREE-TEXT `<status>` DEFEATS AN EXACT-MATCH TERMINAL-WORD TEST** -- the documented
roster trap (`get_agent_status` exact-matches a free-text `<status>`) **arriving in a second, unrelated
instrument, which is what makes it a class rather than a quirk.** The population is **2**: `OG-v-4` and
`OG-v-5`, both to `0.9.0_WK_NFRA_OPLGTW~6`, held on G-C/G-D and G-E/G-F.

**`98909` §4's contradiction, RESOLVED:** the re-seating scopes **THE LANE** to two acts; it does not close
**THE PROJECT** and disposes none of its orders. `OG-v-4`/`OG-v-5` are **not among the two acts and are not
driven by this loop** -- open and unowned-in-this-loop until Andrew re-arms the project. Named so no seat meets
it as a contradiction and **no seat quietly adopts them.**

## 5. OPEN CALLS IN SCOPE, AND THE COMPLETION TEST

**Open calls in scope: 0 adjudicable, 0 reserved.** The four carried calls are out-of-scope projects and one
(`NFRA_OPLGTW` seating) was ANSWERED at ~01:4xZ. Every call this tick raised was decided by this seat the same
tick, per the routing directive. **No empty pitch sent to the CVO.**

**COMPLETION TEST -- NOT DONE: 0 of 2 projects `complete`.** `MDPF_TAXSMA` `status: scoping`, `dep_stage
EXECUTING`; `NFRA_MCPINDEX` `status: active`, `dep_stage PRD`. Both REACHABLE (each has a live lane and a
signed PRD); **0 UNREACHABLE**, so `HELD-AT-STOP` does not apply.

⚠ **INSTRUMENT DEGRADED, DISCLOSED:** `get_agent_status("1.0.0_SA_CTO")` returned **208,705 characters** and
was refused by the harness as over-limit, so §0.8's prescribed inbox call did not run. I substituted a
directory read of my own inbox slice (`0` at top level). **That substitute sees the filesystem queue and NOT
the broker channel**, so the `0` is narrower than the figure §0.8 asks for and is printed as such rather than
as a clean zero.

## 6. ACTS TAKEN THIS TICK

- `98910`-`98913`: the AC10 chain, both corrections, the `OG-v-4`/`OG-v-5` resolution. 4 DELIVERED / 0 QUEUED.
- **Cron re-cut `9d314499` → `852cc1e2`.** ⛔ **My own loop prompt carried a STALE INSTRUCTION I had already
  corrected in public:** it said *"L6 belongs to `2.0.0_SA_COO~T`"* when L6 was done and that lane is at L7.
  **A recurring prompt is a carrier, and correcting a broadcast does not correct the thing that will re-issue
  the error every 30 minutes.** The new prompt carries the measured stage, the hyphen-path rule, the
  positive-control rule and the two-act `NFRA_OPLGTW` scope. ⭐ **A LOOP'S OWN PROMPT AGES LIKE ANY OTHER
  CITATION, AND NOTHING RE-READS IT.** COST: one `CronDelete` + one `CronCreate` per corrected fact.
  NON-APPLICATION: a prompt carrying no state.
- **No TO cut, no seat dispatched, no apply.** L5 is `2.0.0_SA_COO~M`'s, L6/L7 `2.0.0_SA_COO~T`'s, the two acts
  `2.0.0_SA_COO~O`'s.

## 7. STATE AT TICK END

| project | status | dep_stage | lane | orders | next act, and whose |
|---|---|---|---|---|---|
| `MDPF_TAXSMA` | scoping | EXECUTING | `~T` | 27 (25 open) | L7 execution + drains -- **`~T`'s** |
| `NFRA_MCPINDEX` | active | PRD | `~M` | 0 | L5 decomp -- **`~M`'s** |

**Push state: LOCAL ONLY** -- `b103d875e1` was my latest before this log; `ls-remote` read at send time. Only
`0.0.0_AB_MSTR` pushes CLOUD. **Next tick :41.**

## Compiler Tools

`sequence-check.py` (x2, per-project), `agentbus-sqs.sh device`, `git ls-files` over `task-orders/` (x3, one a
positive control), `git show HEAD:<order>` with `encoding='utf-8'` after a cp1252 decode crash, `comp-find`
(x2: `'R-56 item'` 30 hits / 230 files; `'NO VALID ROLLBACK...'` 2 hits / 1 file), `json.load` over the
`OG-r-1` proof instance, `get_live_agents`, `get_agent_status` (**refused, over-limit -- §5**).
