# AMGT_RESAPP -- round 121 L8/L9 (dell1)

<sweep_watermark>2026-10-18T17:56:34Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T17:56:34Z, on 2.0.0_SA_COO~R1 msg 8195 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round121/DRAIN_END_PACKET.md @f954e636d0 (sha256 540f75fdc2790d95...)). Swept: 4 dell1 rows never named, all dismissed. REMEDIATION_v59 W518-S2 advances in place (REMEDIATED, closed; its disarm was written at REMEDIATION_v60 C-S200). The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S201",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T17:56:34Z",
    "one_line": "ROUND 121 L9: the CTO's three cases MET on the running Exec Management tab (PROD d729ee6d, portal-v2.1.241). TSM US prints 'CEO public profile: No CEO profile has been written for this company yet.'; a forced corrupt TSM US prints 'CEO public profile: The CEO profile could not be read.'; HD US prints 'CEO public profile (EDWARD P. DECKER): searched, nothing found -- The CEO web search returned 10 url(s) ...'. The census names every consumer of the reading word, so REMEDIATION_v59 W518-S2 closes in place. 4 rows dismissed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W523-S1",
      "AMGT_RESAPP-D1-W523-S2",
      "AMGT_RESAPP-D1-W523-S3",
      "AMGT_RESAPP-D1-W523-S4"
    ],
    "spec_asserts": "The CTO's round-120 analysis for R1 (ledger/ROUND_ANALYSIS.round120.R1.md @4bae75b9e6, msg 8148): census every consumer of the CEO reading word; each handles the three states explicitly; the types.ts union gains the words; the fallback is never the not-written sentence; W518-S2 closes when the census is clean; graded on the running page. REMEDIATION_v59 W518-S2: close when the served reading reads the not-written state where the profile is null, and a census of the label's consumers names each one.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~18:0xZ. Packet hash verified. I viewed the three screenshots (C:/dev/ui-walk-evidence/r121-page/tsm_live.png, tsm_corrupt.png, hd_live.png (research data only; stay local)). tsm_live: the Exec Management tab shows the research team's management passage (Source: TSMC research pack 4_30_2026), the Bloomberg roster and 'CEO public profile: No CEO profile has been written for this company yet.' tsm_corrupt: the same page with 'CEO public profile: The CEO profile could not be read.' hd_live: the filing roster with tenure, and 'CEO public profile (EDWARD P. DECKER): searched, nothing found -- The CEO web search returned 10 url(s), none of them on ir.homedepot.com, so no page could be confirmed as the company's own ...'. The three sentences differ, and none falls back to the not-written sentence. Caveat, stated by the issuer and visible on all three: the page ran on the live bundle in headless Edge with a stubbed session, fed the served /thesis body as a fixture. The identity header reads 'could not be loaded' because it was not fed. So this is the running page's code on served data, not a staff login. The issuer tied the live site to PROD d729ee6d by bytes: index.html and six entry assets equal run 39149629746's artifact, and the marker chunk equals live, with the prior artifact carrying 0. CENSUS (the issuer's, in the branch's ceoConsumerCensus.json). portal/src: 52 hits in 14 files; every consumer is in ExecManagementTab.tsx and handles SERVED, NOT_WRITTEN, UNREADABLE_OBJECT and SEARCHED_NOTHING_FOUND, each with its own sentence; types.ts gains NOT_WRITTEN. lib/: 332 hits in 50 files, with 9 consumers. render_pack.py prints NOT_WRITTEN, UNREADABLE_OBJECT and SERVED explicitly, and the served searched reason for SEARCHED_NOTHING_FOUND (HD US's PDF line, read at round 118, carries that sentence). block_mgmt_bio.py takes facts from a resolved profile only and prints no state sentence. infra/: 0. This seat reads W518-S2's close as met: every consumer is named, and each handles the three states the CTO named. Whether the PDF should also get an explicit SEARCHED_NOTHING_FOUND branch is put to the CTO in the slug; it does not hold the close. The landing: DEV..PROD = 0 after the fold-back (the issuer's ls-remote read), and the release counts 0 client-facing pages. Checked by this seat on the round-120 TSM US PDF: the 3 non-ASCII characters are U+2019 apostrophes in the served passage, not mojibake. DISMISSED (INERT). W523-S1 and W523-S2: the two lib consumers, read above. W523-S3: no harness pinned the old sentence. W523-S4: a CONFIRMED reading always carries a url by construction, so the page's third sentence is the right fallback.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/dev/ui-walk-evidence/r121-page/tsm_live.png, tsm_corrupt.png, hd_live.png (research data only; stay local) (viewed by this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round121/LIVE_TIE_AND_PAGE_READ_D729EE6D.md",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 121 -> orders=2, verdict=MAY-CLOSE (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round121/DRAIN_END_PACKET.md @f954e636d0 (sha256 540f75fdc2790d95...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (the CTO's three cases MET on the running page; W518-S2 census clean) and INERT census and premise rows."
  }
]
```

-- 3.0.0_SA_CVO
