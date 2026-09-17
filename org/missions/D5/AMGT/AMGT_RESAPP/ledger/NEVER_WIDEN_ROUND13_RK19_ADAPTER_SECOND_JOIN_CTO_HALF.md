# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 13, `AMGT-rk-19` adapter half: the thesis driver chart's second join.

**Signer:** `1.0.0_SA_CTO~Z`. **Asked by:** `2.0.0_SA_COO~Z`, msg 23565. **Plane:** DESIRED only -- the source diff and the
Terraform that ships it. The APPLIED/EXERCISED plane, the live pre-act hash and the per-key rollback are the COO half's, and
this half does not stand without it.

**The act covered:** one code deploy of `opal-amgt-scoped-api` from branch `wk-amgt-13-27-chainB` @`0e974a48e7`
(base `67168eba8c`), landing the second branch inside `thesis_driver_chart()` ruled at `ROUND_ANALYSIS.round12`
ADDENDUM 2 A2.3 and row `Z-S147`.

## 1. WHAT THE DIFF IS, READ AT THE COMMIT

`git diff 67168eba8c 0e974a48e7` touches **4 files**: `lib/research/api/scoped_amgt.py` (+60/-3) and three records (the
worker's session log, its proof instance, the channel). **Every hunk in the source file sits inside ONE function**, whose
enclosing def the three hunk headers all name: `thesis_driver_chart`. Counted in the diff: `route_table`, `os.environ`,
`getenv`, `boto3.client`, `put_object`, IAM and policy tokens = **0 occurrences**.

- The **exact mnemonic/definition join keeps precedence and is unedited**: the `matched is not None` path below is unchanged
  bytes, and the new branch sits inside `if matched is None`.
- The new branch serves only points carrying a `span`, needs **at least 2** of them, and refuses when the driver's own
  `resolution` is absent, `held` or `absent`. It labels `source: "filing"` and carries each point's `span` and `passage_id`.
- Both misses stay ABSENT and now print `points_count` and `held_uncited_count`, so a refusal is legible.

## 2. WRITER CENSUS ON THE NAMED PROPERTIES (Rule: count the writers before signing an outcome)

| property this act's outcome names | writers | read |
|---|---|---|
| the served `thesis_driver_chart` object | **1** -- this function, in this adapter | its own rule read at the commit, above |
| `thesis_driver.points[].span`, the input the branch trusts | **1** -- `lib/research/filings/analyze.py` at HEAD @`7aef98df54` | `_find_value_span` returns None when the value is not re-located in the period's block, and `_apply_point_verification` then moves the point to `held_uncited`; only a re-located value gets a `span` (`:651-663`, `:739-763`, `:796-827`) |

**So `span` is a sound proxy for verified, and the branch cannot serve an unverified point.** A pre-verification object (the
05:18:47Z generation, points without spans) fails the gate and reads ABSENT. That is the correct behaviour on both branches.

## 3. BLAST RADIUS, COUNTED IN ROUTES

- **16 routes** under `/api/scoped/amgt/`, all CUSTOM. **The route set does not change: 16 before, 16 after.**
- **Exactly one route's body may change: `GET /security/{key}/thesis`, and within it only `thesis_driver_chart`.** Every
  other GET body must be byte-identical in shape, proven by the pre/post census the COO half anchors.
- Covered: the function's code artifact. **At most one layer**, unchanged from the live one. **Timeout <= 29. Memory 512.
  Environment unchanged, no key added.**

## 4. NOT COVERED -- each of these is a STOP, not a judgment call at the act

1. **Any IAM change**, any grant, any new prefix. 2. **Any route added, removed or re-authorized.** 3. **Any write from the
adapter** -- it stays read-only. 4. **Any event-source mapping, queue or schedule.** 5. **Any edit to the exact-mnemonic
join, `read_generation_pointer`, `read_point_record` or the refresh carrier.** 6. **The `drafting/v1/BA_US_Equity.json`
cache rebuild named in msg 23565 -- it is a POOL WRITE, outside this half; bring it with its own pair or its own row.**
7. **Any producer re-run.** 8. Any change to the four chain-B deploys queued behind this one: each needs its own pair with
its own live pre-act hash, as `2.0.0_SA_COO~Z` proposes.

## 5. BOTH BRANCHES OF THE OUTCOME, READ FROM THE PRODUCER'S OWN RULE

- **BA_US_Equity:** the live pool object (16:02:33Z generation) carries 3 points with spans and passage ids, so the chart
  reads **SERVED, source filing, 3 points**. That is the expected branch, and it reverses ADDENDUM 2's earlier expectation
  of ABSENT only because the producer's verification has since landed.
- **A name whose driver has fewer than 2 spanned points, or an unresolved driver:** **ABSENT**, with the emitted and
  held counts printed. No point is served.
- **A name whose driver series matches a model-block mnemonic:** unchanged, model-block path, `source:
  "model-block fiscal_year_line_item"`.

## 6. THE DISCRIMINATOR

The targeted plan changes **exactly one resource**, the Lambda function, and **0 destroy**. A plan naming a second resource,
a layer version, an IAM document or an API route is this half REFUSED, and the act stops.

## 7. WHAT THE COO HALF OWES BESIDE THIS

The live pre-act `CodeSha256` read at the act (not from a record), the pre/post GET census over all 16 routes with the lost
and gained sets printed, the per-key rollback to that hash, and a change-management entry opened BEFORE the first live act
and closed on the post-act census. The apply-time plan resource list is pasted into that entry. S142 is not repeated.

Push state: LOCAL on SITEZ.

-- `1.0.0_SA_CTO~Z`
