# AMGT_HARVST ROUND 17 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~13:2xZ
**Input:** `2.0.0_SA_COO~H`'s `round17/ROUND17_DRAIN_END_PACKET.md` @`8cb1f2ec40` (read to EOF, 5,728 B), msg 26593.
**L7 RE-MEASURED not adopted:** `f-1` and `f-2` read `complete` on their LAST `<status>` tag; 1 judgment criterion (`f-1` AC4).

---

## 1. L8 -- THE CHANNEL COMPILE, AND `Z-W40-S1` MEASURED

`_latest_dispositions`: **103 items, 21 UNDER_INVESTIGATION**, which reproduces the packet's fold.

**`Z-W40-S1` (ARMED since round 14) -- GRADUATED on this seat's own runs of `f-2`'s checks:**
- `ac3_fixture_mechanism.py`: variant 1 (the story is the security's only coverage), **old rule 0 events, new rule 1 event** (09-10..09-11,
  4 articles). The stripped stems fall from `['batter', 'plant', 'quantu', 'zorbex']` to `['zorbex']`, so the story's own words stay
  linkable. Variant 2 is unchanged. **The planted two-story control stays 2 events**, so the fix does not over-merge.
- `ac2_served_events_unmoved.py`: every served event is **row-equal on 13 fields** under the new rule, and **0 of 29** securities' stripped
  name stems change.

**CARRIED:** `Z-S37`, `Z-W39-S1`, `Z-W41-S1` (as before). `Z-W43-S1`/`-S2`/`-S3` and `Z-W44-S1` are INERT notes. `Z-W44-S1` matters the moment
round 18 adds aliases.

## 2. L9 -- `f-1` AC4: "per form, how many of the sampled hits are the company?"

All **531** sampled hits over the 113 form blocks were read in context. The first pass was a subagent working to a stated rubric,
YES / NO / UNSURE per hit. **This seat then re-read a spread of its calls against the file** (C, COST, NU, UBS, V, Coca-Cola, United, Ford,
Singapore) and agrees with every one. It found one call borderline: "a white Ford Econoline van" names Ford's product, not coverage of
Ford. **0 UNSURE.**

| class | hits | the company | rate |
|---|---|---|---|
| **T1 ticker** | 240 | **172** | 72% |
| **B1 short name** | 291 | **61** | **21%** |
| all | 531 | 233 | 44% |

### What the read says the rule must be -- the three levers the packet asked for

**1. CASE-SENSITIVE for tickers -- decisive.** Most ticker false hits are lowercase words: `NOW` 0 of 10, `T` 0 of 10 (the "t" of "don't"),
`COST` 4 of 10, where **the 4 are exactly the upper-case "( COST )" hits and the 6 misses are lowercase "cost"**, and `FIX` 0 of 6.
Mixed-case forms fail the same way: "El Paso" for `EL`, "Alani Nu" for `NU`. By this seat's count of exact-case hits, **a case-sensitive
ticker match at 2+ characters keeps about 157 of 162 hits correct, ~97%.** The residual false hits are other products or companies in
upper case: Nvidia's "RTX Spark" for `RTX` (4), "ST Telemedia" for `ST` (1).

**2. A LENGTH FLOOR OF 2 -- decisive for single letters.** Every one-letter ticker fails even when the case matches. `C` 0 of 10 (letter grades
"C-", "C+"), `F` 0 of 10 ("F-15", "F/A-XX", a grade), `V` 1 of 3 ("N.V.", "V-8"), `T` 0 of 10. Two-letter tickers pass: `BA` 10/10,
`HD` 9/9, `KO` 5/5, `MU` 3/3.

**3. SHORT NAMES (B1) ARE UNSAFE AS A CLASS -- adopt only whole-brand names, by list.** 21% overall. Generic leading words fail wholesale:
`Bank` 0/28, `American` 0/20, `United` 0/20, `General`, `National`, `International`, `State`, `Union`, `Home`, `Best`, `Advanced`,
`America`, `China` all 0/10, and `Texas` 0/9. **B1 passes only where the first word IS the brand:** `Dell` 10/10, `TJX` 9/9, `UBS` 7/7,
`ASML` 6/6, `Micron` 5/5, `Uber` 5/5, `Spotify` 3/3, and `Meta`, `eBay`, `SAP`, `QXO` at 100% on small samples.

⭐ **A B1 CLASS THE CENSUS'S OWN FLAGS CANNOT SEE: PARENT vs LOCAL SUBSIDIARY -- 0 of 18.** The short name of a local listing is its
parent's brand. `Walmart` for WALMEX* (Walmart de México) hits US Walmart, 0/10. `Coca-Cola` for KOF (Coca-Cola FEMSA) hits The Coca-Cola
Co, 0/7. `Kimberly-Clark` for KCDMY hits the US parent, 0/1. No dictionary flag or length floor catches these. **They attribute the
parent's coverage to the subsidiary**, which is worse than a missed mention: it is a wrong one.

