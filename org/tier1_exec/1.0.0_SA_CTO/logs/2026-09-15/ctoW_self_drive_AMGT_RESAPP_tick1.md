# /self-drive AMGT_RESAPP -- tick 1 (arm tick) -- 1.0.0_SA_CTO~W

**State:** ARMED. **Ticks covered:** 1. **Cadence:** 30 minutes, off-minute. **Adjudicator:** this lane (Andrew ~19:3xZ).
**Carrier:** `org/XXX.md` Step 1b-F row for `1.0.0_SA_CTO~W` @`2ac5611057` (committed before this tick). **Goal:** the GOAL TEXT in
`ANDREW_DIRECT_20260915_193xZ_GOALS_CTO_W_AND_COO_W_SEE_AMGT_RESAPP_THROUGH_SELF_DRIVE_ADJUDICATE.md` @`2ac5611057`, engaged through
`/goal-set` here; the same text sent to `2.0.0_SA_COO~W` (delivered 19:41:37Z) to engage there. `paired_with: 2.0.0_SA_COO~W /goal-set loop`.

## Scope (measured)

```
SELF-DRIVE SCOPE: AMGT_RESAPP -> 1 directive [D5] -> 1 project [AMGT_RESAPP]
  device: SITEZ   open TOs: 2 (rj-10 staged, partial drain @e0c93010af, amendment 5 @4f0436811b; rj-3 staged)   (denominator: 1 of 15 live directives)
SEQUENCE: org/missions/SEQUENCE.yaml places 0 projects (AMGT_RESAPP not placed) -- driven as before; no DRIFT or UNREADABLE line
```

| project | status | dep_stage | open TOs | round |
|---|---|---|---|---|
| AMGT_RESAPP | active | EXECUTING | 2 of 13 in round 11 | 11 of 13 drained; slug not cut |

## Calls

14 open calls in scope: 12 ADJUDICABLE ruled by this lane, 2 RESERVED at Andrew with citations. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_AMGT_RESAPP_20260915T195xZ.md`. The all-RESERVED tell did not fire.
Rulings, one line each (operative sentences are in the record and the ledger):
1. Management headline = time in executive positions at the company (Bloomberg); company and current-role tenure are companions.
2. The Lusha enrich stays authorized and unused until the v3 API reference documents a no-contact request.
3. Divergence dispersion: CFPS relative scaling at 1FY, EPS fallback, proxy recorded.
4. FWD-20, a house FCF forecast with independently seeded drivers, is appended at the L10 addendum; D ABSENT until it serves.
5. Robustness eligibility by a windowed instrument; x6 latest point only; x3/x4 labelled as debt principal; model parameters unchanged.
6. Displayed percentile = the analyzed pool, deduplicated, floor 5; a labelled sector figure only at 5 or more.
7. Peers: three measure-contract fixes, FIGI resolution first, a round-12 repair of the 23 empty subjects.
8. `4.0.0_SA_CRO~W`'s broken launcher heartbeat routed to `0.0.0_AB_MSTR~Z`.
9. ADR and home listing count once by company FIGI.
10. Filing text from filings, score inputs from Bloomberg.
11. No throttle against the weekly limit; a 429 is logged with its reset time.
12. Adam's exercise of FWD-5 and FWD-7 is asked of Andrew when the page is exercisable.
RESERVED at Andrew: promote the page (PORTAL FROZEN); recurring harvest collection (mechanism and cadence reserved, PRD:831).

## Acts

The record, `drive_pairs/ctoW_AMGT_RESAPP/VERDICTS.jsonl` (12 rows, `consumed` empty), this log, one broadcast. No PRD edit
mid-round: the rulings that change the specification land in the round-11 L10 addendum after the slug.

## Completion test

NOT DONE -- 0 of 1 projects complete (AMGT_RESAPP `status: active`, `dep_stage: EXECUTING`). REACHABLE 1, UNREACHABLE 0. FWD-5 and FWD-7
are exercise-by-a-person outcomes that may end the goal HELD-AT-STOP (card 12).

## Compiler Tools

| tool | used for |
|---|---|
| `python .tools/directives-check.py --json` | scope resolution (D5 -> AMGT_RESAPP, SITEZ, open TOs 2) |
| `python .tools/sequence-check.py --project AMGT_RESAPP` | sequence read (0 placed) |
| `bash .tools/agentbus-sqs.sh device` | device guard (site Z) |
| `git log` / order `<status>` reads | round state and open orders |
| broker `get_agent_status` | live seats (COO~W, CVO~W, CRO~Z LIVE; CRO~W working, heartbeat broken) |
