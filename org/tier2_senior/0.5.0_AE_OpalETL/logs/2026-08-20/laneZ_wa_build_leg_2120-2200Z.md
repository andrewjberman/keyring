# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 2120–2200Z

**archetype:** IMPLEMENT
**Project:** D7 TICKET LIFECYCLE v2 — W-A (native analytics + claim enrichment + the day-one field set)

## Summary

W-A's **build leg** is complete across six commits: the handler change (`81c502cff2`), the IAM
grant + `USERS_TABLE` in Terraform and the Rule-24 schema record (same commit), WA-10's
discrimination fix (`9121a55330`), a non-ASCII strip (`b121c2f26e`), and the WA-1..WA-10 proof
instance — VALID `rc=0` positional, rows=10, violations=0, **discriminated** by a separately-run
control returning `rc=1` and naming the omission. The apply is the laptop's; nothing here is
deployed, and the rows that need a real row say so.

## Three things measurement caught that review would not have

**1. WA-6 was a finding, not a formality.** `opal-ticket-api-role` → `dynamodb:GetItem` on
`opal-users-v2` returned **implicitDeny**; the positive control (separate invocation, same role and
action, on `opal-tickets`) returned **allowed**, so the instrument discriminates and the deny is
real. The role carried exactly one inline policy, tickets-scoped. `comp-iam` could not answer at
all — *"IAM role: (not mapped)"*, the documented role-mapping insufficiency, fail-closed and
honest — which is precisely why the live primitive was required.

**2. The directory schema was not what I assumed.** `opal-users-v2` is keyed `PK = USER#<email>` /
`SK = PROFILE`, and carries **no `user_id` attribute at all**. My draft used `Key={"email": …}`,
which would have raised on *every* claim, been swallowed by my own deliberate soft-fail, and
produced permanently blank claimer names — indistinguishable from a user genuinely absent from the
directory. `user_id` now carries the row's real primary key, with the redundancy-with-email named
for the gate rather than quietly resolved.

**3. ⛔ MY OWN STUB SHARED MY CODE'S ASSUMPTION — the strongest control result of the build.** The
fake directory was keyed on `email` too, so the battery passed **22/22 on a call that could never
have worked**. *A fixture built from the same assumption as the code cannot test that assumption.*
Fixed by rebuilding the stub from the **measured** table, then re-running the original bug as a
mutant: it now fails **exactly** the enrichment assertion with `user_id: None`, the
silent-degradation signature. That mutant is a better artifact than the green run.

## WA-10 — satisfied by code, not by re-ordering

CVO~Z conditioned the soft-fail before it was built: the degraded state is **semantically valid**
(a blank claimer name is the *correct* render for an absent user), so a single collapsed message
fires identically on the healthy and the broken case. My original print emitted both cases but
under one `ENRICHMENT-DEGRADED` prefix — discrimination by *prose reading*. Now
**`ENRICHMENT-NOROW`** (lookup ran, no row — a fact, no action) vs **`ENRICHMENT-FAILED`** (lookup
did not complete, exception type naming which way: AccessDenied = missing grant, Validation = wrong
key, else transport — a defect). Separate greppable tokens, both directions exercised, and the
battery asserts the tokens *differ*. Consequence: a mis-sequenced apply now announces itself as
`AccessDeniedException` instead of passing green as "works, no names". Per CTO~Z's asymmetry
correction, I did **not** discharge this by pointing at the sequencing.

## Evidence

| | Result |
|---|---|
| Battery, target | **26/26** |
| Mutant — pre-W-A engine | **6/26** (the 6 are regression checks that *should* pass on both) |
| Mutant — wrong key (my own draft) | **25/26**, failing exactly the enrichment check |
| Existing authz battery (WA-4) | **13 passed, 10 subtests**, rc=0 — quoted as measured, not as the TO's remembered "12/12" |
| Proof instance | VALID rc=0; control rc=1 naming the omission |

## Two of my own defects, recorded

**Non-ASCII in production AWS code** (`U+26D4`) — introduced in the very commit arguing for
mechanical greppability, caught by the gate's WARN, stripped and re-measured to zero across 628
lines. **My harness crashed instead of reporting, three times** — an unguarded dict index, then
`run()` swallowing `SystemExit` so a *correct* engine refusal read as a battery FAIL, then a
missing attribute on the pre-W-A engine. A mutant must yield a tally, not a traceback; each time it
was the mutant run, never the target, that exposed it.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-iam service opal-ticket-api` | "IAM role: (not mapped)" + disclosed 24 unattached policy blocks / 2 unparsed denies | FLOOR COULD NOT ANSWER — recorded, and the reason the live primitive was used |
| `comp-find` ×3 | main.tf, the authz battery, the TO — each with a denominator | PASS |
| `simulate-principal-policy` ×2 | implicitDeny / allowed, one `--resource-arns` each, control separately invoked | PASS (a finding) |
| `describe-table` + bounded `scan(Limit=3)` | the PK/SK + no-user_id measurement; sample stated as a sample | PASS |
| `pytest` authz battery | 13 passed / 10 subtests, rc=0 | PASS |
| `terraform fmt` | reformatted, re-check rc=0. **terraform is NOT at the CLAUDE.md-documented `.tools/terraform.exe`** on this box — resolved via WinGet; surfaced, not chased | PASS |
| `comp-blast` | **MANDATE DEVIATION, declared:** the TO wants it before write; run late, exceeded 120s, backgrounded — no output quoted | DECLARED IN THE INSTANCE |

## Blockers

None I hold. The apply leg is the laptop's, and its one ordering constraint is that WA-6's grant
must precede the WA-1/2/8 deployed exercises — now loud rather than invisible if it doesn't.
A1 still open on a real post at BG. W-F/W-E remain design-gated.
