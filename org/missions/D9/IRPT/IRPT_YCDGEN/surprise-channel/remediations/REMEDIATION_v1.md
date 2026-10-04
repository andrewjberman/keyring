# IRPT_YCDGEN -- round 1 remediations (the first compile of the project's channel)

<sweep_watermark>2026-10-04T18:45:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-04 ~20:3xZ (DRAFT). Graduated at round 1's L9 (`adjudications/ADJUDICATION_v1.md`, which
dismisses W3-S1, W2-S1 and W2-S2), round label v2 (the round after IRPT_YCDGEN round 1). L8 inputs as named there:
INVESTIGATION_v1.md at CLOUD HEAD (5 rows), the drain `c1d672f636`, the close record and its two ledgers, CTO batches
237 and 239, and this seat's reads at CLOUD HEAD 96f17cdbe9 (read-only AWS; no YCharts call). 2 rows: 1 REMEDIATED and
closed on a served read (S1, BLOCKING, arriving DISARMED: owner 2.0.0_SA_COO~Y, at 2026-10-04T19:22:34Z); 1 OPEN
(W2-S3, owner 2.0.0_SA_COO~Y: the map's 176 table_data and scatter sources, now measured as not answering for a
portfolio as mapped). 0 rows stay ARMED.

```json
[
  {
    "id": "IRPT_YCDGEN-S1",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "opal-data-cottonwood's bucket policy DenyForeignFirmPrincipals denies s3:* to every principal outside role/*-cot-* and four named exceptions, so the research grant applied to the resident's irpt-ycharts-runner-role (CTO batch 237) was inert and close run 1 stopped at its first write (AccessDenied on s3:PutObject); the batch-237 after-read was an identity-only simulation, which cannot see a bucket policy.",
    "evidence": [
      "investigation row IRPT_YCDGEN-S1",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R1-20261004T1842Z_host_run.txt:22-23: AccessDenied on s3:PutObject by assumed-role/irpt-ycharts-runner-role on opal-data-cottonwood/irpt/cottonwood/..., runner rc=1 at 18:42:52Z",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/BEFORE_READ_PRINCIPAL_20261004.txt:6-9: the runner role's PutObject simulated WITH the bucket policy reads explicitDeny",
      "fix 9a01678592 (irpt-cot-ycharts-research-role, assumed by the runner before the lease); CTO RULINGS batch 239 @a44bc85977, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_YCDGEN_COT_RESEARCH_PRINCIPAL_20261004.md on packet blob 97578e0eda",
      "apply b9f350b215; org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/AFTER_READ_PRINCIPAL_20261004.txt (19:22:34Z): WITH the cottonwood bucket policy both research prefixes allowed and ycharts_opal_reports implicitDeny; WITH the 49financial bucket policy explicitDeny; the runner's sts:AssumeRole allowed",
      "close runs 2 and 3 wrote on the principal: org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R1-20261004T1924Z_host_run.txt:8-14 (9abe43df79) and org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R1-20261004T1944Z_host_run.txt:8-14",
      "s3api list-objects-v2 opal-data-cottonwood irpt/cottonwood/state/ycharts_ as user/Andrew_Berman: 12 kept answers (6 per request, YCD-R1-20261004T1924Z and T1944Z) and 2 run.json (36,078 and 36,258 bytes) (this compile's read, 2026-10-04T19:59Z)",
      "ledger irpt-ycdgen-principal-20261004: CLOSED 20261004T195827Z, V1 read back (org/critical_paths/change_management/20261004T1911Z_irpt-ycdgen-principal-20261004_deploy_completion.md, in the shared working tree and uncommitted at this compile's read, 20:15Z); ledger irpt-ycdgen-grant-20261004 CLOSED 20261004T192317Z, V1 SUPERSEDED (b9f350b215)",
      "investigation row IRPT_YCDGEN-S2 (2.0.0_SA_COO~Y, surfaced 19:55Z): the issuer's disarm record, uncommitted at this compile's read and surfaced after this compile's watermark; it is the next compile's"
    ],
    "remedy": "Done: the research writes run on Cottonwood's own principal irpt-cot-ycharts-research-role, which only the runner role may assume, and the bucket fence is untouched; the apply disarmed the hazard, proven at the 19:22:34Z after-read, and the close runs' writes are read back from the store.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-04T19:22:34Z"
    }
  },
  {
    "id": "IRPT_YCDGEN-W2-S3",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Overview element map sources 176 of its 249 elements to /indices/table_data (175) or /charts/scatter_plot_data.json (1), with column or metric ids inferred from the printed labels of a Comparison-report field scrape; live, those calls do not answer for a P:<id> portfolio as mapped: table_data answered 400 or 404 with an empty body, and the scatter call answered 400 'Invalid x axis metric'.",
    "evidence": [
      "investigation row IRPT_YCDGEN-W2-S3 (grounding INFERRED at the cut)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json: 249 elements; sources /indices/table_data 175, BUILDER_ONLY 65, /charts/fund_data.json 6, /securities/securities_info 2, /charts/scatter_plot_data.json 1; every element's claim 'inferred'; 12 calls, 9 of them /indices/table_data (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ)",
      "9abe43df79 (close run 2): 03 scatter_plot_data 400 'Invalid x axis metric: standard_deviation_5y, Invalid y axis metric: annualized_total_return_5y'; 04 table_data 400, empty body; 05 and 06 table_data 404, empty body; 'This measures row W2-S3's inference'",
      "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R1-20261004T1944Z/run.json: steps 1-2 answered 200 (portfolio_info IDENTIFIERS, portfolio_level_series DATA); steps 3-6 answered 400, 400, 404, 404; step 7 stopped WAF_REFRESH_REQUIRED; of 184 elements traced to a call, 8 rest on a 200 answer, 16 on a call that answered 4xx and 160 on calls not reached; 65 NOT_AVAILABLE BUILDER_ONLY (this compile's read, 2026-10-04 ~19:5xZ-20:3xZ, no figure value read)",
      "docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json names printed fields and units, no endpoint or column id (the row's own read @ad781b948a)"
    ],
    "remedy": "Re-source the map's 176 table_data and scatter elements from measured answers: find the call and identifiers YCharts accepts for a P:<id> portfolio (the scatter's metric ids, and which data endpoint serves the table figures), record each element's claim as measured from a kept answer, and mark each element no data endpoint serves as BUILDER_ONLY, rebuilt from data Opal holds or noted as not available (C-BUILDERONLY). Close on: a run whose kept answers carry a 200 DATA answer behind every element the map sources to a call.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v2"
    },
    "closed": false
  }
]
```
