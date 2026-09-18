# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtd-5: the route-bindings object converged to the committed content (row S68)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- served output moves only under CTO+COO sign-off). **Signed:**
2026-09-18 ~14:0xZ. **The act signed:** the apply IB-rtd-5 performs, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtd-4.md` recommends, read at HEAD
`1922c400e1` (packet blob `d3dfc6f6f335762ad9b955d17a1441c13ef088e7`). A packet whose bytes differ from that blob is NOT what this half
signs; IB-rtd-5 re-reads the blob hash before any apply. The CTO half is MDPF's owner's (97865: "It is mine to close").

This half signs the ACT'S BLAST RADIUS and its rollback -- what the act MAY touch whichever branch the producer takes -- never the
producer's intention. Writers and readers of the named property are counted, not assumed (the packet's census, re-read here).

## The act, one key

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K1 | `.tools/safe-apply.sh -chdir=infra/aws/terraform/mdpf-pipeline apply -target=aws_s3_object.mdpf_route_bindings`, sourced from bytes EQUAL TO THE COMMITTED BLOB (`git show HEAD:data/mdpf/config/route_bindings.yaml`, sha256 `98f5e9c51d016d5283562e525b53088292576d86752c6cf0449865fbf328d923`, md5 `650f893a`) -- NEVER this box's CRLF render (`37eb8451...`); the worker materialises the LF bytes at the path before the plan (`git hash-object --no-filters` == `73924ab7ef...`, the only sound on-disk identity on an autocrlf box) | the served object `s3://opal-data-assets/config/mdpf/route_bindings.yaml` gains version #2 with the committed content; **0 of 4** code-level consumers read the served object today (the one intentional grant-holder, `mdpf-gold-lambda-role`, reads its packaged copy and its docstring forbids the S3 leg); **6 of 263** principals hold a GetObject grant (3 human/terminal identities, 1 unexercised intentional, 2 incidental account-wide) -- none exercises it, so the content change reaches no running code; **3 of 263** may write it (the three human/terminal identities), so the apply runs as one of those and nothing automated can race it | `s3api delete-object --version-id <the new version>` -- bucket versioning is `Enabled` and the prior (only) version `iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz` becomes current again; or a re-apply from a checkout at the pre-act content |

**Writers of the named property, counted:** `s3:PutObject` on the key -- **3 of 263**, all human/terminal identities, `0` UNKNOWN,
resource plane 0 allows / 1 unrelated deny. **Readers by grant:** 6 of 263. **Readers by code:** 0 of 4 named consumers. One property,
three writers, all read by the packet's census; this half signs none of those three moves.

## Both branches covered

- The producer takes the apply: the targeted plan re-run immediately before it reads EXACTLY `0 to add, 1 to change, 0 to destroy`
  naming only `aws_s3_object.mdpf_route_bindings`, with `content-sha256` `c9e54ce2... -> 98f5e9c5...` (the COMMITTED sha, not
  `37eb8451...`); post-apply `head-object` reads `content-sha256` `98f5e9c5...`; the post-apply UNTARGETED plan of the root reads
  `0 / 0 / 0` (the packet measured that this object is the root's ONLY drifted resource at HEAD, so convergence is the whole point and
  a root still divergent after the act does NOT clear S68 -- IB-rtd-5 says so and the row stays ARMED).
- The producer STOPS: a plan naming any other resource, or a content-sha256 target that is not `98f5e9c5...` (a CRLF render), is a
  BLOCKING row and nothing is applied on that root.
- The apply lands and a consumer breaks: none can by the census above; if the post-act consumer read (`4 of 4` load their own path,
  the tie-out validator `34 of 34`) fails anyway, the rollback is the version delete the same turn.

## What this half does NOT sign

- Any edit to `data/mdpf/config/route_bindings.yaml` or a `.gitattributes` `eol=lf` line (a row for the file's owner, not this act).
- The two incidental account-wide read grants (`opal-news-lambda-role`, `partners-lambda-role`) -- a packet finding for the IAM owner.
- Anything on the mdpf-pipeline root beyond the one targeted resource.

**Push state at signing:** `1922c400e1` LOCAL; origin/CLOUD `ec5a7afd2b` (the CTO's 12:43Z ls-remote; not re-read here).
