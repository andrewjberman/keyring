# TO IRPT_BCKEND.TO-IB-m21-212 -- The cot login box gets the in-run login retry (row S165)

<to_id>IRPT_BCKEND.TO-IB-m21-212</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.6.2_AE_PartnerETL~S</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-212`
(`decompositions/IRPT_BCKEND_DECOMP_R21_M.md`) | **outcome_ref:** FWD-1 (COT Performance hop) | **depends_on:** IB-mr-211

---

## WORKER FACE

### THE CELL

`IB-mr-212` -- row `IRPT_BCKEND-S165` (yours): the cot box has no in-run login retry, so one transient login failure
costs a whole day (the chain stayed frozen 09-24..09-27). The retry-capable script is the 49F tree's
`infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` (46,900 B; `MAX_LOGIN_ATTEMPTS` from `BD_MAX_LOGIN_ATTEMPTS`,
default 3, and `BASE_BACKOFF_MS` from `BD_LOGIN_BACKOFF_MS`, default 5000, lines 341-348). The cot tree's
`secret-ids.env` already carries `BD_MAX_LOGIN_ATTEMPTS=3` and `BD_LOGIN_BACKOFF_MS=5000` under "Inert until the new .js
is box-deployed (CTO-gated)". The CTO ruled (round-19 analysis section 3): port the retry-capable script under a deploy
ledger, THE DIFF READ BY THE ISSUER BEFORE IT LANDS.

### BUILD -- two stops

**Part 1 (then STOP):** starting from IB-mr-211's committed build input, bring the retry into
`infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js` -- the smallest change that adds the bounded retry and backoff,
keeping every cot-specific behaviour of the running bytes (read both files whole; name each hunk and why). Write
`org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_PORT_DIFF_20260929.md` (the unified diff
against 28dd27a0 and one line per hunk). Commit it and report "DIFF READY" to `2.0.0_SA_COO~M`. Do not deploy.

**Part 2 (only on the issuer's written GO naming your diff commit):** open ledger
`cot-login-retry-s165-m-20260929` (legs: A1 S3 upload of the cot tree to the box's deploy source; A2 S3 -> box deploy
the way the source already deploys; V1 SSM read of the running `.js` md5 and `secret-ids.env`; V2 the next scheduled
`opal-cot-bd-session-fetch` run Success). Deploy, read back, write
`org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_RETRY_DEPLOY_20260929.json` as
`{"command_id": "<the post-deploy SSM read>", "ledger_slug": "cot-login-retry-s165-m-20260929", "running_md5",
"env_lines": [...]}`, close V1; close V2 on the next scheduled run's Success (cron 07:30 America/New_York), then close
the ledger. Vendor sign-in only through the document, never by hand.

### ACCEPTANCE

<criterion id="IBM21-212-AC1" cell_refs="IB-mr-212"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R21_CHECKS/r21_s165_retry_live.py</invocation><expect>RETRY-LIVE followed by the first 12 hex of the running md5</expect></criterion>
`IBM21-212-AC1` -- the box runs the retry-capable script with the retry variables set, under a closed ledger.

<expected_criteria>IBM21-212-AC1</expected_criteria>

Dry-run at the base 2026-09-29 04:3xZ: NOT-LIVE: the read-back JSON absent (FAIL as expected).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **WORLD, two-stop.** Part 2 only on the issuer's GO. Rollback: re-deploy the 28dd27a0 bytes (IB-mr-211's build input)
  under the same ledger.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
.gitattributes
infra/aws/ec2/bd-cot-auto-login/
infra/logic/registry/
infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js
infra/aws/ec2/bd-cot-auto-login/secret-ids.env
org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_PORT_DIFF_20260929.md
org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_RETRY_DEPLOY_20260929.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/cot-login-retry-s165-m-20260929.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R21_M.md</decomp_doc> (round 21, workstream ~M), cell `IB-mr-212`.
<owned_cells>IB-mr-212</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM21-212-AC1. Instance at `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND.TO-IB-m21-212.cot-login-retry-port.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM21-212-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** "DIFF READY" at Part 1; at Part 2 the ledger legs, the running md5, the env lines, the Success run's
command id, the commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- scheduler cot-bd-session-daily-et, cron(30 7) America/New_York; V2 reads its next Success.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; the deploy uses the path TO-IB-s158 used.
comp-adversary: RUN -- 1 file read (the 49F .js lines 341-348: MAX_LOGIN_ATTEMPTS default 3, BASE_BACKOFF_MS default 5000) and 1 row read (S165: 4 consecutive single-attempt failures 09-24..09-27); BLIND: the full 49F vs cot diff was not read at the cut (Part 1 produces it for the issuer).
lane: the <paths> block IS the grant; issued to the seat the CTO named (analysis s.3).
</preflight>

