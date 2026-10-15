# IRPT_ANLREQ round 21, workstream ~G (ENGINE) -- decomposition: build the release-32 resident tarball and its host scripts

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** CTO rulings msgs 8568, 8630, 8647, 8658 (ADDENDUM 3 of `CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md`): `~G2` issues ONE resident release, r32, carrying the merged ENGINE cells (the C-PRICES chain, the per-variant opal maps, the Opal wording, the benchmark and risk-free series, the T-1 price date), `irpt-anlreq-x10-v1` in `additional_policy_revisions`, run 3's producer address `fwd1-staff-r41b@opal.invalid` in place of r41a, and pricing shipped OFF. Order after the build: the r32 never-widen pair, then r33 (the `irpt-ycharts-generate` Lambda leg), then FWD-1 run 3.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **BUILD ONLY.** The cell makes the tarball and the four host scripts locally and writes a record. Upload, install and apply belong to a CloudOps applier under the signed pair; none happens here.
- **The pin is `26d720a980`** (the merge of `AR-g-95`, the last ENGINE source cell). Every file the files-from list takes was last changed by an ANLREQ worker since the r31 pin, so the delta is exactly the ENGINE cells: 14 members changed, 11 added, none removed, 285 identical.
- **The tools are the issuer's, not the worker's.** The driver refuses unless each tool on disk equals the tool at the pin, so the worker cannot edit the build and the check cannot be fitted to it.
- **Two checks, not three.** AC1 is the build verifier (recomputes the delta, the bindings, the producer list, the scripts and the gates from the tarball and git objects, independent of the driver). AC2 is the scope guard (nothing under `infra/`, nothing outside the worker's grant, measured against the merge-base with `box/dell2`).
- **One order is the whole cell.** The tarball, the scripts and the record share one stage folder and one hash chain; splitting them would put two workers on one artifact.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-92` | the r32 resident tarball, its four host scripts and `RESIDENT_R32_BUILD.json`, in a stage folder outside the repo; the record in the worker's folder | the worker's `deliverables` folder, the order, the channel file | WORLD (floor of an infrastructure path; nothing deployed) |
| `AR-g-97` | the APPLY of release 32 to the resident host (leg R): three S3 objects, the pre-read, the signed install, the after-reads and a census, one record, the ledger closed | the applier's `deliverables/irpt_anlreq_r32/` folder and ledger; one host root | WORLD (a host install under a signed never-widen pair) |

## Edges and chains

- ONE chain. `AR-g-92` depends on every ENGINE source cell, merged (the last is `AR-g-95`). It feeds the issuer's pair packet (`make_packet_r32.py`), which refuses unless the verifier passes. `AR-g-97` depends on `AR-g-92` and on both halves of the pair signed (CTO half msg 8693, applier `0.7.0_AE_CloudOps~AQ2`); it is an APPLY order to a Tier-2 applier, not a worker cell, and is issued under `# pipeline-override` as `TO-APPLY-R31L` was.

## Four-postulate record

(i) Domain: the members of the resident package, 310 in r32: 284 identical to r31, 15 changed, 11 added. (ii) One build, one pin, one record. (iii) One intent: a verifiable artifact for the pair to bind. (iv) What this cut does NOT move: any deployed byte, the Lambda leg (r33), the host, the producer list on the host, the DLQ message.

fanout: 1 of 1 chain, cap 8, reason: one build artifact and its record; slot 197.
