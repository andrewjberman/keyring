# NFRA_MCPINDEX ROUND 8 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-10-10 ~23:1xZ, on `2.0.0_SA_COO~MI` msg 33045. **Terminality:** 4 of 4 orders
complete (MX-d-7, MX-c-6, MX-d-8, MX-r-9). Packet `deliverables/2.0.0_SA_COO~MI/round8/L8_PACKET_ROUND8.md` @47b094e5a1
(blob 6c5df7fe86). Round 7 is not compiled here: it stays open on MX-s-19 (event-gated on the 2026-10-13 runs).

**Judgment:** J2 is graded below (Z-C-S43 and Z-C-S44). **J1 is NOT graded.** It waits on Alyssa's own session, HELD at
Andrew through `0.0.0_AB_MSTR~Z` (msgs 33019/33020/33034). `round-close-check --round 8` reads `judgment=2 graded=2`
because it matches old rows Z-C-S26 and Z-C-S38 (`3.0.0_SA_CVO~O`, earlier rounds). That is a false GRADED (Z-C-S42, the
fourth graduated item).

**Measured by this seat at compile:**
- Served catalog: `md5sum /opt/opal-gateway/app/refs/DATA_CATALOG.yaml` on i-07dccb1615503ac99 (ssm e0e742c6) =
  7e9e40bb185f266aa293a7d29ad67e6d. That equals `git show d3c31e972e:` and box/sitez HEAD. A missing-file control
  errors visibly.
- Artifact plane: `s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-d3c31e972e.tar.gz` and
  `-latest.tar.gz` are both 525792 B, both have git-ref metadata d3c31e972e8c6fdb26dda98a1d9ff55ced0ced89, and both were
  written 2026-10-10T21:49:4xZ.
