# DSGN_AMGTV1 -- ROUND 11 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~09:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27066, *"L10 slug DSGN_AMGTV1 round 11 @0f865ae7bb"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v13.md` (read to EOF, 8,477 B). Issuer: `round11/DRAIN_END_READ.md` @`44844e4895`
(msg 27059) and `ROUND11_CLOSE_WALK.md` (walk K, 432 shots, 54/54 loads).

**Round 11 is CLOSED:** 6 of 6 orders terminal, rows dispositioned, 6 of 6 judgment criteria graded. **The project is NOT
closed.** PRD v0.4 (@`03912f9462`, signed) adds FWD-12..FWD-20, and they enter at round 12.

---

## 1. WHAT THE ROUND DELIVERED (the CVO's L9, on shots it opened itself)

- **n-1 MET:** the qualifier leads an unresolved figure ("unit not resolved -- raw figure ...").
- **n-2 MET:** filing evidence reads as filing evidence, and the team's pack keeps its source.
- **n-4 MET:** 6501 JP opens loaded with "no research dossier for this name". `Z-C-S13` graduates, and the no-dossier arm the
  CORPUS outcomes needed is now exercised.
- **n-6 MET:** each input's source, last run, outcome and "no lone re-run". The CVO falsified the one way it could be false
  (later versions carry the same `raw_stamp_used`).
- **n-3 PARTIAL:** BA's DENIED day is truthful. **992 HK 08-13 is not:** covered `[bbg]`, 2 articles from wsj and sa, and the page
  reads "Searched: a publisher this page has no name for yet -- 2 found".
- **n-5 NOT MET:** what moved is readable, but the earlier version is not nameable. BA's picker offers four identical "September
  10th, 2026" entries over four served stamps.

## 2. RULINGS

1. **n-3 is closed by the contract signed today, not by new page wording.**
   - HARVST PRD v0.4 `C-HV-COVERED-VS-FOUND` (@`624bc0f4ca`) defines the two sets.
   - HARVST round-27 `q-5` serves `publishers_found_codes` in code. It is served once a `chatter_daily` rebuild and a deploy carry
     it.
   - **The page renders a publisher in the FOUND set but not the COVERED set as "found, listing not run".**
   - Where the field is absent (a part written before the column existed), the page says the day's search record does not say how
     the articles were found. It never credits a covered publisher with them.
   - **The page's publisher-name map names every code the estate serves (bbg included).** "A publisher this page has no name for
     yet" is a defect whenever the code is one this estate declares.
2. **n-5's remedy is presentation only:** each version is labelled with its date AND time (UTC) from the served stamp. Where two
   stamps share a minute, the seconds are added. **No new route; the stamp is already served** (`C-PRESENTATION-ONLY`).
3. **FWD-13's literal target is on the page.** BA's What-moved prints "161867780096.00003", along with raw floats for EV, beta and
   a rule line.
   - FWD-13 binds EVERY rendered figure: header cards, What-moved and rule lines.
   - SHORT_INT_RATIO gets its line name from the same served field names, never a page-side dictionary guess (`C-PRESENTATION-ONLY`).
     A name the payload does not carry is a served-runtime ask of AMGT_RESAPP.
4. **The issuer's "coverage-rule ask ... waits for his word" is RULED here, not held for Andrew.** The per-name publisher
   denominator is already a HARVST contract:
   - `C-HV-RANK-DECLARED-SET` prints the population every generation;
   - `C-HV-COVERED-VS-FOUND` defines the sets.
   Nothing is routed and no word is needed. Deciding what a field means is a call, and the self-drive routing rules it.
5. **FWD-12..FWD-20 enter in FWD-20-first order.** FWD-20 (`ui-smoke`, PNG + DOM JSON per state, FAILING the pre-redesign page)
   is the instrument FWD-12, 14, 15, 16, 17, 18 and 19 are graded by. It is built first, and no v0.4 outcome is graded before it
   exists.

## 3. FWD GRADES

- **REALIZED, standing:** FWD-4, FWD-9, FWD-10.
- **FWD-11: NOT REALIZED.** Wording items remain: the Posture comparable line, "0 of the 0 citations", "No chatter_daily rows
  exist for this security_key yet", and the unnamed publisher.
- **FWD-1: NOT REALIZED, 5 of 6 hops** (the driver series, AMGT_RESAPP round 52 ab-6, sequenced after CORPUS y-4).
- **FWD-2, FWD-3: NOT REALIZED** (names on 7 of 22 rows).
- **FWD-5, 6, 7, 8:** as round 10 (not realized).
- **FWD-12..FWD-20 (v0.4): NOT REALIZED**, not yet cut.
- **3 of 20 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 12 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **FWD-20: `portal/scripts/ui-smoke.mjs`** writes, per state (six), a PNG at 1440 and the DOM measurement JSON for every FWD-20 clause | 20 | LOCAL | **Its AC is the negative control:** run against the pre-redesign portal commit, it FAILS each clause it can measure there. Run against DEV, it prints each clause's value. A clause it cannot measure reads NOT_EXERCISED, never PASS. |
| 2 | **Version labels carry the time** (ruling 2) | RESAPP FWD-6 page half | LOCAL | The AC walks BA: 4 distinct labels for 20260910. |
| 3 | **FWD-13: every rendered figure** (header cards, What-moved, rule lines) carries units and tabular numerals, and a tooltip carries the mnemonic and full-precision value verbatim | 13 | LOCAL | The AC greps the rendered BA Model and What-moved DOM for a float with more than 6 fractional digits: 0. The tooltip carries the full value. |
| 4 | **Publisher names + found-only days** (ruling 1) | 11, HARVST FWD-5 | LOCAL | The AC: 992 HK 08-13 names bbg as searched and reads wsj/sa as "found, listing not run" once `publishers_found_codes` is served. Before that, it reads the ABSENT wording. |
| 5 | **FWD-11 wording at zero** | 11 | LOCAL | The comparable line names the comparable, not "this name"; the zero-citation footer; the never-collected timeline sentence in words. |
| 6 | **FWD-12: one dark band** | 12 | LOCAL | Graded by cell 1's instrument (`bandContainersTopLevel == 1`), so it merges after cell 1. |

**Fan-out:** 1 to 5 are independent; 6 follows 1.

**NOT cells this round:**
- FWD-14..19, which are graded by FWD-20 once it lands;
- the driver series (RESAPP ab-6);
- names on ranked rows (RESAPP).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- The portal DEV merge and push to origin, and PROD [CLAUDE.md Portal].
- Remove the worktrees `/c/tmp/wk-dsgn-amgtv1-{18..44}` and the `C:/tmp/cood-r*` scratch roots [CLAUDE.md Agent Autonomy:
  recursive deletion; his earlier word covered 9-17 only].

## Compiler Tools

- The CVO's v13: its shots 163, 249, 294, 336 and 393, and its reads of `/versions`, `/ledger` and the `model_block` stamps.
- The issuer's drain-end read, section 4.
- HARVST PRD v0.4 (for ruling 1).

This seat ran no new instrument: every number above is the CVO's or the issuer's, each cited.
