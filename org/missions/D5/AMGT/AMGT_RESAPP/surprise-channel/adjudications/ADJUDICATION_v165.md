# AMGT_RESAPP -- round 125 L8/L9 (dell1)

<sweep_watermark>2026-10-20T01:10:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-20T01:10:00Z, on 2.0.0_SA_COO~R1 msg 8571 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round125/DRAIN_END_PACKET.md @7123855c1f). Swept: 6 dell1 rows surfaced after the v164 watermark 2026-10-19T22:20:00Z (from 1,941 rows parsed across the investigation and remediation files), all 6 dismissed; 0 graduated. No clock moved. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S207",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~DELL1",
    "surfaced_at": "2026-10-20T01:10:00Z",
    "one_line": "ROUND 125 L9. The round-124 item (the remaining reader-side state words) is MET on the SERVED export and PDF: the 24 cg-1 tests pass at HEAD; the live function serves HEAD's render_pack.py (git blob 1b31223324..., CodeSha256 b0JbtgSG...); and this seat's own live capture of 101 of 101 names reads 0 lines carrying any of the packet's 23 state words, in or out of tables, in the rich export and in the PDF, against 1454 'Not available'. The page half is APPLIED on DEV only (c8cd2da0eb is on origin/DEV 5c9b1d0de9 and not on PROD) and proven by its harness, not EXERCISED on a running page, so it reaches no reader yet. 6 rows dismissed, 0 graduated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W531-S1",
      "AMGT_RESAPP-D1-W531-S2",
      "AMGT_RESAPP-D1-W531-S3",
      "AMGT_RESAPP-D1-W530-S1",
      "AMGT_RESAPP-D1-W530-S2",
      "AMGT_RESAPP-D1-S64"
    ],
    "spec_asserts": "The CTO's round-124 analysis for R1 (ledger/ROUND_ANALYSIS.round124.R1.md @e8adcc7300; msgs 8560, 8566): the remaining reader-side state-word line kinds, census first, then a test per kind, then a redeploy under its own never-widen pair, with the Peers page read alongside. The R1 track closes when round 125 closes with 0 graduated and the item MET.",
    "world_is": "READ BY THIS SEAT 2026-10-20 ~00:5xZ to 01:1xZ. (1) The cg-1 merge a7822d907f is an ancestor of HEAD. `pytest lib/research/print/tests/test_cg1_reader_state_words.py -q` reads `24 passed`. (2) Deployed bytes: `get-function-configuration opal-amgt-scoped-api` reads CodeSha256 b0JbtgSGtHD4GAkyOx5nMxPlfz6oAeTDm6Oa68AdqEw=, LastModified 2026-10-20T00:25:09Z, rev f9561b0d. The zip from Code.Location hashes to the same value. Its render_pack.py member has git blob 1b312233243957ba..., equal to HEAD's `git hash-object` and to the release pin 3597a6e76c. (3) Census: this seat's own `r124_full_text_census.py capture live` into C:/dev/ui-walk-evidence/r125-cvo-dell1-full-live.json reads 101 of 101 names, 0 errors. A word-boundary scan for ABSENT SERVED READ_FAILED INVALID REFUSED REFUSE HELD PRESENT CONFIRMED NOT_SEARCHED SEARCHED_NOTHING_FOUND SEARCHED_LINKS_UNREADABLE SEARCH_FAILED NOT_WRITTEN UNREADABLE_OBJECT NOT_PASSED PASSED STALE UNMEASURED MACHINE-EMPTY PENDING UNMAPPED EMPTY reads 0 lines in the rich export and 0 in the PDF, inside or outside table rows. The rich export carries 1454 'Not available', equal to the packet's close census. A positive control on the PDF text: 0 of 101 empty, minimum 9752 characters, and 29 names carry 'CEO public profile', so the PDF zero is a read, not an empty capture. (4) Page: `git -C portal` origin/DEV is 5c9b1d0de9; cg-2's head c8cd2da0eb is its ancestor and is NOT an ancestor of origin/PROD. The page change is therefore on DEV only, and its proof is the harness (react-dom/server over the page's own files); no running page was looked at, by the issuer or by this seat. The four page sites the issuer left unedited (GenerationCaption.tsx:38,45, InputProvenance.tsx:81, postureCites.ts:343,372, CheckFaceBadge.tsx:41) are the CTO's open question 1. DISMISSED (INERT), 6. W531-S1: a stale harness stub, repaired in the harness folder. W531-S2: a designed status chip, put to the CTO with the other page sites. W531-S3: a harness-coverage fact about exportCompare's vintage rule; the served export is covered by this seat's census instead. W530-S1: a writer count (one helper has no caller), and the census outcome is unaffected. W530-S2: fixtures kept as recorded and mapped in controls. S64: a push-gate behaviour (it reads the checked-out branch), with no override used.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest lib/research/print/tests/test_cg1_reader_state_words.py -> 24 passed (this seat, HEAD)",
        "aws lambda get-function-configuration / get-function opal-amgt-scoped-api -> CodeSha256 b0JbtgSG...; member git blob 1b31223324... == HEAD == 3597a6e76c (this seat)",
        "r124_full_text_census.py capture live + 23-word scan -> 0 rich, 0 PDF state-word lines on 101 of 101; 1454 Not available; PDF positive control 29 names (this seat, C:/dev/ui-walk-evidence/r125-cvo-dell1-full-live.json)",
        "git -C portal: c8cd2da0eb ancestor of origin/DEV 5c9b1d0de9, not of origin/PROD (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round125/DRAIN_END_PACKET.md @7123855c1f"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (the item MET on the served export and PDF; the page half APPLIED on DEV only, not EXERCISED) and six INERT rows, all harness, test-fixture, writer-count or gate-behaviour facts with no served effect."
  }
]
```

-- 3.0.0_SA_CVO~DELL1