- `git merge-base --is-ancestor ac148d7eb9`: 407ae3578f yes, f8bf16549e yes; control c6adb5f700 no.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S40",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-10T23:10Z",
    "one_line": "Round 8 L8: the six BLOCKING or ARMED rows are DISMISSED on the issuer's rulings, each re-measured here where a measurement exists: W28-S3, W29-S2, W28-S7, Z-S90, Z-S92, and Z-S93 as Z-S92's evidence carrier.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned BLOCKING or ARMED row of the round.",
    "world_is": "W28-S3 and W29-S2 (commits refused on stale worktree bases) are disarmed by Z-S86. Both branches merged ac148d7eb9 before closing; that is re-read here by is-ancestor, with a negative control. W28-S7 (PHASE A pins void on another live ref) is disarmed by MX-r-9 amendment A1 item 2 (Z-S89): PHASE B re-read the live ref at apply. Z-S90 (.env key count anchored on 51) is disarmed by A3 (Z-S91): the equality is a rule read at the act. Z-S92 (artifacts mislabelled) is disarmed by Z-S95. Re-read here: the release tarball exists and both it and -latest carry git-ref d3c31e972e, and the host's catalog md5 equals the release's. Z-S93 carries the applier's evidence for that disarm.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W28-S3",
      "NFRA_MCPINDEX-Z-W29-S2",
      "NFRA_MCPINDEX-Z-W28-S7",
      "NFRA_MCPINDEX-Z-S90",
      "NFRA_MCPINDEX-Z-S92",
      "NFRA_MCPINDEX-Z-S93"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-S86, Z-S89, Z-S91, Z-S95",
        "git merge-base --is-ancestor ac148d7eb9 {407ae3578f, f8bf16549e}: both yes; control c6adb5f700: no",
        "aws s3api head-object ec2/opal-gateway/opal-gateway-{d3c31e972e,latest}.tar.gz: 525792 B, git-ref d3c31e972e8c6fdb26dda98a1d9ff55ced0ced89",
        "ssm e0e742c6 on i-07dccb1615503ac99: DATA_CATALOG.yaml md5 7e9e40bb185f266aa293a7d29ad67e6d"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each hazard is removed by a committed amendment or repair, and every one that can be measured was re-read here."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S41",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-10T23:10Z",
    "one_line": "Round 8 L8: nine INERT rows are DISMISSED -- W28-S1, W28-S2, W28-S5, W28-S6 (worker choices the issuer confirmed) and the issuer's five ruling rows Z-S86, Z-S87, Z-S89, Z-S91, Z-S95.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every row of the round.",
    "world_is": "W28-S1 and W28-S2 are confirmed under contract 4 (Z-S86): held prose dates no longer pose as served as-of. W28-S5 shows need entries to opal-internal principals only; this keeps the cross-firm test, and Alyssa is internal. W28-S6 ranks by own-text overlap, with ties to the dataset, and the original set stays at 24 of 27 (Z-S87). The five ruling rows are rulings, not defects: their substance is carried in Z-C-S40 and Z-C-S42.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-W28-S1",
      "NFRA_MCPINDEX-Z-W28-S2",
      "NFRA_MCPINDEX-Z-W28-S5",
      "NFRA_MCPINDEX-Z-W28-S6",
      "NFRA_MCPINDEX-Z-S86",
      "NFRA_MCPINDEX-Z-S87",
      "NFRA_MCPINDEX-Z-S89",
      "NFRA_MCPINDEX-Z-S91",
      "NFRA_MCPINDEX-Z-S95"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-S86, Z-S87 (the confirmations)",
        "L8_PACKET_ROUND8.md section 1: d8.AC1 original 24/27"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Confirmed design choices and the issuer's own rulings; none states a standing defect."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S42",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-10T23:10Z",
    "one_line": "Round 8 L8: GRADUATED to REMEDIATION_v6 -- the suite red (Z-S88, W28-S8), the emitter's census path (W29-S1), Alyssa's word folds (W28-S4), orphaned host assets (Z-S94), the deploy procedure behind Z-S92, and round-close-check's false GRADED on a bare judgment id.",
    "class": "OBSERVATION",
    "spec_asserts": "A standing defect or enrichment leaves the round as an owned remediation row.",
    "world_is": "Z-S88 and W28-S8: the gateway suite fails 34 to 38 tests at the round-8 base, all pre-existing. It was 13 named at round 6 (Z-W21-S15), so it is growing. W29-S1: any re-emit in a worktree with the main-tree census path rewrites 32 census_ref lines. W28-S4: two of her phrasings route only through need-local folds. Z-S94: the host holds 105 files against the artifact's 103, because the extract prunes nothing. Z-S92's cause: deploy-to-ec2.sh names and stamps the artifact from rev-parse HEAD, and the manifest auto-commit fails in a sparse tree (commit_gate_runner.py:96, ModuleNotFoundError comp_constants_cli). round-close-check.py:388 applies the order-name requirement only to ids of the form AC<n>, so a bare judgment id of the J<n> form is satisfied by any CVO-kind row in any round. Round 8 reads graded=2 while the thread criterion (FWD-11, Alyssa's run) has never run.",
    "adjudicates": [
      "NFRA_MCPINDEX-Z-S88",
      "NFRA_MCPINDEX-Z-W28-S8",
      "NFRA_MCPINDEX-Z-W29-S1",
      "NFRA_MCPINDEX-Z-W28-S4",
      "NFRA_MCPINDEX-Z-S94"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-S88, Z-W28-S8, Z-W29-S1, Z-W28-S4, Z-S94, Z-S92",
        ".tools/round-close-check.py:386-404 read at HEAD; round-close-check --project NFRA_MCPINDEX --round 8: the thread criterion reads GRADED by adjudication row NFRA_MCPINDEX-Z-C-S26 (3.0.0_SA_CVO~O, an earlier round)",
        "L8_PACKET_ROUND8.md section 5 item 1"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S43",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-10T23:10Z",
    "one_line": "L9, TO-MX-r-9 J2 (FWD-12, via MX-c-6): PASS -- subtracting the served catalog from her two briefs leaves nothing missing, 29 of 29.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-12 (PRD v0.7:222-229): a reviewer subtracts the catalog from her two briefs and finds nothing missing; each entry says what the need is, its source, whether it is served today and which tool answers it; an unserved need names its owner or 'unowned'.",
    "world_is": "The served catalog's needs (host md5 equal to the release) hold E-1 to E-29. The brief's Part IV.A has 29 rows, and none is missing, extra or duplicated. All 29 carry need, source, status and tool. Statuses: 6 SERVED, 6 PARTIAL, 15 GAP, 1 DENIED, 1 UNMEASURED, the same as the brief's count. Every entry that is not SERVED names an owner or 'unowned'. Two entries name a null tool, each with a stated reason: E-25 (SERVED through the bloomberg_standing_read channel, not an MCP tool) and E-18 (PARTIAL, a repo tool). This meets 'which tool answers it' as written.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python subtraction of DATA_CATALOG.yaml needs: against docs/briefs/mcpindex-alyssa-workflows-midstream-brief-20261009.md:104-142 -- brief 29, catalog 29, missing [], extra [], dup []",
        "ssm e0e742c6: host catalog md5 7e9e40bb185f266aa293a7d29ad67e6d = release d3c31e972e"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: J2 FWD-12 PASS."
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S44",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-10T23:10Z",
    "one_line": "L9, TO-MX-r-9 J2 (FWD-18): FAIL, narrow -- the catalog reads 4 of 14 workflows retired by a SERVED entry, but one of the four is wrong (E-25's Bloomberg prices do not retire C1's YCharts reports), so the true count is 3 of 14; and C3 is tagged by no entry.",
    "class": "OBSERVATION",
    "spec_asserts": "FWD-18 (PRD v0.7:270-275): the count of C1-C8 and W1-W6 a served entry answers is read from the catalog; an entry carries its C# or W#.",
    "world_is": "SERVED entries tag C1, C2, W5 and W6, which is 4 of 14. C2, W5 and W6 are answered: E-13 to E-17 serve the model, AUA and account-count figures she reads in Chrome. C1 is tagged only by E-25 (Bloomberg prices and reference data). C1's workflow is generating YCharts Overview, Comparison and Multi-Comp PDFs for about 30 households a month, and that need is E-20, a GAP. The brief's IV.A row calls E-25 the 'C1 alternative', a source of prices, not a replacement for the report. So the catalog overstates the retired count by one. C3 (Schwab Advisor Center: Tax SMA quarter-end statements and cost-basis exports, P0) is tagged by no entry, although E-4, E-5 and E-9 are its needs. The brief's Part II names only C7, C8 and W3 as outside. Every entry otherwise carries a tag or a retires_none reason (E-26, E-27).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python count over DATA_CATALOG.yaml needs (status SERVED, retires): ['C1','C2','W5','W6'] 4 of 14; tagged by any status: 11 of 14; untagged C3, C7, C8",
        "brief :88 names C7, C8, W3 outside; ALYSSA_WORKFLOWS_INDEX_INPUT_MAP_20261009.md C1 and C3 rows"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
