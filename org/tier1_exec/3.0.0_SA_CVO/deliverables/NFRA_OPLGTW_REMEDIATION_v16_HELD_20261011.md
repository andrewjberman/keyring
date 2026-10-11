# NFRA_OPLGTW -- surprise channel, REMEDIATION v16 (site Z) -- THE ROUND-33 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~14:0xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 33: 10 of 10 orders complete with VALID proofs. L8 and L9 are at `adjudications/ADJUDICATION_v24.Z.md`.

**L9:** OG-bh-1's EXACT-SAME criterion PASSES (C-S63, read on two dates). **Two judgment criteria cannot be graded yet**, and
round-close-check reads REFUSED until they are:
- **OG-tl-1, dell2's transcript re-probe:** no re-probe row exists in NFRA_TRNSPT's channel since the release. Indirect
  evidence only: since the release, D2-S16 shows the pull reaching content reads on monday_meeting (a 502 graph_error, not
  403 meeting_not_allowed).
- **OG-rl-16, dell2's first real E2 put:** `smartx/49financial/` does not exist in opal-data-assets, so no fee_statement
  key has ever been written.

Both read acts are dell2's. **NO FWD IS A WAIT applies:** each is a seat act on demand (one re-probe, one put of the Q3
statement), so the ask is a cross-fabric call to dell2, yours to route MSTR to MSTR.

**HELD, not landed in the channel:** surprise-row-gate refuses every new remediation row while
`NFRA_OPLGTW.TO-OG-o-5.runbook-section7-remedy.md` carries no parseable `<status>` tag (row Z-S86).

**L8:** C-S64 dismisses 19 rows. C-S65 graduates the 10 below, including **Z-S85, ARMED** (verified: trunk's deploy
script has 0 allowlist references against 5 in the live release) and **Z-S77**: an unnamed actor drained the shared
converter DLQ, which holds 12 messages now. **W45-S2 is your call:** the BD tool is open to unprofiled principals.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S85",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "box/sitez's infra/aws/ec2/opal-gateway/deploy-to-ec2.sh has 0 meeting_allowlist references (the live release 6aadf7db37 has 5), so a gateway release cut from trunk writes TRANSCRIPT_MEETING_ALLOWLIST empty and silently revokes the 4-meeting allowlist",
    "evidence": [
      "Z-S85; this seat's git show HEAD / 6aadf7db37 grep, 0 vs 5"
    ],
    "remedy": "Round-34 cell: drain the allowlist hunk back onto trunk's deploy-to-ec2.sh (3-way over HEAD's printf), graded by grep plus a positive control; until then every release is cut on the live ref read by host md5.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false,
    "disarm": "Standing, until the drain-back lands: every gateway release is cut on the LIVE ref read by host md5, never on trunk (Z-S85's own notes). The queued MX-r-10 and CT-i-11 releases are both on live refs that carry the hunk.",
    "disarm_owner": "2.0.0_SA_COO~O"
  },
  {
    "id": "NFRA_OPLGTW-Z-S77",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "an unnamed data-plane actor received and deleted six messages from the shared converter DLQ opal-assets-silver-dlq on 2026-10-09 15:39-16:17Z: no PurgeQueue, no management event, 14-day retention, and no Lambda event-source mapping. Any other master's failures can vanish the same way",
    "evidence": [
      "Z-S77; this seat's CloudTrail, sqs and lambda reads (ApproximateNumberOfMessages=12 now)"
    ],
    "remedy": "Name the DLQ's consumers: enable SQS data-event logging on the queue, or name the actor from the window's other planes. Read what the 12 current messages are. A DLQ with an unknown reader is not a failure record.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W45-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "blackdiamond_list_fees is classified legacy and passes an UNPROFILED principal to its own gate, while every Schwab family tool denies one; profiled principals are denied it unless a grant names it",
    "evidence": [
      "Z-W45-S2; test_ogpf1_ac02 pins the current behaviour"
    ],
    "remedy": "A CTO call: deny the BD tool to unprofiled principals (one line in decide(), changing dormant-integration behaviour), or record why it stays open.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S84",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "EC2_MANIFEST.json's opal-gateway file_checksums are stale on 8 of 10 entries, 6 of them untouched by E2",
    "evidence": [
      "NFRA_OPLGTW-Z-S84 (0.7.0_AE_CloudOps~Z, 2026-10-11 ~12:00Z): 8 of 10 file_checksums stale, 6 untouched by E2"
    ],
    "remedy": "Round-34 E4 batch repair re-derives the checksums from the served release, and the deploy rewrites them on every release.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W45-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "tests/test_portal_grant.py fails 2 tests (asker_sender_domain) at the cut base, independent of the cell",
    "evidence": [
      "Z-W45-S4"
    ],
    "remedy": "Round-34 E4 batch repair: fix or route by family, with a recorded baseline id list.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W47-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "four gateway tests in three suites fail on box/sitez for causes unrelated to the E2 carry",
    "evidence": [
      "Z-W47-S2"
    ],
    "remedy": "Round-34 E4 batch repair, same baseline list as Z-W45-S4.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W49-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the naming registry has no table row for fee_statement or market_update, while address() accepts any snake_case table for a registered root",
    "evidence": [
      "Z-W49-S2"
    ],
    "remedy": "Add the two table rows to infra/logic/registry, or make address() refuse an unregistered table (an LGIC question).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W51-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a commit in a sparse release worktree prints a naming-gate NAMING ERROR on org/missions/DIRECTIVES.yaml, because the limb cannot read what the sparse cone omits",
    "evidence": [
      "Z-W51-S3"
    ],
    "remedy": "Make the limb state SKIP: path absent from the sparse cone, rather than ERROR; or document sparse release trees as out of its domain.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W51-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a release order's mechanical AC1 graded the Phase A record (release a88661b145) rather than the live re-cut 6aadf7db37",
    "evidence": [
      "Z-W51-S5; this seat's RE-PIN 1 (patch-id cdecb877 equal) carries the substance"
    ],
    "remedy": "Release checks read the served release (host md5 or the served_release field), never a phase record; re-cut checks re-run against the re-cut sha.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W51-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the bad-quarter refusal was exercised through the installed module entry site_to_s3.copy_site_file_to_s3, not through the MCP tool wrapper a caller uses",
    "evidence": [
      "Z-W51-S6"
    ],
    "remedy": "The next E2 read exercises the refusal through the MCP wrapper.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v16",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v16"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
