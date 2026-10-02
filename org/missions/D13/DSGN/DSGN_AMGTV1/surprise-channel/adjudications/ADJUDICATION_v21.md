# DSGN_AMGTV1 ROUND 23 -- L8 COMPILE + L9 GRADES OF THE THREE ASKED ITEMS -- FWD-2 realized on DEV; FWD-16's reason left the face

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~09:1xZ
**Input:** `2.0.0_SA_COO~D`'s `round23/ROUND23_CLOSE.md` @`3cdc5e9a27` (4,157 B, read to EOF), msg 28346. PRD v0.8 ADMITTED.
**L7:** AV-zb-1, zb-2, zb-4 are VALID per the packet; 0 judgment criteria. The three items the issuer asked this seat to grade are
in section 1.
**Rows past v20:** `Z-W71-S1`, `Z-W71-S2`, `Z-S14` (3 of 45). comp-surprise: open 3, ARMED 0 before this write.

---

## 1. THE THREE GRADES ASKED

| item | grade | what this seat read |
|---|---|---|
| (1) issuer amendment @`ac72f32ba1` to round-22 `codeface.cjs` arm 3 | **SOUND** | Arm 3's purpose (no plain served reason is dropped) now holds through `data-absent-column-reason`. CTO round-22 ruling 1 puts reader words on the face, so AC1 and AC2 no longer contradict (row W71-S1). The no-code arms and the Exec clause are unchanged in the diff. |
| (2) ~73's re-anchor of `claims_with_resolved_cite_equal` (worker commit `72f34f5f`, posture.harness.cjs:483-489) | **SOUND, with two conditions** | The check changes meaning. Before, every claim rested on >= 1 resolved cite. Now a claim with 0 resolved cites counts when the page says "Citation not resolved -- " for EVERY cite and its `data-posture-claim-resolved` equals the cites actually resolved. It keeps teeth: a page that hides an unresolved cite, or misstates the count, still fails. **Conditions:** (a) the name `claims_with_resolved_cite_equal` no longer describes the predicate; (b) the plant (`POSTURE_HARNESS_PLANT=1`) blanks every claim, so it never exercises the new 0-resolved path. One targeted plant is owed: a 0-resolved claim that drops "Citation not resolved" must fail. |
| (3) ~72's python edit, bound 4 (portal `145fe258`) | **SOUND** | `ExecManagementTab.tsx` blob: 21,269 B, 0x08 = 0, non-ASCII 0, CRLF 0. The diff (+19/-10) touches only the cell's intent. The filing is named in words only when the drafting provenance's accession equals the management block's, so another filing is never misattributed. |

## 2. RE-READ -- walk `tmp/ui-walk/20261002T084927Z` (portal 41eeda55, LOCAL worktree 70)

- **FWD-2 (A3): REALIZED on this walk.** `lead-lists.json` has 94 bars and **0** labelled by a ticker alone. This seat's pattern
  flagged one, "SAP SE", which is the company's name.
- **VLO Exec (067):**
  - Officers are named ("Harminder S. "Homer" Bhullar") and roles carry no trailing age, so RESAPP B3 is live. FWD-7's VLO defect
    is gone.
  - The filing line reads "THE 10-K FILED FEBRUARY 25TH, 2026"; no accession.
  - **Still on the face:** the doubled sentence "Contact enrichment was skipped for this company -- Contact enrichment was
    skipped: no company web domain ..." (row S14), and "a SERP not scoped to the company's own domain is not the contract's
    search" (RESAPP B5).
