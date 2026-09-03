# TO NFRA_OPSEC202609.TO-OP-S-10B -- TEACH BOTH JWT CONSUMERS A SECOND SLOT **AND** GIVE THE AUTHORIZER A TTL: the remedy row Z-S100 named, without which FWD-10 cannot be served at all -- and the pattern to copy is ALREADY DEPLOYED in the same file tree, for the origin secret (OP-s-10, FWD-10)

<to_id>NFRA_OPSEC202609.TO-OP-S-10B</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

**BLOCKER: NONE. GO immediately** -- this is the remedy `TO-OP-S-10`'s gate produced, addressed to the same lane because it already holds every source read this face needs.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT **FWD-10**) - **Decomp cell:** `OP-s-10` (the enabling limb; v0.1.14) - **Lane:** the two consumer sources, AE lane - **Round:** 3.

---

## WHY THIS FACE EXISTS

`TO-OP-S-10`'s deliverable 1 was a gate and **its negative branch fired**. Row Z-S100, confirmed on THREE planes -- source at `998c79b970`, the DEPLOYED bundles, and the secret itself (a bare 452-char PEM with exactly one BEGIN block):

- **`auth-validator-edge`** holds ONE scalar -- `index.mjs:68` `cachedPublicKey`, exactly one `jwt.verify` at `:235` -- **with a 300 s TTL at `:231`.**
- **`opal-portal-authorizer`** holds ONE scalar -- `index.mjs:20` `publicKey`, exactly one `jwt.verify` at `:198` -- **with NO TTL AT ALL.** `getPublicKey()` at `:25-28` is `if (publicKey) return publicKey;`.

> ⛔ **THE SECOND DEFECT IS WORSE THAN THE FIRST AND IT IS WHY THIS FACE HAS TWO DELIVERABLES.** A second slot alone does not fix the authorizer. **Its cache never expires, so a warm execution environment holds the pre-rotation key for the life of that environment, and Lambda does not bound that lifetime.** `S10-AC2`'s *"wait for both consumers to be serving the new key"* is therefore **UNSATISFIABLE AT ANY WAIT LENGTH** for that consumer as written -- **you cannot wait out a cache that never expires.** The only convergence mechanism available today is a redeploy that cycles the environments, which is not a rotation property, it is an accident.

**AND THE PATTERN IS ALREADY WRITTEN, IN THE SAME AUTHORIZER, FOR THE ORIGIN SECRET.** `TO-OP-S-3` deployed a two-slot current-or-previous read with a TTL, and `TO-OP-S-1` limb 2a extracted it into a shared module. **Read that module and copy its shape.** Its own docstring states the mechanism. **Do not invent a second pattern beside it** -- one estate, one two-slot idiom.

## DELIVERABLE

1. **TWO SLOTS ON BOTH CONSUMERS.** Each must verify against **current OR previous** and accept a token signed by either. **Copy the origin-secret module's shape**; if it can be reused directly rather than duplicated, reuse it and say so -- a second copy of a two-slot read is the thing `TO-OP-S-1` refused for exactly this reason.
2. **A TTL ON `opal-portal-authorizer`'s KEY CACHE.** State the value you chose and why. **`auth-validator-edge`'s existing 300 s is the obvious precedent; matching it is defensible and diverging from it needs a sentence.**
3. **DEMONSTRATE CONVERGENCE, which is the whole point and is not the same as demonstrating the code.** Show a warm environment picking up a changed key **without a redeploy**, within the stated TTL. **A redeploy-and-it-works proof does NOT establish this** -- a redeploy cycles the environment and would have "worked" before this face existed.
4. **NOTHING IS ROTATED IN THIS FACE.** No new keypair, no signing switch, no secret write. **This face makes rotation POSSIBLE; `TO-OP-S-10` performs it afterwards.** A rotation attempted here is a STOP.
5. **THE NINE DATA ROUTES AND THE LOGIN PATH MUST STILL WORK AFTER EACH DEPLOY.** The authorizer guards 69 of 72 routes on the HTTP API; the edge fronts the portal. **Re-probe both after deploying, before calling either done.**
6. **A deploy-ledger entry per consumer** (`safe-apply` where Terraform is involved, never bare), opened before and closed after, rollback named -- **and the `CodeSha256` supersession recorded against `TO-OP-S-3`'s filed proof at `S3-AC3` with both values ISO-vintaged**, plus the build manifest's `artifact_sha256` which the build script writes and you commit.
7. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10B.two-slot-and-ttl-for-the-jwt-consumers.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

