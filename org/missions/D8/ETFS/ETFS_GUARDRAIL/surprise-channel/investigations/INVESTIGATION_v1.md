# ETFS_GUARDRAIL -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (a seat row; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `ETFS_GUARDRAIL-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `ETFS_GUARDRAIL-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`ETFS_GUARDRAIL-C-S<k>`. **Append-only during the round.** Never edit an existing row.
**Round 1 task orders:** 14, one per cell of `../../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.1.1, on three worker
slots (`0.9.0_WK_ETFS_GUARDRAIL~1`, `~2`, `~3`).

```json
[
  {
    "id": "ETFS_GUARDRAIL-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-04T19:05:00Z",
    "one_line": "EG-s-4: PRD s.7.4 homes the classifier in the ETFS layer and s.7.2 S4 binds its discriminator as 'read upstream partition + count priced' -- but the ETFS layer holds ZERO firm-bucket grants by explicit NEVER#1 design (reporter role: opal-data-etfs/* + the artifact prefix only; aggregation reader: daily/* + config/* only). L5 delegates the discriminator to the firm-scoped producers as a non-writing PROBE (EG-s-1/EG-s-2) and to the relied-on inf producer's own invoke answer; the classifier stays etfs-only and returns UNKNOWN where no probe answers; the one IAM change is an invoke grant on the reporter role (EG-s-7). No firm prefix is opened. Carried for the CTO's L10 read; not a spec edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/etfs-reports/iam.tf:24-59 @291551ca2f -- the reporter instance role's policy: ReadEtfsAggregation (s3:GetObject opal-data-etfs/*), ListEtfsAggregation, WriteReports (platinum/reports/* only), PullRendererArtifact (opal-313476888478-lambda-artifacts/ec2/etfs-reports/*); no statement names opal-data-assets, opal-data-inf, opal-data-cot or opal-data-bd",
        "infra/aws/terraform/shared-infra/etfs-aggregation-iam.tf:1-60 @291551ca2f -- the AVGCAP reader role scoped to opal-data-etfs/daily/* + config/* with the header comment 'ZERO firm-bucket grants (NEVER#1: the metric layer never reads opal-data-inf / opal-data-cot / opal-data-schwab)'",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/prd/ETFS_GUARDRAIL_PRD.md s.7.2 row S4 and s.7.4 @4e30d6b635 -- the bound 'Discriminator = read upstream partition + count priced' and the home 'data/etfs/scripts/coverage/classifier.py ... importable by the renderer'; s.7.4's own clause 'These are step-4 PROPOSALS ... a decomp finding may overturn any of them'",
        "infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py:98-144 @291551ca2f and infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py:68-95 -- each owned producer already performs the discriminator on its own firm's partition (head_object on the date= partition; priced / rows count) under its own least-privilege role"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD s.7.2 S4 bound: 'Discriminator = read upstream partition + count priced'; s.7.4: 'S4 classifier -> data/etfs/scripts/coverage/classifier.py. One home, importable by the renderer.' Read together: the classifier, running in the ETFS layer on the reporter box, reads the three firms' upstream silver partitions.",
    "world_is": "The ETFS layer's principals (etfs-reports-reporter-role; etfs-avgcap-reader-role) hold no grant on any firm prefix, by a design that names NEVER#1 as its reason. Granting the reporter role s3 reads on blackdiamond/cottonwood/*, schwab/08242234/* and orion/inflection/* in opal-data-assets would mint the cross-firm reader that design refused. The producers already hold exactly the per-firm read the discriminator needs.",
    "notes": "L5/L6 resolution (decomposition v0.1.1 s.6a): probe mode on EG-s-1/EG-s-2; the inf producer's own invoke answer for Inflection; EG-s-4 etfs-only with an injected probe and UNKNOWN as an honest value; EG-s-7 holds the invoke and the one IAM Sid (lambda:InvokeFunction on three producer ARNs, reporter role, ledgered). If the CTO's L10 read prefers a data grant instead, that is a PRD addendum at L4 and the cells re-cut; nothing in this round opens a firm prefix. Disarm needs nothing: INERT, an OBSERVATION for the record."
  },
  {
    "id": "ETFS_GUARDRAIL-W3-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~3",
    "surfaced_at": "2026-09-04T21:02:15Z",
    "one_line": "EG-s-13: the CSVs are NOT produced through render_month's call graph -- write_month_csvs is a separate function with its OWN independent load_all_daily(partner) call, invoked directly from main() alongside (not through) render_month. A call wired only inside render_month, as the deliverable's call-site text describes, would leave the CSVs on the raw Orion label. Resolved in this order's own change: _align_inflection_series is ALSO called for partner=='inflection' inside write_month_csvs, so every artifact (deck HTML, charts, matrix, CSVs) shares one date basis, matching the deliverable's stated outcome even though its named call site did not reach all of them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/presentation/render_month_end.py:684-696 @afa47031ed (pre-edit) -- write_month_csvs(month, out_dir) opens with its own `series = load_all_daily(partner)` per partner, independent of render_month's `daily` dict",
        "data/etfs/scripts/presentation/render_month_end.py:700-712 @afa47031ed (pre-edit) -- main() calls `html = render_month(month, ...)` then separately `csv_paths = write_month_csvs(month, os.path.dirname(...))`; write_month_csvs is never called from inside render_month nor passed render_month's daily dict",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only.md:24 @afa47031ed -- deliverable 1: '_align_inflection_series ... called from render_month for partner == \"inflection\" only ... before _carry_forward_avg, the charts, the matrix and the CSVs, so every artifact the month produces shares the one date basis'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Deliverable 1 states the alignment is 'called from render_month for partner == \"inflection\" only ... before _carry_forward_avg, the charts, the matrix and the CSVs' -- implying one call site inside render_month reaches every one of those artifacts, including the CSVs.",
    "world_is": "write_month_csvs is a sibling function to render_month, not a callee of it -- it loads Inflection's series itself via a second, independent load_all_daily call. The single call site the deliverable describes does not reach the CSVs at all; a literal read leaves them on the raw Orion label while the deck is aligned, breaking exactly the 'set beside each other without being a day apart' ACCEPT bar FWD-6 states for the CSVs specifically.",
    "notes": "Disarmed same-turn, no owner needed: this order's own code adds a second _align_inflection_series call inside write_month_csvs (data/etfs/scripts/presentation/render_month_end.py, partner=='inflection' branch), so the CSVs align too. INERT/OBSERVATION -- the deliverable's INTENT ('every artifact... shares the one date basis') is honored; only its literal call-site description undercounted the call graph."
  },
  {
    "id": "ETFS_GUARDRAIL-W3-S2",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~3",
    "surfaced_at": "2026-09-04T21:55:16Z",
    "one_line": "EG-s-13's own <proof_of_spec> section names the instance path 'ETFS_GUARDRAIL.TO-EG-s-13.proof_of_spec.json' (the to_id, short form), but .tools/to-pipeline-gate.py's check_complete_flip derives the expected instance filename from the TASK-ORDER FILE'S OWN BASENAME (the long descriptive stem 'ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only'), not from to_id -- so the TO-instructed filename alone REFUSES the complete flip ('NO proof-of-spec instance was found beside it'). Resolved by committing a second, byte-identical copy at the gate-expected filename alongside the TO-instructed one; both validate VALID at rc=0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/to-pipeline-gate.py:1188-1199 @afa47031ed -- check_complete_flip: `stem = os.path.basename(rel).rsplit('.md', 1)[0]` (rel = the TO FILE's own path) then `names = (stem + '.proof_of_spec.json', stem + '_PROOF_OF_SPEC.json')`, globbed under deliverables/*/ -- keyed on the TO file's basename, never on to_id",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only.md <proof_of_spec> section @afa47031ed -- 'Instance at org/.../deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/ETFS_GUARDRAIL.TO-EG-s-13.proof_of_spec.json' -- the short to_id-only form",
        "measured live: `python .tools/to-pipeline-gate.py <this TO>` with only the short-named instance staged -> REFUSED ('NO proof-of-spec instance was found beside it'); with the long-stem-named copy additionally staged -> 'OK: 0 newly-added TO file(s) carry <decomp_ref> and a complete <preflight> block.', rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The TO's own <proof_of_spec> section states the instance path using the short to_id form: 'ETFS_GUARDRAIL.TO-EG-s-13.proof_of_spec.json'.",
    "world_is": "to-pipeline-gate.py's check_complete_flip computes the expected instance filename from the TO FILE'S basename (including its full descriptive suffix), not from to_id -- a different, longer string. A worker following the TO's own instructed filename literally cannot flip the order to complete without the gate refusing.",
    "notes": "Disarmed same-turn, no owner needed for THIS order: a second, byte-identical proof_of_spec.json was committed at the gate-expected long-stem filename beside the TO-instructed short one; both are structurally VALID (rc=0) and carry identical content. Left for a wider owner: every OTHER ETFS_GUARDRAIL TO whose own <proof_of_spec> section (if any) names the short to_id form will hit the same refusal on its complete flip -- a generic fix (gate accepts EITHER form, or every TO's <proof_of_spec> section is authored to the gate's actual convention) is outside this order's <paths>."
  }
]
```
