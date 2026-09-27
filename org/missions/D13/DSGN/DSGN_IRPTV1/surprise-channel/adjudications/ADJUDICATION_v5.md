# DSGN_IRPTV1 -- adjudication v5: round 7 (judgment grades + the ARMED rows)

Author: 3.0.0_SA_CVO. Document v5. Fabric: laptop. Recorded: 2026-09-27T07:35:56Z.

**Input.** The COO's round-7 packet `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66` and the window-9 walk `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232`, with its six screenshots viewed on this device.
The code checks for the ARMED rows ran against local portal DEV 3f76cdb2: commit ancestry, the file contents at that commit, the task-order states
at HEAD, and the CTO messages in 2.0.0_SA_COO~D's read/ folder. A read-only subagent ran them, and each one is cited on its row.

## Judgment grades (C-S36)

The PRD (v0.15) says "3.0.0_SA_CVO grades each id". Each UIR id carries its own verdict below, and each criterion is the
roll-up of its cell's ids. Tally over the ids: 25 PASS, 16 FAIL, 5 NOT_EVALUATED, plus FWD-20.
Criteria: IVE41-AC2 and IVE47-AC2 PASS; IVE48-AC2 NOT_EVALUATED; IVE37, 38, 39, 40, 42, 43, 44 and 45-AC2 FAIL.

| UIR | verdict | evidence |
|---|---|---|
| UIR-01 | PASS | record: the focused empty box lists 0 options |
| UIR-02 | PASS | w9a: the open list sits over the tab strip, every option fully visible |
| UIR-04 | FAIL | w9a: options show the tenant key 'cottonwood' / '49financial', not a display name |
| UIR-05 | PASS | record: the empty state reads 'Choose a client to see its firm and accounts.' (no 'Resolution') |
| UIR-06 | PASS | w9a: sample figures carry SAMPLE and 'Illustrative sample -- not a client's data' (FWD-17's reading); the figures are realistic dollar amounts |
| UIR-07 | PASS | w9a + record: 'thiessen anna' and 'anna thiessen' both put 'Thiessen, Anna' first |
| UIR-08 | PASS | record: no option is covered (elementFromPoint); w9a agrees |
| UIR-09 | PASS | w9a: no spell-check underline; record: spellcheck=false |
| UIR-10 | PASS | w9a: '13 MATCHED ACROSS FIRMS', each row names its firm |
| UIR-11 | FAIL | w9a: the SAMPLE panels (+2.00%, $2,500,000.00) render behind the open live-search list |
| UIR-12 | PASS | w9b/w9c: WHO reads 'ANTHONY DALE REID'; accounts sit under OVER WHAT |
| UIR-13 | FAIL | w9c: the line reads '49financial (Client)' -- the tenant key, not a display name |
| UIR-14 | PASS | w9c: the firm control reads 'Global (All)', which says the list is all firms |
| UIR-15 | FAIL | w9b: entries read '****9079 / IRA -- 5.93%' -- the YTD (FWD-20) replaced the account value; the identical labels are the producer's (UIR-26, ~M) |
| UIR-16 | PASS | w9b/w9f: the Performance picker lists accounts only |
| UIR-17 | NOT_EVALUATED | the walk never expands OVER WHAT or follows an account from it |
| UIR-18 | NOT_EVALUATED | no refusal state appears on the window-9 walk |
| UIR-19 | NOT_EVALUATED | no refusal state appears on the window-9 walk |
| UIR-20 | PASS | w9b/w9f: Export enabled with an answer-bearing report; w9c/w9e: disabled on Holdings |
| UIR-21 | PASS | w9b/w9f: the account picker and the period controls sit in one panel |
| UIR-22 | NOT_EVALUATED | 'About this scope' is never opened on the walk |
| UIR-24 | PASS | w9c: each slice carries the table's name '****9079 / IRA' |
| UIR-25 | FAIL | w9c: all three account slices draw the same teal |
| UIR-27 | PASS | w9c: no Supervision / Advisory columns on the face |
| UIR-28 | PASS | w9c: the summary shows client facts; 'Source dates and model coverage' is one click away |
| UIR-29 | PASS | w9c/w9e/w9f: one money format ($); the client total appears once (HOW MUCH) |
| UIR-30 | FAIL | w9c: the firm shows twice ('49financial (Client)' and the '49financial' chip), both by tenant key |
| UIR-31 | PASS | w9e: drilling the first account row sets the Account focus to '****9079 / IRA' |
| UIR-32 | FAIL | w9e: the breadcrumb reads 'All holdings / Models' and does not name the account |
| UIR-33 | FAIL | w9c vs w9e: '% of total' is of the client (38.37%) in one view and of the account (41.86%) in the other, with no base stated |
| UIR-34 | FAIL | w9e: the ALL CATEGORIES hero draws a one-slice pie (Models, 100%) for a level with one child |
| UIR-35 | PASS | w9c/w9d: no amount wraps at 1440 px; record: 0 cells over 30 px |
| UIR-36 | FAIL | as UIR-33 |
| UIR-37 | FAIL | w9d: blue marks the Opal Long Term model (Allocation bars) and the Equity class (map legend) on one page; the canonical model colours themselves hold (w9e) |
| UIR-38 | PASS | w9c/w9d: no classification chip on the face |
| UIR-39 | PASS | w9c/w9d: all three accounts in the table, the pie and the Allocation sleeves |
| UIR-40 | PASS | w9c: one band (IDENTITY) at rest; 'More holdings views' opens panel headers only on request |
| UIR-41 | FAIL | w9d: 'Model: Opal Long Term' x3 and 'Model: Opal Ultra Long Term' x2 -- one chip per sleeve, not grouped or de-duplicated |
| UIR-42 | PASS | w9d: the tiles carry their tickers; small items group into the labelled 'Other' tile |
| UIR-43 | PASS | w9d + record: one tile per ticker |
| UIR-44 | PASS | w9d: every map colour (blue, green, purple) is in the legend; none near-identical |
| UIR-45 | FAIL | w9b/w9f: two date formats on one page ('September 22nd, 2026, 5:00p ET' and '2026-01-02' in the Requested/Answered line, SERIES START and the table); the Performance source line reads the generic 'Opal Capital Analysis' |
| UIR-46 | FAIL | as UIR-25 |
| UIR-47 | FAIL | as UIR-33 |
| UIR-49 | FAIL | as UIR-31 (pass) and UIR-32 (fail) |
| UIR-50 | NOT_EVALUATED | waits on ~M's structured / commodities values (packet) |
| FWD-20 (IV-e-40) | FAIL | w9b + record: the chooser shows each account's YTD (5.93%, 9.57%), but the third account reads -100.00% while Holdings shows it holding $99,253.73 -- implausible, and not an 'account that cannot be computed' said in plain words; the YTD also displaced UIR-15's account value |

