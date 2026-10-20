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
    "id": "NFRA_SCHWABBF-W4-S1",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T14:09:00Z",
    "one_line": "The order names exit codes 0, 1 and 2 only; thread_trace.py exits 3 for a store read failure, bad input and an argparse usage error, so rc 2 is only ever the typed NOT-HELD absence.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "not applicable (INERT)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/canonical/schwab/keyform/thread_trace.py main() at a620a5a34c: argparse SystemExit returns RC_ERROR (3); bad --master or --day returns RC_ERROR; any store exception returns RC_ERROR with ERROR: store-read <class>",
        "data/canonical/schwab/keyform/thread_trace.py trace() at a620a5a34c: RC_NOT_HELD (2) only when no bronze in either layout and no silver"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-t1 Build section item 4: exit 0 THREAD-OK, exit 1 THREAD-FAIL, exit 2 NOT-HELD; no code is named for an error or a usage fault.",
    "world_is": "An error path that kept rc 2 would be indistinguishable from the typed absence, so the tool uses rc 3 for errors. The choice is recorded here for the issuer to ratify or change; the tests pin rc 3 for store, day and usage faults."
  },
  {
    "id": "NFRA_SCHWABBF-W4-S2",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T14:09:00Z",
    "one_line": "The row form the worker face names, org/surprise_channel/schemas/investigation_item.schema.json, is in the HEAD tree but not materialised in this sparse worktree, so this row copies the field set of NFRA_SCHWABBF-W4-S1 rather than reading the schema.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "not applicable (INERT)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-tree HEAD org/surprise_channel/schemas/ on branch wk-NFRA_SCHWABBF-4 at 5f1ad506a4: investigation_item.schema.json blob 696468806e9e8163a32b71c65d18d3a98ca318c2 is present",
        "ls org/surprise_channel/schemas/ in worktree wt-bf-4 at 2026-10-20T14:08Z: no such directory; the worktree is a sparse checkout"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face: the investigation row is written per org/surprise_channel/schemas/investigation_item.schema.json, which the worker reads in its worktree.",
    "world_is": "The schema is reachable by git show from HEAD but not by a path read in this worktree; the row shape is unverified against the schema until the surprise-row gate runs at commit."
  },
  {
    "id": "NFRA_SCHWABBF-W4-S3",
    "project": "NFRA_SCHWABBF",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_SCHWABBF~4",
    "surfaced_at": "2026-10-20T14:09:00Z",
    "one_line": "The order names the old-layout partition schwab/M/bronze/acc/YYYYMMDD/ without a bucket; thread_trace.py reads it in the bucket the builder returns for the bronze address, which is opal-data-assets for 08403355.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "not applicable (INERT)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AC2 run at a620a5a34c: HOP bronze line HELD n=1 prefix=s3://opal-data-assets/schwab/08403355/bronze/acc/20261016 form=legacy",
        "read-only aws s3 ls of s3://opal-data-assets/schwab/08403355/bronze/acc/20261016/ at 2026-10-20: one object"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-BF-t1 trace item 2: the second form is the old-layout partition schwab/M/bronze/acc/YYYYMMDD/ for the same day, with no bucket named.",
    "world_is": "Only opal-data-assets was listed. Whether another bucket holds an old-layout copy of the same day is not measured by this order; a copy elsewhere would not be seen by the trace."
  }
]
```
