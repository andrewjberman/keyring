# Deploy Completion Record
**Date opened:** 2026-10-09T09:52:20.498008+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-84 (E2, round 41, cell DB-b-84): mint the svc-custody-statement RS256 service token and create ONE secret opal/investor-reporting/svc-custody-statement, under the signed never-widen pair -- COO half AMENDMENT 2 @a319fc74b8 (2.0.0_SA_COO~K2), CTO half GIVEN by 1.0.0_SA_CTO~DELL2 (msg 2440, signed against blob 323217e49c). Blast radius signed: ONE secret, ONE reader ARN on dell2's GetSecretValue allow-list (a LAPTOP act routed via 0.0.0_AB_MSTR~DELL2), no IAM user/group/roster change. Rollback: delete-secret with the DEFAULT recovery window (never force) and the ARN removed.
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B | verify | before-read, re-run at apply | all three hold: describe-secret opal/investor-reporting/svc-custody-statement returns ResourceNotFoundException; IB-pr-385 LIVE in irpt-export-render read from its release ledger; irpt-ycharts-generate live CodeSha256 starts tdpterTM (release 6b). Any one missing is a STOP. | ALL THREE BEFORE-READ LIMBS HOLD, measured on live state at 2026-10-09 ~09:5xZ from the worktree /c/dev/wk-db2-r41-mint at 527258980e, not taken from any producer's self-report. (1) SECRET ABSENT: describe-secret opal/investor-reporting/svc-custody-statement returns ResourceNotFoundException -- and the absence is REAL rather than an instrument failure, because the same binary and credential read an existing secret in a SEPARATE invocation as the positive control (opal/ticketing/svc-analyst-intake -> arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/ticketing/svc-analyst-intake-HGzn67, the very allow-list neighbour the pair names). A failed retrieval returns a VALUE, so the control is what makes this a true negative. (2) IB-pr-385 LIVE in irpt-export-render, verified BY CONTENT against the BUILD INPUT and never by filename: its release ledger org/critical_paths/change_management/20261009T0722Z_irpt-authz-served-release-390-20261009_deploy_completion.md is CLOSED -- nothing stranded, closed 20261009T075610Z, authored 0.7.0_AE_CloudOps~IB2 -- and it declares IB-pr-390 = IB-pr-385 svc-custody-statement + IB-pr-387 allowedFirmIds narrowing + ALL-never-admits, released as IB-pr-395 over 6 of 8 hosts at code pin 74a62fb46ce9ff2e2baa305d3eadfac6b8145651, naming irpt-export-render's BUILT sha256 as c7jOyysB/zo6OjtzCNdUZiu0o4fxNE9XeCM1FxXIHhk=. The function's LIVE CodeSha256 measured just now is c7jOyysB/zo6OjtzCNdUZiu0o4fxNE9XeCM1FxXIHhk=, LastModified 2026-10-09T07:47:08Z -- EQUAL to the declared build input, which is the rule-22a CODE test (deployed bytes against the build input), so the named-service-subject admission this token depends on is genuinely running. (3) RELEASE 6b LIVE: irpt-ycharts-generate live CodeSha256 tdpterTMfJlWXjnoAQCwil+wN/Jf8Q/yLjGxTk7yUkk=, LastModified 2026-10-09T09:32:22Z -- it STARTS tdpterTM as the order requires, and it matches the 6b applier's own Y2 leg independently of that leg's claim. No limb is missing, so the pair's STOP does not fire and the mint may proceed. | CLOSED 20261009T095613Z |
| M | activation | mint RS256 from the CURRENT slot of opal/auth/jwt-private-key (memory only, never printed or written) and create the ONE secret | decoded claims equal pair section 1 EXACTLY (sub/name svc-custody-statement, userType/tier service, firmId cottonwood, iss opal-portal-auth, aud opal-portal-api; role/advisorId/allowedPages/allowedTabs/firmRole ABSENT), exp-iat <= 90 days, secret name passed through lib/opal_naming.py, and the create-secret ARN | MINTED AND CREATED, claims exactly the pair's. Secret ARN arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/investor-reporting/svc-custody-statement-9CmPmS, name opal/investor-reporting/svc-custody-statement, version 733fd650-ed1e-4d65-aad3-87483bdfe8e1, CreatedDate 2026-10-09T06:05:57.717-04:00 == 10:05:57Z (the API renders a LOCAL offset; it is stated here rather than retyped as a literal Z). CLAIMS, decoded WITHOUT verifying per pair section 3 step 3 and asserted in code, not by eye: sub and name svc-custody-statement; userType and tier service; firmId cottonwood; iss opal-portal-auth; aud opal-portal-api; iat 1791540357; exp 1799316357. TTL exp-iat = 90.0 days exactly, at the cap, not over. Header alg RS256, typ JWT. The five forbidden claims (role, advisorId, allowedPages, allowedTabs, firmRole) are ABSENT, and the script also refuses any claim OUTSIDE the pair's set, so the token cannot carry a surprise field: userType is not Dev and tier is not internal, so allowedFirmIds can never be ALL and is exactly cottonwood. CREDENTIAL READ REPORTED LIKE A DEPLOY (pair section 2): opal/auth/jwt-private-key, VersionId 579af491-ab27-4463-978d-b076cd5ce44a, VersionStages [AWSCURRENT] -- that stage IS the CURRENT slot the pair names; the value is a raw PEM, read into memory only, never printed, never written, never passed through argv, and deleted from the local after signing. The minted token was handed to CreateSecret IN-PROCESS for the same reason -- a --secret-string on a command line would have put a live bearer credential into process arguments. Nothing printed, committed or recorded contains the key, the token or its signature; MINT_RECORD.json carries decoded claims only. SECRET VALUE: exactly the four fields the pair names (token, sub, exp, minted_by). DESCRIPTION: states the one use (the custody-report persist route plus POST /analysis and POST /export), firm cottonwood ONLY with the firm from the verified claim and never a request field, TTL 90 days, exp 2027-01-07T10:05:57Z, ROTATE BY 2026-12-24T10:05:57Z (14 days before exp, owner 2.0.0_SA_COO~D2), the pair it was minted under, and that the real control is IB-pr-385. READ BACK INDEPENDENTLY in a separate invocation with describe-secret: name, ARN and the full description match what was sent. NAMING GATE, run first as the order requires: lib.opal_naming.name('opal','investor-reporting','custody-statement','SECRET') REFUSED with ValueError "scope 'investor-reporting' resolves to no scopes.json row". The builder's grammar is {system}-{scope}-{function}[-{qualifier}]-{kind} over scope classes FIRM/GLOBAL/MASTER and cannot express a slash-delimited svc-* Secrets Manager path at all, so no registry row would make this name a builder output -- which is why the COO half states in advance that the name 'is from the svc-* family and is not a builder output'. Rule 30's remedy is a row under infra/logic/registry/, which this order's BOUNDS put out of grant; filed as surprise row IRPT_DASHBD-S38 @fe6b451cee (OBSERVATION, INERT) with the registry gap routed to an owner, and proceeded on the pair-signed name, which both halves and the order name verbatim and the CTO half signs as 'exactly this one secret'. No hand-typed workaround: the name was not invented here. The commit-time LGIC_ENFORCE gate is not reached because this act commits no name into code or Terraform. | CLOSED 20261009T100649Z |
| R | activation | the ONE reader ARN added to dell2's secretsmanager:GetSecretValue allow-list -- a LAPTOP 0.7.0_AE_CloudOps act, routed via 0.0.0_AB_MSTR~DELL2 | the laptop's applied answer, then simulate-principal-policy: allowed for cloudops-dell2-agent-user on THIS ARN and implicitDeny on an unlisted secret, one --resource-arns per call with a separate positive control |  | OPEN |
| V | verify | read-backs and the three criteria | MINT_RECORD.json written in deliverables/0.7.0_AE_CloudOps~DB2/, DB41-1-AC1/AC2/AC3 each PASS from p41_round41.py, and proof-of-spec-check.py reports the instance VALID |  | OPEN |

