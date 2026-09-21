# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rth-1: `_authz/loaders.py::load_ownership` recognises
S3's AccessDenied existence-masking as an absent ownership map, the same as NoSuchKey

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-21 (post-reboot,
resumed round 8). **The act signed:** the apply IB-rth-1's arm (c)/(d) would perform and the live proof arm
(e) would then take, exactly as the packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rth-1.md`
describes it at HEAD, **blob `19389dc50b6e3bfb7436681328cb2721c9c11802`** (the worker's own report of the
committed blob; re-derive at signing: `git rev-parse HEAD:<path>`). A packet whose bytes differ from that
blob is NOT what this half signs. The CTO half is asked the same turn, by this blob.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches -- never the worker's intention.
**Independently re-verified this turn, not taken from the packet's own word:**
- committed `infra/aws/lambda/investor-reporting/_authz/loaders.py` at HEAD -- 9779 bytes, sha256
  `0c086052e6e65d2cb411f15362862b1656bad0b2320f9756be6a32444b665765` -- **matches the packet's claim exactly**
  (`python -c "hashlib.sha256(open(...,'rb').read())"`, this turn).
- the "7 of 7 serving functions, 2 of 9 non-serving" blast-radius claim -- re-derived from
  `infra/aws/lambda/ci/lambda-source-map.json` `functions{}` (216 total functions in the map; 9 `irpt-*`
  prefixed; exactly 7 -- `irpt-directory-search`, `irpt-export-render`, `irpt-holdings`, `irpt-narrative`,
  `irpt-performance-adapter`, `irpt-status`, `irpt-ycharts-generate` -- carry `loaders.py` in `files[]`; the
  2 that do not are `irpt-intake-poller` and `irpt-directory-refresh`, neither a serving function). **Exact
  match to the packet.**
- the "GetObject-only, object-scoped, no ListBucket" grant shape that makes this fix narrow -- re-derived on
  TWO instruments: `comp-iam service irpt-performance-adapter` (live role, 3 statements: 1 logs, 2 both
  `s3:GetObject` only, no `s3:ListBucket` anywhere) AND the Terraform source
  (`infra/aws/terraform/investor-reporting/performance/iam.tf:65-96` -- `aws_iam_role_policy.
  performance_adapter_ownership_map`, `Action = ["s3:GetObject"]`, `Resource =
  local.ownership_map_object_arns` = one ARN per client firm, `platinum/${firm_id}/ownership_map.json`;
  comment at :65-66 states the design intent verbatim: "ONE OBJECT per client firm, GetObject only ...
  never ListBucket"). **Both instruments agree with the packet and with each other.**

## The key, as the packet names it

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| source-only, no build/deploy yet (this signature covers the code CHANGE; a SEPARATE build+apply pass, sequenced after both halves land, is arm (c)/(d)) | `_authz/loaders.py::load_ownership`'s exception branch: ONE new `elif` clause (`code == "AccessDenied" or exc.__class__.__name__ == "AccessDenied"` -> treat as absent, same `{"schema_version": 1, "advisors": {}}` as the existing `NoSuchKey` branch); the pre-existing `NoSuchKey` branch is byte-identical; every other function in the file, and every other file, is untouched | **IF built and deployed to all 7 serving functions:** for 49financial and cottonwood (ownership maps exist), `load_ownership` never reaches this branch -- **no observable change for either firm today.** For inflection, a request that today fails `UNEXPECTED` (opaque outage, no CloudWatch trace per `errors.py:191-192`'s `sink=None`) instead resolves with an EMPTY ownership map -- the same served answer a zero-grant advisor already gets, i.e. `EMPTY_GRANT`/the correct policy code, never `UNEXPECTED`, for inflection specifically. No new bucket, no new key, no IAM change, no Terraform resource, no env var. The residual risk (a genuine future grant removal for a firm whose map DOES exist would now read as an empty map, silently, rather than an outage) is disclosed and judged acceptable per the packet section 4(a)-(c): the grant is a single narrow per-firm statement unlikely to partially vanish, and a removed grant is independently visible on the existing IAM census arms (`battery_ib_rtf_10.py` arm (a)/(e)) regardless of this code path. | re-publish each of the 7 functions at its packet-listed pre-change `CodeSha256` via Terraform (`source_code_hash` + build-store `VersionId` pinned), never `update-function-code` (NEVER-9); verify `served == CodeSha256` read back for all 7. **On rollback, inflection returns to `UNEXPECTED` on every scoped request -- the exact state this packet found.** |

## Both branches covered

- **Built and applied** (both halves at HEAD naming this blob): the packet's own arm (d)/(e) sequence applies
  --- fresh plan per root, the subtraction-gate discipline (this project's established construction, per the
  IB-rtg-4 half above), all 7 roots showing EXACTLY this one source-hash change and nothing else, `.tools/
  safe-apply.sh` per root under a change-management ledger opened before, `served == CodeSha256`; **arm (e)
  measures live, under the deployed role, 3 of 3 firms resolve with no regression** -- this half does not
  predict that outcome, arm (e) does.
- **A half absent, or the blob differs at signing time:** nothing is built or applied; the source sits
  committed on `CLOUD` at rest (this session's drain, commit `0d0daf06ad`), verified per the packet's section
  3 (py_compile, ds-precommit, 141/141 existing `_authz` tests, the 4-of-4 in-process battery over the REAL
  measured wire shapes); inflection stays `UNEXPECTED`; `R76-AC1` stays `DISCLOSED-INCOMPLETE` with this
  packet named as the carry.

## What this half does NOT sign

Any IAM grant, bucket policy, or Terraform resource change (there is none in this packet -- verified above,
both instruments). Any change outside the single named `elif` branch. The mint-principal (B2) or new-bucket
(B3) branches -- both explicitly STOP-and-carry, neither taken by this worker. Row `IRPT_BCKEND-W1-S46`
(the face's stale `opal-data-inflection`/FWD-11 cross-reference -- the live blocker is entirely inside
`opal-data-inf`) and `IRPT_BCKEND-W1-S47` (the naming-gate's pre-existing stale marker, unrelated to this
cell's edit) -- both OBSERVATION rows, this seat's to disarm, not part of this signature.

**Push state:** LOCAL -- signed on `CLOUD` this turn; the CTO half is asked the same turn, by this blob.
