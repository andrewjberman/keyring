# TO NFRA_SCHWABBF.TO-BF-m3 -- the move tool moves 08403355 only

<to_id>NFRA_SCHWABBF.TO-BF-m3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-m-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R3.md`) |
**outcome_ref:** FWD-1, FWD-4 | **depends_on:** `TO-BF-k3` (earlier in your queue, on your branch)

---

## WORKER FACE

### THE CELL

`BF-m-3`, PRD v0.7 C-MOVE: "(1) copy every stored 08403355 object to its builder key (only 0840 moves; 0824 and 0833 stay where they are); (2) verify by count and sha per type". Andrew-direct ~16:3xZ: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
The tool `data/canonical/schwab/keyform/move_bronze_key_form.py` (round 2, merged `ef38445985`) moves 08242234, 08335338 AND 08403355. Narrow it to 08403355. It still has NO delete and still never runs `copy --apply` for real in this order.

**What exists (read first).** `SCOPE_MASTERS` (the in-scope set), `plan_from_listing`, `print_plan`, `copy_entries`, `verify_entries`, `main`; the round-2 test `test_move_bronze_key_form.py` (19 tests) and the fixture `tests/fixtures/move_listing.json` (13 SYNTHETIC keys: 08242234, 08335338, 08403355 x feeds acc and rps x dates 20231017 and 20261016 = 12, plus one legacy-shaped key under 08719286). The key contract is `TO-BF-k3`'s, in `data/canonical/schwab/silver/_canonical_silver_lib.py` (`parse_legacy_bronze_key`, `bronze_key_for_file`, `firm_of`, `is_firm_form`).

**Build.**
1. `SCOPE_MASTERS` is exactly `("08403355",)`. A legacy-shaped key under ANY other master (08242234, 08335338, 08719286, ...) is counted `foreign` and never planned. A key already in the firm form for 08403355 is `already`.
2. `plan --master M` with M not in scope REFUSES: prints `MOVE-REFUSED master=M out of scope (PRD v0.7 C-SCOPE)` and exits 2, listing nothing (no AWS call).
3. Outputs, flags, `copy`, `verify`, the `MOVE-SAMPLE` line and the no-delete property are unchanged. `events` counts planned copies whose destination key starts with `schwab/49financial/bronze/` or `schwab/cottonwood/bronze/` and ends in `.zip`.
4. The fixture `move_listing.json` stays at 13 keys. Expected plan on it now: `MOVE-PLAN in_scope=4 foreign=9 copy=4 already=0 events=4`, and `MOVE-SAMPLE src=schwab/08403355/bronze/acc/20231017/08403355.CRS20231017.ACC.zip dst=schwab/49financial/bronze/acc/date=2023-10-17/08403355.CRS20231017.ACC.zip`.
5. Rework `test_move_bronze_key_form.py` to the new scope: the plan numbers above; every destination equals `address('schwab','49financial','bronze',feed,'date=...')` plus the name; idempotence (`copy=0 already=4` after a fake copy); verify catches a flipped byte and a size mismatch; 0824 and 0833 keys are foreign; the out-of-scope refusal (rc 2, no S3 client created); the module text contains none of the delete verbs.

### ACCEPTANCE

<criterion id="BF3-m3-AC1" cell_refs="BF-m-3"><invocation>python -m pytest data/canonical/schwab/tests/test_move_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-m3-AC1` -- plan, copy, verify, the refusal and the absence of any delete path, on the synthetic listing and fake S3, 0840 only.

<criterion id="BF3-m3-AC2" cell_refs="BF-m-3"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --listing-file data/canonical/schwab/tests/fixtures/move_listing.json</invocation><expect>^MOVE-PLAN in_scope=4 foreign=9 copy=4 already=0 events=4$</expect></criterion>
`BF3-m3-AC2` -- the CLI on the fixture: only 0840's four keys are planned; the other masters are foreign.

<criterion id="BF3-m3-AC3" cell_refs="BF-m-3"><invocation>python data/canonical/schwab/keyform/move_bronze_key_form.py plan --master 08403355</invocation><expect>^MOVE-PLAN in_scope=[0-9]+ foreign=0 copy=[0-9]+ already=[0-9]+ events=[0-9]+$</expect></criterion>
`BF3-m3-AC3` -- the seam probe against the REAL neighbor: a live, read-only listing of the whole real `schwab/08403355/bronze/` prefix (about 6,000 keys; it wrote 6,074 on 2026-10-20 ~16:0xZ) plans into the firm form. It writes nothing.

<expected_criteria>BF3-m3-AC1,BF3-m3-AC2,BF3-m3-AC3</expected_criteria>

Dry-run at the base: AC1 `19 passed` (control against the three-master scope), AC2 prints `in_scope=12 foreign=1` (FAIL against the bar), AC3 passes against the real prefix today (control). Rework the test first; AC1 must FAIL against the three-master tool before you change it.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **LOCAL.** The only AWS call is the read-only listing in AC3. You never run `copy --apply` against the real bucket. If AC3's listing is refused, stop on AC3, write a surprise row naming the refusal, and do not weaken the criterion.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W1-S<k>` and use the next), and do not weaken the test to pass.

<paths>
data/canonical/schwab/keyform/move_bronze_key_form.py
data/canonical/schwab/tests/test_move_bronze_key_form.py
data/canonical/schwab/tests/fixtures/move_listing.json
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R3.md</decomp_doc> (round 3), cell `BF-m-3`.
<owned_cells>BF-m-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-m3-AC1, BF3-m3-AC2, BF3-m3-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-m3.move-tool-0840-only.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF3-m3-AC1,BF3-m3-AC2,BF3-m3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the fixture plan line, the live 0840 plan line with its denominator, the refusal line, the pytest summary line, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the copy window (outside the fires 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z) is a release act.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; no existing role can run the copy, so it runs from a repo checkout under the caller's identity; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 4 (the firm folder is shared with Cottonwood masters; the master filter still applies) is inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.7 C-MOVE, C-SCOPE; Andrew-direct ~16:3xZ via CTO msg 109927; decomposition round 3 cell BF-m-3; round-2 reference `ef38445985`.
