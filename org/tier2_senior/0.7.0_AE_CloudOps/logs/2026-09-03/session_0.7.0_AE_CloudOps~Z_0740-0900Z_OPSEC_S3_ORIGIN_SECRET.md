# Session log -- `0.7.0_AE_CloudOps~Z` -- 2026-09-03 0740-0900Z

**Archetype:** BUILD (L7 worker, one cell, deployed and verified)
**Project:** `NFRA_OPSEC202609` (D12, site-z fabric) -- **TO:** `NFRA_OPSEC202609.TO-OP-S-3` (cell `OP-s-3`, round 1)
**Issuer:** `2.0.0_SA_COO~Z` (GO msg 19488)

---

## Current State

**TO-OP-S-3 is COMPLETE on its APPLIED half and IN-FLIGHT on one held criterion.** A request that did
not enter through CloudFront is now refused by both HTTP-API consumers even when it carries a valid
login. Proof-of-spec instance **VALID rc=0** (checker-vintage `c765283365`), 5 of 6 criteria PASS,
S3-AC5 `UNCOMPUTABLE-BY-CONSTRUCTION` with `status_reason` "OP-x-1 HELD at Andrew" exactly as the face
prescribes. Deploy ledger `opsec-s3-origin-secret-both-gateways` **CLOSED, 6 of 6 legs proven**,
sentinel removed.

Landed at `7abe7552b5` (10 files, 687 insertions). **Push state: LOCAL** -- not an ancestor of
origin/SITEZ, the expected reading under LD-0367 / GATE 5.

## What was built

One secret, two consumers, per the face.

- `opal/auth/origin-verify` (`...origin-verify-Pe97BM`) -- Secrets Manager **container only**, the
  module's jwt-keypair pattern; value minted OUT OF BAND and never authored in Terraform.
- `X-Opal-Origin-Verify` as a CloudFront **custom origin header** on the two gateway origins
  (`APIGateway-portal` / `7k3ed8px20`, `APIGateway-portfolio` / `f61h681z9g`), value read from the
  secret at plan time.
- The check in **both** consumers: `originVerify.ts` + `index.ts:160-186` (auth handler, `/auth/*`,
  which is `NONE` at the API by design so the check has to live in our code) and `index.mjs:265-283`
  (portal authorizer, before token extraction).
- Rotation runbook, and the deploy-ledger entry.

## Decisions worth carrying

**A NEW header name, not the existing `X-Origin-Verify`.** The face offered either. The edge still
injects the constant `X-Origin-Verify: "cloudfront"` at `auth-validator-edge/index.mjs:392`, so
reusing the name would make correctness depend on CloudFront's custom-origin-header taking precedence
over a same-named header set by a viewer-request function. That precedence is real, but it would have
been **asserted here rather than measured**, and the failure mode if wrong is a full portal outage.
A distinct name removes the question entirely. `:392` is now inert and deliberately left alone --
removing it needs an edge deploy against gated Terraform with `ignore_changes` on the live association.

**Deploy ORDER, because the reverse is an outage.** Header onto the distribution first, confirmed
`Status=Deployed` (propagated to every edge), and only then the consumers that require it.

**The defect I found in my own first build.** The shipped-then-superseded pair cached the secret
UNBOUNDED. That silently breaks the rotation the two-slot design exists for: a container that cached
`{current: A}` before a rotation holds no knowledge of B, so the moment the header moves it 403s
everything it serves until recycled -- and Lambda does not bound container lifetime. **Without the fix
the runbook's central claim would have been false.** Both consumers now TTL at 300 s and the runbook's
step 2 waits 600 s before the header moves. Caught before the leg was closed, not after.

## Findings routed, not chased

- **`NFRA_OPSEC202609-Z-S2`** -- the origin-secret value rests in Terraform state by construction.
  Issuer DISARMED it 2026-09-03 (19500, design call (a) ACCEPT); deliverable 1's comment and the
  runbook's residual paragraph carry it.
