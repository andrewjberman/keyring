# AMGT_CORPUS -- ROUND 10 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~07:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26483, READ-acked, subject *"L10 SLUG AMGT_CORPUS round 10
@28d775c30f"*, citing `surprise-channel/adjudications/ADJUDICATION_v13.md`. Issuer packet
`deliverables/2.0.0_SA_COO~X/ROUND10_DRAIN_END_PACKET.md` @`bc50ea89cf`.

**Round 10 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

**Every served case's unit now claims only what the pack states.** The CVO read all 95 dossiers at `amgt-corpus-dossier/3`
(0 read errors): 10 carry a symbol as written; 1 sets a currency (ML_FP, EUR, where the symbol's one ISO code equals the
listing); every null names its reason. `l-1` AC3 MET. The six unreadable tables serve ABSENT with their own reason; `cases-report`
refuses an underscore key (`Z-S55`, graduated).

## 2. THE DECISIONS THE SLUG AND THE PACKET HAND ME

1. **The team-vs-rule gap (packet s.7 item 1).** Two implementations now agree: l-2 median 0.6931 team/rule over 22 names, the
   CVO's round-46 join 1.44 rule/team over 20 (1/0.6931 = 1.443), with all 8 names beyond 2x on the rule's side. **RULED: no new
   cell.** The call was already made at `CTO_RULING_RESAPP_BASE_CASE_ANCHOR_20260929.md` @`1621a80b0c`: the team's Base leads
   where one exists, and the rule's value is a "Historical-multiple reference". The corroboration confirms that ruling's
   measurement; it does not re-open it.
2. **`$` on a USD listing (the CVO's optional note, 3 names: CPA, SPOT, UNVGY) -- RULED: set USD.** The criterion's own words are
   "a currency only where the pack and the listing agree on exactly one". `$`'s ISO set intersected with a USD listing is
   exactly {USD}, so the criterion admits it; the current code requires the symbol alone to map to one code, which is stricter
   than the rule. The change can never set a currency the listing does not carry. **Cell 1.**
3. **The blank Base cell on the six tables (packet s.7 item 2) -- RULED: cut a positional read.** Read the pdf page's
   x-coordinates at extraction. Serve the value only where the position places the blank cell in exactly one column; any
   other outcome stays ABSENT with the reason already served. No arithmetic fills a cell. **Cell 2.**
4. **`Z-W2-S12` (`$` team figures on EUR listings, ORA_FP and SAP_GY) -- RULED: stays as served, row CLOSED by this ruling.**
   Whether the pack means USD is not decidable from the payload; the served unit is the symbol as written with a null
   currency and its reason. That is the honest answer, and nothing converts it.

## 3. FWD GRADES

- **`FWD-12`: NOT REALIZED -- data half MET, render half not this project's.** The team's cases are served with units that
  claim only what the pack states. Rendering them as the team's happens on AMGT_RESAPP's API (`vv-2` complete, `vv-4` redeploy
  pending) and on DSGN_AMGTV1's page (its round-2 cell 2).
- The others stand as `ROUND_ANALYSIS.round9.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 11 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **A currency where the pack's symbol and the listing agree on exactly one** (ruling 2) | intersection rule; expected CPA, SPOT, UNVGY -> USD, and no other name moves; the served move goes under a never-widen pair shared with cell 2 |
| 2 | **Positional read of the six blank Base cells** (ruling 3) | serve only an unambiguously placed value; the pair names each of the six names' two branches (placed / stays ABSENT) |

**Fan-out:** 2 cells on one dossier write surface, so one chain and one pair; LOCAL build, one served rewrite. Cap 8 not pressed.
**NOT cells:** the Base anchor (ruled); `Z-W2-S12` (closed by ruling 4).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Remove the merged worker worktrees `/c/tmp/wk-crps10-1..3`, `wk-crps7-5`, `wk-crps8-1..3`, `wk-crps9-1` if he wishes: a forced
  recursive delete [CLAUDE.md Agent Autonomy, human confirmation for recursive deletion]. Nothing waits on it.

## 6. WHAT THIS ANALYSIS DOES NOT DO

It does not close the project, moves no outcome, and does not re-open the PRD (no ENDPOINT change).

## Compiler Tools

The CVO's 95-dossier read (v13) and its census corroboration taken as measurements; the packet read at sections 3-8.
