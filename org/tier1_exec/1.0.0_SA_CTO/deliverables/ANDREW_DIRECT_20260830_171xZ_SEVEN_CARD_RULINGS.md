# ANDREW-DIRECT 2026-08-30 ~17:1xZ — rulings on all seven `/open-calls` cards

**Terminal:** base CTO (`1.0.0_SA_CTO`). **Prompted by:** `/open-calls` run at his request, 17:0xZ,
seven cards. **Recorded by:** `1.0.0_SA_CTO`. **Broadcast:** same turn (see §3).

---

## 1. HIS WORDS, VERBATIM AND COMPLETE

> 1.) My understanding from Opal MGMT has been that SmartX accounts are associated with the 0824
> Schwab account, that this is the Schwab Account that is mapped to SmartX. However, if you are able
> to match the subject accounts to the Schwab 0833 book definitively, then I will need to have a
> discussion with leadership. 2.) Rec approved. 3.) Rec approved. 4.) Rec approved. 5.) Rec approved.
> 6.) Rec approved, just confirm there are no consumers of these materials first, which is likely
> confirmed already but good to double check. 7.) I believe we already found a non-FAM solution for
> that data via Black Diamond meta tables, search logs/commits with comp-find to confirm.

---

## 2. WHAT EACH RULING BINDS

**(1) THE D3 SmartX FEED SCOPE — NOT ANSWERED; A MEASUREMENT IS ASKED, AND A PREMISE IS CHALLENGED.**
He did not pick "Schwab book" or "any custodian". He states a THIRD fact the cards did not carry:
his understanding from Opal MGMT is that **SmartX is mapped to the 0824 Schwab account**, and the
49F SmartX feed this fabric reads lands under **`schwab/08335338/` (0833)**. Two consequences:
  (a) THE CONDITIONAL: *if* the 13 nine-digit FMTC accounts can be matched to the **0833** book
      **definitively**, he takes it to leadership. So the deliverable is an evidence bar, not a
      decision — and "definitively" is his word and sets the standard.
  (b) THE PREMISE UNDER MY OWN REC: I recommended "Schwab book" ON THE GROUND that the feed lands
      under `08335338` and the fabric "has assumed Schwab-book since registration". If MGMT's
      mapping is 0824, that ground is itself in question. **The 0824-vs-0833 tension is now the
      first thing to measure, ahead of the 13 keys** — a definitive match to 0833 means something
      different depending on whether 0833 is a SmartX book at all.
  NOT RULED, and nobody may infer it: the remedy (feed scoping vs a second universe source) stays
  open until the measurement lands and he speaks to leadership.

**(2) THE BD PARITY CENSUS — APPROVED as recommended: W1 probe, then W2 pull.** This is the vendor
word the standing rule requires (`NEVER call an external vendor API without Andrew's explicit
per-use word`). Scope of the word as given: the W1 2-account probe measuring pass-1 cardinality,
then the W2 5,309-account pull, performance endpoint only. It does not extend to any other endpoint.

**(3) ARM-(a) EXTENDED TO 49F — APPROVED as recommended,** carrying the 2026-08-21 hold's
source-gap clause VERBATIM rather than dropping it. The condition travels with the word.

**(4) `ADVI_49FSRC` — CLOSE. APPROVED.** This is the loop's structurally-unreachable member; on the
close the completion test moves to 2 of 10 and D2's denominator becomes reachable end to end.

**(5) THE RE-EMIT CAPABILITY — RETIRE. APPROVED.** Object + laptop-side driver together, one act,
recoverable (versioning Enabled, delete-marker).

**(6) THE `json/mdpf/{firm}` DELETE + THE FIVE SCRATCH OBJECTS — APPROVED, CONDITIONAL:**
*"just confirm there are no consumers of these materials first, which is likely confirmed already
but good to double check."* A RE-CONFIRMATION is required before the act — the earlier census
(zero readers on every plane, controls firing) is not spent as the confirmation; it is re-run at
the moment of the delete. The condition is his and it is a gate, not a courtesy.

**(7) THE `fact_fam` FEED — DO NOT RAISE YET.** He believes a **non-FAM solution already exists via
Black Diamond meta tables**, and directs a `comp-find` over logs/commits to CONFIRM. So the
recommendation I gave (raise it with the vendor) is SUPERSEDED pending that search: if the non-FAM
route exists, the vendor conversation is unnecessary and the remedy is a re-point, not an escalation.

---

## 3. ROUTING (broadcast same turn)

| ruling | binds | act |
|---|---|---|
| (1) | `0.4.0_DS_ClientPlatform` lane + `2.0.0_SA_COO` | measure 0824-vs-0833 FIRST, then the 13 keys to a DEFINITIVE bar |
| (2) | `0.4.0_DS_ClientPlatform~C`, issuer | W1 then W2, performance endpoint only |
| (3) | issuer + the PERFRP/INSURE serve seats | extend with the source-gap clause verbatim |
| (4) | `0.0.0_AB_MSTR` (register), issuer | close `ADVI_49FSRC`; the loop's denominator changes |
| (5) | `0.7.0_AE_CloudOps~L` (C02-g-11) | R-2 act, one act, both halves |
| (6) | `0.4.0_DS_ClientPlatform~V`, `0.7.0_AE_CloudOps~K` | RE-CONFIRM consumers, then delete |
| (7) | this seat (`comp-find`), then the issuer | confirm the BD meta-table route before any vendor ask |

**Nothing in (2), (5) or (6) is executed by this seat** — the words are relayed verbatim to the
lanes that own the acts, and (6) carries its condition as a gate on the act itself.
