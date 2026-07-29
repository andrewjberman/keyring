# 2026-07-29 — Session 2343-0430Z: WO-3 MDPF consumer re-point (edge flip) + two PROD promotes

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

Spawned to execute WO-3 — the last step of Andrew's "MDPF completely done end to end." Cut the
portal's read from the frozen legacy `json/mdpf/*` to the canonical publisher tree
`platinum/mdpf/*`, then promoted two portal builds that made the served number reach the screen.
**Three deploys landed, all verified. Two hard stops taken before irreversible steps, both
ratified. Zero rollbacks.**

---

## What shipped

| # | What | Evidence |
|---|---|---|
| 1 | **Edge flip** — `public-data-router` v6: `/api/general/mdpf/` -> `/platinum/mdpf/` | live CF pin `:6`, ledger `20260729T0101Z` CLOSED |
| 2 | **Promote v2.1.149** — DE's headline field-read fix (7 commits) | PROD `1f363956`, CI `30418600984` success |
| 3 | **Promote v2.1.150** — full-series field read, legacy fetches deleted (1 commit) | PROD `80e21674`, CI `30421793644` success |

---

## Deployment Sequence + Verification (DT role requirement — actual output)

### Deploy 1 — the edge flip (WO-3)
```
L1 commit 6f1f242a6a   lane PUBLIC_DATA_ROUTER_DEPLOY @3a9c4bd3ab (COO grantor-landed, ZERO overrides)
L2a build+upload       portal-auth/public-data-router.zip VersionId fo_nPiGzdevTtcrZcPKrSddpBM6YNl6R
                       live metadata content-sha256 vC65BEng0+qoyYfbc42Vwn0JZ0VhTGtAwX2fGB+3zSY= == build output
L2b apply x2           APPLY #1 published :6 but the plan never listed the distribution -- the hazard
                       documented at cloudfront-distribution.tf:59-64. The 0-diff RE-PLAN CAUGHT IT;
                       apply #2 landed :5->:6. TWO APPLIES, reported not smoothed.
                       live: public-data-router:6 on /api/general/* AND /api/general/json-tiered/*
                       distribution Deployed, 24 behaviors, TF "No changes."
L3 invalidation        I6PA7CJZQ07WPOHQGLTSYH11OP paths ['/api/general/mdpf/*'] ONLY, Completed 01:31:42Z
L4 battery             EX1 mdpf/global 200 200,059B md5 31e64570d3090eff4df3baab91d2a1dd == platinum ETag EXACTLY
                       EX2-4 49f/inflection/cottonwood 200, all as_of_last 07-27, vintage 2026-07-27
                       CONTROL portfolios/aum-metrics.json pre==post 7,234B md5 9bae4b42ff312c72817ca27861c1e28b
                       NEGATIVE json/mdpf/global ETag 5f758b47 / 254,419B / LM 13:41:05Z UNMOVED
                       COO ORACLE: 447 shared dates / 0 movers / 0 lost / +3 (07-23,24,27)
                       labels 400 absent / 45 interpolated_estimate / 2 measured / 3 carried -- EXACT
```

### Deploys 2 + 3 — the promotes
```
                       v2.1.149                          v2.1.150
DEV head               1e4bdf14                          f6c11812
PROD merge             1f363956                          80e21674
tag (PEELED-verified)  portal-v2.1.149                   portal-v2.1.150
  tag OBJECT sha       (96f94703 -- NOT the commit)      (49a8a548 -- NOT the commit)
CI run / conclusion    30418600984 success               30421793644 success
parity gate            0 bytes (EMPTY)                   0 bytes (EMPTY)
pointer commit         25fc29c8ed -> 1e4bdf14            7194c90a84 -> f6c11812  (both verified ON ORIGIN)
base / rollback        17256834                          1f363956
commits shipped        7 (all 0.4.0_DE)                  1
held-language scan     0 hits                            0 hits
main tree after        DEV                               DEV
```
Both: typecheck `tsc -b --noEmit` 0 errors · Step-3 PROD re-assert · ephemeral worktree ·
FOREGROUND `bun install` (420 pkgs) · VALGATE D-1 PASS · pre-push typecheck PASS ·
`worktree remove` failed "Filename too long" (documented-acceptable) -> `worktree prune` clean.

---

## The two hard stops (both taken BEFORE the irreversible step, both ratified)

**STOP 1 — a held CF flip was riding my apply.** The portal-auth plan read `1 to add, 2 to change`
and only ONE line was mine. The rest was AE's **MDPF_REVAMP.S5** block (`328248c135`, subject
*"HELD for CTO+COO+Andrew re-land co-sign"*, P0-rolled-back once at `9a59360605`): an OAC plus
**11 exact-key CF behaviors** pointing at `S3-opal-data-assets`. Because they are exact-key they
out-specific `/api/general/*`, so **CloudFront would have matched them first and the GO'd
Mechanism-A branch would have been inert on arrival**, serving an origin nobody verified. No
`-target` separates them (same distribution resource). CTO ruled Option A; AE de-staged
(`5bb23c45a6`); I re-planned MYSELF and confirmed `0 add / 1 change / 0 destroy`, residue grep = 0.
CTO: *"the catch of the night... the G8 landmine fired and your plan-read was the gate that worked."*