Source: CTO round-19 analysis (@d797a87872) section 3 row S165/S166, section 6 item 2.

## AMENDMENT 1 (2026-09-29 06:5xZ, issuer 2.0.0_SA_COO~M)

The repo runs core.autocrlf=true and `.gitattributes` has no rule for `infra/aws/ec2/**/*.js`, so a checkout rewrites
`infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js` to CRLF and the byte-exact build input (and IBM21-211-AC1, which
md5s the working file) breaks. Grant widened by one path: `.gitattributes`. Add exactly one line,
`infra/aws/ec2/bd-cot-auto-login/*.js -text`, in the same commit as the .js, so git stores and checks out the bytes
unchanged. Criteria unchanged. Graded by: no gate limb grades a modified order's paths (LIMB 6 fires on new orders
only; GATE (viii) does not apply, `<placeholders>NONE`).

## AMENDMENT 2 (2026-09-29 07:3xZ, issuer 2.0.0_SA_COO~M) -- CTO ruling on row IRPT_BCKEND-S198 (msg 102634)

The running bytes are EVIDENCE (`infra/aws/ec2/bd-cot-auto-login/bd_49f_auto_login.js.running-capture.txt`, TO-IB-m21-211
amendment 2), not a committable build input. So Part 1 builds the DEPLOYABLE cot script: start from the capture, add
the bounded retry and backoff (as before), and carry every firm or product name the naming limb grades through the
registry (`lib/opal_naming` / `infra/logic/registry/`; a builder refusal is a missing registry row to add, never a
hand-typed literal -- CLAUDE.md rule 30). The commit must pass the naming limb with no waiver and no override.
The diff document diffs the new `.js` against the capture (not against a committed .js) with one line per hunk,
separating the retry hunks from the naming hunks. "DIFF READY" goes to 2.0.0_SA_COO~M AND 1.0.0_SA_CTO: the CTO
reads the diff (ruling S198), and the issuer's Part 2 GO names both your diff commit and the CTO's read. Rollback
per key: re-deploy the captured bytes from the capture file under the same ledger. Criterion unchanged.

## AMENDMENT 3 (2026-09-29 07:4xZ, issuer 2.0.0_SA_COO~M) -- row IRPT_BCKEND-S199 (ARMED), ruled inside this cell

S199: the cot script's session `smPut` (running bytes :438) is unguarded, so a failed Secrets Manager write leaves
rc=0 -- and the retry loop's `if (rc === 0) break` then stops on a run whose fresh session was never persisted. That
defeats the purpose of this cell (S165: one transient failure must not cost a day), so the port carries 49F's F2
persist-binding as well: wrap that `smPut` so a failed write sets rc=1 and logs it, the shape of
`infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` :582-593 at HEAD. No other 49F hunk (classifyByDom and the
rest stay out). The Part 1 diff names it as its own hunk, beside the retry hunks and the naming hunks; the CTO reads
it with the rest before the GO. The rollback to the captured bytes undoes it with the retry. This disarms S199 at the
Part 2 V1 read (running md5 = the committed port). Criterion unchanged.

