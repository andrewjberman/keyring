# OPAL_ANALYST.W4c-1 — `/ticket-center`, the first mutation-axis run (resume → DRY → sealed)

**archetype:** MIXED
**Agent:** `0.1.0_DE_MarketIntelligence~Z` · **2026-08-12** · **TO:** `OPAL_ANALYST.W4c-1` (CTO~Z)

## What this session did

Resumed a run whose three enumeration planes and reconciliation were already committed by a
predecessor killed at 07:52Z (planned N-able RMM restart as SYSTEM; nothing respawns seats). Carried
it from `c0` to **DRY, planted and sealed**, and handed the verifier packet to `3.0.0_SA_CVO~Z`.

| commit | increment |
|---|---|
| `baf8173754` | `c0` — axis declaration, 108 cells all UNMEASURED, run manifest |
| `14298eed49` | `c0` amendment — the intersecting-blind-spots binding |
| `351719a4e3` | `c1` — Plane A measured, 66 cells |
| `23c2eea324` | `c2` — VERIFY via applied-IAM lens + 4 relations |
| `ce6cd3de1b` | DRY + W expectation (**before** any plant) |
| *(this)* | plant + seal + verifier packet + consumable + log |

Commit-per-increment is deliberate — CTO~Z made it mandatory this session after the 07:52Z outage.

## The finding

**`authority_gate_server_differentiates` = NO on all six routes**, measured from the **deployed
package** of `opal-ticket-api`. The handler reads caller identity and never gates on it: every use of
`_actor()` is a stamp (`created_by`, `assignee`, audit rows), and the only `ConditionExpression`s are
state-machine guards (`status.eq('open')`, `status.ne('completed')`). `list_tickets` applies **no
firm scoping at all**, on routes namespaced `/api/scoped/`. With Plane A's measured **zero**
client-side guards, any authenticated portal user can list every firm's tickets and claim or complete
anyone's. **Rule 9 disposition only — no act, nothing built, nothing invoked.** CTO~Z is routing it
to Andrew as a security finding; I did not adjudicate its scope.

**The method finding underneath it:** three documents — the axis spec, my own Plane B, and my own c0
declared limits — recorded that cell as *expected-UNMEASURED-forever* because the authorizer's source
is out of repo. **The reasoning was sound and the conclusion was wrong: we were looking in the wrong
COMPONENT.** The authorizer answers authentication; per-caller authorization lives in the business
handler, whose deployed bytes are readable. A 3,838-byte download settled it — cheaper *and* safer
than the preflight probe the spec offered as the sanctioned safe form. CTO~Z bound the general rule:
**an "unmeasurable" claim must name the component it was unmeasurable in.**

## What I got wrong, and how it was caught

1. **My path-fragment lint read a hand-transcribed dict, not the artifact** — so it validated my
   typing. Found only because CVO~Z's prose-locator measurement reached me mid-build via COO~Z and I
   checked my own artifact instead of assuming I was clear. **6 of 6 of my `entity_keys` are prose**;
   a path-shaped test over them finds zero rows and reports clean. Fixed structurally (typed
   `entity_locators`, artifact-reading lint, classification census, refuses rather than skips).
2. **K18 — a constraint I authored at c0 and called dormant — fired at c1 with 3 violations, and the
   defect was in MY matrix.** I conditioned the authority-gate fields on `entity_kind` (what it does)
   when they belong to the serving surface (how it is reached). Rule 24(iii), in my own axis. CTO~Z
   ruled the fix program-wide.
3. **My pre-handler kind assignment for `tc.06` was falsified by the deployed bytes.** Reclassified to
   ARTIFACT, declared and routed rather than switched quietly; CTO~Z ruled it correct.
4. **A count I nearly generalised from one sample.** I told CVO~Z 24 `NOT_MEASURABLE` locators might
   lack a component and I had checked one. The sweep says **24/24 mechanically, 1/24 truthfully** —
   the 23 KIND cells do not owe a component. Same shape as `0 useQuery` true / `0 accessors` false on
   this very page.

