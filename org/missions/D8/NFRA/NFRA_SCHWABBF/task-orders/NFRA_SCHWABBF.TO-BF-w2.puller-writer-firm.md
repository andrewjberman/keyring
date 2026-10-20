# TO NFRA_SCHWABBF.TO-BF-w2 -- thread hop 2: the daily puller lands the FIRM form; its index and guard filter by master

<to_id>NFRA_SCHWABBF.TO-BF-w2</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~3</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-w-2` (`decompositions/NFRA_SCHWABBF_DECOMP_R2.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-w-2`, PRD contracts C-DAILY and the writer half of C-BACKFILL at v0.5. FWD-6 ACCEPT: "A new day's Schwab files appear where the builder says, with no later fix-up step." Andrew-direct 2026-10-20 ~14:3xZ: "abiding by the path structure that already exists in that bucket ... schwab vendor and 49 firm for the 0840 and cottonwood firm for the various master accounts".
WORLD only because the file sits under `infra/`; nothing is deployed or run against Schwab by this cell.

**What exists (read the whole file first).** `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` at HEAD carries round 1's MASTER-form edit (merged `98290da161`): `Get-BronzeKeyDir`, `Get-LandedIndex`, `Select-PlanAsOf`, the `-OnlyAsOf` parameter, and `$keyDir` using `Get-BronzeKeyDir`, all keyed `schwab/{master}/bronze/{type}/date=YYYY-MM-DD`. Its tests are `data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py` (7 tests, AST-extraction harness).
The target key is now `schwab/{firm}/bronze/{type}/date=YYYY-MM-DD/{vendor name}` with `{firm}` = `49financial` for 08242234, 08335338 and 08403355 (`address('schwab','49financial','bronze','acc','date=2023-10-17')` is `s3://opal-data-assets/schwab/49financial/bronze/acc/date=2023-10-17`). The three masters now SHARE the folder; their files differ only by the vendor name's master prefix.
Round 1's measured effects of sharing (read the code, do not trust this list as complete):
- `$KEYROOT`/`$PREFIX` for the monolith target is `schwab/$Master/bronze`; the pre-loop resumability index (`$landed`, keyed on the file name from `aws s3 ls ... --recursive`) and the post-run listing + `Get-LandedIndex` + `Get-LandingGuardVerdict` run over `$PREFIX`. Over the firm folder those listings contain the OTHER masters' files too: the index and the guard must keep only names that start with `{$Master}.` or the guard reports surplus on a correct run.
- Legacy-only files (round 1 row `NFRA_SCHWABBF-W2-S3`): the index must still count the OLD master-form prefix `schwab/$Master/bronze/` so a not-yet-copied file is skipped, not re-pulled; list both prefixes for the resumability index. The post-run guard reads the NEW prefix only.
- The staging target (`opal-data-schwab`) is a retired escape hatch: leave its grammar exactly as it is.

**Build (edit only `sdd-daily-pull.ps1`; the deployed file stays ONE file).**
1. A literal map of master to firm in the script (the seven masters of PRD C-SCOPE: the three above to `49financial`; 08719286, 08134043, 08165601, 08480305 to `cottonwood`), a function `Get-FirmOf([string]$Master)` that THROWS on an unknown master, and `Get-BronzeKeyDir([string]$Master,[string]$Type,[string]$AsOf8)` returning `schwab/{firm}/bronze/{type}/date=yyyy-MM-dd`. The script's existing `ValidateSet` on `$Master` stays at the three masters (C-ONEWRITER: the 49F box holds those three only).
2. `$keyDir` and the header comments (lines ~7-11, ~39) follow the firm form; the index and the guard filter by master as above; `Get-LandedIndex` keeps its signature but takes the master and the type/date split follows the new key (`{type}/date=YYYY-MM-DD/{file}` after the firm folder).
3. Keep `-OnlyAsOf` and `Select-PlanAsOf` exactly as round 1 (empty = today's behavior; zero kept = exit 9; the denominator subtracts the excluded files).
4. Tests: rewrite `data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py` for the firm form, same AST-extraction harness (extract the functions from the script, do NOT run it, do NOT call Schwab):
   - KEY PARITY (name contains `key_parity`): `Get-BronzeKeyDir` for 7 masters x 17 types (acc rps trn tnn sec uln ult rld rlu rly rtu rty fam slm upn upt trn_nna) x 2 dates (20231017, 20261016) equals `address('schwab', firm, 'bronze', type, 'date=YYYY-MM-DD')` without `s3://opal-data-assets/`, where `firm` is read from `infra/logic/registry/scopes.json` (the row whose `masters` names the master), NOT from the script's own map; and the script's map equals the registry for the seven masters. An unknown master throws.
   - GUARD (name contains `landing_guard`): sample `aws s3 ls` lines from the firm folder holding THREE masters' files for one type and date: for `$Master = 08403355` the index counts only that master's names and the verdict is `ok=True` with zero shortfall, surplus and collisions; a missing own file is a shortfall; a legacy-only own file counts in the resumability index.
   - FILTER (name contains `only_asof`): unchanged from round 1 (5-file, 3-day plan: one day kept, all kept when empty, none matching signals exit 9).

### ACCEPTANCE

<criterion id="BF2-w2-AC1" cell_refs="BF-w-2"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no -k "key_parity or landing_guard"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-w2-AC1` -- the writer's directory for 7 masters x 17 types x 2 dates equals the builder's firm address, and the guard accepts a correct run in a folder shared by three masters.

<criterion id="BF2-w2-AC2" cell_refs="BF-w-2"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no -k only_asof</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF2-w2-AC2` -- the single-day filter still holds after the rewrite.

<expected_criteria>BF2-w2-AC1,BF2-w2-AC2</expected_criteria>

Dry-run at the base 2026-10-20 (round-1 merged tree): AC1 and AC2 PASS against the round-1 MASTER-form test file (`4 passed` and `3 passed`). That is a control, not a build check: the build is graded by the rewritten file. FIRST rewrite the test for the firm form and run AC1: it must FAIL against the master-form script (the key-parity arm); only then change the script.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (`lib/opal_naming.py`, the registry, the other `.ps1` files, the Terraform).
- **WORLD floor, nothing applied.** You do not deploy, upload or run the puller, you do not contact Schwab, and you do not touch AWS. Deployment to the box is the issuer's release act.
- **Fire times (do not change the schedule):** 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z. The session lock, the vendor-master guard (`QUARANTINE (master MISMATCH)`) and the date-disagreement quarantine stay exactly as they are.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1
data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R2.md</decomp_doc> (round 2), cell `BF-w-2`.
<owned_cells>BF-w-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF2-w2-AC1, BF2-w2-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~3/NFRA_SCHWABBF.TO-BF-w2.puller-writer-firm.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF2-w2-AC1,BF2-w2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** every line number you changed and why (the index, guard and prefix first), the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- fire times inlined above; no schedule edit.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; the box role's write grant does NOT yet cover the firm prefix (cell BF-i-2 adds it); this cell changes no IAM; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 2 (index and guard list the whole firm folder) and 5 (W2-S3 legacy-only skip) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-DAILY, C-BACKFILL, C-ONEWRITER; decomposition round 2 cell BF-w-2; round-1 merge `98290da161`.
