# AMGT_RESAPP -- round 122 L8/L9 and the R1 endpoint read (dell1)

<sweep_watermark>2026-10-19T14:44:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-19T14:44:55Z, on 2.0.0_SA_COO~R1 msg 8280 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round122/DRAIN_END_PACKET.md (sha256 f34782b1b9022f8d...)). Swept: 2 dell1 rows never named, both dismissed; 0 graduated. Clocks: REMEDIATION_v61 C-S203 remediated in place; REMEDIATION_v59 W518-S2 re-closed by appended line. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S204",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-19T14:44:55Z",
    "one_line": "ROUND 122 L9 and the R1 ENDPOINT READ. C-S203 MET: render_pack.py _ceo_profile_sentence (lines 1016-1041 at HEAD) has a branch for every known reading, a fixed sentence per state for a non-plain reason, and the third sentence for an unknown reading; the not-written words belong to NOT_WRITTEN alone. The 101-name census is DELTA 0 against the live function. So C-S203 and W518-S2 close. FWD-5 printed pack: MET (held since round 117). Surface parity, the CEO line on page, PDF and export: MET on the measured names, with the limits named. 2 rows dismissed, 0 graduated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W524-S1",
      "AMGT_RESAPP-D1-W524-S2"
    ],
    "spec_asserts": "The CTO's round-121 analysis for R1 (ledger/ROUND_ANALYSIS.round121.R1.md @48c576b954): C-S203 graded by a per-state test with a non-plain reason and the 101-name census, with DELTA 0 needing no pair; one live read of TSM US and HD US under a real staff login, on the page and in the PDF; then, with 0 graduated, the R1 endpoint read (FWD-5 and the surface-parity outcomes), per ROUND_ANALYSIS.round120.R1.md item 2.",
    "world_is": "READ BY THIS SEAT 2026-10-19 ~14:4xZ. Packet hash verified (the FINAL copy). lib/research/print/render_pack.py:995-1041 at HEAD: NOT_WRITTEN and UNREADABLE_OBJECT print their own sentences, and CONFIRMED with a url prints the url. _CEO_PROFILE_FIXED_BY_READING maps SEARCHED_NOTHING_FOUND, NOT_SEARCHED, SEARCHED_LINKS_UNREADABLE and SEARCH_FAILED each to a fixed sentence, used only when the reason is not plain. Any other reading prints 'the state of this profile is not recognised by this document.' None of the fixed sentences says 'not on file', 'no public profile', 'never written' or 'has been written'. The old fallback 'no public profile is on file yet' is gone. The issuer reports the cd-1 test file read 23 failed, 16 passed at base and 39 passed after, with the seven CEO files at 143 passed before and after. Census (the issuer's, live after the cd-4 apply, UdNfBJqF... at 22:39Z): 101 names in both captures, 101 byte-identical, 0 MOVED, DELTA 0. The lines split 72 with no CEO line, 24 not-written, 5 a plain reason or link. Live hop (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round122/LIVE_HOP_REAL_LOGIN_D729EE6D.md): the /ui-walk service account under a real login on a local dev:live build of PROD d729ee6d, against the live data and live auth. TSM US's page prints 'CEO public profile: No CEO profile has been written for this company yet.' and HD US's prints its searched sentence, with the real data loaded. The print route answers 200 under the login (TSM US pdf 107766 B, HD US pdf 124242 B), but the PDF content under that login was not read; its lines come from the same function by direct invocation, which the census covers. R1 ENDPOINT. FWD-5 (each live printed pack reads as a document): MET at round 117 (ADJUDICATION_v155 C-S191). Every round since held it: 0 paths, order ids or state tokens; recommendation-led Summaries; the page's currency rule; labelled cleared passages. The issuer's leak scan reads 101 clean of 101 and money vs page 16 of 16. SURFACE PARITY: the CEO line and Management section agree page = PDF = rich export on TSM US and HD US under the login, PDF = export on 101 of 101 (census), and cross-surface 8 of 8; money vs page 16 of 16. The limits, named: the PDF under a real login was read by status and size, not by content; the page under login covers two names; the corrupt case is a fixture. PACK FORM 5 of 8 NO (the issuer's read against SC1's capture 14h40m earlier): read as a market-data move, not a render defect. The changed lines are values (share price, market cap, beta, consensus figures on GOOGL US, ICICIBC IN, HD US); sections, labels and money-line counts match; SC1's same-session read is YES 8 of 8. bp-5 (G4 positive arm) is NOT shown: the 11:30Z fire returned rc=1 with no output kept. The CTO has placed the capture cell in round 123; it is outside the R1 endpoint. DISMISSED (INERT). W524-S1: a plain reason that itself carries a status word (for example 'ABSENT, ...') would print as served, because the plain-words mapper does not screen status words. It is latent: the 101-name census shows no such printed line. Whether the mapper should treat a status word as not plain is put to the CTO. W524-S2: the sparse worktree lacked the schema file, and the row was shaped from HEAD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/research/print/render_pack.py:995-1041 at HEAD (read by this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round122/LIVE_HOP_REAL_LOGIN_D729EE6D.md",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 122 -> orders=2, verdict=MAY-CLOSE (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round122/DRAIN_END_PACKET.md (sha256 f34782b1b9022f8d...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (C-S203 MET; the R1 endpoint read) and two INERT rows, one latent on the census and one a worktree fact."
  }
]
```

-- 3.0.0_SA_CVO