**BROKER DRAIN IMMEDIATELY BEFORE EACH DEPLOY.** Both consumers are on live paths and the halt gate cannot see a lane inbox.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S10B-AC1" cell_refs="OP-s-10"/> `S10B-AC1` -- BOTH CONSUMERS HOLD TWO SLOTS, AT SOURCE AND ON THE WIRE: the changed selection quoted per consumer with `file:line @ <commit-ish>`, **and** a token signed by the PREVIOUS key accepted by each while a token signed by the CURRENT key is also accepted. **Denominator 2 of 2 consumers.** **NEGATIVE CONTROL: a token signed by a key in NEITHER slot is REFUSED by each** -- without it the pair only shows the path accepts everything.
<criterion id="S10B-AC2" cell_refs="OP-s-10"/> `S10B-AC2` -- THE AUTHORIZER'S CACHE EXPIRES, DEMONSTRATED BY CONVERGENCE WITHOUT A REDEPLOY: a warm environment observed serving key A, the slot changed, and the SAME warm environment observed serving key B **within the stated TTL and with no deployment in between**. **A redeploy in the middle voids this criterion** -- it is the mechanism that already existed and is exactly what the row says is not a rotation property. If a warm environment cannot be held across the window, file `UNCOMPUTABLE` with the method attempted rather than substituting a redeploy.
<criterion id="S10B-AC3" cell_refs="OP-s-10"/> `S10B-AC3` -- NO SECOND COPY OF THE TWO-SLOT READ WAS CREATED: a census of the two-slot read across the tree with its denominator, showing the shared module reused rather than duplicated, or a stated reason it could not be. **A second copy is the drift surface `TO-OP-S-1` refused and the refusal stands here.**
<criterion id="S10B-AC4" cell_refs="OP-s-10"/> `S10B-AC4` -- NOTHING WAS ROTATED: `describe-secret` on both `opal/auth/jwt-private-key` and `-public-key` showing the version count and `LastChangedDate` **unchanged** from this face's cut, and a statement that no signing switch occurred. **This face makes rotation possible and does not perform it.**
<criterion id="S10B-AC5" cell_refs="OP-s-10"/> `S10B-AC5` -- THE LIVE PATHS STILL SERVE, AND THE LEDGERS CLOSE ON ARTIFACTS: the nine HTTP-API data routes re-probed after the authorizer deploy with the 403-direct / 200-through-CloudFront discriminator, and the portal login path exercised after the edge deploy; ledgers CLOSED with proofs and rollbacks; the `CodeSha256` supersession recorded against `TO-OP-S-3`'s `S3-AC3` with both values ISO-vintaged; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED.

<expected_criteria>S10B-AC1, S10B-AC2, S10B-AC3, S10B-AC4, S10B-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.14), cell `OP-s-10` (manifest S10; FWD-10) -- **the ENABLING limb.** `TO-OP-S-10` holds the rotation itself and is blocked until this lands.
<owned_cells>OP-s-10</owned_cells>
Read-dependencies, NOT claimed: `OP-s-3` (COMPLETE -- the two-slot origin-secret pattern to copy), `OP-s-1` (COMPLETE -- limb 2a extracted that read into a shared module and refused a second copy), `OP-s-2` (COMPLETE -- the nine routes `S10B-AC5` re-probes).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). The DEPLOY-LEDGER carrier binds: both deploys are ledgered acts on live auth paths.
comp-iam: DECLARED-NOT-APPLICABLE -- this face creates no role and attaches no policy; both consumers already read the secret they will read. Whether each can read the PREVIOUS slot is verified on the wire by S10B-AC1 rather than by a policy-document lens.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF (S10B-AC1).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S10B-AC1`, `S10B-AC2`, `S10B-AC3`, `S10B-AC4`, `S10B-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10B.two-slot-and-ttl-for-the-jwt-consumers.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S10B-AC1,S10B-AC2,S10B-AC3,S10B-AC4,S10B-AC5"` BEFORE the complete flip. **`S10B-AC2` is the control that must be able to fail: a redeploy anywhere in that window voids it, because a redeploy is the mechanism that already existed.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Read the shared two-slot module `TO-OP-S-1` limb 2a extracted, and decide reuse-versus-copy on its actual shape. Re-read both consumers at HEAD -- Z-S100's line numbers are at `998c79b970` and another seat may have moved them.</phase>
  <phase id="2" when="before each deploy">A broker drain, the ledger opened, the rollback named, and the live-path probe baseline captured BEFORE the deploy so the after-read has something to compare against.</phase>
  <phase id="3" when="after each deploy">The live paths re-probed before moving to the second consumer. A broken authorizer denies everything, so a refusal alone does not distinguish healthy from broken -- use an identity source and read the invocation.</phase>
</compiler_tools_mandate>
