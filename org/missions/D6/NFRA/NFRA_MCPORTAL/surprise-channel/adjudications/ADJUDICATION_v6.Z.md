# NFRA_MCPORTAL -- workstreams PE + PF round 2 L8 compile + L9 (site Z), with the PD and earlier backlog

Author: 3.0.0_SA_CVO~Z. Round: v6. Fabric: site-z. Recorded: 2026-10-16 ~02:4xZ.
**Input:** `2.0.0_SA_COO~MP` `deliverables/2.0.0_SA_COO~MP/pf/PF_R2_DRAIN_PACKET.md`, read to EOF (msg 34664, acked). It
reports PE + PF with 5 of 5 orders terminal and round-close-check `MAY-CLOSE`. One judgment criterion is owed, MP-pf-2 AC2,
and it is graded here (Z-C-S38).

**Channel read:** `investigations/INVESTIGATION_v1.Z.md` holds 119 rows: 110 `UNDER_INVESTIGATION` and 9 `DISMISSED_WITH_REASON`.
Of the 110, 83 are adjudicated in v2-v5 or disarmed by an issuer row. That leaves **27 undispositioned rows**, every one
dispositioned below.
- 24 are DISMISSED in Z-C-S39. Z-W33-S4 (no true 390 px reading) is among them; the issuer's 390 px run, graded in
  Z-C-S38, closes it.
- 3 GRADUATE: Z-C-S40 takes Z-W25-S2; Z-C-S41 takes Z-W31-S6 and Z-W31-S7.
- Total: 24 + 3 = 27.

The subtraction had to be run twice. The first pass filtered on the wrong disposition token and read 0; this second
pass keys on `UNDER_INVESTIGATION`.

**Watermark:** every row through `NFRA_MCPORTAL-Z-W31-S8` (surfaced 2026-10-15T23:23:18Z) is dispositioned.

## The grade (L9)

**MP-pf-2 AC2, legibility at 1280 px and 390 px: PASS, bounded.**

The bar is the order's own quote of Andrew: "extremely legible, clean, and well-designed ... readable by human eyes and
not wrapped or squished on text and segments ... each displayed tool segment is very clearly segmented ... by bucket,
and in the case of opal-data-assets, by client/vendor pairs".

I looked at all four screenshots (`pf/evidence_421f8fb/`) myself:

- **1280, full page (`pf_1280.png`):** The summary table leads with each bucket, and its vendor/firm segments are
  indented under it. Every opal-data-assets and opal-data-bd pair is its own bordered card, with a bold
  `Vendor / Firm` heading, a tool count and a four-column table. Each bucket is a separate section with a rule between
  sections. Nothing wraps, and no column is squished. The gap segment reads in red as a gap, not as a firm. This
  clearly meets Andrew's segmentation ask.
- **1280, segment detail (`pf_1280_segment.png`):** The cards are evenly spaced. Every cell is on one line with generous
  column widths, and the reason lines (SmartX "One object mixes firms", Market data "Not a client source") read plainly.
- **390, top (`pf_390_top.png`):** The title, button and status line read. The summary table keeps every group name on
  one line, so nothing is squished. Its Kind/Tools/Holders columns run off the right edge ("AWS", "Segr") and are
  reached by scrolling inside the table's box. The page itself does not scroll sideways (issuer: scrollWidth 390 of 390).
- **390, segment (`pf_390_segment.png`):** The card heading breaks between words ("Firm not / resolved"), and the red gap
  line wraps as prose. The tools table shows Tool and Access, and the other two columns are behind the inner scroll.
  The Indexes line breaks at a hyphen (`idx-` / `performance`), as the packet discloses.

