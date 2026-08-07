# SSCN_PRICOL -- portal promote v2.1.159 + SSCN price Lambda end-to-end

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, VALIDATE

Session 2026-08-07 ~1950Z-2215Z. Serial `0.3.0_DT_TradingOperations` (PID 30452).
Spawned for SSCN_PRICOL under an EXTERNAL clock: Andrew committed to Yang Liu in Teams
19:18:39Z, VERBATIM "Yes ok will have it within the hour or so" (outer edge ~2018Z).

---

## Current State

TWO INDEPENDENT LEGS BOTH LANDED. Neither is pending, neither is half-landed.

### Leg 1 -- portal DEV->PROD promote, COMPLETE

| Field | Value |
|---|---|
| PROD commit | `a211e09f4c9705ef95c344ab8b979f05571e496e` |
| Tag | `portal-v2.1.159` -- tag object `15f0e645`, PEELED `rev-parse ^{commit}` = `a211e09f` = origin/PROD head |
| CI | run `31220873661` "Deploy to Production" conclusion=**success**, SOLE workflow for headSha (enumerated by sha, not branch badge) |
| Parity gate | `git diff origin/DEV HEAD` = **0 lines** |
| Base / rollback | `08ebe7fe` (portal-v2.1.158) -- single step |
| Workspace pointer | CLOUD `aecb61dad8` (committed; push is integrator's) |
| Main tree | on DEV at `7877d7e1` THROUGHOUT -- Rule 19 never bent |
| Ledger | `sscn-pricol-portal` **CLOSED**, 5/5 legs proven (opened at deploy-start 2107Z) |

Promote set was exactly 3 commits, ENUMERATED BEFORE the push, not discovered after:
- `7877d7e1` 0.3.0_DE -- DataRefresh UploadTab.tsx + constants.ts (+30/-4). THE PAYLOAD.
- `e293ec5e` 1.0.0_SA_CTO~C -- portal-proxy.ts, COMMENT-ONLY (I read the diff; 0 executable lines)
- `e6bca5ce` Andrew Berman -- deletes `.github/workflows/surface-check.yml` (his own retirement)

`src/pages/SecurityScanner/**` UNTOUCHED -- verified with a diff, not by trusting the claim.

**What shipped, in user terms:** the DataRefresh upload page now advertises the file types the
path ALREADY accepted. Yang uploaded successfully and then asked whether the feature existed,
because the UI listed 5 sources and not his. A working path the UI does not advertise reads to a
user as an unsupported path -- he nearly did not try it.

### Leg 2 -- SSCN price Lambda, LIVE and served-verified

Andrew reassigned this to me at ~2050Z, VERBATIM (relayed by DE): *"have 0.3.0_DT do it, they
should have cloud permissions for lambdas."* Superseded MSTR's 2009Z routing to `0.7.0_AE_CloudOps`;
AE stood down and confirmed measured state (no commit, no TF, no invoke -- nothing to unwind).

| Step | Evidence |
|---|---|
| commit | `c76aaef814` -- price projection onto BOTH row builders (`:245`, `:288`) |
| artifact | `VersionId QL10fsF9Ys5HVz3BDTizpsReNEycU2e2`, `content-sha256 9ozYU1v8V0M0qVQmFn1Bo4KUmKB6HzVFNKWLCdfkkiY=` |
| terraform | `safe-apply` -> 1 changed / 0 destroyed -> **0-diff plan rc=0** |
| APPLIED truth | downloaded the DEPLOYED zip, read its bytes: **2** price projections (was **0** before) |
| re-trigger | ad-hoc QA invoke, StatusCode 200, no FunctionError, `{"asOf":"2026-08-06","universesProcessed":6}` |
| SERVED | sp500 write time MOVED `19:00:33Z` -> `21:59:13Z` (acwx `21:59:28Z`); **501 of 502** rows carry a real price |

Served samples: A 141.34 | AAPL 312.41 | ABBV 243.87 | ABNB 151.64 | ABT 107.96.

**Andrew's motivating case closed in the right universe:** ticker AU is in **r1000**, not sp500
(DE caught this; my first check on acwx returned 0 of 1830 and I nearly banked a non-finding).
`AU -> price 87.59, mktVal 44233.6` -- exactly the ~44.2b he was eyeballing against ~48.6b
externally. The sanity-check affordance now works on the exact ticker that motivated the request.

`price` REMAINS in `NON_SCORING_COLS` (`:78`) by design -- a human sanity-check affordance, not an
analytic. Percentile-ranking it would pollute factor_metadata and the composite. Do not "tidy" it.

---

## A CORRECTION I OWE THE RECORD

I reported to MSTR and CTO that *"three seats reported price is not in the dataset."* **That was
mine and it was wrong.** MSTR corrected it with evidence: DE's report explicitly made the layer
distinction (data exists upstream; cited `price` in NON_SCORING_COLS as POSITIVE evidence the
header exists), MSTR relayed it intact, and CTO's commit `@5261bde7a2` says "TRUE OF THE EXCEL AND
FALSE OF THE SERVED JSON." The distinction was made correctly and held across at least three hops.
Something flattened it before it reached Andrew; MSTR is checking their own relay and I am not
guessing at it.

**I attributed an error to colleagues that the record does not support, while writing up a lesson
about reading instruments carefully.** The mechanism half stands and is worth banking; the
"three seats were wrong" half is retracted.

**The mechanism (keep this):** the served `universe_data.json` sits DOWNSTREAM of the producer's
exclusion filter, so it reports "vendor never supplied the column" and "producer discarded the
column" with BYTE-IDENTICAL output. An absence verdict read from it is taken from the one
instrument structurally incapable of distinguishing the two -- CLAUDE.md's DESIGNED denominator
half, where no way of calling the instrument differently fixes it and the remedy is corroborating
OUTSIDE its domain (the vendor file, or the exclusion list itself). Andrew did exactly that:
"its in column AB." DE later confirmed header AB is literally `price`, lowercase, no whitespace --
so `row.get("price")` resolves, which is what made the deploy safe rather than lucky.

---

## Deployment Sequence + Verification (DT role requirement -- ACTUAL output)

```
0-diff plan after apply:
  No changes. Your infrastructure matches the configuration.
  detailed-exitcode rc=0

deployed artifact bytes (get-function -> Code.Location -> download -> read):
  2026-08-07T21:38:25.000+0000  9ozYU1v8V0M0qVQmFn1Bo4KUmKB6HzVFNKWLCdfkkiY=
  DEPLOYED price projections: 2
  entries: ['factor_metadata_registry.json', 'lambda_function.py']

served artifact after re-trigger:
  asOf: 2026-08-06 | rows: 502
  row0 keys: [ticker, name, mktVal, country, sector, industryGroup, universeWeight, divzWeight, price]
  rows with a non-null price: 501 of 502

CI by headSha a211e09f:
  runs for a211e09f: 1
  31220873661 Deploy to Production completed success

tag peel:
  tag object : 15f0e645ec58bd619dd45dcddae2538934807dc6
  tag PEELED : a211e09f4c9705ef95c344ab8b979f05571e496e
  origin/PROD: a211e09f4c9705ef95c344ab8b979f05571e496e   MATCH
```

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which "how do I grep the repo"` | PASS | A.3 startup EXERCISE -- forwarder produced its own banner (resolution is not execution) |
| A.3 PATH denominator | PASS | 96 of 97 comp-tools resolve bare |
| `deploy_ledger.py open/close-leg/close` | PASS | ledger opened at deploy-START, 5/5 legs closed with proof, entry CLOSED |
| `deploy_ledger.py check` | WARN | found 3 OPEN past-window ledgers under 0.7.0_AE_CloudOps (~237h) -- NOT mine, surfaced to COO |
| `safe-commit.sh` | PASS | 2 commits; risk-reflex CLEAN on the lambda (1 file vs 1659 danger nodes), HOLD citation read on `portal` |
| `safe-apply.sh` | PASS | gated apply; rejected my first call for missing the `apply` subcommand (correct) |
| `terraform plan -detailed-exitcode` | PASS | rc=0 post-apply |
| `commit-gate.sh` (via safe-commit) | PASS | py_compile + ruff on the lambda edit |
| raw `grep` on portal workflows | rail-checked | needed to answer "does any workflow gate on lint" -- a CI-gating question no comp-tool covers |

**What worked:** the deploy ledger's `close` REFUSES while any leg is unproven -- it would not let
me report done with L5 open. `safe-apply` refusing a call with no `apply` subcommand is a gate that
fails loud rather than guessing.
**What failed:** nothing silently. `aws lambda invoke --cli-binary-format` failed LOUD on CLI v1
(1.44.44) -- a v2-only flag; retried with v1 syntax.
**Gap found:** LD-0367's refusal message named branch **CLOUD** while I was pushing **PROD** --
the ephemeral worktree lives under `ajb_workspace/.runtmp/` so the hook resolved the PARENT repo's
HEAD, not the worktree's. It refused correctly here only because both branches are integrator-only.
A gate that misidentifies which branch it is protecting will eventually allow or deny the wrong
thing, and its message sends the next agent to the wrong place. Surfaced in one line mid-promote;
MSTR is carrying it to CTO.

---

## Gates that fired correctly (worth recording -- these are the session's real controls)

1. **owned-paths** refused DT on `infra/aws/**` (lane CLOUD_OPS_OR_ETL, any AE agent). Used the
   audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`. `--force` would NOT have worked --
   it does not bypass an owned-paths refusal, per CLAUDE.md 14a.
2. **LD-0367/LD-0368 integrator-only push** blocked me on DEV *and* PROD. The audited
   `# never-override:` escape was available BOTH times and **NOT taken** -- its own text says
   coordinate with the integrator first, so I did. MSTR ran both pushes (2114Z, 2138Z) and
   re-verified my enumeration and parity gate independently before each.
3. **Baseline typecheck on the PROD base BEFORE the merge** -- an environment control, so a red
   post-merge typecheck would be attributable to DE's change rather than my tree. It stayed green.

---

## Blockers

**None.** Both legs landed. Two integrator pushes were external dependencies, not blockers --
both cleared inside minutes.

---

## Residuals (banked, not chased -- none blocking)

1. **NKE** is the single null-price row in sp500 (1 of 502); r1000 has 2 of 1022. Data nulls, not
   defects. DE's column should render them honest-absent -- NOT the 502-em-dash dormant-column case
   MSTR ruled against.
2. **Price is in LOCAL TRADING CURRENCY, not USD** (DE's finding, DE's lane). acwx max 2,708,000
   (South Korea). **Do NOT "fix" this in the Lambda** -- no conversion, no normalization, no
   currency column. Raw local price is the correct emission; presentation is a DISPLAY concern and
   a producer-side FX conversion would be a derivation outside this project's fence.
3. Pre-existing lint error `ModelPortfolios.tsx:15:149 'ReferenceLine' defined but never used`
   fails `ci.yml` on DEV. Unrelated to this work; **cannot reach PROD** -- `deploy.yml`
   (branches [PROD]) has NO lint step (all three workflows grepped, not assumed). Deliberately not
   fixed by DE or me: tidying an unrelated file into a time-boxed promote is how a clean rollback
   stops being clean.
4. PROD no longer carries the Surface-Check Gate workflow -- the ACCEPTED CONSEQUENCE of Andrew's
   comp-surface-check retirement (Rule 20). No replacement guard built; that would be an
   unrequested gate.
5. Not mine, flagged once to COO: 3 deploy ledgers OPEN past-window under `0.7.0_AE_CloudOps` --
   `cot-pair-tolerance-recal` (237.8h), `emitter-wo4a-totals-refusal` (237.7h),
   `emitter-wo4c-cadence-acceptance` (237.1h, stranded=[L1,L2,L3]).
6. Stale inbox mail resolved without action: the 2026-07-22 P0 handoff
   (`hotfix/global-monthly-axis-key` @`8fd61dbf`) is contained in BOTH DEV and PROD -- it landed 16
   days ago. Branch is residue on origin, plus a stale worktree at `Desktop/_portal_hotfix_wt`.
   Not touched during a promote window.
7. Physical `.runtmp/portal-promote-20260807T201046Z` persists -- `worktree remove` hit the known
   Windows "Filename too long" class. `worktree prune` ran; gitignored and operationally inert.

---

## Next Steps

1. **[0.0.0_AB_MSTR]** Push CLOUD -- two commits local at this seat: `c76aaef814` (lambda price
   projection) + `aecb61dad8` (portal pointer). Integrator-only per LD-0367.
2. **[0.3.0_DE_TradingOperations]** Ship the frontend price column (~10 lines per tab, immediately
   before 'Mkt Val ($M)' in UniverseDataTab.tsx + UniverseScannerTab.tsx). GREEN sent 2202Z with
   the served-artifact evidence. Handle the local-currency formatting per their own finding.
3. **[0.3.0_DT_TradingOperations / me]** STAY WARM for the second promote -- worktree pruned but
   bun/node_modules knowledge is fresh and PROD base is known. A second promote today is cheap.
4. **[1.0.0_SA_CTO]** LD-0367 hook resolves the PARENT repo's HEAD from a `.runtmp/` worktree and
   names the wrong branch in its refusal. Routed by MSTR.
5. **[0.7.0_AE_CloudOps]** Three past-window deploy ledgers (item 5 above) -- ~10 days open, one
   with 3 stranded legs. Our own law calls a stranded leg RED-ALERT material.
