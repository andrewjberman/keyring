# TO NFRA_SCHWABBF.TO-BF-m1 -- thread hop 3a: the move script and its dry run (plan, copy, verify; no delete)

<to_id>NFRA_SCHWABBF.TO-BF-m1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-m-1` (`decompositions/NFRA_SCHWABBF_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-4 | **depends_on:** `TO-BF-k1` (the key contract; it is the previous order in your queue and is merged into your worktree before this one starts)

---

## WORKER FACE

### THE CELL

`BF-m-1`, PRD contract C-MOVE steps 1-2. Andrew-direct 2026-10-20 ~13:0xZ call 2: "Yes, rec is accurate" -- one cutover, same-day rollback, no side-by-side copy, the old keys deleted only on his confirmation.
This cell builds the TOOL that copies every stored Schwab bronze object from the old key to the builder's key and verifies it. It does not run the copy and it contains NO delete.

**What exists (read, never edit).** Stored today (measured in the brief, 2026-10-20): 21,782 objects under `s3://opal-data-assets/schwab/{08242234,08335338,08403355}/bronze/{feed}/{YYYYMMDD}/{vendor name}`
(7,960 + 7,758 + 6,064). Example: `schwab/08403355/bronze/acc/20261016/08403355.CRS20261016.ACC.zip`. Your key contract is `TO-BF-k1`'s: `parse_legacy_bronze_key`, `bronze_key_for_file`, `parse_bronze_key`
in `data/canonical/schwab/silver/_canonical_silver_lib.py` (import it by file path; this tool runs from a repo checkout, never inside the bd-tree deployment).
The builder is `lib/opal_naming.py` `address()`.

**Why this tool must report a number most movers do not.** Every ObjectCreated under `schwab/<m>/bronze/` with suffix `.zip` invokes the silver converter Lambda (`infra/aws/terraform/opal-assets/silver.tf:242-244,769-780`).
A server-side copy is an ObjectCreated. So the copy re-converts every moved day. The plan must print that count, and the change record will name it as blast radius.

**Build `data/canonical/schwab/keyform/move_bronze_key_form.py`** (stdlib + boto3 only; create `data/canonical/schwab/keyform/__init__.py`, empty):
1. `plan`: input is `--listing-file F` (a JSON list of `{"Key","Size","ETag"}` objects, i.e. the `Contents` of ListObjectsV2) or a live read-only listing with `--master M [--type T]` (paginated; count client-side;
   the DENOMINATOR is the number of keys listed and is printed). For each key: in scope only if `parse_legacy_bronze_key` accepts it AND the master is one of 08242234, 08335338, 08403355 (C-SCOPE; Andrew: the other 210 masters are out).
   A legacy-shaped key under any other master is counted as `foreign` and never planned. A key already in the new form is counted as `already` (its old twin is not re-planned). The new key is `bronze_key_for_file(master, feed, date_compact, filename)`.
   Prints: `MOVE-PLAN in_scope=N foreign=F copy=C already=A events=E` then one `MOVE-COUNT master=M type=T n=K` per master and type, where `events` is the number of planned copies whose new key starts with `schwab/<m>/bronze/` and ends in `.zip`
   (the expected converter invocations). `--out plan.json` writes `[{"src","dst","size"}...]`.
2. `copy --plan plan.json [--apply]`: without `--apply` prints `COPY-DRY n=K` and touches nothing. With `--apply`: server-side `copy_object` src -> dst in the same bucket, never overwriting a destination that already exists with the same size
   (skip and count it), idempotent on re-run, bounded concurrency (default 8), prints `COPY-DONE copied=C skipped=S failed=X`. The copy preserves the source bytes; it sets no metadata that changes them.
3. `verify --plan plan.json`: for every entry, size equal and sha256 of the destination body equal to the source body (stream both); prints `VERIFY-OK n=K` or `VERIFY-FAIL n=K bad=B` plus the first 20 bad pairs; exit 1 on any bad.
4. NO DELETE: the module contains no `delete_object`, no `delete_objects`, no `rm`, no `mv`, and no CLI verb for removal. The old-key delete is Andrew's confirmed act (R7) and is run outside this tool.
5. Counts per master and type go through ONE function that both `plan` and `verify` print from, so the two agree by construction.

