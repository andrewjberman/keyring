# TO IRPT_DASHBD.TO-DB-b-192 -- READ where the four Opal model benchmark returns come from (MDPF's yang-model-portfolio-benchmarks, served as period windows), whether a dated daily model series exists in gold, and what the report's 32 benchmark members can be filled from; read only

<to_id>IRPT_DASHBD.TO-DB-b-192</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~157</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>102</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 7486, 7490 and 7494 ("The four benchmark rows are Opal model returns, produced by yang-model-portfolio-benchmarks and served as JSON in opal-data-portal-v2 json/benchmarks (DATA_CATALOG.yaml:1590, tool mdpf_get_model_benchmarks). It serves period windows 1D to since-inception, current vintage only, no dated series. Round 102 cell, read only: find the gold parquet that producer reads or writes. If a dated daily model series exists, the builder compounds the household's windows (QTD/YTD/12M/since its first day) and the chart from that gold. If not, it maps QTD/YTD/1Y from the served period figures, labeled model-design returns as of data_as_of. Since-inception and the chart stay (c). Keep the baseline's four rows.") | **Rows:** IRPT_DASHBD-D2-W157-S<k> | **Decomp cell:** `DB-b-192` (decomposition section 104) | **outcome_ref:** FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-157` (branch `wk-IRPT_DASHBD-157`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~157/`.

**Why.** The default performance report (contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`) carries 32 benchmark members: the four stems `benchmark_ultra_short_term`, `benchmark_short_term`, `benchmark_intermediate_term`, `benchmark_long_term`, each in the four windows (QTD, YTD, last 12 months, since inception) of both value summaries (`avs.*` and `pvs.*`). The contract sources every one ABSENT today ("Opal holds no benchmark return series"). The CTO has found the producer: the Opal model returns are MDPF's `yang-model-portfolio-benchmarks`, served as JSON under `opal-data-portal-v2` at `json/benchmarks` and read by the tool `mdpf_get_model_benchmarks` (the catalog entry is in `DATA_CATALOG.yaml`, about line 1590: find the file with `comp-find --files 'DATA_CATALOG' --limit 10`). Served: period windows 1D to since-inception, current vintage only, no dated series.

**The cell (`DB-b-192`): a READ. Nothing is changed, deployed or written.**
1. **The producer.** Find `yang-model-portfolio-benchmarks` (a Lambda, script or pipeline: `comp-which "yang model portfolio benchmarks"`, `comp-estate --resource benchmarks`, `comp-pipescript io <script>` once you name it; enumerate before you list S3). Record `producer` {`name` "yang-model-portfolio-benchmarks", `entry_file` (the repo-relative path of its entry script or handler, an EXISTING file), `reads` (a list of `{address, kind}`: every input it reads, for example a gold parquet prefix, a table, an API: name the address as bucket and prefix without date partitions), `writes` (a list of `{address, kind}`: every output, including the served JSON)}.
2. **The served figures.** Read the served JSON's SHAPE by one S3 GET of the current object (the bucket and prefix are in `served`; the key names, the window names and the `data_as_of` field; DO NOT write any figure, name or value into your record or report beyond the window names and key names): record `served` {`tool` "mdpf_get_model_benchmarks", `bucket`, `prefix`, `windows` (the window names the JSON carries), `dated_series` (bool: does it carry any dated daily series), `vintage` (words: current only, or history), `data_as_of_field` (the key that carries the as-of date)}. Record in `benchmarks` one entry per stem: `{member_stem, served_name (the served JSON's key or label for that model benchmark), found_in_served (bool)}`; map the report's four stems to the served names in words (the report's "ultra short term" etc. are the Opal model benchmarks' own terms: say which served row each is).
3. **Is there a dated daily model series in gold?** From the producer's reads and writes and one named-prefix S3 LIST of each gold input (no recursive listing): `dated_daily_model_series` {`exists` (bool), `address` (when it exists), `columns` (the column names, when it exists), `partitions` (the count of `date=` partitions you listed, 0 if none), `evidence` (words: what you read)}. A series of dated daily model RETURNS (or levels) is what counts; a holdings or position table does not.
4. **The plan for the builder.** `mapping_plan` {`choice`, `windows_covered`, `chart_available`, `label_words`}: `choice` is `COMPOUND_FROM_GOLD` if (and only if) a dated daily model series exists (the builder would compound the household's windows and draw the chart from it); `MAP_SERVED_PERIOD_FIGURES` if not (the builder maps the served period figures for the windows the served JSON carries among `qtd`, `ytd`, `last_12_months`; since inception and the chart stay absent; every one of the four stems must be found in the served JSON); `NOT_ESTABLISHED` if you cannot tell (say why in `recommendation`). `windows_covered` is the subset of `qtd`, `ytd`, `last_12_months`, `since_inception` the plan fills; `label_words` is the exact label the report would print (for example "model-design returns as of data_as_of"). `recommendation`: one to three sentences: what the builder cell should do, which gold or served address it reads, and any mismatch you found between the served windows and the report's (for example a calendar quarter against a model quarter).
5. **Record** `BENCHMARK_SOURCE_READ.json` in your folder with exactly: `producer`; `served`; `dated_daily_model_series`; `benchmarks`; `mapping_plan`; `recommendation`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `served_values_changed` false; `pushed` false; `deployed` false. Names, addresses, counts and words only: no benchmark figure, no run of eight or more digits (an address under a key named `address`, `entry_file`, `path`, `file` or `key` is exempt).

<criterion id="DB102-1-AC1" cell_refs="DB-b-192"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r102/p102_round102.py" . DB102-1-AC1</invocation><expect>DB102-1-AC1 PASS</expect></criterion>
`DB102-1-AC1` -- the record names the producer (yang-model-portfolio-benchmarks) with an existing entry file and its reads and writes; names the served tool, bucket, prefix and windows with the as-of field; states whether a dated daily model series exists (partitions above 0 exactly when it does, with an address and columns when it does); holds one entry for each of the four benchmark stems; states a mapping plan consistent with the evidence (COMPOUND_FROM_GOLD only with a dated series; MAP_SERVED_PERIOD_FIGURES only without one, with since-inception and the chart absent and every stem found in the served figures); no write, push or deploy; no vendor call; no run of 8 or more digits. Base: FAIL (no record).

<expected_criteria>DB102-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call (no YCharts call), no secret read.** Reads only: repo files; S3 named-prefix LIST and single-object GET with the box's existing identity. A denial is recorded verbatim, not retried by another route. If the comp-rail hook refuses a raw S3 call, run what it says next, or annotate `# rail-checked: <why>` (audited). Take every bucket from `lib/opal_naming.py address()` or the catalog, never from `data/firm_registry.json`'s bucket field (it is not where gold lives).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Where you cannot establish something, say `NOT_ESTABLISHED` with the reason; never guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W157-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~157/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-192.model-benchmark-source-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 104 (round 102), cell `DB-b-192`.
<owned_cells>DB-b-192</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB102-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~157/IRPT_DASHBD.TO-DB-b-192.model-benchmark-source-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB102-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the producer and its entry file; what it reads and writes; the served windows and the as-of field; whether a dated daily model series exists and where; the plan (choice, windows covered, chart) and the label; any mismatch; row ids. Names, counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read; nothing is changed, deployed or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: repo reads and S3 named-prefix LIST and single GET with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 15 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
