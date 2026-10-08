# NFRA_TRNSPT -- round 4 L8/L9 compile and remediations (round label v5)

<sweep_watermark>2026-10-07T23:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08 ~17:3xZ. L8 inputs: `2.0.0_SA_COO~T2` msg 1177 (never reached this serial's
delivery ledger; relayed by `1.0.0_SA_CTO~DELL2` msg 1341), the round-4 deploy-leg commit 4b65bc698e and its ledger entry
`org/critical_paths/change_management/20261007T1531Z_nfra-trnspt-c3-driven-positive-arm-20261007_deploy_completion.md`. Round 4
(issuance 6f698f1b9b): TO-TR-w4, TO-TR-l4, TO-TR-r4 complete, 0 judgment criteria. The issuer's served act C3 is graded in the
ledger (L1-L4 closed); its L5 leg (the 2026-10-08T23:30Z fire reads window_days=7) is open and owned by `2.0.0_SA_COO~T2`.

Undispositioned before this compile: 2 of 38 rows (exact-id census over every adjudication and remediation file): D2-S1, D2-S2.
Both graduate OPEN below; no row is dismissed, so no adjudication file is minted. ARMED after this compile: none.

This seat's reads (dell2 CLOUD, 2026-10-08 ~17:3xZ): `python -m pytest data/transcripts/scripts/tests -q --collect-only` ->
`ModuleNotFoundError: No module named 'test_teams_chat_tenant'` from test_eod_voice.py, 292 collected, interrupted at collection
(D2-S1 holds). `data/transcripts/scripts/outlook/gateway_mail.py:147-168` list_rows follows `next_page_token` until absent (cap
MAX_LIST_PAGES 200), and `infra/aws/ec2/opal-gateway/app/mail_route.py:327,376` mints `next_page_token` from Graph's
`@odata.nextLink`. In SOURCE both ends page to the end. So `listed=100 = 4 x 25` is truncation only if the RUNNING gateway differs from
this source, or Graph returned no nextLink. The census D2-S2 names must include the deployed gateway bytes (rule 22a), not the repo.

FWD-7's DONE WHEN is met by the 3 admitted messages (ledger L3), so D2-S2 does not hold FWD-7.

```json
[
  {
    "id": "NFRA_TRNSPT-D2-S1",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Five teams-chat test modules (test_eod_voice, test_teams_chat_eod_republish, test_teams_chat_jobs, test_teams_chat_natural, test_teams_chat_stale_eod) import the sibling test module test_teams_chat_tenant by bare name, so one pytest process over data/transcripts/scripts/tests stops at collection and the issuer's single-process drain check (r2_suite_check.py) reads SUITE-ERROR.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S1 (2.0.0_SA_COO~T2): 244 passed, 5 errors with --continue-on-collection-errors",
      "python -m pytest data/transcripts/scripts/tests -q --collect-only (3.0.0_SA_CVO, dell2 CLOUD, 2026-10-08 ~17:3xZ): ModuleNotFoundError: No module named 'test_teams_chat_tenant'"
    ],
    "remedy": "The test author makes the five imports resolvable in one process (a package-relative import or a conftest path), checked by r2_suite_check.py reading SUITE-GREEN with no collection errors.",
    "owner": "4.0.0_SA_CRO",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "4.0.0_SA_CRO",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-D2-S2",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C3's scheduled 60-day fire (run 20261007T233013Z) landed 3 admitted messages (2026-09-02, 09-15, 09-17) but not the 2026-08-11 message the window was widened for; listed=100 = 2 senders x 2 spans x 25 (the gateway default page size), and the run record does not say whether 08-11 was listed and classed a near miss or never listed. All 3 silver rows are held_out.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S2 (2.0.0_SA_COO~T2)",
      "ledger leg L3 of nfra-trnspt-c3-driven-positive-arm-20261007",
      "gateway_mail.py:147-168 (client follows next_page_token to the end) and mail_route.py:327,376 (token minted from @odata.nextLink) at HEAD (3.0.0_SA_CVO, 2026-10-08)"
    ],
    "remedy": "A counts-only listing census per sender and span against the RUNNING gateway (its deployed bytes compared to mail_route.py at HEAD first), deciding truncation vs classification; the held-out rate is FWD-10's input.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v5",
    "remediation": {
      "state": "CLOSED_UNREMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v5",
      "closure": {
        "reason": "NOT_A_DEFECT",
        "pointer": "org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/adjudications/ADJUDICATION_v5.md (round 7 E1 census R7_E1_ENCRYPTED_CENSUS.json: 368 of 368 encrypted-only author messages, the 08-11 pair included, are Opal-internal; CTO msg 1517)"
      }
    },
    "closed": true
  }
]
```
