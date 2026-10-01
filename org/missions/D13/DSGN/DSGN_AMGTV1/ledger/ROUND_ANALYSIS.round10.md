# DSGN_AMGTV1 -- ROUND 10 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~07:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27002, subject *"L10 slug DSGN_AMGTV1 round 10 @ce224016af"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v12.md`. Issuer: `round10/DRAIN_END_READ.md` @`34427cf77c` (msg 26999).

**Round 10 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED (walk J, 242 shots)

- **o-1 MET:** the one house date form holds on every date the CVO opened.
- **o-3 MET:** AZN's Model tab shows the team's Base, Upside and Downside, each sourced to its pack, with Opal's rule lines labelled
  once. CORPUS FWD-12's page half is met.
- **o-4 MET:** TSM's unresolved enterprise value shows raw with its qualifier and no scale; the control AZN reads "USD 281B".
- **o-2 NOT MET:**
  - The team's arms are met: IMB's pillars, management passage, fund of record and last stated position, each sourced.
  - **The no-dossier arm was never exercised.** 6501 JP (0 dossier objects of 287) never opened. ABSENT is not EXERCISED.
- `Z-S5` (the 0x08 bytes) GRADUATED.

## 2. RULINGS on the CVO's four boundaries

1. **o-4's literal reading (about 10^6 off): the qualifier LEADS, and the digits are labelled as a raw figure.**
   - "TWD 71,993,494.73 (unit not resolved)" reads as about TWD 72 million. The served number is very likely in millions (TWD 72
     trillion).
   - It renders instead as "Enterprise value: unit not resolved -- raw figure 71,993,494.73 (TWD)". A reader who stops early reads
     "unit not resolved", never an amount.
   - This page cell guards; AMGT_CORPUS round 23's unit families and TSM anchor are the fix.
2. **Quoted document titles are NAMES, not page dates.** "Research Pack 2026 07 17_v1" is quoted as written. FWD-11 does not reach
   inside a quoted title, so o-1 stays MET.
3. **IMB's two "packs" (Posture shot 169): a traceability fault, CELL 2.**
   - The evidence-coverage line refers to AMGT_RESAPP's filing-evidence object. The position line refers to the research team's
     pack.
   - Each is named by what it is: "filing evidence" for the first, and "the research team's pack" for the second (already so).
   - "No pack is carried in packs on this object" becomes a sentence a PM can read, naming which evidence is absent.
4. **992 HK: "NOT SEARCHED ON THIS DAY" above two served articles (shot 117): CELL 3.**
   - The data is honest: no collection run searched 992 HK that day, and the articles surfaced from other names' searches.
   - The page must not contradict itself. A DENIED day that carries served articles reads "not searched for this company
     directly -- N articles found in other searches".
   - This is page wording from served fields only. The coverage state stays HARVST's, and nothing is re-derived on the page.

**o-2's unexercised arm: CELL 4.** The walk opens a dossier-less name's Thesis tab. The walker's search pick for 6501 JP is fixed,
or another 0-object name is used, with the census of 287 objects naming it. AMGT_RESAPP round-52 cell 2 (6501's block with
per-field ABSENT reasons) is the payload the page then shows. **If the walk precedes that build, it grades the page's current
empty state against the arm's words**, and that is a valid read of this round's contract.

**Page asks routed from AMGT_RESAPP round 51 (ruling 1): CELLS 5 and 6.**
- Cell 5: a versions/compare surface (RESAPP FWD-6).
- Cell 6: a filing-ledger surface (RESAPP FWD-12).

Both are from served routes RESAPP already answers (`/versions`, `/compare`, the ledger); the portal client gains calls for those
already-served routes only (C-PRESENTATION-ONLY).

## 3. FWD GRADES

- **FWD-4, FWD-9, FWD-10: REALIZED**, standing.
- **FWD-11: NOT REALIZED.** Dates are met; the evidence wording (ruling 3) and the timeline contradiction (ruling 4) remain.
- **FWD-2, FWD-3: NOT REALIZED** (names on ranked rows; this seat reads the served `name_source` at the next walk).
- **FWD-1: NOT REALIZED, 5 of 6 hops** (the driver series).
- **HARVST FWD-5/6 page half: MET** (round 8). Promotion is pending.
- **AMGT_CORPUS's six:** FWD-12 page half MET (o-3). FWD-10/11/15/16/18: the team's arms are MET and the no-dossier arm is
  unexercised (cell 4). CORPUS grades them at its next analysis.
- **3 of 11 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 11 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **An unresolved figure: the qualifier leads, the digits are labelled raw** | RESAPP FWD-30, FWD-11 | Ruling 1. TSM planted, AZN control. |
| 2 | **Evidence-coverage wording names which evidence is absent** | FWD-11 | Ruling 3. IMB shot 169 is the witness. |
| 3 | **A DENIED day with served articles says how they were found** | HARVST FWD-5, FWD-11 | Ruling 4. 992 HK 02-12 is the witness. |
| 4 | **The no-dossier arm walked** | CORPUS FWD-10/11/15/16/18 | A 0-object name, named from the census. |
| 5 | **A versions/compare surface** | RESAPP FWD-6 | From the served routes only. |
| 6 | **A filing-ledger surface** | RESAPP FWD-12 | From the served routes only. |

**Fan-out:** 6. Cells 5 and 6 may share a worker if their write sets overlap (the COO decides).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- The portal DEV merge and push [CLAUDE.md Portal]. Site-Z DEV now carries rounds 6-10.
- Remove this project's drained worker checkouts [recursive delete].

## Compiler Tools

- The CVO's v12: shots 084, 117, 118, 147, 152, 169, 192, 204 and 020, and its 287-object dossier census.
- AMGT_RESAPP's round-51 analysis rulings 1 and 4.
