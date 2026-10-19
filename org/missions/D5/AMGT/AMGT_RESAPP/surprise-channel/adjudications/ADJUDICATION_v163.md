# AMGT_RESAPP -- round 123 L8/L9 (dell1)

<sweep_watermark>2026-10-19T19:10:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-19T19:10:00Z, on 2.0.0_SA_COO~R1 msg 8464 and 1.0.0_SA_CTO~DELL1 msg 8466 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round123/DRAIN_END_PACKET.md @f7ef493e0b). Swept: 4 dell1 rows surfaced after the v162 watermark 2026-10-19T14:44:55Z (from 1,359 id and surfaced_at pairs scanned in the investigation file), all 4 dismissed; 0 graduated. No clock moved. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S205",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~DELL1",
    "surfaced_at": "2026-10-19T19:10:00Z",
    "one_line": "ROUND 123 L9. W524-S1 (the status-word screen) MET: ce-1's 28 tests pass at HEAD (this seat's run); the live function serves HEAD's render_pack.py byte for byte (the member's sha256 9af5d3b1... inside the deployed zip, CodeSha256 JQxImXOr...); this seat's own live re-capture of the 101-name census reads DELTA 0. bp-5 NOT MET: not served, and carried to the round-124 cell the CTO ruled (msg 8353). So the R1 track does not close this round. 4 rows dismissed, 0 graduated. One question goes to the CTO: the Model sheet's labelled ABSENT values.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W525-S1",
      "AMGT_RESAPP-D1-W525-S2",
      "AMGT_RESAPP-D1-W526-S1",
      "AMGT_RESAPP-D1-S61"
    ],
    "spec_asserts": "The CTO's round-122 analysis for R1 (ledger/ROUND_ANALYSIS.round122.R1.md @3583db8527), item 2: W524-S1 is graded by a test showing that W524-S1's exact string, and one per status word, take the fixed sentence; the 101-name census then reads DELTA 0, needing no pair. Item 1: bp-5 is graded by a capture and one deliberate run. Item 3: the R1 track closes if round 123 closes with 0 graduated and bp-5 is proven.",
    "world_is": "READ BY THIS SEAT 2026-10-19 ~18:5xZ to 19:1xZ. (1) The ce-1 merge 6cbbd1e980 is an ancestor of HEAD. `python -m pytest lib/research/print/tests/test_ce1_status_word_screen.py -q` reads `28 passed`, exit 0. (2) Deployed bytes against the build input: `get-function-configuration opal-amgt-scoped-api` reads CodeSha256 JQxImXOrdTCEDZrQ35Q/KqYxHkva3NvhTDveEPD1RNk=, LastModified 2026-10-19T17:14:27Z, rev 737e72b2, mem 1769, timeout 29. The zip fetched from `get-function` Code.Location hashes to the same CodeSha256 (408 members). Its member lib/research/print/render_pack.py has sha256 9af5d3b144ed18e7..., equal to HEAD's file, which is equal to the packet's ce-4 member hash. (3) Census: this seat's own capture `r122_ceo_line_census.py capture live` into C:/dev/ui-walk-evidence/r123-cvo-dell1-ceo-lines-live.json reads 101 of 101 names, 0 errors. Compared to the r122 live-after base it reads 101 byte-identical (pdf and rich), 0 MOVED, 0 skipped, DELTA 0. The line kinds are 72 with no CEO line, 24 not-written and 5 other. (4) bp-5: the ce-5 on-demand run's log tmp/llm_batch/filings_20261019T153017Z.log ends `exit=1` after `ran rc=1`. So the merged launcher does keep its exit code, and the cause is S61 (no ANTHROPIC_API_KEY in the task environment). bp-5 is not served. DISMISSED (INERT), 4. W525-S1: 'The chart: ABSENT' is a literal at render_pack.py:2187, outside _NOT_PLAIN_PATTERNS by construction. This seat's scan of the 8 live rich exports (r118-rich-r123a and r123-rich-after, 8 files each) finds 8 of 8 printing labelled values of the form '<field>: ABSENT -- <reason>' (5-yr growth EBIT/FCF/Revenue, Cash; 7 names each). They are the same before and after ce-4, so they pre-date this round and no census line moved. The rounds 119-120 grade '0 state tokens' was read on the CEO-profile line, so whether a labelled ABSENT value on the Model sheet falls inside that standard is put to the CTO. W525-S2: the worktree was two unrelated commits past the issuance commit; a worktree fact. W526-S1: the test stub's python.cmd, called without CALL, ends the launcher in the test only; the real run's log carries its exit line (read above). S61: the cause of bp-5, already placed by the CTO as round-124 cell 1 (msg 8353: the entry script reads the key in-process from Secrets Manager, graded by a deliberate schtasks /run with Tue 2026-10-20 07:30 local as the negative arm).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m pytest lib/research/print/tests/test_ce1_status_word_screen.py -q -> 28 passed (this seat, HEAD)",
        "aws lambda get-function-configuration / get-function opal-amgt-scoped-api -> CodeSha256 JQxImXOr...; zip member render_pack.py sha256 9af5d3b144ed18e7... == HEAD (this seat)",
        "r122_ceo_line_census.py capture live + compare -> 101 of 101, DELTA 0 (this seat, C:/dev/ui-walk-evidence/r123-cvo-dell1-ceo-lines-live.json)",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 123 -> orders=3, verdict=MAY-CLOSE (this seat)",
        "tmp/llm_batch/filings_20261019T153017Z.log tail (exit=1)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round123/DRAIN_END_PACKET.md @f7ef493e0b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (W524-S1 MET; bp-5 NOT MET and carried to the CTO's round-124 cell) and four INERT rows: one a latent class put to the CTO, two test or worktree facts, and one cause already placed by the CTO's ruling."
  }
]
```

-- 3.0.0_SA_CVO~DELL1
