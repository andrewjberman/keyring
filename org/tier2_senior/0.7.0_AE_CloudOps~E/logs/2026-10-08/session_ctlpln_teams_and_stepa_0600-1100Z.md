# Three WORLD applies in one morning, one STOP that was right, and two verification instruments found wrong -- `0.7.0_AE_CloudOps~E`

**Date:** 2026-10-08
**Task Orders:** NFRA_CTLPLN.TO-APPLY-11 (teams-agent, `2.0.0_SA_COO~R`); NFRA_CTLPLN.TO-APPLY-12 (identity step A,
`2.0.0_SA_COO~C`); NFRA_CTLPLN.TO-APPLY-11 (identity plan 1, `2.0.0_SA_COO~C`) -- STOPPED and then HELD
**Status:** COMPLETE for the two that ran; the third is on hold by its issuer
**archetype:** DEPLOY

**Preceding log:** `session_ctlpln_apply10_0450-0600Z.md` (TO-APPLY-10, the same session). **Box:** the laptop.
All three orders WORLD-risk, genre DEPLOY, each with two signed never-widen halves read in full before acting.

---

## Deployment Sequence

| order | act | result |
|---|---|---|
| TO-APPLY-11 identity plan 1 | untargeted apply of the Dell identity root | **STOPPED at step 3, branch B.** Nothing applied |
| TO-APPLY-11 teams-agent | one targeted apply of `module.ldo_001` in `infra/aws/terraform/transcripts` | `0 added, 3 changed, 0 destroyed` at **08:15:28-08:15:35Z**; entry CLOSED 6/6; proof VALID rc=0 |
| TO-APPLY-12 identity step A | one targeted apply of two managed policies | `0 added, 2 changed, 0 destroyed` at **09:19:39Z**; entry CLOSED 6/6; proof INVALID rc=1 on the order's own citation |

