# TO IRPT_BCKEND.TO-IB-m22-222 -- the Holdings L0 re-mint on its signed release order, read on the served page

<to_id>IRPT_BCKEND.TO-IB-m22-222</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~76</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-222`
(`decompositions/IRPT_BCKEND_DECOMP_R22_M.md`) | **outcome_ref:** FWD-5 (Holdings) | **depends_on:** portal PROD reads
CATEGORY (release step 2, Andrew's word on the hotfix) AND IB-mr-204 drained

---

## WORKER FACE

### THE CELL

`IB-mr-222` -- the scheduled Holdings producer (R4) runs per-firm code packages from S3, not CLOUD:
`s3://opal-data-{49financial,inflection,cottonwood}/irpt/<firm>/code/gold/investor-reporting-holdings.tar.gz`, today
metadata `members-sha256=94f2e3433d9e...`, 41 members. CLOUD carries three signed Holdings changes the packages lack:
IB-mr-202 (each ACCOUNT's children are CATEGORY nodes Models / SMAs / Client), IB-mr-203 (the document's
`source_vendor_keys`, the COT ACCOUNT's `assigned_strategy`), IB-mr-213 (49F account labels read the registration type,
`schwab_account_codes.json` in the closure). Both halves are signed:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_HOLDINGS_L0_CATEGORIES_AND_VENDOR_KEYS_20260929.md` and
`org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_HOLDINGS_UIC16_49F_20260929.md`, with the COO halves in
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_{L0_CATEGORIES,VENDOR_KEYS,UIC16_49F}_20260929.md`.
Their release order: (1) the handlers' contract copy carries the new shape (done by 2.0.0_SA_COO~P, ledger
irpt-holdings-contract-category-20260929); (2) portal PROD reads CATEGORY; (3) this re-mint, every reader read on the
served page. No "a category renders as a security for one cycle" interim.

**Step 0 -- the refusal gate, before anything else.** Stop with a BLOCKING row (id `IRPT_BCKEND-W76-S<k>`) and open
no ledger if EITHER is false:
- portal PROD reads CATEGORY: `git -C portal fetch origin PROD` then `git -C portal show
  origin/PROD:src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts` contains `CATEGORY`, and
  `git -C portal show origin/PROD:src/pages/InvestorReporting/contracts/adapt.ts` maps it to `'category'`;
- `org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-m20-204.r4-first-scheduled-fire-read-back.md` reads
  `<status>complete</status>` at HEAD.

