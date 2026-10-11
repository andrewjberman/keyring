# MDPF_CANON task order -- `CN-c-3` -- THE INFLECTION FEEDER READS THE BRONZE AT THE BUILDER'S ADDRESS (M4, first slice, FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-c-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~9</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the feeder runs in the daily runner's Stage 1 as before.
comp-iam: DECLARED-NOT-APPLICABLE -- the read grant is cell CN-c-2's (the same runner role, the same prefix); this cell changes one script.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r3_checks.py reader 0 of 3 at base (old path literal, no prefix function, the listing names opal-data-mdpf); a reference tree reads 3 of 3 (the arms can pass).
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-c-3` (round 3, decomposition v3)

The reader census (`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md`, section for `mdpf/bronze/`) finds ONE
reader of the Orion model-composition bronze: `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py`. Cell `CN-c-2` moves the
writer to the builder's address (read its order at `org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-c-2.md`, section 1):

```
address("mdpf", "inflection", "bronze", "orion_model_composition", "date=2026-10-09")
  -> s3://opal-data-assets/mdpf/inflection/bronze/orion_model_composition/date=2026-10-09
```

Repoint the reader, and only the bronze read:

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D1, 2026-10-11 ~03:2xZ, row MDPF_CANON-D1-W9-S1, CTO ruling msg 3417 = B):** the daily runner has no `lib/`
(it syncs only `code/scripts/` and `code/config/`), so the feeder cannot import `lib.opal_naming`. It reads the generated file
`data/mdpf/config/bronze_homes.json` that cell `CN-c-2` writes before this order starts (same worktree). If that file is absent, read
`CN-c-2`'s order section 1 step 1 for its shape and stop on a BLOCKING row: it is not this cell's file.

1. Add a module-level function `bronze_partition_prefix(date_iso: str) -> tuple[str, str]` returning `(bucket, key_prefix)` for that
   date, read from `../../config/bronze_homes.json` relative to the script's own directory (on the runner `/opt/mdpf/scripts/gold/`
   resolves it to `/opt/mdpf/config/`; in the repo, to `data/mdpf/config/`): `bucket`, and `key_prefix =
   <feeds.orion_model_composition.key_prefix> + "/" + partition.format(date=date_iso)`. Do NOT import `lib` or `opal_naming`. A missing
   or unreadable file raises; there is no fallback.
2. Replace the typed `MDPF_BRONZE_PREFIX` and its two uses:
   - `resolve_bronze_date` (about lines 190-216) lists the PARENT of the builder's partition prefix (everything up to and excluding
     `date=<...>`) on the builder's bucket with `Delimiter="/"`, and parses partition tokens of the form `date=YYYY-MM-DD` (the old form
     was a bare `YYYY-MM-DD`). Its roll-forward rule (latest on-or-before, staleness in days) is unchanged.
   - `read_orion_bronze` (about lines 219-251), S3 branch, lists `<key_prefix>/` on the builder's bucket and reads each
     `model_<id>.json` from it. The `--bronze-source local` branch is unchanged.
3. Leave `MDPF_BUCKET` and everything that writes the feeder's OUTPUT alone (the feeder's parquet still goes to `opal-data-mdpf`; it is not
   this cell's). Update the module docstring's "Output"/"bronze" lines to name the new home and say the old home is retired.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, not even from a test. Read-only
   `get`/`describe`/`head`/`list` is allowed. No install, no push. REFUSE, do not rescue.
2. Only the file in section 3 changes (plus your deliverables and the surprise channel). Do not edit the writer (`CN-c-2`'s).
3. **Never** add a fallback to the old bronze path, a dual read or a comparator (PRD DEC-14): the reader reads the new home only.
   Where the new home holds no partition on-or-before the date, `read_orion_bronze` raises as it does today.
4. **Every NEW address comes from the builder, through the generated file**; a refusal is a row, never a typed workaround.
5. **CLIENT DATA:** never print a client figure or account id.
6. Keep the file's line endings as you find them (read them first). No non-ASCII. Use the Edit tool.
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~9/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `lib/opal_naming.py`, `data/mdpf/scripts/bronze/pull_orion_model_composition.py` (as `CN-c-2`
leaves it) and the runner `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`. The issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round3/checks/r3_checks.py` is also read-only (never edit it).

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-c-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round3/checks/r3_checks.py" reader; echo "exit=$?"</invocation><expect>ROUND 3 READER: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-c-3" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-3 close (never self-graded): `/seams` on the writer-to-reader seam, grounded on the DEPLOYED artifact
after CloudOps deploys both scripts and one on-demand pull has landed -- MECHANICAL (the feeder reads the files the pull wrote at the
builder's keys), DECLARATIVE (the census and the docstrings match the code), SEMANTIC (the feeder's `model_composition` output for the
as-of is value-equal to the output built from the old home's same date).

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~9/MDPF_CANON.TO-CN-c-3.proof_of_spec.json`, with AC3
UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-3 close". **Flip this order's `<status>` to `complete` in the SAME
commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W9-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at
filing. Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-11 ~03:2xZ, row MDPF_CANON-D1-W9-S1; CTO ruling msg 3417):** step 1 re-cut to read the generated config (B) instead of importing the builder; criteria unchanged, the issuer's `reader` arms amended in step. Gate limb: only GATE (viii) grades a modification, and `<placeholders>` is NONE.

**ISSUER NOTES:** round 3 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round2.md` @71e85b7191 section 3 item 3 (M4 first slice). The
issuer picked this reader from the census's dependency order: it is the only reader of the only bronze writer (census note 3), so the
slice closes a whole surface (writer plus reader) and moves no served output. Runs in slot ~9's queue AFTER `CN-c-2`; one chain. The
`/seams` read is the issuer's at the drain (a worker has no skill tool). Base box/dell1. LF only.

<status>complete</status>
<round>3</round>
<to_id>MDPF_CANON.TO-CN-c-3</to_id>
<slot>~9</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
