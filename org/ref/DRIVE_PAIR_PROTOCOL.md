# DRIVE PAIR — /self-drive (CTO) + /drive (COO) on one target

**Authority:** Andrew-direct 2026-08-27 at the base CTO terminal — *"if we engage a self-drive on CTO
we shoudl definitely be also instituting drive on COO tied to the same target"* + the ratifying
**"DO it get this set up"** on the presented design. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260827_DRIVE_PAIR_SETUP.md`.

**One sentence:** the CTO half SENSES and ADJUDICATES (open-calls -> rec -> CVO verdict -> own-lane
acts); the COO half ACTUATES (verdict-driven + measured-block dispatches); the coupling is an
append-only ledger, not a message.

## The verdict ledger (the coupling artifact)

**Location:** `org/{tier}/{driver_base_serial}/drive_pairs/<scope>/VERDICTS.jsonl` — the self-drive
driver's OWN agent folder (producer-owned; the consumer READS, so the pair needs zero new grants;
lane drivers use the base folder, lane-prefixed scope dirs). Append-only; committed with each tick
log under the driver's author line. `<scope>` is the selector string, filesystem-safe
(spaces -> `-`).

**Row schema (one JSON object per line):**
```json
{"ts": "<UTC>", "tick": N, "scope": "<selector>",
 "state": "VERDICT | HELD",
 "call": "<the open-call, one sentence>", "rec": "<driver's rec, one sentence>",
 "verdict": "<CVO's operative sentence, verbatim>", "verdict_msg": "<msg-id>",
 "grounding": "<file:line @ commit / tool+output the verdict cites>",
 "unblocks": [{"kind": "GO | TO-CUT | RESEAT | RECORD | NONE",
               "target": "<lane class / TO id / face path>", "note": "<one line>"}],
 "consumed": null}
```
- `state: HELD` rows are calls pitched into a DARK CVO lane (carried, not adjudicated) — a respawned
  CVO reads its backlog from the artifact, never from a scrolled message.
- `unblocks[].kind = NONE` is a legal, honest row: an adjudication that unblocks nothing still lands
  so the pair's history is complete.
- `consumed` is written ONLY by the consumer (the one field the COO half may edit): the /drive tick
  id + dispatch receipt, or `"no-act: <reason>"`. Everything else is the producer's.

**Cursor:** /drive keeps its read position in its OWN drive log (last consumed `{ts, tick}`); on lost
state it re-derives from the newest `consumed` field in the ledger itself.

## Mechanics, stated once

1. **One arming act.** `/self-drive <scope>` at CTO offers the COO half at arm time — DEFAULT YES
   when the scope has dispatchable lanes; a pure-own-lane scope may run solo (stated in the carrier).
   The operator word that arms the pair is ONE word naming ONE scope.
2. **One carrier clause** in the ARMING DRIVER's XXX.md Step 1b-F row, carrying `paired_with:
   /drive <scope> @ 2.0.0_SA_COO` (or `solo`), both cadences, and ONE stop-condition. **No tick 1
   until the carrier commit exists** — the twice-measured loss class (a 3.5h-unrecoverable COO word;
   a 29-tick-late CTO~X carrier) is closed mechanically, not hortatorily.
3. **Offset cadence:** CTO at :T, COO at :T+15 (30m default each; off the :00/:30 fleet marks).
   Pipeline, not barrier — verdicts land before the dispatch sweep reads them.
4. **The COO half's obligation is SCOPED:** unconsumed ledger rows + measured blocks INSIDE the
   scope's register predicate. Empty ledger + no in-scope blocks = a LEGAL no-op tick. This is the
   deliberate exception to /drive's all-standing-by-is-failure gate, and the reason a paired /drive
   cannot break a hold on a timer (@014de1937 class).
5. **One stop-condition, struck once:** the /self-drive §4 register-read test (or Andrew's
   stand-down). Whichever half reads it first strikes the SHARED carrier clause, CronDeletes BOTH
   jobs (its own; the peer's on the peer's next tick reading the struck clause), and both write
   final logs.
6. **The wire stays primary.** BLOCKING/ARMED items route by MCP immediately, exactly as unpaired
   operation does; the pair bounds latency for unattended windows. CVO's adjudicator independence is
   untouched — the pair changes who CONSUMES verdicts, never who renders them.
7. **Rule 27 intact on both halves:** the CTO half never dispatches; the COO half cuts TOs only from
   decomp cells; seats spawn via MSTR.