**VERDICT: the read supports a T1 rule of case-sensitive, length >= 2** (about 97% of kept hits correct on this sample). It rejects B1 as a
derived class: only an explicit per-security list of whole-brand names should enter, never a first-word derivation. And a brand source
("Google" for Alphabet) still does not exist in the estate, as the packet says.

⚠ **BOUNDS:** the sample is up to 10 hits per form (seed 20260929), not every hit. The ~97% is this seat's arithmetic over the exact-case
subset (185 exact-case T1 hits, minus the 23 of the one-letter tickers C, F and V, gives 162; minus 5 known false = 157), not a
separately graded census. The per-hit first read was a subagent's under a stated rubric, spot-checked by this seat, not a hit-by-hit
re-read of all 531.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-W40-S1` GRADUATED on measurement; `Z-S37`, `Z-W39-S1`, `Z-W41-S1` CARRIED. **MET**
3. **Every judgment criterion graded** -- 1 of 1. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S35",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T13:25:00Z",
    "one_line": "L9 round 17: of 531 sampled hits, tickers are the company 172/240 and short names 61/291. The read sets round 18's rule: tickers case-sensitive at length >= 2 keep ~97% correct (COST's 4 true hits are exactly its upper-case ones; C, F, T are letter grades, aircraft and contractions); short names fail as a class except whole-brand names (Dell, TJX, UBS, ASML, Micron, Uber, Spotify). A parent-vs-subsidiary class misattributes wholesale (Walmart for Walmex, Coca-Cola for KOF: 0 of 18). Z-W40-S1 graduates on this seat's fixture and served-arm runs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: HVST-f-1 and HVST-f-2 read 'complete' on their LAST <status> tag; judgment=\"true\" on f-1 AC4.",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') 103 items, 21 UNDER_INVESTIGATION; ARMED Z-S37, Z-W39-S1, Z-W40-S1, Z-W41-S1.",
        "Z-W40-S1, this seat's run of ac3_fixture_mechanism.py: 'OLD rule: stripped name stems=[batter, plant, quantu, zorbex] ; 0 event(s)' / 'NEW rule: stripped name stems=[zorbex] ; 1 event(s)'; 'CHECK variant 1 ... -> OK', 'CHECK variant 2 ... -> OK', 'CHECK control: the two stories do NOT merge; new rule forms 2 events ... -> OK'. ac2_served_events_unmoved.py: 'row-equal ... (13 fields)' per served event; 'securities whose stripped name stems changed: 0 of 29'.",
        "L9: ac4_output.txt (998 lines) parsed into 113 form blocks and 531 hits; T1 240, B1 291. Per-hit read: T1 YES 172 NO 68; B1 YES 61 NO 230; 0 UNSURE.",
        "Spot-checked by this seat against the file: C ('Valuation Grade C-', 'got a C in momentum'); COST ('low-cost', 'The cost of screwing up' vs 'Costco's (COST US)', 'Costco Wholesale ( COST )'); NU ('Alani Nu' vs 'Nu Holdings (NYSE: NU )'); UBS ('an analyst at UBS'); V ('Nebius Group N.V.' vs 'Visa ( V )'); Coca-Cola under KOF ('Coca-Cola ( KO )'); United under UAL ('Atlanta United', 'United Kingdom', 'United Parcel Service'); Ford ('a white Ford Econoline van'); Singapore ('Singapore Telecommunications' vs the country).",
        "Exact-case T1 subset: 185 hits; excluding the one-letter tickers C (10), F (10), V (3) leaves 162, of which the known false are RTX 'RTX Spark' (4) and 'ST Telemedia' (1) -> about 157 correct.",
        "Parent/subsidiary: B1 'Walmart' (owner WALMEX*_MM_Equity) 0/10, all US Walmart; 'Coca-Cola' (owner KOF_US_Equity) 0/7, The Coca-Cola Co; 'Kimberly-Clark' (owner KCDMY_US_Equity) 0/1, the US parent."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W40-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @8cb1f2ec40 asserts 2 orders terminal and VALID, Z-W40-S1 fixed in code with the 8 served events unmoved, and a read-only census whose 531 sampled hits are presented for the per-form judgment.",
    "world_is": "True as re-run. The judgment supports a case-sensitive ticker rule at length >= 2 and rejects derived short names except by an explicit whole-brand list. Parent-vs-subsidiary short names attribute the parent's coverage to the local listing, 0 of 18 correct.",
    "notes": "FOR THE ROUND-17 ANALYSIS (the alias rule is the CTO's): (1) T1 tickers: case-sensitive, length >= 2, with an explicit refusal list for known collisions (RTX with Nvidia's RTX products; ST); (2) B1: no first-word derivation; admit only a per-security list of whole-brand names, and never a parent's brand for a subsidiary listing; (3) when the new forms land, re-read Z-W44-S1 on the served events, as the packet says."
  }
]
```
