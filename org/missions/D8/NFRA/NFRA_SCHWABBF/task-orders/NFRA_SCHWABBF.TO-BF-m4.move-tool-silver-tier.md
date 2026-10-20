# TO NFRA_SCHWABBF.TO-BF-m4 -- the move tool gains the silver tier for 08403355 (copy with rename, sha-verified)

<to_id>NFRA_SCHWABBF.TO-BF-m4</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-m-4` (`decompositions/NFRA_SCHWABBF_DECOMP_R4.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-m-4`, PRD v0.9 C-TIERS and C-MOVE. Andrew-direct ~17:0xZ: "a, yes. this needs to go through the same full bronze/silver process that the other masters go through." For 08403355 the silver moves with the bronze, in the same cutover, and "the silver key carries the master in its file name": `schwab/08403355/silver/{T}/date={D}/data.parquet` becomes `schwab/49financial/silver/{T}/date={D}/08403355.parquet`. The move RENAMES the object (the bytes are unchanged). The tool still has NO delete and you never run `copy --apply` against the real bucket.

**What exists (read first).** `data/canonical/schwab/keyform/move_bronze_key_form.py` (round 3, merged `1fa08c5fb7`): `SCOPE_MASTERS = ("08403355",)`, `plan` / `copy` / `verify`, the refusal `MOVE-REFUSED master=M out of scope (PRD v0.7 C-SCOPE)` (rc 2), `MOVE-PLAN`, `MOVE-SAMPLE`, `MOVE-COUNT`, `MOVE-OTHER` lines, and the plan JSON `[{"src","dst","size"}]`. It imports the bronze key contract from `data/canonical/schwab/silver/_canonical_silver_lib.py`. The builder: `lib/opal_naming.py address()`; `address('schwab','49financial','silver','dim_balance','date=2026-10-16')` is `s3://opal-data-assets/schwab/49financial/silver/dim_balance/date=2026-10-16`.
Live silver of 08403355 (measured): 18 tables under `schwab/08403355/silver/`, one `data.parquet` per date; `meta/` and `_ops/` are separate trees and are NOT this round (the builder refuses those tiers today; round 5).

**Build (edit the tool, its test, and one new fixture).**
1. New flag `--tier bronze|silver` on `plan` (default `bronze`: every behavior and output line exactly as today). `--tier silver` accepts only `--master 08403355` (any other master: the same `MOVE-REFUSED`, rc 2, no S3 call).
2. Silver plan: list `schwab/08403355/silver/` (live, read-only, paginated) or take `--listing-file`. A key qualifies when it is `schwab/08403355/silver/{T}/date={YYYY-MM-DD}/data.parquet`. Its destination is `address('schwab','49financial','silver',T,'date=D')` with the bucket removed, plus `/08403355.parquet` (build it through the builder, never a typed string). Entries carry `"tier": "silver"`. A key under `silver/` that does not qualify is counted `unrecognized` and never planned.
3. Output for `--tier silver`, exactly: `MOVE-PLAN tier=silver in_scope=N foreign=0 copy=C already=A events=0` (`events` is always 0: silver is not an event source), then `MOVE-SAMPLE src=... dst=...` for the first planned source in sorted order, one `MOVE-COUNT tier=silver table=T n=K` per table, and `MOVE-OTHER unrecognized=U`. A destination that already exists is `already` (idempotent re-plan).
4. `copy` and `verify` work on silver entries unchanged in mechanism (server-side copy to the new key; `verify` compares size and sha256 of source and destination bodies, so the rename is proven byte-preserving). Still NO delete verb anywhere.
5. Fixture `data/canonical/schwab/tests/fixtures/move_listing_silver.json` (SYNTHETIC; real shapes): 08403355 silver for tables `dim_balance` and `fact_rps` on dates 2023-10-17 and 2026-10-16 (4 keys), one `meta/` key and one `silver/` key with a wrong shape (2 odd keys), and one key under master 08335338's silver (foreign: never planned). Expected: `MOVE-PLAN tier=silver in_scope=4 foreign=1 copy=4 already=0 events=0` and `unrecognized=1` for the silver-shaped odd key (the `meta/` key is outside the silver prefix and is not counted).
6. Tests (fake S3, no network) in `test_move_bronze_key_form.py`: the default bronze behavior is byte-identical (the 20 existing tests stay green); silver destinations equal `address(...)` plus `/08403355.parquet`; idempotence; verify catches a flipped byte after a rename; other masters refuse; silver entries never count as events; no delete verb in the module text.

### ACCEPTANCE

<criterion id="BF4-m4-AC1" cell_refs="BF-m-4"><invocation>python -m pytest data/canonical/schwab/tests/test_move_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF4-m4-AC1` -- the bronze behavior unchanged (20 passed at the base) and the silver-tier arms.

<criterion id="BF4-m4-AC2" cell_refs="BF-m-4"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --tier silver --listing-file data/canonical/schwab/tests/fixtures/move_listing_silver.json</invocation><expect>^MOVE-PLAN tier=silver in_scope=4 foreign=1 copy=4 already=0 events=0$</expect></criterion>
`BF4-m4-AC2` -- the CLI on the synthetic silver listing.

<criterion id="BF4-m4-AC3" cell_refs="BF-m-4"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --tier silver --master 08403355</invocation><expect>^MOVE-PLAN tier=silver in_scope=[0-9]+ foreign=0 copy=[0-9]+ already=[0-9]+ events=0$</expect></criterion>
`BF4-m4-AC3` -- the seam probe against the REAL neighbor: a live, read-only listing of the real `schwab/08403355/silver/` tree plans into the firm silver form. It writes nothing.

<expected_criteria>BF4-m4-AC1,BF4-m4-AC2,BF4-m4-AC3</expected_criteria>

Dry-run at the base: AC1 `20 passed` (PASS as expected: a control that must stay green); AC2 and AC3 fail (`--tier` and the fixture do not exist) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS call is the read-only listing in AC3. You never run `copy --apply` against the real bucket. If AC3's listing is refused, stop on AC3, write a surprise row naming the refusal, and do not weaken the criterion.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W2-S<k>` and use the next), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/move_bronze_key_form.py
data/canonical/schwab/tests/test_move_bronze_key_form.py
data/canonical/schwab/tests/fixtures/move_listing_silver.json
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R4.md</decomp_doc> (round 4), cell `BF-m-4`.
<owned_cells>BF-m-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF4-m4-AC1, BF4-m4-AC2, BF4-m4-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-m4.move-tool-silver-tier.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF4-m4-AC1,BF4-m4-AC2,BF4-m4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the fixture plan line, the live silver plan line with its denominator and the per-table counts, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the copy window is a release act.
comp-iam: RUN -- decomposition battery scanned silver.tf and monolith-iam.tf (2 Terraform files); no existing role can run the copy, so it runs from a repo checkout under the caller's identity (the CloudOps identity is confirmed at the change entry); BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 4 (the equality read must survive the rename) is served by the sha verification on the rename.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.9 C-TIERS, C-MOVE; decomposition round 4 cell BF-m-4; round-3 merge `1fa08c5fb7`.
