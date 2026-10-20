# TO NFRA_SCHWABBF.TO-BF-x5 -- the move tool gains the state tier for 08403355 (cross-bucket copy with rename, sha-verified), and its live re-plan sees the destination

<to_id>NFRA_SCHWABBF.TO-BF-x5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~3</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-x-5` (`decompositions/NFRA_SCHWABBF_DECOMP_R5.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-x-5`, PRD v1.0 C-TIERS and C-MOVE. Andrew-direct ~17:0xZ: "a, yes. this needs to go through the same full bronze/silver process that the other masters go through." For 08403355 the `meta/` and `_ops/` trees move with bronze and silver, as the builder's `state` tier in the FIRM bucket. This tool still has NO delete and you never run `copy --apply` against a real bucket. The move is CROSS-BUCKET: source `s3://opal-data-assets/schwab/08403355/...`, destination `s3://opal-data-49financial/schwab/49financial/state/...`.

**The mapping (fixed in `decompositions/NFRA_SCHWABBF_DECOMP_R5.md`).** Counts measured 2026-10-20 ~17:4xZ: 6,898 objects under `meta/`, 32 under `_ops/`. Real shapes: `meta/complete/date=2023-10-03.json`, `meta/conversions/20261009T104537Z-3b71d000.json`, `meta/pulls/20261009T104527Z.json`, `meta/backfill-status.json`, `_ops/daily_pull/last_run.json`, `_ops/daily_pull/runs/20261009T104527Z.json`.
| source key under `schwab/08403355/` | destination (bucket `opal-data-49financial`) |
|---|---|
| `meta/complete/date=D.json` | `schwab/49financial/state/complete/date=D/08403355.complete.json` |
| `meta/conversions/{run_id}.json` | `schwab/49financial/state/conversions/date={YYYY-MM-DD of the run id's first 8 digits}/08403355.{run_id}.json` |
| `meta/pulls/{RUNID}.json` | `schwab/49financial/state/pulls/date={date of RUNID}/08403355.{RUNID}.json` |
| `_ops/daily_pull/runs/{RUNID}.json` | `schwab/49financial/state/daily_pull/date={date of RUNID}/08403355.{RUNID}.json` |
| `_ops/daily_pull/last_run.json` (rolling) | `schwab/49financial/state/daily_pull/date={UTC date of the source object's LastModified}/08403355.last_run.json` |
| `meta/backfill-status.json` (rolling) | `schwab/49financial/state/backfill_status/date={UTC date of the source object's LastModified}/08403355.backfill-status.json` |
Build every destination prefix with `lib/opal_naming.address('schwab','49financial','state',<table>,'date=D')` (never a typed string), and take the BUCKET from the address it returns. The bytes are not changed; the object is renamed and, for the six shapes above, re-dated.

**What exists (read first).** `data/canonical/schwab/keyform/move_bronze_key_form.py` (round 4 merged `f6078a5d99`): `--tier bronze|silver`, `plan` / `copy` / `verify`, the refusals, `MOVE-PLAN` / `MOVE-SAMPLE` / `MOVE-COUNT` / `MOVE-OTHER` lines, plan JSON `[{"src","dst","size","tier"}]`, and the same-bucket `copy_object`. The silver listing also lists the destination so a re-plan reports `already` (row W2-S8); the BRONZE live listing does not.

