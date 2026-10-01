# ETFS_RIVALS -- round 4 L8/L9 adjudication (site-Z fabric)

<sweep_watermark>2026-10-01T22:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01 ~23:xxZ. L8 packet: 2.0.0_SA_COO~RV msg 28073 (acked), `deliverables/2.0.0_SA_COO~RV/round4/DRAIN_END_READ_ROUND4.md` @550af8d320. Source: 1.0.0_SA_CTO~Z round-3 analysis @d4a1e22801. Review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R4_REVIEW_20261001.md` (co-committed).

Round 4: 6 of 6 orders terminal; ledgers `etfs-rivalfunds-round4` and `-round4-a1` CLOSED. Round 4's rows are the 27 surfaced after 2026-10-01T11:25Z, through 22:40Z (121 in the channel minus 94). Disposition: 24 dismissed by the 3 rows below, 3 graduated in `remediations/REMEDIATION_v4.Z.md` (W4-S9 still ARMED, W4-S7, W4-S14). In the same commit, six earlier remediation rows advance their own clocks in place, all REMEDIATED (v3 W1-S27 also DISARMED): v1 W1-S4, v2 W1-S11, v3 W1-S27, W4-S5, W4-S2 and S6. Every code hazard below was graded by reading the fix at HEAD, not by a census of the data it reads.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S14",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T23:00:00Z",
    "one_line": "Five ARMED code hazards are closed at HEAD and deployed: W2-S11 (GQGU displacing BASG in G1), S9 (GQGU labelled BASG), S10 (the enrichment step a silent no-op), W4-S8 (floors turning tests red), W4-S13 (G2 attributing every issuer capture to BASG).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S11",
      "ETFS_RIVALS-Z-S11",
      "ETFS_RIVALS-Z-S9",
      "ETFS_RIVALS-Z-W1-S35",
      "ETFS_RIVALS-Z-S10",
      "ETFS_RIVALS-Z-W1-S36",
      "ETFS_RIVALS-Z-W4-S8",
      "ETFS_RIVALS-Z-W1-S37",
      "ETFS_RIVALS-Z-W4-S13",
      "ETFS_RIVALS-Z-W1-S38",
      "ETFS_RIVALS-Z-W4-S16"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Read at HEAD by this seat: gold_canonical_shape.py:77 reads issuer silver PER FUND ('the prefix holds basg-* and gqgu-*') (W2-S11); :293-297 derives source_channel 'issuer-site:<source token of the silver object>' (S9); enrichment_bloomberg.py:579 exit_code, :589 main, :612 `if __name__ == \"__main__\"` (S10); gold_holdings_coverage.py:25-29 and :289 take a sidecar's own `fund` (a legacy sidecar is BASG's) (W4-S13). The package suite reads 306 passed, 2 skipped, 0 failed (W4-S8). All five rivalfunds Lambdas show LastModified 2026-10-01T21:54:46Z..21:55:09Z (the addendum-1 apply), after every fix merged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W2-S11, S11, S9, W1-S35, S10, W1-S36, W4-S8, W1-S37, W4-S13, W1-S38, W4-S16",
        "this seat's reads of the four modules at CLOUD HEAD 550af8d320 (line numbers above)",
        "this seat's `python -m pytest data/etfs/scripts/rivalfunds/tests -q`: 306 passed, 2 skipped",
        "this seat's `aws lambda list-functions` (LastModified per function)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R4_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each fix is in the code and in the deployed package. Two have a live proof still owed, named in the review: W4-S13 at the 2026-10-02 07:00 ET fetch (BASG then GQGU), and S10 at the next 08:03 ET vehicle run."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S15",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T23:00:00Z",
    "one_line": "Ten in-round repairs leave nothing open: two issuer check defects (W1-S28/S29 t-5.AC1, W4-S11 d-5.AC1), the retired '-h' test and the name-max G2 reader moved onto the revision contract (W1-S30..S33), and G2's missing GQGU path built and served (W4-S12, W1-S39, W4-S15).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S28",
      "ETFS_RIVALS-Z-W1-S29",
      "ETFS_RIVALS-Z-W4-S11",
      "ETFS_RIVALS-Z-W1-S30",
      "ETFS_RIVALS-Z-W1-S32",
      "ETFS_RIVALS-Z-W1-S31",
      "ETFS_RIVALS-Z-W1-S33",
      "ETFS_RIVALS-Z-W4-S12",
      "ETFS_RIVALS-Z-W1-S39",
      "ETFS_RIVALS-Z-W4-S15"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Packet :11, :16, :46-49: t-5.AC1 amended @c17bb31c04 to read G6 for a zero-trade window; d-5.AC1 amended @ba6af9b1d8 to read thresholds.min_resolved_fraction; addendum 1's control equals the deployed module on 4094 of 4094 G2 keys, and the fix moves GQGU 0 -> 307 G2 rows with BASG 645 -> 645 and 0 cross-fund rows. revision.py at HEAD carries newest(), used by the G2 reader (W1-S33). The suite reads 306 passed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W1-S28, W1-S29, W4-S11, W1-S30, W1-S32, W1-S31, W1-S33, W4-S12, W1-S39, W4-S15",
        "DRAIN_END_READ_ROUND4.md:9-18, :38-49",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R4_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired in round. The packet names the pattern: three issuer checks failed only when a worker ran them on real data. A check that FAILs at base is not proof it can PASS. The review carries it as a COO P2."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S16",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T23:00:00Z",
    "one_line": "Three rows are decided or carried: W1-S34 (an alias-bearing G1 is its own revision, served), W4-S10 (GQGU not-updated by a 2-day freshness lag, accepted until tomorrow's fetch), and S12 (the procedural bound on graduated W4-S9).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S34",
      "ETFS_RIVALS-Z-W4-S10",
      "ETFS_RIVALS-Z-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W1-S34: packet :36, BASG 2026-09-30 resolves 1.000 (33/33) via issuer-alias on the served G1. W4-S10: this seat's get of platinum/page/date=2026-10-01/manifest.json reads generated_at 2026-10-01T22:03:35Z, batch d5-publish-a1, funds_total 13, funds_updated 12, the one not-updated fund PFOE/GQGU on report_date_freshness ('latest report 2026-09-28 vs expected 2026-09-30: lag 2'), and top-level status 'not-updated'. The issuer took no 09-29/30 backfill (packet :31-32). S12 bounds W4-S9 by procedure only (no bulk import without a windowed G1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W1-S34, W4-S10, S12",
        "this seat's manifest read (above)",
        "remediations/REMEDIATION_v4.Z.md ETFS_RIVALS-Z-W4-S9 (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Decided and recorded. W4-S10's proof is the 2026-10-02 07:00 ET fetch (GQGU's 10-01 report). GQGU's 09-29 and 09-30 stay a permanent gap in its G1 history unless someone backfills them; the review names it."
  }
]
```