- **VLO Peers (073):**
  - The subject row is 382.86 / 116,115 / 116,978, and the counts line is in reader words.
  - **All 12 absent columns read "<Column> is not available for these peers."** FWD-8's "no internal system text" is met on the
    face.
  - **FWD-16's DONE WHEN ("an 'Absent columns (N)' disclosure lists each with its registry reason") is no longer met on the face.**
    The reason survives only in `data-absent-column-reason`, and "not available" is not a reason. This is the FWD-13 shape: a
    round fix moves content off the face, and ratified text still asks for it there.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W71-S1` | DISMISSED_WITH_REASON | resolved by the amendment @ac72f32ba1, graded SOUND above |
| `Z-W71-S2` | DISMISSED_WITH_REASON | its resolution record. Both rows carry `surfaced_at` "2026-10-02T00:00Z", a placeholder rather than the time they were written |
| `Z-S14` | **GRADUATED** | a doubled sentence on the VLO Exec face, demo-visible. Carried as an OPEN remediation row, owner `2.0.0_SA_COO~D` |

## 4. L10 PRECONDITION

Every task order terminal, 3 of 3. No BLOCKING or ARMED row open. 0 judgment criteria. **MET.**

## 5. WHAT YOU SHOULD HAVE ASKED BUT DID NOT

- **FWD-16 against FWD-8.** The page cannot satisfy both texts with "not available for these peers". Either the face gives a
  reason in reader words (e.g. "the data source does not report share counts"), or FWD-16's DONE WHEN gets an addendum that
  moves the reason to the DOM. Decide before a grade cites either.
- **Still none of this is on PROD.** 41eeda55 is LOCAL in worktree 70, and PROD is b3a1d8a6. The DEV push and the promote are
  Andrew's word.

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S25",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T09:07:00Z",
    "one_line": "Round 23 L9: codeface arm-3 amendment SOUND; ~73's claims_with_resolved_cite_equal re-anchor SOUND with two conditions (the name no longer fits; no plant exercises the 0-resolved path); ~72's python edit SOUND (bytes clean, diff confined). Walk 20261002T084927Z (41eeda55, LOCAL): FWD-2 0 of 94 ticker bars; VLO officers fixed; Peers face clean but FWD-16's 'with its registry reason' left the face.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show ac72f32ba1 -- round22/checks/codeface.cjs: plain reason passes 'peersText.includes(r) || carried.has(r)'; Exec clause unchanged.",
        "portal 72f34f5f posture.harness.cjs: statedResolved + allSaySo replace 'resolvedHere >= 1'; the plant knob blanks every basis claim.",
        "portal 145fe258 src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx blob: 21269 B, 0x08 0, non-ASCII 0, CRLF 0; filingWords() names the form only when prov.accession == management.source_accession.",
        "tmp/ui-walk/20261002T084927Z/lead-lists.json: Trending x Price 94 rows, 0 ticker-only labels.",
        "tmp/ui-walk/20261002T084927Z/shots/073-VLO-US-Peers-expanded.png: 12 of 12 absent items '<Column> is not available for these peers.'; subject 382.86 / 116,115 / 116,978.",
        "tmp/ui-walk/20261002T084927Z/shots/067-VLO-US-Exec-Management.png: 'Harminder S. \"Homer\" Bhullar'; 'THE 10-K FILED FEBRUARY 25TH, 2026'; doubled 'Contact enrichment was skipped' sentence; SERP sentence.",
        "DSGN_AMGTV1_PRD.md FWD-16 DONE WHEN: an \"Absent columns (N)\" disclosure lists each with its registry reason."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-W71-S1",
      "DSGN_AMGTV1-Z-W71-S2"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W71-S1's contradiction is resolved by the amendment graded SOUND here; W71-S2 is its resolution record.",
    "spec_asserts": "The packet asks three grades: the codeface amendment, the BABA re-anchor, the python edit against bound 4.",
    "world_is": "All three SOUND (the re-anchor with two conditions); FWD-16's reason limb left the face in the same round.",
    "notes": "FOR THE CTO: FWD-16 vs FWD-8; one targeted plant for the 0-resolved path; W71-S1/S2 surfaced_at placeholders."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S26",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T09:07:00Z",
    "one_line": "VLO Exec prints the doubled sentence 'Contact enrichment was skipped for this company -- Contact enrichment was skipped: ...' (AV-z-1's lead-in plus RESAPP B2's plain reason); demo-visible; one-line wording item.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20261002T084927Z/shots/067-VLO-US-Exec-Management.png",
        "investigations/INVESTIGATION_v1.md#DSGN_AMGTV1-Z-S14"
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S14"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-11 and the card family: one sentence per fact on the face.",
    "world_is": "The same fact prints twice in one line.",
    "notes": "Carried OPEN in REMEDIATION_v1, owner 2.0.0_SA_COO~D."
  }
]
```

-- 3.0.0_SA_CVO~Z
