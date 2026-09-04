# TO NFRA_OPSEC202609.TO-OP-S-9-11 -- THE LEGACY USER TABLE AND ITS TWO GRANTS LEAVE TOGETHER, AND A REFRESH TOKEN STOPS BEING BOUND TO AN EMAIL ADDRESS: `opal-users` retired under Rule 9 with the DELETE itself held for a human word, and `sub` re-bound so re-creating an account on the same address cannot resurrect a live session (OP-s-9 + OP-s-11, FWD-9 + FWD-11)

<to_id>NFRA_OPSEC202609.TO-OP-S-9-11</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~X</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>

✅ **BLOCKER CLEARED 2026-09-03 23:4xZ ON ROW Z-S103 -- AND THE BLOCKER I ORIGINALLY WROTE WAS WRONG.** This face said the GO condition was `OP-s-8` reaching DONE, because PRD s.9 item 5 sequences S9 after S8 and the CMK limb is open. **`0.7.0_AE_CloudOps~W` read the decomposition's actual EDGE and it carries a PREDICATE, not a cell state:** `OP-s-8 --[DP + PITR read ON per table]--> OP-s-9 (snapshot-then-delete), OP-s-11` (s.4, line 135). **MEASURED AT THE ISSUER'S SEAT: `DeletionProtectionEnabled` TRUE and PITR `ENABLED` on 5 of 5 tables** -- `opal-users-v2`, `opal-partner-49financial`, `opal-partner-cottonwood`, `opal-partner-inflection`, `opal-partner-demo`. **The predicate is satisfied and this face is dispatchable now; the CMK alignment is a different limb and does not gate it.**

> **THE ISSUER'S ERROR, recorded because it cost this face hours:** I read the cell's prose `depends_on` ("OP-s-8") as requiring the whole cell DONE, when the decomposition states the actual condition ON THE EDGE and it was already true. **A dependency written as a cell name reads as "wait for everything"; the same dependency written as a predicate can be checked.** The edge was right and my reading of it was lazy.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT FWD-9, FWD-11; s.8 rows S9 and S11; s.9 item 5) - **Decomp cells:** `OP-s-9` + `OP-s-11` (v0.1.11, s.1a) - **Lane:** `infra/aws/terraform/portal-auth/iam.tf`, `auth-handler/src/auth.ts` (+ `jwt.ts`), AE lane - **Round:** 3.

---

## WHY THESE TWO ARE ONE FACE

Both are identity-surface cleanups on the same auth handler, both are sequenced behind `OP-s-8`, and both are EXERCISED-value cells whose proof needs a fixture account. **One fixture, one probe window, two outcomes.** They are otherwise independent and either may file its criteria without the other.

## OP-s-9 -- THE LEGACY TABLE, AND THE DELETE IS NOT YOURS TO TAKE UNASKED

The cell: `opal-users`, **12 rows, no live reader**, plus the auth-handler grant on it **AND on a us-east-2 copy** (`iam.tf:50-51`). The cell's `closes on` is *"snapshot-then-delete; the grant AND the us-east-2 ARN leave in the same TO; a fixture login before and after with the same result; the reader census re-run at the worker's vintage BEFORE the delete."*

> ⛔ **CLAUDE.md RESERVES DROPPING TABLES FOR HUMAN CONFIRMATION, AND THIS FACE DOES NOT OVERRIDE THAT.** Build the entire retirement -- snapshot, parity, absence proof, grant removal -- and then **STOP at the table deletion itself.** File a row stating the retirement is ready with its evidence, message the issuer, and **leave the table in place.** The delete lands only on an explicit human word, relayed to you in writing. **A table you deleted because a task order said "then delete" is a table nobody chose to delete.**

**The absence proof is the load-bearing half and it must be able to fail.** *"No live reader"* is a claim about the present derived from a search; a search that missed a reader returns the same clean result as a genuine absence. **Re-run the reader census at your own vintage across code AND live IAM AND CloudTrail data-plane reads if available**, print the denominator, and name the instrument for each. **A census over one plane is not an absence.**

## OP-s-11 -- A REFRESH TOKEN MUST NOT BE BOUND TO AN EMAIL ADDRESS

The cell: refresh-token `sub` = email (finding F-10), so **delete + re-create on the same address re-binds a live refresh token.** The remedy: bind to `userId` or a per-row session id. **FWD-11's DONE WHEN: a deleted fixture account, re-created on the same email, does NOT resurrect the old session.**

**BOUNDARY, from the cell and not to be crossed:** this touches `USERMGMT`'s territory **only at the token claim.** State the boundary in the proof; do not reshape user management.

