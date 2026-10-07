# AMGT_RESAPP -- CTO adjudication of the 32 BLOCKED remediation rows re-owned to this seat (round 76, az-3)

**Seat:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~22:1xZ. **Input:** `deliverables/0.9.0_WK_AMGT_RESAPP~264/TRIAGE.md` (az-3: 109 OPEN rows
= 30 closed by evidence, 26 cut, 53 BLOCKED; 32 of the 53 name this seat), COO~Z msg 30335.

**Denominator:** 32 rows, in 12 causes. Every row gets one of four outcomes:
- **RULED-CELL:** a ruling, plus a cell for `2.0.0_SA_COO~Z`'s next issuance.
- **RULED-CLOSED:** a ruling that ends the row.
- **RE-OWNED:** the fix belongs to another lane, named here.
- **AT ANDREW:** his decision, carded.

The CVO writes the citing rows from this table.

## A. Identity (5 rows): Z-S117, Z-W7-S3, Z-W19-S6, Z-W20-S12, Z-W21-S4

**Ruling.**
1. **The grading denominator is the 89 covered crosswalk records.** The keyed count is printed beside it (33 of 89 today). The
   256-name union is NOT a grading denominator. Its unkeyed members read UNRESOLVED with a reason.
2. **ONE resolving cell.** It joins the 56 unkeyed covered records to AMGT_CORPUS's registered security keys
   (`model_block_pull._registered_security_keys()`, 96 at round 38), by research folder and name.
   - CORPUS already resolved these folders (FWD-19: 96 of 97), so RESAPP reads that answer and does not resolve a second time.
   - No vendor call.
   - Proof: keyed N of 89 printed, and every residual named with its reason. Control: a name CORPUS does not hold stays
     UNRESOLVED.
3. **Holdings identifiers** (167 of 170 with no CUSIP/FIGI/SEDOL join, W19-S6): the tri-state stays (`held None`). After the
   resolving cell, membership is re-read. A residual that needs a vendor identifier map comes back as ONE row with its count.
   It is not built speculatively.
4. **DE** (W20-S12) resolves if CORPUS holds it. Otherwise it stays with its plain reason (av-5).

**Outcome:** RULED-CELL (one cell) for all five.

## B. The comparable pack (Z-W20-S11) and Peers V (Z-S162)

**Ruling.**
- **The comparable pack is RESTRICTED SELECTION, stated.** The set is built from names that carry a key and the factor values,
  and the pack prints its restriction (N eligible of M). A set too short to compare reads ABSENT with its reason.
- **Z-S162 part 1 is a cell.** `peers_v.py` reads the peer objects through ONE declared mapping table (scanner-factor name to
  measure, such as fcfy and ey_ntm), and every ABSENT carries an `absent_reason`. Today 33 of 33 read ABSENT_SOURCE because
  the two vocabularies share no key.

**Outcome:** RULED-CELL (one cell). **Z-S162 part 3** (what Peers V means where a peer set is short) is AT ANDREW, card 2.

## C. The CSC column contract (2 rows): Z-W18-S13, Z-W21-S6

**Ruling, the contract.**
- A PRESENT CSC column carries {value, period or horizon, currency, source field}.
- An ABSENT column carries {derivable_from, reason} and NO value.
- So the ABSENT partition in `csc.py:21-31` is right as written. What is owed is the four fields on the PRESENT columns.

**Outcome:** RULED-CELL (one cell: the PRESENT columns carry period, currency and source).

## D. Set-level dispatch (2 rows): Z-S2, Z-C-S2

**Ruling.** `receiving-check.py` stays one artifact per invocation. The set grain is the ISSUER's loop over every artifact of the
issuance, printed in the drain-end packet as "checked N of N" with the list. No set-level limb is built (build ladder rung 1).

**Outcome:** RULED-CLOSED (NOT_A_DEFECT; the packet line is the mechanism).

## E. Single rulings