**Why PASS:** at both widths no text is squished or broken inside a word, and the segmentation is unmistakable. At 390
the order's own design (one-line cells, a scroll box per table, named test `every table cell keeps its text on one
line`) trades wrapping for an inner scroll. That is exactly Andrew's "not wrapped or squished".

**Bounds, carried and not grounds to fail:**
1. **This is the FIXTURE, not the live catalog.** The live page segments nothing until MCPINDEX's C-GROUP catalog
   release and OG-ap-23 (Z-C-S41). The served look is a separate read and Andrew's sitting.
2. **Enrichment candidate, 390 px:** a cut column shows no scroll cue. A reader sees "Segr" with nothing saying more
   lies to the right, and on the summary table that hides the Kind column of the page's index. A fade or a visible
   scroll edge would close it. This is a judgment for the next round, not a failure of this criterion.
3. The 390 viewport figure is the issuer's measurement in a real browser. This seat read the PNGs, which are 390 px
   wide, and did not re-render.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S38",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T02:45Z",
    "one_line": "L9 grade, NFRA_MCPORTAL.TO-MP-pf-2 AC2 (judgment, PF round 2): PASS, bounded -- at 1280 and 390 px no text is squished or broken inside a word and every bucket and vendor/firm pair is its own bordered segment; bounds: fixture not live catalog, and at 390 a cut table column shows no scroll cue.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-pf-2 AC2: legibility at 1280 px and 390 px, graded from the issuer's screenshots, against Andrew's words in the order (legible, not wrapped or squished, each segment clearly segmented by bucket and by client/vendor pair).",
    "world_is": "pf_1280.png and pf_1280_segment.png: summary table with segments indented under buckets; one bordered card per (vendor, firm) with bold heading, count, reason line where owed, four one-line columns; the gap segment in red. pf_390_top.png and pf_390_segment.png: no page-level sideways scroll (issuer scrollWidth 390/390); group names and tool names on one line; headings break between words; tables scroll inside their card, so Kind/Tools/Holders and Data class/Indexes are off the right edge with no visible cue; Indexes breaks at a hyphen. Run is the checked-in fixture through the real GatewayView and CSS at mcportal 421f8fb.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/pf/evidence_421f8fb/pf_1280.png, pf_1280_segment.png, pf_390_top.png, pf_390_segment.png -- viewed by this seat",
        "task-orders/NFRA_MCPORTAL.TO-MP-pf-2...md:31-33 (Andrew's words), :121 (AC2 judgment=true)",
        "deliverables/2.0.0_SA_COO~MP/pf/PF_R2_DRAIN_PACKET.md (the one real run table)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-MP-pf-2 AC2 PASS, bounded. Enrichment candidate for the round-N analysis: a scroll cue on a cut table column at narrow widths."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S39",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T02:45Z",
    "one_line": "PE/PF round 2 L8 + PD and earlier backlog: 24 rows DISMISSED with per-row reasons; the two BLOCKING rows (Z-W25-S1, Z-W27-S1) are closed by the order's own fallback and by pd-3 Amendment 1; the worker-status-flip note recurs in 4 cells.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row before the L10 slug; a BLOCKING row is dispositioned or the round does not close.",
    "world_is": "Z-S51: superseded, FWD-22 was cut (MP-pc-4, MP-pd-5/6). Z-W23-S1: the worker's repo sweep timed out; its finding U1 was graded PASS bounded in v5 (Z-C-S35). Z-W22-S1: the optional-field choice keeps the read-only test fixtures typechecking; the view shows the basis when present. Z-W25-S1 (BLOCKING): the operator role is denied dynamodb:Query, but MP-pd-1 step 3 names 'GetItem on a known key' as the alternative ('try Query first'), so the worker used a permitted branch and pd-1 is complete. Carried fact: opal-gateway-access-admin cannot Query gateway-access-state-table, so any later cell that assumes Query under that role will fail. Z-W26-S1: the Decimal revision is normalized by _plain_record before the check. Z-W26-S2, Z-W28-S4, Z-W29-S3, Z-W31-S8: the worker cannot flip its own <status> because the task-order file is outside <paths>. The issuer flipped all four (pd-2, pd-4, pd-6 and pf-3 read complete). This is the same note in 4 cells across two workstreams, a worker-bar versus <paths> mismatch the issuer can remove from the bar. Z-W29-S1, Z-W29-S2: unspecified branches (absent payload over a kept snapshot; non-object JSON). The worker's reading keeps the never-replace rule, and the issuer may rule otherwise; no defect. Z-W27-S1 (BLOCKING): resolved by MP-pd-3 AMENDMENT 1 (the key-set assertion gains 'principal'); pd-3 reads complete. Z-W27-S2: the reference body is pinned as ROUND1_PEOPLE from a pre-edit run. Z-W27-S3: the writer was absent from that base, and MP-pd-2 built set_person_access later. Z-W28-S2: a route-list comment is one route short (GET /api/admin/people); nothing reads it at runtime. Z-W28-S3: pd4.AC1.sh prints sed's rc as 'bun test rc', a misleading token, but its verdict fails closed on the parsed counts. Z-S53: site Z python is RESOLVED; Andrew reinstalled 3.14.8 (~15:0xZ 10-15, MSTR~Z msg 34481), and bare python ran several scripts for this seat this session (gr_grant_gen.py --check rc=0). Z-W31-S5: stripping whitespace in the segment key is the worker's choice and stands (one line to reverse). Z-W33-S1: 'one grid step' read as spacing.sm 20px, the C10 gap. Z-W33-S2: the h1 already takes the DESIGN.md page-title values through App.css; the default heading the issuer saw was a render without App.css. Z-W33-S3: amendment (b) already held at the inherited commit. Z-W33-S4: headless Edge floors at 477 px; the issuer's real-browser 390 px run closes it (Z-C-S38). Z-W33-S5: the branch name differs by the pf segment, and no ref was moved. Z-W33-S6: the read window reached the record-face marker; no step was taken from it, and the issuer may cut the window to lines 1-126.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S51",
      "NFRA_MCPORTAL-Z-W23-S1",
      "NFRA_MCPORTAL-Z-W22-S1",
      "NFRA_MCPORTAL-Z-W25-S1",
      "NFRA_MCPORTAL-Z-W26-S1",
      "NFRA_MCPORTAL-Z-W26-S2",
      "NFRA_MCPORTAL-Z-W29-S1",
      "NFRA_MCPORTAL-Z-W29-S2",
      "NFRA_MCPORTAL-Z-W27-S1",
      "NFRA_MCPORTAL-Z-W27-S2",
      "NFRA_MCPORTAL-Z-W27-S3",
      "NFRA_MCPORTAL-Z-W28-S2",
      "NFRA_MCPORTAL-Z-W28-S3",
      "NFRA_MCPORTAL-Z-W28-S4",
      "NFRA_MCPORTAL-Z-W29-S3",
      "NFRA_MCPORTAL-Z-S53",
      "NFRA_MCPORTAL-Z-W31-S5",
      "NFRA_MCPORTAL-Z-W31-S8",
      "NFRA_MCPORTAL-Z-W33-S1",
      "NFRA_MCPORTAL-Z-W33-S2",
      "NFRA_MCPORTAL-Z-W33-S3",
      "NFRA_MCPORTAL-Z-W33-S4",
      "NFRA_MCPORTAL-Z-W33-S5",
      "NFRA_MCPORTAL-Z-W33-S6"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.Z.md rows read by id (27 undispositioned of 110 UNDER_INVESTIGATION)",
        "task-orders: last <status> of MP-pd-1..6, pe-1..2, pf-1..3 reads complete; pd-7/pd-8 staged",
        "task-orders/NFRA_MCPORTAL.TO-MP-pd-1...md:46-54 (Query first, or GetItem on a known key); TO-MP-pd-3...md:65-69 (AMENDMENT 1)",
        "deliverables/2.0.0_SA_COO~MP/pd/PD_R2_STATE_FOR_CTO.md @98bfe6e2c8",
        "broker msg 34481 (MSTR~Z, python resolved); this session's python runs"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is closed by a permitted branch, an amendment, a later cell, or an issuer-accepted choice with its limit stated; no standing defect. Carried: the operator role has no dynamodb:Query."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S40",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T02:45Z",
    "one_line": "Z-W25-S2 GRADUATES -- Z-W24-S2's limit is closed for each principal's CONTENTS, not for the principal SET: the People equality runs over the principals the host-role scan returns, because the operator role is denied Scan, so a principal the scan misses is invisible to both sides.",
    "class": "OBSERVATION",
    "spec_asserts": "PD_R2_STATE_FOR_CTO.md row MP-pd-1: 'the People view read under the OPERATOR role equals the grant store ... Z-W24-S2's limit is closed'.",
    "world_is": "MP-pd-1 read each listed principal's profile and grants under the operator role (GetItem), which closes Z-W24-S2 for those principals. The list of principals came from app.admin_gateway_breakdown._scan_principals(BD._ddb_client()), a host-role Scan, because the operator role is measured denied dynamodb:Scan (and, per Z-W25-S1, Query). The set the page lists and the set the check iterates are therefore one read under one credential. Today 1 principal holds a data grant, so the exposure is small. It grows with every person F2 adds.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W25-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row Z-W25-S2 (admin_gateway_breakdown.py:174; pd1_page_probe.py passes BD._ddb_client())",
        "deliverables/2.0.0_SA_COO~MP/pd/PD_R2_STATE_FOR_CTO.md:9"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S41",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T02:45Z",
    "one_line": "Z-W31-S6 + Z-W31-S7 GRADUATE -- PE/PF is built against keys the live catalog does not carry (tool_index has 0 vendor, 0 firm, 0 serves, 0 store lines; a real _compute lists 2 channels, m365 11 and undeclared 75), so the served page segments nothing until MCPINDEX's C-GROUP release, and that release must not read the 273 owning-firm 'firm:' keys outside tool_index.",
    "class": "OBSERVATION",
    "spec_asserts": "PRD v0.9 C-GROUP: the Gateway page segments each bucket and, for opal-data-assets and opal-data-bd, each (vendor, firm), from the catalog's declarations.",
    "world_is": "DATA_CATALOG.yaml tool_index block (from line 1349): zero vendor, firm, serves, kind-store and source_group lines (Z-W31-S6 at 43f62f5be7, Z-W31-S7 at 994447aa53). The 273 'firm:' lines elsewhere are owning-firm values on channel, silver and portal rows, which is a different meaning under the same key name. The real _compute run gives 86 tools in 2 channels and no segments. All PE/PF evidence is fixture-driven. The handler cells ride OG-ap-23 (2.0.0_SA_COO~O).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W31-S6",
      "NFRA_MCPORTAL-Z-W31-S7"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows Z-W31-S6, Z-W31-S7",
        "deliverables/2.0.0_SA_COO~MP/pf/PF_R2_DRAIN_PACKET.md 'What the run does not show' item 1"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

## Outcome state at this compile

- PE/PF: 5 of 5 orders complete and merged; the risk is LOCAL; the live page is not served. No FWD of PE/PF is REALIZED
  until three things happen: (a) MCPINDEX's C-GROUP release, (b) OG-ap-23 carries the handler, (c) a served read (and
  Andrew's look) shows the segments on the live catalog.
- PD: 6 of 8 complete; MP-pd-7/pd-8 are staged on OG-cp-1 and Andrew's sitting (the CTO hold). FWD-21 and FWD-22 are not REALIZED.

-- 3.0.0_SA_CVO~Z
