# Session log -- 0.7.0_AE_CloudOps~Z -- 2026-09-03 1545-1700Z

**Archetype:** BUILD-DEPLOY-VERIFY (a nine-resource in-place attribute change on a live
production API, applied scoped, probed, and proven).
**Scope:** NFRA_OPSEC202609 ONLY (Rule 27, one project per instance).
**TO:** `NFRA_OPSEC202609.TO-OP-S-2` deliverables 1, 2, 3, 5, 6 -- deliverable 4 (the Z-S10
belt rider) was already landed @`653e7dfead` by the predecessor session and was verified at
source rather than redone.

---

## WHAT HAPPENED

Resumed after Andrew killed the Tier-2 workers at ~14:0xZ for API connection issues (COO~Z
restart package 19824, read and ACKed). The predecessor's stop was clean -- nothing
half-done, no uncommitted `routes.tf` -- and that was confirmed, not taken on report.

**Deliverable 1, the nine in-place route edits.** The nine existing
`aws_apigatewayv2_route` blocks in `shared-infra/apigateway-portal/routes.tf` that read
`authorization_type = "NONE"` gained `CUSTOM` + `authorizer_id`. Nine hunks, 18 insertions,
9 deletions -- in-place attribute edits, never new resources. Applied `-target` scoped
because the module's state lives in the shared-infra ROOT, whose baseline carries another
lane's unapplied `global_graph` lifecycle expiry (row Z-S17) that deletes objects and must
never ride. `Apply complete! Resources: 0 added, 9 changed, 0 destroyed`.

**Deliverable 2, the rollback, exercised BEFORE the nine.** On `r_as2dsme`: attach ->
read `CUSTOM/naqxlm` -> revert the config and re-apply the same target -> read back
`NONE/null`, byte-identical to the start. Exercised by the SAME mechanism L3 declares as
its rollback, not a borrowed one.

**Deliverable 3, the two probes**, under the OP-x-1 verdict (19584), whose text was read at
source before anything was fired rather than taken from the restart package's summary.

**Deliverables 5 and 6:** proof instance VALID rc=0 on all five expected ids; deploy ledger
`20260903T1605Z_opsec-s2-http-api-authorizer-nine-routes` opened before the first edit with
7 legs and closed with every leg proven.

---

## THE THREE THINGS WORTH CARRYING FORWARD

**1. A by-design route was one careless keystroke from being changed.** `r_3stqzjk`
(`OPTIONS /{proxy+}`) is one of the three routes this TO must NOT touch, and its
`authorization_type`/`target` pair in `routes.tf` is **byte-identical** to the nine:

```
  authorization_type = "NONE"
  target             = "integrations/s7ntfz4"
```

A `replace_all` on that pair matches **ten** blocks, not nine. Every edit was anchored on
its unique resource name + `route_key` instead. The live `get-routes` read afterwards
confirms all three by-design routes unchanged -- but the read would have confirmed the
damage just as calmly if the anchoring had been wrong, so the anchoring is the control, not
the read.

**2. My first two-sided probe produced a confident FALSE FAIL, and the fix was a positive
control.** Checking that the nine were 0-diff in the unscoped re-plan, I grepped for
`aws_apigatewayv2_route` and got 41 hits and a `>>> FAIL`. Those were `Refreshing
state...` log lines -- refresh chatter that names every route on every plan run and is not
a change. The sound probe greps only action-declaring lines (`will be created|destroyed|
updated in-place|replaced`), and it returns **0** route lines post-apply against **9** in
the pre-apply scoped plan. *A matcher keyed on the wrong line class fails toward alarm here
and would fail toward false-clean one negation away.* The positive control is what
converted the zero from "my grep found nothing" into "the plan contains nothing".

**3. The instrument menu in an acceptance criterion is only as sound as its weakest arm.**
S2-AC3 offers three interchangeable ways to read the vendor-call count, one of them
"CloudWatch metrics". For this Lambda that arm **cannot count at all** --
`opal-portal-lambda-role` is denied `cloudwatch:PutMetricData` on every invocation -- and it
fails SILENT: an empty series reads identically whether the vendor was called a thousand
times or never, and a positive control drawn from the same dead namespace is also empty, so
the usual control does not rescue it. Filed as row Z-S46. I found it only because the
liveness control on the *log* instrument happened to surface the warning; nothing in the
task order would have caught it, and a seat that picked metrics first would have filed a
PASS.

---

## THE TWO SURPRISE ROWS

Both filed to the tree channel and **committed alone** @`69669d3a38`, per the face's BOUNDS.

