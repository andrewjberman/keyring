# PENDING VERIFICATION — MDPF per-partner gate, the 15:03Z OUTCOME

**STATUS:** OPEN. Fires after the **~15:03Z 2026-07-10** `mdpf-daily-trigger` INF-spine-sentinel run.
**Executor:** any live base serial. **`0.5.0_AE_OpalETL` authored the gate and named this verification itself.**
**Deploy:** LANDED `2026-07-10T00:17:02Z` on Andrew's direct GO (CTO `001053Z`). Ledger
`20260710T0013Z_mdpf-per-partner-gate-deploy` **CLOSED 5/5, nothing stranded.**

---

## >>> THE LEDGER IS CLOSED AND THE DELIVERABLE IS UNVERIFIED. THOSE ARE DIFFERENT THINGS. <<<

**The ledger's five legs prove the DEPLOY LANDED** — git-source on origin, build+upload with content-sha256,
`safe-apply` one-plan 0-diff, `get-role-policy` + `simulate-principal-policy` **applied**, `comp-pipescript
deployed → MATCH`. **Every leg is applied-or-exercised. The closure is correct.**

> **What no leg proves: that Inflection actually advances.** *A read is knowledge; knowledge can wait. A write is
> state.* The write landed. **The knowledge fires at 15:03Z.**

**Closing this ledger was right. Closing the QUESTION would not be.**

## VERIFIED IN THE DEPLOYED BYTES (COO, `2026-07-10T00:24Z`) — not from the ledger's word
```
aws lambda get-function -> Code.Location -> unzip -p lambda_function.py
  CONTROL: lambda_function.py present in the artifact              (1)
  :521  stale_partners = [p for p, v in partners.items() if not v["fresh"]]
  :528  if not GATE_ENFORCE: stale_partners = []                   <- the (D) fix, live
  :534  "stale_partners": stale_partners
  the unconditional `if GATE_ENFORCE and not gate["all_fresh"]: DEFER` is GONE
live env: GATE_ENFORCE=1 · BD_MAX_LAG_TRADING_DAYS=2 · MDPF_BUCKET=opal-data-mdpf
```

---

## THE EXERCISE (after the ~15:03Z fire, and NOT before)

1. **CloudWatch `/aws/lambda/mdpf-daily-trigger`, the 15:03Z invocation.**
   **PASS shape:** `stale_partners: ["49financial"]`, **dispatch proceeds** (not `DEFER`).
   **FAIL shape:** `DEFER`. If it defers, the gate is not doing its job and Andrew's deliverable did not land.

2. **THE DECISIVE READ — the SERVED artifact, not the log.** Inflection's `as_of` must **ADVANCE** past
   `2026-07-08`. **A Lambda that ran is not a partner that advanced.**

3. **49F must FREEZE at its last coherent vintage (`2026-07-06`), roll-forwarded as a unit** — with
   `as_of_by_partner` on its face. **49F freezing is the CORRECT outcome, not a compromise:** it is sovereign
   out-of-scope, and WS-E never runs on a stale minuend, so it never fabricates another residual.
   > **CTO: *"The plug is not fixed — it is not reached. I built a detector for a value we do not have to compute."***

## PROHIBITIONS — every one of these was earned on 2026-07-09

- **DO NOT close on `rc=0`, on "the Lambda ran", or on a CloudWatch line that merely appears.** *Never trust a
  producer's self-report; verify against the SERVED artifact.* (NEVER#5.)
- **DO NOT read Sentinel 3 passing as evidence the rolled 49F block is correct.** It certifies a rolled block
  **verbatim** — `0.5.0` declared that branch in the code rather than let it be discovered.
  > **A coherence check catches an INCOHERENT block. It cannot catch a COHERENT-BUT-FABRICATED one.**
  > `:216` asserts `total == model + sma + non_model`. **The 07-06 block satisfies that AND its `non_model_aua`
  > is still a plug against a minuend that had stopped moving. Coherence is not correctness.**
- **DO NOT touch `data/black_diamond/`, `schwab/`, `opal-data-bd`, or `opal-data-schwab`.** Sovereign
  out-of-scope. Both `bd-49f` ledgers remain `gate=sovereign/SUSPENDED`; their verifies **do not run.**
- **DO NOT re-arm the fabrication.** `/mdpf/custody_source` is `"schwab"` (v4). **It was `"bd"` at version 1.**
  **One SSM write re-arms the BD filename path.** *A dead path that fabricates when re-armed is worse than a live
  one.* `0.5.0` hardened `_latest_bd_silver_partition` with the schwab path's content assertion — **do not
  regress it, and do not flip the parameter to "test" anything.**
- **An empty result is not evidence.** Run a positive control before drawing any conclusion from a zero. Six
  times on 2026-07-09 an empty result was a broken query, not an absent fact — including
  `aws ssm get-parameter --name /mdpf/...`, where **MSYS mangles the leading slash**. Use PowerShell or an
  ARN-form identifier.

## IF IT DEFERS ANYWAY
Read `partners[*].fresh` in the invocation log **before** touching anything. The INF limb must be `fresh=true`
(its own gate log said `inflection: fresh=true` all night). If **INF** is the stale limb, this is not the 49F
problem and the gate is not the cause. **Escalate; do not patch inside a window.**
