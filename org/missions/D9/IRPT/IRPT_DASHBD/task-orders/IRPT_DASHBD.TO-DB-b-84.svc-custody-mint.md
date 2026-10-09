# TO IRPT_DASHBD.TO-DB-b-84 -- E2: land the svc-custody-statement service token under its signed never-widen pair -- before-read, mint, secret, reader grant routed via MSTR to the laptop, read-backs, ledger committed after each leg

<to_id>IRPT_DASHBD.TO-DB-b-84</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~DB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>41</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 9.1 (msg 3011; the IRPT_CUSTDY handover @185805a565), enrichment item E2 | **Decomp cell:** `DB-b-84` (decomposition section 43) | **outcome_ref:** FWD-12 | **depends_on:** the pair (both halves); IB-pr-385 and release 6b live.

---

## WORKER FACE

You are the seat `0.7.0_AE_CloudOps~DB2` (seated for IRPT_DASHBD, MSTR msg 2572). Work in your own linked worktree, cut from box/dell2. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/`.

**The cell (`DB-b-84`).** Run leg M of the never-widen pair. Read every part of it:
- the COO half and AMENDMENTS 1 and 2: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/NEVER_WIDEN_PAIR_SVC_CUSTODY_STATEMENT_MINT.md` (signed by `2.0.0_SA_COO~K2` @a319fc74b8);
- the CTO half: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_SVC_CUSTODY_STATEMENT_MINT_CTO_HALF.md` (msg 2440).

AMENDMENT 2 is binding: no roster row, and the token's firm comes from its verified claim. The CTO's ADDENDUM 9.1 (msg 3011) places this act in
round 41 under the existing pair.

1. **Ledger first, pinned.** Use `python .tools/deploy_ledger.py`. Name legs B (before-read), M (mint + secret), R (reader grant) and V
   (read-backs), and state in it the pair you act under. Commit the ledger after EACH leg (relay msg 2973). Record `ledger_entry`.
2. **Before-read (re-run at apply).** Each of the following must hold; any one missing is a STOP.
   - `describe-secret opal/investor-reporting/svc-custody-statement` returns ResourceNotFoundException;
   - IB-pr-385 is live in `irpt-export-render` (inside IB-pr-390, applied 07:49Z; read its release ledger);
   - `irpt-ycharts-generate` is live at a CodeSha256 starting `tdpterTM` (release 6b).

   Record `before_read` {secret_absent, ib_pr_385_live, release_6b_code}.
3. **Mint.**
   - Use the claims of the pair's section 1 exactly: `sub`/`name` `svc-custody-statement`, `userType`/`tier` `service`, `firmId`
     `cottonwood`, `iss` `opal-portal-auth`, `aud` `opal-portal-api`, `exp - iat` <= 90 days.
   - None of `role`, `advisorId`, `allowedPages`, `allowedTabs`, `firmRole`.
   - RS256 with the CURRENT slot of `opal/auth/jwt-private-key`, read into memory and never printed or written.
   - Run the secret name through `lib/opal_naming.py` first; a refusal is a registry row (rule 30).
   - `create-secret` with the value and description the pair's section 2 names.
   - Record `claims` (the decoded claims, no signature) and `ttl_days`, and `secret` {name, arn}.
4. **Reader grant.** Add this ONE ARN to dell2's GetSecretValue allow-list. Per the CTO correction, that is a laptop `0.7.0_AE_CloudOps` act.
   - Send `0.0.0_AB_MSTR~DELL2` the exact secret ARN, the two halves and this order's path, and wait for the laptop's applied answer.
   - Then simulate `GetSecretValue`: allowed for the dell2 user on this ARN, and implicitDeny on an unlisted secret.
   - Record `reader` {routed_via "0.0.0_AB_MSTR~DELL2", applied, simulate_listed, simulate_unlisted}.
5. **Report the credential read by secret name and run, like a deploy.** Rotation is due 14 days before exp; its owner is
   `2.0.0_SA_COO~D2`.

Record `MINT_RECORD.json` in your folder. The positive and negative arms (steps 4-6 of the pair) are DB-b-86's.

<criterion id="DB41-1-AC1" cell_refs="DB-b-84"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-1-AC1</invocation><expect>DB41-1-AC1 PASS</expect></criterion>
`DB41-1-AC1` -- the before-read holds and the token's claims are exactly the pair's (cottonwood, service, no role), TTL at most 90 days. Base: FAIL.

<criterion id="DB41-1-AC2" cell_refs="DB-b-84"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-1-AC2</invocation><expect>DB41-1-AC2 PASS</expect></criterion>
`DB41-1-AC2` -- the secret is created and its reader grant, routed via MSTR, simulates allowed on it and implicitDeny elsewhere. Base: FAIL.

<criterion id="DB41-1-AC3" cell_refs="DB-b-84"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41/p41_round41.py" . DB41-1-AC3</invocation><expect>DB41-1-AC3 PASS</expect></criterion>
`DB41-1-AC3` -- the ledger names the act. Base: FAIL.

<expected_criteria>DB41-1-AC1,DB41-1-AC2,DB41-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's acts, under the signed pair:** ONE secret created, ONE reader-ARN add requested from the laptop through
  `0.0.0_AB_MSTR~DELL2`, and reads.
  - The signing key is read into memory only.
  - No IAM user, group or roster change. No other secret.
  - Rollback is the pair's: delete-secret with the DEFAULT recovery window (never force), and the ARN removed.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-84.svc-custody-mint.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 43 (round 41), cell `DB-b-84`.
<owned_cells>DB-b-84</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB41-1-AC1, DB41-1-AC2, DB41-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~DB2/IRPT_DASHBD.TO-DB-b-84.svc-custody-mint.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB41-1-AC1,DB41-1-AC2,DB41-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the before-read, the claims, the secret ARN, the reader grant's laptop answer and simulations, and the ledger path, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the pair IS the blast-radius read: one secret, one allow-list ARN (laptop act), no IAM user/group/roster change; the code admission (IB-pr-385) is the real control.
comp-iam: RUN -- the reader grant is one ARN on dell2's existing GetSecretValue allow-list, simulated allowed/implicitDeny after the laptop applies it.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes; the route is IRPT_BCKEND's, already live.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: a one-off act; no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB41-1-AC1/AC2/AC3 FAIL at base (no record). Pair: COO @a319fc74b8, CTO msg 2440; preconditions live (IB-pr-390 07:49Z, 6b tdpterTM 09:32Z).
lane: the <paths> block IS the grant.
</preflight>
