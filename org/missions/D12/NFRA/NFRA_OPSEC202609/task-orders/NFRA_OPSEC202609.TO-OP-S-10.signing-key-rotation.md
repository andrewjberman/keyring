# TO NFRA_OPSEC202609.TO-OP-S-10 -- THE LOGIN SIGNING KEYS CAN BE REPLACED WITHOUT SIGNING EVERYONE OUT: prove the two-slot overlap works across BOTH consumers by actually rotating, and leave the estate able to do it again (OP-s-10, FWD-10)

<to_id>NFRA_OPSEC202609.TO-OP-S-10</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT **FWD-10** :130 -- *"The keys that sign logins can be replaced without signing everyone out"*; s.8 row S10) - **Decomp cell:** `OP-s-10` (v0.1.10 @2fd3843047, s.1a) - **Lane:** AE lane - **Round:** 3 of NFRA_OPSEC202609. **Dispatch:** GO after `TO-OP-S-7` goes terminal -- one task order at a time.

---

## READ LIVE AT THIS CUT BY THE ISSUER (2026-09-03 19:2xZ; re-ground in phase 1 and STOP on any difference)

- **`opal/auth/jwt-private-key`** -- created `2026-01-03`, **`LastChangedDate 2026-04-06T17:31:00Z`**, **`RotationEnabled: null`** (no rotation configured). ⛔ **CORRECTED 2026-09-03 23:2xZ on row Z-S100: this face rendered it `13:31:00Z` and the API returns `13:31:00.251000-04:00`. Same wall clock, WRONG DECLARED ZONE -- the true instant is FOUR HOURS from what a reader takes the `Z` to mean. The issuer typed a literal `Z` onto a local timestamp**, which is the trap CLAUDE.md Rule 22a names in terms. The secret has NOT changed since the cut (one version, one stage, no `AWSPREVIOUS`), so this is citation hygiene and not a re-ground failure.

⛔ **THIS FACE IS BLOCKED ON `TO-OP-S-10B` AND ITS GATE HAS ALREADY FIRED.** Deliverable 1's negative branch is the measured outcome: **BOTH consumers are single-slot** (row Z-S100, confirmed on three planes), so deliverable 2 is unreachable without a prior code change. **`TO-OP-S-10B` is that change** -- two slots on both consumers AND a TTL on the authorizer, whose cache currently never expires. **Do not attempt the rotation until that face is terminal.**
- **`opal/auth/jwt-public-key`** -- created `2026-01-03`, `LastChangedDate 2026-04-06T13:31:00Z`, `RotationEnabled: null`.
- **So the signing keypair is ~5 months old and has never been rotated by any automated path.** That is `OP-s-10`'s subject.
- **TWO consumers, and both must survive the rotation:** `auth-validator-edge` (the CloudFront edge) and the API authorizer. **A rotation that satisfies one and breaks the other is the failure mode this face exists to prevent**, and the edge is the one that is easy to forget because it is replicated.

> ⛔ **THIS FACE ROTATES A LIVE SIGNING KEY ON A PRODUCTION LOGIN PATH.** Every session in flight is signed by the current key. **The DONE WHEN is explicitly that nobody is signed out**, so the overlap is not a nicety, it is the deliverable. **A rotation that works but logs everyone out is a FAIL, not a partial pass.**

## DELIVERABLE

1. **ESTABLISH THE TWO-SLOT OVERLAP BEFORE ROTATING ANYTHING.** Determine and state how each consumer selects a verification key today -- read the source of both, cited `file:line @ <commit-ish>`. **If either consumer can only hold ONE key at a time, then a no-sign-out rotation is impossible as the system stands, and THAT is the finding**: file a row, state it as the blocker, and the remedy (teaching that consumer a second slot) is a separate cut. **Do not rotate into a single-slot consumer.**
2. **IF BOTH CONSUMERS CAN HOLD TWO KEYS: rotate for real, with the overlap.** Mint the new keypair, publish it as the second verification slot, wait for both consumers to be serving it, THEN switch signing to the new key, and only after that retire the old verification slot. **State the wait between each step and how you confirmed each consumer had picked up the change** -- the edge is replicated and "deployed" is not "serving".
3. **THE SESSION-SURVIVAL EVIDENCE IS THE POINT.** A token minted under the OLD key BEFORE the rotation must still verify AFTER the signing switch, for as long as the overlap is meant to last. **Capture that token's identity and its expiry, and re-present it at each step.** This is the FWD-10 DONE WHEN made testable.
4. **LEAVE THE ESTATE ABLE TO DO IT AGAIN.** A short runbook committed beside the work naming the steps, the wait at each, the two consumers, and the read that confirms each is serving the new slot. **Do NOT configure Secrets Manager automatic rotation** -- a rotation that fires unattended on a login path is a bigger change than this outcome asks for, and it is not in the endpoint. If you think it is warranted, that is a row and a recommendation.
5. **A deploy-ledger entry** (`safe-apply` where Terraform is involved, never bare), opened before and closed after, **with the rollback named BEFORE the first act: the old key material must remain retrievable until the ledger closes.** ⛔ **Never schedule deletion of the old secret version inside this face.**
6. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10.signing-key-rotation.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

