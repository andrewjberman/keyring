# AMGT_CORPUS -- round 41 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-09T18:27Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T18:27:00Z. L8 packet: 2.0.0_SA_COO~C1 msg 2965, `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/ROUND41_DRAIN_END_PACKET.md @38b91c82a3`. 4 of 4 complete.
**L9 -- aq-3 AC3 (judgment): MET** (row D1-C-S5). BLOCKING D1-W1-S1 dismissed (resolved by AMENDMENT 1). D1-S1 stays in REMEDIATION_v6.

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S5",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T18:27:00Z",
    "one_line": "AMGT_CORPUS.TO-CRPS-aq-3 (feed-matches-real-terms-only) AC3 MET: on PBR US's News tab the team's thesis term is offered as one filter, 'production -- 1 of 10 headlines', and no pillar title is offered as a filter; the one matching headline ('Petrobras signs production-sharing deals for eight Ivory Coast exploration blocks') is listed among the ten. On 8035 JP the page says 'The research team's thesis pillars carry no term to filter the news.' and shows no filter. Notes: the walk did not press the filter (its count is read from the render check, term 'production' count 1 -> that headline); the match is lexical ('production-sharing' is a contract form, close to but not the same as an output theme); and only 2 of 95 names qualify (14 no term, 49 no pillars served), so the feature reaches few names today.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "AMGT_CORPUS TO-CRPS-aq-3 AC3 (feed-matches-real-terms-only); spine L9: graded by a seat that did none of the work.",
    "world_is": "AMGT_CORPUS.TO-CRPS-aq-3 (feed-matches-real-terms-only) AC3 MET: on PBR US's News tab the team's thesis term is offered as one filter, 'production -- 1 of 10 headlines', and no pillar title is offered as a filter; the one matching headline ('Petrobras signs production-sharing deals for eight Ivory Coast exploration blocks') is listed among the ten. On 8035 JP the page says 'The research team's thesis pillars carry no term to filter the news.' and shows no filter. Notes: the walk did not press the filter (its count is read from the render check, term 'production' count 1 -> that headline); the match is lexical ('production-sharing' is a contract form, close to but not the same as an output theme); and only 2 of 95 names qualify (14 no term, 49 no pillars served), so the feature reaches few names today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T173706Z/shots/005-PBR-press-1.png: ten headlines, 'THE RESEARCH TEAM'S THESIS TERMS -- FILTER THE NEWS', one filter 'production -- 1 of 10 headlines', the Ivory Coast production-sharing headline listed",
        "3.0.0_SA_CVO viewed tmp/ui-walk/20261009T173706Z/shots/037-8035-press-1.png: one headline; 'The research team's thesis pillars carry no term to filter the news.'; no filter",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/evidence/r41_aq3_close_read_20261009.txt @b0585eff04: render check PBR real terms ['production'], count 1 -> the Ivory Coast headline, pillar-title filters 0; 8035 real terms [], pillar-title filters 0",
        "evidence/r41_aq3_close_pick_20261009.txt: 95 names, qualify 2 (BP/ LN, PBR US), no_term 14, no_dossier 49, errors 0",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/ROUND41_DRAIN_END_PACKET.md @38b91c82a3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: judgment criterion AC3 of TO-CRPS-aq-3 graded MET by a seat that did none of the work."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S6",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T18:27:00Z",
    "one_line": "D1-W1-S1 (BLOCKING) dismissed: the aq-1/aq-2 control arms compared the whole value; the issuer's check AMENDMENT 1 @2ceea5883b makes each control grade its own edge, and aq-2 was re-proved on it in-round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_CORPUS-D1-W1-S1"
    ],
    "spec_asserts": "AMGT_CORPUS TO-CRPS-aq-3 AC3 (feed-matches-real-terms-only); spine L9: graded by a seat that did none of the work.",
    "world_is": "D1-W1-S1 (BLOCKING) dismissed: the aq-1/aq-2 control arms compared the whole value; the issuer's check AMENDMENT 1 @2ceea5883b makes each control grade its own edge, and aq-2 was re-proved on it in-round.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_CORPUS-D1-W1-S1",
        "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/ROUND41_DRAIN_END_PACKET.md @38b91c82a3 s.4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S1 (BLOCKING) dismissed: the aq-1/aq-2 control arms compared the whole value; the issuer's check AMENDMENT 1 @2ceea5883b makes each control grade its own edge, and aq-2 was re-proved on it in-round."
  },
  {
    "id": "AMGT_CORPUS-D1-C-S7",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T18:29:00Z",
    "one_line": "Pointer for row AMGT_CORPUS-D1-C-S5: judgment criterion AC3 of AMGT_CORPUS.TO-CRPS-aq-3.feed-matches-real-terms-only is graded MET there (the order carries no <to_id>, so its id is its filename stem).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "spine L9: a judgment criterion is graded by a seat that did none of the work.",
    "world_is": "Pointer for row AMGT_CORPUS-D1-C-S5: judgment criterion AC3 of AMGT_CORPUS.TO-CRPS-aq-3.feed-matches-real-terms-only is graded MET there (the order carries no <to_id>, so its id is its filename stem).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "row AMGT_CORPUS-D1-C-S5 in this file",
        "org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aq-3.feed-matches-real-terms-only.md (no <to_id> tag)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A pointer to an L9 grade record, not a hazard."
  }
]
```
