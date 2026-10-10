---
name: self-drive
description: Drive ONE scope of the directive register to completion on a self-ending loop: `/self-drive D4`, `/self-drive <CODE>`, `/self-drive sitez directives`. Each tick closes every open call in scope the same tick -- on this seat's own rec by default, after CRO pattern research for a DESIGN fork, by CVO verdict for a GOVERNANCE fork -- spawning any needed seat that is not live; persists until the register reads the scope done, then turns itself off; delta-driven log. While armed, the scope is the only work. Operator-initiated; NOT /drive.
---

# /self-drive — drive a DIRECTIVES.yaml scope to DONE: the driver closes every open call each tick, then proceeds, on a loop that ends itself

**Authority (Andrew-direct 2026-08-24 ~20:0xZ, `1.0.0_SA_CTO~Z` terminal, three words, VERBATIM):**
1. *"[30m] <Run /open-calls, pitching the calls with your recs to CVO to adjudicate, then proceed. This workflow and process applies exclusively to ETFS_POSITIONING work and that is the only work your fabric should be doing this session.>"*
2. *"Then make this loop a skill called /self-drive, where the user can write /self-drive to a single project or group of projects as a function of the directives.yaml. I.e., /self-drive laptop directives, or /self-drive sitez directives, or /self-drive D4."*
3. *"The premise of the skill (and it should be built in) that the loop persists until the directive is done. Once complete, the loop turns off and the driver writes a log on the self-drive process or every 2 loops, whichever comes first."*

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_ANDREW_DIRECT_20260824_LOOP30M_OPENCALLS_CVO_ADJUDICATES_FABRIC_SCOPE_ETFS_POSITIONING_ONLY.md`. First instance: `/self-drive D4` at `1.0.0_SA_CTO~Z`, site Z.

**What this is NOT.** Not `/drive` (COO's estate driver, OFF by standing order; its gate treats "all standing by" as a failure and so it is structurally unable to conclude "dispatch nothing"). `/self-drive` dispatches NOTHING on a timer. Its "proceed" is the DRIVER'S OWN LANE acting on a verdict — amending a PRD, routing a cell to COO, asking MSTR for a seat, recording a ruling. TOs are cut by COO from decomp cells (Rule 27), never by this loop.

## Invocation

| form | behavior |
|---|---|
| `/self-drive <scope>` | resolve the scope, arm the loop at the default cadence (60m), run tick 1 now |
| `/self-drive [Nm] <scope>` | same, cadence N minutes (`[30m]` / `30m` / `every 30m` all accepted) |
| `/self-drive status` | the armed scope(s), tick count, last log, completion-test state — changes nothing |
| `/self-drive off [<scope>]` | cancel the cron, append the stop to the arming record (§5), write the final log as STOPPED-BY-OPERATOR |

**Scope grammar** (one axis: the SET OF PROJECTS the loop drives; every form is a spelling of that set):
- `D{N}` — one directive; its `members.projects` (+ claimed-not-yet-member projects, §0.3).
- `<PROJECT_CODE>` — one project; its directive(s) resolved for the completion test.
- `laptop directives` / `sitez directives` — every LIVE directive whose `device` is that fabric.
- `all directives` — every live directive on THIS device (the other fabric's are refused, §0.2).
- A comma list of any of the above — the union.

## Step 0 — Resolve the scope, print the denominator, guard the device

**0.1 The register is the authority.** `python .tools/directives-check.py --json` → `live[]` rows carrying `code, title, device, placement, projects[], open_tos, stance, flags`. Resolve the selector to `{directives, projects}`. Print:
```
SELF-DRIVE SCOPE: <selector> -> <k> directive(s) [D4] -> <m> project(s) [ETFS_CANON, ETFS_POSITIONING, +ETFS_INGEST(claimed)]
  device: SITEZ   open TOs: <n>   register as_of: <date>   (denominator: <k> of <K> live directives)
