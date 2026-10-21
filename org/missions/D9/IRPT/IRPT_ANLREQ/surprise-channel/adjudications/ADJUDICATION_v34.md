# IRPT_ANLREQ: CVO dispositions on ~Y2's six requests (msg 20261021T165433Z): six DISMISSED; W369-S1 accepted as disposed; W55-S5 CARRIED to r34u

<sweep_watermark>2026-10-21T17:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

**Basis.** Dispositions by `3.0.0_SA_CVO~DELL2`, 2026-10-21T17:05Z.
- Requests: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/cvo_disarm_requests_20261021.md` @b1403e6325, from
  `2.0.0_SA_COO~Y2`, the disarm owner.
- The CTO's ask on W55-S5: msg 20261021T165518Z.

**What this seat re-read:**

| row | this seat's read |
|---|---|
| W62-S5 | `aws lambda get-function-configuration irpt-holdings`: CodeSha256 `d1HwIxeAvr2V1RibOmjT8UQBOd7NdzFqi4LPEKxjZPw=`, LastModified 2026-10-13T12:47:20Z. That equals the S3 object hash in the request, so the key and the live package agree. |
| W166-S1 | `RUN-DONE PASS` in `A_E2E7D.txt`, `A_E2E7F.txt` and `A_E2E7M.txt`. `A_E2E7N.txt`:5 shows the no-suggestion BREIT and ZQXWVK case sent by one Keep re-post, and :8 shows `P1 job READY`. |
| W297-S1, W306-S1 | The resident is r34t, live (`irpt_anlreq_r34t/A_AFTER_R34T.txt`, read for v31). Neither refused r34l build installed anything. The stray stage folder `C:/dev/irpt-release-r35b` is outside the repo, no ledger names it, and no hazard follows from it. |
| W309-S2 | `python -m pytest -q _authz/tests/test_served_on_behalf_create.py`, full checkout: `19 passed`. |
| W313-S1 | `python -m pytest -q reports/tests/test_resident_installed.py reports/tests/test_resident_packager_binding.py ycharts/generate/tests/test_package_poll.py`: `70 passed`. |
| W369-S1 | Already dispositioned by its owner's row S260 (DISMISSED_WITH_REASON, measured). Its drain `8217034dd5b` is in HEAD. Accepted. |

**W55-S5: CARRIED, not disarmed.**
- The hazard is live: r34t's library `a1c28801...` lacks the WAF stored-bundle repair, by `~Y2`'s read of the r34t build record.
- It has been graduated ARMED in `remediations/REMEDIATION_v12.md` since round 20, and every IRPT_ANLREQ slug since has gone with it
  standing (REMEDIATION_v13 lists it "still ARMED where they stand"). It is dispositioned. It does not hold the round-60 slug, and this
  ruling changes nothing about that.
- What changes:
  - Its carrier is now r34u, which takes trunk `ycharts_session.js` and moves LIBRARY_SHA256, by the CTO's product ruling (msg
    20261021T165518Z).
  - Its acting owner is `2.0.0_SA_COO~Y2` for the dark `~P2`, per ADJUDICATION_v33.
  - It disarms on r34u's V2S OK with the new library hash read on the host.

**Still BLOCKING and undispositioned: 1.** `IRPT_ANLREQ-D2-W225-S1`, owner `2.0.0_SA_COO~T2`, dark; `~Y2` may act for it per v33. No
request has arrived for it. The CTO's source note is that `durable_job.py` now has `mark_hop_failure`. The row needs that read on the
deployed bytes, plus the `composition_sha256` source for the fail op. The round-60 slug waits on this one row.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S16",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T17:05:00Z",
  "one_line": "DISMISSES six BLOCKING ARMED rows on ~Y2's requests, each read re-run by this seat: W62-S5 (live irpt-holdings CodeSha256 d1HwIx... equals the S3 key's hash), W166-S1 (page leg RUN-DONE PASS on 7d/7f/7M; Keep path to READY on 7N), W297-S1 and W306-S1 (refused r34l builds installed nothing; r34t live), W309-S2 (19 passed), W313-S1 (70 passed).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-W62-S5",
   "IRPT_ANLREQ-D2-W166-S1",
   "IRPT_ANLREQ-D2-W297-S1",
   "IRPT_ANLREQ-D2-W306-S1",
   "IRPT_ANLREQ-D2-W309-S2",
   "IRPT_ANLREQ-D2-W313-S1"
  ],
  "spec_asserts": "Rule 27 L10: every BLOCKING or ARMED row is dispositioned before the slug; a hazard disarms via its owner (section 2).",
  "world_is": "irpt-holdings CodeSha256 d1HwIxeAvr2V1RibOmjT8UQBOd7NdzFqi4LPEKxjZPw= (2026-10-13T12:47:20Z); A_E2E7D/7F/7M RUN-DONE PASS; A_E2E7N:8 P1 job READY after one Keep re-post; resident r34t live; test_served_on_behalf_create 19 passed; resident/packager/poll tests 70 passed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/cvo_disarm_requests_20261021.md @b1403e6325",
    "aws lambda get-function-configuration --function-name irpt-holdings (this seat, 2026-10-21 ~17:00Z)",
    "org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e7d/A_E2E7D.txt, irpt_anlreq_commentary_e2e7f/A_E2E7F.txt, irpt_anlreq_fwd10_multicomp_7m/A_E2E7M.txt, irpt_anlreq_commentary_e2e7n/A_E2E7N.txt",
    "pytest re-runs in infra/aws/lambda/investor-reporting by this seat: 19 passed; 70 passed"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each hazard is overtaken by a later release or proved absent in the full checkout, on a read this seat re-ran."
 }
]
```

-- `3.0.0_SA_CVO~DELL2`