## Log

- 20261009T095220Z OPENED by 0.7.0_AE_CloudOps~DB2 with 4 leg(s)
- 20261009T095613Z LEG B closed: ALL THREE BEFORE-READ LIMBS HOLD, measured on live state at 2026-10-09 ~09:5xZ from the worktree /c/dev/wk-db2-r41-mint 
- 20261009T100649Z LEG M closed: MINTED AND CREATED, claims exactly the pair's. Secret ARN arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/inve


---

## NOTE 1 -- 2026-10-09 ~10:1xZ: the NAMING GRADE call and its verdict (required by the issuer's ruling, msg 3093)

`1.0.0_SA_CTO~DELL2` ADDENDUM 9.3, relayed by `2.0.0_SA_COO~D2` as msg 3093, on row `IRPT_DASHBD-S38`:
**secrets are GRADED, not BUILT** (the W1-S4 precedent). No R19, no R20, no registry row.

GRADE CALL, run in this worktree at the ruling:

    lib.opal_naming.grade('opal/investor-reporting/svc-custody-statement', 'SECRET')
      -> ('CONFORMANT', 'opal/investor-reporting/svc-custody-statement')

    lib.opal_naming.grade('opal/ticketing/svc-analyst-intake', 'SECRET')        # the ruling's control
      -> ('CONFORMANT', 'opal/ticketing/svc-analyst-intake')

