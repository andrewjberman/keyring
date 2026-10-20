# TO NFRA_SCHWABBF.TO-BF-w3 -- the daily puller on the PER-MASTER rule: firm form for 0840 only, 0824 and 0833 byte-for-byte today's behavior

<to_id>NFRA_SCHWABBF.TO-BF-w3</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~3</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-w-3` (`decompositions/NFRA_SCHWABBF_DECOMP_R3.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-w-3`, PRD v0.7 C-DAILY and C-KEYFORM. v0.7: "the key function holds the set of firm-form masters (08403355 and the four Cottonwood masters) and returns today's key, byte-for-byte, for any other master, so 0824 and 0833 are written and read exactly as before"; C-SCOPE: 0824 and 0833 "keep their daily pull and their current keys byte-for-byte". Andrew-direct ~16:3xZ: "I dont care about that 0824, I want the new Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
WORLD only because the file sits under `infra/`; nothing is deployed or run against Schwab by this cell.

**What exists (read the whole file first).** `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` is ONE script that serves three masters (`ValidateSet('08242234','08335338','08403355')`), scheduled per master. Round 2 (merged `8360d83c35`) made it write the FIRM form for ALL THREE: `Get-FirmOf` (a seven-master map), `Get-BronzeKeyDir`, `$KEYROOT` as the firm folder, `$LEGACYROOT` as the master folder, `Get-ResumeNames` (resumability index over both prefixes, filtered by master), `Get-LandedIndex $Master` (post-run listing of the firm folder, filtered by master), plus `Select-PlanAsOf` and the `-OnlyAsOf` parameter. That would move 0824's and 0833's daily files to a folder nobody reads, and break their own resumability (every day re-pulled). It is wrong now.
The pre-round script is `git show 5f1ad506a4:infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`; the master-form behavior to preserve for 0824 and 0833 is its `$keyDir = "$PREFIX/$($p.type)/$($p.date)"` with `$PREFIX = schwab/$Master/bronze`, its `$landed` index (own prefix only), and its post-run guard index of `type/yyyyMMdd` from segments 0 and 1 of the key under `$PREFIX`.

**Build (edit only `sdd-daily-pull.ps1`; the deployed file stays ONE file).**
1. The firm-form set in the script: `08403355` -> `49financial` (and the four Cottonwood masters 08719286, 08134043, 08165601, 08480305 -> `cottonwood`, for the map's completeness; the `ValidateSet` stays at the three 49F masters). `Get-FirmOf` THROWS for a master outside the set. A function `Test-FirmForm([string]$Master)`.
2. `Get-BronzeKeyDir`: firm-form master -> `schwab/{firm}/bronze/{type}/date=yyyy-MM-dd`; any other master -> `schwab/$Master/bronze/{type}/{yyyyMMdd}` (today's).
3. Make `$KEYROOT`, the resumability index and the post-run guard conditional on `Test-FirmForm $Master`: for 0840 exactly the round-2 behavior (firm folder, filter by master prefix, resumability over both prefixes, guard reads the firm prefix only); for 0824 and 0833 the PRE-ROUND behavior (own old prefix only, the pre-round index and guard split). A test must prove the 0824/0833 path equals the pre-round script's.
4. Keep `-OnlyAsOf`, `Select-PlanAsOf`, the session lock, the vendor-master guard, the date-disagreement quarantine, the staging target and the schedule exactly as they are. Fire times (do not change): 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z.
5. Tests (rework `data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py`, same AST-extraction harness: extract the functions from the script, do NOT run it, do NOT call Schwab):
   - KEY PARITY (name contains `key_parity`): firm-form masters (5) x 17 types (acc rps trn tnn sec uln ult rld rlu rly rtu rty fam slm upn upt trn_nna) x 2 dates (20231017, 20261016): `Get-BronzeKeyDir` equals `address('schwab', firm, 'bronze', type, 'date=YYYY-MM-DD')` without `s3://opal-data-assets/`, `firm` read from `infra/logic/registry/scopes.json`; AND for 08242234 and 08335338 x 17 x 2: equals `schwab/{master}/bronze/{type}/{yyyyMMdd}` (today's), proven against the pre-round script's `$keyDir` expression read from `git show 5f1ad506a4:<path>`.
   - GUARD (name contains `landing_guard`): 0840 in a firm folder holding THREE masters' files -> `ok=True`, only its names counted; a missing own file is a shortfall; a legacy-only own file counts in the resumability index. For 0833 with old-form `aws s3 ls` lines (`type/yyyyMMdd/file`): the verdict equals what the pre-round guard code gives on the same lines.
   - FILTER (name contains `only_asof`): unchanged (5-file, 3-day plan; empty keeps all; none matching signals exit 9).

### ACCEPTANCE

<criterion id="BF3-w3-AC1" cell_refs="BF-w-3"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no -k "key_parity or landing_guard"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-w3-AC1` -- the writer's directory per master (firm for the five, today's for 0824 and 0833) and the guard in both shapes.

<criterion id="BF3-w3-AC2" cell_refs="BF-w-3"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no -k only_asof</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF3-w3-AC2` -- the single-day filter still holds after the rework.

<expected_criteria>BF3-w3-AC1,BF3-w3-AC2</expected_criteria>

Dry-run at the base: the round-2 tests (`9 passed` in the file) are a control for the three-master firm behavior. FIRST rewrite the test for the per-master rule and run AC1: the 0824/0833 arms must FAIL against the all-firm script; only then change the script.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** You do not deploy, upload or run the puller, you do not contact Schwab, and you do not touch AWS. Deployment to the box is the issuer's release act.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W3-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` for the highest `W3-S<k>` and use the next), and do not weaken the test to pass.

<paths>
infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1
data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R3.md</decomp_doc> (round 3), cell `BF-w-3`.
<owned_cells>BF-w-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF3-w3-AC1, BF3-w3-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~3/NFRA_SCHWABBF.TO-BF-w3.puller-per-master.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF3-w3-AC1,BF3-w3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** every line number you changed and why, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- fire times inlined above; no schedule edit.
comp-iam: RUN -- decomposition battery scanned 2 Terraform files (monolith-iam.tf, iam.tf) and 3 enumerated masters; the box role's write grant for the firm prefix is cell BF-i-3; this cell changes no IAM; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition finding 3 (one script serves three masters; 0824/0833 byte-for-byte) is inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.7 C-DAILY, C-KEYFORM, C-SCOPE; decomposition round 3 cell BF-w-3; round-2 merge `8360d83c35`.
