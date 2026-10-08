# TO IRPT_BCKEND.TO-IB-pr-366 -- the live guard resolves an on-behalf owner: an OPAL_GLOBAL filer's CREATE for a listed firm is admitted through the real served path; every other case keeps today's owner

<to_id>IRPT_BCKEND.TO-IB-pr-366</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~174</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>79</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO round analysis ADDENDUM 2 @b227133904 (msg 1362), E5, on `~Y2` msg 1361
and row D2-W156-S2 | **Decomp cell:** `IB-pr-366` (decomposition section 72) | **outcome_ref:** X-1 (TCKT_VNEXT TV-r-1 waits on it) |
**depends_on:** none (IB-yr-631, IB-pr-354, IB-pr-358 drained).

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-174` (branch `wk-IRPT_BCKEND-174`). Work and commit only there. Paths below are relative
to it. `L` = `infra/aws/lambda/investor-reporting`.

**What failed live.** Release 2 shipped the on-behalf upload door and was rolled back at 17:44:54Z. Unit tests passed because they
hand `UploadService.create` an owner the live guard never builds. On the served path:
1. `L/_authz/served.py` ~line 907 builds `InteractiveAccess(lambda: request.headers, tenant)` with NO `profile_reader`. So
   `current()` never carries `allowedFirmIds` on the served path. Only `reports/generate_installed.py` `compose_upload` wires one
   (IB-pr-358).
2. `served.py` ~line 920 resolves the create owner as `access.prospect_owner()` with no storage firm. `_scope/interactive_access.py`
   `prospect_owner` (~lines 123-137) then copies the ACTOR's own firm and principal into the owner.
3. So in `L/intake/uploads.py` `create` (~lines 241-248), `on_behalf` needs `principal_id != owner principal_id` AND the owner's firm
   listed in the actor's `allowedFirmIds`. That is never true on the served path.

The shape `create` admits for on-behalf is in `L/intake/tests/test_uploads_on_behalf.py`: the owner is the FIRM advisor's owner
(`resolve_prospect_owner` on that firm's claims), and the principal is the Opal filer with `allowedFirmIds` listing the firm.

**Your cell.** Change the served CREATE path so that, when the verified subject is an OPAL_GLOBAL filer (home opal-capital) whose
`allowedFirmIds` explicitly lists the target firm, the owner the guard resolves is that admitted shape. Every other case keeps
exactly today's owner and today's refusal codes.
- `allowedFirmIds` comes from the EXISTING canonical profile read (`CanonicalProfileReaders.get_user`, as IB-pr-354/358 use it). Add
  no new client and no new table read.
- The owner firm and owner principal are SERVER-RESOLVED from verified request fields or existing server state. No unverified body
  field becomes authority. If you find no server-resolvable owner principal for the target firm, STOP: file a row with disposition
  `DECOMP_INVALIDATING` naming what is missing, and do not invent one.
- Do not edit `L/intake/uploads.py`. It is `~Y2`'s lane, and its rule is the target.

**The test.** Write `L/_authz/tests/test_served_on_behalf_create.py`.
- It must `import served` and drive the REAL guarded handler (`served`'s prospect CREATE path with a verified internal subject),
  never `create` directly.
- `test_served_admits_listed_firm`: the listed firm is admitted, and the stored upload record names `acting_principal_id` = the
  filer and `owner.firm_id` = the firm.
- Negative arms, each refused with its EXISTING code, and no record stored:
  - `test_served_refuses_unlisted_firm`
  - `test_served_refuses_all` (`allowedFirmIds` = "ALL")
  - `test_served_refuses_non_internal` (an ordinary advisor of another firm)
  - `test_served_refuses_owner_opal_capital`

**AMENDMENT 1 (2026-10-08 ~18:3xZ, issuer `2.0.0_SA_COO~P2`, on row D2-W174-S1 and CTO ruling msg 1402: option (c)).**
- **The owner principal's source.** The CREATE request names an advisor email. It is used ONLY as a lookup key, verified through
  the EXISTING `CanonicalProfileReaders.get_partner_profile(email, firm)` on the registry-validated owner firm (the guard's tenant).
  The owner is built exactly as `resolve_prospect_owner` builds it for that advisor. `uploads.py` stays unchanged. Andrew confirmed
  ~18:3xZ that on-behalf upload is a wanted function (CTO msg 1402).
- **Fail closed, with existing codes:** email absent; profile absent (None); profile disabled; an advisor whose profile belongs to
  a different firm than the named one; any read error. In every one of these, no record is stored.
- **Four more negative arms** on the real served path, named exactly:
  - `test_served_refuses_advisor_email_absent`
  - `test_served_refuses_advisor_profile_absent`
  - `test_served_refuses_advisor_profile_disabled`
  - `test_served_refuses_advisor_of_other_firm`
  IB79-1-AC2 now requires all eight arms. The check is amended in the same commit.
- **Resolve your row.** When the cell is done, append `IRPT_BCKEND-D2-W174-S2`, a DISMISSED_WITH_REASON whose `dismissal_reason`
  starts `Resolves IRPT_BCKEND-D2-W174-S1:` and cites CTO msg 1402 and your fix commit.
- Gate limb: none graded this amendment (a modification; GATE viii only).

<criterion id="IB79-1-AC1" cell_refs="IB-pr-366"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r79/p79_cells.py" . IB79-1-AC1</invocation><expect>IB79-1-AC1 PASS</expect></criterion>
`IB79-1-AC1` -- the test file imports `served`, and its admit arm passes through the real served path. Base: FAIL (no file).

<criterion id="IB79-1-AC2" cell_refs="IB-pr-366"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r79/p79_cells.py" . IB79-1-AC2</invocation><expect>IB79-1-AC2 PASS</expect></criterion>
`IB79-1-AC2` -- the four named negative arms are defined and pass through the same path. Base: FAIL (no file).

<criterion id="IB79-1-AC3" cell_refs="IB-pr-366"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r79/p79_cells.py" . IB79-1-AC3</invocation><expect>IB79-1-AC3 PASS</expect></criterion>
`IB79-1-AC3` -- the six existing guard, scope and uploads suites pass, each in its own process. Base: PASS (no regression). Run them
one file at a time: together they collide on a double import of `uploads.UploadRefused`.

<expected_criteria>IB79-1-AC1, IB79-1-AC2, IB79-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block and nothing else. No AWS call, no build, no deploy.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause.** If a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W174-S<k>` (dell2 coordinate). Re-read the channel right before you append. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~174" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~174@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~174 <0.9.0_WK_IRPT_BCKEND~174@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_scope/interactive_access.py
infra/aws/lambda/investor-reporting/_authz/tests/test_served_on_behalf_create.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-366.live-guard-resolves-on-behalf-owner.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~174/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 72 (round 79, workstream ~P), cell `IB-pr-366`.
<owned_cells>IB-pr-366</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB79-1-AC1, IB79-1-AC2, IB79-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~174/IRPT_BCKEND.TO-IB-pr-366.live-guard-resolves-on-behalf-owner.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the commit hashes, each criterion's last line, how the owner principal is server-resolved, and any
row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- served.py's prospect CREATE path (_handle_prospect) is shared by every function that packages _authz/served.py and _scope/interactive_access.py; the change is confined to the OPAL_GLOBAL + listed-firm CREATE branch, every other owner unchanged (AC2 + AC3). No function is released by this order; release 2 re-pins after it drains (ADDENDUM 2).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission changes; the profile read is the existing CanonicalProfileReaders.get_user.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p79_cells.py dry-run at base 5ff7717f66 on dell2 2026-10-08 ~18:1xZ: AC1 FAIL (no file), AC2 FAIL (no file), AC3 PASS (each suite alone; together they fail 7 on a double import, measured).
lane: the <paths> block IS the grant; _scope/ and _authz/served.py are ~P's (lane IRPT_LIVE_SCOPE_P, ADDENDUM 2 citing msg 944 (1)); intake/uploads.py is ~Y2's and is NOT granted.
</preflight>