**Fixture `data/canonical/schwab/tests/fixtures/move_listing.json`** (SYNTHETIC: invented sizes and ETags; real key shapes): exactly 13 keys: for each of 08242234, 08335338, 08403355 the feeds `acc` and `rps` on dates 20231017 and 20261016 (12 keys, file names `{master}.CRS{date}.{FEED}.zip`),
plus one legacy-shaped key under the foreign master 08719286. Expected plan: `in_scope=12 foreign=1 copy=12 already=0 events=12`.

**Tests `data/canonical/schwab/tests/test_move_bronze_key_form.py`** (fake S3, no network): the plan above; idempotence (apply a fake copy, re-plan from the new listing: `copy=0 already=12`); a destination that exists with a different size is reported and not overwritten;
verify catches a flipped byte and a size mismatch; a key under a foreign master is never planned; the module text contains none of the delete verbs listed in item 4.

### ACCEPTANCE

<criterion id="BF1-m1-AC1" cell_refs="BF-m-1"><invocation>python -m pytest data/canonical/schwab/tests/test_move_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF1-m1-AC1` -- plan, copy, verify and the absence of any delete path, on the synthetic listing and fake S3.

<criterion id="BF1-m1-AC2" cell_refs="BF-m-1"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --listing-file data/canonical/schwab/tests/fixtures/move_listing.json</invocation><expect>MOVE-PLAN in_scope=12 foreign=1 copy=12 already=0 events=12</expect></criterion>
`BF1-m1-AC2` -- the CLI itself on the fixture: the exact plan line.

<criterion id="BF1-m1-AC3" cell_refs="BF-m-1"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --master 08403355 --type acc</invocation><expect>^MOVE-PLAN in_scope=[0-9]+ foreign=0 copy=[0-9]+ already=[0-9]+ events=[0-9]+</expect></criterion>
`BF1-m1-AC3` -- the seam probe against the REAL neighbor: a live, read-only listing of the real `schwab/08403355/bronze/acc/` prefix parses as old-form keys (the real prefix holds partitions such as `20261016/`). It writes nothing.

<expected_criteria>BF1-m1-AC1,BF1-m1-AC2,BF1-m1-AC3</expected_criteria>

Dry-run at the base 2026-10-20: AC1 "file or directory not found", AC2 and AC3 "can't open file" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS call you make is the read-only listing in AC3. You never run `copy --apply` against the real bucket: the copy is the issuer's release act R4 under a change record and a never-widen pair.
  If AC3's listing is refused (no read identity in your shell), stop on AC3, write a surprise row naming the refusal, and do not weaken the criterion.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/move_bronze_key_form.py
data/canonical/schwab/keyform/__init__.py
data/canonical/schwab/tests/test_move_bronze_key_form.py
data/canonical/schwab/tests/fixtures/move_listing.json
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP.md</decomp_doc> (round 1), cell `BF-m-1`.
<owned_cells>BF-m-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF1-m1-AC1, BF1-m1-AC2, BF1-m1-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-m1.move-script.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF1-m1-AC1,BF1-m1-AC2,BF1-m1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three plan lines (fixture, and the real 0840 acc listing with its denominator), the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the pull-fire times that bound the real copy window are in the decomposition's R4.
comp-iam: RUN -- decomposition battery: no existing role can run the copy (the box role has no GetObject and no DeleteObject on bronze; the C3(a) remap role cannot read the monolith). The tool runs from a repo checkout under the caller's identity; the CloudOps identity's rights are confirmed at R1.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; finding 1 (the copy fires the silver converter per object) and finding 2 (versioning is on) are inlined in the face above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-MOVE, C-SCOPE; decomposition round 1 cell BF-m-1.