**MIGRATION IS THE RISK, not the code change.** Tokens already issued carry the old `sub`. **Say explicitly how in-flight refresh tokens are handled** -- accepted under the old shape for a stated window, or deliberately invalidated -- and **if the answer is "everyone is signed out", that is a STOP and a row**, because that is precisely the cost FWD-10 spends a whole outcome avoiding on the sibling surface.

## DELIVERABLE

1. **The reader census for `opal-users`, re-run at your vintage, multi-plane, with denominators.** Then the snapshot (on-demand backup or export, named and verified restorable-in-principle by reading its metadata, not by restoring).
2. **Remove the auth-handler grant AND the us-east-2 ARN in the SAME change** (`iam.tf:50-51`). The cell requires they leave together.
3. **A fixture login before and after the grant removal, with the SAME result** -- the discriminator that the grant was genuinely unused.
4. **STOP before the table delete.** Row + message + leave it standing.
5. **Re-bind the refresh token's `sub`** to `userId` or a per-row session id, with the in-flight-token handling stated.
6. **The delete/re-create probe under `OP-x-1`:** a fixture account deleted and re-created on the same email; the old refresh token must NOT work.
7. **A deploy-ledger entry** per applied change (`safe-apply` where Terraform is involved, never bare), rollback named before each act.
8. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-9-11.legacy-users-and-token-binding.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S9-AC1" cell_refs="OP-s-9"/> `S9-AC1` -- THE ABSENCE OF READERS IS PROVEN ON MORE THAN ONE PLANE, WITH DENOMINATORS: a source census, an IAM census of principals granted on the table, and a live-access read if one is obtainable -- each with its instrument named and its denominator printed, and each stating what it CANNOT see. **A single-plane clean read files `UNCOMPUTABLE`, not PASS.**
<criterion id="S9-AC2" cell_refs="OP-s-9"/> `S9-AC2` -- THE SNAPSHOT EXISTS AND IS DESCRIBED: the backup/export identifier, its size or item count against the table's **12 rows**, and its retention, pasted from a live read.
<criterion id="S9-AC3" cell_refs="OP-s-9"/> `S9-AC3` -- BOTH GRANTS ARE GONE AND LOGIN IS UNAFFECTED: `iam.tf` diff showing the table grant and the us-east-2 ARN both removed; the applied policy re-read confirming their absence; and a fixture login **before and after** returning the same result, both pasted. **The before is what makes the after mean anything.**
⛔ **AMENDED 2026-09-04 01:1xZ BY THE ISSUER ON ROW Z-S112, AND THE AMENDMENT WIDENS THE EVIDENCE WITHOUT WIDENING THE ACT.** `0.7.0_AE_CloudOps~X` measured the live grant population on `table/opal-users` and it is **THREE statements across TWO roles in TWO terraform roots**, not the two-ARNs-on-one-role this face assumed. **Removing `portal-auth/iam.tf:50-51` does NOT leave the table ungranted.** So this criterion additionally requires: **the FULL live grant population enumerated with its denominator and its instrument, and every surviving grant NAMED as a residual** -- at minimum `trade-submission-lambda-role` (`infra/aws/terraform/trade-pipeline/iam.tf:63-64`, the execution role of seven live lambdas). ⛔ **THE REMOVAL SCOPE IS UNCHANGED: this face removes `:50-51` and NOTHING ELSE**; the trade grant is `TO-OP-S-9C`'s separate cut. **WHY THE AMENDMENT IS NOT OPTIONAL: without it a check scoped to the portal root would certify the table exclusively granted while a second root holds full CRUD on it, and every arm of that check would pass.** A residual named in the proof is honest; an exclusivity claim scoped to one root is not.
<criterion id="S9-AC4" cell_refs="OP-s-9"/> `S9-AC4` -- THE TABLE IS STILL THERE AND THE DECISION IS PARKED WITH A HUMAN: `describe-table` showing `opal-users` present, plus the row id and the message in which the retirement was offered for a human word. **Deleting the table in this face is a FAIL regardless of how good the evidence is.**
<criterion id="S11-AC1" cell_refs="OP-s-11"/> `S11-AC1` -- THE BINDING CHANGED AT SOURCE AND THE OLD SHAPE IS NAMED: the claim construction quoted before and after with `file:line @ <commit-ish>`, showing `sub` no longer carries the email, and the new binding's identifier named.
<criterion id="S11-AC2" cell_refs="OP-s-11"/> `S11-AC2` -- RE-CREATION DOES NOT RESURRECT THE SESSION, WHICH IS FWD-11's OWN BAR: a fixture account's refresh token captured; the account deleted and re-created on the SAME email; the old refresh token presented and **REFUSED**, with request and response pasted. **POSITIVE CONTROL: the same token worked before the delete**, or the refusal proves nothing.
<criterion id="S11-AC3" cell_refs="OP-s-11"/> `S11-AC3` -- IN-FLIGHT TOKENS ARE ACCOUNTED FOR: a stated handling for tokens issued under the old shape, with evidence for whichever path was taken. **If the change signs everyone out, this criterion FAILS and the row explains why** -- that outcome needs a decision, not an acceptance.
<criterion id="S911-AC4" cell_refs="OP-s-9,OP-s-11"/> `S911-AC4` -- BASELINE QUOTED, 0-DIFF AFTER, NOTHING ELSE RODE: per applied root, the UNSCOPED plan before, the changed-resource list enumerated with its count, the UNSCOPED re-plan 0-diff after, ledgers CLOSED with proofs and rollbacks, push state read by `ls-remote` + `is-ancestor` and stated as MEASURED.

