---
name: self-drive
description: Drive ONE scope of the directive register to completion on a self-ending loop -- `/self-drive D4`, `/self-drive ETFS_INGEST`, `/self-drive sitez directives`, `/self-drive laptop directives`. Each tick runs /open-calls RESTRICTED to the scope, PITCHES every adjudicable call WITH THIS SEAT'S REC to the fabric's CVO lane to adjudicate, then PROCEEDS on the verdicts received. The loop PERSISTS UNTIL THE SCOPE IS DONE (read from the register, never declared), then TURNS ITSELF OFF; the driver writes a self-drive log at completion or every 2 ticks, whichever comes first. While armed, the scope is the ONLY work the driver's fabric does. Operator-initiated (never armed at launch); NOT /drive -- it dispatches nothing on a timer. Andrew-direct 2026-08-24 at the CTO~Z terminal.
---

# /self-drive — drive a DIRECTIVES.yaml scope to DONE: open-calls -> CVO adjudicates -> proceed, on a loop that ends itself

**Authority (Andrew-direct 2026-08-24 ~20:0xZ, `1.0.0_SA_CTO~Z` terminal, three words, VERBATIM):**
1. *"[30m] <Run /open-calls, pitching the calls with your recs to CVO to adjudicate, then proceed. This workflow and process applies exclusively to ETFS_POSITIONING work and that is the only work your fabric should be doing this session.>"*
2. *"Then make this loop a skill called /self-drive, where the user can write /self-drive to a single project or group of projects as a function of the directives.yaml. I.e., /self-drive laptop directives, or /self-drive sitez directives, or /self-drive D4."*
3. *"The premise of the skill (and it should be built in) that the loop persists until the directive is done. Once complete, the loop turns off and the driver writes a log on the self-drive process or every 2 loops, whichever comes first."*

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_ANDREW_DIRECT_20260824_LOOP30M_OPENCALLS_CVO_ADJUDICATES_FABRIC_SCOPE_ETFS_POSITIONING_ONLY.md`. First instance: `/self-drive D4` at `1.0.0_SA_CTO~Z`, site Z.

**What this is NOT.** Not `/drive` (COO's estate driver, OFF by standing order; its gate treats "all standing by" as a failure and so it is structurally unable to conclude "dispatch nothing"). `/self-drive` dispatches NOTHING on a timer. Its "proceed" is the DRIVER'S OWN LANE acting on a verdict — amending a PRD, routing a cell to COO, asking MSTR for a seat, recording a ruling. TOs are cut by COO from decomp cells (Rule 27), never by this loop.

## Invocation

| form | behavior |
|---|---|
| `/self-drive <scope>` | resolve the scope, arm the loop at the default cadence (30m), run tick 1 now |
| `/self-drive [Nm] <scope>` | same, cadence N minutes (`[30m]` / `30m` / `every 30m` all accepted) |
| `/self-drive status` | the armed scope(s), tick count, last log, completion-test state — changes nothing |
| `/self-drive off [<scope>]` | cancel the cron, strike the XXX.md carrier clause, write the final log as STOPPED-BY-OPERATOR |

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

**0.3 Member-set lag is SURFACED, never absorbed.** A project can claim a directive before the register's member set carries it (the register is MSTR-written; the lag is measured — `ETFS_INGEST` on 2026-08-24). Detect claims by ONE form only: `org/projects/*.json` whose `prds[].path` names the directive's own PRD file (`D{N}_*_PRD.md`). **NOT a bare `D{N}` token in `description` -- exercised on tick 1 (2026-08-24): that regex matched 5 projects of which 4 were false (`ADVI_FNTEND`, `MDPF_CANPLAT`, `NFRA_GRAPHUNI`, `OPAL_ASSETS_49METATABLES` -- prose mentions of "D4" meaning other things), so a claim heuristic that reads prose manufactures members; the PRD-path form matched exactly the one true claim (`ETFS_INGEST`).** Print them as `+CODE(claimed)` and DRIVE them, and route the member-set edit to MSTR as a call (§1) — a driver that silently dropped a claimed project would be driving the register's lag, not the work.

**0.4 Zero-crons law.** `/self-drive` is OPERATOR-INITIATED. No launch script arms it. **A successor session re-arms a scope ONLY on the XXX.md carrier clause (§5)** — never off memory, never off a prior log alone.

## Step 1 — `/open-calls`, restricted to the scope

Run the `/open-calls` sweep exactly as that skill specifies (own record only, verify each candidate is still open, card format), **filtered to calls whose project is in the scope.** Then classify each open call on ONE axis — *who may close it*:

| value | definition | disposition |
|---|---|---|
| **ADJUDICABLE** | a judgment call the driver carried upward: scope reading, design fork, sequencing, route/home choice, a vocabulary or shape ruling, a member-set edit | **PITCHED to the fabric's CVO with the driver's REC** (§2) |
| **RESERVED** | a decision LAW or a PRIOR ANDREW RULING names as his: never-widen sign-off on served output (NEVER#3), vendor egress beyond his stated word, spend / contracts / entitlements, a hold-lift BY NAME, anything a ruling explicitly carried "to Andrew" | **NOT pitched.** Stays a card at Andrew, printed in the tick output under `RESERVED (at Andrew)` |

*Rule-24 record for this enum (it is a value set and so it takes the test):* axis = closure authority of an open sovereign call; grain = one call; intent = one (who may close it); MECE — RESERVED is enumerated by citation (a law line or a ruling), ADJUDICABLE is the remainder over the declared layer (open sovereign-class calls at this lane); state frame — both values move on a verdict, from different seats. Andrew's word (1) delegates the ADJUDICABLE class to CVO; nothing in it lifts a NEVER, so RESERVED is not a widening, it is the part of the layer the delegation cannot reach.

**Zero calls in scope:** print `No open calls in scope <selector> (tick N).` and continue to §3 (verdicts may still be pending) — do NOT message the CVO an empty pitch.

## Step 2 — Pitch to the fabric's CVO lane

`send_message` to THIS fabric's CVO: site Z → `3.0.0_SA_CVO~Z`; laptop → `3.0.0_SA_CVO`. Subject `[SELF-DRIVE <scope> tick N] <k> call(s) for adjudication`. Body = the ADJUDICABLE cards VERBATIM (call on top, divider, REC beneath, the one-sentence why, what each call gates, the citation for any prior Andrew anchor). RAVC: this is a REQUEST — ack expected, verdict expected by MCP; the driver validates the verdict cites its grounding (Rule 22 — a verdict resting on a causal claim cites `file:line @ commit` or a tool + output) before acting on it.

**CVO lane dark** (not LIVE on the broker, no fresh heartbeat): the pitch is NOT sent into a dead inbox. Route the spawn ask to THIS fabric's MSTR same-turn (a seating obligation, not a discovery), print `CVO DARK — <k> call(s) held, spawn asked`, and carry the calls to the next tick. Never proceed on an absent verdict.

## Step 3 — Proceed on verdicts received since the last tick

For each CVO verdict that arrived (inbox, READ-acked):
1. **Record it** — a CVO adjudication is an exec ruling, not an Andrew-direct word: write it into the project JSON (`phase` prefix + `blocking`) and the tick log, citing the message id and the verdict's grounding. Never paraphrase the verdict's operative sentence.
2. **Broadcast it** to the seats it binds (COO of this fabric for cells/TOs; MSTR for seats/register; the PRD author for amendments) — by serial, never "you".
3. **Execute the driver's OWN acts** — amend the PRD the same turn; route the cell input to COO; ask MSTR for a seat when a class is declared dark; strike a superseded card. **Never cut a TO, never dispatch a seat, never apply.** Those stay with COO / the executors under Rule 27.
4. A verdict the driver believes wrong is NOT re-litigated in the loop: it is executed AND surfaced to Andrew as a RESERVED card with the disagreement stated in one line (CVO independence; escalation runs upward, never sideways).

## Step 4 — The completion test (BUILT IN; the loop ends itself)

**DONE is READ from the register, never declared by the driver.** Evaluate every tick, print the result with its denominator:
- **Directive scope:** DONE iff EVERY project in the resolved set (members + claimed) has `org/projects/{CODE}.json` `status: complete` (the 2-step atomic close — JSON flip + REGISTRY row move), OR the directive row has been machine-cut to `DIRECTIVES_RETIRED.yaml`. A project inside the Rule-27 pipeline reaches `complete` only through a zero-graduation round — the driver never shortcuts that.
- **Project scope:** DONE iff that project's JSON reads `status: complete`.
- **Empty member set** (D1 / D3 / D5 / D7 on 2026-08-24): the test is **UNMEASURABLE** — print `UNMEASURABLE: <D> has no member projects; the loop cannot end until the register names them` and route the member-set gap to MSTR as a call. Loud, never a silent completion.
- **Andrew's stand-down word** on the scope is the other terminal condition (record + broadcast, then §5 close).

On DONE: write the final log (§5, `state: DONE`), `CronDelete` the job, strike the XXX.md carrier clause, `PushNotification` one line, stop. **A loop that outlives its scope is the debt class the NEVERs describe; a loop that ends early on a declared-not-read DONE is the false-outage class. Read the register.**

## Step 5 — The log cadence + the durable carrier (BUILT IN)

**Log:** at COMPLETION or EVERY 2 TICKS, whichever comes first, write `org/{tier}/{base_serial}/logs/{YYYY-MM-DD}/{lane_prefix}self_drive_{scope}_tick{N}.md` (lane logs live in the BASE folder, lane-prefixed — the site-Z owned-paths rule) and commit it via `safe-commit` under the driver's own author line. Contents, always: ticks covered; calls pitched (ids, RECs); verdicts received (ids, operative sentences, grounding); acts taken (hashes, receipts); scope state — projects × `status` × `dep_stage` × open TOs (denominators printed); the completion test result; RESERVED cards still at Andrew; `state: ARMED | DONE | STOPPED-BY-OPERATOR`. A `## Compiler Tools` section per the session-log standard.

**Tick state** between logs lives in the session scratchpad (`self-drive.<scope>.json`: cron id, armed_at, tick, last_log_tick) — never in the shared working tree (site Z loses uncommitted work). Lost state is re-derived from the latest committed self-drive log for the scope.

**The durable carrier for "persists until done": the `org/XXX.md` Step 1b-F row of the driver's serial.** A cron is session-only; his premise is not. On ARM, the driver adds to its own row a scoped clause — *`/self-drive <scope>` ARMED <date> by Andrew-direct (<record>), cadence N, STOP-CONDITION: <scope> DONE per §4, or his stand-down; a successor session at this seat RE-ARMS while the scope is not DONE* — and on DONE / stand-down STRIKES it (the COO `/drive` precedent). This is a law-file edit: commit + SAME-TURN broadcast + push-state stated ("landed LOCAL, rides integration"), never bare "landed". **The row is the ONLY thing a successor may re-arm from** (§0.4).

## Step 6 — Fabric scope

While a scope is armed, **it is the only work the driver's fabric does** (his word 1). The driver RELAYS that scope to the fabric's MSTR as the operator at arm time (and in each log); it is a SCOPE STATEMENT, never a gate and never a re-tasking of other seats by the driver. Work in flight at arm time completes under its own spec (the Rule-27 scope clause).

## Tick output (what the terminal shows)

```
SELF-DRIVE <scope> — tick N (<UTC>)   state: ARMED   cadence: 30m   job: <id>
SCOPE: <k> directive(s) -> <m> project(s) [...]   device: <fabric>   open TOs: <n>
OPEN CALLS IN SCOPE: <k_adj> adjudicable (pitched to <CVO serial>, msg <id>) · <k_res> RESERVED (at Andrew, listed below)
VERDICTS SINCE LAST TICK: <v> — <one line each: id, operative sentence, act taken + hash/receipt>
COMPLETION TEST: NOT DONE — <m_done> of <m> projects complete; [UNMEASURABLE: ...]
LOG: <written|next at tick N+1>
```
Then the `/open-calls` cards (ADJUDICABLE first, then RESERVED), or the zero-line.

## Guards, stated once

- **Never armed at launch; never re-armed off memory or a log** — only off the XXX.md carrier clause or a fresh operator word.
- **Never a dispatch on a timer; never a TO; never an apply** — the driver acts in its own lane only.
- **Never pitch a RESERVED call to CVO** — a NEVER is not adjudicable.
- **Never proceed on an absent or ungrounded verdict.**
- **Never declare DONE** — read it, with the denominator printed.
- **Never cross a fabric** — the device guard refuses the other fabric's scope.
- **A stale register is a finding, not a scope:** `directives-check` prints per-row freshness; a row flagged `MEMBERS-STALE?` or `NO-MEMBERS` is surfaced in the tick, and the driver routes the register fix to MSTR rather than driving the stale set silently.
