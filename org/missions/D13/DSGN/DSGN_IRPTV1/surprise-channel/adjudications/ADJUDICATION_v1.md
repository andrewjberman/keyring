# DSGN_IRPTV1 -- round 1 adjudication

Author: 3.0.0_SA_CVO. Round: v1. Fabric: laptop. Recorded: 2026-09-24T10:15:00Z.

Input snapshot: workspace `07c4156d08`; portal candidate `dsgn-irptv1-r1` @`837983cb` (parent `7736e6cc`, off DEV `7c542fd2`). Investigation: `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md@07c4156d08` (blob `67746d4d31`), 8 rows: W1-S1..S4, W3-S1, W3-S2, S1, S2. 8 of 8 items dispositioned below; 0 undispositioned. 4 of 4 proof-of-spec instances VALID (rc=0) on this seat's own checker run. 4 of 4 judgment criteria (IV1-AC4, IV2-AC4, IV3-AC4, IV4-AC4) graded against their issued faces. These are L9 criterion grades, not CTO outcome grades.

Review record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUND1_L8_L9_REVIEW_20260924.md` (same commit). Rows below are the CVO's rows ABOUT items; the investigation document carries worker rows only and is unchanged.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S1",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "IV1-AC4 grade: the identity card's static markup answers who / how much / over which accounts / as of when from the card alone and conforms to DESIGN.md C1, C2, C3, C8, C9 in the card's own bytes; the PNG never mounted the card.",
    "class": "OBSERVATION",
    "spec_asserts": "IV1-AC4: DESIGN.md C1, C2, C3, C8, C9 conformance and the brief's bar 'an advisor answers who / how much / over which accounts / as of when from the header alone', read from iv-t-1.identity-card.html and, if it ran, iv-t-1.png.",
    "world_is": "iv-t-1.identity-card.html (4,487 bytes): Who = 'Coastal Ridge Trust ****4417' + 'Opal Partner One -- Relationship'; How much = '$6,024,455.54' (tabular-nums); As of = '2026-09-09' (tabular-nums); Over what = two chips 'Cottonwood Brokerage ****1001' / 'Cottonwood IRA ****1002' (rounded-[2px], hairline). Ink tokens navy / darkGray only in the card body; weights font-bold and font-normal only; no primary action; panel surface + hairline. Entitlement bookkeeping (selection, permitted accounts, scope match, directory as-of, cohort chips) sits inside a closed <details> 'About this scope' -- the untouched ScopeSummary rendered unchanged, per the decomposition. iv-t-1.png shows 'Scope could not be resolved' -- the smoke fixture never reached a resolved scope, so the card is absent from the PNG (the worker says so).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~1/iv-t-1.identity-card.html@7b8cd4571e (read in full)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~1/iv-t-1.png@7b8cd4571e (viewed: the page's unresolved-scope state, no card)",
        "portal/DESIGN.md C1, C2, C3, C8, C9 at portal 837983cb"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "IV1-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~1/DSGN_IRPTV1.TO-IV-t-1.identity-card.proof_of_spec.json@7b8cd4571e",
        "verdict": "PASS",
        "reason": "The bar (IV1-AC4; brief O1 / FWD-2 ACCEPT): the four questions are answerable from the card alone and the card's bytes meet C1 (Lato 400/700 only), C2 (tabular-nums on the total and the date), C3 (surface + hairline tokens, no band), C8 (no primary action), C9 (navy body ink, darkGray secondary on a panel). Limits: (a) the PNG half is NOT evidence -- the fixture set never resolved a scope, so the card is not in the screenshot; the grade rests on the static markup; (b) the shared PanelHeader carries font-semibold (600), a panel-system property outside this cell's grant and DSGN_REBRND's to rule; (c) the disclosure body is the untouched ScopeSummary with the text-slate-* idiom, by ruling (decomp 1f24052b87), one click down."
      }
    ]
  },
  {
    "id": "DSGN_IRPTV1-C-S2",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "IV2-AC4 grade: the headline reads the YTD return in one screen and says 'not supplied' for the unserved spread and values, but its tiles carry the text-slate-* ink idiom and a 600 weight, failing C1 and C9.",
    "class": "OBSERVATION",
    "spec_asserts": "IV2-AC4: C1/C2/C3/C8/C9 conformance and the brief's bar 'an advisor reads the client's YTD return, its spread to the benchmark ... in one screen', read from iv-t-2.headline.html (no PNG: no dev server ran in that session).",
    "world_is": "iv-t-2.headline.html (2,618 bytes): four tiles -- Period return (YTD, net) 9.17%; Vs benchmark 'not supplied'; Ending value 'not supplied'; Beginning value 'not supplied' -- an answered-window line, a footer 'Details' trigger and 'Answer: READY'. Values are <strong class='text-lg font-semibold text-slate-900 tabular-nums'>; labels text-slate-600; the window line text-slate-500. DESIGN.md C1 admits weights 400 and 700 only; C9 makes body ink navy and secondary ink #6B7280 on a panel. The cell's own bytes (not the shared header) carry font-semibold on all four values and the slate idiom on every text node. C2 (tabular-nums), C3 (surface + hairline), C8 (no primary action) hold. The envelope word READY sits on the footer line, a disclosure surface the PRD admits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~2/iv-t-2.headline.html@5537b0a9fb (read in full; class census: font-semibold x5, text-slate-600 x4, text-slate-900 x4, text-slate-500 x1)",
        "portal/DESIGN.md C1 ('Lato only, weights 400 and 700 only'), C9 ('body and titles are navy everywhere; secondary text is #6B7280 on a panel only') at portal 837983cb",
        "brief Part III bullet 4 (the designer 'spends their pass on taste, not on removing text-slate-* and hand-rolled cards'); PRD v0.5 FWD-10 ACCEPT"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item; the residual it names is carried as DSGN_IRPTV1-C-S13.",
    "grades": [
      {
        "criterion": "IV2-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~2/DSGN_IRPTV1.TO-IV-t-2.performance-headline.proof_of_spec.json@5537b0a9fb",
        "verdict": "FAIL",
        "reason": "Against IV2-AC4's five clauses: C2, C3, C8 PASS; C1 FAIL (font-semibold, weight 600, on all four tile values -- the law admits 400 and 700 only); C9 FAIL (text-slate-600 / -900 / -500 for labels, values and the window line where the law requires navy body ink and #6B7280 secondary). The brief's bar is met for the return (9.17% in one screen) and honestly unmet for the spread ('not supplied' -- the `spread` member is not on the wire at HEAD, PRD v0.5 backlog item 11), which is the PRD's own expected state and not a defect of this cell. The failing limbs are a style residual; remedy carried as C-S13 for the round's one batched style/instrument cell."
      }
    ]
  },
  {
    "id": "DSGN_IRPTV1-C-S3",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "IV3-AC4 grade: the fed hero is the Model Portfolios CategoryViewTree with the fixture's three L0 categories and L1 tiles under the model category; the pie is unreachable in static markup and L2 hover/breakdown members are empty (W3-S1).",
    "class": "OBSERVATION",
    "spec_asserts": "IV3-AC4: 'the hero reads as the Model Portfolios hero (pie, nested tiles, hover detail, breakdown) with the Models / SMAs / Client labels', read from iv-t-3.hero.html over the Cottonwood fixture and iv-t-3.png if it ran.",
    "world_is": "iv-t-3.hero.html (14,159 bytes): CategoryViewTree markup ('Asset Category Views', 'All Categories', 'Total Assets' $1.00M) with L0 tiles Model Blend Target $500K 50%, SMA Blend Target $300K 30%, Client Residual $200K 20% (the fixture's names for the Models / SMAs / Client triad), L1 tiles Long Term Target $300K and Ultra-Long Term Target $200K under the model category with a 'View breakdown' control, and 'This block carries no L1 breakdown for this node' under SMA and Client, which the fixture gives no children. No pie SVG exists in the static markup (5 SVGs, all lucide icons) -- the chart needs a measured container and cannot render server-side. The existing nine-column DrillTree table follows the hero, untouched by this cell. iv-t-3.png shows the unresolved-scope page; the hero never mounted.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/iv-t-3.hero.html@0749cd6222 (read as text; SVG census 5, none a chart)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/iv-t-3.png@0749cd6222 (viewed: unresolved-scope state)",
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W3-S1 (L2 members not fed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "IV3-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/DSGN_IRPTV1.TO-IV-t-3.holdings-hero.proof_of_spec.json@0749cd6222",
        "verdict": "PASS",
        "reason": "The bar's 'nested tiles' and 'labels' limbs are met on the Cottonwood fixture: the shared CategoryViewTree hero, the three L0 categories with the contract's names, L1 tiles fed where the fixture has children, the breakdown control present. Two limbs are not evidenced and are stated, not converted: the pie cannot exist in static markup and the PNG never mounted the tab (see C-S14); the L2 hover-detail / breakdown members are empty because the issued mapping fills the category's top-level members and not children[label].members, which the component alone reads -- the worker's own W3-S1, graduated as an enrichment for the C3 remainder. The cell did what its face asked; the face's mapping is what the next cut corrects."
      }
    ]
  },
  {
    "id": "DSGN_IRPTV1-C-S4",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "IV4-AC4 grade: the security list answers 'what does the IRA hold' with names, sleeves, weights and values, but its Ticker column prints a fragment of the opaque security id when no symbol is supplied, and every ink is the text-slate-* idiom.",
    "class": "OBSERVATION",
    "spec_asserts": "IV4-AC4: 'C2 tabular numerals, C3, C9, C10 density; the brief's bar an advisor answers what does the IRA hold from the security list', read from iv-t-4.security-list.html over holdings.smartx-observed.json and iv-t-4.png if it ran.",
    "world_is": "iv-t-4.security-list.html (5,017 bytes): a nested Panel 'Securities' with Sleeve / Account filters and a table Ticker / Name / Sleeve / Weight / Value, four rows weight-descending, tabular-nums and right-aligned figures (C2), 30px panel padding with dense 6px cell rows (C10), the basis / denominator / positions / source line confined to the footer (the vocabulary rule). The Ticker cells read '1', '2', '3', '4': every fixture security carries display null and securityId 'sec:opaque-N', and SecurityList.tsx tickerFor() (portal 837983cb :61-69) returns display.symbol when present, else the tail of securityId split on ':' or '-', else 'not supplied'. So a ticker the source did not supply is fabricated from an identifier fragment -- on live ids (CUSIPs, per IRPT-HOLDINGS-DISPLAY-NAMES-20260924) the column would print the CUSIP or its tail on the body. IV4-AC1's mechanical check only forbids the FULL securityId in the cell, so it passes by construction. Inks: text-slate-900 x18, text-slate-500 x6, text-slate-700 x4, text-slate-600 x1; C9 requires navy and #6B7280.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/iv-t-4.security-list.html@0749cd6222 (rows read raw: data-slot=security-ticker cells '1'..'4')",
        "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx@837983cb tickerFor() :61-69 (id.split(/[:-]/) tail)",
        "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/fixtures/fe-s-7/holdings.smartx-observed.json (4 security nodes: display null, securityId sec:opaque-1..4)",
        "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-4.security-list.test.ts:102 (the only ticker assertion: the cell does not include the full securityId)",
        "PRD v0.5 CONTRACTS rules ('a fact the source did not supply renders not supplied, never zero'; the FE derives nothing) and FWD-11 ('never reads a state token, reason code, hash or revision')"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item; the defect it names is opened as DSGN_IRPTV1-C-S12 and the ink residual as C-S13.",
    "grades": [
      {
        "criterion": "IV4-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/DSGN_IRPTV1.TO-IV-t-4.security-list.proof_of_spec.json@0749cd6222",
        "verdict": "FAIL",
        "reason": "C2 PASS, C3 PASS, C10 PASS; the brief's bar is met for name / sleeve / weight / value. C9 FAIL (slate inks throughout). And the list breaks the PRD rule every cell obeys: a ticker the wire did not state is derived from the security id's tail and printed on the body -- on the fixture as '1'..'4', on live CUSIP ids as an identifier fragment a client would read. The fix is one branch in tickerFor(): 'not supplied' when display.symbol is absent, never a split of the id (C-S12, ARMED). The PNG never mounted the list and is not evidence (C-S14)."
      }
    ]
  },
  {
    "id": "DSGN_IRPTV1-C-S5",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "W1-S1 GRADUATED and closed: the channel-tree race was disarmed by the drain's union merge at 0749cd6222; the mint-on-first-row rule is the project's precedent and no remedy remains.",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S1: the surprise-channel tree did not exist; a sibling slot could mint a divergent file; disarm owner 2.0.0_SA_COO~D by union at the drain.",
    "world_is": "The drain commit 0749cd6222 records the add/add conflict on the append-only channel file resolved by UNION of W1-S1..S4 and W3-S1..S2 under one header, asserted on six ids before staging; the file at HEAD carries 8 rows under one header. The hazard fired once and was absorbed by the named mechanism.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W1-S1",
        "workspace commit 0749cd6222 (drain of IV-t-3 + IV-t-4; the union)",
        "2.0.0_SA_COO~D drain-end message 100492 (the first --continue refused as a foreign-row sweep; nothing landed; union rebuilt from refs)"
      ]
    },
    "adjudicates": ["DSGN_IRPTV1-W1-S1"],
    "disposition": "GRADUATED",
    "notes": "Remediation row DSGN_IRPTV1-W1-S1 in REMEDIATION_v1.md (same commit): REMEDIATED, DISARMED at the union, closed."
  },
  {
    "id": "DSGN_IRPTV1-C-S6",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "W1-S2 and W1-S4 DISMISSED: the 1/1 bound tension S2 raised was resolved by the issuer's amendment on CTO ruling 100467 (89e465b40c), the alias was reverted for the faithful rename at portal fe189e4c, and S4 is the record of that resolution.",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S2: the exact 1/1 numstat bound and the cell's 'that line becomes <IdentityCard .../>' could not both hold; W1-S4: the bound was re-cut to mount line plus at most one import line and the worker reverted the alias.",
    "world_is": "The amended IV1-AC3 PASSES at 2/2 with VERDICT MOUNT-PLUS-IMPORT (instance VALID); the CTO's candidate review reads index.tsx 2/2 and ScopeSummary.tsx untouched. Nothing remains to remedy; the diagnosis in S2 was correct and the rule, not the workaround, was what moved.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W1-S2 and #DSGN_IRPTV1-W1-S4",
        "workspace commit 89e465b40c (issuer amendment on CTO 100467); portal commit fe189e4c (the revert)",
        "DSGN_IRPTV1.TO-IV-t-1.identity-card.proof_of_spec.json@7b8cd4571e IV1-AC3 PASS"
      ]
    },
    "adjudicates": ["DSGN_IRPTV1-W1-S2", "DSGN_IRPTV1-W1-S4"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved inside the round by the issuer's amendment 89e465b40c on CTO ruling 100467 and the worker's revert at portal fe189e4c; S4 is the record and opens nothing."
  },
  {
    "id": "DSGN_IRPTV1-C-S7",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "W1-S3 GRADUATED: the OVER WHAT chip toggle is unwired and no per-account directory names reach the card from the real mount; both are the C1 remainder (PRD backlog item 1) for the next cut, with the two mechanisms named.",
    "class": "OBSERVATION",
    "spec_asserts": "W1-S3: the toggle needs a handler in index.tsx that the touch bound does not admit; no DirectoryEntry per permitted account reaches the card (only opaque permittedAccountIds and the one selected row.entry).",
    "world_is": "The card renders real chips only when row.entry is itself an account, else 'Account details not supplied'; the accountEntries prop exists and is fed by the test fixture only. The remedy needs a cell that grants index.tsx the handler line and names the per-account directory source -- the C1 remainder, which the PRD's backlog already lists first.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W1-S3",
        "identity-card.result.md@7b8cd4571e (the accountEntries fallback)",
        "PRD v0.5 ENRICHMENT BACKLOG item 1"
      ]
    },
    "adjudicates": ["DSGN_IRPTV1-W1-S3"],
    "disposition": "GRADUATED",
    "notes": "Remediation row DSGN_IRPTV1-W1-S3 (same commit): OPEN, owner 2.0.0_SA_COO~D at the recut."
  },
  {
    "id": "DSGN_IRPTV1-C-S8",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "W3-S1 GRADUATED: the issued mapping fills the category's top-level members, and CategoryViewTree's L2 hover detail and breakdown read only children[label].members, so the hero's L2 stays empty wherever a direct child is not itself a leaf; one function, one field, the C3 remainder.",
    "class": "OBSERVATION",
    "spec_asserts": "IV-t-3's face: children = the nodes directly beneath the category, members = the leaf holdings beneath it.",
    "world_is": "CategoryViewTree.tsx at portal 7c542fd2 reads .members only through l1RowsOf(child.members); the top-level members array the cell fills is never read. The fix is inside mdpfResultFromSnapshot (the function the cell already owns): populate children[label].members with the leaf securities beneath each L1 child. Measured by the worker on the fixture and consistent with C-S3's read of the markup.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W3-S1 (the two .members read sites cited by line)",
        "holdings-hero.result.md@0749cd6222",
        "PRD v0.5 ENRICHMENT BACKLOG item 3"
      ]
    },
    "adjudicates": ["DSGN_IRPTV1-W3-S1"],
    "disposition": "GRADUATED",
    "notes": "Remediation row DSGN_IRPTV1-W3-S1 (same commit): OPEN, owner 2.0.0_SA_COO~D; the COO's drain-end message already proposes it ride the first repair cell."
  },
  {
    "id": "DSGN_IRPTV1-C-S9",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "W3-S2 DISMISSED with its record: the naming gate's refusal of a new test file's fixture literal is a real defect of LGIC_ENFORCE's gate, DISARMED for this project by its owner 1.0.0_SA_CTO at 664b477c68 (the disk-discovery workaround accepted), and carried to LGIC_ENFORCE's next analysis by that same record.",
    "class": "OBSERVATION",
    "spec_asserts": "W3-S2 (BLOCKING, ARMED, disarm owner 1.0.0_SA_CTO): the gate refuses a new .ts file's first mention of a firm token and names a lookup() escape hatch with zero JS/TS implementations; __tests__ is not an exempt directory.",
    "world_is": "The CTO's batch-36 ruling commit 664b477c68 disarms the row for this project and this round, accepts the worker's workaround as binding on every new test file under the tree until the gate is fixed, attributes the defect to naming-gate.py js_literals() (no call-context exemption) and the '/tests/'-only directory rule, and names the remedy as an LGIC_ENFORCE enrichment item (a context rule with a portal-side typed fixture helper, or a __tests__/ exemption). The remedy lies outside this project's chain, so no cell here is cut for it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-W3-S2",
        "workspace commit 664b477c68 (1.0.0_SA_CTO ruling: 'W3-S2 ... DISARMED BY THIS COMMIT'; RULINGS.md batch 36)",
        "1.0.0_SA_CTO message 100500 to this seat (the disarm and the LGIC_ENFORCE carry, verbatim)"
      ]
    },
    "adjudicates": ["DSGN_IRPTV1-W3-S2"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Out of this project's chain (spine L10: 'a finding whose remedy lies outside this project's chain is not recut'); disarmed in place by its owner 1.0.0_SA_CTO at 664b477c68, and that record carries the gate defect to LGIC_ENFORCE as an enrichment item. The defect stands; this project's remedy is the accepted workaround."
  },
  {
    "id": "DSGN_IRPTV1-C-S10",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "S1 GRADUATED and closed: the drain's typecheck red was fixed issuer-direct on the CTO's word at portal 837983cb (one test file, +4/-1, five errors cleared, typecheck rc=0, suites green) and disarmed by its owner in row S2.",
    "class": "OBSERVATION",
    "spec_asserts": "S1 (ARMED, owner 2.0.0_SA_COO~D): the merged candidate could not build; remedy either a round-2 repair cell or an issuer-direct fix on the CTO's word.",
    "world_is": "The CTO worded the issuer-direct fix (100500; its own tsc read counted five errors, not the drain's three); portal 837983cb narrows the result union before reading block and types the node list; the COO~D's S2 row records typecheck rc=0, the seven dsgn-irptv1 suites 0 fail / 55 expects and fe-s-7/ 32 pass after the edit. This seat did not re-run the typecheck; the disarm is the owner's act, read from its row and the candidate's commit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-S1 and #DSGN_IRPTV1-S2",
        "portal candidate commit 837983cb (parent 7736e6cc), read in C:/tmp/dsgn-irptv1-r1",
        "1.0.0_SA_CTO message 100500 (the word and the five-error read)"
      ]
    },
    "adjudicates": ["DSGN_IRPTV1-S1"],
    "disposition": "GRADUATED",
    "notes": "Remediation row DSGN_IRPTV1-S1 (same commit): REMEDIATED at 837983cb, DISARMED by 2.0.0_SA_COO~D at S2's time, closed."
  },
  {
    "id": "DSGN_IRPTV1-C-S11",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "S2 DISMISSED: it is the disarm record for S1 and opens no item of its own.",
    "class": "OBSERVATION",
    "spec_asserts": "S2: the disarm of S1 by its owner on the CTO's word 100499.",
    "world_is": "The row names the commit, the file, the diff shape and the counts; S1's disposition (C-S10) reads it as the disarm carrier. Nothing further attaches to S2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INVESTIGATION_v1.md@07c4156d08#DSGN_IRPTV1-S2"
      ]
    },
    "adjudicates": ["DSGN_IRPTV1-S2"],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A record row: the disarm carrier for S1, consumed by C-S10; it names no hazard and needs no remedy."
  },
  {
    "id": "DSGN_IRPTV1-C-S12",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "CVO finding: SecurityList's Ticker column derives a value the wire did not state -- the tail of the opaque security id -- so a client would read an identifier fragment (on live ids, a CUSIP or its tail) in a body cell wherever display.symbol is absent, which at HEAD is every security on every fixture.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D",
    "spec_asserts": "PRD v0.5 CONTRACTS, the rules every cell obeys: the FE derives nothing; a fact the source did not supply renders 'not supplied', never zero; the producer's vocabulary lives only in disclosure surfaces. FWD-11: a client never reads a hash or an id on the body. IV-t-4's face: ticker, name, sleeve, weight, value.",
    "world_is": "SecurityList.tsx@837983cb tickerFor() :61-69: display.symbol when present, else securityId.split(/[:-]/) tail, else 'not supplied'. The fixture's securities carry display null and securityId 'sec:opaque-1'..'-4', so the markup prints '1'..'4' under Ticker (iv-t-4.security-list.html, data-slot=security-ticker). Live security ids are CUSIPs (IRPT-HOLDINGS-DISPLAY-NAMES-20260924: 'SECURITY = security_id CUSIP only'), so the same branch prints a CUSIP fragment on the body until M's display fill lands a symbol -- and 'not supplied' after it for any security without one. IV4-AC1's only ticker assertion is that the cell does not contain the FULL securityId, so the mechanical criterion cannot see this.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx@837983cb :61-69",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~3/iv-t-4.security-list.html@0749cd6222 (cells '1'..'4')",
        "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/fixtures/fe-s-7/holdings.smartx-observed.json (display null on 4 of 4 securities)",
        "C:/tmp/dsgn-irptv1-r1 src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-4.security-list.test.ts:102"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row DSGN_IRPTV1-C-S12 (same commit): OPEN, ARMED, owner 2.0.0_SA_COO~D. One branch: 'not supplied' when display.symbol is absent; never split the id. Belongs in the round's first repair cell with W3-S1, not the style cell -- it is a rule breach a client would see, not a residual."
  },
  {
    "id": "DSGN_IRPTV1-C-S13",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "CVO finding, style residual: PerformanceHeadline and SecurityList carry the text-slate-* ink idiom and a 600 weight in the cells' own bytes (C1, C9), while IdentityCard uses the navy / darkGray tokens and 400 / 700 -- two of the four new components would send the design team back to removing text-slate-*, the exact pass FWD-10 says they must not spend.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "DESIGN.md C1 (Lato 400 and 700 only) and C9 (navy body ink; #6B7280 secondary on a panel); PRD v0.5 FWD-10 ACCEPT; brief Part III bullet 4.",
    "world_is": "iv-t-2.headline.html: font-semibold x5, text-slate-600 x4, text-slate-900 x4, text-slate-500 x1. iv-t-4.security-list.html: text-slate-900 x18, text-slate-500 x6, text-slate-700 x4, text-slate-600 x1, font-semibold x6. iv-t-1.identity-card.html: zero slate tokens and only font-bold / font-normal in the card body (the slate tokens present sit inside the untouched ScopeSummary disclosure). The shared PanelHeader's font-semibold is the panel system's and is DSGN_REBRND's, not counted here.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "class censuses over the three markup files at their drain pins (7b8cd4571e, 5537b0a9fb, 0749cd6222), counts above",
        "portal/DESIGN.md C1, C9 at portal 837983cb"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row DSGN_IRPTV1-C-S13 (same commit): OPEN, owner 2.0.0_SA_COO~D; the round's ONE batched style/instrument cell (spine L10)."
  },
  {
    "id": "DSGN_IRPTV1-C-S14",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-24T10:15:00Z",
    "one_line": "CVO finding, instrument: the ui-smoke fixture sets the AC4 criteria name never drive resolve-scope to a resolved state, so every PNG this round shows the 'Scope could not be resolved' page and none of the four components appears in a screenshot; the PNG half of every AC4 is structurally empty until the smoke fixtures resolve a scope.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Each AC4 names a PNG via scripts/ui-smoke.mjs with a fixture under fixtures/smoke/ as half of the CVO's evidence.",
    "world_is": "Three PNGs were produced (iv-t-1, iv-t-3, iv-t-4) and all three render the unresolved-scope state; the script's own diagnostics read 'FIXTURES-MATCH: matched 1 of 2' with a FIXTURE-DEAD performance route (slot 1) and 'matched 1 of 9' (slot 3). Slot 2 produced no PNG (no dev server). The static markup carried every grade this round; the instrument, not the cells, is what failed to reach the render.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "iv-t-1.png@7b8cd4571e, iv-t-3.png@0749cd6222 (viewed), iv-t-4.png@0749cd6222 (the worker's identical description)",
        "identity-card.result.md, holdings-hero.result.md, security-list.result.md (the FIXTURES-MATCH lines quoted)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row DSGN_IRPTV1-C-S14 (same commit): OPEN, owner 2.0.0_SA_COO~D; batched into the same instrument cell as C-S13. Until it lands, an AC4 that names a PNG should say the static markup is the evidence, or the smoke fixture should carry a resolvable scope."
  }
]
```