| row | ruling | outcome |
|---|---|---|
| Z-W3-S1 (two ONE PAGER workbooks, no precedence) | The workbook with the newer stored modified date is read. The other is listed as superseded, with its date, on the same line. | RULED-CELL (rides cell A's issuance) |
| Z-S119 (a ranking generation ran at 10:00Z while "collection" was bounded OFF) | `amgt-resapp-chatter-axis-daily` is a RANKING producer over articles already landed (`chatter-axis-schedule.tf:229-233`: a root producer on its own clock). It is not collection, so the bound did not cover it. | RULED-CLOSED (NOT_A_DEFECT) |
| Z-W173-S4 (the export prints a chart-ABSENT line where the page renders no chart) | The export mirrors the page. Where an undrafted thesis renders no chart, the export prints no chart line. An ABSENT line claims a slot the page does not have. | RULED-CELL |
| Z-S228 (no name search; the page passes the raw string as a key) | Contract: `GET /api/scoped/amgt/resolve?q=` over the crosswalk. An exact key passes through. A name or ticker returns candidates {security_key, name, ticker}. No match returns a reason. The page search calls it and never treats a typed name as a key. | RULED-CELL |
| Z-S283 (rcg R-0021 against the PRD's vendor-grant "R-21") | Citation rule, no renumbering: an rcg ruling is cited `R-00NN` (four digits, `rcg/rulings/RULINGS.jsonl`). A PRD-local ruling is cited `PRD R-NN` with its PRD. | RULED-CLOSED |
| Z-S14 (the VINTAGEID fixture is excluded by name) | The name-based exclusion stands. A provenance discriminator for one fixture is not built. | RULED-CLOSED (NOT_A_DEFECT) |
| Z-C-S369 (no `lib/__init__.py`) | The namespace-package convention stands. Every packaged Lambda imports `lib.*` today, and a marker would change every zip. A failing import is a new row with its evidence. | RULED-CLOSED (NOT_A_DEFECT) |
| Z-W31-S3 (MFA gates the automation login) | Closed by evidence. Walks sign in as the UI walker service account on the protected dev channel (`/ui-walk`; the CORPUS round-39 walks of 2026-10-06 were "signed in as the walker"). No MFA exemption is asked. | RULED-CLOSED |
| Z-C-S24, Z-S6 (`prd_signoff_lib.py:232` compares the version string for a legacy record with no `half_hash`) | A legacy record ages out at its PRD's next re-sign, which is byte-bound. RESAPP's is owed now (v0.41, ADDENDUM E). So both rows close when `prd-signoff.py status AMGT_RESAPP` reads the ratified half SIGNED with a hash. No code change. | RULED-CLOSED on that read |
| Z-C-S46, Z-W2-S10 (no handoff rule: path + commit + resource identifier) | This is a LAW proposal, not a RESAPP defect. CLAUDE.md is locked to Andrew's express order. The existing rules ("cite the file"; push state as a measured value) are the carrier. | RULED-CLOSED (NOT_A_DEFECT here) |

## F. Re-owned to another lane (3 rows)

| row | owner | the act |
|---|---|---|
| Z-S242 (`etf-classifications.tf` is CRLF in the index against `eol=lf`) | `0.7.0_AE_CloudOps`, as a seat act placed by COO~Z | One LF re-commit. It is the same class as the YangDataPipeline definition drift normalized today (OPAL_BBGTML-Z-S6). |
| Z-W2-S3, Z-C-S3 (`_comprail.py:340-341` EPHEMERAL_DIRS lacks `.terraform`) | the comp-tool rail's lane (`0.8.0_AE_CloudComp`) | Add `.terraform` to EPHEMERAL_DIRS. It is one line, with the rail's own falsifier. |

## G. AT ANDREW (7 rows, 3 cards)

| card | rows | the decision |
|---|---|---|
| 1 | Z-W22-S2, Z-W22-S3, Z-W22-S6, Z-W22-S7, Z-W22-S8 | Whether FWD-11's social half gets an admitted source at all (the CEO's X profile is client-rendered and billed per call), and if so its per-name budget. |
| 2 | Z-S162 part 3 | What Peers V reads where a peer set is short. |
| 3 | Z-S230 | Whether the Bloomberg Terminal credential is rotated. The username sits in 4 tracked artifacts, and his "LEAVE IT, no history rewrite" (MSTR~Z call 6, 18:18Z) settled the artifacts but not the rotation. |

## Count

RULED-CELL 11 rows in 6 cells (A 5, B 1, C 2, E 3); RULED-CLOSED 11 rows (D 2, E 9); RE-OWNED 3 rows; AT ANDREW 7 rows (Z-S162 is counted here once; its part 1 rides cell B). 11 + 11 + 3 + 7 = 32.

## ADDENDUM 1 (2026-10-06 ~22:1xZ) -- three rows from the COO's adjudication @fb9ca91ad5 (msg 30366)

| row | ruling | outcome |
|---|---|---|
| Z-W20-S8 (no named-section coverage on filing passages) | **CUT in round 77.** Each name's passage set carries the list of named sections it covers and the list it does not. A name with partial coverage (BABA) says so on the passage read. It serves FWD-18. | RULED-CELL |
| Z-S221 (`text_translated` is produced and never served) | **CUT in round 77.** The scoped API serves the translated text beside the original. It adds a `translated: true` flag and the source language, so a reader can tell a translation from the source words. The original is never replaced. | RULED-CELL |
| Z-S220 (SERP bronze partitions by `date=` with no security key) | **The key design, ruled now and built only when a web-search source is admitted.** The partition is `security_key=<key>/date=<d>/`, with the address from `lib/opal_naming.py address()` (rule 30). An unkeyed query is refused, not stored under date alone. The row stays PARKED with this design as its disposition. | RULED-CLOSED (design given; the build is gated on the source) |

These do not wait for the round-76 analysis. That analysis follows the CVO's slug and will list them as placed.

## ADDENDUM 2 (2026-10-07 ~05:5xZ) -- section G's three cards are ANSWERED (Andrew-direct "all recs approved")

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_054xZ_ALL_RECS_APPROVED_CTOZ_THREE_CARRIED_CARDS.md`.

| card | rows | Andrew's ruling | what follows |
|---|---|---|---|
| 1 | Z-W22-S2, Z-W22-S3, Z-W22-S6, Z-W22-S7, Z-W22-S8 | **No social source now.** | FWD-11's social half reads "no source admitted yet", with that reason, on the page and in `/overlay` (the top band already prints "no social source is admitted yet"). No billable social call runs. The five rows close as CLOSED_UNREMEDIATED / CARRIED_BY Andrew's later word. The budget ledger (W22-S2), the billing reader (W22-S7) and the collection contract (W22-S6, S8) are NOT built. |
| 2 | Z-S162 part 3 | **(a): "not available", with its reason, below 3 peers.** | It goes into cell ba-16 (the Peers V mapping), or its successor if ba-16 is terminal. With fewer than 3 eligible peers, every Peers V measure reads ABSENT with `absent_reason` naming the count ("2 peers; 3 are needed"). It is never a value computed on 1 or 2. Proof: a plant at 2 peers and one at 3. |
| 3 | Z-S230 | **No rotation.** | The row closes NOT_A_DEFECT on his word. The username stays in the 4 tracked files (his 2026-10-06 "LEAVE IT"). Nothing is rotated. |

**Count:** the 7 rows at Andrew are now ruled. The 32 rows re-owned to this seat read: RULED-CELL 12 (the 11, plus Z-S162's
part 3 into its cell), RULED-CLOSED 17 (the 11, plus the five social rows and Z-S230), and RE-OWNED 3. 12 + 17 + 3 = 32.