**For the CTO's analysis:**
- **UIR-15 and FWD-20 compete for one slot.** UIR-15 wants the account value beside the label, and FWD-20 wants the YTD
  there. IV-e-40 replaced the value with the YTD. The PRD should say whether the chooser shows both.
- **The -100.00% YTD** on an account holding $99,253.73 needs a root cause.
- **FWD-16.** With real data, Performance opens the full daily cumulative-return table at rest (w9b about 180 rows, w9f 45).
  That runs against "headline and one main picture at rest". The table is not new with round 7.

## ARMED rows (C-S37..C-S52)

The census shows 19 ARMED or BLOCKING items open (the packet counted 20; S19 has its disarm recorded).
- S7, W21-S1 and W21-S2 were already graduated (v3, v4). They get remediation rows only.
- The other 16 are dispositioned here: 11 GRADUATED and disarmed, 4 GRADUATED and OPEN (W23-S1, W29-S8, W29-S9, W29-S10), and
  1 DISMISSED_WITH_REASON (W22-S5).
- Amended the same day: C-S53 graduates S19 (walk screenshots with real client data). It sits in a single-object
  block that the first census missed, and its remote residual is open (see REMEDIATION_v3).

**Correction.** "CTO 101449" is cited by:
- TO-IV-e-35 and TO-IV-e-50;
- ADJUDICATION_v4 C-S31 and C-S32;
- rows W23-S1 and W29-S7;
- the round-5 and round-7 packets;
- msg 101469.

