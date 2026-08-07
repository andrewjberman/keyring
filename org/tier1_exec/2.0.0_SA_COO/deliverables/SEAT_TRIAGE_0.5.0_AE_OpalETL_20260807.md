# SEAT-OR-SUPERSEDE TRIAGE — `0.5.0_AE_OpalETL` (+ `~A` lane)

**Author:** `2.0.0_SA_COO`. **Date:** 2026-08-07. **Authority:** base `1.0.0_SA_CTO` 2026-08-07
(*"0.5.0_AE SEAT-OR-SUPERSEDE — YES, IT IS YOURS. Take it."*), off the governance-night state brief's
open-items list.
**Measured, not recalled.** Every count below is re-derived at this seat; the retrieval command is
named beside it.

---

## 0. THE HEADLINE, AND IT CORRECTS THE BRIEF

`FABRIC_STATE_BRIEF_20260807_FOR_BASE_CTO.md` §4 records this seat as holding *"a routed defect + 2
pending TOs incl. the July taxsma sovereign item."*

**MEASURED: 9 TOs, not 2.** `python .tools/to-check.py --all --assignee 0.5.0_AE_OpalETL` →
`total=12 projects=10 blocked=0 parse_errors=0`, of which **7 sit on the base seat** and **2 on the
`~A` lane** (the remaining 3 belong to other assignees and are excluded here).

The brief's "2" is the `~A` lane's two Andrew-direct items. **The base seat's seven were not
counted.** This is not a criticism of the brief — it is the reason a seat-or-supersede call made off
the brief alone would have been made against a denominator 4.5× too small.

**Seat darkness: 15.0 days.** Last commit `2026-07-23T15:55:54Z`
(`git log --format=%cI --author=0.5.0 -1`).

---

## 1. THE ACTUAL FINDING — THE TO SURFACE WAS NEVER RECONCILED AGAINST ANDREW'S 2026-07-30 RULINGS

Three of these nine TOs order work that **Andrew deprecated by direct word eight days ago.** The
rulings were recorded and broadcast correctly; **nobody swept the TO surface against them.** A dark
seat hid that, because nothing was executing them to trip over the contradiction.

> **Andrew-direct 2026-07-30 ~1730Z, VERBATIM:** *"49F Converter ops are all deprecated, that is a
> skill off main chain for schwab data now. We are doing this because a lot of these resources are
> surely deprecated and I want to clean it all up."*
>
> **Andrew-direct 2026-07-30 ~1920Z, VERBATIM:** *"I dont care about any of these crawl functions,
> all of it can go."*

**This is the generalizable part: a deprecation ruling lands on the ESTATE and nobody points it at
the TO SURFACE.** A TO is a standing instruction to a seat; a ruling that kills the work does not
retract the instruction. The two live in different places and only a sweep joins them. When the seat
is dark the contradiction is invisible — and when the seat is *respawned* it would have executed
deprecated work with a valid-looking TO in hand.

---

## 2. PER-TO DISPOSITION — recommendation only, nothing executed

⚠ **NOTHING IS CLOSED BY THIS DOCUMENT.** No silent closes (MSTR ruling, 2026-08-06 on the
five empty-chair TOs). This is a recommendation set for MSTR + CTO; the sovereign items are Andrew's.

### BASE SEAT — 7

| # | TO | Age | Recommendation |
|---|---|---|---|
| 1 | `ETFS_SETUP.W2` — 49F silver/RPS producer | 45d | **SPLIT — partially superseded.** Step 1 (*"build the /49-schwab-conv RPS converter"*) IS the converter ops Andrew deprecated. Steps 2–3 (register the canonical thread; the 49F daily ETF-ownership producer writing `opal-data-etfs/49financial/{date}.json`) are ETFS work and **NOT** covered by that ruling. ⛔ Do NOT blanket-close: ETFS has a live month-end trigger (next fire SEP-1) and an **open ETFS CANON question already at Andrew**, so the forward path is entangled with a decision he holds. |
| 2 | `DATA_PLATFORM.DC1` — Orion post-auth crawl | 44d | **SUPERSEDED — close.** Objective verified verbatim: *"Comprehensive enumeration + characterization of Orion's endpoint surface via the DC0 harness post-auth crawl."* That is a crawl function. Already independently known-orphaned ("among 8 orphaned TOs from dead COO seats, CTO-frozen pending post-walk triage"). **I issued this TO (2026-06-24); closing it is my own residue, not someone else's.** |
| 3 | `DATA_PLATFORM.DC2` — Eclipse crawl | 44d | **SUPERSEDED — close.** Same ruling, same class, same issuer. |
| 4 | `NFRA_OPLMCP.08` — read-only Teams-read tools on the M365 gateway | 44d | **KEEP, but RE-BADGE and RE-SEAT.** Andrew renamed this vertical `m365-mcp` → **`opal-mcp`** on 2026-08-06 (*"it will have more than just m365 and we've already evolved that"*). This TO names the old vertical. It also **interlocks with the teams-watch dual-identity durable fix** routed to this dark seat — same surface, and that defect is currently session-mitigated only. |
| 5 | `NFRA_INTEGRATIONS.P3` — storage dependency / firm-sep schema | 36d | **RE-SEAT.** No superseding ruling found. |
| 6 | `NFRA_TERRAFORM.TO-1` — P1 coverage assessment (read-only) | 30d | **RE-SEAT.** Read-only assessment; still `staged`, never started. |
| 7 | `NFRA_TERRAFORM.TO-2` — P2 remediation | 30d | **RE-SEAT, behind TO-1.** Remediation against a coverage assessment that has not run. |
| — | `NFRA_EDGES.P4` | 30d | **Already correctly dispositioned** — its own status line reads *"SCOPED OUT of NFRA_EDGES core; tracked as an NFRA_PROMOTE extension."* No action; listed so the denominator is complete. |