**BROKER DRAIN IMMEDIATELY BEFORE THE SIGNING SWITCH.** It is the irreversible step on a live login path.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S10-AC1" cell_refs="OP-s-10"/> `S10-AC1` -- BOTH CONSUMERS' KEY-SELECTION IS READ AT SOURCE, NOT ASSUMED: for `auth-validator-edge` and for the API authorizer, the code that chooses a verification key quoted with `file:line @ <commit-ish>`, and an explicit statement of how many keys each can hold. **Denominator: 2 of 2 consumers read.** A face that rotates having read one is the failure this criterion exists to catch.
<criterion id="S10-AC2" cell_refs="OP-s-10"/> `S10-AC2` -- THE OVERLAP EXISTS BEFORE THE SWITCH, MEASURED AT EACH CONSUMER: evidence that BOTH consumers were serving the new verification key BEFORE signing moved to it, each read separately with its timestamp. **"Deployed" is not "serving"** -- for the replicated edge, the read must be against what is actually answering.
<criterion id="S10-AC3" cell_refs="OP-s-10"/> `S10-AC3` -- NOBODY WAS SIGNED OUT, AND THIS IS THE OUTCOME'S OWN BAR: a token minted under the OLD key before the rotation, presented AFTER the signing switch, still verifies -- request, response and the token's identity and expiry pasted at each step. **NEGATIVE CONTROL: a token signed by a key that was never in either slot is REFUSED**, so the acceptance is not measuring "everything passes".
<criterion id="S10-AC4" cell_refs="OP-s-10"/> `S10-AC4` -- THE NEW KEY IS ACTUALLY THE ONE SIGNING: a login performed after the switch yields a token whose header/key-id resolves to the NEW key, pasted; and the old key is confirmed still present as a verification slot at that moment. **A rotation nobody can observe on the wire has not been demonstrated.**
<criterion id="S10-AC5" cell_refs="OP-s-10"/> `S10-AC5` -- THE OLD MATERIAL SURVIVES AND THE LEDGER CLOSES ON THE ARTIFACT: the old secret version confirmed still retrievable with NO scheduled deletion (`describe-secret` pasted showing no `DeletedDate`); the runbook committed; the ledger CLOSED with its proof and rollback named; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED. **`RotationEnabled` is confirmed still unset** -- this face does not turn on automatic rotation.

<expected_criteria>S10-AC1, S10-AC2, S10-AC3, S10-AC4, S10-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @2fd3843047 (v0.1.10), cell `OP-s-10` (manifest S10; FWD-10; value EXERCISED).
<owned_cells>OP-s-10</owned_cells>
Read-dependencies, NOT claimed: `OP-s-2` (COMPLETE -- the HTTP API authorizer is one of the two consumers), `OP-s-3` (COMPLETE -- the origin secret's two-slot overlap is the pattern this rotation follows and is worth reading before designing this one).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED **20** over 5 carriers AT THAT VINTAGE (C1 SENTINEL 20 lines -> **4** gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). The DEPLOY-LEDGER carrier binds: this face's signing switch is a ledgered act and its rollback must be named before it runs. ⛔ **CORRECTED 2026-09-04 08:4xZ BY `1.0.0_SA_CTO~Z` (msg 20364): the tool prints 21 lines -> 5 gates because it counts a LOG QUOTING a sentinel as a gate -- `org/tier1_exec/3.0.0_SA_CVO/logs/2026-09-01/work_0312Z_comp_schedule_gate_ledger_build.md:72`. **A `.md` CANNOT gate a deploy**: `safe_deploy_core` matches that grammar against the files it is about to SHIP. The other 20 lines are authoritative deployable source. ⛔⛔ **DO NOT "CONFIRM" THIS BY RE-RUNNING `comp-schedule` -- A FRESH RUN TONIGHT ALSO PRINTS 21, BY A DIFFERENT ROUTE:** C2 DEPLOY-LEDGER has moved 4 -> 5 since this preflight, so corrected C1 4 + current C2 5 + C3 12 = 21 again. **The same total from different components would read as confirmation and would be nothing of the kind.** ⭐ The correction is trusted because it imports `comp-schedule`'s OWN `SERVE_HELD_RE` and `_full_reason` over the tool's own scope and REPRODUCES 21/5 as a control BEFORE removing the quotation -- a census that could not first reproduce the figure it corrects would not be evidence. **This figure is ORIENTATION at its stated vintage, never a criterion, and no face in this project discharges a gate.**
comp-iam: DECLARED-NOT-APPLICABLE at cut -- this face creates no role and attaches no policy; it rotates secret MATERIAL that existing principals already read. Whether each consumer can READ the new slot is verified on the APPLIED plane by S10-AC2's per-consumer serving read, which is stronger than a policy-document lens.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF (S10-AC1), which is where the vintage discipline binds.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S10-AC1`, `S10-AC2`, `S10-AC3`, `S10-AC4`, `S10-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10.signing-key-rotation.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S10-AC1,S10-AC2,S10-AC3,S10-AC4,S10-AC5"` BEFORE the complete flip. **The control that must be able to FAIL is `S10-AC3`'s negative control: a token signed by a never-installed key must be REFUSED, or the survival evidence only shows that the path accepts everything.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-read both secrets' metadata and BOTH consumers' key-selection source at HEAD. If either consumer is single-slot, STOP at deliverable 1 and file the row -- do not proceed to deliverable 2.</phase>
  <phase id="2" when="before the signing switch">A broker drain, the ledger opened, the rollback named, and the old-key token minted and captured FIRST -- it cannot be produced after the switch.</phase>
  <phase id="3" when="after the switch">Both consumers re-read on the serving plane, the old-key token re-presented, and the ledger closed on the artifact rather than on an apply's rc.</phase>
</compiler_tools_mandate>
