# NFRA_OPLGTW -- surprise channel, REMEDIATION v2 -- THE SLUG (rounds 3-12)

Author: 3.0.0_SA_CVO~O. Round: v2. Fabric: site-z. Recorded: 2026-10-02T00:44:59Z. **Reader:** `1.0.0_SA_CTO~O`.

11 rows, all OPEN, graduated at L8 (adjudications/ADJUDICATION_v3.Z.md Z-C-S13); grade Z-C-S14 (OGTX2-J1 PASS; OG-tx-2's AC1 FAIL is row Z-S43). Two ARMED: Z-S41 (Tax bearer tuple) and Z-W13-S5 (DATA_CATALOG CRLF). One dated: Z-W12-S7 (operator client idle expiry ~2026-10-18). Carried from REMEDIATION_v1 and not re-graded here.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S43",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "OG-tx-2 reads 3 of 4: the Research Team Meeting is refused 403 (3003) because Andrew is not an invitee; the other three read in full as invitee-not-organizer. CTO ruling 28043: reach is by an invitation to the series, not the application route.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S43",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S42"
    ],
    "remedy": "OPEN: an invitation of the delegated identity to the Research Team Meeting series (a person's act), then re-run OG-tx-2's REACH arm on that meeting.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S41",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "app/taxsma_workbook.py _OTHER_ROUTE_BEARERS omits TRANSCRIPT_BEARER and MAIL_BEARER; latent while every bearer compares DIFFER (OG-tr-1 M1 read all DIFFER before the upload).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S41"
    ],
    "remedy": "OPEN: add both to the tuple in OPLGTW's next gateway release (CTO 28026); until then any bearer rotation compares DIFFER first.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-04T00:15:00Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W13-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The line-ending renormalization of infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml never landed: read by this seat at HEAD, git ls-files --eol says i/crlf w/crlf attr/-text and 1,614 of 1,614 stored lines carry CR. The naming limb refused the renorm commit (16 findings on a line-ending-only diff), so OG-h-1 item A's AC1 (stored CRLF 0) is unmet and W2-S8 stays open.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W13-S5"
    ],
    "remedy": "OPEN: the issuer decides: have the naming limb admit a line-ending-only diff (gate owner) or have an admitted seat land it; then apply ITEM_A_BLOCKED.md.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-W10-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Schwab dim_position and dim_asset collide under the declared grain on all 8 snapshots (2 masters x 2 dates); 5 of 10 colliding position keys and the one colliding asset key carry a blank component, and one more contract column makes each snapshot unique (candidate only). The units question can only be sealed as the C3 refusal.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W10-S1",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W10-S2"
    ],
    "remedy": "OPEN: a spec decision on the Schwab position and asset grain (adopt the candidate column or another grain); until then quantity-against-value stays unexercised.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W12-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The operator's upload client (identity_tool_allowlist.txt:19) has no live refresh family (revoked 2026-09-29, refresh_token_reuse) and reads EXPIRED under OG-u-2's idle lifetime from about 2026-10-18 unless an authorization-code exchange extends it first.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W12-S7"
    ],
    "remedy": "OPEN: the operator re-authorizes that client before ~2026-10-18 (a dated act, not a wait); the owner names the session and records the new expiry.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W12-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The access-state table's only real POLICY partition is write-capable person #1's and holds an ACTIVE email_deny record (plus 3 synthetic probe partitions from 2026-09-16): no tier moves, but it is a live refusal on a roster principal's sign-in path.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W12-S8"
    ],
    "remedy": "OPEN: the owner reads the deny record's origin and either removes it with its own halves or records why it stays; delete the 3 synthetic partitions or record them as fixtures.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-W13-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A burst dispatch's chain aborted before writing any chain log (2026-09-23 09:46:32Z, /tmp/advi_49f_code/chain_49f_entrypoint.py absent, rc 1): OG-m-3's classifier reads the chain log, so an abort that writes none still reads UNKNOWN, not ABORT.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W13-S2"
    ],
    "remedy": "OPEN: place with the 49F ADVI chain's owner; classify a dispatch with no chain log as ABORT (or prove the bootstrap order makes it impossible).",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W15-S23",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The gateway audit record carries no byte count for read_meeting_transcript (OG-tx-2 matched on transcript id and read count only) and carries the caller's email, never the principal key (tier reads attributed by email after the principal cutover).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S23",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W12-S10"
    ],
    "remedy": "OPEN: an app/audit.py change adding returned-bytes and the principal key to the record, under its own order.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S34",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "deploy-to-ec2.sh's host-side roster log line reports 'write_capable 1 pairs' while the rendered .env and the secret hold 2 (hash MATCH): a log-count defect.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S34"
    ],
    "remedy": "OPEN: fix the count at OPLGTW's next enrichment (with Z-S32's .env shape fix).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S23",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-merge.sh, draining in the shared tree, committed a peer's uncommitted project.json edit into the merge commit; the same window lost that peer's PRD edit and the issuer's A2 edits (recovered by the peer).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S23"
    ],
    "remedy": "OPEN: place with safe-merge.sh's owner: refuse a drain whose merge commit would carry a path outside the branch's diff.",
    "owner": "1.0.0_SA_CTO~O",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~O",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-S63",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Phase 1's committed seal b0d4bba5df no longer has its salt: a re-verification of OGV4-AC8 minted a fresh salt and rewrote SEALED_EXPECTED.json uncommitted in wk-nfra-oplgtw-og-v-4-p1. OG-v-4 is superseded on Andrew's word; OG-v-7 (staged) re-grades the controlled walkthrough.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S63"
    ],
    "remedy": "OPEN: before OG-v-7 runs, record which seal is phase 1's of record (the 18:06Z working seal is the only one whose salt exists) and mark AC8's probe MUTATING so a verifier re-runs only a read-back.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  }
]
```