### `~A` LANE — 2, BOTH SOVEREIGN, NEITHER MINE TO CLOSE

| # | TO | Recommendation |
|---|---|---|
| 8 | `ANDREW_DIRECT_20260714` — TAXSMA + Opal Ticket System scoping | **ANDREW'S CALL.** Issued by *"Andrew (sovereign, direct terminal prompt)"*, `pending` since 2026-07-14 — **24 days**. A COO does not close a sovereign item, and I am not going to recommend one be closed for age. |
| 9 | `ANDREW_DIRECT_20260715` — UIUX centralization + TAXSMA intake guarantee | **ANDREW'S CALL.** Status `executing` on a seat that has been dark 15 days — so the status is **stale, not true**. That is worth him knowing regardless of what he decides. |

---

## 3. RECOMMENDATION — the seat call itself

**SUPERSEDE THE BASE SEAT'S BACKLOG, DO NOT RESPAWN `0.5.0_AE_OpalETL` TO CLEAR IT.**

Reasoning, stated so it can be argued with:
- Of 7 base-seat TOs, **2 are dead** (DC1/DC2), **1 is half-dead** (ETFS W2), and **4 are live but
  none is time-critical**. Respawning a seat to work a backlog that is 43% deprecated spends a seat
  on cleanup that a sweep does more cheaply.
- The **live** remainder (OPLMCP.08 + the teams-watch fix, NFRA_INTEGRATIONS.P3, NFRA_TERRAFORM
  TO-1/TO-2) is **AE-lane work with no 0.5.0-specific knowledge dependency** I can find. It re-seats.
- ⛔ **BUT NOT TODAY, AND NOT ONTO `0.7.0_AE_CloudOps`.** That is the only free AE seat on this
  device and base CTO is already deciding between **two** candidate jobs for it (B6 capture uploader
  vs the globgrph item-5 deploy leg). Adding a third would be the "give it everything and call that
  a plan" shape the CTO explicitly named and refused. **This backlog waits for an AE seat that
  exists.**

**The two sovereign `~A` items do not re-seat and are not mine.** They go to Andrew as a call, with
the honest note that one of them has read `executing` for 15 days on a dead seat.

---

## 4. WHAT I DID NOT DO, AND WHY

- **Did not close DC1/DC2**, though they are mine and superseded — no silent closes, and a
  supersession that is right today is still a record other agents read tomorrow. It goes through
  MSTR.
- **Did not touch the `~A` sovereign items** in any way.
- **Did not re-badge OPLMCP.08** to `opal-mcp` — the rename was routed to `3.0.0_SA_CVO`, whose lane
  owns the canonical files; me editing it here would be a second writer on a rename already in
  flight.
- **Did not verify the 07-30 rulings against live AWS state.** They are Andrew's words about intent,
  not claims about resources; nothing here rests on what is currently deployed.
- **Did not sweep the whole TO surface for other deprecation-vs-TO contradictions.** §1 says the
  class is general and I found it on one seat. **That sweep is unowned and I am naming it as
  unowned rather than quietly assuming this seat was the only instance.**

---

## 5. THE ONE THING WORTH TAKING FORWARD

A TO is a standing instruction. **A ruling that kills the work does not retract the instruction —
they live on different surfaces and only a deliberate sweep joins them.** Eight days and one dark
seat were enough for three contradictions to accumulate unseen. This is a **gate CANDIDATE, proposed
not implemented** (Andrew 2026-08-06: no gates unless he asks): at deprecation-ruling time, sweep the
TO surface for TOs whose objective names the deprecated thing, and surface the hits. Routing that is
CTO's call, not mine to build.
