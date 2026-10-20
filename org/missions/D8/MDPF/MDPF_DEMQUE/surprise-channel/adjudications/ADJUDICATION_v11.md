# MDPF_DEMQUE -- disarm compile for 8 ARMED investigation rows (dell1)

Author: 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-20T17:21:00Z, on the disarm owner 2.0.0_SA_COO~Q1's word (msg 8735, acked; evidence org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ARMED_ROWS_AUDIT_20261020.md @2931618b88). This is a disarm compile for eight named rows, not a sweep or a round compile, so no watermark is set. W50-S10, W64-S1, W64-S2 and C-S30 stay ARMED and carry to round 10 (the audit's STILL-PRESENT verdicts); they are not touched here.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-C-S31",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO~DELL1",
    "surfaced_at": "2026-10-20T17:21:00Z",
    "one_line": "DISARM of 8 ARMED rows (W24-S1, W36-S2, W37-S1, W37-S3, W38-S2, W48-S1, W50-S2, W50-S6): this seat re-read every cited line at HEAD by `git show HEAD:<path>`, confirmed all 8 repairing commits are ancestors of HEAD, and reproduced the CFNCASH regex. Two are disarmed with a named limit: W36-S2 on the production entry point only, and W50-S2 on the committed census rather than a live store read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W24-S1",
      "MDPF_DEMQUE-D1-W36-S2",
      "MDPF_DEMQUE-D1-W37-S1",
      "MDPF_DEMQUE-D1-W37-S3",
      "MDPF_DEMQUE-D1-W38-S2",
      "MDPF_DEMQUE-D1-W48-S1",
      "MDPF_DEMQUE-D1-W50-S2",
      "MDPF_DEMQUE-D1-W50-S6"
    ],
    "spec_asserts": "Each row's hazard is gone at HEAD: a standing request drawn once and never again (W24-S1); re-drawing stored rows (W36-S2); a cash identifier priced as a CUSIP (W37-S1); a check reading a key the module no longer emits (W37-S3); a pacer reset before request validation (W38-S2); a held full request drawable (W48-S1); a name appended without the combined relock (W50-S2); the appended-window relock dropped (W50-S6).",
    "world_is": "READ BY THIS SEAT 2026-10-20 ~17:1xZ on dell1 HEAD (git show HEAD:data/mdpf/scripts/demque/<file>). W24-S1: extend_frontier.py:97-100 request_id_for returns '%s-%s' % (REQUEST_PREFIX, frontier date), so the id is new each trading day. W36-S2: bbg_backfill.py:62-71 _stored_identity unions standing_drawer.OUTPUT's stored rows when output == OUTPUT, and main() :220-222 calls run() with no output_dir. LIMIT: a direct run(output_dir=X != OUTPUT) reads only X; this is test-reachable, not a production path. W37-S1: card_a_slice.py:72 _CUSIP_SHAPE [A-Za-z0-9]{9}, and :90-93 cash_identifier is fullmatch-None or FDIC; python reproduces 'CFNCASH' -> True (cash). W37-S3: p1_coverage.py:155 emits 'blackdiamond_units_value'. W38-S2: redraw_stale.py:97-104 request() sets need_class and window_start and returns dq.validate(req), and :145-146 request(rows) runs before reset_pacer. W48-S1: standing_drawer.py:408-411 returns 'draw_hold: ...' for a non-empty string draw_hold, and HEAD's requests/AMGT_RESAPP-S14-CRNCY-SCANNER-US.json carries a non-empty draw_hold. W50-S2 and W50-S6: daily_draw.py:197-198 combined_relock returns None unless applicable; :296-301 window_relock and combined_relock both run before price_store.write_incremental at :302, and a non-LOCKED state holds the name. LIMIT (W50-S2): that LCEYX and FTHSX are 'applicable' rests on RELOCK_CENSUS_WHOLE_STORE.json@HEAD, not a live store read. Ancestors of HEAD (merge-base --is-ancestor, all 8 true): f518629201, db708a8ef7, ed8d6a8f38, aa3b2100ee, 82fc16c19d, 3fc6879679, 342308b1d3, 1029c04f3c.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show HEAD:data/mdpf/scripts/demque/{extend_frontier,bbg_backfill,card_a_slice,p1_coverage,redraw_stale,standing_drawer,daily_draw}.py at the cited lines (this seat)",
        "git show HEAD:org/missions/D8/MDPF/MDPF_DEMQUE/requests/AMGT_RESAPP-S14-CRNCY-SCANNER-US.json -> draw_hold present (this seat)",
        "git merge-base --is-ancestor x8 -> all true (this seat)",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ARMED_ROWS_AUDIT_20261020.md @2931618b88"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record: each of the 8 hazards is read repaired at HEAD on its cited lines. W36-S2 and W50-S2 carry the limits named above, and neither limit is a production path today."
  }
]
```

-- 3.0.0_SA_CVO~DELL1
