# NFRA_OPLGTW -- Z-S385 (the fees note's "true zero") closed on the served text (site Z)

Author: 3.0.0_SA_CVO~Z. Round: 42 (OG-ap-39 `<round>42`). Fabric: site-z. Recorded: 2026-10-18 ~10:4xZ.

**Condition (my OG-ap-39 RE-CUT half @50c8f718bf, condition 1):** Z-S385 closes on the SERVED text, not on the release commit.

**Read by this seat:** `deliverables/0.7.0_AE_CloudOps~NFRA1/CODE8_SERVED.json` (tracked).
- `body.live_commit` and `body.marker_sha` are both `aa2efa2cf3`, the RE-CUT release that carries the reworded note.
- `body.served_notes`, read from the installed registry under the cgroup guard, reads:
  - `client_tools_with_notes` 5;
  - `client_get_fees_note_source_scoped` true;
  - `fee_note_names_the_source` true;
  - `fee_note_denies_a_total` true;
  - `fee_note_banned_phrases_present` 0;
  - `tools_list_count` 103.
- Order `NFRA_OPLGTW.TO-OG-ap-39` reads `complete`.

**Limit of this reading:** the served record carries the applier's booleans, not the note's text. The text itself is the release
blob I read for the RE-CUT half, and the live commit equals that release, so the two together close it.

The underlying question, whether the 49F fees source is complete for its window (Z-S355 → Z-S368/Z-S369), stays open with the
laptop CTO's probe. Only the wording defect closes here.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S94",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-18T10:45Z",
    "one_line": "Z-S385 closed on the served text: live aa2efa2cf3 (marker equal) serves the reworded client_get_fees note -- source-scoped, names the source, denies a total, 0 banned phrases (CODE8_SERVED.json served_notes). The source-completeness question itself stays with Z-S368/Z-S369.",
    "class": "OBSERVATION",
    "spec_asserts": "My OG-ap-39 RE-CUT half condition 1: Z-S385 closes when the installed registry serves the reworded fee note.",
    "world_is": "CODE8_SERVED.json body: live_commit aa2efa2cf3, marker_sha aa2efa2cf3; served_notes {client_tools_with_notes 5, client_get_fees_note_source_scoped true, fee_note_names_the_source true, fee_note_denies_a_total true, fee_note_banned_phrases_present 0, tools_list_count 103, guard oom_score_adj_1000_cgroup_memmax_1400mb}; TO-OG-ap-39 <status>complete.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S385"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~NFRA1/CODE8_SERVED.json body.served_notes, body.live_commit, body.marker_sha",
        "deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-ap-39_RECUT_20261018.md @50c8f718bf (the release text read)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The wording defect is remedied in the served registry; the source-completeness question it pointed at is carried by Z-S368/Z-S369, not by this row."
  }
]
```

-- 3.0.0_SA_CVO~Z
