# NFRA_TRNSPT -- round 1 remediations

<sweep_watermark>2026-09-30T20:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30. Graduated at round 1's L9 (ADJUDICATION_v1.md).

```json
[
  {
    "id": "NFRA_TRNSPT-S2",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Today's tool exposes none of those three fields; the round-1 contract partitions by receivedDateTime and derives the id from sender, receivedDateTime, subject and the body hash, flagged fallback on every row.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S2 (2.0.0_SA_COO~T): The deployed gateway's read_email returns the raw HTML body but no internetMessageId, ccRecipients, conversationId or sentDateTime, so C-DEDUP's primary key cannot be computed this round and every round-1 mail row carrie",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Relay to site Z with S04: read_email should return internetMessageId, ccRecipients, conversationId and sentDateTime so C-DEDUP's primary key replaces the fallback id every row carries today.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S3",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 12 targets carry the pre-merge registry hash; the site Z registry change landed without a laptop regenerate, and no gate refused the merge.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S3 (2.0.0_SA_COO~T): All 12 generated naming targets at CLOUD HEAD are stale: stamped registry@5576b01fd4684bfa while infra/logic/registry at HEAD hashes ffa41913935c3281, so a `python lib/opal_naming.py generate --out .` moves every target ",
      "python lib/opal_naming.py generate --out <scratch> at HEAD (this seat ~20:1xZ): 13 written; 12 identical to the committed file, 1 differing in its mark line only",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Restamp the one generated target still on the pre-merge registry mark: portal src/pages/InvestorReporting/header/firmDisplayNames.generated.ts (registry@5576b01f; regeneration reads registry@ffa41913). Its content is unchanged; only the mark line differs. The CTO decides who restamps a portal target that signed packets pin.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S6",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "One of the ten is checkout-dependent; the parser itself reads CRLF, and the real Monday meeting parsed with unparsed=0.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S6 (2.0.0_SA_COO~T): Post-drain hygiene at CLOUD: test_teams_parse_silver.py::test_missing_metadata_cue_leaves_wall_clock_null_with_warning splits the metadata fixture on a bare double LF, so it passes on the worker's LF-written file and fai",
      "python -m pytest data/transcripts/scripts/tests in one process at HEAD (this seat ~20:0xZ): 23 failed, 95 passed",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Round-2 batched repair cell: read fixtures with universal newlines.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S7",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Each file passes alone except the rows S6/S8 name; together the two sources' modules collide by name.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S7 (2.0.0_SA_COO~T): Post-drain hygiene at CLOUD: running data/transcripts/scripts/tests in ONE pytest process gives 22 failed / 30 passed because the teams and outlook packages both expose bare top-level modules named land_bronze and pull (",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Round-2 batched repair cell: package-qualified imports so the teams and outlook modules stop shadowing each other.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S8",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "It is present now, so the hop runs; the seam is real and untested with a listing fake.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S8 (2.0.0_SA_COO~T): Chain A x chain B seam after the drain: with parse_silver.py now beside pull.py, pull.run(with_silver=True) imports it for real and parse_and_write lists the bronze prefix, but the chain-A test fakes (FakeS3 in test_team",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Round-2 batched repair cell: both pull fakes gain list_objects_v2, and the seam is asserted, not assumed.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S9",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The real tool envelope is not what the contract described; the lander raises before any write. Measured read-only with the envelope unwrapped: both real messages classify sender_ok=true, client_recipient=true, recipient_firm=49financial, ycharts_pdf=false, near_miss=true, ingest=false (their only non-inline attachments are application/octet-stream images of 6,866 and 197,768 bytes).",
    "evidence": [
      "investigation row NFRA_TRNSPT-S9 (2.0.0_SA_COO~T): FWD-7's round-1 real run broke at its first real input: list_email_attachments returns the Graph envelope {\"@odata.context\", \"value\": [...]}, but the decomposition's BRONZE CONTRACT (issuer text) told TR-b-1 it returns a",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Round-2 thread-breaking item 1: unwrap the Graph {value: [...]} envelope in the lander, then land the recorded real sample; FWD-7 has no real row until then.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S10",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "It reads them only as a pair; after the ruling the pair can never be complete, so the versioned authors table is dead data.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S10 (2.0.0_SA_COO~T): Chain C x chain D seam: outlook/criterion.py load_tables() reads data/transcripts/assets/authors.json only when client_domains.json ALSO exists; TR-a-1's ruled shape retired client_domains.json (the domains are registry ",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Round-2 thread-breaking item 2: load_tables reads the ruled authors table alone and the registry for domains, so the versioned authors table is live data.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-W4-S8",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Case-sensitive dictionary matching means a standalone lower-case name (e.g. 'we asked ottoline') is NOT wiped unless the same message showed the name capitalised or ALL-CAPS; matching lower-case case-insensitively would wipe ordinary words (will, grant, mark, rate). The surnames list holds ordinary English words, so sentence-initial 'Ask'/'Mail' are wiped unless in the stopword list (a small one is in wipe.py). The planted-token test plants the lower-case name beside its ALL-CAPS form. The held-out rate on the real sample is unmeasured here; the issuer's real silver run prints held_out=<h>.",
    "evidence": [
      "investigation row NFRA_TRNSPT-W4-S8 (0.9.0_WK_NFRA_TRNSPT~4): Wipe limits found while building: a name is matched in another case only with same-message evidence (or ALL-CAPS in the dictionary); capitalised surnames that are also English words (Ask, Mail, Reach) are wiped at senten",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "State the wipe's limits where the PII gate reports: a lower-case name with no capitalised sibling in the same message is not wiped, and ordinary-word surnames rely on a small stopword list. Measure the held-out rate on the first real rows before any reader beyond the two named ones.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-W4-S10",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The table projects none of those fields; replay.py --extract-irpt scanned 1102 items, found 0 compositions and wrote the six invented fixture requests as the order directs. A real replay set needs the composition blobs (analysis.record composition_ref), an S3 read of client-bearing artifacts this order does not grant.",
    "evidence": [
      "investigation row NFRA_TRNSPT-W4-S10 (0.9.0_WK_NFRA_TRNSPT~4): The irpt-requests table holds no request composition (variant, comparison_keys, account type, holdings): a full read-only scan of 1102 items found 0 carrying them, so the replay set is the six invented fixture requests.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R1_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "The slicer's real replay reads analysis.record composition_ref, since irpt-requests (1,102 items scanned) holds no composition fields.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v2"
    },
    "closed": false
  }
]
```
