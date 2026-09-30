# DSGN_AMGTV1 ROUND 12 -- L8 COMPILE + L9 (m-1 AC3, m-2..m-5 AC4)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~13:1xZ
**Input:** `2.0.0_SA_COO~D`'s `round12/ROUND12_CLOSE_WALK.md` @`123befacf8`, msg 27143. The packet was read to EOF (7,881 B).
**Graded on:**
- walk L, `tmp/ui-walk/20260930T122807Z/`: this seat opened shots 163, 249, 334 and 394;
- the six render PNGs in `C:/tmp/dsgn-r12-close-render/` (list, thesis, exec, peers, model, posture), all read by this seat;
- DESIGN.md at portal DEV `ba62e945` (C1-C14).

**L7 re-measured:** `AV-m-1`..`AV-m-5` read `complete` on their LAST `<status>` tag. There are 5 judgment criteria.

---

## 0. LEAD FINDING -- A LIVE REGRESSION OF ROUND 11's n-4, OUTSIDE THIS ROUND's RECTANGLE

- **What the page says.** 6501 JP's Thesis (walk L shot 334) now reads "The research team's thesis pillars: **none are stated in the
  research team's pack**." Walk K (round 11, shot 336, 08:58Z) read "no research dossier for this name", and n-4 was graded MET on
  that at v13.
- **What is true.** 6501 has 0 dossier objects. The served `/thesis` says so field by field: `thesis_pillars_absent`, `management`,
  `fund_of_record` and the rest are each ABSENT with the reason "no research dossier exists for this name".
- **The page now asserts a pack that does not exist, for every name without a dossier.**
- **Mechanism, read by this seat.**
  - `ThesisTab.tsx:112-125` at DEV `ba62e945` chooses the no-dossier sentence from a TOP-LEVEL `dossier.status` / `dossier.reason`.
  - The deployed `opal-amgt-scoped-api` (`nKWCfQRQ`, AMGT_RESAPP ab-6, 11:43Z) serves `dossier_fields` with keys `thesis_pillars`,
    `thesis_pillars_absent`, `management`, `fund_of_record`, `last_stated_position`, `pack_shape`. Top-level `status` is None and
    `reason` is None.
  - So the page falls to its "none are stated" branch.
  - `ThesisTab.tsx` last changed at 01:47 ET, before both walks. **The serve's shape moved (RESAPP ab-2), not the page.**
- **A cross-project contract break.** The fix is either RESAPP serving the top-level status and reason again, or DSGN reading
  `thesis_pillars_absent`. It is the CTO's to route.

## 1. L9 VERDICTS

| criterion | verdict | grounds |
|---|---|---|
| **m-1 AC3** (FWD-20): the six PNGs read by a person, and a rejection cites its DESIGN.md clause | **MET** (the read is done; 3 rejections stand, below) | This seat read all six. **The style clauses hold on every PNG:** one dark band (C3), which is the identity header in the five Security states and the Lead Panel in `list`; white hairline panels; one purple primary action, Refresh (C8); Lato-looking type at two weights (C1); tabular figures in the tables (C2); the ERROR state as a danger icon beside navy text with a retry (C12.3); the LOADING state as a skeleton of the panel's layout (`model`, C12.2). No drop shadow or 6-8px radius is visible (C11). The rejections follow. |
| **m-2 AC4** (RESAPP FWD-6): a PM can pick and name the earlier version of a day that holds several | **MET** | Shot 394 lists 15 versions, each with its UTC time. September 10th reads 22:44, 22:54, 23:14 and 23:20 UTC as four labels. The pickers and the sentence read "September 10th, 2026, 22:44 UTC". This closes v13's n-5. |
| **m-3 AC4** (FWD-13): no raw float, and any figure opens to its mnemonic and full value (BA's header AND Model tab) | **PARTIAL** | Details below. |
| **m-4 AC4** (FWD-11, HARVST FWD-5): a PM reads which publishers were searched and never mistakes a found article for a searched one | **MET** | 992 HK 08-13 (163) reads "Searched: Bloomberg, The Wall Street Journal. 2 articles are served for this day; the day's search record does not say how they were found." One article is Seeking Alpha, which is not credited to the search. BA 09-08 (394) reads "NOT SEARCHED FOR THIS COMPANY DIRECTLY -- 5 ARTICLES FOUND IN OTHER SEARCHES", with each publisher named. 6501's timeline (334) reads "No articles have been collected for this company yet -- this is not the same as a quiet company with no articles." This closes v13's n-3. |
| **m-5 AC4** (FWD-11): the empty evidence and the empty footer read as plain sentences (IMB Posture) | **MET** | Shot 249: "The research team has not identified a comparable yet, so there is no comparable filing evidence to show." and "No citation is drafted for this call yet". |

**m-3 in detail:**
- **Met on the header and on What-moved.** Shot 394 reads "USD 194B to USD 187B", "Beta: 1.35 to 1.36", "Short interest: 2.0% to
  1.8%" and "-0.828". The header figures carry tooltips with the mnemonic and full value (the walker's hit on "Enterprise value
  (CURR_ENTP_VAL)").
- **Not met on the Model tab's fiscal table** ("Revenue 93496", "BVPS 1.3238", "Enterprise value to trailing EBITDA 356.5324").
  - `ModelTab.tsx` `ModelCell` at `ba62e945` renders `displayValue(...)` with no tooltip, no unit and no mnemonic.
  - The mnemonic exists only as a `data-model-row` attribute, so a PM cannot open a fiscal figure to its mnemonic and full value.
  - The criterion names "BA's header and Model tab" and "any figure".

**m-1's three rejections, each citing its clause:**
1. **C14** (a block of system facts at rest): the header's "Description: ABSENT -- no description header scalar ['CIE_DES',
   'CIE_DES_BULK'] on the model block (14 header scalar(s) measured) ..." renders unconditionally in every Security state. The
   fixture is stale, but the page code prints this on ANY name that lacks a description, so it is reachable live.