**Build (edit the tool, its test, and one new fixture).**
1. `--tier state` (accepts only `--master 08403355`; any other master: the same `MOVE-REFUSED`, rc 2, no S3 call). The plan lists `schwab/08403355/meta/` and `schwab/08403355/_ops/` in `opal-data-assets` (read-only, paginated) or takes `--listing-file`; each key matching one of the six shapes is planned to its destination; others are `unrecognized`. Plan entries carry `"tier": "state"`, `"src_bucket"`, `"dst_bucket"`. Output, exactly: `MOVE-PLAN tier=state in_scope=N foreign=0 copy=C already=A events=0`, `MOVE-SAMPLE src=... dst=...` (first source in sorted order), one `MOVE-COUNT tier=state table=T n=K` per state table, `MOVE-OTHER unrecognized=U`. The live plan also lists the destination prefix in the firm bucket (read-only) so a re-plan reports `already`.
2. `copy` and `verify` honor `src_bucket` and `dst_bucket` per entry (existing entries without them mean `opal-data-assets` for both). `verify` compares size and sha256 of source and destination bodies. NO delete verb anywhere.
3. The BRONZE live listing (`--master M [--type T]` without `--listing-file`) also lists the destination firm prefix `schwab/49financial/bronze/{feed}/` (read-only) so a live bronze re-plan reports `already` (round-3 gap, row W2-S8's twin). Default behavior and output of every existing flag are otherwise unchanged.
4. Fixture `data/canonical/schwab/tests/fixtures/move_listing_state.json` (SYNTHETIC; real shapes): one object of each of the six shapes (6 keys; for the two rolling ones include a `LastModified`), plus one odd `meta/` key and one key under 08335338's `meta/` (foreign). Expected: `MOVE-PLAN tier=state in_scope=6 foreign=1 copy=6 already=0 events=0` and `MOVE-OTHER unrecognized=1`.
5. Tests (fake S3 with TWO buckets, no network) in `test_move_bronze_key_form.py`: every destination equals `address(...)` plus the name and the bucket the builder returns; the rolling date comes from `LastModified`; idempotence (`already`); verify catches a flipped byte across buckets; the other tiers' behavior stays identical (the 31 existing tests stay green); other masters refuse; no delete verb in the module text.

### ACCEPTANCE

<criterion id="BF5-x5-AC1" cell_refs="BF-x-5"><invocation>python -m pytest data/canonical/schwab/tests/test_move_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-x5-AC1` -- the bronze and silver behavior unchanged (31 passed at the base) and the state-tier and destination-listing arms.

<criterion id="BF5-x5-AC2" cell_refs="BF-x-5"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --tier state --listing-file data/canonical/schwab/tests/fixtures/move_listing_state.json</invocation><expect>^MOVE-PLAN tier=state in_scope=6 foreign=1 copy=6 already=0 events=0$</expect></criterion>
`BF5-x5-AC2` -- the CLI on the synthetic state listing.

<criterion id="BF5-x5-AC3" cell_refs="BF-x-5"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --tier state --master 08403355</invocation><expect>^MOVE-PLAN tier=state in_scope=[0-9]+ foreign=0 copy=[0-9]+ already=[0-9]+ events=0$</expect></criterion>
`BF5-x5-AC3` -- the seam probe against the REAL neighbor: a live, read-only listing of the real `schwab/08403355/meta/` and `_ops/` trees (about 6,930 objects) plans into the firm bucket's state tier, with a read-only listing of the destination. It writes nothing.

<expected_criteria>BF5-x5-AC1,BF5-x5-AC2,BF5-x5-AC3</expected_criteria>

Dry-run at the base: AC1 `31 passed` (PASS as expected: a control that must stay green); AC2 and AC3 fail (`--tier state` and the fixture do not exist) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS calls are the read-only listings in AC3 (the source tree in `opal-data-assets` and the destination prefix in `opal-data-49financial`). You never run `copy --apply` against a real bucket. If the destination listing is refused (no read on the firm bucket for your identity), report `already` as UNKNOWN in the output line (`already=-1`), say so in your report and file a surprise row, but do not weaken the criterion beyond that: AC3's bar accepts `already=[0-9]+` only, so if it is refused, stop on AC3, file the row, and do not flip the order.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W3-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]` and keep the file's own line endings; verify `git diff --numstat` shows only added lines). Do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/move_bronze_key_form.py
data/canonical/schwab/tests/test_move_bronze_key_form.py
data/canonical/schwab/tests/fixtures/move_listing_state.json
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R5.md</decomp_doc> (round 5), cell `BF-x-5`.
<owned_cells>BF-x-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF5-x5-AC1, BF5-x5-AC2, BF5-x5-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~3/NFRA_SCHWABBF.TO-BF-x5.move-tool-state-tier.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF5-x5-AC1,BF5-x5-AC2,BF5-x5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the fixture plan line, the live state plan line with its denominator and per-table counts, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the copy window is a release act.
comp-iam: RUN -- decomposition battery scanned silver.tf and monolith-iam.tf (2 Terraform files); no existing role can run the cross-bucket copy, so it runs from a repo checkout under the caller's identity (confirmed at the change entry); the firm bucket's policy was NOT read; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 3 (rolling objects take a date) is the LastModified rule above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-TIERS, C-MOVE; decomposition round 5 cell BF-x-5; round-4 merge `f6078a5d99`.
