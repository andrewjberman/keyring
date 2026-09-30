# DSGN_AMGTV1 ROUND 2 -- L8 COMPILE + L9 ADJUDICATION (the L10 slug waits on e-3, e-5, e-7 in the record)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~08:5xZ
**Input:** `2.0.0_SA_COO~D`'s `round2/ROUND2_CLOSE_WALK.md` @`6e17397ea5` (read to EOF, 5,556 B), msg 26514, and the walk's PNGs
at `tmp/ui-walk/20260929T082619Z/shots/`, **read by this seat**: `004`, `030`, `035`, `042`, `049`.
**L7 RE-MEASURED not adopted:** `e-1`, `e-2`, `e-4`, `e-6` read `complete` at HEAD. **`e-3` and `e-5` read `pending` at HEAD**:
their `complete` flips sit MODIFIED in the shared working tree, uncommitted. The packet's "six instances VALID" is true of the
instances, but the record has not caught up. **`e-7` (ADDENDUM 2 direct act) reads `pending`.** L8/L9 are done here; **the L10
slug is held until the record reads e-3, e-5 and e-7 terminal.**

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions`: **11 items, 8 UNDER_INVESTIGATION.** Gating: `Z-W3-S2` (BLOCKING/ARMED), `Z-S1` (ARMED), `Z-W4-S1` (ARMED).

| row | disposition | grounds |
|---|---|---|
| `Z-W3-S2` (BLOCKING/ARMED: the tabs check anchored off the face) and its carrier `Z-W3-S3` | **GRADUATED** | Disarmed under AV-t-4 AMENDMENT 1. This seat ran `tabs.harness.cjs` at round 1's close: `CHECKS-OK 20 of 20`, rc=0 (ADJUDICATION_v2) |
| `Z-S1` (ARMED: move FWD-1's thread to a name the team covers) | **CARRIED** | an ENDPOINT-side decision, the CTO's. The live Valero dossier carries no team case, so hop 6 cannot close on Valero |
| `Z-W4-S1` (ARMED: whether the export follows the page) | **CARRIED** | the issuer's decision, open |
| `Z-W5-S1`, `Z-W8-S1`, `Z-W8-S2`, `Z-S2` | **CARRIED** as INERT notes | `Z-W8-S2` is graded against e-6 below |

## 2. L9 -- THE SIX JUDGMENTS, ON THE PNGs

| order | criterion (short) | verdict | what the page shows |
|---|---|---|---|
| **e-3** | the header reads every money figure one way, in the company's served currency | **PASS** | INTU `Price USD 277.13`, `Enterprise value USD 75.28B`; Valero `Price USD 382.86`, `Enterprise value USD 117B` (`042`, `030`). Round 1's `USD 382.86` beside `$117B` is fixed |
| **e-4** | Model lines in plain names; each missing line one sentence; the team's Base leads where served | **PASS** | `030`: "Share price (last close)", "Revenue", "Free cash flow", "Enterprise value to trailing EBITDA"; each of the 18 refused lines reads "The number is in the pack, but this page cannot show it yet because its unit convention is not built."; "The research team's Base case is not in this pack yet." leads the cases (Valero has none) |
| **e-2** | INTU: the Recommendation leads with the team's case, labelled as the team's; Valero: one sentence that it is not in the pack | **Valero clause PASS; INTU clause UNGRADED live** | `049` (INTU, live): *"The research team's Base case is not in this pack yet. The research team fills it in."*, then the machine-draft band. The served rendering is proven only offline (AC1 3 of 3), because vv-4 has not deployed `model.team_cases` |
| **e-1** | the Thesis panel and header read as plain sentences, with one dark band | **PARTIAL** | One dark band: **PASS** (the Thesis header is white). Chart and footer are sentences: **PASS**. **But the header and Thesis still carry machine strings:** "Social: no source measured **(S13)**", "identity **crosswalk/v1** @ 2026-09-25", "On today's rankings: chatter: **generation: none -- no committed pointer for this date**", "BLOOMBERG SESSION: NOT REPORTED" |
| **e-5** | lead-panel captions and states in words; every ticker without a slash | **PARTIAL** | Slash: **PASS** (`BP LN`). First caption: **PASS** ("Showing the Trending x Price list (movement is measured)."). **The Source line beneath is raw:** "generation 20260926T110728Z-df5d006844da \| state COMPLETE \| 32 row(s) committed \| coverage vintage bloomberg-dapi-boxside-pull:2026-09-26T11:07Z (**blp_client 127.0.0.1:8194**, live)" |
| **e-6** | Posture reasons as words, no path or code on the face | **PARTIAL** | Reasons: **PASS**; the six numbered reasons and every absence read as sentences. **Codes remain:** "identity UNRESOLVED: the form '**WMB_US_Equity**' matches no persisted or measured identifier form in **crosswalk/v1** (as_of 2026-09-25, 236 records)", "identity crosswalk/v1 @ 2026-09-25", "model **claude-opus-5** -- marked machine" |

### ⛔ e-2's LIVE INTU SENTENCE IS FALSE, NOT MERELY UNSERVED

*"The research team's Base case is not in this pack yet"* is printed for INTU. **INTU's pack has the team's Base.** This seat read
it served by `read_dossier` at AMGT_CORPUS rounds 9-10 (Price 2026E **371**). What is missing is the scoped API's field, which
vv-4 deploys. The page asserts a fact about the PACK from an absence in the PAYLOAD. Until vv-4 lands, the sentence should
name the gap it can see ("not served on this page yet"), not one it cannot. That is the same "a value must carry its claim"
line as elsewhere.

### ⭐ THE THREE PARTIALS HAVE ONE CAUSE: THE RAW-CODE CHECK SEES ONE SHAPE

Every mechanical FWD-11 criterion passed at "0 hits" (e-1 AC1-AC2, e-5 AC1, e-6 AC1). Yet the page shows `(S13)`,
`crosswalk/v1`, `generation: none`, `127.0.0.1:8194`, `WMB_US_Equity` and `claude-opus-5`. The issuer already named one blind
spot (the mnemonic class cannot match a mixed-case key). **The class is wider:** the check is a blacklist of one token shape
(`\b[A-Z][A-Z0-9]*_[A-Z0-9_]+\b`), and machine text arrives in many shapes (lowercase-slash ids, parenthesised codes, host:port,
model ids, "key: value" jargon). **A blacklist tuned by what it has already caught will keep reading 0 on the next shape.** This
is why the walk judgment, not the regex, is FWD-11's oracle.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- **NOT MET in the record**: e-3 and e-5 flips are uncommitted, e-7 pending.
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-W3-S2` GRADUATED; `Z-S1` and `Z-W4-S1` CARRIED with owners. **MET**
3. **Every judgment criterion graded** -- 6 of 6 (2 PASS, 1 PASS+UNGRADED, 3 PARTIAL). **MET**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S3",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T08:55:00Z",
    "one_line": "L9 round 2 on the walk PNGs: e-3 PASS (money one way) and e-4 PASS (Model in words); e-2 PASS on Valero, UNGRADED live on INTU, where the page says the team's case 'is not in this pack yet' although INTU's pack has it (371), because the API does not serve it until vv-4. e-1, e-5 and e-6 are PARTIAL on one cause: the raw-code check reads 0 while the page shows (S13), crosswalk/v1, generation: none, 127.0.0.1:8194, WMB_US_Equity and claude-opus-5. The L10 slug waits on e-3/e-5 flips (uncommitted) and e-7.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: AV-e-1, e-2, e-4, e-6 read 'complete' at HEAD; AV-e-3 and AV-e-5 read 'pending' at HEAD with their order files MODIFIED (uncommitted) in the shared tree; AV-e-7 reads 'pending'.",
        "L8: _latest_dispositions('.', 'DSGN_AMGTV1') 11 items, 8 UNDER_INVESTIGATION; gating Z-W3-S2 (BLOCKING/ARMED), Z-S1 (ARMED), Z-W4-S1 (ARMED). Z-W3-S2 graduates with its carrier Z-W3-S3 on this seat's tabs.harness.cjs run, CHECKS-OK 20 of 20 (ADJUDICATION_v2).",
        "e-3 (shots 042, 030): 'Price USD 277.13', 'Enterprise value USD 75.28B' (INTU); 'Price USD 382.86', 'Enterprise value USD 117B' (VLO).",
        "e-4 (shot 030): plain line names; 18 refused lines each read 'REFUSED -- The number is in the pack, but this page cannot show it yet because its unit convention is not built.'; 'The research team's Base case is not in this pack yet. The research team fills it in.' leads the cases.",
        "e-2 (shot 049, INTU, live): 'The research team's Base case is not in this pack yet. The research team fills it in.' above the machine-draft band. INTU's served dossier carries a team Base (Price 2026E 371; this seat's read_dossier at AMGT_CORPUS rounds 9 and 10).",
        "e-1 (shot 042): the Thesis header is white; the chart reads 'The series for the thesis driver ... is not in the model data yet ... The research data team adds the series.'; the footer reads 'The drafted document does not say how many claims were held back uncited.'. Still on the header and Thesis: 'Social: no source measured (S13)', 'identity crosswalk/v1 @ 2026-09-25', 'On today's rankings: chatter: generation: none -- no committed pointer for this date', 'BLOOMBERG SESSION: NOT REPORTED'.",
        "e-5 (shot 004): 'BP LN' without a slash; caption 'Showing the Trending x Price list (movement is measured).'; source line 'generation 20260926T110728Z-df5d006844da | state COMPLETE | 32 row(s) committed | coverage vintage bloomberg-dapi-boxside-pull:2026-09-26T11:07Z (blp_client 127.0.0.1:8194, live)'.",
        "e-6 (shot 035): six numbered reasons in words; 'identity UNRESOLVED: the form 'WMB_US_Equity' matches no persisted or measured identifier form in crosswalk/v1 (as_of 2026-09-25, 236 records)'; 'Snapshot as of 2026-09-16 -- model claude-opus-5 -- marked machine'.",
        "Check shape: the packet names round2/checks/raw.cjs's mnemonic class \\b[A-Z][A-Z0-9]*_[A-Z0-9_]+\\b; e-1 AC1/AC2, e-5 AC1 and e-6 AC1 read 0 hits against faces that carry the strings above."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W3-S2",
      "DSGN_AMGTV1-Z-W3-S3"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The close record @6e17397ea5 asserts six instances VALID, every mechanical criterion PASS, and the walk's remaining hits off the round's cells.",
    "world_is": "The instances are VALID, but two flips are not yet in the record. Three of the six faces still carry machine text the check cannot see. The live INTU Recommendation states the team's case is not in the pack when it is, because the payload does not serve it yet.",
    "notes": "FOR THE ROUND-2 ANALYSIS: (1) the empty-state sentence for a team case must name the gap the page can see ('not served on this page yet') until the API serves it, never assert the pack's contents from the payload; (2) FWD-11's check is a one-shape blacklist -- replace it with an allowlist of the page's own vocabulary, or accept that the walk read is the only oracle and stop citing '0 hits' as evidence; (3) the three PARTIAL residuals are one round-3 cell across header, lead-panel source line and Posture identity line."
  }
]
```
