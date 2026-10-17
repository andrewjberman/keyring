# TO SOC2_MSLOGS.TO-R2-d2 -- a memory-bounded (streaming) derive in the door

<to_id>SOC2_MSLOGS.TO-R2-d2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~9</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Risk note:** WORLD only by the gate's path floor; the cell calls nothing live. `staged` until TO-R2-s2 is terminal (the issuer then flips it to `pending` and continues you on it); both orders write `silver_builder.py`.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-d-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-7 | **depends_on:** TO-R2-s2 (same files)

---

## WORKER FACE

### THE CELL

`SM-d-2`. The door's `derive_silver` op reads every bronze object of Eastern day D and of D+1 into one Python list of record dicts, then calls `silver_builder.build(records, only_date=D)`. A busy day does not fit:
round 1 raised the door to its 10240 MB maximum to survive it (Andrew-direct "use the biggest lambad"). This cell makes the derive hold a BOUNDED working set whatever the day's size, so the release can bring the memory down.

READ first: `infra/aws/lambda/globgrph-trino-access/handler.py` (`_derive_silver`, `_list_keys`, the DOOR CONTRACT v3 docstring), `infra/aws/lambda/globgrph-trino-access/silver_builder.py` (`build`, `COLUMNS`, `_utc`, `partition_date`),
the tests beside them, and the check `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py` (the functions `_synth`, `derive_run`, `derive`: this is exactly how your work is measured).

BUILD TO THIS CONTRACT:
- `build(records, only_date=None)` stays exactly as it is, the REFERENCE. The streaming path is new code beside it, for example `build_stream(parts, only_date, tmpdir=None) -> bytes` in `silver_builder.py`, where `parts` is an iterator that yields ONE bronze object's
  list of records at a time (the handler gives it a generator, so only one object is parsed at any moment).
- Output: parquet bytes identical in rows, row order and every column to `build(all_records_in_listing_order, only_date=D)`. The sort key is the record's parsed UTC instant at FULL precision (the same as `build`, whose stored `creation_time` column is truncated to seconds and is NOT the sort key);
  records with an equal instant keep their listing order (listing order = partition D's keys in key order, then partition D+1's, records in file order). Only records whose own Eastern date is D are kept.
- The working set is bounded: a suggested design is one sorted run per bronze object written to a temporary parquet file, then a k-way merge reading each run in small batches and writing the final table with `pyarrow.parquet.ParquetWriter` in row groups. The runs go under
  `tempfile.TemporaryDirectory()` (the function's `/tmp`, 512 MB by default; keep the runs compressed), removed before the function returns even on an error. Any design that passes the check is acceptable.
- `handler._derive_silver(s3, bucket, ev, silver_builder)`: same validation, same answer `{"ok": true, "rows": n}` where `n` is the number of records READ from the two partitions, same single `put_object` of the result to `SILVER_OBJECT % date`, same refusal when there is no builder.
  It must not hold all records at once. `handle(...)`'s signature and every other op are unchanged. `pyarrow` is imported lazily, inside the builder's own functions as today (the handler module imports without it).
- Update the DOOR CONTRACT docstring line for `derive_silver` to say the derive is streaming and bounded. Add tests to `tests/test_silver_builder.py` and `tests/test_handler.py`: byte-equal rows against `build` on a small shuffled set with ties and sub-second instants; a day that straddles midnight into D+1; an empty day; the temp directory removed after an error.

Hard limits: ASCII only; stdlib plus `pyarrow` (the AWS-managed pandas layer provides it in the Lambda); no AWS call, no network.

### ACCEPTANCE

<criterion id="R2-d2-AC1" cell_refs="SM-d-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py derive</invocation><expect>R2-DERIVE-OK</expect></criterion>
`R2-d2-AC1` -- the door's derive writes the same silver as `build()` over the same records, at no more than half of `build()`'s peak memory, with peak memory growing no more than 2.0x for 4x the data, leaving no temporary file behind.

<expected_criteria>R2-d2-AC1</expected_criteria>

Dry-run at the base 2026-10-17 ~06:2xZ: AC1 `R2-DERIVE-REFUSED peak memory is 1.00 of build()'s ...; peak memory grew 3.08x for 4x the data` -- FAIL as expected. The check runs three subprocesses of about 10 seconds each; run it from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL work only; NOTHING is called live.** No AWS call, no network, no Terraform. Never read a stored object. `access.tf` (the memory setting) is the release's, never yours.
- `build.sh` and the prefixes in `handler.py` belong to TO-R2-n2, the next order of this queue: do not change the bronze prefix constants or `build.sh` here.
- **Refusal clause.** If the check cannot be met as written (for example the ratio is unreachable by any design), stop, write the measured figures in your report and a surprise row (id `SOC2_MSLOGS-D1-W9-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken the check.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~9 <0.9.0_WK_SOC2_MSLOGS~9@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/silver_builder.py
infra/aws/lambda/globgrph-trino-access/handler.py
infra/aws/lambda/globgrph-trino-access/tests/test_silver_builder.py
infra/aws/lambda/globgrph-trino-access/tests/test_handler.py
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-d-2`.
<owned_cells>SM-d-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: R2-d2-AC1. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~9/SOC2_MSLOGS.TO-R2-d2.streaming-derive.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-d2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the check line with its ratio and growth figures, the `pytest` summary line (`python -m pytest infra/aws/lambda/globgrph-trino-access/tests -q`), the design in two sentences, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- equality with the reference `build` is the check.
lane: the <paths> block IS the grant.
</preflight>

Source: the CTO's round-1 analysis section 3 item 3 (@843819d1ab); decomposition round 2 cell SM-d-2, ruling 4. The proof on the busiest real day and the memory reduction are the release's (TO-R2-r2).
