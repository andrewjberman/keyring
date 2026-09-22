# AMGT_RESAPP round 24 -- never-widen pair, `AMGT-rk-97` -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED at the round-24 issuance.** Re-read live at SITEZ `1229b10b83`: MemorySize
512, Timeout 29, EphemeralStorage 512, layer `opal-amgt-print-deps:1`, CodeSha256 `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=`,
LastModified 2026-09-22T08:12:12Z, and the same two env keys, all equal to the cut. `scoped-amgt-api.tf:267` still
reads `memory_size = 512`, and nothing under the adapter's roots has changed since `4ecff8064b`. The paired CTO half is to be written by
`1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND24_RK97_CTO_HALF.md` and signed against live reads. The order does not act
on one half (its AC0).

**Sources:**
- decomposition s.32;
- CTO msg 24168 (row `AMGT_RESAPP-Z-S216`, pre-ruled);
- the order `task-orders/AMGT_RESAPP.TO-AMGT-rk-97.print-latency.md`.

**Measured at the cut:** 2026-09-22, SITEZ `4ecff8064b`, read-only by the issuer. Where the worker's AC0 re-read
differs, the ROLLBACK TARGET is the worker's value.

## `AMGT-rk-97` -- the print route's render time

### THE ACT

The act is ONE targeted apply of `module.scoped_amgt_api.aws_lambda_function.this`:
`HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -target=...`.
- It changes ONE attribute: `memory_size` 512 -> 1769 (declared at `infra/aws/terraform/harvest/scoped-amgt-api.tf:267`).
- **Before the apply:**
  - the declared `.tf` edit is committed;
  - the plan reads `0 to add, 1 to change, 0 to destroy`, with that one attribute as its ONLY changed line (the
    order's AC3). A plan showing any other attribute or resource applies NOTHING.
- **Deploy ledger:** `amgt-rk97-print-memory`, opened before the apply and closed on the post-act read.

### BLAST RADIUS

What the act MAY move, and nothing else:
- **(B1) `opal-amgt-scoped-api` MemorySize:** 512 -> 1769, and with it the function's CPU share (about 0.29 -> 1.0
  vCPU). This applies to every route the function serves (16 in its route table), because one function serves them all.
- **(B2) Every execution environment is recycled once.** The next request on each new environment pays a first-use
  cost: Init (about 130-170 ms today), and on the print route the plotting-stack import. So for a short window after
  the apply, the FIRST print per environment is a cold one. That cold cost is the quantity the order's AC5 grades
  against 20 s. At 512 MB it is 22.8-23.9 s, or a 29 s timeout.
  - The order reads it COLD FIRST (CTO msg 24174): a 10-way concurrent coldphase with no invoke between the apply
    and it, then 5 x 3 warm prints, then a 10-way burst.
  - The coldphase and the burst each open up to 10 concurrent environments. That is inside the account's concurrency
    and adds only reads of the served route.
- **(B3) Function configuration attributes** `LastModified` and `RevisionId`.
- **(B4) Per-invoke price:** x3.45 per ms. Measured volume is 306 invokes in 8 h, so the upper bound is well under
  $0.05 per 8 h.

**NOT moved** (asserted by the order's AC4, AC6 and AC7):
- CodeSha256 (`r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=` at the cut; equal pre and post);
- the artifact key and its versions;
- the attached layer `opal-amgt-print-deps:1`;
- Timeout 29 and EphemeralStorage 512;
- the environment (keys `HARVEST_ARTICLES_TABLE` and `HARVEST_METRICS_TABLE`);
- the scoped role and its inline policy;
- the HTTP API and its 29,000 ms integration timeout;
- the route table;
- the served PACK TEXT on each of the 5 names (extracted-text hash equal pre and post);
- every non-print route's status;
- every stored model block and every other S3 object.

### WRITER CENSUS

- **The function's memory setting:** N = 1 writer in the repo, `scoped-amgt-api.tf:267`, reaching the resource
  through `infra/aws/terraform/modules/yang-lambda/main.tf:29`.
  - 0 scripts call `update-function-configuration` / `update_function_configuration` on this function (a
    `git grep` across `infra`, `.tools`, `lib` and `integrations` at the cut).
  - No other round-24 order applies this function: rk-96 is code only in `lib/research/harvest`, and rk-95 is the
    gate parser in `.tools`.
- **The value on the print route:** N = 1 rule. It is `render_pack.build_pack`, reached from
  `scoped_amgt._print_pack` (`scoped_amgt.py:3953`), and it is unchanged by this act. Memory changes how fast the
  rule runs, never what it renders.
- **The act's own write set, one call deeper (Z-S192):**
  - `terraform init` writes the local `.terraform/` directory only;
  - the apply calls `UpdateFunctionConfiguration` once, with MemorySize only (the plan's one changed line);
  - the Terraform state object for the harvest root is updated.
  - 0 S3 object writes outside the state backend; 0 IAM writes; 0 layer publishes.

### EXPECTED OUTCOME -- read from the rule and from the measurement, BOTH branches covered

- **The pack bytes' content:** unchanged. The render rule has no input from memory or CPU.
- **Speed, projected from the measured seconds by the CPU ratio:**
  - warm prints 8.6-18.6 s -> about 2.5-5.4 s;
  - the first print on a fresh environment 22.8-23.9 s -> about 6.6-6.9 s.
- **Branch KEEP, TARGET MET:** every warm print is under 10 s and every fresh-environment print is under 20 s, with no
  rollback trigger. MemorySize stays 1769.
- **Branch KEEP, TARGET MISSED:** no rollback trigger fires, but a target is missed. MemorySize STAYS 1769, because it
  is strictly better on every name and inside (B1)-(B4). The order's AC5 is refused and a row routes candidate (a) to
  the CTO; a missed cold target sends the Z-S217 layer rebuild to round 25 (msg 24174). This half covers that resting
  state.
- **Branch ROLLBACK:** any trigger below fires. MemorySize returns to 512.

### PER-KEY ROLLBACK

- **MemorySize:**
  1. A NEW commit sets `memory_size = 512` at `scoped-amgt-api.tf:267`.
  2. The same targeted apply runs.
  3. `get-function-configuration` must print `MemorySize 512`, and the targeted plan must read `No changes.`.
- **Every other attribute:** not moved, so there is nothing to roll back. If the post-act read shows one moved, that
  IS a rollback trigger.
- **Rollback trigger (any one):**
  - post-act CodeSha256, Layers, Timeout or EphemeralStorage differs from the order's AC0 read;
  - any of the 5 names' extracted pack text differs from its baseline hash;
  - any non-print route whose baseline status was 200 is no longer 200;
  - any name's post-act median print duration is not lower than its baseline median.

### NOT COVERED

The following are not covered by this half:
- a layer rebuild or publish, i.e. candidate (a): a packaged font cache or MPLCONFIGDIR, or packaged bytecode;
- a PDF cache in S3, i.e. candidate (c);
- a code change to `render_pack.py` or `scoped_amgt.py`;
- any timeout change, whether the function's or the HTTP API's;
- any IAM, environment or artifact change, INCLUDING the env-var bump the CTO's msg 24174 names as a way to force a
  fresh environment (the order replaces it with a concurrent coldphase; if needed, the bump is its own paired act);
- a portal change;
- any S3 write or delete.

Each needs its own pair. The held branch `wk-amgt-14-50` is not read or named as a surface.

**Signature (COO):** SIGNED `2.0.0_SA_COO~Z`, 2026-09-22, at the round-24 issuance; the issuance commit's hash is the
signature's vintage.
