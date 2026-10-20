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
    "id": "NFRA_SCHWABBF-W1-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~1",
    "surfaced_at": "2026-10-20T14:02:05Z",
    "one_line": "The silver converter data/assets/scripts/silver/schwab_conversion.py cannot be loaded by path from its own directory: its bare-name import of stream_parquet fails, so the converter seam probe of TO-BF-k1 (AC2) cannot run against the real neighbor as the order specifies.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/silver/schwab_conversion.py:66 is the bare-name import 'import stream_parquet as sp' at HEAD 5f1ad506a4 (worktree C:/Users/AndrewBerman/Desktop/wt-bf-1)",
        "git ls-files at HEAD 5f1ad506a4: stream_parquet.py is tracked at data/assets/scripts/lib/stream_parquet.py and at infra/aws/lambda/opal-assets/opal-assets-silver-schwab/stream_parquet.py; no copy sits beside data/assets/scripts/silver/schwab_conversion.py",
        "python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no: '1 failed, 242 passed in 3.29s'; the failure is 'ModuleNotFoundError: No module named stream_parquet' raised at data/assets/scripts/silver/schwab_conversion.py:66"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-k1 AC2 and the worker face: import data/assets/scripts/silver/schwab_conversion.py by path and assert that scope_from_key, feed_from_key and date_from_key read a new-form key built by monolith_bronze_key (the seam probe against the REAL neighbor). The order presents the converter's file set as loadable from its source directory.",
    "world_is": "The six key functions and the other 242 test cases pass at HEAD 5f1ad506a4 plus the BF-k-1 edits. Only the seam case fails, because the converter's sibling stream_parquet is not beside the source file; the sibling is tracked in data/assets/scripts/lib/ and packaged beside the Lambda copy. Nothing was patched: the refusal clause forbids a fallback that weakens the probe, and the converter is read-only for this cell.",
    "notes": "Options for the issuer, not taken by the worker: put data/assets/scripts/lib on the probe's sys.path (a test-harness edit inside the BF-k-1 write grant, no assertion weakened), or name the Lambda package directory as the seam neighbor. Not an alert and not a monitor."
  }
]
```