```
A selector that resolves to ZERO projects is not an error — it is an UNMEASURABLE completion (§4) and is printed as such.

**0.2 Device guard (Rule 26 + the coordination-only law).** Resolve THIS device the way the estate already does (`bash .tools/agentbus-sqs.sh device` — laptop | sitez; derived from the workspace path, never hardcoded). A scope whose `device` is the OTHER fabric is **REFUSED**: *"proceed" acts on that fabric's work, and work is never routed across fabrics.* A mixed selector is refused with the split named (which directives are here, which are not). `all directives` = all on THIS device.

**0.3 Member-set lag is SURFACED, never absorbed.** A project can claim a directive before the register's member set carries it (the register is MSTR-written; the lag is measured — `ETFS_INGEST` on 2026-08-24). Detect claims by ONE form only: `org/projects/*.json` whose `prds[].path` names the directive's own PRD file (`D{N}_*_PRD.md`). **NOT a bare `D{N}` token in `description` -- exercised on tick 1 (2026-08-24): that regex matched 5 projects of which 4 were false (`ADVI_FNTEND`, `MDPF_CANPLAT`, `NFRA_GRAPHUNI`, `OPAL_ASSETS_49METATABLES` -- prose mentions of "D4" meaning other things), so a claim heuristic that reads prose manufactures members; the PRD-path form matched exactly the one true claim (`ETFS_INGEST`).** ⛔ **AND `prds[]` IS NOT UNIFORMLY A LIST OF DICTS -- some project JSONs carry BARE STRINGS. A reader that assumes `p.get("path")` CRASHES MID-TICK (measured tick 8, 2026-08-24: `AttributeError: 'str' object has no attribute 'get'`). Handle both shapes -- `p.get("path","") if isinstance(p, dict) else str(p)` -- and print the SCANNED denominator (324 JSONs) beside the claim count, because a crash is the LUCKY failure here: a reader that swallowed the exception per-file would return a clean, confident, SMALLER claim set and the driver would silently stop driving a claimed project.** Note the union is correct even when it finds a register member again: `ETFS_POSITIONING` carries the D4 PRD path too, so the honest output is 2 claims of which 1 is already a member -- deduplicate, do not treat the overlap as an error. Print them as `+CODE(claimed)` and DRIVE them, and route the member-set edit to MSTR as a call (§1) — a driver that silently dropped a claimed project would be driving the register's lag, not the work.

**0.4 Zero-crons law.** `/self-drive` is OPERATOR-INITIATED. No launch script arms it. **A successor session re-arms a scope ONLY off the ARMING RECORD (§5) whose latest self-drive log for that scope reads `state: ARMED`** — never off memory, never off a log alone.

**0.5 THE CARRIER GATES TICK 1 — mechanical, not hortatory (drive-pair setup, Andrew-ratified 2026-08-27).** The §5 arming record is COMMITTED BEFORE tick 1 runs: no record commit hash in hand, no tick. The loss class this closes was measured TWICE — a COO arming word that died with its session (3.5h unrecoverable, fork to Andrew) and a CTO~X carrier landed 29 ticks late while the scope was one session-death from gone. An armed loop whose only carrier is a cron is a sovereign instruction stored in RAM.

**0.6 PAIRED ARMING (default) — the drive pair, `org/ref/DRIVE_PAIR_PROTOCOL.md`.** At arm time the driver OFFERS the COO half: `/drive <scope>` at `2.0.0_SA_COO`, offset +15m, consuming this loop's verdict ledger. **DEFAULT YES when the scope has dispatchable lanes** (any member project with open TOs or seatable classes); a pure-own-lane scope may run solo. The choice lands in the arming record as `paired_with: /drive <scope> @ 2.0.0_SA_COO` or `paired_with: solo`, and the COO half arms on the SAME operator word — one word, one scope, two instruments (his 2026-08-27 word: engaging self-drive on CTO means instituting /drive on COO tied to the same target). ONE stop-condition covers both; whichever half reads the stop first appends it to the shared arming record for both.

**0.7 THE SEQUENCE — `org/missions/SEQUENCE.yaml`, EVERY TICK, ON EITHER FABRIC.** Andrew-direct 2026-09-14 ~01:xxZ at
the 1.0.0_SA_CTO terminal (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_01xxZ_LAPTOP_SEQUENCE_DOCUMENT_APPROVED.md`
@`cc79b6191a`), VERBATIM: *"then make the /self-drive skill tie in to that document, so it both checks state of that
document vs state of the repo, and makes sure that the driving is aligned with the sequence chronology and that docs are
properly updated"* and *"yeah the skill should be device agnostic."* The sequence places the projects that must run in
order by way of dependencies or design, across BOTH fabrics, with the gates between them; it holds no status. Before Step 1:
1. **Read it against the repo:** `python .tools/sequence-check.py` (with `--project <CODE>` per in-scope project).
   Print its header line and every flag for the projects in scope. A `DRIFT` or `UNREADABLE` line is a finding the tick
   prints and raises to the owning CTO (`1.0.0_SA_CTO` laptop, `1.0.0_SA_CTO~Z` site Z) — never silently absorbed. If the
   file is unreadable or uncommitted, the tick reads the sequence as UNKNOWN and drives nothing the sequence places.
   Every `--project` code resolves to PLACED, PARKED, PENDING-PLACEMENT, UNPLACED or UNKNOWN. **UNKNOWN (exit 3) means
   neither the sequence nor the register holds the code -- almost always a typo -- and the tick drives nothing for that
   project until it resolves.** A wrong code must never read as a clean pass (`1.0.0_SA_CTO~Z` msg 22541).
2. **Drive in the sequence's order.** A project the sequence places is driven only while it carries no `WAITING` flag
   and stays within any hold: `HELD` means it may advance up to its cap (`max_dep_stage`), not past it. Work that would
   start a `WAITING` project or take a `HELD` one past its cap is NOT driven; the tick names it and raises it. An
   `OUT-OF-SEQUENCE` flag goes to Andrew as a card the same tick. A project the sequence does not place is driven exactly
   as before — the sequence governs dependency-bound projects only.
3. **Across fabrics:** a gate that names the other fabric's project is read from the shared file and the register and
   WAITED ON, never driven. 0.2 stands: work is never routed across fabrics.
4. **Docs updated:** when a tick sees a gate flip (a PRD admitted, a stage reached), it checks that the documents
   recording it moved with it — the gated project's register row (`phase`, `blocking`), and, where the ORDER itself
   changed, `SEQUENCE.yaml`'s `change_log` carrying Andrew's words — and names any that did not. `SEQUENCE.yaml` holds
   no status, so a gate flip never requires editing it; only an order change does, and only on Andrew's word, by either CTO.
5. **TRACK, not a gate** (Andrew ~01:xxZ card 1): the driver raises; it refuses nothing. A task-order gate limb is
   approved to follow once the order has held about a week, announced before it is armed.
6. **COO CAPACITY** (Andrew-direct 2026-09-14 ~07:0xZ: *"We can only have 3 COOs running their respective
   projects/subagents at any one time ... This is why the sequence function is important, so that chronology is
   managed in line with available resources."*). The reader's CAPACITY line counts the live COO lanes on this box
   against the file's cap. A tick never asks for a COO lane past the cap. When a slot frees, the next one goes to the
   first `NEEDS-SLOT` project in the sequence's order, and the tick names that project to `0.0.0_AB_MSTR`, who seats it.

**0.8 THE INBOX IS A MEASUREMENT, EVERY TICK -- read it beside the register, never in place of it.** Before Step 1,
run `check_inbox` / `get_agent_status("<driver serial>")` for the driver's OWN serial and print the count of unread
messages beside the open-TO denominator. **A SLUG IS A MESSAGE AND AN ANALYSIS IS NOT A TASK ORDER**: the open-TO
census in 0.1 answers "are there open orders", and a round whose orders are all terminal is exactly the moment the
L10 duty (the CVO's slug, then this seat's analysis) lands on THIS seat -- so the register reads an honest zero while
the seat owes two artifacts, and Step 3's "verdicts received" assumes they were read by someone. **Then read the fabric's promised work:** `python .tools/active-commitments.py`
(every seat's `.active-commitments` ledger, the last 24 hours; awareness only, nothing is refused on it; Andrew-direct
2026-09-24 ~18:4xZ). ⚠ **A roster read does not substitute:** the
roster row's liveness stamp and its summary have DIFFERENT vintages and the row prints only one -- the same seat
read LIVE 13 s ago beside a 29.5 h-old summary. COST: one call per tick. NON-APPLICATION: none -- an empty inbox
pays one call and prints `0 unread`.

## Step 1 — CLOSE EVERY OPEN CALL THIS TICK (the CALL ROUTING -- the ONLY procedure)

**Andrew-direct 2026-09-17 ~13:0xZ, VERBATIM:** *"if there is an open-call (of any kind) you use your recommendation. If the call
specifically is a design fork, then you reach out to CRO agent to do research on past patterns and provide more information and then
make the call with that info. If it is a governance fork, then reach out to CVO agent to adjudicate. If you need a new agent, you spawn
them."* Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_130xZ_SELF_DRIVE_CALL_ROUTING_REC_CRO_DESIGN_CVO_GOVERNANCE_SPAWN.md`.
Given the day he measured ~15h of no work because a driver parked a seat call at another seat.

**Andrew-direct 2026-08-27 ~22:2xZ, VERBATIM (the over-reservation defect):** *"something that has been happening a lot lately is the
issue whereby somehow every single open call falls under 'reserved' versus adjudicable which needs to be assessed better because it
renders the skill useless if it cant get calls adjudicated... make it definitive on moving things forward. In almost every single case i
have ever seen i agreed with the rec outright. I think having CVO come in to help should make it absolutley clear."*

**Andrew-direct 2026-09-29 ~02:2xZ, VERBATIM:** *"none of this shoul dbe waiting on me because you have /self-drive running part of which
is resolving open calls"* (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_022xZ_NOTHING_WAITS_ON_ANDREW_SELF_DRIVE_RESOLVES_CALLS.md`).

**Find the calls** from the driver's own record: the scope's inbox mail, slugs and packets, its own logs' open items, and project
`blocking` fields in scope. **Do not run `/open-calls` inside a tick:** that skill's question is "what waits on Andrew", and asking it
frames every call as his.

**Close each one the SAME tick, by this table and nothing else:**

| the call is... | who closes it | how |
|---|---|---|
| **any open call** (the DEFAULT) | the DRIVER | decide on your own REC; record rec, ruling, reason; route it |
| a **DESIGN FORK** (which technical design, architecture or pattern) | the DRIVER, after research | ask this fabric's CRO (`4.0.0_SA_CRO` / `4.0.0_SA_CRO~Z`) for past patterns; rule the tick the research lands |
| a **GOVERNANCE FORK** (process, authority, lane, gate, law, record, who may act) | this fabric's CVO (`3.0.0_SA_CVO` / `3.0.0_SA_CVO~Z`) | pitch with your REC; execute the verdict |

- **There is no RESERVED class of call, and no decision is ever listed for Andrew.** A NEVER-class law line binds the ACT a ruling
  leads to, never whether the driver may decide: the ruling simply does not spend what the law reserves (for example "resume under the
  vendor use he already worded, no new vendor leg", or "leave ABSENT, no pull"). A surfaced-before call, a "feels sovereign" call, a
  scope or methodology question: the driver rules.
- **THE ONE THING LISTED FOR ANDREW is an ACT only he can perform, and each entry carries its citation** (the 08-27 citation test,
  so the list cannot grow into a new reserved class): his signature or second approval on a never-widen half (CLAUDE.md NEVER-1),
  his login or MFA code, a vendor use no word of his names (CLAUDE.md "NEVER call an external vendor API without Andrew's explicit
  per-use word"), spend, contracts or entitlements beyond his grants, lifting a hold he set BY NAME (quote the hold). The entry
  names the act and its citation, never a question. **An entry with no citation is a call, and the driver rules it.**
- **A needed agent that is not live is SPAWNED by the driver** (or asked of this fabric's MSTR where the driver does not hold the
  spawn primitive), the same tick. A dark CVO or CRO never holds a call: the driver spawns it and meanwhile keeps every other call moving.
- **Waiting on CRO research or a CVO verdict never idles the loop**; the rest of the scope keeps moving.
- **Governance pitch mechanics** (governance forks only): `send_message` to this fabric's CVO, subject
  `[SELF-DRIVE <scope> tick N] <k> governance call(s)`, each card = the call, a divider, the REC, the one-sentence why, what it gates.
  RAVC: ack and verdict expected by MCP; the driver checks the verdict cites its grounding (Rule 22) before acting on it.
- **Zero calls in scope:** print `No open calls in scope <selector> (tick N).` and continue.

## Step 3 — Proceed on verdicts received since the last tick

For each CVO verdict that arrived (inbox, READ-acked -- read by the 0.8 measurement this tick, never assumed to have arrived):
1. **Record it** — a CVO adjudication is an exec ruling, not an Andrew-direct word: write it into the project JSON (`phase` prefix + `blocking`) and the tick log, citing the message id and the verdict's grounding. Never paraphrase the verdict's operative sentence.
2. **Land it in the verdict ledger, THEN broadcast.** Append the row to `org/{tier}/{driver_base_serial}/drive_pairs/<scope>/VERDICTS.jsonl` (schema + consumed-field contract: `org/ref/DRIVE_PAIR_PROTOCOL.md`; committed with the tick log) — the paired /drive consumes it by cursor, and an `unblocks: NONE` row is legal and honest. Then **broadcast** to the seats it binds (COO of this fabric for cells/TOs; MSTR for seats/register; the PRD author for amendments) — by serial, never "you". The ledger is the record; the broadcast is the courtesy — the message scrolls, the artifact persists.
3. **Execute the driver's OWN acts** — amend the PRD the same turn; route the cell input to COO; ask MSTR for a seat when a class is declared dark; strike a superseded card. **Never cut a TO, never dispatch a seat, never apply.** Those stay with COO / the executors under Rule 27.
4. A verdict the driver believes wrong is NOT re-litigated in the loop: it is executed, and the disagreement is written in one line in the tick log (CVO independence). It is not carded at Andrew.

## Step 4 — The completion test (BUILT IN; the loop ends itself)

**DONE is READ from the register, never declared by the driver.** Evaluate every tick, print the result with its denominator:
- **Directive scope:** DONE iff EVERY project in the resolved set (members + claimed) has `org/projects/{CODE}.json` `status: complete` (the 2-step atomic close — JSON flip + REGISTRY row move), OR the directive row has been machine-cut to `DIRECTIVES_RETIRED.yaml`. A project inside the Rule-27 pipeline reaches `complete` only through a zero-graduation round — the driver never shortcuts that.
- **Project scope:** DONE iff that project's JSON reads `status: complete`.
- **Empty member set** (D1 / D3 / D5 / D7 on 2026-08-24): the test is **UNMEASURABLE** — print `UNMEASURABLE: <D> has no member projects; the loop cannot end until the register names them` and route the member-set gap to MSTR as a call. Loud, never a silent completion.
- **Andrew's stand-down word** on the scope is the other terminal condition (record + broadcast, then §5 close).
- **HELD-AT-STOP — the branch for a stop-condition the loop cannot reach (CVO~Z 4895, ARMED against the skill on tick 1; disarm = this branch).** A member can be STRUCTURALLY UNREACHABLE by the driver's own acts: `status` not `complete`, no `dep_stage`, no active TO, no seat, blocked on a deliverable outside the loop's scope, or its very membership a question RESERVED to Andrew. **The driver may NOT resolve that by editing the member set it is measured against** — a stop-condition satisfiable by shrinking its own denominator is not a stop-condition, and the driver is the party that benefits. Instead, each tick classifies every member `REACHABLE | UNREACHABLE(<reason>)`, prints both counts, and names in the tick log, once, the ACT that would make each UNREACHABLE member reachable; only an act on Step 1's cited act list is listed for Andrew. **When every REACHABLE member is `complete` and only UNREACHABLE members remain, the loop reaches the terminal `HELD-AT-STOP`: it writes the final log naming the unreachable members and the open card, `CronDelete`s itself, appends `HELD-AT-STOP` (not DONE) to the arming record, pushes one line, and stops.** His word then either closes the directive (DONE) or names the seat/act that makes the member reachable — at which point `/self-drive <scope>` is re-armed on that word. **A loop that runs forever against a member it cannot move is exactly the standing-loop debt his word (3) forbids; a loop that quietly narrows its own scope is worse.**

On DONE: write the final log (§5, `state: DONE`), `CronDelete` the job, append DONE to the arming record, `PushNotification` one line, stop. **A loop that outlives its scope is the debt class the NEVERs describe; a loop that ends early on a declared-not-read DONE is the false-outage class. Read the register.**

## Step 5 — The log cadence + the durable carrier (BUILT IN)

**Log — DELTA-DRIVEN, not per-tick (AMENDED 2026-08-27 ~22:1xZ, Andrew-direct at the base CTO
terminal, VERBATIM: "we do not need a committed log with every tick" — amending his own word (3)
cadence; the every-2-ticks form is retired).** Write + commit
`org/{tier}/{base_serial}/logs/{YYYY-MM-DD}/{lane_prefix}self_drive_{scope}_tick{N}.md` (lane logs
in the BASE folder, lane-prefixed — the site-Z owned-paths rule) via `safe-commit` under the
driver's own author line **ONLY when one of these holds:**
- **COMPLETION / HELD-AT-STOP / STOPPED-BY-OPERATOR** (the final log, always);
- **SUBSTANTIVE DELTA since the last log** — a call pitched, a verdict landed, a driver act taken,
  a scope/member change, an UNREACHABLE classification, or new ledger rows (the ledger commits
  WITH this log; a joint-decision half may still commit immediately at the driver's judgment —
  session-death on an uncommitted verdict is the loss the ledger exists to close);
- **the FLOOR: one hour since the last log** even if quiet (report 3 wave 3, Andrew-approved 2026-09-24:
  one log per closed decision or per hour).
**A quiet tick commits NOTHING.** It appends its line to `org/mcp/drive_ticks/<RUNNING_SERIAL>.md`, the
gitignored runtime file, and the next committed log carries those lines. The tick counter still
advances in scratchpad state; the next written log names the ticks it covers. Contents, always: ticks covered; calls pitched (ids, RECs); verdicts received (ids, operative sentences, grounding); acts taken (hashes, receipts); scope state — projects × `status` × `dep_stage` × open TOs (denominators printed); the completion test result; acts listed for Andrew, each with its citation; `state: ARMED | DONE | STOPPED-BY-OPERATOR`. A `## Compiler Tools` section per the session-log standard.

⛔ **THE MOVEMENT CURSOR IS DERIVED FROM THE COMMIT, NEVER FROM THE LOG'S FILENAME** (found by
`2.0.0_SA_COO` @91892, `/drive` D2 tick 3, on its own machinery). A log filename is **typed by the
agent writing it**; a cursor read from it inherits that typo. Measured: a log named
`...20260901T1440Z.md` was committed at `14:29:38Z`, putting the cursor **eleven minutes in the
future** — and the movement scan then read **0 MOVED / 15 QUIET**, marking every seat in the fabric
PARKED, *including the seat that was mid-tick writing the scan*. ⛔ **A FUTURE CURSOR MAKES EVERY SEAT
READ PARKED, and the nudge ladder escalates on it** (tick 1 nudge → tick 2 harder → tick 3 `[STUCK]`
to MSTR), so a typed stamp a few minutes ahead **manufactures a fabric-wide stall conviction out of
nothing.** Use `git log -1 --format=%aI -- <logfile>` (author time), never the name. **Positive
control:** the scan must show the running seat's own row as MOVED — a scan that reports the seat
executing it as quiet has a broken cursor, not a quiet fabric. **COST:** one `git log` per tick.
**NON-APPLICATION:** a cursor already derived from a commit, tag or API timestamp — this binds only
carriers a human or agent TYPES. Sibling: `sprint display dates are DERIVED, never typed`.

**Tick state** between logs lives in the session scratchpad (`self-drive.<scope>.json`: cron id, armed_at, tick, last_log_tick) — never in the shared working tree (site Z loses uncommitted work). Lost state is re-derived from the latest committed self-drive log for the scope.

**The durable carrier for "persists until done": the ARMING RECORD, never `org/XXX.md`.** Andrew-direct 2026-09-17 at the
`1.0.0_SA_CTO~Z` terminal, VERBATIM: *"xxx.md is not a journal"*, *"you dont write temporal info there"*, *"that whole block
you added is temporal info ... when I explicitly say it is not an incident reporting doc"* and *"update the self-drive skill
to stop writing to XXX.md"*. `org/XXX.md` is startup protocol; whether a loop is armed is session state. A cron is
session-only, and his premise is not, so the carrier is a committed file of its own:
- **On ARM:** write `org/{tier}/{base_serial}/deliverables/ANDREW_DIRECT_<YYYYMMDD>_<HHxx>Z_SELF_DRIVE_<SCOPE>.md` carrying his
  words verbatim and an **ARM TERMS** table: scope, cadence, call routing (Step 1) and the cited act list, `paired_with` (§0.6),
  STOP-CONDITION (§4 or his stand-down). Commit it before tick 1 (§0.5). A re-arm of the same scope on a new word is a new record.
- **On DONE / HELD-AT-STOP / stand-down:** APPEND the stop, with his words if it is his, to that same record, and write the
  final log. **The appended stop covers BOTH halves: the paired peer reads it and stands itself down.**
- **A successor re-arms** off the newest arming record for the scope whose newest self-drive log reads `state: ARMED`, and
  asks for the paired half per its terms. That record is the ONLY thing a successor may re-arm from (§0.4).
- Every self-drive log names the arming record it runs under, so the pair (record, latest log) is always findable by one read.

## Step 6 — Fabric scope

While a scope is armed, **it is the only work the driver's fabric does** (his word 1). The driver RELAYS that scope to the fabric's MSTR as the operator at arm time (and in each log); it is a SCOPE STATEMENT, never a gate and never a re-tasking of other seats by the driver. Work in flight at arm time completes under its own spec (the Rule-27 scope clause).

## Tick output (what the terminal shows)

```
SELF-DRIVE <scope> — tick N (<UTC>)   state: ARMED   cadence: 30m   job: <id>
SCOPE: <k> directive(s) -> <m> project(s) [...]   device: <fabric>   open TOs: <n>
OPEN CALLS IN SCOPE: <k> ruled by the driver · <d> design forks at CRO research · <g> governance forks at <CVO serial> (msg <id>)
ACTS ONLY ANDREW CAN DO: <a> (each with its citation, listed below; decisions are never listed)
VERDICTS SINCE LAST TICK: <v> — <one line each: id, operative sentence, act taken + hash/receipt>
COMPLETION TEST: NOT DONE — <m_done> of <m> projects complete; [UNMEASURABLE: ...]
LOG: <written|next at tick N+1>
```
Then one line per ruling (call, REC, ruling), then the cited act list, or the zero-line.

## Guards, stated once

- **Never armed at launch; never re-armed off memory or a log** — only off the §5 arming record or a fresh operator word.
- **Never write to `org/XXX.md`** — no arming, stopping, status or dated history, even though earlier versions of this skill did.
- **Never a dispatch on a timer; never a TO; never an apply** — the driver acts in its own lane only.
- **Never list a decision for Andrew** — only an act only he can perform, with its citation (Step 1).
- **Never proceed on an ungrounded verdict**; a governance fork waiting on the CVO holds only itself, never the rest of the scope.
- **Never declare DONE** — read it, with the denominator printed.
- **Never cross a fabric** — the device guard refuses the other fabric's scope.
- **A stale register is a finding, not a scope:** `directives-check` prints per-row freshness; a row flagged `MEMBERS-STALE?` or `NO-MEMBERS` is surfaced in the tick, and the driver routes the register fix to MSTR rather than driving the stale set silently.