**Part 1 -- mint and one QA fire, then STOP.**
1. Open the ledger FIRST: `python .tools/deploy_ledger.py open --slug irpt-holdings-l0-remint-m-<YYYYMMDD> --title
   "L0 re-mint: irpt_holdings_{49f,inf,cot} from CLOUD <sha> (CATEGORY, vendor keys, assigned strategy, 49F
   registration labels)" --author 0.9.0_WK_IRPT_BCKEND~76` with legs M1/M2/M3 (`safe_deploy_core.py --mint-bundle
   irpt_holdings_<49f|inf|cot>`, closed by the BUNDLE MINTED line + head-object members-sha256 + member-count), Q1
   (the QA fire, 3 of 3 Success) and V1/V2/V3 (each firm's SERVED read at the next scheduled publication). Commit the
   sentinel and the entry at once. Model: the 2026-09-28 entry
   `org/critical_paths/change_management/*_irpt-holdings-packages-m-20260928_deploy_completion.md`.
2. Re-trace `_IRPT_HOLDINGS_CLOSURE` in `.tools/safe_deploy_core.py` against a real build at HEAD (the audit-hook
   method amendment 1 of TO-IB-m19-2 used); a missing member is an edit in this order, named in the ledger.
3. Mint from a CLEAN worktree (the mint reads working-tree bytes, row S124: `git status --short` empty over `data/`,
   `lib/`, `infra/`, `docs/contracts/`): `python .tools/safe_deploy_core.py --mint-bundle irpt_holdings_49f --author
   0.9.0_WK_IRPT_BCKEND~76`, then `_inf`, `_cot`. Close M1-M3.
4. One QA fire: invoke `irpt-holdings-refresh-lambda` with payload `{"qa": true}` (a QA fire publishes to
   `holdings_qa`, never the served table). If the runner `i-02448edb624a7a7cf` is offline the first invoke returns
   `RUNNER_OFFLINE_START_ISSUED`; poll `ssm.describe_instance_information` (at most every 30 s, at most 15 min) until
   Online, then invoke once more. Poll each firm's command (at most every 60 s, at most 60 min) to a terminal status.
   Download each firm's holdings_qa candidate and read it: CATEGORY names, source_vendor_keys, COT assigned_strategy,
   49F labels by registration type. Close Q1 on 3 of 3 Success with those reads; on any failure, leave Q1 open, file a
   row and STOP.
5. Record each firm's SERVED Holdings object (key + VersionId) before and after the QA fire -- they must be equal.
   Report "PART 1 DONE" with the ledger slug, the three members-sha256 and the QA reads. Never a manual non-QA fire.

**Part 2 -- on a fresh spawn after the next scheduled publication (`irpt-holdings-snapshot`, cron 10:15
America/New_York, Mon-Fri).** Read each firm's scheduled command and its served object (key + VersionId, which must
have MOVED for a firm whose command succeeded and stayed for one that failed), write
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_L0_REMINT_READBACK.json` as `{"firms": [{"firm",
"package_bucket", "package_key", "members_sha256", "command_id", "served_bucket", "served_key", "served_version"}]}`,
close V1-V3 and the ledger, and read every reader named in the three COO halves on the served page (the portal Holdings
card and tree, the account picker, the COT assigned strategy) -- each read recorded in the ledger. Rollback per key:
re-mint the packages from the pre-change commit under the same ledger; a served revision is never rewritten.

### ACCEPTANCE

<criterion id="IBM22-222-AC1" cell_refs="IB-mr-222"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_CHECKS/r22_l0_remint.py</invocation><expect>SERVED-L0 followed by each firm's served category names</expect></criterion>
`IBM22-222-AC1` -- the packages are re-minted under a closed ledger and the next scheduled publication serves the L0 shape at every firm.

<expected_criteria>IBM22-222-AC1</expected_criteria>

Dry-run at the base 2026-09-29 10:3xZ: NOT-SERVED (read-back JSON absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **WORLD, two-part, gated.** Step 0 first; Part 2 only on a fresh spawn after the scheduled publication. No
  manual non-QA fire, ever. No schedule change.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W76-S<k>`), and do not weaken the test to pass.

<paths>
.tools/safe_deploy_core.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-holdings-l0-remint-m-*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_L0_REMINT_READBACK.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_L0_REMINT_QA/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R22_M.md</decomp_doc> (round 22, workstream ~M), cell `IB-mr-222`.
<owned_cells>IB-mr-222</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM22-222-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~76/IRPT_BCKEND.TO-IB-m22-222.holdings-l0-remint-served-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM22-222-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** "PART 1 DONE" at Part 1 (ledger slug, members-sha256 x3, QA reads); at Part 2 the scheduled command ids,
the served keys + VersionIds, every reader read, the commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- irpt-holdings-snapshot, cron(15 10 ? * MON-FRI *) America/New_York, ENABLED (IB-mr-201); Part 2 reads its next fire; no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; the firm principals already carry GetObjectVersion (IB-mr-2 amendment) and PublishOwnHoldings.
comp-adversary: RUN -- 3 signoffs read (CTO L0+vendor keys @98ec00b676, CTO UIC-16 on acct_regis, COO halves) and 1 package head read at the cut (members-sha256 94f2e3433d9e, 41 members); BLIND: the portal PROD state is unread at the cut (step 0 reads it) and the closure is untraced at HEAD (step 2 traces it).
lane: the <paths> block IS the grant; ~M owns the Holdings producer.
</preflight>

Source: CTO sweep-1 analysis (`ledger/ROUND_ANALYSIS.sweep1.md` @eaefb76322) section 4 item 3; the signed release order.