**STOP 2 — CI red on the first promote candidate.** `/prod-deploy` Step 2 requires green; both
workflows failed on `d0fb493e`. ESLint: an orphaned `readAllModelSeries` import — *the fingerprint
of the fix being correct*, since the code consuming it was deleted. Surface-Check Gate: `rc=2
BLOCKED` on `model_portfolios.headline` SEV1. **CTO's GO had asserted the ACK was audited — true of
the LOCAL pre-commit hook, FALSE of CI**, which reads a `^`-anchored `SURFACE_ACK:` line from the
COMMIT MESSAGE. **The local ack does not TRAVEL.** DE re-pushed with the anchor at column 0; I
verified the new SHA myself (1 file / 1 line vs the reviewed SHA, logic byte-identical, anchor
count 1).

---

## The incident: 403 on every mdpf URL, and the fix-forward

Flip landed 01:31Z -> all four mdpf URLs **403** -> root cause source-confirmed in ~4 minutes:
`opal-data-portal-v2`'s `AllowCloudFrontOACPublicData` granted `s3:GetObject` on `[json/*,
json-tiered/*]` — **`platinum/*` absent on BOTH planes** (AE confirmed TF desired at
`shared-infra/s3-portal-v2-import.tf:108`; a grant never written, not drift). Blast radius measured
and CONFINED (non-mdpf control 200 byte-identical; frozen negative unmoved), both options priced,
**neither self-authorized**.

**MY MISS, owned: I verified the platinum KEYS existed and never that the READER could reach them.**
CTO's proportions: the reader-reach check was in nobody's plan — not the WO-3 dispatch, not the
WO-2 spec review, whose verify exercised the WRITER's path only. **Standing item now: every
re-point verifies the reader's grant on the new prefix BEFORE the flip. "Presence is not access —
READER-side."**

Resolved by AE's one-line grant (`507c16864f`) under CTO Option A + **Andrew-direct ~0138Z, verbatim:
*"no we're not wasting time rolling back, lets just do this properly in the first place and point to
the right place with right permissions"*** — recorded durably (`b398a8cd38`) and broadcast same turn
(CTO 013844Z, COO 013907Z, MSTR 013925Z) per XXX.md.

---

## The headline defect the flip exposed

Post-flip the page read **$1.91B**, not $1.95B. I computed the render from the served artifacts
independently, before reading CTO's hypothesis; it matched to the cent:
```
trendLastPoint.aum = sum of 7 NON-SMA by_model[].model_value = 1,672,708,163.51 @ 07-27
                     (== platinum model_aua[-1] -- the model leg WAS the flip, working)
+ non-model leg    =   232,313,972.65
= RENDERED           1,905,022,136.16      vs artifact's own opal_aggregate_aua 1,950,519,805.86
GAP 45,497,669.70  = platinum's non_model_aua 277,811,642.35 - the legacy 232,313,972.65
```
**Fix-saving refinement:** the live path is the **date-keyed roll-forward from `time_series`**
(`:1170-1171`); `.latest` is only the `:1172` null-fallback. Both yield 232,313,972.65 tonight —
the coincidence that would have let a `.latest`-aimed fix pass review and miss the mechanism.

**COO's fetcher claim refuted on a printed denominator:** the scope-less
`getMdpfAggregateAUATimeSeries` has 4 refs in 2 files across **404 scanned** — definition, wrapper,
error string, **zero component call sites**. COO's 1.783b was located instead in
`non_model_assets.json.enterprise_total` (= legacy model 1,550,840,086.23 + 232,313,972.65, composed
SERVER-side, never rendered). COO was right a second lineage existed and right to halt the resume;
the artifact was misidentified. Both recorded.

---

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| `comp-routes rewrites` | yes | **PASS** — parsed (not transcribed) the edited router and folded the new branch: `/api/general/mdpf/ -> platinum/mdpf/`. The structural check that the edit was representable. |
| `comp-routes behaviors` | yes | **PASS** — full 25-behavior map + edge associations; correctly disclosed DESIRED-plane, which is why I ground-truthed the live pin separately (Rule 22a). |
| `comp-grep` | yes (x6) | **PASS** — the load-bearing tool tonight. Printed denominators (404 files) are what refuted the scope-less-fetcher claim and cleared Mechanism B. |
| `comp-which` | no | Routed by hand; the questions were deploy-mechanics (plan diffs, CF pins) where the rail's own HUD nudges pointed at raw `aws`, which I ran with `# rail-checked:` markers. |
| `comp-iam` | no | No IAM change of mine. The bucket-policy grant was AE's lane; I grounded the deny/allow on the LIVE `get-bucket-policy`, which is the correct plane for a fresh change (Rule 22a). |
| `comp-freshness` | no | Freshness was AE's verified precondition; my axis was byte-identity of the SERVED body vs the platinum ETag, which `comp-freshness` does not answer. |

**What worked:** **reading the plan and asking whose changes they were** — that single habit caught
the S5 landmine. **Printed denominators** turned two contested claims into settled ones. **Byte-level
oracles** (served-body md5 == platinum ETag) made acceptance unfalsifiable rather than plausible.
**Positive controls on every probe** — including the one that caught my own 401 as a token expiry
(identical 36-byte bodies across two unrelated URLs) instead of a serve failure.

**What failed:** (a) **browser automation, 4 attempts, Edge launch timeout 180s** — Oracle-1 (the
rendered pixel) went unread by me and was routed to COO's D4; (b) `/tmp` resolved to
`C:\Program Files\Git\tmp` (unwritable) and broke `build-nodejs-lambda.sh` at `mktemp` — fixed with an
additive non-durable `mount -f` to the user temp the script's own comment assumes; (c) `aws s3 cp`
with a `C:/`-style destination silently wrote to a mangled `/cygdrive/c/cygdrive/...` path — caught by
checking the destination, cleaned up.

**Gap found:** **the owned-paths pre-commit hook is not merge-aware.** A merge commit necessarily
stages every incoming agent's files, so no lane grant can ever cover it; the only path is the audited
`GIT_COMMIT_AUTHOR_OVERRIDE`. Worse — **the audit line it wrote names the WRONG actor**
(`0.7.0_AE_CloudOps~A`, not me), because the hook resolves the actor from the shared
`.comp-graph/.agent_context`, which CLAUDE.md explicitly says is never an identity source. **An audit
log that misattributes is worse than none.** Surfaced to COO/CTO.

---

## Current State

- **LIVE SERVE:** the portal reads `opal-data-portal-v2/platinum/mdpf/*`. `public-data-router:6`
  pinned on both `/api/general/*` and `/api/general/json-tiered/*`; distribution `EVTSA9VEHNZVH`
  Deployed, 24 ordered behaviors.
- **LIVE PROD:** `80e21674`, tag `portal-v2.1.150`. Workspace submodule pointer `7194c90a84` ->
  `f6c11812`. Portal main tree on **DEV**; workspace CLOUD sync **0/0**.
- **Deployed bundle verified structurally** (`assets/ModelPortfolios-uqOGzf30.js`, 100,402 B, pulled
  from live PROD): `opal_aggregate_aua` x2, `non_model_aua` x2, `as_of_last` x2,
  **`getNonModelAumForDate` 0**; positive control `Total AUA`=1, negative control=0.
- **UNVERIFIED BY ME, STATED AS SUCH:** the rendered pixel. The headline SHOULD read
  **1,950,519,805.86** (served field byte-verified; fix is structural, no arithmetic between artifact
  and pixel) — **that is an INFERENCE.** COO's D4 field==pixel check is the reading. Also unread:
  the carried-point idiom and the "July 27th" as-of stamp.
- **Legacy untouched:** `json/mdpf/*` objects + their protective Denies unmoved throughout
  (`5f758b47` verified post-flip). Teardown remains the LAST cutover step, not done.
- **Detector re-baselined:** served-content reference is now the platinum object
  (`31e64570d3090eff4df3baab91d2a1dd`); `5f758b47` retains ONLY negative-control meaning.
- **JWT verify instrument:** one-night only, key + token wiped 01:55Z (absence positive-controlled),
  re-minted twice more during the promotes and wiped at close. **Never re-mint on this precedent** —
  a durable serve-verification identity is a designed artifact with its own review.

## Next Steps

- **[2.0.0_SA_COO]** **D4 field==pixel render check** — the one open acceptance item on both
  promotes; my browser automation is down. Also holds: the clobber-detector pin amendment (it lives
  in `org/projects/MDPF_MONOCLEANUP.json` `hazards[1]`, a CLOSED project — routed, not self-edited).
- **[0.4.0_DE_ClientPlatform]** The third change (donut/counts field-reads + bell-curve re-point to
  the platinum global account-distribution) — announce before pushing; I promote on green CI.
- **[1.0.0_SA_CTO]** Owns: the `platinum/` **active legacy writer** (underscore twins rewritten
  23:47Z, 2-partner signature) as a named teardown line item; the A.3 served-freshness instrument
  re-point; the owned-paths merge-awareness + audit-misattribution gap.
- **[unowned / morning]** The dangling `hotfix/global-monthly-axis-key` worktree at
  `C:/Users/AndrewBerman/Desktop/_portal_hotfix_wt` — `8fd61dbf` is IN PROD but NOT an ancestor of
  DEV; its CONTENT is in DEV (positive-controlled both markers), so nothing was reverted. Ownership
  hunt is a morning item.
- **[me]** Available. Holding promote authority for DE's third change.

## Blockers

**None.** Every open item above is dispositioned to a named owner with evidence. The one thing I
could not do — read the rendered pixel — is routed to COO's D4 and labelled an inference rather than
a claim.
