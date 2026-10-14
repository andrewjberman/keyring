# MDPF_CANON -- round 6 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-14T14:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T14:05:00Z. L8 packet: 2.0.0_SA_COO~D1 msg 5581, `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round6/ROUND6_DRAIN_END.md` @e647498179 (blob 4def2599f9ff, verified).

**L9:** AC4 of TO-CN-f-1 MET on the first folded scheduled fire (D1-C-S67). **Rows:** 9 of 9 since v8's watermark: 4 graduated ARMED/BLOCKING, 2 graduated INERT, 3 dismissed; this seat's D1-S24 graduated. Clocks closed: D1-S18, D1-C-S65.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S67",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:05:00Z",
    "one_line": "ROUND 6 L9: JUDGMENT MDPF_CANON.TO-CN-f-1 AC4 MET -- fold-to-served seam read after the 13:30Z fire: 0 lines held by fewer than two firms, the statement names no model, and the client-visible deltas are the pair's (Total Holdings -177 vs -185 named, cards -$43.6M, history from 2026-05-15, 10 of 20 quarter cells absent) plus the PRD's ratified Other Models line.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-f-1 AC4 (judgment): '/seams on the fold-to-served seam, grounded on the objects after the first scheduled run that carries the code -- MECHANICAL (the four global objects read back hold no model line held by fewer than two firms on any date they carry), DECLARATIVE (the in-band statement says why per-model detail begins when it does, and names no model), SEMANTIC (the only client-visible deltas are the ones the never-widen pair names: the two inflection blends leaving the Model Portfolios roll-up and the Total Holdings count, and per-model history starting where Global first combined two firms).'",
    "world_is": "ROUND 6 L9, JUDGMENT MDPF_CANON.TO-CN-f-1 AC4: MET, on this seat's re-runs after the first folded scheduled fire (2026-10-14 13:30Z). Packet @e647498179 (blob 4def2599f9ff, verified), msg 5581. MECHANICAL: r6_fold_readback.py read (global 2026-10-13, prior 2026-10-12, 496 dates) R1 PASS 6 model-class lines over 569 line-dates, 0 held by fewer than two firms; ROUND 6 READBACK 9 of 9 arms on this seat's run, including R4 headline fields equal on 494 common dates, R5 identity 0 violations on 485 valued dates, R6 three firm scopes 1,464 firm-dates equal, R9 run.code.commit = package = MDPF_GOLD_COMMIT = 51cfc93ea8 with errors empty. DECLARATIVE: R2 PASS -- min_firms 2, detail begins 2026-05-15 = the first kept date, the statement is 264 characters and names no model. SEMANTIC, against the pair's section 6 (portfolios_card.py after --date 2026-10-14, the tool's documented run date): Total Holdings 8,607 -> 8,430 (-177; the pair named -185, the 8-account gap is R7's roster drift 211 vs 207); archetype cards -$43.61M in all (the pair named -$43.16M at the 2026-10-09 as-of; this read is the 10-13 as-of); trend first per-model date 2024-11-01 -> 2026-05-15 and series 14 -> 6; core quarter cells absent 0 -> 10 of 20 (named, section 6 bullet 4). The page also shows an 'Other Models' card ($69,190,304.67, 205 accounts) and an Other Models trend series on 49 dates. That is FWD-3's pooled 'Other Models' line, the PRD's ratified outcome (PRD :200, :260, :620), built by the order under that display name and named by the pair (section 4's other_models key; section 6 bullet 3); the pair's client-visible list does not name the CARD in words, which the card to Andrew should. aum-metrics total.aum +$6,834,349.37 with account_count unchanged is the new as-of date (10-12 -> 10-13), not a fold delta (R4: headline fields equal on every common date). NOT EXERCISED: the CTO's refusal arm (no one-firm as-of occurred). The packet's own 'Total Holdings 8,607 -> 8,607' is a wrong-date read: row D1-S24.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python round6/checks/r6_fold_readback.py read: ROUND 6 READBACK: 9 of 9 arms",
        "3.0.0_SA_CVO python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py after --date 2026-10-14 (and --date 2026-10-13 for the packet's figure)",
        "round6/NEVER_WIDEN_PAIR_R6_CN_F_1.md sections 4-6",
        "prd/MDPF_CANON_PRD.md :200, :260, :620",
        "task-orders/MDPF_CANON.TO-CN-f-1.global-min-firms-fold.md :62, :80, :123, :133-134, :197-200"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record: AC4 MET."
  },
  {
    "id": "MDPF_CANON-D1-C-S68",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:05:00Z",
    "one_line": "GRADUATED to REMEDIATION_v6 (ARMED/BLOCKING): D1-W16-S1 (disarmed by AMENDMENT 1, refusal branch not yet exercised), D1-W16-S2+S4 (stale Other Models current value on a no-pool day), D1-W16-S5 (unfolded staged copy, readers unverified).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W16-S1",
      "MDPF_CANON-D1-W16-S2",
      "MDPF_CANON-D1-W16-S4",
      "MDPF_CANON-D1-W16-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to REMEDIATION_v6: D1-W16-S1 (BLOCKING: an unbalanced Global category-views build on a one-firm as-of) is DISARMED by AMENDMENT 1 (a one-firm as-of refuses Global whole, pair section 5), but the refusal branch has not run on a served day (the CTO's third arm, NOT EXERCISED); it stays OPEN, owner 2.0.0_SA_COO~D1, until the first organic one-firm as-of is read. D1-W16-S2 with D1-W16-S4 (ARMED: on a no-pool as-of the fold line is None on the last date and build_aum_metrics' _frontier fallback serves the last pooled dollars as the Other Models card's CURRENT value and its q-cells; not live today, reachable on any no-pool day; the issuer reads it INERT because the carried dollars were pooled at two firms, which answers privacy, not the honest-None the pair's own section 6 relies on) -> 1.0.0_SA_CTO~DELL1, as both rows route. D1-W16-S5 (ARMED: the staged global aggregate is written pre-guard and unfolded on every run, and its readers are unverified) -> 1.0.0_SA_CTO~DELL1 to rule whether it moves behind the guard; 'unfolded by design' holds only while no reader serves it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-W16-S1, MDPF_CANON-D1-W16-S2, MDPF_CANON-D1-W16-S4, MDPF_CANON-D1-W16-S5",
        "round6/NEVER_WIDEN_PAIR_R6_CN_F_1.md section 5",
        "R6_DRAIN_END section 3: the CTO's third arm NOT EXERCISED"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "MDPF_CANON-D1-C-S69",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:05:00Z",
    "one_line": "GRADUATED to REMEDIATION_v6, INERT: D1-S22 (publisher cannot read its own pointer), D1-S23 (equality tool hashes the working tree), D1-S24 (the card's Total Holdings misread).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S22",
      "MDPF_CANON-D1-S23",
      "MDPF_CANON-D1-S24"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "GRADUATED to REMEDIATION_v6, INERT, owner 2.0.0_SA_COO~D1: D1-S22 (the portal publisher's role is denied s3:GetObject on its own latest.json, so every run republishes all 18 leaves with the same data and a newer written_at; nothing served is wrong; the remedy is one IAM grant). D1-S23 (the code-equality tool hashes the working tree, so a CRLF checkout reads a false DIFFER; the round-7 repair cell the packet stages). D1-S24 (this seat's: the packet's card reads Total Holdings delta 0 on the wrong date; the card to Andrew states -177).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows MDPF_CANON-D1-S22, MDPF_CANON-D1-S23, MDPF_CANON-D1-S24"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "MDPF_CANON-D1-C-S70",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:05:00Z",
    "one_line": "DISMISSED 3 round-6 rows (D1-W16-S3, D1-S20, D1-S21), each with its own reason.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W16-S3",
      "MDPF_CANON-D1-S20",
      "MDPF_CANON-D1-S21"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "DISMISSED, 3 rows: D1-W16-S3: A judgment input for AC4, not a hazard; C-S67 grades AC4 on the served objects. D1-S20: BLOCKING, INERT on read: the two new tax-prelude snapshot objects are create-if-absent writes inside the pair's signed radius (section 4, 'tax prelude stores ... create-if-absent'); the same pattern is on record for 2026-10-12 before the deploy; every served object and VersionId was unchanged. D1-S21: 0.00 against each date's own dated object on 21 of 21; the difference is the newest series restating, which the card carries.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "the investigation rows named",
        "round6/NEVER_WIDEN_PAIR_R6_CN_F_1.md section 4"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "DISMISSED, 3 rows: D1-W16-S3: A judgment input for AC4, not a hazard; C-S67 grades AC4 on the served objects. D1-S20: BLOCKING, INERT on read: the two new tax-prelude snapshot objects are create-if-absent writes inside the pair's signed radius (section 4, 'tax prelude stores ... create-if-absent'); the same pattern is on record for 2026-10-12 before the deploy; every served object and VersionId was unchanged. D1-S21: 0.00 against each date's own dated object on 21 of 21; the difference is the newest series restating, which the card carries."
  },
  {
    "id": "MDPF_CANON-D1-C-S71",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T14:05:00Z",
    "one_line": "L10 record: round 6's 9 rows since the watermark dispositioned; D1-S18 and D1-C-S65 clocks closed; AC4 MET.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S18",
      "MDPF_CANON-D1-C-S65"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "L10 PRECONDITION MET: round-close-check --project MDPF_CANON --round 6 on this seat: orders=1, proof_ok 1, judgment 1 graded 1 (AC4 by C-S67), verdict MAY-CLOSE. Every investigation row after ADJUDICATION_v8's watermark (2026-10-12T17:51Z) is dispositioned: 9 of 9 (C-S68 graduates 4, C-S69 2, C-S70 dismisses 3), plus this seat's D1-S24. Remediation clocks closed: D1-S18 (REMEDIATION_v5) -- R9 on this seat's run reads run.code.commit = package = MDPF_GOLD_COMMIT = 51cfc93ea8; D1-C-S65 (REMEDIATION_v5) -- the CN-f-1 pair names the control key in its radius (sections 3-4), the sign-off C-S65 found missing. AC4 MET (C-S67). The CTO's refusal arm is carried by D1-W16-S1's open remediation.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this file's rows C-S67..C-S70",
        "remediations/REMEDIATION_v5.md clocks D1-S18, D1-C-S65",
        "3.0.0_SA_CVO r6_fold_readback R9"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The L10 record."
  }
]
```