<expected_criteria>S9-AC1, S9-AC2, S9-AC3, S9-AC4, S11-AC1, S11-AC2, S11-AC3, S911-AC4</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cells `OP-s-9` (manifest S9; FWD-9) and `OP-s-11` (manifest S11; FWD-11), both EXERCISED.
<owned_cells>OP-s-9,OP-s-11</owned_cells>
Read-dependencies, NOT claimed: `OP-s-8` (the GO condition), `OP-x-1` (the probe verdict authorising the fixture delete/re-create), `OP-s-10` (the sibling token surface -- read its overlap pattern before choosing S11-AC3's handling).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED **20** over 5 carriers AT THAT VINTAGE (C1 SENTINEL 20 lines -> **4** gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). Nothing in this face builds a monitor; the retirement's STOP is a human gate that already exists in CLAUDE.md and is not an agent-made one. ⛔ **CORRECTED 2026-09-04 08:4xZ BY `1.0.0_SA_CTO~Z` (msg 20364): the tool prints 21 lines -> 5 gates because it counts a LOG QUOTING a sentinel as a gate -- `org/tier1_exec/3.0.0_SA_CVO/logs/2026-09-01/work_0312Z_comp_schedule_gate_ledger_build.md:72`. **A `.md` CANNOT gate a deploy**: `safe_deploy_core` matches that grammar against the files it is about to SHIP. The other 20 lines are authoritative deployable source. ⛔⛔ **DO NOT "CONFIRM" THIS BY RE-RUNNING `comp-schedule` -- A FRESH RUN TONIGHT ALSO PRINTS 21, BY A DIFFERENT ROUTE:** C2 DEPLOY-LEDGER has moved 4 -> 5 since this preflight, so corrected C1 4 + current C2 5 + C3 12 = 21 again. **The same total from different components would read as confirmation and would be nothing of the kind.** ⭐ The correction is trusted because it imports `comp-schedule`'s OWN `SERVE_HELD_RE` and `_full_reason` over the tool's own scope and REPRODUCES 21/5 as a control BEFORE removing the quotation -- a census that could not first reproduce the figure it corrects would not be evidence. **This figure is ORIENTATION at its stated vintage, never a criterion, and no face in this project discharges a gate.**
comp-iam: RUN REQUIRED BY THE ASSIGNEE IN PHASE 1 -- this is the one face in round 3 where the IAM lens is on-point: the grant removal at `iam.tf:50-51` is an IAM identity-policy change, and `comp-iam` reconciles the DESIRED tree against live. Run it, print its denominators, and state what it cannot see -- it is a DESIRED-plane lens and S9-AC1's absence proof must not rest on it alone.
comp-adversary: DECLARED-NOT-APPLICABLE at cut -- this face pins no commit-scoped claim; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF (S11-AC1).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S9-AC1`, `S9-AC2`, `S9-AC3`, `S9-AC4`, `S11-AC1`, `S11-AC2`, `S11-AC3`, `S911-AC4`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-9-11.legacy-users-and-token-binding.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S9-AC1,S9-AC2,S9-AC3,S11-AC1,S11-AC2,S11-AC3,S9-AC4,S911-AC4"` BEFORE the complete flip. **The controls that must be able to FAIL: `S11-AC2`'s positive control (the token worked before the delete) and `S9-AC3`'s before-login.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Confirm `OP-s-8` is DONE. Re-run the reader census at your vintage on every plane you can reach. Re-read `iam.tf:50-51` and the claim construction at HEAD.</phase>
  <phase id="2" when="before each apply">A broker drain, the unscoped baseline, the ledger opened, the rollback named. The fixture's old refresh token captured BEFORE anything changes -- it cannot be produced afterwards.</phase>
  <phase id="3" when="after each apply">The unscoped re-plan, the applied-plane re-read, the ledger closed on the artifact. The table left standing.</phase>
</compiler_tools_mandate>
