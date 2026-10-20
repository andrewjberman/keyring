# TO NFRA_SCHWABBF.TO-BF-w1 -- thread hop 2: the daily puller lands the builder's form, and can pull one named day

<to_id>NFRA_SCHWABBF.TO-BF-w1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-w-1` (`decompositions/NFRA_SCHWABBF_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** none (the PowerShell function is tested against the builder directly)

---

## WORKER FACE

### THE CELL

`BF-w-1`, PRD contracts C-DAILY and the writer half of C-BACKFILL. FWD-6 ACCEPT: "A new day's Schwab files appear where the builder says, with no later fix-up step." FWD-1 needs Schwab's oldest 0840 day pulled through this writer.
WORLD only because the file sits under `infra/`; nothing is deployed or run against Schwab by this cell.

**What exists (read the whole file first).** `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` (569 lines), the scheduled puller. For the monolith target it writes
`s3://opal-data-assets/schwab/{master}/bronze/{type}/{YYYYMMDD}/{vendor name}` (header lines 8-9 and 37; `$KEYROOT` line 55; `$keyDir = "$PREFIX/$($p.type)/$($p.date)"` line 442; `aws s3 cp` line 482).
The partition `date` is the API's `AsOfDATE` formatted `yyyyMMdd` (line 353), never the file name; `TypeFolder` (line 307) derives the lower-case type code. Other places parse the old layout BY POSITION:
- line 372-380: `$landed` index (filename -> present) from `aws s3 ls ... --recursive` (keys on the file name, so it survives a layout change; check it still counts both forms during the copy-to-delete window).
- lines 75-120 `Get-LandingGuardVerdict` and lines 506-526: the post-run guard builds `filename -> "type/yyyyMMdd"` by splitting the listed key's segments 0 and 1 and compares with the plan's `type/date`. With the new layout segment 1 is `date=YYYY-MM-DD`; every occurrence must change together or the guard reports shortfall/collisions on a correct run.
The builder: `lib/opal_naming.py` `address('schwab', master, 'bronze', type, 'date=YYYY-MM-DD')`. The staging target (`opal-data-schwab`) is a retired escape hatch: leave its grammar exactly as it is, and say so in a comment.

**Build (edit only `sdd-daily-pull.ps1`; the deployed file stays ONE file).**
1. A function `Get-BronzeKeyDir([string]$Master,[string]$Type,[string]$AsOf8)` returning `schwab/$Master/bronze/$Type/date=yyyy-MM-dd` (monolith). `$keyDir` uses it. The file name stays the vendor's, unchanged.
2. Update the header comment (lines 7-9, 37), `$KEYROOT` use, the post-run guard's partition token (compare `type/yyyyMMdd` on both sides after converting `date=YYYY-MM-DD` back), and every other place that reads the old layout by position, so a correct run produces `ok=True shortfall=0 surplus=0 collisions=0`.
3. A new optional parameter `[string]$OnlyAsOf = ''` (format `yyyy-MM-dd`). Empty = today's behavior exactly. Non-empty: after the canonical date of each enumerated file is computed (line 344-355), the plan keeps only files whose `date` equals it. If it keeps ZERO, `Die` with exit code 9 and a message saying the served window holds no file for that day (the floor moved, or a non-business day) -- never exit 0. The header documents the backfill use:
   `-Master 08403355 -OnlyAsOf 2023-10-17 -LookbackDays 1200` (one wide search, never chunked; 1200 days reaches before the 2023-10-17 floor from 2026-10).
4. Tests `data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py` (Windows PowerShell 5.1 is on this box; call it with `subprocess`, `-NoProfile`; extract the functions you test from the script by the PowerShell AST, do NOT run the script, do NOT call Schwab):
   - KEY PARITY (name contains `key_parity`): `Get-BronzeKeyDir` for 3 masters x 17 types (acc rps trn tnn sec uln ult rld rlu rly rtu rty fam slm upn upt trn_nna) x 2 dates (20231017, 20261016) equals `address(...)` with `s3://opal-data-assets/` removed.
   - GUARD (name contains `landing_guard`): `Get-LandingGuardVerdict` fed a plan and a new-layout landed index built the way the script builds it from sample `s3 ls` lines returns `ok=True` with zero shortfall, surplus and collisions; and flags a real shortfall.
   - FILTER (name contains `only_asof`): the plan filter keeps exactly the files of that day from a 5-file, 3-day plan; with the parameter empty it keeps all 5; with a day that matches none it signals the exit-9 path.

### ACCEPTANCE

<criterion id="BF1-w1-AC1" cell_refs="BF-w-1"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no -k "key_parity or landing_guard"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF1-w1-AC1` -- the writer's directory for 3 masters x 17 types x 2 dates equals the builder's address, and the post-run guard accepts a correct run on the new layout.

<criterion id="BF1-w1-AC2" cell_refs="BF-w-1"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no -k only_asof</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF1-w1-AC2` -- the single-day filter: one day kept, all days kept when empty, and a day with no file dies with exit 9 instead of exiting 0.

<expected_criteria>BF1-w1-AC1,BF1-w1-AC2</expected_criteria>

Dry-run at the base 2026-10-20: both "file or directory not found" (rc 4) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (`lib/opal_naming.py`, the other `.ps1` files in that directory, the Terraform).
- **WORLD floor, nothing applied.** You do not deploy, upload or run the puller, you do not contact Schwab, and you do not touch AWS. Deployment to the box is the issuer's release act R5 under a change record; the first real run is R8.
- **Fire times (the puller is scheduled; do not change the schedule):** 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z.
- **The session lock, `Acquire-SessionLock`/`Release-SessionLock`, and the vendor-master guard (`QUARANTINE (master MISMATCH)`), and the date-disagreement quarantine, stay exactly as they are.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1
data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP.md</decomp_doc> (round 1), cell `BF-w-1`.
<owned_cells>BF-w-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF1-w1-AC1, BF1-w1-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-w1.puller-writer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF1-w1-AC1,BF1-w1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** every line number in the script you changed and why (the by-position parsers first), the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; fire times inlined above.
comp-iam: RUN -- decomposition battery: the box role writes `schwab/<m>/bronze/*` (monolith-iam.tf:60-81); the new layout sits inside it; this cell changes no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; findings 3 (by-position parsers) and 4 (AsOfDATE not filename; boundary-lossy search) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-DAILY, C-BACKFILL; decomposition round 1 cell BF-w-1.
