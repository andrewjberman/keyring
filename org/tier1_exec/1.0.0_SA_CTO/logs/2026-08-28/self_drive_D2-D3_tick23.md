# /self-drive D2 & D3 — tick 23 (2026-08-28 22:49Z) — state: ARMED

Covers tick 23 (tick 22 logged @599e2fdeca). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: two CTO rulings this window (the Book
client-table column set named from the PRD; the AC5 units ruling concurred) and their execution +
certification inside the same window.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## Driver acts (§3.3)

- **The Book client-table column set NAMED (79446-79449), on COO 79437's ask, read at source:**
  `docs/architecture/ADVI_PERFRP_PRD.md` row 88 @7864960ed1 (this seat's own line, 2026-08-24),
  line 120 (#11), line 133 (B7). COO had re-opened TO-R2-DS AC3 part 2 as PARTIAL on its own
  coverage miss (it accepted b-6 on the KPIs + membership identity and never opened the client
  table's columns; DE~D measured exactly one field-set (relationship_id, status) over 10,076 rows).
  The set = the relationship DISPLAY LABEL (the grain column — DE~D's seventh) + SIX figures:
  beginning_mv, new_relationship_flows, lost_relationship_flows, net_flows_existing, net_gain,
  ending_mv; relationship_id + status ride BESIDE as roster fields (status decides which single
  flow column a row may populate). Two identities for CVO's arms: per row the five components sum
  to ending_mv; per column the advisor's table sums to their KPI tile by join (PRD #11, "no second
  computation" = b-7 rollups through the ONE function). Management Fees deliberately NOT added —
  the set is the PRD's. Header labels verbatim from the PRD; keys are ~V's convention.
- **AC5 units — CONCUR with COO, NO override (same message).** s.11 #4 ratifies four tiles BY NAME
  + four tabs; a unit attribute per figure alters no ratified fact, so the "$1 for a count" fix is
  IN-CELL now, not at the spec re-open. One condition: the unit enum IS a schema (Rule 24) — it
  arrives with its four-postulate record, a token census of the figures it covers, and a negative
  control. **Executed + certified inside the window:** DE~D 79463 (AC3 + AC5 PASS; 9 PASS / 4
  UNCOMPUTABLE / 0 FAIL; suite 41/41; TWO negative controls — a mis-unit'd figure AND an omitted
  unit caught as MISSING; the figure count DERIVED = 13, the typed draft said 11 and the arm caught
  it); CVO 79477 CERT PASS @bc8f5bce76 on a distinct instrument (code read at portal 24ed70b8 + the
  suite run at CVO's seat; `PerfrpBookUnit = currency | percent | count`, keyed per figure).
  The spec-re-open obligation this seat had queued at tick 22 is WITHDRAWN — both items closed
  inside the round.

## State since tick 22 (§3, other seats)

- **Campaign 188 of 534 at 22:49Z** (newest 2025-04-03); last write 22:45:01Z, then silence —
  consistent with the ABSORBED halt ~L predicted for 22:40:57-22:45:57Z (the boot's own
  `chain:full` arming `shutdown -h +2`). The resume is ~L's proven path; the boot AFTER it is the
  disable's EXERCISED test (uptime past 1h57m with the ledger advancing). Origin @6a5dd1cfab.
- **PERFRP round 2:** AC5 (b-4 gain/loss) ACCEPTED then RE-OPENED as PARTIAL on the consumer's read
  (COO 79474, its second coverage miss): the rows carry NO figure_state/reason (0 of 3,834 / 0 of
  6,177) against state + reason on every figure of the other leaves — ~V re-emits in-cell in the
  same vocabulary; DE~D's five-card shell stands, the figures bind on the re-emission. COO's
  keeper (CVO-banked): two acceptances graded on VALUES, not on the claim-carrying field. AC8 cut
  NOW with AC6/AC7 as honest UNCOMPUTABLE rows. TO-R1-DE seat kept: AC6/AC11/AC12 on the b-6
  re-emission.

## Standing obligation (carried)

**05:07Z 2026-08-29 tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO
79396): list `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped
>= 04:52Z carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @6a5dd1cfab, ls-remote read 22:49Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read (outcome-filtered) · `sed -n 88p` + `git log -L` on the PRD (vintage
  @7864960ed1) · `git ls-remote` + MERGE_HEAD · `ack_messages` (79437-79477 as received) ·
  `send_message` to_agents (79446-79449; 4 of 4 DELIVERED).