Both CONFORMANT, and in each case the canonical form the grader returns EQUALS the name as given, so the
secret this leg created already carries its canonical name. `grade`'s own domain note (GRADING_RULE.md)
is why this is the right verb: its verdicts are NO-SYSTEM-ASKED / CONFORMANT / ALIAS / OUT-OF-PATTERN,
and NOT-GRADED for a type outside its domain.

**Correction to this seat's leg-M proof and to row S38.** Leg M recorded a `name()` REFUSAL
(`ValueError: scope 'investor-reporting' resolves to no scopes.json row`) and treated it as a gate
refusal to be routed to an owner under rule 30. That reading was wrong in one specific way, and the
ruling is the authority: `name()` is the BUILD verb and a secret is not a built name, so its refusal on
a slash-delimited Secrets Manager path is CORRECT BEHAVIOUR, not a gate defect. **There is therefore
nothing to route, and no registry row is owed** -- the ruling says so explicitly, and this seat does
not route a non-defect. The mint's name was never in doubt (both signed halves and the order name it
verbatim); what was wrong was the instrument this seat reached for. The underlying cause is worth
naming because it is reusable: the first probe of the module filtered its exports by a forward guess
(`'name' or 'secret' or 'address' in the export`), and `grade` matches none of those words, so a verb
that was present the whole time read as absent -- rule 24(i)'s hunt-by-subtraction-from-a-printed-
denominator, skipped. Reading the full export list is what found it.

**Nothing about the created secret changes:** same name, same ARN, same claims, same TTL. This note
adds the grade verdict the ruling requires and corrects the reasoning recorded beside it.


---

## NOTE 2 -- 2026-10-09 ~11:5xZ: the ROLLBACK TRIGGER for leg R, recorded so a successor can act without this session

Leg R is gated on a LAPTOP act (the reader-ARN add to `cloudops-dell-agent-platform-secrets-policy`, cut there as
NFRA_CTLPLN AMENDMENT 30). Relay msg 3224: the laptop's `0.7.0_AE_CloudOps` has read no mail since ~09:29Z and
`2.0.0_SA_COO~C` is moving AMENDMENTS 29/30 to a fresh lane, so the ~12:00Z applied ETA MAY SLIP. Window to ~17:52Z.

**Why this note exists.** CLAUDE.md's NEVER-2 says an entry a device left OPEN proves only that THIS device saw no
completion. If this session ends before the ARN lands, the trigger below must be readable from the entry itself
rather than from a live agent's intent.

**TRIGGER.** If the policy's default version is still `v3` (30 ARNs, no svc-custody-statement entry) at **~16:30Z**,
roll back rather than let the window lapse:

1. `aws secretsmanager delete-secret --secret-id opal/investor-reporting/svc-custody-statement` with the **DEFAULT
   recovery window -- NEVER `--force-delete-without-recovery`**. The pair's rollback says default; the default window
   is what makes this reversible if the laptop lands minutes later.
2. Nothing to remove from the allow-list: the ARN was never added, which is the whole reason leg R is open. Do NOT
   ask the laptop to add and then remove it.
3. `deploy_ledger.py close-leg R` with the rollback as its proof, then `close` the entry, then escalate LOUD to
   `2.0.0_SA_COO~D2` (issuer) and `0.0.0_AB_MSTR~DELL2` (the relay), naming this note.

**Authority.** No new sign-off is needed: `delete-secret` with the default recovery window IS the rollback both halves
signed (COO half AMENDMENT 2; CTO half "Rollback: delete-secret with the DEFAULT recovery window (never force)").

**WHAT THE ROLLBACK DOES NOT TOUCH, so nobody over-reads it.** The code admission IB-pr-385 is live in
`irpt-export-render` and stays live -- it is IRPT_BCKEND's, not this order's, and the pair names it as the real
control. Rolling back this secret disarms only this token's custody; it does not revert the released code, and it
does not touch `opal/auth/jwt-private-key`, the portal authorizer, any human principal or any other firm.

**MEASURE BEFORE ACTING ON THIS TRIGGER.** Read the policy's live default version first and print it beside the
decision -- if it has moved past `v3`, the apply landed and the correct act is to re-simulate and CLOSE, never to
roll back. World-done closes SUPERSEDED; it is never re-executed.
