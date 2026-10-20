# TO NFRA_SCHWABBF.TO-BF-m2 -- thread hop 3a: the move tool in the FIRM form (plan, copy, verify; no delete)

<to_id>NFRA_SCHWABBF.TO-BF-m2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-m-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-4 | **depends_on:** `TO-BF-k2` (the key contract; earlier in your queue, already on your branch)

---

## WORKER FACE

### THE CELL

`BF-m-2`, PRD contract C-MOVE steps 1-2 at v0.5. Andrew-direct 2026-10-20 ~13:0xZ call 2: one cutover, same-day rollback, no side-by-side period, the old keys deleted only on his confirmation; and ~14:3xZ: the bronze lives under "schwab vendor and 49 firm ... cottonwood firm".
This tool copies every stored Schwab bronze object from its OLD master-form key to its FIRM-form key and verifies it. It does not run the copy for real and it contains NO delete.

**What exists.** A master-form version of this tool is on your branch from round 1's history, for REFERENCE: `git show 293346aff1:data/canonical/schwab/keyform/move_bronze_key_form.py` and its test and fixture at the same commit under `data/canonical/schwab/tests/`. The files in your worktree today ARE that master-form version (round 1 left them in place). Keep the CLI, the output lines, the fixture counts and the structure; change what maps a source to a destination.
- Stored today (measured 2026-10-20): 21,782 objects under `s3://opal-data-assets/schwab/{08242234,08335338,08403355}/bronze/{feed}/{YYYYMMDD}/{vendor name}` (7,960 + 7,758 + 6,064); real example `schwab/08403355/bronze/acc/20261016/08403355.CRS20261016.ACC.zip`.
- The contract is `TO-BF-k2`'s, in `data/canonical/schwab/silver/_canonical_silver_lib.py` (import it by file path; this tool runs from a repo checkout, never inside the bd-tree deployment): `parse_legacy_bronze_key` (source), `bronze_key_for_file` and `firm_of` (destination), `parse_bronze_key`.
- Destination: `schwab/{firm}/bronze/{feed}/date={YYYY-MM-DD}/{vendor name}`; for the three masters the firm is `49financial`. Example: `schwab/49financial/bronze/acc/date=2026-10-16/08403355.CRS20261016.ACC.zip`. Masters share the destination partition; their files differ by the name prefix.
- Every ObjectCreated under an event-ruled prefix with suffix `.zip` invokes the silver converter (`infra/aws/terraform/opal-assets/silver.tf:242-244,769-780`). Once the firm event rule exists (another cell, applied before the copy), a server-side copy re-converts every moved day, so the plan must print that count.