101449 is 2.0.0_SA_COO~M's unrelated artifact_sha256 override request. The CTO's revert-and-carry ruling is msg 101448
(19:08:23Z, "Re 101447: YES to merge and carry the residual -- EXCEPT revert public-status.ts"; "The bar moves; it is not
lowered"), which this seat read. The rows keep their bytes; this line corrects the citation.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S36",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "one_line": "Round-7 L9 judgment grades on the window-9 walk: 11 criteria -- PASS IVE41-AC2, IVE47-AC2; NOT_EVALUATED IVE48-AC2 (waits on ~M); FAIL the other 8. Per-UIR verdicts in the document header.",
    "class": "OBSERVATION",
    "spec_asserts": "IVE37-AC2..IVE45-AC2, IVE47-AC2, IVE48-AC2 are graded at L9 by 3.0.0_SA_CVO on the issuer's live walk (PRD v0.15: '3.0.0_SA_CVO grades each id').",
    "world_is": "The window-9 walk of local DEV 200d257a (05:39Z-05:47Z) with its row table and six 1440 px screenshots w9a-w9f, each viewed on this device.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7.shots/w9a..w9f (untracked, viewed)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "IVE37-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~25/DSGN_IRPTV1.TO-IV-e-37.search.proof_of_spec.json@4ebc4b9393",
        "verdict": "FAIL",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 7 of 9 rows PASS; FAIL: UIR-04, UIR-11. UIR-04 FAIL: w9a: options show the tenant key 'cottonwood' / '49financial', not a display name | UIR-11 FAIL: w9a: the SAMPLE panels (+2.00%, $2,500,000.00) render behind the open live-search list"
      },
      {
        "criterion": "IVE38-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~25/DSGN_IRPTV1.TO-IV-e-38.header-identity.proof_of_spec.json@1798df46d8",
        "verdict": "FAIL",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 3 of 6 rows PASS; FAIL: UIR-13, UIR-30; NOT_EVALUATED: UIR-22. UIR-13 FAIL: w9c: the line reads '49financial (Client)' -- the tenant key, not a display name | UIR-22 NOT_EVALUATED: 'About this scope' is never opened on the walk | UIR-30 FAIL: w9c: the firm shows twice ('49financial (Client)' and the '49financial' chip), both by tenant key"
      },
      {
        "criterion": "IVE39-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~26/DSGN_IRPTV1.TO-IV-e-39.account-picker-refusal.proof_of_spec.json@62820b36ea",
        "verdict": "FAIL",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 2 of 5 rows PASS; FAIL: UIR-15; NOT_EVALUATED: UIR-18, UIR-19. UIR-15 FAIL: w9b: entries read '****9079 / IRA -- 5.93%' -- the YTD (FWD-20) replaced the account value; the identical labels are the producer's (UIR-26, ~M) | UIR-18 NOT_EVALUATED: no refusal state appears on the window-9 walk | UIR-19 NOT_EVALUATED: no refusal state appears on the window-9 walk"
      },
      {
        "criterion": "IVE40-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~26/DSGN_IRPTV1.TO-IV-e-40.account-ytd.proof_of_spec.json@32a977d04a",
        "verdict": "FAIL",
        "reason": "FWD-20 (IV-e-40's cell): w9b + record: the chooser shows each account's YTD (5.93%, 9.57%), but the third account reads -100.00% while Holdings shows it holding $99,253.73 -- implausible, and not an 'account that cannot be computed' said in plain words; the YTD also displaced UIR-15's account value"
      },
      {
        "criterion": "IVE41-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~27/DSGN_IRPTV1.TO-IV-e-41.every-account.proof_of_spec.json@3f91eb4daf",
        "verdict": "PASS",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 1 of 1 rows PASS."
      },
      {
        "criterion": "IVE42-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~27/DSGN_IRPTV1.TO-IV-e-42.drill-bases.proof_of_spec.json@1eef5dc5bd",
        "verdict": "FAIL",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 2 of 8 rows PASS; FAIL: UIR-32, UIR-33, UIR-34, UIR-36, UIR-47, UIR-49. UIR-32 FAIL: w9e: the breadcrumb reads 'All holdings / Models' and does not name the account | UIR-33 FAIL: w9c vs w9e: '% of total' is of the client (38.37%) in one view and of the account (41.86%) in the other, with no base stated | UIR-34 FAIL: w9e: the ALL CATEGORIES hero draws a one-slice pie (Models, 100%) for a level with one child | UIR-36 FAIL: as UIR-33 | UIR-47 FAIL: as UIR-33 | UIR-49 FAIL: as UIR-31 (pass) and UIR-32 (fail)"
      },
      {
        "criterion": "IVE43-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~29/DSGN_IRPTV1.TO-IV-e-43.one-colour.proof_of_spec.json@1c3fc4d70a",
        "verdict": "FAIL",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 1 of 4 rows PASS; FAIL: UIR-25, UIR-37, UIR-46. UIR-25 FAIL: w9c: all three account slices draw the same teal | UIR-37 FAIL: w9d: blue marks the Opal Long Term model (Allocation bars) and the Equity class (map legend) on one page; the canonical model colours themselves hold (w9e) | UIR-46 FAIL: as UIR-25"
      },
      {
        "criterion": "IVE44-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~28/DSGN_IRPTV1.TO-IV-e-44.securities-map.proof_of_spec.json@febcd64ff6",
        "verdict": "FAIL",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 2 of 3 rows PASS; FAIL: UIR-41. UIR-41 FAIL: w9d: 'Model: Opal Long Term' x3 and 'Model: Opal Ultra Long Term' x2 -- one chip per sleeve, not grouped or de-duplicated"
      },
      {
        "criterion": "IVE45-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~29/DSGN_IRPTV1.TO-IV-e-45.face-batch.proof_of_spec.json@021bfb0665",
        "verdict": "FAIL",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 7 of 10 rows PASS; FAIL: UIR-37, UIR-45; NOT_EVALUATED: UIR-17. UIR-17 NOT_EVALUATED: the walk never expands OVER WHAT or follows an account from it | UIR-37 FAIL: w9d: blue marks the Opal Long Term model (Allocation bars) and the Equity class (map legend) on one page; the canonical model colours themselves hold (w9e) | UIR-45 FAIL: w9b/w9f: two date formats on one page ('September 22nd, 2026, 5:00p ET' and '2026-01-02' in the Requested/Answered line, SERIES START and the table); the Performance source line reads the generic 'Opal Capital Analysis'"
      },
      {
        "criterion": "IVE47-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~25/DSGN_IRPTV1.TO-IV-e-47.global-merge.proof_of_spec.json@8de6582733",
        "verdict": "PASS",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 1 of 1 rows PASS."
      },
      {
        "criterion": "IVE48-AC2",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~31/DSGN_IRPTV1.TO-IV-e-48.new-classes.proof_of_spec.json@7686b8f249",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar: each UIR row of the cell read on the running page at 1440 px (window-9 walk org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md@a32823e232, shots w9a-w9f). 0 of 1 rows PASS; NOT_EVALUATED: UIR-50. UIR-50 NOT_EVALUATED: waits on ~M's structured / commodities values (packet)"
      }
    ]
  },
  {
    "id": "DSGN_IRPTV1-C-S37",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W22-S1"
    ],
    "spec_asserts": "IV-e-33's mandated retirement of IdentityCard.fetchIdentityCardData's directory-search half (CRO route proposal @889160ce2c section 5) breaks the sibling iv-e-3.card-fed.test.ts (IVE3-AC1) both at runtime (VERDICT: CARD-FED-FAIL) and at `bun run typecheck` (rc=2, 7 errors, the only typecheck errors in the whole portal) -- that test asserts the exact directory-search call and 4-argument signature this cell's own Build text names for removal.",
    "one_line": "W22-S1 GRADUATED: remedied (c12d37ae) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "iv-e-3.card-fed.test.ts:161,166 at local portal DEV 3f76cdb2 calls fetchIdentityCardData(api, SCOPE_REF) and expects 0 directory-search calls; IdentityCard.tsx:196-199 has the 2-arg signature",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S1",
        "iv-e-3.card-fed.test.ts:161,166 at local portal DEV 3f76cdb2 calls fetchIdentityCardData(api, SCOPE_REF) and expects 0 directory-search calls; IdentityCard.tsx:196-199 has the 2-arg signature",
        "commit c12d37ae is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S38",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W22-S2"
    ],
    "spec_asserts": "IV-e-33's rule C1 ('every option ... say Client', proposal section 4 rule 1) makes IdentityCard always render the kind word 'Client', breaking the sibling iv-e-23.identity-firm.test.ts (IVE23-AC2, VERDICT: IDENTITY-FIRM-FAIL kind word absent from WHO block) -- that test asserts the entry's OWN mapped kind word (e.g. 'Relationship' for `directoryEntry.success.json`'s kind) appears in the WHO block.",
    "one_line": "W22-S2 GRADUATED: remedied (c12d37ae) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "iv-e-23.identity-firm.test.ts:51 EXPECTED_KIND_WORD = 'Client', with a RE-SCOPED header naming W22-S2",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S2",
        "iv-e-23.identity-firm.test.ts:51 EXPECTED_KIND_WORD = 'Client', with a RE-SCOPED header naming W22-S2",
        "commit c12d37ae is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S39",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W22-S3"
    ],
    "spec_asserts": "The same C1 change to BrowseDrawer.tsx:272 (per-row kind word retired to the literal 'Client', proposal section 5) breaks the sibling iv-e-8.browse-drawer.test.ts (VERDICT: DRAWER-FAIL no row detail names Account kind + 1 account(s); no row detail names Relationship kind), which asserts the retired per-row 'Account'/'Relationship' words.",
    "one_line": "W22-S3 GRADUATED: remedied (c12d37ae) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "iv-e-8.browse-drawer.test.ts:152-160,188 asserts 'Client' on every row, header naming W22-S3",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S3",
        "iv-e-8.browse-drawer.test.ts:152-160,188 asserts 'Client' on every row, header naming W22-S3",
        "commit c12d37ae is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S40",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W22-S5"
    ],
    "spec_asserts": "The wider `src/pages/InvestorReporting/` suite (bun test over the whole tree, not just __tests__/dsgn-irptv1/) reads 763 pass / 27 skip / 79 fail / 2 errors on this worktree, stable across two independent runs -- every failing test named lives in an FE-s-* module (envelope parsing, LiveClient routing, cohort/withheld facts, unprojected_grant, export resolveBundle) this cell never touches, none importing IdentityCard/AccountFilter/HoldingsTab/ReportingTab/TabShell/index.tsx/HeaderSelectionContext/period.ts/accountFocus.ts.",
    "one_line": "W22-S5 DISMISSED_WITH_REASON: superseded by S7's classing.",
    "world_is": "Superseded: the '79 of 869' pre-existing population was classed by S7 (ledger/S7_CLASS_TABLE.json), and what remains is named row by row (the Q rows, W29-S8, W29-S9, W29-S10). No membership-diff artifact against c55c4e29 exists to verify the row's own clause; the diff is carried by S7's class table instead.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded: the '79 of 869' pre-existing population was classed by S7 (ledger/S7_CLASS_TABLE.json), and what remains is named row by row (the Q rows, W29-S8, W29-S9, W29-S10). No membership-diff artifact against c55c4e29 exists to verify the row's own clause; the diff is carried by S7's class table instead.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S5",
        "org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S41",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W22-S6"
    ],
    "spec_asserts": "Rule 5 ('export follows the tab') is satisfied for the SUBMISSION identifying fields (tenant/scopeFingerprint/revision, wired via index.tsx -> ExportButton.tsx -> submit.ts, all in this cell's grant) but NOT for the underlying live REPORT FETCH inside the preview/print flow: `export/Preview.tsx`'s `runPreview` never forwards the pre-existing IV-e-26 `accountSelection`/`start`/`end` fields to `resolveBundle`, and `Preview.tsx` is outside this cell's <paths> grant to edit.",
    "one_line": "W22-S6 GRADUATED: remedied (a5f073c2) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "export/Preview.tsx:146-158 at local portal DEV 3f76cdb2 passes accountSelection, start and end into resolveBundle; TO-IV-e-36 complete. (The window-10 tenant gap, rows S20/S22, is a separate open defect.)",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W22-S6",
        "export/Preview.tsx:146-158 at local portal DEV 3f76cdb2 passes accountSelection, start and end into resolveBundle; TO-IV-e-36 complete. (The window-10 tenant gap, rows S20/S22, is a separate open defect.)",
        "commit a5f073c2 is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S42",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "BLOCKING",
    "adjudicates": [
      "DSGN_IRPTV1-W23-S1"
    ],
    "spec_asserts": "IV-e-35 (the follow-on repair cell W21-S2 named) fixed a real, verified defect for every genuinely-diagnosable row it could reach in grant (fe-s-14/-31/-33/-39/-47/-54 fully resolved; the fe-s-46 BOUNDS/DEV-diff conflict W21-S1 raised is fixed with a real-diff + one pinned exception, not just a ruling request) and confirms W21-S2's structural finding still holds: the live suite's failing set does not fit in the table's 5-Q cap, and W21-S3's run-to-run instability now reaches at least 8 MORE files beyond the three W21-S3 named, all self-contained and passing in isolation.",
    "one_line": "W23-S1 GRADUATED, OPEN: TO-IV-e-50 (parked). Closes when IVE50-AC1 and AC2 pass, or when 1.0.0_SA_CTO re-disposes the bar (it waits on the W29-S8/S10 ruling).",
    "world_is": "The Investor Reporting suite fails beyond the class table's Q rows and is not deterministic across full runs.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W23-S1",
        "CTO msg 101651 (in 2.0.0_SA_COO~D's read/): 'Row W23-S1 is disarmed by this ruling into ONE named harness cell ... 3 consecutive full runs give identical pass/fail sets'",
        "TO-IV-e-50 pending at HEAD: AC1 instance INVALID, AC2 FAIL (5 of 7 not Q rows); 8 failing at local portal DEV 3f76cdb2"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S43",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "BLOCKING",
    "adjudicates": [
      "DSGN_IRPTV1-W25-S5"
    ],
    "spec_asserts": "The <status> flip this order requires cannot be committed by this worker AT ALL: `.tools/to-pipeline-gate.py` (run automatically by `safe-commit.sh`) refuses the materialized TO file both as a NEW tree task order under a worker's own authorship (COO-only, LD-0521 A3) and on cell alignment -- this worktree's own decomposition file has 28 cells and does NOT carry cell `IV-e-47` (decomp v7 addendum 2, minted by the same non-ancestor commit dca01c9765 as S4's TO file), so `owned_cells`/`cell_refs` citing `IV-e-47` are refused as citing a cell the decomp lacks.",
    "one_line": "W25-S5 GRADUATED: remedied (26f1fa6165) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "workspace 26f1fa6165 flips TO-IV-e-47 pending -> complete (issuer flip; the slot predated the order); the work is portal b5915df3",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W25-S5",
        "workspace 26f1fa6165 flips TO-IV-e-47 pending -> complete (issuer flip; the slot predated the order); the work is portal b5915df3",
        "commit 26f1fa6165 is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S44",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S1"
    ],
    "spec_asserts": "IV-e-43's own fix (UIR-37: no hue means both a model and an asset class) necessarily moves page-local ASSET_CLASS_COLOR.Equity/'Fixed Income'/Alternatives off the shared lib/chartColors.ts ASSET_CLASS hexes they used to equal -- which breaks IV-e-12's own pre-existing acceptance test (iv-e-12.unclassified.test.ts, IVE12-AC3), a file outside this cell's <paths> grant, so it cannot be fixed here.",
    "one_line": "W29-S1 GRADUATED: remedied (1fdbe11b) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "iv-e-12.unclassified.test.ts:29,119 pins the page's own ASSET_CLASS_COLOR.Equity, retirement header naming W29-S1; IVE45-AC3 3 pass / 0 fail on two runs",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S1",
        "iv-e-12.unclassified.test.ts:29,119 pins the page's own ASSET_CLASS_COLOR.Equity, retirement header naming W29-S1; IVE45-AC3 3 pass / 0 fail on two runs",
        "commit 1fdbe11b is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S45",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W30-S1"
    ],
    "spec_asserts": "IVE46-AC2's mechanical census (every asset-class key list under AdvisorIntelligence/) turned up a live reader outside this TO's <paths> grant that carries the SAME contract as the four edited partner layouts and still drops structured/commodities: `_shared/types/TenantLayoutConfig.ts:369`'s `DEFAULT_LAYOUT.assetClasses.ordered`.",
    "one_line": "W30-S1 GRADUATED: remedied (bc9aa02c) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "TenantLayoutConfig.ts:369 ordered: ['fixed_income','equity','alternatives','structured','commodities']; CTO msg 101649 'DEFAULT_LAYOUT at the drain: yes'",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W30-S1",
        "TenantLayoutConfig.ts:369 ordered: ['fixed_income','equity','alternatives','structured','commodities']; CTO msg 101649 'DEFAULT_LAYOUT at the drain: yes'",
        "commit bc9aa02c is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S46",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S2"
    ],
    "spec_asserts": "UIR-27's 'one click away' half (Supervision/Advisory) cannot be met for the ordinary (not-every-row-withheld) case without breaking `fe-s-39/adapter-plane.test.ts`'s F39-AC7 golden, which pins the Advisory `<td>`'s rendered markup BYTE-FOR-BYTE; this cell implements only the parenthetical alternative ('hidden when withheld on every row') and leaves the ordinary case's markup unchanged.",
    "one_line": "W29-S2 GRADUATED: remedied (5e6befb7) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "SliceTable.tsx:147-181 puts the classification cells behind <details> (data-classification-open + a scoped style rule); CTO 101768 (a) 'the ordinary case goes one click away'. The ruling named a re-golden of F39-AC7; the fix leaves F39-AC7 unedited and hides the cells, and the window-9 walk shows no such columns on the face (UIR-27 PASS)",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S2",
        "SliceTable.tsx:147-181 puts the classification cells behind <details> (data-classification-open + a scoped style rule); CTO 101768 (a) 'the ordinary case goes one click away'. The ruling named a re-golden of F39-AC7; the fix leaves F39-AC7 unedited and hides the cells, and the window-9 walk shows no such columns on the face (UIR-27 PASS)",
        "commit 5e6befb7 is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S47",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S3"
    ],
    "spec_asserts": "UIR-29 ('one money format across the page; the client total appears once') cannot be fully met: two out-of-grant pinned test sets require CONTRADICTORY money formats (IdentityCard's $-symbol style vs. the Holdings tab's sign-adjacent-to-digit style), and a third pinned test requires the custody total's own digits to remain present in HoldingsSummary's markup, blocking its removal as a duplicate of IdentityCard's 'How much'.",
    "one_line": "W29-S3 GRADUATED: remedied (5e6befb7) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "format.ts:32,41 Intl.NumberFormat currency '$'; HoldingsSummary.tsx:54-55 retires the Current value tile; CTO 101768 'one authoritative total ... HoldingsSummary drops its total'",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S3",
        "format.ts:32,41 Intl.NumberFormat currency '$'; HoldingsSummary.tsx:54-55 retires the Current value tile; CTO 101768 'one authoritative total ... HoldingsSummary drops its total'",
        "commit 5e6befb7 is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S48",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S6"
    ],
    "spec_asserts": "Unifying format.ts on the identity card's '$1,234.56' style breaks THREE out-of-grant tests that pin the four Holdings-tab formatters' PRIOR code-prefix output verbatim: iv-e-45.face-batch.test.tsx's UIR-29d/UIR-29e arms (`formatMoney(1234567.89,'USD')` no longer equals '1,234,567.89' or 'USD 1,234,567.89'; `formatMoney(-150000,'USD')` no longer .includes('-150,000.00')), plus iv-e-5.allocation-bars.test.ts / iv-t-4.security-list.test.ts / iv-e-13.map-drill.test.ts (not individually re-read line by line, flagged by their own use of `currency: 'USD'` fixtures through the same shared formatter) ",
    "one_line": "W29-S6 GRADUATED: remedied (464b7a37) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "iv-e-45.face-batch.test.tsx:283-289 expects '$1,234,567.89' and '-$150,000.00'; the other candidate files carry no money-string pins",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S6",
        "iv-e-45.face-batch.test.tsx:283-289 expects '$1,234,567.89' and '-$150,000.00'; the other candidate files carry no money-string pins",
        "commit 464b7a37 is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S49",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S7"
    ],
    "spec_asserts": "fe-s-30/predicate.test.ts's F30-AC4 ('a status carrying no state ... UNCERTAIN') fails at this worker's HEAD -- NOT one of the two tests this task order names as IV-e-45's own breakage (only F30-AC5 was named) -- and is a standing residual from a CTO-ruled revert (CTO 101449, commit 96282c4d) that was never actually carried out: that ruling required the feeding tests to be re-classed H or R 'in the follow-on cell that carries the residual' (named as IV-e-35), but IV-e-35's own commits never touch fe-s-30/ at all.",
    "one_line": "W29-S7 GRADUATED: remedied (464b7a37) and disarmed, verified at local portal DEV 3f76cdb2.",
    "world_is": "fe-s-30/_scenarios.ts adds performanceEnvelopeNoStatus(); F30-AC4 re-scoped as class R; public-status.ts untouched. The row cites ruling '101449'; the CTO's ruling is msg 101448 (see header)",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S7",
        "fe-s-30/_scenarios.ts adds performanceEnvelopeNoStatus(); F30-AC4 re-scoped as class R; public-status.ts untouched. The row cites ruling '101449'; the CTO's ruling is msg 101448 (see header)",
        "commit 464b7a37 is an ancestor of local portal DEV 3f76cdb2 (merge-base --is-ancestor)"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S50",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "BLOCKING",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S8"
    ],
    "spec_asserts": "IV-e-50 fixed 8 real, root-caused non-Q S7 residuals (fe-s-14, fe-s-15 x2, fe-s-19, fe-s-25 x2, fe-s-30/F30-AC4) at the fixture/test level, but two more non-Q residuals genuinely require an out-of-grant PRODUCT-code fix and remain failing after this cell: fe-s-45/residuals.test.ts's F45-AC9 (scripts/dev-live.mjs's write measurement) and fe-s-57/carry.test.ts's F57-AC2 (contracts/adapt.ts's carryUnprojectedGrant) -- the suite therefore still does not read exactly the table's 5 Q rows.",
    "one_line": "W29-S8 GRADUATED, OPEN: A 1.0.0_SA_CTO ruling: a product-path cell for the two tests, a wider Q allowance, or another disposition; then the cell it names.",
    "world_is": "F45-AC9 (scripts/dev-live.mjs) and F57-AC2 (contracts/adapt.ts) fail on product paths no open order grants.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S8",
        "no CTO ruling on W29-S8 after msg 101768 (03:44Z) in the COO~D or COO~P inboxes; no open order grants scripts/dev-live.mjs or contracts/adapt.ts",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S51",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S9"
    ],
    "spec_asserts": "A file never named by W21-S3 or W23-S1, src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts, showed genuine run-to-run instability in this cell's own 3-full-run baseline (failed run 1, passed runs 2 and 3, identical committed tree) -- a NEW flaky file this cell's <paths> grant does not cover (dsgn-irptv1/ is only granted iv-e-17.regenerated.test.ts, the s7-*.ts instruments and iv-e-45.face-batch.test.tsx by name).",
    "one_line": "W29-S9 GRADUATED, OPEN: A cell granting iv-e-26.wire-regen.test.ts makes it deterministic, or 1.0.0_SA_CTO folds it into IV-e-50's harness bar.",
    "world_is": "IVE26-AC3 (iv-e-26.wire-regen.test.ts) failed 1 of 3 runs: a flaky test.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S9",
        "no task order grants iv-e-26.wire-regen.test.ts; no CTO ruling folds it into W23-S1",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S52",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:35:56Z",
    "class": "BLOCKING",
    "adjudicates": [
      "DSGN_IRPTV1-W29-S10"
    ],
    "spec_asserts": "A SECOND 3-full-run baseline (this cell's own graded s7-determinism-check.ts invocation, taken ~40 minutes after the first, no edit to any test/fixture file between the two baselines) shows a DIFFERENT internally-stable 7-test failing set than the FIRST baseline's stable 15 -- row W29-S9's own claim ('only 1 of 240 files showed any instability... it has not reached zero [for just that one file]') is SUPERSEDED: the instability is corpus-wide across BOTH baselines, it is just that each individual 3-run sample can land in one of (at least) two internally-self-consistent regimes, not that any one",
    "one_line": "W29-S10 GRADUATED, OPEN: A 1.0.0_SA_CTO ruling on how the S7 bar is graded under run-to-run regimes (a follow-on cell, a wider Q allowance, or another disposition).",
    "world_is": "Two independent 3-run samples of the suite gave different stable failing sets (15 vs 7), so 'only Q rows fail' cannot be graded deterministically on this machine.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-W29-S10",
        "IV-e-50 result: two 3-run samples, 15 vs 7 failing; no CTO ruling on W29-S10",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round7-L8-packet.md@ce13f9af66"
      ]
    }
  },
  {
    "id": "DSGN_IRPTV1-C-S53",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-27T07:41:09Z",
    "class": "OBSERVATION",
    "adjudicates": [
      "DSGN_IRPTV1-S19"
    ],
    "one_line": "S19 GRADUATED, OPEN: the walk screenshots are untracked and ignored locally, but origin/CLOUD's tip still carries 28 of them with real client data, because the untrack is unpushed.",
    "spec_asserts": "Walk artifacts carry client data and stay off git (the ui-walk skill: 'Client data stays local').",
    "world_is": "Locally the lane's disarm is done: 0 tracked shots, and *.shots/ is ignored. On the remote, origin/CLOUD tip 262d0e8d16 still holds 20 + 8 real-client screenshots, because cfed2c067b is local-only; after the push they remain in pushed history.",
    "disposition": "GRADUATED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S19",
        "org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md#DSGN_IRPTV1-S21 (closing evidence: untracked @cfed2c067b, *.shots/ ignored @01d82f1550)",
        "git ls-files of the three .shots folders at HEAD = 0; git check-ignore: deliverables/2.0.0_SA_COO~D/.gitignore:2 '*.shots/'",
        "origin/CLOUD tip 262d0e8d16 (fetched by 3.0.0_SA_CVO): git ls-tree lists 20 files in prod-uiwalk-20260926.shots (added @4f632208c5) and 8 in prod-walk-20260926.shots (added @9b5eed8f9d); w9-round7.shots (@a32823e232) is local-only; cfed2c067b is NOT an ancestor of origin/CLOUD"
      ]
    }
  }
]
```
