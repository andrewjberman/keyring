# NFRA_SCHWABBF -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~SB` at the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_SCHWABBF-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a
seat's row is `NFRA_SCHWABBF-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `NFRA_SCHWABBF-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "NFRA_SCHWABBF-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~SB",
    "surfaced_at": "2026-10-20T13:45:00Z",
    "one_line": "The monolith's S3 notification invokes the silver converter Lambda for every ObjectCreated under schwab/<master>/bronze/ with suffix .zip, so the server-side copy of the ~21,782 stored Schwab objects to the builder's key form will re-convert every moved day, which the PRD's C-MOVE does not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~SB (release act R1 names the fan-out as blast radius in the never-widen pair; R3 prints the event count; R6's compare is the check that the re-conversion changed nothing)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/opal-assets/silver.tf:242-244 (rules schwab-08242234, schwab-08335338, schwab-08403355: prefix schwab/<m>/bronze/, suffix .zip) and :769-780 (one lambda_function block per rule, events s3:ObjectCreated:*), read at HEAD ed7d0dc3db 2026-10-20",
        "data/assets/scripts/silver/schwab_conversion.py:133-197 (scope_from_key reads segment 1; feed_from_key and date_from_key read the FILE NAME), so a new-form key is accepted and the same silver partitions are rewritten",
        "infra/aws/terraform/opal-assets/monolith.tf:142-147 and :194-227 (versioning Enabled, no noncurrent expiry): a later delete of the old keys writes delete markers and keeps every version"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-MOVE: copy every stored object to its builder key, verify by count and sha, then deploy readers and run FWD-5's equality read; it names no consequence of the copy for the silver tier.",
    "world_is": "The copy is an ObjectCreated event for every object, so about 21,782 silver converter invocations follow it; the converter derives master from path segment 1 and type and date from the file name and so writes the same silver partitions again. Whether those rewrites are byte-identical is unmeasured (the cutover's compare answers it).",
    "notes": "Inlined into TO-BF-m1 (the plan prints the event count) and into the decomposition battery (comp-adversary finding 1). Not an alert and not a monitor: a one-time count at a dry run."
  },
  {
    "id": "NFRA_SCHWABBF-W3-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~3",
    "surfaced_at": "2026-10-20T14:03:37Z",
    "one_line": "On the real dim_balance partition for 0840 on 2026-10-16 all 40 columns are non-numeric, so the equality capture records an empty numeric_sums and the content_sha256 field is the only check on figure values for silver tables read this way.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: live read-only capture (AC2, rc 0, CAPTURED cells=1 missing=0) written to C:/Users/AndrewBerman/AppData/Local/Temp/bf_e1_capture_probe.json at worktree branch wk-NFRA_SCHWABBF-3; cells[0].columns lists 40 names and cells[0].numeric_sums is empty",
        "data/canonical/schwab/silver/_canonical_silver_lib.py:125 at worktree HEAD (read_schwab_raw returns values as string; dtype standardization is the caller's typed step)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BF-e1 / C-EQUAL: capture records numeric_sums{col: float} for the figures of each cell, and compare reports a changed numeric cell as field=numeric_sums.",
    "world_is": "The silver partition s3://opal-data-assets/schwab/08403355/silver/dim_balance/date=2026-10-16/data.parquet holds 30 rows and 40 columns, none numeric-typed on read, so numeric_sums is {}. A figure change in any column still moves content_sha256, so the compare is not blind; the numeric_sums arm is inert for this table.",
    "notes": "Recorded, not worked around: the instrument follows the cell text and does not parse strings into floats. Whether the issuer wants a typed numeric pass for the figure check is the issuer's decision."
  },
  {
    "id": "NFRA_SCHWABBF-W3-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~3",
    "surfaced_at": "2026-10-20T14:03:37Z",
    "one_line": "The equality cell hashes every column of a silver partition, including the provenance columns _source_file, _source_as_of and _master_observed, so a rebuilt day whose figures are unchanged but whose provenance names the moved bronze key would read as a DIFF.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: the captured dim_balance cell at C:/Users/AndrewBerman/AppData/Local/Temp/bf_e1_capture_probe.json lists _source_file, _source_as_of and _master_observed among its 40 columns, and content_sha256 is computed over all of them (data/canonical/schwab/keyform/equal_sample.py _content_sha256 at worktree HEAD)",
        "data/canonical/schwab/silver/build_fact_position.py:15 at worktree HEAD (provenance columns _source_file, source_as_of, schema_version are declared deterministic, idempotency #6)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO BF-e1 / C-EQUAL: content_sha256 is the sha256 of the rows, and compare reports a difference where a figure for an already stored day differs (FWD-5 ACCEPT).",
    "world_is": "content_sha256 covers every column, provenance included, so the compare cannot separate a provenance-only rewrite from a figure change. Whether the rebuilt bytes differ in provenance is unmeasured; the cutover's compare after the move answers it. The instrument follows the spec and excludes no column.",
    "notes": "Recorded for the issuer: whether provenance columns are in scope of the equality check is the issuer's decision, not the worker's."
  }
]
```
