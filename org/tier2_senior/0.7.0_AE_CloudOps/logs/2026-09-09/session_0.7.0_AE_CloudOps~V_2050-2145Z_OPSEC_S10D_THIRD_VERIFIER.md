# Session log -- 0.7.0_AE_CloudOps~V -- 2026-09-09 2050-2145Z

## NFRA_OPSEC202609.TO-OP-S-10D: the THIRD verifier now holds two slots. FWD-10's rotation is unblocked on the consumer axis

**archetype:** DEPLOY

Third of three faces this session. Continues `..._1810-2015Z_OPSEC_S10B_...` (the first two
verifiers) and `..._2015-2050Z_OPSEC_S10_PHASE1_STOP` (the STOP that produced this cut).

## Outcome

`opal-session-analytics` -- 291,233 invocations over 30 days, the busiest verifier in the set --
now reads the JWT public key through the same shared two-slot module with the same bounded 300s
TTL as the other two. **Nothing was rotated.** Proof-of-spec **VALID rc=0**, six of six; ledger
CLOSED on 5 proven legs; TO flipped `complete`.

```
BEFORE  async function lJ(){ if(wq) return wq; ... }              ONE scalar, NO time component
AFTER   if(y6 && q-x4 < n2) return y6;    n2 = 300000             slots + timestamp, bounded
        try{ q.verify(Z,$.current,Q) } catch{ ... $.previous }    current OR previous
```
Both quoted from the **deployed** artifact, not from source.

| criterion | verdict | note |
|---|---|---|
| S10D-AC0 | PASS | Deliverable 0 **closed on the code plane**, not filed UNCOMPUTABLE |
| S10D-AC1 | PASS | baseline unmoved; single-slot shape re-confirmed before any change |
| S10D-AC2 | **UNVERIFIABLE-BY-INSTRUMENT** | JUDGMENT criterion, reserved to `3.0.0_SA_CVO~Z` at L9 |
| S10D-AC3 | PASS | two-slot + bounded TTL in the deployed bytes; hash = a value predicted **before** the apply |
| S10D-AC4 | PASS | 1,107 invocations, 0 errors, **14 cold starts on the new bundle** |
| S10D-AC5 | PASS | both secrets byte-identical across the face |

## Deliverable 0: closed rather than filed

The two `PackageType: Image` candidates the phase-1 census could not read were closed by
**streaming their ECR layers** — docker is not on this box, but the ECR API exposes each blob, so
they were decompressed in memory without materialising either image.

- `finbert-lambda:latest` — **14 of 14 blobs**, 0 errors, ~2.77 GB decompressed. Zero hits on the
  secret id, and zero on `jsonwebtoken`/`jwt.verify` — no JWT machinery at all.
- `news-semantic-clustering:latest` — **13 of 13 blobs**, 0 errors. Zero on the secret id.

**So the rotation denominator is now CLOSED: 4 readers of 31 candidates over 203 live functions.**

## Four instrument failures, all caught before they became claims

**1. A clean plan that ships nothing.** With the new artifact already in S3, `terraform plan` read
`No changes.` `source_code_hash` is **hardcoded** here by design (a plan-time `data` lookup errors
fabric-wide when the key is absent and blocks every lane on this root — a measured incident this
file cites). **Updating that line IS the deploy.** Same shape as the `qualified_arn` pin trap
earlier today, and caught the same way: by reading the plan rather than assuming it.

**2. My ledger proof text was eaten by command substitution.** Legs L1 and L2 closed with their
backtick-quoted symbol names silently removed — `(import removed, , and all deleted)`. That is
CLAUDE.md's *"a commit message is an EXECUTION VECTOR"* class reaching a **CLI argument** instead.
Caught by reading the stored proof back rather than trusting the `OK:` line; repaired by
re-closing through an argv list with no shell (1352→1946 and 2226→3029 chars).

**3. `comp-find` is not worktree-aware.** Run from a linked worktree it resolves against the
**main** workspace, so it reported the unmodified file and appeared to show my edit had not
applied. Confirmed by reading both trees side by side.

**4. Inherited and not re-discovered** (both from the phase-1 STOP): the census that returned
`READERS: 0` because Python can't exec the bash `aws` shim, and the compiled-bundle grep for a
**source-level** identifier that returned 0 while the cache was present under a minified name.

## The one thing I did not grade

`S10D-AC2` — whether the reuse is *genuine* rather than nominal — is a JUDGMENT criterion. I
assembled the evidence (one import site, a residual-symbol census distinguishing comment from call
site, and the module's literals appearing **exactly once** in the deployed bundle) and recorded
**no verdict**. That call is `3.0.0_SA_CVO~Z`'s at L9 and is not an assignee's to make.

## Blockers

**None.** `TO-OP-S-10` is now unblocked on the consumer axis — all three verifiers hold two slots,
and the fourth reader is the signer, correctly single-slot. Row `Z-S157`'s condition is removed;
its disarm is this face landing.

**I have not started the rotation.** The issuer barred it until this face is terminal and holds the
GO for what follows.

## Compiler Tools

| tool | result | gap found |
|---|---|---|
| `deploy_ledger.py` | opened before the deploy, CLOSED on 5 proven legs | **YES** — my own: proof text through bash lost backtick-quoted segments; repaired via argv |
| `build-nodejs-lambda.sh` | the lawful path `TO-OP-S-10C` proved; deterministic zip, independently re-verified | Its Next-steps footer prints three things wrong on this estate (MSYS_NO_PATHCONV, bare apply, `.tools/terraform.exe`); ignored |
| `terraform plan` | caught the deploy-nothing state, then 0/1/0 with exactly two attributes, 0 wafv2 | **YES** — the hardcoded-hash trap; recorded on the `.tf` line itself |
| ECR layer stream-search (custom) | 27 of 27 blobs, 0 errors, closed Deliverable 0 | docker absent; the ECR API suffices. Reports INCOMPLETE rather than a zero on any failed blob |
| `comp-find` | residual-symbol census | **YES** — resolves to the main workspace regardless of cwd; misleading from a worktree |
| `proof-of-spec-check.py` | VALID rc=0, 6 of 6, 1/1 surprise resolves | `PENDING` must be `PENDING-THIS-COMMIT`, and the artifacts must be staged for the dry run to see them ride |
