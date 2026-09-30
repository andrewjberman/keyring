# DSGN_AMGTV1 ROUND 3 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~11:5xZ
**Input:** `2.0.0_SA_COO~D`'s `round3/ROUND3_CLOSE_WALK.md` @`459d2e8a3a` (read to EOF, 6,314 B), msg 26581. PNGs read by this seat:
walk A (VLO) `004`, `011`, `035`; walk B (INTU, SAP GY) `020`, `062`. Walk A's INTU/SAP shots are VOID (session lost, sign-in page),
so those two names are graded on walk B only.
**L7 RE-MEASURED not adopted:** `AV-r-1`..`AV-r-5` all `complete` on their LAST `<status>` tag at HEAD (round 3), 1 judgment each.

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions`: **15 items, 10 UNDER_INVESTIGATION.** Gating (ARMED): `Z-S1`, `Z-W4-S1`.

| row | disposition | grounds |
|---|---|---|
| `Z-W4-S1` (ARMED: does the export follow the page) | **CARRIED** | Half **(a)**, the harness keys on data, is **served by AV-r-3 and verified by this seat's own run** (below). Half **(b)**, the export's wording from one shared source, is still open (AMGT_RESAPP round 47 packet s.5 item 3). A row with an open half is not graduated |
| `Z-S1` (ARMED: move FWD-1's thread to a name the team covers) | **CARRIED** | the CTO's ENDPOINT call |
| `Z-W12-S1` and its resolution `Z-W12-S2` | **GRADUATED** | exec.cjs reads 3 of 3 arms after AV-r-1 drained |
| `Z-S3` (INERT: a walk step that lands on the sign-in page reports 0 findings instead of failing) | **CARRIED**, owner the ui-walk skill | ⭐ **the most important row this round.** A reader that cannot see reports ABSENCE: walk A's INTU and SAP shots were sign-in pages that would have read "0 findings" as a clean page. The COO caught it by eye and re-walked. **Until walk.mjs fails a step on a sign-in page, every "0 findings" on a walk is unproven** |
| `Z-W5-S1`, `Z-W8-S1`, `Z-W8-S2`, `Z-S2`, `Z-W11-S1` | **CARRIED** as INERT notes | `Z-W8-S2` (mnemonics in Posture cites) stands: the packet saw `OPER_MARGIN` / `NET_DEBT` inside SAP's cites |

## 2. L9 -- THE FIVE JUDGMENTS

| order | verdict | what the page shows |
|---|---|---|
| **r-3** (the parity harness reads the page's data and card windows, and a real difference still fails it) | **MET -- run by this seat** | `vv-5.AC1.sh`: sets exact **4 of 4**, ABSENCES 17/17, CASES 3/3, "FWD-30 HARNESS READS THE REDESIGNED PAGE: YES". `parity-ctl.sh`: deleting one export `ABSENT --` line takes absences 17 -> 16, and the harness returns **rc=1**, `missing=1`. **A real difference fails it.** Bound (`Z-W11-S1`): AC1's fixture has no Thesis cites, so its CITES 0=0 does not exercise the window read; the worker exercised it on the tabs fixtures |
| **r-2** (INTU leads with the team's case; Valero says in one true sentence the pack has none) | **Valero clause MET; INTU clause UNGRADED** | Every walked name now reads **"The research team's Base case is not served on this page yet."** That sentence is **TRUE**, and it fixes the false "not in this pack yet" this seat graded at round 2. INTU's lead-with-the-team-case arm cannot be seen until AMGT_RESAPP re-lands vv-4 |
| **r-4** (Exec Management reads its absence in words and says where the list came from) | **MET on the face** | `020`: "No officer list is in this name's pack yet: the company's 10-K had no officer section this page could read, and no other source was used." / "The research team fills this once an officer list is sourced." ⚠ **Behind "Read detail" the text is raw**: "roster_status UNRESOLVED-SOURCE; roster_reason ...; source_item Item 10...; source_accession 0000896878260000037". The panel header is still a dark band |
| **r-5** (the Model tab adds no second band; no money in an unserved form; a served chart's caption in words) | **MET on band and money; caption UNGRADED** | `062`: Model header white; `Price EUR 184.18`, `Enterprise value EUR 226B`, Base "159.61 EUR" as served. No chart is served on any walked name. ⚠ The Model face still carries status words outside this criterion: "REFUSED --" x18, "ABSENT --", "Base case: SERVED --", "PEERS V / DIVERGENCE D not read" |
| **r-1** (header, lead panel, Thesis identity line and Posture carry no machine text; no second band on Posture; census tokens judged) | **PARTIAL -- one residual** | Header: "identity as of 2026-09-25", "Social: no source measured", "price: no ranking has been published for this date yet" -- **clean**. Lead-panel source: "ranked 2026-09-28 from Bloomberg prices (32 names)" plus a collapsed Details -- **clean**. Posture: white header; "its ticker is not yet identified by the research team"; "Snapshot: drafted by a machine on 2026-09-16" -- **clean**. **Residual: lead row #10 reads "WALMEX\* MM"** -- the `*` of the `WALMEX*_MM_Equity` key (AMGT_CORPUS `Z-S39`'s glob metacharacter), the same class as round 2's `BP/ LN`, which e-5 fixed for `/` only. The census is blind to it (a punctuation mark inside a ticker token). **The six census tokens:** "P/E", "P/B", "y/y" are finance terms of art (accept); "Revenue/Sh" is an abbreviation a PM reads but the page elsewhere spells out ("Revenue per share"), so it is a consistency nit; "2026-2027" is inside a served quote (accept) |

## 3. ⭐ THE INSTRUMENT MOVED FROM A BLACKLIST TO AN ALLOWLIST, AND IT WORKED

At round 2 this seat found the raw-code check a one-shape blacklist that read 0 on six visible shapes. This round's inverted census
counts every non-prose token: **40 -> 6** on the walked bytes, and the 6 are all judgeable. **It has two blind spots, both named:**
it admits upper-case status words (so it cannot see "REFUSED" or "ABSENT"), and a metacharacter inside a ticker token ("WALMEX\*")
passes as prose. With `Z-S3`'s walk defect alongside, the census and the walk each still need the other.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 5 of 5. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 2 ARMED, both CARRIED with reasons (one half-served). **MET**
3. **Every judgment criterion graded** -- 5 of 5 (r-3 MET by this seat's run; r-2, r-4, r-5 MET on their exercisable clauses; r-1 PARTIAL). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S5",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T11:55:00Z",
    "one_line": "L9 round 3 on the walk PNGs and this seat's own harness runs: r-3 MET (4 of 4 sets exact; a deleted absence fails it, rc=1); r-2 MET on Valero with a now-TRUE 'not served on this page yet', INTU UNGRADED until vv-4 re-lands; r-4 MET on the face with a raw 'Read detail' drawer; r-5 MET on band and money, caption UNGRADED; r-1 PARTIAL on one residual, 'WALMEX* MM' on the lead panel (a glob metacharacter the census cannot see). Z-S3 (a walk that lands on sign-in reports 0 findings) makes every walk zero unproven until fixed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AV-r-1..AV-r-5 read 'complete' on their LAST <status> tag at HEAD, round 3, 1 judgment each.",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 15 items, 10 UNDER_INVESTIGATION; ARMED Z-S1, Z-W4-S1 (carried); Z-W12-S1 + Z-W12-S2 graduated; Z-S3 'a step that lands on the sign-in page reports 0 findings instead of failing' carried to the ui-walk skill's owner.",
        "r-3, this seat's runs: vv-5.AC1.sh -> 'ABSENCES page=17 rich=17 same=17 missing=0 extra=0', 'CASES page=3 rich=3 same=3', 'sets exact (missing=0 extra=0): 4 of 4', 'FWD-30 HARNESS READS THE REDESIGNED PAGE: YES', exit=0; parity-ctl.sh -> 'deleted export line 259 ... export absences 17 -> 16; harness rc=1; ABSENCES page=17 rich=16 same=16 missing=1', 'PARITY CONTROL: a deleted export absence is caught: YES', exit=0.",
        "r-1, walk A shots 004/011/035: header 'identity as of 2026-09-25', 'Social: no source measured', 'price: no ranking has been published for this date yet'; lead source 'ranked 2026-09-28 from Bloomberg prices (32 names) (requested 2026-09-29)' with a collapsed 'Details'; Posture white header, 'its ticker is not yet identified by the research team', 'Snapshot: drafted by a machine on 2026-09-16'; lead row #10 'WALMEX* MM'.",
        "r-2: 'The research team's Base case is not served on this page yet' on VLO's Recommendation card (shot 011); vv-4 is rolled back (ADJUDICATION_v57 of AMGT_RESAPP), so team_cases is unserved and the sentence is true.",
        "r-4, walk B shot 020: 'No officer list is in this name's pack yet: the company's 10-K had no officer section this page could read, and no other source was used.'; 'Read detail' opens 'roster_status UNRESOLVED-SOURCE; roster_reason ...; source_item Item 10. Directors, Executive Officers and Corporate Governance; source_accession 0000896878260000037'.",
        "r-5, walk B shot 062: Model header white; 'Price EUR 184.18', 'Enterprise value EUR 226B', 'Base case: SERVED -- 159.61 EUR ...'; 18 lines 'REFUSED -- The number is in the pack, but this page cannot show it yet ...'.",
        "Census (packet): 'NON-PROSE CENSUS: 6 token(s) over 6 surface(s)' (base 40): P/E x2, P/B, y/y, Revenue/Sh, 2026-2027."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W12-S1",
      "DSGN_AMGTV1-Z-W12-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @459d2e8a3a asserts 5 orders terminal and VALID, a census from 40 to 6 tokens, and each judgment's observations on walks A and B, with walk A's INTU/SAP shots void.",
    "world_is": "True as read, with the harness re-run by this seat. One residual on the lead panel ('WALMEX* MM') is the metacharacter class, invisible to the census. The Exec 'Read detail' drawer and the Model face carry raw status text outside their criteria. Z-S3 means a walk's zero is unproven until the walker fails on a sign-in page.",
    "notes": "FOR THE ROUND-3 ANALYSIS: (1) fix walk.mjs so a step on the sign-in page FAILS (Z-S3), before any further walk grade leans on 'N findings'; (2) extend the ticker cleanup from '/' to any key metacharacter ('*' on WALMEX*), and teach the census the punctuation-inside-a-ticker shape; (3) the Model face's status words (REFUSED/ABSENT/SERVED --, PEERS V / DIVERGENCE D) and Exec's raw 'Read detail' are the next surface; (4) the census admits upper-case status words, a second blind spot to close."
  }
]
```
