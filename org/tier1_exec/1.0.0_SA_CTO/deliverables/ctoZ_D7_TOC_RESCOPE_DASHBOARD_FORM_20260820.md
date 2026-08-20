# ctoZ — D7 TO-C RE-SCOPE: intake pivots to the client-facing dashboard form (2026-08-20 ~00:5xZ)

**Authority:** Andrew-direct (record @c7aa4bb03a, MSTR~Z ferry 004536Z), load-bearing verbatim:
*"run this straight from the dashboard, no interaction with outlook emails coming in at all, we
simply have a form fill out in the dashboard client-facing."* Ticketing Center channel APPROVED
(his part 3). Gate owner: this seat (D-family ownership @550b20ec5b). Validation-lane input
adopted: COO~Z 004728Z (TAC-2' shape; §7.3 named gate; portal-build frame; color law).

## The re-scope (what changes, what survives)

| element | disposition |
|---|---|
| Intake SOURCE | **DL mail → CLIENT-FACING DASHBOARD FORM submissions.** No Outlook interaction. TO-B (laptop, shared-mailbox leg) stands down as scoped — its ferry preceded bytes; zero cost. |
| 4.2 intake loop + SLA memory + buzz format | **SURVIVE unchanged** — the duty's mechanics were never mail-specific; the source swaps. |
| Buzz channel | **The APPROVED Ticketing Center channel** (his part 3); ChannelMessage.Send consent already established per TO-A §2. |
| TAC-1 | **CLOSED fully-answered** (TO-A output stands; the DL discovery remains valid recon — it produced the question that produced the pivot). |
| TAC-2 | **WRONG-BY-PIVOT (tested a dead path). REPLACED by TAC-2':** one real CLIENT-FACING FORM SUBMISSION → ticket + buzz + link opens the board; SLA triple derivable; duty config committed on-box per the register rules. (COO~Z's validation-lane shape, adopted verbatim.) |
| TAC-3 | **SURVIVES UNTOUCHED** — the production-SCHEDULE exit (a schedule, never an alert) is source-agnostic; stays COO~Z's hold. |
| TO-C gate set | WAS: TO-B + U3/U4 + Andrew's 3 answers + WDAC acceptance. **NOW: §7.3 authz design (NAMED GATE, see below) + U3 (thread confirmed via TO-A) + the 08-20 07:00 WDAC acceptance.** TO-B is dead as a gate; U4 dispositioned below. |
| **§7.3 — THE NAMED GATE, promoted to critical path** | External submitters creating tickets END the internal-only mitigation boundary on the WRITE path. §7.3's ticket-API authorization design — which ABSORBS the 08-12 tenant-authz finding as ruled scope (@a2b93df332) — is now the form backend's critical path, and **the resolver floor stays up until §7.3 lands** (built for exactly this moment; TO-B/TO-F carry it structurally). No form write path ships ahead of §7.3. |
| U4 service-identity ruling | **STANDS AS-IS as shape law** for ANY service-identity caller of ticket-create (the five constraints are caller-shape constraints, not mail-intake constraints). Whether the form backend writes via a service subject with the client as display-grade requester (constraint 4's own shape) or via authenticated client tokens directly is **a §7.3 DESIGN OUTPUT, not ruled here**. Nothing executes against U4 meanwhile (standing rider). |
| Form build surface | **A PORTAL BUILD** — DE~Z hands precedent (D8 edit surface), routing mine at decomposition. **Silver-canvas color law + /frontend-dev render-check BINDING** — client-facing surface, the exact class the law exists for. |
| "v1 INTERNAL-ONLY" (Do-not) | **Re-read per latest-word-per-element:** the SUBMISSION surface is client-facing BY HIS NEWER VERBATIM; the notification set / board visibility stays INTERNAL per his standing positions (no bobby@ until his word). No element widened beyond his words. |

## Decomposition frame (handed to COO~Z per the split)

Three legs, sequenced: **(1) §7.3 authz design** (the named gate; absorbs T-4; owner proposal:
this seat authors the design with the D8 TO-C ruling + U4 as shape inputs, since both already
live at this gate) → **(2) the form (portal build)** — DE~Z-class hands, portal DEV branch,
color law + /frontend-dev binding, form backend BEHIND §7.3's design → **(3) TO-C duty
activation** at the box-resident Analyst against TAC-2'/TAC-3, gated on WDAC acceptance +
(1)+(2). COO~Z decomposes; spawn/census mechanics theirs + MSTR~Z's.

**Nothing lands before the 08-20 07:00 WDAC acceptance; lane commits only.**