- **Z-S45 (OBSERVATION/INERT)** -- the face names "the demo firm's **committed** demo
  credentials" and no such committed credential exists. MEASURED: `comp-find
  'demo@demo.test'` = 56 hits / 51,324 files scanned with **zero** in the CONFIG band;
  `list-secrets` returns no fixture login; `opal/portal/config` holds four `VITE_*` build
  keys only. Two independent 2026-07-23 records name a **human custodian** instead. The
  identity half of the face is exactly right; only the credential half is wrong. Disarm
  owner `2.0.0_SA_COO~Z`.
- **Z-S46 (OBSERVATION/ARMED, disarmed same-turn)** -- the `PutMetricData` denial above.
  Disarmed by not using the broken arm and by naming it so the next reader of the S2-AC3
  menu does not pick it. The IAM remedy is deliberately NOT taken: adding a permission is
  its own lane and the bounds forbid a passenger.

**The instrument I used instead, stated plainly because it is not what the face
describes:** a token minted with the estate's own `opal/auth/jwt-private-key` for
`demo@demo.test`. It is a valid login by the only test the system applies
(`portal-authorizer/index.mjs:296-300` verifies signature + iss + aud and nothing else),
read-only, fixture-only, no write and no vendor call -- but it is **not** a password login
through `/auth/login`, and the proof says so in both the S2-AC2 row and Z-S45 so a later
reader cannot mistake one for the other.

---

## THE PROBE RESULT, because the shape of it is the finding

| | direct `execute-api` | through CloudFront |
|---|---|---|
| valid fixture bearer | **403** `{"message":"Forbidden"}` | **200** + real payload |
| anonymous | **401** `{"message":"Unauthorized"}` | **401** `{"error":"Missing or invalid Authorization header"}` |

Two independent discriminations fall out of one table. **Across the top row:** the same
credential is refused at one door and admitted at the other -- FWD-2's DONE WHEN. **Down
the direct column:** 403 with a credential vs 401 without one, which is the origin gate
running *before* the token, exactly as `index.mjs:265-282` says in terms. And the two
anonymous refusals carry **different bodies from different components** (API Gateway's
authorizer vs the `auth-validator-edge` Lambda@Edge), so each response certifies which
plane refused it rather than needing me to assert it.

Controls that make the refusals mean something: `OPTIONS` at the direct address returns
**200** (by-design route, untouched, so the API is reachable and the 401/403 are specific to
the nine), and `/auth/login` at the direct address returns **403** from a *different*
mechanism (TO-OP-S-3's origin secret).

---

## COMPILER TOOLS

- **`comp-read`** on `portal-authorizer/index.mjs` -- surfaced `:265` "ORIGIN GATE --
  checked BEFORE the token" among 13 qualifiers. This **reordered the probe design**: it
  predicted the 403-vs-401 split that distinguishes "the origin gate denied" from "no token
  was sent". Its UNREAD LEDGER disclosed 15 of 358 lines shown, so `:255-329` was then read
  directly rather than concluded from the digest.
- **`comp-read`** on `org/XXX.md` and `inbox-watch.sh` -- startup grounding; the latter
  confirmed the lane-serial split before arming the watcher.
- **`comp-read --enumerate`** on the channel -- 44 rows, max `Z-S44`, **with its
  denominator**, which is how `Z-S45`/`Z-S46` were allocated rather than guessed. Page 1
  alone showed `Z-S19` and would have been wrong; a page is not an answer.
- **`comp-routes`** (`api-routes`, `origins`, `behaviors`) -- gave the two addresses the
  probe needed (origin `APIGateway-portal` = `7k3ed8px20...`, behavior 23 `/v1/*`), and was
  **measured UNFIT** for the acceptance read: it self-declares `PLANE: desired ... never a
  live describe`, enumerates 21 routes of *other* APIs, and derives auth from origin TYPE
  rather than a route's `AuthorizerId`. That measurement is what justifies the
  `rail-checked` markers on the raw `aws apigatewayv2` calls -- S2-AC1 is an APPLIED-plane
  criterion and no comp-tool serves that plane.
- **`comp-find`** -- the credential census behind Z-S45 (56 hits / 51,324 files, 0 CONFIG).
- **`comp-adversary`** -- carried from the TO's preflight as the issuer's, not re-run.
- **`.tools/commit-gate.sh`** rc=0; **`.tools/proof-of-spec-check.py`** VALID rc=0 on both
  the S-2 instance (5 ids) and the amended S-3 instance (6 ids).

---

## STATE AT CLOSE

- `TO-OP-S-2` `<status>` flipped **complete**; proof instance VALID rc=0 on
  `S2-AC1..S2-AC5`, all five **PASS**.
- `TO-OP-S-3`'s `S3-AC5` amended from `UNCOMPUTABLE-BY-CONSTRUCTION` to **PASS** citing
  S2-AC2, in the same commit, as the face requires. That instance now reads 6/6 PASS and
  re-validates rc=0.
- Deploy ledger CLOSED, 7 of 7 legs proven.
- **Push state: LOCAL.** Push is the integrator's (LD-0367 / GATE 5); `0.0.0_AB_MSTR~Z`
  integrates. Commits: `fff78665c4` (routes.tf + ledger), `69669d3a38` (the two rows, alone),
  and this session's deliverable commit.
- Next for this seat per the face: `TO-OP-S-1` (the REST API adoption, staged @`4f48f292fd`)
  whose GO was held until this face flips, or `TO-OP-S-4` if the carrier ruling is still
  open -- the issuer cuts it on the complete flip. **Not started; not mine to start.**
