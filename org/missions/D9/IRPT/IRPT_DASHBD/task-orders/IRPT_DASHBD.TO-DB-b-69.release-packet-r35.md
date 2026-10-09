# TO IRPT_DASHBD.TO-DB-b-69 -- the activity-and-lot release's never-widen packet re-cut at HEAD, carrying the S32 read (classify_and_sum on pandas 2.2.3 vs the tested version, the returns table under the old and new pin, DB-b-43 on 2.2.3) and the S33 refusal count from one full kit run

<to_id>IRPT_DASHBD.TO-DB-b-69</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~46</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>35</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-34 ADDENDUM 3 @fde009aab3 (msg on ADJUDICATION_v19), enrichment item the release ask | **Decomp cell:** `DB-b-69` (decomposition section 37) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-67 (merged @2bc194b282) and the kit (relay @7aea38af1e).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-46`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/`.

**The cell (`DB-b-69`).** The activity-and-lot release (the extended reporting-gold handler: returns plus the class table plus the three
lots tables) has been withheld since round 26 on rows S31, S32 and S33. Its round-26 packet is
`deliverables/0.9.0_WK_IRPT_DASHBD~23/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE.md`, pinned at `efeb21df71`. The issuer measured that 6 of its 19
file-list rows no longer match HEAD: `handler.py`, `account_activity_lots.py`, `lib/opal_naming.py`, `infra/logic/registry/systems.json`,
`exemptions.json` and `reporting_policies.json`. The CTO ruled S31 and S33 MET on the pandas 2.2.3 kit (round 34 DB-b-67: 7,604 accounts,
447 s, lots peak 1,500.7 of 2,048 MB). S33 holds only if the packet prints the run's refusal count as 0. S32 is MET only on one read the
packet carries.

