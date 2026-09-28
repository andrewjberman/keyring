# TO IRPT_BCKEND.TO-IB-mr-2 -- R4: re-mint the three Holdings packages, one QA fire, fill the ENABLE half

<to_id>IRPT_BCKEND.TO-IB-mr-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~42</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-28</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-2` (`decompositions/IRPT_BCKEND_DECOMP_R19_M.md`) | **outcome_ref:** FWD-5 backend half, goal criterion 3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-2` -- the scheduled daily Holdings producer (R4) is built and applied with its schedule DISABLED. It runs a
per-firm code package from S3, not CLOUD. CLOUD now carries two Holdings changes the packages lack: the cash-line rule
(`classify_security` on `display.description`) and UIC-16 (the account type in full), both in
`C:/Users/AndrewBerman/Desktop/ajb_workspace/data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`
(on CLOUD at bcf7a6adde; your worktree's HEAD carries it). Three steps, in order:

**Step 1 -- re-mint the three packages under a new ledger.** Measured 17:5xZ: at
`s3://opal-data-{49financial,inflection,cottonwood}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz` each
object carries metadata `members-sha256=83f6a81aab34...` and `member-count=40` (minted 2026-09-25 from 4f58a95c84).
The bundles are declared in `C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/safe_deploy_core.py` STANDALONE_BUNDLES
as `irpt_holdings_49f`, `irpt_holdings_inf`, `irpt_holdings_cot` (never commit-routed; minted only explicitly).
- Open the ledger FIRST: `python .tools/deploy_ledger.py open --slug irpt-holdings-packages-m-20260928 --title "R4 D.0:
  re-mint irpt_holdings_{49f,inf,cot} from CLOUD bcf7a6adde+ (cash rule + UIC-16); nothing scheduled runs them"
  --author 0.9.0_WK_IRPT_BCKEND~42 --leg "M1|s3-prefix|safe-deploy --mint-bundle irpt_holdings_49f|BUNDLE MINTED line +
  head-object members-sha256 + member-count"` plus legs M2 (`irpt_holdings_inf`) and M3 (`irpt_holdings_cot`). Commit
  the sentinel and entry at once. The 2026-09-25 entry is the model:
  `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/critical_paths/change_management/20260925T1810Z_irpt-holdings-packages-m-20260925_deploy_completion.md`.
- Mint each: `python .tools/safe_deploy_core.py --mint-bundle irpt_holdings_49f --author 0.9.0_WK_IRPT_BCKEND~42`
  (then `_inf`, `_cot`). Mint from a CLEAN worktree: the mint reads working-tree bytes (row IRPT_BCKEND-S124), so no
  member file may differ from HEAD (`git status --short` empty over `data/`, `lib/`, `infra/`, `docs/contracts/`).
- Close each leg with the `BUNDLE MINTED` line and the head-object `members-sha256` + `member-count`; then `close`.

**Step 2 -- one QA fire.** Invoke `irpt-holdings-refresh-lambda` with payload `{"qa": true}` (boto3
`lambda.invoke(FunctionName=..., Payload=b'{"qa": true}')`). A QA fire publishes to `holdings_qa`, never the served
table (source `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/investor-reporting/holdings_refresh/refresh_dispatch.py`).
The runner host `i-02448edb624a7a7cf` (mdpf-daily-runner) was STOPPED at 18:0xZ: the first invoke then returns
`RUNNER_OFFLINE_START_ISSUED` and starts it. Poll `ssm.describe_instance_information` (at most every 30 s, at most
15 min) until PingStatus is Online, then invoke ONCE more. That returns `DISPATCHED` with one SSM command per firm,
commented `irpt holdings refresh qa <firm> 2026-09-28`. Poll each command (at most every 60 s, at most 60 min) to a
terminal status and read its output (`get_command_invocation`): the rc, the as_of it built, and the holdings_qa
revision it published. Before the second invoke and after the last command ends, record each firm's SERVED Holdings
manifest (`irpt/<firm>/platinum/...current/manifest.json` in the firm bucket; find the exact key from
`holdings_snapshot.py`'s publisher `location("platinum", "current", "manifest.json")`) VersionId: they must be equal.
Do not stop the host afterwards (it has its own shutdown).

**Step 3 -- fill the ENABLE half.** Copy
`C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_DRAFT.md`
to `.../IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_20260928.md` and fill every `{{slot}}` from your measurements:
- Precondition 1 (N1): DONE -- ledger `irpt-holdings-principals-dispatch-m-20260925` CLOSED @26127abf10 (4 of 4, SSM
  da369659). Cite it; do not re-run N1.
- Precondition 2: the three QA command ids, rc, holdings_qa revisions, and served manifest VersionId before = after.
- Precondition 3: run `holdings_publication_diff_classes.py --firm <firm> --candidate <the firm's holdings_qa platinum
  JSON, downloaded> --out .../IRPT_MVP_M/R4_ENABLE_DIFF_20260928/QA_<firm>.json` for each firm and fill the class table
  from those three files. The pinned re-run at the served date is already in `R4_ENABLE_DIFF_20260928/README.md`
  (0 node / amount / clock changes; labels 2,970 / 875 / 755; classes 123 / 30,881 / 2,577); cite it beside the QA
  numbers.
- Precondition 4: repeat the INF name census on the INF QA candidate by the method in
  `.../IRPT_MVP_M/R4_ENABLE_DIFF_20260926/README.md` (email-like count, six-plus-digit texts, each dispositioned).
- Add three lines to "What the first scheduled publication moves": the cash-line rule (`CASH -- CASH` -> `cash`, count
  per firm from the QA diff); UIC-16 account-type labels (INF only; 49F keeps Schwab codes); ETF Part A (16 keys incl.
  VNQ -> alternatives; CTO @c516dab84b).
- Add under "Does not touch": `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`
  (the directory chain's bundle, ETag 4155283a, stays; UIC-16's directory side waits on 2.0.0_SA_COO~P's next directory
  package).
- Add the members-sha256 of the re-minted packages (Step 1) as the code the schedule will run.
- Do NOT send it. The issuer sends it to 1.0.0_SA_CTO and 4.0.0_SA_CRO at the drain.

### ACCEPTANCE

<criterion id="IBM19-2-AC1" cell_refs="IB-mr-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_CHECKS/r19_m2_packages_reminted.py</invocation><expect>REMINTED followed by a 12-hex members-sha256 that is not 83f6a81aab34</expect></criterion>
`IBM19-2-AC1` -- the three packages carry one new members-sha256 and the mint ledger is CLOSED.

<criterion id="IBM19-2-AC2" cell_refs="IB-mr-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_CHECKS/r19_m2_qa_fire.py</invocation><expect>QA-FIRED followed by 49financial, inflection and cottonwood each with a Success command id</expect></criterion>
`IBM19-2-AC2` -- one QA fire reached Success at all three firms.

<criterion id="IBM19-2-AC3" cell_refs="IB-mr-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R19_CHECKS/r19_m2_half_filled.py</invocation><expect>FILLED with at least 3 command ids</expect></criterion>
`IBM19-2-AC3` -- the half is filled from the fire, no slot left.

<expected_criteria>IBM19-2-AC1,IBM19-2-AC2,IBM19-2-AC3</expected_criteria>

All three run from your worktree root and exit 1 at the base (dry-run 2026-09-28 18:2xZ: NOT-REMINTED / NOT-FIRED 0 of
161 commands / NOT-FILLED). The QA-fire check reads AWS, so it is graded after your commands end.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **WORLD act, bounded.** You may write ONLY the three package objects and invoke the dispatch with `{"qa": true}`. Never
  invoke it without `qa`, never touch the schedule `irpt-holdings-snapshot` (it stays DISABLED), never re-mint
  `investor-reporting.tar.gz`, never write a served Holdings table or index. Any deploy other than Step 1 is out of bounds.
- **Rollback of Step 1** (if a mint fails verify): re-put the prior object version of each package (the 2026-09-25
  versions) and record it in the ledger.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row (id `IRPT_BCKEND-W42-S<k>`), and do not weaken the test to pass.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-holdings-packages-m-20260928.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_R4_ENABLE_20260928.md
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R4_ENABLE_DIFF_20260928/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named on this face (the draft half, the diff tools, the 09-26 README,
the checks in `R19_CHECKS/`, `.tools/`, the Holdings and dispatch source) you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R19_M.md</decomp_doc> (round 19, workstream ~M), cell `IB-mr-2`.
<owned_cells>IB-mr-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM19-2-AC1, IBM19-2-AC2, IBM19-2-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~42/IRPT_BCKEND.TO-IB-mr-2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM19-2-AC1,IBM19-2-AC2,IBM19-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the ledger slug and its close, the new members-sha256, the three QA command ids with
rc and holdings_qa revision, served manifest VersionIds before/after, the QA as_of, the half's path, the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- schedule irpt-holdings-snapshot DISABLED (ledger irpt-holdings-dispatch-qa-m-20260926 read-back); runner i-02448edb624a7a7cf stopped at 18:0xZ; dispatch starts it (refresh_dispatch.py:110-112).
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; the dispatch role and the firm principals are applied (ledger irpt-holdings-principals-dispatch-m-20260925 CLOSED).
comp-adversary: RUN -- S124 (mint reads working-tree bytes) bounded by minting from a clean worker worktree; head-object 17:5xZ: 3 of 3 packages at 83f6a81aab34.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>


Source: `STATUS~M.md` @e589729e6a next-list items 2-4; runbook `IRPT_MVP_M/MONDAY_20260928_RUNBOOK.md` D.0, D.2, D.3.
