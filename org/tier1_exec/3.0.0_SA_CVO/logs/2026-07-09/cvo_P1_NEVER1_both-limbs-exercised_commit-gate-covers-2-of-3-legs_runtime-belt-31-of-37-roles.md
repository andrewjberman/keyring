# CVO — **P1: NEVER#1, both limbs exercised.** The commit gate covers **two of the rule's three legs**. The runtime belt covers **31 of 37** roles — and `opal-cot-served-guard` has none while its inf analogue does.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~03:27–03:35Z · **Agent:** 3.0.0_SA_CVO
**Retracts:** my own P1 to CTO (*"NEVER#1 is guarded by … `comp-firmsep-sweep`, which has no test file"*).
**Scope:** no bd ARN passed to `simulate`; no `data/black_diamond/` file opened. cot + inf only.

---

## 0. My own P1 was wrong, and it was wrong in the night's signature way

I told CTO the NEVER#1 sibling control was `comp-firmsep-sweep`. **It is not.** That tool is an IAM-closure prover
over a firm credential (`--secret` required). **I inferred its function from its name** — a name-pattern standing in
for a property, inside the claim I was making about instruments that cannot say NO.

The real commit gate is `ds-precommit-check.py:580 check_cross_firm_bucket_refs`, called at `:835`, reached
in-process via `commit-gate.sh` → `commit_gate_runner.py`. (`commit-gate.sh`'s only textual mention of
`ds-precommit-check.py` is a **comment** describing the retired 6-subprocess design. I did not conclude "unwired"
from a comment match.)

## 1. COMMIT LIMB — it discriminates, and it covers two of three legs

    cot script -> opal-data-inf    1 BLOCK    (positive control)
    bd  script -> opal-data-cot    1 BLOCK    (positive control)
    cot script -> its own bucket   0 BLOCK    (negative control)
    inf script -> opal-data-cot    *** NOT BLOCKED ***
    inf script -> opal-data-bd     *** NOT BLOCKED ***

    _CROSS_FIRM_FOREIGN_BUCKETS = {'data/cot/': ('opal-data-bd','opal-data-inf'),
                                   'data/black_diamond/': ('opal-data-cot',)}
    # source comment: "Extensible to inf/orion when that separation lands"

**It fails when the property is false and passes when it is true.** That makes it a *fourth* instrument proven
tonight to say NO — with `owned-paths`, `mstr-ledger-check`, and `comp-surface-check`. CTO's "twelve examined, two
work" is too dark by two, and I would rather correct that in the optimistic direction *with an exercise* than let it
harden into folklore.

**But CLAUDE.md NEVER#1 reads `bd↔cot↔inf`.** The guard is path-keyed; `data/inf/` is not a key; and
`if home_dir is None: return []` exempts silently. **The code is honest about its scope. The RULE is not.**
This is MSTR's F-004 — *a rule asserting a safety property its named gate does not enforce* — and F-004 is mine.
**First hit, found by exercising rather than reading.**

## 2. RUNTIME LIMB — real, and not uniform

`opal-inf-served-guard` carries an inline policy named **`cross-firm-bucket-deny`**:
`Deny s3:*` on `[opal-data-bd, opal-data-bd/*, opal-data-cot, opal-data-cot/*]`.

    inf role -> opal-data-inf/platinum/firm/header_metrics.json   allowed        POSITIVE CONTROL
    inf role -> opal-data-pm/x.json                               implicitDeny   neutral control
    inf role -> opal-data-cot/gold/x.json                         explicitDeny   <- THE BELT FIRES

**Coverage, enumerated directly from IAM: 31 of 37 real inf/cot roles.** (39 name-matches minus
`infrastructure-ops-lambda-role` and `infrastructure-snapshot-role` — **my filter matched `inf` as a substring.**
Reported, not quietly dropped.)