**The kit:** the path is in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/relay/KIT_PATH_PY312_PANDAS223.txt` (sha256
c76af678143a5f92c4a9638a8ac25e47d2f2c294a014cd3a457af96c55ff17bf). It holds 7 cp312 wheels plus a pin file. It carries no boto3 or psutil:
round 34 side-loaded those from dell2's own site-packages through a `.pth` file, offline (row W44-S1). Do the same. Build the venv in
`.scratch/` with dell2's Python 3.12 (`C:/Users/Test/AppData/Local/Programs/Python/Python312/python.exe`) and
`pip install --no-index --find-links <kit> -r <pin file>`. The "tested version" is dell2's default Python (pandas 3.0.6).

1. **The S32 read** (`S32_READ_E1.json`):
   - **`classify_and_sum` on a named fixture:** at least one trading day's custodian transaction partition and every population account,
     read from S3. Run it under the kit (2.2.3) and under the tested version, and compare the outputs. Record `equal`, and `differences`
     naming each by account, column and the two values (numbers only).
   - **The returns table** for one day, built by `account_return_daily.py` at the OLD pin (`git show bc50d5711e:<path>`, the deployed one)
     and at HEAD, both on the kit. Record `sha256_old_pin`, `sha256_head` and `identical`.
   - **DB-b-43's test** `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py` on the kit: record `passed` and
     `failed`.
   - `runtime_kit` and `runtime_tested`, each printed from its own process.
2. **One full kit run** (`full_run`): the extended handler `--local` over its population for 2026-10-06 at the default batch, using round
   30's runner `deliverables/0.9.0_WK_IRPT_DASHBD~31/lots_750_run.py`. Count `refusals` as the REFUSED, LOTS_SKIPPED and CLASS_SKIPPED lines
   in its log. Record `population_count`, `accounts_run`, `lots_stage_completed`, `lots_peak_mb` and `s33_holds` (refusals == 0).
3. **Re-cut the packet** as `NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R35.md` in your folder.
   - Keep the round-26 packet's structure and its reasoning where it still holds: the blast radius, the expected plan, the writers of the
     property counted, the rollback per key, BRANCH A, BRANCH B and the after-reads.
   - Re-derive every value that changed: the file-list table with each member's sha256 at YOUR commit (one row per member,
     `| `<repo_path>` | ... | `<sha256>` |`); the pins; what the six changed files change in behaviour (read their diffs since
     `efeb21df71`); and whether any new behaviour widens the blast radius. A wider radius is stated, never hidden.
   - Print beside S31, S32 and S33 the measured values from steps 1 and 2, including the line `refusals: <n>`.
   - Leave both halves UNSIGNED. The COO and the CTO sign them.

<criterion id="DB35-1-AC1" cell_refs="DB-b-69"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r35/p35_round35.py" . DB35-1-AC1</invocation><expect>DB35-1-AC1 PASS</expect></criterion>
`DB35-1-AC1` -- the S32 read: classify_and_sum equal or differences named, the returns table under the old and new pin compared by sha256, DB-b-43's test bodies passing on the kit in the SERVED mode (`future.infer_string` at pandas 2.2.3's default) with the forced pandas-3-mode result recorded beside it, both runtimes printed. Base: FAIL.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-09 ~03:1xZ, on row W46-S1).** DB-b-43's test forces `future.infer_string` ON (its own name: `..._under_pandas_3_string_inference`), a pandas-3 mode that is experimental on 2.2.3, where `str.contains` raises. The served runtime never enters it: `account_activity_lots.set_served_runtime()` forces it off and the returns path never sets it (verified in the source at HEAD). The CTO's S32 is `classify_and_sum` equality, which this cell measured equal (0 differences, 3 days, 7,604 accounts). So `db_b_43_test` is now recorded as `served_default` {passed, failed} -- the test bodies with the option at its 2.2.3 default -- which must pass, plus `forced_option_on` {passed, failed, note} recorded as measured. The criterion graded the wrong mode; this is the issuer's check defect, not the worker's.

<criterion id="DB35-1-AC2" cell_refs="DB-b-69"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r35/p35_round35.py" . DB35-1-AC2</invocation><expect>DB35-1-AC2 PASS</expect></criterion>
`DB35-1-AC2` -- one full kit run over >= 7,000 accounts with its refusal count, S33 holding iff it is 0. Base: FAIL.

<criterion id="DB35-2-AC1" cell_refs="DB-b-69"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r35/p35_round35.py" . DB35-2-AC1</invocation><expect>DB35-2-AC1 PASS</expect></criterion>
`DB35-2-AC1` -- the re-cut packet's file list matches HEAD's bytes row by row, carries the rollback, writers and both branches, and prints the measured refusals. Base: FAIL.

<expected_criteria>DB35-1-AC1,DB35-1-AC2,DB35-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This cell applies nothing.** No terraform, no Lambda invoke, no source-map or pin edit, no S3 write. It writes the packet for the halves.
- **No network.** The kit installs offline from the delivered zip only; boto3 and psutil are side-loaded from dell2's site-packages.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-69.release-packet-r35.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 37 (round 35), cell `DB-b-69`.
<owned_cells>DB-b-69</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB35-1-AC1, DB35-1-AC2, DB35-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~46/IRPT_DASHBD.TO-DB-b-69.release-packet-r35.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB35-1-AC1,DB35-1-AC2,DB35-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the S32 read (equal or the differences), the returns sha comparison, DB-b-43's result, the full run's refusals and peak, what the six changed files change, and whether the blast radius widened, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the packet itself is the blast-radius read of the next apply of infra/aws/terraform/investor-reporting/reporting-gold; this cell applies nothing.
comp-iam: RUN -- 214 IAM roles parsed, 196 services scanned (comp-iam stats, 2026-10-09 ~02:5xZ); the lens is BLIND on this subject: `comp-iam role irpt-49f-reporting-gold-role` and `role reporting-gold` return no matching role. So the packet reads the role's write and read sets directly from infra/aws/terraform/investor-reporting/reporting-gold/ (the role and its inline policy), not from comp-iam. This cell changes no role.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the daily schedule is unchanged by this cell; the packet names its after-reads on the first fire.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB35-1-AC1/AC2/2-AC1 base FAIL at base 49cecd310d (no record, no packet); the issuer measured 6 of the round-26 packet's 19 rows stale at HEAD with the same row parser AC1 of cell 2 uses.
lane: the <paths> block IS the grant.
</preflight>