**Build (edit `data/canonical/schwab/keyform/move_bronze_key_form.py`; stdlib + boto3 only for the CLI plumbing; the silver helper's own imports are accepted).**
1. `plan`: unchanged inputs (`--listing-file F`, a JSON list of `{"Key","Size","ETag"}`, or a live read-only listing with `--master M [--type T]`; the DENOMINATOR is the number of keys listed and is printed). A key is in scope only if `parse_legacy_bronze_key` accepts it AND the master is one of 08242234, 08335338, 08403355 (C-SCOPE). A legacy-shaped key under any other master is counted `foreign` and never planned. A key already in the FIRM form is counted `already`.
   The new key is `bronze_key_for_file(master, feed, date_compact, filename)`. Prints exactly: `MOVE-PLAN in_scope=N foreign=F copy=C already=A events=E` then one `MOVE-COUNT master=M type=T n=K` per master and type. `events` = planned copies whose destination key starts with `schwab/49financial/bronze/` or `schwab/cottonwood/bronze/` and ends in `.zip` (the expected converter invocations once the firm rule exists). `--out plan.json` writes `[{"src","dst","size"}...]`. After the `MOVE-PLAN` line it also prints ONE `MOVE-SAMPLE src=<source key> dst=<destination key>` line for the planned copy whose source key sorts first.
   Two planned sources must never map to the same destination: if they would, REFUSE the plan with both keys named (the filename carries the master, so this should be impossible; the guard proves it).
2. `copy --plan plan.json [--apply]`: without `--apply` prints `COPY-DRY n=K` and touches nothing. With `--apply`: server-side `copy_object`, never overwriting a destination that exists with the same size (skip and count), idempotent, bounded concurrency (default 8), prints `COPY-DONE copied=C skipped=S failed=X`.
3. `verify --plan plan.json`: size equal and sha256 of the destination body equal to the source body; prints `VERIFY-OK n=K` or `VERIFY-FAIL n=K bad=B` plus the first 20 bad pairs; exit 1 on any bad.
4. NO DELETE: the module contains no `delete_object`, no `delete_objects`, no `rm`, no `mv`, and no CLI verb for removal.
5. Counts per master and type come from ONE function that `plan` and `verify` both print from.

**Fixture `data/canonical/schwab/tests/fixtures/move_listing.json`** (SYNTHETIC; real key shapes): unchanged from round 1 (13 keys: 08242234, 08335338, 08403355 x feeds `acc` and `rps` x dates 20231017 and 20261016 = 12, plus one legacy-shaped key under the foreign master 08719286). Expected plan: `in_scope=12 foreign=1 copy=12 already=0 events=12`.

**Tests `data/canonical/schwab/tests/test_move_bronze_key_form.py`** (fake S3, no network), rewritten for the firm form: the plan and every destination equals `address('schwab','49financial','bronze',feed,'date=YYYY-MM-DD')` plus the vendor name; idempotence (after a fake copy, re-plan from the new listing gives `copy=0 already=12`); a destination that exists with a different size is reported, not overwritten; verify catches a flipped byte and a size mismatch; a foreign-master key is never planned; two masters' same-type, same-date files land in the SAME partition with different names and neither overwrites the other; the module text contains none of the delete verbs.

### ACCEPTANCE

<criterion id="BF2-m2-AC1" cell_refs="BF-m-2"><invocation>python -m pytest data/canonical/schwab/tests/test_move_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-m2-AC1` -- plan, copy, verify and the absence of any delete path, on the synthetic listing and fake S3, firm form.

<criterion id="BF2-m2-AC2" cell_refs="BF-m-2"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --listing-file data/canonical/schwab/tests/fixtures/move_listing.json --out C:/Users/AndrewBerman/AppData/Local/Temp/bf_m2_plan_probe.json</invocation><expect>^MOVE-SAMPLE src=schwab/08242234/bronze/acc/20231017/08242234\.CRS20231017\.ACC\.zip dst=schwab/49financial/bronze/acc/date=2023-10-17/08242234\.CRS20231017\.ACC\.zip$</expect></criterion>
`BF2-m2-AC2` -- the CLI on the fixture prints the first planned copy with its FIRM-form destination (the plan line itself is graded by AC1's tests; the only write is the scratch file named in the invocation).

<criterion id="BF2-m2-AC3" cell_refs="BF-m-2"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --master 08403355 --type acc</invocation><expect>^MOVE-PLAN in_scope=[0-9]+ foreign=0 copy=[0-9]+ already=[0-9]+ events=[0-9]+</expect></criterion>
`BF2-m2-AC3` -- the seam probe against the REAL neighbor: a live, read-only listing of the real old-form `schwab/08403355/bronze/acc/` prefix plans into the firm form (it wrote 516 keys in round 1). It writes nothing.

<expected_criteria>BF2-m2-AC1,BF2-m2-AC2,BF2-m2-AC3</expected_criteria>

Dry-run at the base: your worktree holds the round-1 MASTER-form tool and test, which pass against the round-1 library; after `TO-BF-z2` and `TO-BF-k2` the library is firm-form, so the old tool's import and its master-form destination assertions fail. Run all three first and record what they print; they must FAIL before you change anything.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS call is the read-only listing in AC3. You never run `copy --apply` against the real bucket. If AC3's listing is refused, stop on AC3, write a surprise row naming the refusal, and do not weaken the criterion.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/move_bronze_key_form.py
data/canonical/schwab/tests/test_move_bronze_key_form.py
data/canonical/schwab/tests/fixtures/move_listing.json
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-m-2`.
<owned_cells>BF-m-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-m2-AC1, BF2-m2-AC2, BF2-m2-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-m2.move-script-firm.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-m2-AC1,BF2-m2-AC2,BF2-m2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the fixture plan line, the real 0840 `acc` listing line with its denominator, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the copy window (outside the fires 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z) is a release act.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; no existing role can run the copy (box role has no GetObject; remap role cannot read the monolith), so it runs from a repo checkout under the caller's identity; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 4 (the event rule order and the per-object converter run) is inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-MOVE, C-SCOPE; decomposition round 2 cell BF-m-2; round-1 reference `293346aff1`.
