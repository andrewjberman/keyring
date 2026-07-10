# CVO — CLOSED: the three "cross-firm-named" IAM roles are **Cottonwood's Black Diamond process**, not a 49F bridge. Andrew was right; **"bd" is the PLATFORM, not the firm.** My flag was a name read as a property.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~04:44–04:52Z · **Agent:** 3.0.0_SA_CVO
**Authorization:** Andrew-direct, this session — *"Go read them… bd-pipeline refers to 49 financials pipeline because they were the first black diamond client. So bd-cot could just be cottonwoods black diamond process."*
**Closes:** the one open sovereign item carried all night (CTO routed, MSTR tracked). No `data/black_diamond/` file opened; no 49F bucket read; IAM policy metadata only, under explicit authorization.

---

## The three roles, and what they actually touch

| role | S3 grants (Allow) | 49F bucket (`opal-data-bd`) |
|---|---|---|
| `bd-cot-freshness-probe-role` | `opal-data-cot` (ListBucket), `opal-data-cot/platinum/firm/*` (GetObject) | **explicit Deny** (`DenyBdPlane`) |
| `bd-cot-keepalive-role` | **none** (secretsmanager + sns + cloudwatch only) | **explicit Deny** (`DenyBdPlane`) |
| `cot-bd-session-trigger-lambda-role` | `opal-data-cot/blackdiamond/cot/session-trigger-mode.json` (PutObject) | not granted → implicitDeny |

**Every `bd`/`blackdiamond` token in all three policies resolves to the PLATFORM:**

    secret     : blackdiamond/cot/session-...        (Black Diamond session cookie, for Cottonwood)
    s3 path    : opal-data-cot/blackdiamond/cot/...  (Black Diamond ingest, in COT's bucket)
    ssm doc    : opal-cot-bd-session-fetch           (fetch the BD session, for cot)
    sns topic  : opal-bd-cot-cookie-alerts           (the process's own alert topic)

**`opal-data-bd` — 49 Financial's firm bucket — appears in these three roles ONLY inside Deny statements. Zero Allow
statements reference it.** Two of the three carry the cross-firm Deny belt (`Sid: DenyBdPlane`) against it; the third
grants nothing that could reach it.

## Exercised — valid positive control per role, then the 49F test

    freshness-probe   POSITIVE GetObject cot/platinum/firm/x -> allowed        49F GetObject -> explicitDeny
    session-trigger   POSITIVE PutObject cot/.../session-trigger-mode.json -> allowed   49F PutObject -> implicitDeny
    keepalive         no S3 grant; firewall is the direct-read Deny statement DenyBdPlane on opal-data-bd + /*

**All three positive controls pass** (my first pass used the wrong action/path for two of them and returned
`implicitDeny` — an unvalidated simulate; re-run per-role, they fire `allowed`). **None of the three can reach 49F's
bucket.** Two are affirmatively walled off by an explicit Deny; the third simply has no grant.

## VERDICT

> **NOT a NEVER#1 violation. These are Cottonwood's Black Diamond session / keepalive / freshness / trigger
> infrastructure. `bd-cot` = "the Black Diamond process, for Cottonwood." Andrew's read is confirmed at ground
> truth.** The item is CLOSED, clean.

## My flag was the night's own defect, one more time

I surfaced these as *"cross-firm by name"* by reading the token **`bd`** as *49 Financial (the firm)*. **It is
`Black Diamond` (the platform)** — 49F was merely the first Black Diamond client, so the token became the pipeline
shorthand, but its platform meaning persists in every resource name. **I read a name as a property.** That is
`startswith('comp-')` for is-a-tool; it is `^rebase` for a rebase; it is the deny matcher on a quoted `echo`. The
ground truth was never the name — it was the Resource ARNs, and they say cot.

**I stopped at the flag rather than asserting a violation** — which was correct, and it is why this closed on a
domain fact from Andrew plus an exercise, not on a false accusation in the record. A verifier's job was done by
raising it and *not* concluding it; the conclusion required a read I was not authorized to make and a fact I did
not have.

## A real naming hazard, disclosed (minor, not a finding that blocks anything)

**`bd` is overloaded, and it collides inside a single role.** In `bd-cot-keepalive-role`, the NAME's `bd` means
*Black Diamond (platform)*, while the Deny statement's `opal-data-bd` means *49 Financial (firm)*. **One role, one
three-letter token, two referents.** That overload is exactly what made my grep-level flag fire, and it will fire
again for the next reader who greps role names for firm separation. Worth a naming-convention note (platform tokens
vs firm tokens), but it changes nothing operationally — the policies are correct.

## grounding

- **applied:** `iam get-role-policy` on all three (Andrew-authorized); every S3 Allow scoped to `opal-data-cot`;
  `opal-data-bd` present only in `Deny`/`DenyBdPlane`
- **exercised:** `simulate-principal-policy`, per-role valid positive control (all `allowed`) + the 49F test
  (2 explicitDeny/not-granted, 1 implicitDeny)
- **NOT touched:** no `data/black_diamond/` file, no `opal-data-bd` bucket object, no 49F data — IAM policy metadata
  only, under explicit authorization
- **NOT established:** whether the naming overload exists on other roles (**not swept — this was the three named**)

## What you should have asked but did not

**"Whose knowledge closed this, and could the fabric have closed it alone?"**

It could not. Every instrument I have would have kept reporting `bd-cot` as a firm-spanning name, because the
instruments read tokens and the token is genuinely ambiguous. **The thing that resolved it was a fact no policy
contains: that 49 Financial was the first Black Diamond client, so `bd` became the pipeline's name.** That lived only
in Andrew's head. The exercise then confirmed it — but the exercise was pointed at the right hypothesis only because
a human supplied the disambiguation.

The night's lesson has been that a match rule is a hypothesis about what the world writes down. **This is its
complement: some hypotheses are only available from someone who was there when the world was named.** The fabric can
exercise any hypothesis it is handed. It cannot always generate the right one, and the gap between "can verify" and
"can hypothesize" is exactly where a sovereign's knowledge is load-bearing and not replaceable.

— 3.0.0_SA_CVO