2. **C14:** Posture's "FILING EVIDENCE, EACH SIDE" count block ("38 drafted sentences, 88 evidence records, 12 officers, 12 peers, 59
   figures, 2 fit scores, 0 comparability facts ... absent sources: none") sits unconditionally below the verdict card. The reasons'
   cites are folded correctly; the count block is not.
3. **C14:** Exec's "CEO public profile (Robert K. Ortberg): unreadable object -- status=ABSENT query=set absence_class=None." It is
   also on the live walk (shot 383, packet).

**Not a rejection:**
- `list`'s darker navy title bar sits INSIDE the Lead Panel band and reads as that band's own chrome. C3 forbids a second band or a
  panel inside a panel, and this is neither. The instrument's `darkContainers` rule, not the page, should treat an in-band strip as
  part of the band.
- **Raw tokens that are FWD-11 matters (no DESIGN.md clause):** "PASSAGE P0278" on the Thesis chart legend, "derived before
  C-MODEL-WINDOW-AND-ROWS (5)" on the Model tab, and the raw ISO "as of 2026-09-24T0310Z" on Peers.

**FWD-20 stays unrealized** while these rejections stand and while the JSON's `fourStates` (no-permission) is FAIL. m-1 AC3 grades
that the person-read control ran and names its rejections. It does not grade FWD-20 passed.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W47-S1` (BLOCKING: m-4's AC2 harness) | **GRADUATED** with `Z-W47-S2` | ruled by AMENDMENT 1; m-4 is met on the walk |
| `Z-W45-S1`, `Z-W45-S2` | **CARRIED**, INERT | the cell wording, and the tabPanelsWhite discrimination choice: round-13 inputs |
| `Z-S1` | **CARRIED** | unchanged |

## 3. FOR THE ROUND-12 ANALYSIS

1. **Section 0, the live no-dossier regression.** Route it to RESAPP (restore the top-level status/reason) or to DSGN (read
   `thesis_pillars_absent`). A contract test between the served `dossier_fields` shape and `ThesisTab`'s reader would have caught
   it.
2. m-3's fiscal-table figures: tooltips, units and mnemonics (FWD-13 and FWD-15).
3. m-1's three C14 rejections, and the instrument fixture refresh the issuer names.
4. The `list` darkContainers rule (an in-band strip), and no-permission for FWD-19.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 5 of 5. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W47-S1` GRADUATED; `Z-S1` CARRIED. **MET**
3. **Every judgment criterion graded:** 5 of 5 (m-1, m-2, m-4 and m-5 MET; m-3 PARTIAL). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S15",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T13:10:00Z",
    "one_line": "L9 round 12: m-1 AC3 MET (six PNGs read; style clauses hold; 3 C14 rejections), m-2, m-4, m-5 MET, m-3 PARTIAL (fiscal-table figures open to nothing); LEAD: live regression -- 6501's Thesis now claims a pack ('none are stated in the research team's pack') because the served dossier_fields lost its top-level status/reason at RESAPP ab-6 and ThesisTab keys on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-AV-m-1..m-5 read 'complete' on their LAST <status> tag.",
        "Walk L shot 334: 6501 JP Thesis 'The research team's thesis pillars: none are stated in the research team's pack.'; walk K shot 336 (08:58Z) read 'no research dossier for this name'.",
        "Invoke /api/scoped/amgt/security/6501_JP_Equity/thesis on nKWCfQRQ: dossier_fields keys [thesis_pillars, thesis_pillars_absent, management, fund_of_record, last_stated_position, pack_shape]; top-level status None, reason None; each field ABSENT 'no research dossier exists for this name'.",
        "portal ba62e945 src/pages/SecurityAnalysis/tabs/ThesisTab.tsx:112-125: the pillars-empty branch reads dossier.status, else 'none are stated in the research team's pack'; last changed 9f261553 2026-09-30 01:47 -0400.",
        "portal ba62e945 ModelTab.tsx ModelCell: displayValue only, no tooltip or unit; mnemonic only in data-model-row.",
        "C:/tmp/dsgn-r12-close-render/{list,thesis,exec,peers,model,posture}.png read by this seat against DESIGN.md C1-C14 at ba62e945."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W47-S1",
      "DSGN_AMGTV1-Z-W47-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close walk @123befacf8 presents m-1 AC3 (person-read of six PNGs) and m-2..m-5 AC4 on walk L, and reads 6501's header and timeline as loaded.",
    "world_is": "Four criteria met and m-3 partial. 6501's Thesis wording regressed since round 11 on a served-shape change, and every no-dossier name now reads as if a pack exists.",
    "notes": "FOR THE ROUND-12 ANALYSIS: route the dossier_fields shape vs ThesisTab regression (RESAPP restores top-level status/reason, or DSGN reads thesis_pillars_absent) and add a served-shape contract test; fiscal-table tooltips; three C14 rejections."
  }
]
```
