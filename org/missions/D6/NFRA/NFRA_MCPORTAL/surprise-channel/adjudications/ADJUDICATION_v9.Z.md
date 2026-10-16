# NFRA_MCPORTAL -- S1 served arm, item (iii) legibility on the SERVED body (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v9. Fabric: site-z. Recorded: 2026-10-16 ~11:3xZ.
**Input:** `2.0.0_SA_COO~MP` msg 34942 (acked); `deliverables/2.0.0_SA_COO~MP/pf/PF_S1_SERVED_PACKET.md` @e734663690, read to EOF.
**Channel read:** `investigations/INVESTIGATION_v1.Z.md` holds 125 rows, 1 after the v8 watermark (Z-S63): `Z-S64`, BLOCKING, ARMED,
disarm owner `2.0.0_SA_COO~MP`. It is carried below (Z-C-S46), not dismissed. **Watermark:** every row through `NFRA_MCPORTAL-Z-S64`.

## The grade

**S1 item (iii), legibility of the served page at 1280 and 390 px: NOT MET.** It is met at 1280 and fails at 390.

I looked at all four images in `pf/evidence_s1_served_0cb4a87bcb/`, the SERVED body read at 10:59:30Z rendered through the real
`GatewayView` and CSS at mcportal `090b9cdc85`.

- **1280 (`s1_1280_top.png`, `s1_1280_card_smartx_multi.png`): MET.**
  - The summary reads "14 groups, 127 tools", with `opal-data-assets` (5 tools, 1 holder) and its eight resolved segments
    indented beneath it as links. Black Diamond / 49 Financial and Black Diamond / Cottonwood, Commonwealth / Cottonwood,
    Eclipse / Inflection, Orion / Inflection, Schwab / 49 Financial, SmartX / 49 Financial and SmartX / Several firms are
    each one line.
  - Kinds read in plain words (AWS bucket, Segment, Data store).
  - The SmartX / Several firms card carries its reason line ("One object mixes firms; the tools filter rows by firm").
  - Its long Indexes cell is clipped inside the table's own scroll box with the cue showing.
  - This is Andrew's segmentation ask met on the real catalog, not the fixture.
- **390 (`s1_390_top.png`, `s1_390_page_scrolls_sideways_harvest.png`): FAIL.**
  - The top reads. But the second image is the page itself slid sideways: the harvest card is cut at the left, and empty
    canvas fills the right third.
  - The issuer measured `scrollWidth` 561 against 390.
  - Cause (Z-S64): the channel-level Indexes paragraph holds unbroken index names of about 65 characters, wider than its
    328 px column, in six sections.
  - A reader at 390 gets a page that moves under the thumb. That is the "squished / not readable by human eyes" Andrew's
    words exclude, and it is exactly what the MP-pf-2 fixture's short names could not show. My v6 grade (Z-C-S38) was
    bounded on that point, "the FIXTURE, not the live catalog", and this is that bound biting.
- **Observation, not grounds:** the line under the status ("Each tool joins the first group whose rule holds, in this order:
  its integration spec's channel; else ...") is a developer's placement rule shown to the page's reader. It is legible, but
  it is not what an owner reading the page needs. Shortening it is an enrichment.

**What closes (iii):** the issuer's named fix, one LOCAL mcportal cell:
- the Indexes paragraph scrolls in its own box;
- a real 60-plus-character index name goes into the checked-in fixture;
- one test pins both;
- then a served re-read at a true 390 px with `scrollWidth` equal to 390.

S1 also stays NOT REALIZED until Andrew's own signed-in look (call 21d9). That look is his and is not graded here.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S46",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T11:30Z",
    "one_line": "S1 item (iii) legibility on the SERVED body: NOT MET -- MET at 1280 (eight resolved vendor/firm segments under opal-data-assets, plain kinds, reason lines, tables scroll in their own boxes) and FAIL at 390 (the page itself scrolls sideways, scrollWidth 561 against 390, from unbroken index names in the channel Indexes paragraph; Z-S64 stays ARMED on the issuer).",
    "class": "OBSERVATION",
    "spec_asserts": "CTO PE+PF round-2 analysis (msg 34676) S1 item (iii): the served /gateway page is legible at 1280 and 390 px, against Andrew's words in MP-pf-2 (legible, not wrapped or squished, each segment clearly segmented by bucket and by client/vendor pair).",
    "world_is": "pf/evidence_s1_served_0cb4a87bcb/ (4 images, viewed by this seat): 1280 summary '14 groups, 127 tools' with the eight resolved segments indented under opal-data-assets; the SmartX/Several firms card with its reason line and a clipped scrolling Indexes cell. 390: the top reads, but s1_390_page_scrolls_sideways_harvest.png shows the page slid sideways with empty canvas on the right; issuer scrollWidth 561/390; cause the channel Indexes paragraph (~65-char unbroken names, 328 px column) in six sections.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S64"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/pf/PF_S1_SERVED_PACKET.md @e734663690",
        "deliverables/2.0.0_SA_COO~MP/pf/evidence_s1_served_0cb4a87bcb/s1_1280_top.png, s1_1280_card_smartx_multi.png, s1_390_top.png, s1_390_page_scrolls_sideways_harvest.png (viewed)",
        "NFRA_MCPORTAL-Z-C-S38 (v6: the fixture-not-live-catalog bound this grade realizes)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not a dismissal: Z-S64 stays ARMED on 2.0.0_SA_COO~MP until the Indexes-paragraph cell lands and a served 390 px re-read shows scrollWidth equal to 390; this seat re-grades (iii) on that read. Enrichment: replace the placement-rule sentence under the status line with an owner-facing line."
  }
]
```

-- 3.0.0_SA_CVO~Z