Commits: `2e49335` (the stop), `9138a27e09` + `9ce5f872b8` (teams open + close), `ef89619d9b` + `5642814fbf`
(step A open + close), `a88c35ede4` (the CTO's answer). **Push state at close: every one LOCAL.** `origin/CLOUD`
read `6ff91789da` by `ls-remote` at the step-A close; `0.0.0_AB_MSTR` pushes on Andrew's word.

---

## The STOP was the most useful thing this seat did today

Identity plan 1's halves signed a five-resource plan. At HEAD the untargeted plan read **`4 to add, 1 to change, 2
to destroy` over SEVEN resources**: commit `f7b668e9c5` had landed plan 2's resource-policy ALLOW in that root
*after* the halves were signed, and its `count` was derived from a data document rather than gated, so it was live
to any untargeted apply. **An untargeted apply would have granted the Dell group 70 resource-policy actions that
neither half signs.**

The order's commit clause was satisfied -- HEAD *did* contain the pin it named -- while the plan shape it signed no
longer was. **"Contains the pin" does not bound what else arrived.** Filed as `NFRA_CTLPLN-S25`, BLOCKING/ARMED,
`disarm_owner` the issuer, with three candidate routes named and none of them chosen by this seat.

**The issuer's answer, 25 minutes later:** the stop was right, the error was its own, the act became a targeted
apply (AMENDMENT 1), and the root gained `variable "apply_respol_allow" { default = false }` gating both
resources -- route (iii) of the three. **Four hours later that flag is why TO-APPLY-12's plan could be trusted not
to carry unsigned work**, and this seat read it at its declaration (`iam.tf:82-86`, `:89`, `:108`) rather than
assuming the default.

## Two verification instruments were found wrong, both by their own controls

**1. A rollback that cannot pass its own gate.** The teams order's code rollback requires a rebuild at
`55cb79f93c` to reproduce `IBrveNQC+Zbry9pHjbJ7C1Ww6EZb95XRXaFrziNSn6E=`. Exercised **before** the apply: the
rebuild gives `eXsoJG6SGZQ+TVHu+g5ohw7TFc4sxlitzZi/WPEjwPs=`. Cause measured, not guessed -- two packaged registry
files (`remediations.json`, `scopes.json`) sit CRLF in the shared working tree and LF from a fresh checkout
(`core.autocrlf` is `false`; parsed JSON identical; bytes identical after normalising). **A package hash on this
device is a function of (commit, tree line endings), not of the commit.** A rebuild at the cell's *own* pin gives a
third value, so the cell's recorded hash was never reproducible either. The act proceeded only because a byte-exact
substitute was established first: the live deployed bytes, downloaded via `get-function` and verified to hash to
exactly the reference. Filed `NFRA_CTLPLN-S27`.

**2. A comparator of this seat's own that passed a mutant.** Step A's V1 comparator checked that the four new Sids
were *present* and the six pre-existing statements unchanged -- and **a planted wildcard queue on
`DenyAgentbusQueuePolicy` read True**. Rewritten to assert every added statement's content field by field; it now
refuses all seven mutants. Both forms are in the evidence. A control that only ever confirms is not a control.

## The attribution instrument hit its limit, and the one arm that escaped it carried the finding

Every order in this series asks for each refusal attributed to a **named statement**, by leave-one-out (the
instrument this project settled on after offset arithmetic was measured wrong on TO-APPLY-8). On step A's read-back
**10 of the 12 refusal arms returned nothing**, because two policies now deny the same act and no single removal
lifts it. A **leave-TWO-out** sweep, restricted to the policies the live call named as matched, names both. Filed
`NFRA_CTLPLN-S29`, with the note that step B destroys the old Deny policy and will collapse the pairs back to
singles -- the same instrument will then produce a different shape of output.

**The exception is the sharpest evidence of the day:** `s3:PutLifecycleConfiguration` on the audit bucket
attributes to **one statement alone**, `create-policy/DenyAuditTrailBucketPolicy`, because the old resource-policy
Deny never covered a lifecycle write. **That is the measured proof that step A, and nothing already in place,
closes the seven audit-bucket settings the Dells could do that morning.** The doubled arms could not have shown it.

## Verification, per act

- **Teams agent.** Both functions' `CodeSha256` moved to the built package; the live policy went v2 -> v3 and 12 ->
  14 statements, equal to the saved one plus exactly `TellDell1OnTheBus` and `TellDell2OnTheBus`, with two planted
  mutants False; targeted re-plan `exit=0` against a pre-apply `exit=2` control; the untargeted after-read still
  `9 to add, 1 to change` over 10 headers, **0 under `module.ldo_001`**, none applied; the root's own
  `.terraform/terraform.tfstate` byte-unchanged across three reads.
- **Step A.** 26 of 26 live arms over both Dell users. The bus is intact (receive on each user's own queue, send to
  another box, both still allowed). The parameter grant is one parameter and not the family -- the 6.1 twin
  refused, and the basis printed rather than assumed: a census of all 8 live identity documents finds **exactly one
  statement naming `ssm:GetParameter` anywhere**. `aws:username` supplied on all four self-simulate arms, because
  an unevaluated condition returns the same `implicitDeny` for the wrong reason.
- **Both.** Every zero printed beside its denominator and a non-zero positive control on the same filter.

## Decisions Made

1. **A signed condition was released by its author, not by this seat.** The teams half's condition 2 put that order
   behind identity plan 1. One question went to the CTO; every step that did not depend on the answer ran meanwhile;
   only the apply waited. The release then arrived written into the signed half itself (`c519ff55b3`) and answered
   directly (msg 106828).
2. **The handler's first-hour read was reported NOT OBSERVED, not clean.** It is event-driven, had zero invocations
   and no CloudWatch datapoint at all. An absent error and an absent invocation read identically. The import class
   the condition targets *is* covered, because both functions share one package and the ingress loaded it 19 times.
   Filed `NFRA_CTLPLN-S28`.
3. **A step-A proof instance that cannot be made valid was left faithful to its order.** The order cites
   `round4.md` for cell `CT-a-1`; `round4.md` holds no `CT-a` cell. The checker enforces both that the instance
   match the TO and that the cell exist, so citing `access1.md` trades one violation for two. Filed
   `NFRA_CTLPLN-S30`; one line of the order fixes it, and TO-APPLY-11 carries the same fields.
4. **A row-id collision was resolved in the committed row's favour.** Another seat's `NFRA_CTLPLN-S26` landed
   between this seat's id census and its append. Ids are permanent, so this seat renumbered **its own uncommitted**
   rows to S27 and S28. The census is now re-read immediately before every append.

## Compiler Tools

| tool | result |
|---|---|
| `check_chat_assist_bus.py`, `gen_bus_devices.py --check` | teams AC1, `ok=True boxes=4 statements=4 matched=4 extra=0` and `BUS-DEVICES ok=True`, before the build and again at the close |
| `simulate_policy.py` | step A AC1, `undo_denied=181/181 ... all_ok=True`, before the plan and after the apply, identical |
| `terraform` plan/apply (scratch `TF_DATA_DIR` for transcripts) | both applies as signed; both re-plans `exit=0` against pre-apply `exit=2` controls |
| `iam:SimulatePrincipalPolicy` / `SimulateCustomPolicy` | 26 live arms + the leave-one-out and leave-two-out sweeps; one action and one resource ARN per call throughout |
| `aws cloudwatch get-metric-statistics` | the handler's **no datapoint** is what made its zero legible as "did not run" |
| `aws logs filter-log-events` | counted **client-side** from a dumped file, because `--query length(events)` on a paginated call returns the PAGE count -- hit and corrected mid-run |
| `comp-read`, `comp-find` | `comp-read`'s qualifier ledger found the fixture dependency behind S24; `comp-find` gave the measured zero behind S30 and read the `apply_respol_allow` default |
| `deploy_ledger.py`, `proof-of-spec-check.py` | two entries opened before their applies and CLOSED 6/6 each; teams proof VALID rc=0, step A INVALID rc=1 on the order's citation alone |
| `comp-iam` | **correctly not run** on both, and named so: it models `(action)` and never `(action, resource)`, and every claim in these acts is about *which* resource |

**What worked:** the mutant controls, twice -- they caught a rollback that could not run and a comparator of this
seat's own that passed a widening. **What failed:** nothing in the tools; two of this seat's own instruments, both
found by their controls and both recorded beside their corrected forms. **Gap found:** an acceptance check whose
verdict depends on a tracked fixture being stale (S24); a package hash that is not a function of its commit (S27);
a first-hour read that cannot be taken for one of the two functions it names (S28); leave-one-out unable to express
a doubly-denied act (S29); an order citing a decomp that does not hold its own cell (S30).

## Blockers

**None.** Nothing is owed by this seat.

## Current State

Three WORLD applies landed today (TO-APPLY-10 at 05:17:17Z, the teams agent at 08:15:35Z, step A at 09:19:39Z),
three NEVER-2 entries CLOSED with every leg proven, and `.open_deploys/` carries no sentinel of this seat's. Both
grants are **APPLIED, NOT EXERCISED**, in those words: this seat invoked nothing, sent no text and no bus line, read
no chat or mail content, and read no secret's value by any route.

`1.0.0_SA_CTO` msg 106590 is **answered** (`a88c35ede4`): the 49F insurance stage does run and the header says 18;
zero of four 09:46Z logs abort, against a denominator of 4 rather than 5 because 2026-10-05 has no such log. Both
figures in the record it questioned were out of date, and the abort pattern it described is real but historical.

## Next Steps

1. **[`2.0.0_SA_COO~C`]** The fresh GO for identity plan 1 with its restated shape -- both halves predict
   `2 to add, 0 to change, 2 to destroy` now that the create policy is at its final text. **This seat holds it.**
2. **[`2.0.0_SA_COO~C`]** S30's one-line fix to both CT-a-1 orders' `<decomp_ref>`, without which no proof
   instance of either can be VALID.
3. **[`2.0.0_SA_COO~R` / the builder's owner]** S27: make the zip byte-reproducible from the commit, and stop
   writing a rebuild-reproduces-the-hash gate into a rollback.
4. **[`1.0.0_SA_CTO`]** S28's wording fix for the first-hour read; and the two applied times to pass on --
   08:15:35Z to Andrew for the Teams agent, 09:19:39Z to dell2 for the parameter.
5. **[dell2 / a Dell, by another route]** The exercises: dell2's YCharts `terraform plan` reading the AMI
   parameter; one real request from a person in Teams; dell1's own read of a firm bucket.
6. **[whoever owns the seat gates]** CROSSBOX-DEPLOY read `verdict=STOP` in WARN mode on two of three applies
   today, once on a real cross-box overlap in a shared root. Under ENFORCE all three signed, targeted acts would
   have been stopped. `open_deploy` also read `hit` and `clear` on two applies with an open entry in both cases.
