# CVO verdict — NFRA_COMPAWS: **CONFIRM-CLOSED. The 13/13 certs HOLD.**

**archetype:** VALIDATE

**Date:** 2026-07-09 ~18:40-19:05Z · **Agent:** 3.0.0_SA_CVO · **Requested by:** 2.0.0_SA_COO (/drive cycle 1)
**Bar set by COO:** "confirm the 13/13 certs still HOLD on the current estate. If they hold -> I execute
the 2-step atomic close." CTO: "confirm-closed rather than re-open (re-activation re-litigates done work)."

**VERDICT: close-ready. Certs hold. Do NOT re-open.** Two of the three certified oracle scorers now
report aggregate F1 below 0.95 — and **neither is a compiler regression.** Both trace to a stale oracle,
one of them because the estate got *safer*. Detail below, because a naive read of those two numbers would
have re-opened a parked project on a false alarm.

---

## Exercised — the three certified oracle scorers, live, current estate

| class | AGG F1 | gate | what actually happened |
|---|---|---|---|
| `stepfunctions` | **1.0000** | PASS | node 1.0, attr 1.0 (incl `definition_hash`), **INVOKES 26/26 recall 1.0** |
| `s3` | 0.9118 | "below" | **recall 1.0**, attr 1.0 on 62 axes; 6 FP = new buckets absent from the fixture |
| `iam-ec2` | 0.9000 | "below" | `declared_f1` 1.0; `overperm_recall` 0.667 from **one remediated role** |

**Zero false negatives anywhere** — `node_fn=0`, `invokes_fn=0`, `declared_recall=1.0`. The compiler has
not lost a single thing it was certified to find. Every dip is precision-side, and every precision-side
miss is the *oracle* being out of date, not the derive being wrong.

### stepfunctions — the strongest result
This is the cert that was originally **REJECTED** (`stepfunctions_cert_REJECT_20260608_1930Z.md`,
`SFN-INVOKES-NESTED-GAP`, INVOKES recall 9/26 = 0.346) and then re-certed. On the live estate today it
scores **INVOKES precision 1.0 / recall 1.0, 26 TP, 0 FP, 0 FN**, against live `describe_state_machine`.
The nested-Parallel walker fix holds. `attr_accuracy` 1.0 includes `definition_hash`, independently
corroborating ~A's 07-01 `def_hash 5082ce9dba1318fd unchanged` claim.

### s3 — fixture staleness, verified
`score_s3()` (`org/modules/graph/comp_aws_cli.py:2219`) loads its truth from
`aws-shapes/s3-hand-audit-fixture-v1.1.yaml` — a **frozen hand-audit fixture** (last commit 2026-06-24,
37 buckets), not a live pull. The 6 "extra" buckets are all **live-confirmed present** via `head-bucket`:
`opal-crawl-catalog`, `opal-data-astn`, `opal-mcp-athena-results`, `opal-mcp-audit`,
`opal-served-key-write-trail-logs`, `opal-website-backups`. Several are artifacts of this month's own
security work. Derive is right; the fixture is 6 buckets behind.

### iam — derive matches live EXACTLY; the scorer does not
- `derived_role_count = 168`. Live customer roles = **168** (180 total roles − 12 service-linked; the CLI
  paginates, so the count must be summed across pages). **Exact match.** The fixture's
  `customer_role_count: 111` is stale. `count_match:false` is fixture lag, and is not part of the F1.
- `overperm_precision = 1.0`, `overperm_recall = 0.6667`. The fixture (`:109-112`) asserts three
  over-permissioned roles as ground truth. Derive flags two. The third is `market-update-lambda-role`
  — and it is no longer over-permissioned. Live: its only attached managed policy is
  `market-update-lambda-policy`. The `AmazonS3FullAccess` + `AmazonDynamoDBFullAccess` the fixture
  records are **gone**, removed by today's firm-sep B2 remediation (`926d3e35f`). The other two
  (`opal-news-lambda-role`, `seeking-alpha-scraper-role`) still carry their broad managed policies live,
  exactly as the fixture says, and derive flags both.

**So derive is correct on all three roles. The oracle is wrong on one, because that one got fixed.**

---

## Findings

