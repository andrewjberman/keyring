# D1_CATVIEWS.TO-L2-DS — CERTIFICATION RECORD (AC1, AC2, AC4, AC5)

**Certifier:** `3.0.0_SA_CVO~Z`
⛔ **WRITTEN ~23:1xZ, AFTER THE CERTIFICATIONS WERE ISSUED. THAT IS A DEFECT AND IT IS DISCLOSED IN §0
RATHER THAN PAPERED OVER BY A TIDY DATE.**

---

## 0. ⛔ WHY THIS RECORD IS LATE, AND WHAT THAT MEANS FOR ANYONE READING IT

**Both certifications below were issued as BROKER MESSAGES and had NO durable carrier until now:**
```
TL2DS-AC1            certified ~21:5xZ   msgs 10334-10337   NO ARTIFACT
TL2DS-AC2/AC4/AC5    certified ~22:0xZ   msgs 10415-10418   NO ARTIFACT
```
**Found by a positive-controlled sweep of my own deliverables: `TL2DS` returned ZERO files.**

>> ⛔ **THIS IS THE EXACT DEFECT I ENFORCED AGAINST ALL EVENING — *a finding whose only carrier is a
   broker message id* — committed by the seat enforcing it, twice, on its own certifications.** <<

⭐ **AND IT IS THE SAME SHAPE AS THE CHANNEL-SCHEMA DEFECT FOUND AN HOUR EARLIER:** I wrote durable
artifacts for `POSN_TENANCY`'s decomp, `TO-2-DS`, `TO-3-AE`, `TO-4-AE` and the Andrew-direct — **and
not for the two `D1_CATVIEWS` ones.** *A practice applied to one project and not the other is not a
practice.* **Second instance tonight of a control of mine bound to part of its domain.**

⚠ **CONSEQUENCE FOR THE READER: the verdicts below are re-stated from the messages that issued them,
at the vintages named. This record does not RE-CERTIFY anything and no verdict moved in writing it.**

---

## 1. ⛔ WHAT I DID **NOT** CERTIFY — READ THIS BEFORE ASSUMING COVERAGE

**`TL2DS-AC3` IS NOT CERTIFIED BY THIS SEAT.** It was delivered before the criteria I took and I never
issued a verdict on it. ⛔ **Anyone reading *"CVO certified TO-L2-DS"* would wrongly infer AC3 is
covered. It is not.**

This matters **now**: `1.0.0_SA_CTO~Z` has ruled (~23:0xZ) that `AC3`'s structural leg — a diff at
`407e1e057b` plus a grep proving `sma_member_aum` was **never read** — **EXPIRES AT `14b077f559`**,
because the restructure's whole purpose is that `sma_member_aum` **is** now read (`:641-643`).
**Nothing in that ruling touches a certification of mine, and this record exists partly to make that
checkable rather than assumed.**

## 2. `TL2DS-AC1` — THE RULE 24 RECORD. **CERTIFIED** (~21:5xZ, instance @`41a52a8459`)

**All four postulates affirmed; (i) and (iii) re-derived at this seat.**
- **(i) MECE** — computed independently *before* the sovereign answer landed:
  `ETF{divz,idvz,pfde,pfoe}=4` · `ALT{muni,tax}=2` · union == domain(6) · uncovered `[]` · overlap `[]`.
  ⭐ **And the record names the branch on which it would have FAILED** — under the rival reading it was
  4 of 6 with `idvz`/`pfde` uncovered. **A MECE record that could not have failed is not evidence.**
- **(ii) SAME GRAIN** — the author's own catch: **the PRIOR tree violated it** (L1 values *were*
  members while `idvz`/`pfde` sat at the same level with no node). **The restructure REPAIRS a grain
  defect rather than merely avoiding one.**
- **(iii) INTENT COHERENCE** — different cuts, crossing cell `{divz, pfoe}`, one-directional
  implication. Verified against my own set computation.
- **(iv) STATE COHERENCE** — carried as a **future-input probe**: *when `idvz` later gains a
  `strategy_id`, does its bucket change? It must not.*

**`un_noded_members` dissolves BY DERIVATION** — the exact complement of the struck predicate, empty by
construction — **and Andrew's ~21:3xZ rule independently forbids an always-empty emitted key. Two
independent grounds, one answer.**

**HOMONYM VERIFIED HERE:** bare `alt` case-insensitive → **12 files** in `portal/src`; `ALT Strategies`
case-sensitive → **1**. **The naming constraint is measured, not stylistic.**

## 3. `TL2DS-AC2 / AC4 / AC5` — **CERTIFIED** (~22:0xZ, implementation @`14b077f559`)

Verified at source: `VIEW_TREE :81-82` gained the two bucket paths; `SMA_MEMBERS :307+` carries the
bucket as **registry DATA**; `l1_nodes` and `un_noded_members` **gone**.

⭐ **The certifiable principle is one line:** *SMA members now sit at their bucket path the way model
members already sat at theirs* — **which satisfies the same-pattern rule STRUCTURALLY, not
cosmetically.**

**`AC4` is NOT VACUOUS and said so unprompted:** Models L1sum `600.00 == 600.00`, SMA `100.00 ==
100.00`, **member counts exhibited** (Primary 5 / Custom 4, ETF 4 / ALT 2). **A bucket that sums
because it is empty is not a pass.**

**FINDING CONFIRMED AND BOUNDED — `D1-inv-4`'s L1-sums-to-L0 half is enforced by nothing:**
```
registry      28 raise sites, ZERO touching sum arithmetic; the :875-878 DOCSTRING claims
              "TWO PLANES, BOTH ASSERTED ... every L1 set sums to its L0 parent" and nothing raises
consolidator  3 candidates -> ALL FALSE POSITIVES (matched "L1" as a COTTONWOOD BUILD LABEL)
estate-wide   regex for assert/raise near L1+sum -> EMPTY
```
⭐ **POSITIVE CONTROL — the control EXISTS in a sibling pipeline:** `runners_49f/d04_clients_tab.py:81`
`raise SystemExit("REFUSED: clients[].aua sum != headline total_aua")`. **So this is a gap mdpf LACKS,
not one nobody invented** — and *"49F refuses on it and mdpf does not"* is a gap with a template.

**And the author's framing is affirmed:** *Models has the same gap, so I inherited it, not caused it.*
**The restructure made it visible; it did not create it.**

## 4. WHAT THIS RECORD DOES NOT DO

- **Does not re-certify.** Verdicts are re-stated at their issuing vintages.
- **Does not cover `AC3`, `AC6`, or `AC7`.** §1 is the explicit statement of that.
- ⛔ **Does not lift the `D1_CATVIEWS` NO-SHIP.** The standing criterion is unchanged: **`category_views`
  is certifiable only from a SCHEDULED run.**
