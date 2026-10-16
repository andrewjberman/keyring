# NFRA_MCPORTAL -- S1 item (iii) re-graded on the second served packet (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v10. Fabric: site-z. Recorded: 2026-10-16 ~14:3xZ.
**Input:** `2.0.0_SA_COO~MP` msg 35050 (acked). `deliverables/2.0.0_SA_COO~MP/pf/PF_S1_SERVED_PACKET_20261016T14Z.md`, sha256
`2a49a7959c46`, read whole. It supersedes the first packet, which v9 (`Z-C-S46`) graded NOT MET at 390 px.

**S1 item (iii), legibility of the served page at 1280 and 390 px: MET, bounded.**

- **Host state** (packet section 1): `mcportal_commit` `c66ca82952` (MP-pf-8) and `deployed_commit` `d14445961d` on the v3
  catalog base. The built files equal the host's by sha256 (`pf9.AC2.sh`).
- **The defect v9 failed on is gone, by measurement.** At a true 390 px in a real browser over the SERVED body, `scrollWidth=390
  innerWidth=390 offenders=0`, against 561 of 390 before. 1280 reads 1280 of 1280.
- **The fix, read at its bytes** (`mcportal c66ca82952:src/pages/gateway/gateway.css:101-103`): `.gateway-indexes {
  overflow-x: auto; }`. The Indexes paragraph now scrolls inside its own box instead of widening the page.
- **Images, viewed by this seat:**
  - `served_1280_top.png`: the summary at 14:08:44Z, "14 groups, 127 tools", with the eight resolved segments indented under
    `opal-data-assets`.
  - `served_390_top.png`: the same at phone width. Group names sit on one line, the page does not slide, and the summary's
    cut columns show the right-edge shade.
- **The bounds:**
  1. The card Indexes paragraphs, where the defect lived, are not imaged. The issuer withheld those images because the real
     index names carry Schwab master numbers and this box's client-data check is not running (Z-S63). That is a correct
     withholding. Their non-overflow is carried by the measured `offenders=0`, not by sight.
  2. **No scroll cue on the Indexes box.** The cue's background layers are declared on `.gateway-scroll` only (`:72-78`), not
     on `.gateway-indexes`. At 390 px a 65-character index name is therefore cut inside its box with nothing saying more lies
     to the right. That is the same gap this seat carried for the tables in v6 (`Z-C-S38`), which MP-pf-5 closed there. It is
     an enrichment, not grounds: the page reads, and nothing is squished or broken mid-word.
  3. Andrew's own signed-in look (call 21d9) is his and is not graded here.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S47",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T14:30Z",
    "one_line": "S1 item (iii) legibility on the SERVED body: MET, bounded -- after MP-pf-8/pf-9 the page no longer scrolls sideways at 390 px (scrollWidth 390/390, offenders 0, against 561 before) and 1280 reads; bounds: the card Indexes paragraphs are not imaged (rightly withheld, Schwab master numbers), and the Indexes box carries no scroll cue (CSS declares the cue on .gateway-scroll only).",
    "class": "OBSERVATION",
    "spec_asserts": "CTO PE+PF round-2 analysis S1 item (iii): the served /gateway page is legible at 1280 and 390 px, against Andrew's words in MP-pf-2 (legible, not wrapped or squished, clearly segmented).",
    "world_is": "PF_S1_SERVED_PACKET_20261016T14Z.md (sha256 2a49a7959c46): mcportal c66ca82952 on deployed d14445961d, host files equal by sha256; real browser over the served body: 390 -> scrollWidth 390, offenders 0; 1280 -> 1280. served_390_top.png and served_1280_top.png viewed: summary and eight segments read, no page slide, summary scroll cue present. gateway.css@c66ca82952:101-103 .gateway-indexes overflow-x auto; :72-78 the cue layers on .gateway-scroll only.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-C-S46"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/pf/PF_S1_SERVED_PACKET_20261016T14Z.md (read whole)",
        "deliverables/2.0.0_SA_COO~MP/pf/evidence_pf9_served_d14445961d/served_1280_top.png, served_390_top.png (viewed)",
        "mcportal c66ca82952:src/pages/gateway/gateway.css:72-78, :101-103 (read by this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade: S1 item (iii) MET, bounded. Supersedes v9's NOT MET (Z-C-S46). Enrichment: give .gateway-indexes the same scroll cue .gateway-scroll carries. S1 itself waits on Andrew's look (21d9)."
  }
]
```

-- 3.0.0_SA_CVO~Z
