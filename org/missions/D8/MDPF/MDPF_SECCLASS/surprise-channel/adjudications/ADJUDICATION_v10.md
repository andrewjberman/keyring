# MDPF_SECCLASS -- round 12 L8/L9 adjudication, PART 1 (dismissals)

<sweep_watermark>2026-10-08T03:34Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-08T03:34Z. L8 packet: 2.0.0_SA_COO~M1 `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R12_20261008.md`
@9584c21462 (msg 781). Index: dell1 CLOUD at the drain plus this seat's ADJUDICATION_v7..v9. 40 rows had no disposition (24 new
since round 10, plus 16 carried); 24 were read this compile by two forks of this seat, with own spot-checks on S66 (ai_leg_verify.py:84,
no unresolved term) and S64/S67 (fix 0d91b0fa96).

Landed below: 15 dismissals, including BLOCKING W49-S1, S61 (the walker 403: proxy past CloudFront, @f77d1c8d7e, fixed @91a899001f),
W53-S1, D1-S2 and the blocking S67.

Drafted, gate-refused while TO-DEPLOY-e21, TO-DEPLOY-e42 and TO-DEPLOY-e66 read pending: graduations of S60, W56-S2, S63, S65, S66 ARMED, S68, D1-S1, D1-S3, D1-W62-S1, W32-S1, W32-S2, W32-S3, W32-S4; and from rounds 9-10,
S54 (ARMED), S58, W35-S3, W31-S1..S4, W36-S2, W36-S3, W41-S2..S4. Round-12 orders e67 and e71 read `issued` on this index; they are held
lines on item 5. Held-branch rows (D1-W57-S1 on e67; W34, W38, W41-S5, W44, W47, W48) compile on merge.

Supersession: this seat's earlier row "S60" (the walker 403, branch cvo-secclass-r9-compile @bcd60149e4, never merged) collided with
2.0.0_SA_COO~M1's MDPF_SECCLASS-S60 (COT multi_asset). The id belongs to M1's row; the walker finding is carried by M1's S61 and is
dismissed here. Branch cvo-secclass-r9-compile is superseded by cvo-secclass-r12-compile.

AccessDenied met this compile: s3:GetObject on opal-data-49financial/_code/tests/test_a07_canonical_first.py (cloudops-dell1-agent-user,
~03:4xZ), reported to 1.0.0_SA_CTO~DELL1 the same hour.

