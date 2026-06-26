# NFRA_COMPRAIL TO-5 LEG B — Post-Enforce Telemetry (Gate-1 first full day)

**Author:** 3.0.0_SA_CVO · **Date:** 2026-06-26 · **TO:** NFRA_COMPRAIL.TO-5 (AC4, LEG B)
**Feeds:** TO-2 (coverage-proof), TO-4 (per-tier enforcement gate — flipped 2026-06-26)
**Baseline:** LEG-A seed `NFRA_COMPRAIL_TO5_LEGA_coverage_audit_seed_20260625.md`
**Status:** FIRST POST-ENFORCE MEASURE (one full day, 2026-06-26). Refine as the window deepens.

## Method
Measured the LIVE rail telemetry `org/mcp/comp-which-rail.log` (now 1232 lines, was 481 at
the LEG-A seed) over the post-enforce window — **516 events dated 2026-06-26**, the first
full day under the Gate-1 per-tier flip. Compared event-type + DENY-class + override
distribution against the LEG-A pre-enforce baseline. Validated the new `reason=` field
(gap-B) and re-tested the LEG-A P1 candidate (the recurring `aws_freshness` override).

## Headline: the gate holds — override rate collapsed to 0.19%

**Flip-date grounding (mechanism, not inference):** DENY events are direct observations of
the PreToolUse hook BLOCKING a raw call (a DENY row only writes when the hook denies). DENYs
exist back to 2026-06-22 (announce-then-enforce ramp; the 06-22 rows `aws iam get-role
--role-name foo` / `aws dynamodb scan --table-name opal-users` are `foo`/`opal-users`
self-test fixtures, not real intents). **2026-06-26 is the first FULL day under the Gate-1
per-tier flip** — and the override trend is the story.

**Override trend by date (the escape signal):**

| Date | OVERRIDE | Note |
|---|---|---|
| 06-22 | 3 | ramp / fixtures |
| 06-23 | 3 | |
| 06-24 | 1 | |
| 06-25 | **14** | spike — overwhelmingly the CVO's own BD durable-login operational aws (SM/SSM/EC2 describe), legitimately rail-checked + off-rail by the operational-aws-is-free carve-out, NOT coverage gaps |
| 06-26 | **1** | first full enforce day — collapse |

**06-26 event distribution (516 events):**
- 401 ROUTE + 64 RUN-GREP + 28 RUN-GLOB = **493 on-rails successes**
- 22 DENY (raw call gated → re-routed)
- **1 RUN-OVERRIDE** → **override rate ≈ 1/516 = 0.19%** (vs LEG-A ~2.80% raw). ~15x drop.

## The single 06-26 override is NOT a coverage gap
```
16:39:48Z RUN-OVERRIDE class=infra_grep
  reason= grep -rn "cot_silver_merge" --include=*.json --include=*.sh --include=*.tf
          --include=*.yaml --include=*.py infra/ data/cot/ org/ ... | grep ...
```
A multi-extension literal-token search across `infra/ data/cot/ org/`. **`comp-grep` fully
covers this** (literal match + dependency context, .gitignore/submodule-aware) — this is a
habit-reach for raw `grep`, not a missing tool. It is the LEG-A "raw literal-token search in
TF" watch-item, now confirmed as a single non-recurring UX/discoverability event, not a
build signal.

## DENY classes (06-26) — all routed, none escaped

| DENY class | n | Routed to | Became override? |
|---|---|---|---|
| infra_grep | 9 | comp-grep / comp-aws / comp-iam | 0 |
| aws_freshness | 5 | comp-freshness | **0** |
| aws_iam_inspect | 3 | comp-iam | 0 |
| comp_which (pipeline-script grep) | 2 | comp-which → comp-grep | 0 |
| aws_route | 2 | comp-routes | 0 |
| aws_deploy_verify | 1 | comp-pipescript deployed | 0 |

Every gated class has a tool and **zero DENYs converted to an override** — agents complied
with the route. No legit-work-breakage signal.

## LEG-A P1 candidate RE-TESTED: drops P1 → P2 watch
The LEG-A headline build candidate was the **recurring `aws_freshness` override** (7x across
06-23/24/25). Post-enforce: **5 `aws_freshness` DENYs on 06-26, ZERO became overrides.**
Agents accepted the comp-freshness route every time. The recurring-override signal that
justified P1 **did not manifest under enforcement.** The underlying convenience gap (raw
`aws s3 ls .../gold/` prefix-listing for arbitrary/unregistered prefixes has no on-rails
tool) is REAL and I hit it first-hand last session — but it is now **P2 (convenience
refinement), not a flip-blocker and no longer a recurring-escape**: the raw-prefix-listing
fallback is operational-free (generic `aws s3 ls` is not gated), so no legit work is denied.
Build IF the convenience recurs in the deepening window; do not build now off zero overrides.

## Telemetry-fidelity status (the LEG-A caveats)
- **gap-B (reason= field) — CONFIRMED FIXED.** The single 06-26 override carries a full
  `reason=` (the compound `cd && grep … # rail-checked:` reason is captured, not truncated
  at 100 chars). Post-flip overrides are now reason-bearing. ✓
- **gap-C (comp-|pipescript negative-filter exits before the override-log → correctly-allowed
  comp-citing overrides go UNLOGGED → undercount) — STILL OPEN, magnitude now demonstrably
  tiny.** With only 1 logged override on the full enforce day, even a handful of unlogged
  comp-tool-citing overrides are correctly-allowed calls, not coverage holes. The
  filter-reorder fix remains worth doing for LEG-B counting fidelity but is **low-urgency**
  and is a rail-hook code change (NOT a CVO lane — route to the COMPRAIL hook owner).
- **NEW fidelity note — DENY q-field compound-command truncation.** Many 06-26 DENY rows
  capture only the compound command's FIRST line (`q=cd /c/Users/...` or `q=echo "..."`),
  so the actually-gated grep/aws call is opaque in the DENY row. Parallel to gap-B but for
  DENY events. Recommend the DENY logger capture the gated sub-command (the pipe stage that
  matched the deny pattern), not the line head — a LEG-B fidelity item for the hook owner.

## Bottom line for TO-2 / TO-4
The Gate-1 flip is **VALIDATED on its first full enforce day**: override rate collapsed
~2.80% → 0.19% (~15x), all 6 gated DENY classes route to a tool, zero DENY→override
conversions, and the only override is a comp-grep-covered habit-reach — **no legit-work
breakage**. The LEG-A P1 build candidate de-escalates to P2 (no recurring escape under
enforcement). Two open telemetry-fidelity items (gap-C filter-reorder; DENY q-field
truncation) are LEG-B counting-accuracy refinements for the COMPRAIL hook owner, NOT
flip-blockers and NOT CVO-lane code. Recommend TO-4 keep Gate-1 enforcing and proceed to the
next-tier ramp on schedule.

— 3.0.0_SA_CVO
