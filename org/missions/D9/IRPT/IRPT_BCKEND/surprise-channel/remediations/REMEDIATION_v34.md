# IRPT_BCKEND -- backlog remediations (rows the rounds 86-93 compile missed)

<sweep_watermark>2026-10-09T02:49Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-09. Graduated at the backlog adjudication (ADJUDICATION_v42.md), round label v95: 6 rows, OPEN.
Four are ARMED with a dated deadline (cottonwood OVER_AGE 2026-10-12) and disarm on IB-pr-383's live landing.

```json
[
  {
    "id": "IRPT_BCKEND-D2-S13",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The r61 release's own driven refresh fire reached state READY at only 1 of 3 firms: inflection and cottonwood answered REFRESH_FAILED with a SAFE CORRECT action because the build dropped an entry the previous build carried, so the previous directory stays served; separately the manifest key is the manifest's OWN as_of_business_date and not the event's business_date, so the packet's '_refresh/<today>/manifest.json at all three firms' cannot hold for a firm whose source lags.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-S13",
      "MEASURED 2026-10-08 ~23:32Z on dell2, ONE driven fire of irpt-directory-refresh with payload {\"business_date\": \"2026-10-08\"}: StatusCode 200, no FunctionError, manifest_written=true for 3 of 3 firms",
      "durable manifests re-read after the fire: 49financial state=READY reason_code=REFRESH_COMPLETED_WITH_ADDITIONS revision irpt-dir/49financial/2026-10-07/1.0 delta added=19 current_entry_count=4719; inflection state=FAILED reason_code=REFRESH_FAILED; cottonwood state=FAILED reason_code=REFRESH_FAILED",
      "own round r89 (IB-pr-377 complete), terminal at commit (override scope, CTO msg 2224)"
    ],
    "remedy": "Closes with IB-pr-383's after-read: READY at 3 of 3 firms, terminated 1/1/0, the removed entry served; the manifest-key wording (its own as_of, not the event date) is stated in that order.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v95"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-D2-W187-S1",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Both dropped directory entries (inflection 1, cottonwood 1) are SOURCE_REMOVAL: the build is right and the disappearance rule fails a legitimate vendor-side removal, so IB-pr-379 stops at the diagnosis and the rule needs a ruling before inflection and cottonwood go OVER_AGE on 2026-10-12.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W187-S1",
      "deliverables/0.9.0_WK_IRPT_BCKEND~187/IB91-1_dropped_entry_diagnosis.json (this branch): disappeared ids, per-firm evidence, over-age computation",
      "inflection: household cli_eee3d5ecc6dda8132ba25158 is in silver/api_dims household_rep_mapping and accounts_v2 at snapshot 2026-10-05 (321 households) and absent from both at 2026-10-06 (320); its one account is still in accounts_v2, now under the pre-existing household cli_7f8b2aacad67b512d1e05a29 (2 accounts at 10-05, 3 at 10-06). The vendor merged the household away.",
      "own round r91 (IB-pr-379 complete), terminal at commit (override scope, CTO msg 2224)"
    ],
    "remedy": "Ruled (CTO msg 1959) and built (IB-pr-380, IB-pr-381). It disarms when IB-pr-383 is live and cottonwood reads READY before 2026-10-12 (its OVER_AGE date); inflection before 2026-10-13.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-D2-W188-S1",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The IB-pr-380 rule is correct in the refresh Lambda but cannot operate in production from directory/ alone: the artifact states no source snapshot (fail-closed REFRESH_FAILED stays) and the Lambda cannot write the carried TERMINATED entries into the served directory.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W188-S1",
      "directory_runner.py run_firm builds the payload (~line 930): top-level keys are schema, firm_id_opaque, directory_revision, as_of_business_date, source_completion_date, source_revision, census (counts), entries ... none carries the source's client keys; refresh.py SsmBuildDispatcher.__call__ can only read what the artifact holds.",
      "infra/aws/terraform/investor-reporting/directory/schedule.tf: the refresh role has s3:GetObject on the directory prefix and s3:PutObject ONLY on _refresh/* (refresh_manifest_arns, lines ~212-233), so the Lambda cannot rewrite directory.json; the search readers read latest.json -> directory.json.",
      "own round r92 (IB-pr-380 complete), terminal at commit (override scope, CTO msg 2224)"
    ],
    "remedy": "Built in IB-pr-381 (the runner emits source_client_ids and carries removed entries); it disarms on IB-pr-383's live landing.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-D2-W188-S2",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "From a fire dated 2026-10-09 the refresh's previous-state read (last_manifest, limit 10 trading days) no longer sees inflection's last READY build (2026-09-25), so previous_entries is None and the disappearance check, and with it the TERMINATED carry-forward, goes dark.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W188-S2",
      "Read live with the live zip's own refresh.last_manifest (client = s3, AWS reads): inflection at 2026-10-08 -> manifest 2026-09-25 (directory_key .../2026-09-25/directory.json); at 2026-10-09 -> None. Cottonwood (last READY 2026-10-05) and 49financial are unaffected: 2026-10-09 -> found.",
      "inflection _refresh/ holds REFRESH_FAILED manifests for every fire from 2026-09-29 to 2026-10-08 and no READY after 2026-09-25 (the manifest list printed from the live bucket this session).",
      "own round r92 (IB-pr-380 complete), terminal at commit (override scope, CTO msg 2224)"
    ],
    "remedy": "Built in IB-pr-381 (the refresh reads the served directory when no manifest is in the window); it disarms on IB-pr-383's first live inflection fire after 2026-10-08 reading terminated 1, not a false 294 additions.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-D2-W189-S1",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The served directory has already lost the removed entry at both firms (inflection since the 2026-10-06 build, cottonwood since 2026-10-07), so a runner that carries from the served directory restores nothing; terminated_count 1 with the entry served needs one reconciling runner run per firm from the last accounted-completion build.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W189-S1",
      "Live reads (AWS, this session): inflection latest.json names 2026-10-08/directory.json (294 entries), which lacks the dropped client key; the 2026-09-25 build (292 entries, the last accounted-completion build) holds it. Cottonwood latest.json names 2026-10-07/directory.json (269 entries), which lacks it; 2026-10-05 (270 entries) holds it. The runner landed a build on every 09:40 ET fire from 2026-10-06 regardless of the refresh verdict (IB93-1_directory_writers.json).",
      "Replay on the real inputs through the BUILT runner bundle (deliverables/0.9.0_WK_IRPT_BCKEND~189/IB93-1_release_replay.json, runner arms): previous = the served directory -> carried 0 keys at both firms (landed 294 and 269 entries, no marked entry); previous = the last accounted-completion build via --previous-key (inflection 2026-09-25, cottonwood 2026-10-05) -> carried 1 key (1 entry at inflection, 2 entries at cottonwood), landed 295 and 271 entries, the built refresh READY with terminated_count 1.",
      "own round r93 (IB-pr-381 complete), terminal at commit (override scope, CTO msg 2224)"
    ],
    "remedy": "The one-time reconciling runner run per firm from the last accounted-completion build is part of IB-pr-383 (the seeding run); it disarms on that run's served read.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-D2-W189-S4",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The runner lands a build even when a previous client is missing from it while still in the source (a build fault); the refresh can only judge it afterwards, and not at all on the first fire after a gap longer than its 10-trading-day window.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W189-S4",
      "Replay, negative arm (the dropped key put back into the source only): the built runner lands 294 and 269 entries with held_in_source 1 and carries nothing (the ordered 'NOT carried'), i.e. the faulty build is landed to the served directory; the built refresh over it is REFRESH_FAILED at cottonwood and at inflection for a 2026-10-08 fire, but READY with terminated_count 0 for an inflection fire dated 2026-10-09 (its previous state is the served directory, which is the landed artifact itself).",
      "IB93-1_directory_writers.json: the verdict never gates the artifact (the refresh has no PutObject on directory.json or latest.json), so the served directory carries whatever the runner landed. That is why the served inflection 2026-10-08 build lacked the entry while every verdict was REFRESH_FAILED.",
      "own round r93 (IB-pr-381 complete), terminal at commit (override scope, CTO msg 2224)"
    ],
    "remedy": "Ruled yes by the CTO as a cell after this release: the runner refuses a landing with held_in_source > 0.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v95",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v95"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "at": null
    }
  }
]
```