```json
[
  {
    "id": "MDPF_SECCLASS-C-S78",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S55 (OBSERVATION/ARMED) dismissed: The row's disarm condition is met: the CTO half @b3092be6d2 is now on the trunk, so any reader can print its bytes, and S56 records that its eight conditions match what the deploy carried.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S55"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The row's disarm condition is met: the CTO half @b3092be6d2 is now on the trunk, so any reader can print its bytes, and S56 records that its eight conditions match what the deploy carried.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git fetch origin; git merge-base --is-ancestor b3092be6d2 origin/CLOUD -> yes; git ls-tree -r origin/CLOUD now lists org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECCLASS_SC_e42_A07_CANONICAL_FIRST_20261007.md (count 1), read 2026-10-08 ~03:4xZ",
        "S56 (0.7.0_AE_CloudOps~S): the half's own bytes confirm every one of the eight conditions was carried by the completed deploy",
        "investigation row MDPF_SECCLASS-S55 (0.7.0_AE_CloudOps~S)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The row's disarm condition is met: the CTO half @b3092be6d2 is now on the trunk, so any reader can print its bytes, and S56 records that its eight conditions match what the deploy carried."
  },
  {
    "id": "MDPF_SECCLASS-C-S79",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S56 (OBSERVATION/INERT) dismissed: S56's residual (the half lived only on candidate branches, not the trunk) no longer holds: the half is on origin/CLOUD. The conditions-match finding it records needs no action.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S56"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S56's residual (the half lived only on candidate branches, not the trunk) no longer holds: the half is on origin/CLOUD. The conditions-match finding it records needs no action.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor b3092be6d2 origin/CLOUD -> yes; the CTO half path is in origin/CLOUD's tree (read 2026-10-08 ~03:4xZ)",
        "investigation row MDPF_SECCLASS-S56 (0.7.0_AE_CloudOps~S)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S56's residual (the half lived only on candidate branches, not the trunk) no longer holds: the half is on origin/CLOUD. The conditions-match finding it records needs no action."
  },
  {
    "id": "MDPF_SECCLASS-C-S80",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S57 (OBSERVATION/ARMED) dismissed: Disarmed by S59: the test key was minted under the half addendum, and the push moved exactly a07 (byte-identical) plus the one test key. That served-key read is the laptop's; dell1 is denied the 49F bucket.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S57"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Disarmed by S59: the test key was minted under the half addendum, and the push moved exactly a07 (byte-identical) plus the one test key. That served-key read is the laptop's; dell1 is denied the 49F bucket.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor 8798e5f484 origin/CLOUD -> yes (held-32 r2 is on the trunk, as S59 cites)",
        "S59: laptop read-back 16:33Z: _code/a07_dim_asset_classification.py ETag 4092c5b8... = repo md5; _code/tests/test_a07_canonical_first.py ETag 46420cd1... = repo md5 (new key); covered by the SC-e-42 half addendum @d8d0c6ed22; 1.0.0_SA_CTO~DELL1 msg 427 ruled it met",
        "AccessDenied: s3:HeadObject (s3:GetObject) on arn:aws:s3:::opal-data-49financial/_code/tests/test_a07_canonical_first.py -> 403 Forbidden, principal cloudops-dell1-agent-user, ~03:4xZ 2026-10-08. This seat could not re-read the 49F keys itself; the disarm rests on the laptop read-back and the trunk commit",
        "dell1 read of opal-data-49financial/_code/tests/test_a07_canonical_first.py: s3:GetObject 403 for cloudops-dell1-agent-user (~03:4xZ, reported to 1.0.0_SA_CTO~DELL1); disarm graded on the laptop read-back",
        "investigation row MDPF_SECCLASS-S57 (0.7.0_AE_CloudOps~S)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed by S59: the test key was minted under the half addendum, and the push moved exactly a07 (byte-identical) plus the one test key. That served-key read is the laptop's; dell1 is denied the 49F bucket."
  },
  {
    "id": "MDPF_SECCLASS-C-S81",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S59 (OBSERVATION/INERT) dismissed: An evidence row: S57's disarm, consumed by S57's dismissal. It carries no hazard of its own.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S59"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "An evidence row: S57's disarm, consumed by S57's dismissal. It carries no hazard of its own.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor 8798e5f484 origin/CLOUD -> yes",
        "AccessDenied: s3:HeadObject (s3:GetObject) on arn:aws:s3:::opal-data-49financial/_code/tests/test_a07_canonical_first.py -> 403 Forbidden, principal cloudops-dell1-agent-user",
        "investigation row MDPF_SECCLASS-S59 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An evidence row: S57's disarm, consumed by S57's dismissal. It carries no hazard of its own."
  },
  {
    "id": "MDPF_SECCLASS-C-S82",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "W49-S1 (BLOCKING/INERT) dismissed: BLOCKING resolved by the issuer's repair 4f0b68c9ce (the <paths> block now parses). The build landed at 16092a4806, which is on the trunk, with no override (W49-S2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W49-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING resolved by the issuer's repair 4f0b68c9ce (the <paths> block now parses). The build landed at 16092a4806, which is on the trunk, with no override (W49-S2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor 4f0b68c9ce origin/CLOUD -> yes; 16092a4806 (the ~49 build commit) -> yes on origin/CLOUD",
        "investigation row MDPF_SECCLASS-W49-S1 (0.9.0_WK_MDPF_SECCLASS~49)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING resolved by the issuer's repair 4f0b68c9ce (the <paths> block now parses). The build landed at 16092a4806, which is on the trunk, with no override (W49-S2)."
  },
  {
    "id": "MDPF_SECCLASS-C-S83",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "W49-S2 (OBSERVATION/INERT) dismissed: An evidence row: W49-S1's resolution, confirmed on the trunk.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W49-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "An evidence row: W49-S1's resolution, confirmed on the trunk.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "4f0b68c9ce and 16092a4806 both ancestors of origin/CLOUD",
        "investigation row MDPF_SECCLASS-W49-S2 (0.9.0_WK_MDPF_SECCLASS~49)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An evidence row: W49-S1's resolution, confirmed on the trunk."
  },
  {
    "id": "MDPF_SECCLASS-C-S84",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S61 (BLOCKING/INERT) dismissed: BLOCKING resolved. The 403 was the local dev proxy sending /api/scoped/partners past CloudFront's origin check, not the walker's role and not the product. The proxy is fixed on portal DEV 3b8c292f47, and the walker now reads 200 on the three named clients. FWD-1's live client-page read is no longer ",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S61"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING resolved. The 403 was the local dev proxy sending /api/scoped/partners past CloudFront's origin check, not the walker's role and not the product. The proxy is fixed on portal DEV 3b8c292f47, and the walker now reads 200 on the three named clients. FWD-1's live client-page read is no longer blocked; whether it is REALIZED is an L9 grade, not this row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_S60_WALKER_403_CAUSE_20261007.md @f77d1c8d7e: opal-portal-authorizer logs 'Origin verification FAILED - request did not come through CloudFront'; the walker's token verified role admin, allowedFirmIds ALL",
        "portal 3b8c292f47 is on portal origin/DEV; vite.config.ts:140-144 now targets https://d2n2nzpeqf34ge.cloudfront.net for /api/scoped/partners (comment cites row S61)",
        "MDPF_SECCLASS_S60_PROXY_FIX_CHECK_20261007.md @91a899001f (on origin/CLOUD): the walker gets 200 on the advisor and three client platinum-summaries (z08373330, z0893406, z08123628) with ?firmId=49financial; signed out gets 401",
        "investigation row MDPF_SECCLASS-S61 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING resolved. The 403 was the local dev proxy sending /api/scoped/partners past CloudFront's origin check, not the walker's role and not the product. The proxy is fixed on portal DEV 3b8c292f47, and the walker now reads 200 on the three named clients. FWD-1's live client-page read is no longer blocked; whether it is REALIZED is an L9 grade, not this row."
  },
  {
    "id": "MDPF_SECCLASS-C-S85",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "W53-S1 (BLOCKING/ARMED) dismissed: BLOCKING/ARMED resolved by AMENDMENT 3 (b2144dedb1). The port at b359a829d7 carries the 4e73b996d0 blobs, census included, and the trunk holds exactly those blobs (W53-S2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W53-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "BLOCKING/ARMED resolved by AMENDMENT 3 (b2144dedb1). The port at b359a829d7 carries the 4e73b996d0 blobs, census included, and the trunk holds exactly those blobs (W53-S2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git rev-parse at HEAD vs 4e73b996d0 vs b359a829d7: data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py 355b2b98 = 355b2b98 = 355b2b98; d00_census_out.json 66c09de8 = 66c09de8 = 66c09de8",
        "b2144dedb1 (AMENDMENT 3) and b359a829d7 (the port commit) are ancestors of origin/CLOUD",
        "investigation row MDPF_SECCLASS-W53-S1 (0.9.0_WK_MDPF_SECCLASS~53)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "BLOCKING/ARMED resolved by AMENDMENT 3 (b2144dedb1). The port at b359a829d7 carries the 4e73b996d0 blobs, census included, and the trunk holds exactly those blobs (W53-S2)."
  },
  {
    "id": "MDPF_SECCLASS-C-S86",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "W53-S2 (OBSERVATION/INERT) dismissed: An evidence row: W53-S1's resolution, confirmed by blob equality on the trunk.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W53-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "An evidence row: W53-S1's resolution, confirmed by blob equality on the trunk.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "blob equality as above at HEAD; b359a829d7 on origin/CLOUD",
        "investigation row MDPF_SECCLASS-W53-S2 (0.9.0_WK_MDPF_SECCLASS~53)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An evidence row: W53-S1's resolution, confirmed by blob equality on the trunk."
  },
  {
    "id": "MDPF_SECCLASS-C-S87",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "W56-S1 (OBSERVATION/INERT) dismissed: A disclosure, not a hazard. The builder's documented --held-root option reused the 08:26Z held set and no firm read was denied. The custody count (857) and refused_stale=0 agree, and the order is complete.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W56-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "A disclosure, not a hazard. The builder's documented --held-root option reused the 08:26Z held set and no firm read was denied. The custody count (857) and refused_stale=0 agree, and the order is complete.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MDPF_SECCLASS.TO-SC-e48.clean-name-row-set-v2.md line 8 <status>complete</status> at HEAD; CLEAN_NAME_ROW_SET_V2_20261007.tsv and R11_CHECKS/clean_name_row_set_v2.py tracked",
        "investigation row MDPF_SECCLASS-W56-S1 (0.9.0_WK_MDPF_SECCLASS~56)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disclosure, not a hazard. The builder's documented --held-root option reused the 08:26Z held set and no firm read was denied. The custody count (857) and refused_stale=0 agree, and the order is complete."
  },
  {
    "id": "MDPF_SECCLASS-C-S88",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S62 (OBSERVATION/INERT) dismissed: Both halves resolved: (a) clean_name is ASCII-only since R12c and both live names now read ASCII; (b) the V3 re-plan carries the cash rows, and the 17 legacy fixed_income/Cash remainder is tracked as D1-W62-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S62"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Both halves resolved: (a) clean_name is ASCII-only since R12c and both live names now read ASCII; (b) the V3 re-plan carries the cash rows, and the 17 legacy fixed_income/Cash remainder is tracked as D1-W62-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -- infra/aws/lambda/v2_portal/_shared/security_name.py: d3f6b47cac (TO-SC-e47 amendment R12c) makes clean_name output ASCII only; security_name.py:57-58 DROPPED_SIGNS = U+00AE U+2122 U+00A9, :110 _ascii_fold",
        "dynamodb get-item etf-classifications (fork of 3.0.0_SA_CVO, 2026-10-08 ~03:4xZ): VWUAX name 'Vanguard US Growth Admiral' (0 non-ASCII), CUSIP:025083882 'American Century Ultra Inv' (0 non-ASCII)",
        "part (b) is superseded by the V3 set: D1-W62-S1 measures 328 unique cash keys planned, all present at plan",
        "investigation row MDPF_SECCLASS-S62 (2.0.0_SA_COO~M1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both halves resolved: (a) clean_name is ASCII-only since R12c and both live names now read ASCII; (b) the V3 re-plan carries the cash rows, and the 17 legacy fixed_income/Cash remainder is tracked as D1-W62-S1."
  },
  {
    "id": "MDPF_SECCLASS-C-S89",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S64 (OBSERVATION/ARMED) dismissed: The predicted UTC-midnight coupling of the listing limb is repaired: AC1 now reads the newest listing, not the wall-clock day's key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S64"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The predicted UTC-midnight coupling of the listing limb is repaired: AC1 now reads the newest listing, not the wall-clock day's key.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -- R12_CHECKS/ai_leg_verify.py: 0d91b0fa96 (2026-10-08T01:14Z) 'reads the NEWEST AI listing, not today's -- a run crossing midnight'",
        "ai_leg_verify.py at HEAD: lists every mdpf/global/gold/ai_classified_securities/*/index.json and reads max(listings); no wall-clock day term remains in the listing limb",
        "3.0.0_SA_CVO own read: git log ai_leg_verify.py -> 0d91b0fa96 'reads the NEWEST AI listing, not today's'",
        "investigation row MDPF_SECCLASS-S64 (0.7.0_AE_CloudOps~SC)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The predicted UTC-midnight coupling of the listing limb is repaired: AC1 now reads the newest listing, not the wall-clock day's key."
  },
  {
    "id": "MDPF_SECCLASS-C-S90",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "S67 (BLOCKING/ARMED) dismissed: The measured midnight flip (false FAIL after 00:00Z) is removed by the newest-listing fix; the false-PASS half is S66's and stays graduated there.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S67"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The measured midnight flip (false FAIL after 00:00Z) is removed by the newest-listing fix; the false-PASS half is S66's and stays graduated there.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0d91b0fa96 (2026-10-08T01:14Z) changed the listing limb to the newest index.json, after S67's 00:18Z measurement; no wall-clock day read remains in the limb at HEAD",
        "3.0.0_SA_CVO own read: git log ai_leg_verify.py -> 0d91b0fa96 'reads the NEWEST AI listing, not today's'",
        "investigation row MDPF_SECCLASS-S67 (0.7.0_AE_CloudOps~SC)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The measured midnight flip (false FAIL after 00:00Z) is removed by the newest-listing fix; the false-PASS half is S66's and stays graduated there."
  },
  {
    "id": "MDPF_SECCLASS-C-S91",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "D1-S2 (BLOCKING/INERT) dismissed: Repaired on dell1: the Windows companion now resolves dell1's CLI and derives from PATH as a last resort, so native-Python callers reach a real aws.exe.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Repaired on dell1: the Windows companion now resolves dell1's CLI and derives from PATH as a last resort, so native-Python callers reach a real aws.exe.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -- .tools/aws.cmd: 62d57c9f73 (0.0.0_AB_MSTR~DELL1, 2026-10-07 21:40 -04:00) adds %LOCALAPPDATA%\\Programs\\Amazon\\AWSCLIV2\\aws.exe and a 'where aws.exe' derive fallback (:31-34)",
        "cmd /c .tools\\aws.cmd --version on dell1 (fork): aws-cli/2.37.9 Python/3.14.6 Windows/11",
        "investigation row MDPF_SECCLASS-D1-S2 (0.7.0_AE_CloudOps~SD)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired on dell1: the Windows companion now resolves dell1's CLI and derives from PATH as a last resort, so native-Python callers reach a real aws.exe."
  },
  {
    "id": "MDPF_SECCLASS-C-S92",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T03:34:00Z",
    "one_line": "W59-S1 (OBSERVATION/INERT) dismissed: An observation, not a hazard: the backfill's empty planned set is the measured state; the writer change is the live part of e69 and the backfill stays a standing guard. Whether a half is wanted for an empty set is the issuer's and the CTO's, recorded in the half request.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W59-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "An observation, not a hazard: the backfill's empty planned set is the measured state; the writer change is the live part of e69 and the backfill stays a standing guard. Whether a half is wanted for an empty set is the issuer's and the CTO's, recorded in the half request.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-SC-e69 <status>complete</status> at HEAD; packet: namespace_backfill.py dry run rows=9155 missing_cusip=0 missing_name=0 puts=0",
        "investigation row MDPF_SECCLASS-W59-S1 (0.9.0_WK_MDPF_SECCLASS~59)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An observation, not a hazard: the backfill's empty planned set is the measured state; the writer change is the live part of e69 and the backfill stays a standing guard. Whether a half is wanted for an empty set is the issuer's and the CTO's, recorded in the half request."
  }
]
```
