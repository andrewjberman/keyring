# AMGT_RESAPP -- round 126 L8/L9 (dell1)

<sweep_watermark>2026-10-20T03:35:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-20T03:35:00Z, on 2.0.0_SA_COO~R1 msg 8596 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round126/DRAIN_END_PACKET.md @76cfd24129). Swept: 7 dell1 rows surfaced after the v165 watermark 2026-10-20T01:10:00Z (from 1,948 rows parsed across the investigation and remediation files), all 7 dismissed; 0 graduated. Two of them were ARMED (W532-S1, W532-S2), and both are read disarmed below. No clock moved. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S208",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~DELL1",
    "surfaced_at": "2026-10-20T03:35:00Z",
    "one_line": "ROUND 126 L9. The round-125 item 2 (the page half of the reader state words) is MET on PROD. Both features (c8cd2da0eb, ebd7b44720) are ancestors of origin/PROD e890aaa94f; CI 'Deploy to Production' run 39359584436 is completed/success on that sha; DEV..PROD reads 0. This seat read the DEPLOYED bundle the packet left unread: the production CloudFront index, last-modified 02:35:45Z, and its 61 chunks. The Security Analysis chunk carries the plain-word helper (READ_FAILED 'could not be read', ABSENT 'is not on file', EMPTY 'is empty', REFUSED 'was refused', INVALID 'is not valid'), the Peers suffix '(read failed|served|absent)', and the cg-2 sentences, with 0 '(read READ_FAILED)'. The issuer's served and forced DEV reads stand on its records. 7 rows dismissed, 0 graduated; the 2 ARMED rows are read disarmed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W532-S1",
      "AMGT_RESAPP-D1-W532-S2",
      "AMGT_RESAPP-D1-W532-S3",
      "AMGT_RESAPP-D1-W532-S4",
      "AMGT_RESAPP-D1-W532-S5",
      "AMGT_RESAPP-D1-S65",
      "AMGT_RESAPP-D1-S66"
    ],
    "spec_asserts": "The CTO's round-125 analysis for R1 (ledger/ROUND_ANALYSIS.round125.R1.md @5ff77594ab; msgs 8573, 8584): the posture cite misses print plain words; GenerationCaption stays as the attribute; the page change lands on DEV, is read on the running page under a real login (one response forced per state where no served name carries it), and is then promoted to PROD. The R1 track closes when round 126 closes with 0 graduated.",
    "world_is": "READ BY THIS SEAT 2026-10-20 ~03:2xZ to 03:3xZ. (1) `git -C portal fetch` then rev-parse: origin/PROD e890aaa94f, origin/DEV 84b680871f. c8cd2da0eb (cg-2) and ebd7b44720 (ch-1) are both ancestors of origin/PROD. `rev-list --count origin/DEV..origin/PROD` reads 0. `gh run view 39359584436` reads name 'Deploy to Production', status completed, conclusion success, headSha e890aaa94fea5850.... (2) The deployed bundle. The production host named in docs/deployment, portal.opalinvest.com, does not resolve from this box (nslookup: Non-existent domain); the doc is stale and is named as a finding. The documented distribution d2n2nzpeqf34ge.cloudfront.net serves index.html with Last-Modified Tue 20 Oct 2026 02:35:45 GMT, after the ch-4 promote. Its 5 entry scripts and 61 referenced chunks (62 fetched over three passes) were read. index-DRtE2u6J.js carries function Zn: READ_FAILED 'could not be read', ABSENT 'is not on file', EMPTY 'is empty', REFUSED 'was refused', INVALID 'is not valid', default 'is not available', null 'is not carried'. It is used as `${name}'s management block ${Zn(status)}`, which is ch-1's statusWords.ts as at origin/PROD (its lines 16 and 18 read 'could not be read' and 'is not on file'). The chunk also carries the Peers suffix ` (read ${wi(status)})` with wi: READ_FAILED 'failed', SERVED 'served', ABSENT 'absent', else 'not recognised'; and the cg-2 sentences 'The document could not be made: ' and 'The pack could not be printed' (1 chunk each). '(read READ_FAILED)' is in 0 of 62 files. Raw 'REFUSED' occurs 3 times in that chunk, all accounted for: the CheckFaceBadge label (the CTO ruled it stays), a scrubber regex that strips ABSENT, REFUSED and HELD OFF from served reasons, and the Zn mapping. This is a read of the served BYTES. It is not a browser render at the production host: no login was used there, and the arms are proven present in the served code, not shown rendered. (3) The issuer's records round126/LIVE_READ_DEV_5552E219.md and PROD_READ_E890AAA9.md carry the served and forced DEV reads and the PROD-head source read under a real login. This seat did not re-run the walker; the bundle read above covers the PROD side independently. DISPOSITIONS (all INERT now). W532-S1 (ARMED): the PROD-only Peers gap is closed, because the served bundle prints the plain suffix (S66's disarm, confirmed). W532-S2 (ARMED): the raw REFUSED sites. On the served chunk the only raw display is the CheckFaceBadge label (ruled to stay, msg 8573); the export and print error lines now read 'The document could not be made: ...' and 'The pack could not be printed: ...', and served reasons pass the REFUSED-stripping scrubber, so S65's disposition is confirmed. W532-S3 and W532-S5: a stale local DEV ref, corrected by S5 after a fetch. W532-S4: a worktree missing the schema file; the rows were checked against HEAD. S65 and S66: the issuer's own dispositions, confirmed above.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal: c8cd2da0eb and ebd7b44720 ancestors of origin/PROD e890aaa94f; DEV..PROD = 0 (this seat)",
        "gh run view 39359584436 -> Deploy to Production, completed, success, headSha e890aaa94f (this seat)",
        "curl https://d2n2nzpeqf34ge.cloudfront.net/index.html (Last-Modified 2026-10-20T02:35:45Z) + 61 chunks; index-DRtE2u6J.js Zn / wi mappings and the cg-2 sentences; 0 '(read READ_FAILED)' (this seat, scratchpad prodbundle/)",
        "git -C portal show origin/PROD:src/pages/SecurityAnalysis/statusWords.ts lines 16, 18 (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round126/LIVE_READ_DEV_5552E219.md and PROD_READ_E890AAA9.md (the issuer's)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round126/DRAIN_END_PACKET.md @76cfd24129"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (the page half MET on PROD, read on the deployed bundle) and seven rows: the two ARMED ones read disarmed on the served bytes, and five INERT ref, worktree or self-disposition facts."
  }
]
```

-- 3.0.0_SA_CVO~DELL1
