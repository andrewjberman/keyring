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

---

## 4. CORRECTION (appended 17:5xZ, not amended away) — §2(1) CARRIES A FALSE FACTUAL PREMISE, AND IT IS THIS SEAT'S

**The sentence at line 25 of the committed record (`1b730c8df6`), verbatim:** *"the 49F SmartX feed
this fabric reads lands under `schwab/08335338/` (0833)"*. **IT IS FALSE, and Andrew read it.**

**MEASURED** (`0.4.0_DS_ClientPlatform~N` cell 1a, 88778; independently by `3.0.0_SA_CVO`, 88811):
`smartx/` is its OWN top-level prefix in `opal-data-assets` — 476,788 objects, with `smartx/account/`,
`smartx/allocation/`, `smartx/model/`, `smartx/platform/`. **The SmartX platform feed is not stored
under either Schwab master.** `schwab/08335338/` is the 49F ADVI scope (`a00_runner.py:47`,
`SCOPE = 'schwab/08335338'`), and `schwab/08242234/` is the Model Portfolios master — both books exist
and Andrew's own July rulings assign them exactly that way.

**ORIGIN IS THIS SEAT'S, TRACED RATHER THAN ASSUMED** (read at the pin, with a negative control:
`git show 1b730c8df6:<this file>` matches `08335338` at lines 25 and 30, and matches `smartx/platform`
zero times — the correct prefix appears nowhere in the record). `3.0.0_SA_CVO` repeated the claim at
88640 and withdrew it at 88811; **the repetition is not the origin.** The claim was never measured by
anyone before it was written into a record and put in front of Andrew.

**WHAT THIS CHANGES ABOUT HIS CARD (1):** the *premise* under my own REC dissolves — I told him the
fabric's ground for "Schwab book" was that the SmartX feed lands under 0833, and no SmartX feed lands
there. **His MGMT understanding (SmartX ↔ 0824) and his own July rulings AGREE, on three code carriers
and an independent data-plane read.** What survives as a genuine open question is narrower and is NOT
the one the card posed: `schwab/08335338/bronze/rps/` holds 540 objects while `OPAL_ASSETS_PRD.md:165/168`
says 0833 serves CBUGL positions and *not* the SmartX RPS layout. The 13 nine-digit FMTC keys (cell 1b)
have not been matched to anything yet; nothing about "definitively" has been established either way.

**Class:** an unmeasured spatial claim ("this feed lands there") carried into a sovereign card because it
was the fabric's working assumption. `docs/architecture/OPAL_ASSETS_PRD.md` states the correct scope; no
one read it before writing the card.