## Predictions scored (not back-fitted)

- **ARTIFACT rows: predicted 0, measured 1 → FAILED.** Original line left standing in the artifact.
- **`invocation_surface`/`consumer_set` collapse on COMPUTED_READ → CONFIRMED**, with the denominator
  correction stated (predicted over 3 rows, scored over 2, because `tc.06` moved kind for an
  unrelated reason).

## Compiler Tools

| tool | invocation | result / what it bought |
|---|---|---|
| `comp-which` | *"how do I grep the repo"* (startup exercise); *"what routes are registered on an API Gateway…"* | Startup probe **exercised on output, not rc** — forwarder ran. The API-GW question returned a **near-tie of 3 with no fit** (`comp-estate`/`comp-routes`/`comp-transform`), which is what authorised the rail-checked raw `aws` read. A tool correctly declining to answer is a result. |
| `comp-find` | `--name` ×4, content ×6 (`api/scoped/tickets`, interpolation/concat probes, `*ticket*api*`) | Denominators on every call. **Warned that `\( \) \|` are LITERAL to python `re`** — I dropped the `apiRequest\(` probe rather than report a zero from a predicate I could not vouch for. Found the handler is **not in repo** (0/25,673, control 2), which redirected the whole run to deployed bytes. |
| `ssot_validate.py` | `--self-test`; `rectangle` ×6; `patch --out` ×2 | Self-test 13/13. **I did not trust the rc**: ran 3 negative controls on *my own* payload (non-rectangular / `NOT_APPLICABLE` / UNMEASURED-with-value) — all refused with the specific violation named, positive control passed. Caught that the census display caps at 5 entities (`:282`) while the total is correct. |
| `comp-iam` | **deliberately NOT used** | It parses TF-**DESIRED** and models `(action)`, never `(action, resource)`. The c2 discriminator needed **applied** truth with resource ARNs, so I used `aws iam get-role-policy` per Rule 22a. Naming the tool I declined and why, since a blank here is not acceptable. |
| `aws` (rail-checked, read-only) | `apigatewayv2 get-routes`, `lambda get-function`, `iam get-role-policy`/`list-*-policies` | All materialised and counted from the artifact; no `--query length` on a paginated call; `NextToken`/`IsTruncated` checked on every list. Nothing invoked. |

## Declared exclusions

- 42 Plane B/C cells left UNMEASURED — **K4**, `3.0.0_SA_CVO~Z`'s by delegation. Not a gap.
- `tc.06.vintage_grain` left NOT_MEASURABLE/REACH — the resolving observation is a read of **ticket
  item data** (client data). `CHALLENGE_NOT_MEASURABLE` declined **on scope, not difficulty**.
- No route invoked; no denial path exercised; no cross-firm read. Per CTO~Z, a live cross-firm read
  would **create** the exposure the run documents.

## Surprises

- The live CloudFront read **refuted a source comment** (`tickets.ts:7-8` "4xx at the edge"). Desired
  and applied agree; the comment is stale. Reporting the 27-day zero *without* that read would have
  made BROKEN the natural inference, and it is the wrong one.
- The IAM role is **well-scoped and that does not help**: resource-pinned with no `DeleteItem`/
  `BatchWriteItem` (so `effect_scope` SINGLE-RECORD is bounded at two layers), **and** it grants
  unconditioned `Query`/`Scan` over the whole table — so no compensating tenant isolation exists
  beneath the handler. I went looking for the control that would have weakened my finding.
- The package tree **moved under the run** across the session boundary. Both vintages recorded; the
  schema is semantically identical (the 1420-line diffstat is a CRLF→LF reformat, tested by parsing
  both, positive-controlled).

## Next

`c6` certification is with CVO~Z (started, `MUTANT_SEALED.md` shut). Post-verdict: amendment sweep
for the REACH-cell component gap. Then **W4c-3 `/trade-submission`** — where the same
authorizer story and an out-of-repo handler make the P2 double-falsification likely to recur, and I
will go to deployed bytes first rather than record it unmeasurable.