**F-1 (P1, methodology — comp-aws owner).** `score_iam_ec2()` scores the over-permission axis against a
**frozen findings catalog** (`iam_cataloged_findings_HELD.overperm_roles`). A remediated role becomes a
false negative. **The metric therefore punishes security work and degrades monotonically as the fabric
gets safer** — and it makes a "confirm-closed" gate structurally impossible to pass over time: every
future remediation drives the cert further "below" 0.95. Precision is already 1.0, which shows the
detector itself is sound. Recommend the axis be scored as a *detector* (does the compiler correctly
classify each role's CURRENT broad-managed state?) rather than against a frozen finding list; at minimum
the fixture needs a `remediated:` field with a date, and the scorer must exclude remediated entries.
This is a real defect in the cert methodology, not in the compiler.

**F-2 (P2, maintenance).** Three hand-audit fixtures are stale against the live estate: s3 (37 vs 43
buckets), iam (`customer_role_count` 111 vs 168), and the iam overperm catalog (1 of 3 remediated). Not a
cert failure; a fixture refresh. The fixtures are the regression oracle, so leaving them stale silently
erodes the gate.

**F-3 (P1, governance — my own error, owned).** The 2026-06-18 status flip `complete -> ACTIVE`
(`796c6ecf3`, on my cert-authority determination 154253Z) reasoned that "the `f9a92fcec` Wave-4 cert is a
9-class MILESTONE, not project-complete; intended scope = the 13-class taxonomy; 9-of-13 was never a
descope." That reasoning is contradicted by my own earlier artifact:
`cmpaws_f1/FINAL_13of13_certified_20260608_2025Z.md` (2026-06-08) certifies **all thirteen** classes —
S3, EC2, eventbridge, dynamodb, kms, lambda, secrets, SQS, CloudFront, CloudWatch, StepFunctions, SNS,
IAM — and records LD-0167 CLOSED, sovereign done-gate met. Wave-4 (2026-06-11) is *three days later* and
is a deeper live-oracle re-measure of nine classes, a subset — **not** "9 of 13 done". I read a subset
cert as a coverage ceiling and re-opened a project whose done-gate had already been met. That flip
re-opened 3 TOs and produced ~2 weeks of re-dispatch onto already-done work, which is precisely what
Andrew stopped on 07-01 and what CTO means by "re-litigates done work." The correction stands on my
ledger, not AE's or COO's.

**F-4 (COO's premise is malformed — the decisive question, answered).** COO: *"project JSON says
`status: active`, but Andrew DEPRIORITIZED it 07-01. Your verdict settles which is true."* Neither
horn holds. `org/projects/NFRA_COMPAWS.json` reads **`"status": "inactive"`, `"completed": null`** —
flipped `active -> inactive` on 2026-07-01 by `fac5c11ed` (2.0.0_SA_COO~B, Andrew-direct). And
`REGISTRY.md:81` sits under the **`## Inactive / On Hold`** heading (L77), carrying a 2026-07-01 date.
**JSON and REGISTRY are already ALIGNED.** There is no active-vs-deprioritized mismatch to settle; the
board's "JSON says active" is a stale read that predates `fac5c11ed`.

---

## Closure recommendation (COO executes; the call is COO's)

Terminal state should be **`complete`**, not `Inactive / On Hold`. Per `org/XXX.md` closure triggers,
"Inactive / On Hold" is reserved for a project blocked by an **external** dependency. COMPAWS has none:
the project's own sovereign done-gate (LD-0167, 13/13) was **met 2026-06-08**, and Andrew's 07-01 words
are that the re-cert "re-litigates a DONE completion" — he parked the *re-cert activity*, not a project
awaiting an unblock. A parked activity on a met done-gate is a completed project, and leaving it in
On-Hold keeps a done project visible as open work.

**Do not let the carve-out ride this close.** The staged SFN->Lambda `trace_graph` blast-radius bridge is
**net-new scope pending Andrew's go**, and its TO already lives under a different project
(`org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_GRAPHUNI.SFNBRIDGE.trace-graph-sfn-invoke-edges.md`
— NFRA_GRAPHUNI). It must not block, and must not be absorbed into, COMPAWS's close.

`VERDICT: close-ready (complete). Certs hold. F-1 + F-2 route to the comp-aws owner as follow-on
maintenance, NOT as COMPAWS re-activation.`

## grounding

- **desired:** `comp-aws classes` (taxonomy + "Certified oracle scorers: s3, iam-ec2, stepfunctions");
  `comp-kuzu` canonical surface `Nessie HEAD: current`, auto-refreshed, 20033 nodes / 35113 edges.
- **applied:** live `iam list-attached-role-policies` on all 3 overperm roles;
  `iam list-roles` census (180 total / 12 service-linked / **168 customer**);
  `s3api head-bucket` on all 6 "extra" buckets — all present.
- **exercised:** `comp-aws score --class {s3, iam-ec2, stepfunctions}` — the certified oracle scorers
  themselves, run against the live estate. Real outputs, not a config read.
  `stepfunctions` exercised INVOKES recall via live `describe_state_machine` (26/26).
- **source-confirmed (mechanism):** `comp_aws_cli.py:2219` `score_s3()` loads
  `SHAPES/s3-hand-audit-fixture-v1.1.yaml` (frozen fixture, NOT a live oracle);
  `:2243-2272` `score_iam_ec2()` derives `truth_overperm` from
  `oracle["iam_cataloged_findings_HELD"]["overperm_roles"]` — a frozen findings catalog. This is the
  mechanism behind F-1; it is read from source, not inferred from the score.

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-aws score --class s3 / iam-ec2 / stepfunctions` | re-exercise the certified oracles on the live estate | 0.9118 / 0.9000 / **1.0000**; all three dips diagnosed as oracle staleness |
| `comp-aws classes` | confirm taxonomy + which scorers are certified | only 3 of 13 classes expose a certified scorer |
| `comp-aws metrics` | structural invariants (edges/dangling/crosswire) | **BLOCKED — rc=124, timed out at 400s** with no `--graph` (attempts a live derive). Gap below. |
| `comp-kuzu "MATCH (n:CloudNode)..."` | per-class counts off the canonical surface (Rule 20 query-not-rebuild) | `Nessie HEAD: current`; global-graph taxonomy, so **not** directly comparable to the comp-aws 13-class fixture |
| `comp-grep "node_precision"` | locate the scorer implementation | `org/modules/graph/comp_aws_cli.py:2236` |

**Coverage gaps to route (CTO / 0.8.0_AE_CloudComp):**
1. `comp-aws metrics` with no `--graph` hangs past 400s (silent live derive). It should either take the
   canonical graph by default or fail fast with guidance. I could not confirm the cert's structural
   invariants (2787 edges / 0 dangling / 0 crosswire) through the tool, so **those three axes of the
   06-08 cert are re-confirmed only by inference from the per-class scorers, not exercised.** Stated as a
   residual, not papered over.
2. 10 of the 13 certified classes have **no certified oracle scorer** at all (`comp-aws classes`:
   "Certified oracle scorers: s3, iam-ec2, stepfunctions"). "The 13/13 certs hold" is therefore exercised
   on 3 classes and inferred on 10. I am confident in the verdict — zero FNs on everything measurable,
   and the two hardest classes (IAM, StepFunctions) are among the three exercised — but the honest scope
   of the re-confirmation is 3-of-13 exercised, and the gate cannot be *re*-run in full today.

## What you should have asked but did not

**"Is the cert oracle a live measurement or a frozen artifact — and if frozen, what is its half-life?"**
The whole COMPAWS method is "hand-audit becomes the regression fixture." That is sound the day it is
written and decays every day after, and nothing in the project tracks the decay. Two of three scorers
already read "fail" today purely from decay, one month on. The compiler is fine; the *oracle* is the
thing rotting. Worse, F-1 shows the decay is not merely neutral drift — the overperm axis decays
**faster the better the fabric behaves**, so the metric is anti-correlated with the outcome it exists to
protect. Any future "do the certs still hold?" question will hit the same trap and, absent this analysis,
will read three sub-0.95 numbers and re-open a done project — exactly the loop Andrew stopped on 07-01
and that my own 06-18 flip started. The fixture needs a refresh cadence and a `remediated:` field, or the
gate should re-derive its oracle live and diff *shapes* rather than compare against frozen sets.

— 3.0.0_SA_CVO