- **`NFRA_OPSEC202609-Z-S10`** -- `cross-firm-secret-deny.tf:6-10` justifies its Deny belt on a
  `secret:opal/*` wildcard held by `opal-portal-lambda-role`. **That role holds no such wildcard
  today.** Had I trusted the comment I would have skipped the authorizer's grant and the authorizer
  would have failed CLOSED on every authorized route at deploy. The grant exists because the live
  primitive was measured instead. Disarm owner `1.0.0_SA_CTO~Z`; the Deny itself is correct, untouched.
- **Site-Z build defect, named as the face requires:** `build-nodejs-lambda.sh`'s `to_native_path`
  handles `/c/` only and throws "No source_dir found" from a `/cygdrive/c/` cwd. Both builds run from
  the `/c/` mount. Not fixed -- CI-script surface, not this cell's.

## An error of mine, disclosed

Commit `7abe7552b5` **also carried `3.0.0_SA_CVO~Z`'s 15-line correction bullet** at
`@@ -146,0 +147,15 @@` of the shared channel file, under my author line, and my commit message named
only my own row. `2.0.0_SA_COO~Z` warned about exactly this shape at 08:49Z (19564); my commit landed
at 08:47Z, before the note existed -- which is the timeline, not a defense: I staged a shared
lane-ANY file without classifying its hunks first. Substance is unharmed (the bullet's attribution is
in-band and names the CVO), the commit metadata is wrong, and history is not being rewritten for a
metadata field. Disclosed to both seats. Side effect worth stating plainly: the channel file is now
clean, so the CVO's own gated commit is unblocked.

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-read` | Located the `:5` import bound verbatim in QUALIFIERS; its UNREAD LEDGER (15 of 899 lines) is why the origin blocks were then read directly rather than concluded from the digest. |
| `comp-read --enumerate` | `custom_header` = 0 of 899 pre-change. Gateway ids WARNed as FRAGMENTS. My own `origin {` regex returned a **false zero** against a file full of origins -- caught only because the tool prints its denominator. |
| `comp-find` | 23 hits / 50,949 files re-grounded brief F1 at my vintage (zero consumers of the constant header). Also found `shared-infra/opal-portal-lambda-role.tf` and the Phase-A narrowing plan that falsified the belt file's premise. |
| `comp-routes` | 28 behaviors mapped. Used within its own stated bound -- it declares `auth_api_gw` is topology-inferred, so it renders `/api/private/portfolio*` as having an API-GW authorizer while that gateway has **zero**. F2/F4 grounded on the live plane under an audited `# rail-checked:` marker naming that gap. |
| `comp-blast` | Triggered a full kuzu_nessie rebuild and did not return in time. **NOT cited as evidence** -- the zero-consumer finding rests on the comp-find census, a different instrument. |
| `terraform show -json` | **The instrument that settled the cell.** The human renderer showed `custom_header` zero times and rendered all origins as `-> null` (TypeSet re-render), indistinguishable from the change being absent. The structured plan showed denominator 7, exactly 2 origins carrying the header, action `update`. |
| `safe-apply` / `deploy_ledger.py` / `safe-commit` | 3 applies, all through safe-apply; ledger opened before the first irreversible act and closed 6/6. The surprise-row gate **refused** my first row on three ratified-enum violations -- corrected, not overridden. |

## Next

1. **[`2.0.0_SA_COO~Z`]** Validate the instance and the deliverable report; sequence TO-OP-S-5.
2. **[Andrew, via OP-x-1]** S3-AC5's probe authorization. Until then the cell is IN-FLIGHT by design.
3. **[`0.7.0_AE_CloudOps~Z`]** TO-OP-S-5 (logging) activates on this complete flip; its S3 legs wait on
   `opal-data-security` from `0.7.0_AE_CloudOps~S` (TO-OP-S-17-16) -- **on that seat's artifact, never
   on a message**. That seat's row Z-S3 is BLOCKING/ARMED.
4. **[`1.0.0_SA_CTO~Z`]** Row Z-S10 (belt-file premise) and the state-bucket lifecycle finding.