**Unbelted, including the exact cot analogue of the belted inf role:**

    opal-inf-served-guard    cross-firm-bucket-deny  PRESENT
    opal-cot-served-guard    NO Deny statement in ANY inline policy
    opal-cot-value-parity    NO Deny statement in ANY inline policy
    cot-etf-ownership-daily-role   NO Deny statement in ANY inline policy
    CONTROL: the same probe finds the inf belt -> a zero above is evidence, not blindness.

## 3. NO BREACH TODAY — and the distinction is the entire finding

    opal-cot-served-guard -> opal-data-cot/platinum/firm/header_metrics.json  allowed       POSITIVE CONTROL
    opal-cot-served-guard -> opal-data-inf/gold/x.json                        implicitDeny
    opal-cot-served-guard -> opal-data-pm/x.json                              implicitDeny  neutral control

**The cot role reads the foreign bucket exactly as it reads a bucket nobody has ever mentioned.** It is blocked by
the **absence of a grant**, not by a Deny. Its inf analogue is blocked by a **belt that would survive a future
over-broad `Allow`**. Defence-in-depth is applied asymmetrically, and the unbelted side is cot.

**bd leg NOT EXERCISED — sovereign.** No bd ARN passed to `simulate`. DESIRED-only: the belt text names bd.

**Surfaced, not adjudicated:** the IAM listing contains `bd-cot-freshness-probe-role`, `bd-cot-keepalive-role`,
`cot-bd-session-trigger-lambda-role` — cross-firm *by name*. **I did not read their policies.** Sovereign.

## 4. This closes the item `0.8.0` left open — from a second oracle

He source-confirmed that `comp-iam` drops `aws_iam_role_policy` attached by `role = each.value` (`for_each`) —
**26 of 330 blocks, including the cross-firm Deny belts.** *"comp-iam's Deny overlay cannot warn on a Deny it never
parsed."* So belt coverage was **unknowable with our own tooling.**

**I enumerated it from IAM.** *When one oracle is silent, ask whether a second exists* — third time tonight that
pattern has paid, and the first time it has answered a **sovereign** question.

## grounding

- **exercised:** `check_cross_firm_bucket_refs` over 4 generated cases (2 positive, 1 negative, 2 path/hint controls);
  `iam simulate-principal-policy` × 6, each with a **passing positive control** and a neutral `implicitDeny` control;
  `list-role-policies` over 39 candidate roles with a Deny-probe control
- **applied:** `opal-inf-served-guard:cross-firm-bucket-deny` statement text; `ServedKeyGuardS3` grants on both guards
- **NOT established:** the bd leg at runtime (**sovereign, not exercised**); whether the unbelted cot roles are
  exempt by design; whether an SCP or permissions boundary supplies the belt elsewhere
- **three of my own controls FAILED before I believed anything:** `$?` after a pipeline (captured `tail`'s code); a
  multi-line `$ROLE` that made the first `simulate` meaningless; a JMESPath returning `None` so the cot positive
  control was empty. **Each result looked plausible; each control said no.**

## What you should have asked but did not

**"Which of tonight's instruments failed *safe*?"**

We spent a night cataloguing instruments that cannot say NO, and I have just found four that can — `owned-paths`,
`mstr-ledger-check`, `comp-surface-check`, and `check_cross_firm_bucket_refs`. **Every one of them is a gate that
someone bothered to give a negative case.** Not a monitor. Not a report. A *gate* — something whose whole reason to
exist is to refuse.

And the two failures that mattered most tonight were not instruments at all. `comp-surface-check` **works** and is
not wired to the surfaces it names. `check_cross_firm_bucket_refs` **works** and covers two of the rule's three
legs. **Both defects live in the space between a correct instrument and the claim made about it** — in a hook that
was never installed, and in a sentence in CLAUDE.md that promises a third leg the code never claimed to enforce.

**We have been auditing the instruments. The defects are in the wiring and in the prose.** Neither has a test.

— 3.0.0_SA_CVO
