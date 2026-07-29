# 2026-07-29 — 1630-2100Z: promotes #5 and #6, an oracle that saved itself, and the Cottonwood root cause

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE, DIAGNOSE

Two PROD promotes landed under a sovereign instruction that reversed mid-window. The re-specified
acceptance oracle earned itself on its first outing. A 3.5-hour-stalled order was escalated and, once
fired, produced the definitive Cottonwood root cause.

---

## Deployment Sequence + Verification (DT role requirement — actual output)

```
                        PROMOTE #5 (blend revert)          PROMOTE #6 (toggle removal)
source                  de/blend-cohort-interim-revert     origin/DEV a969d615
                        fa687486, parent == origin/PROD
PROD merge              b7c296dc                          67675b93
tag (PEELED-verified)   portal-v2.1.153                   portal-v2.1.154
CI run                  30474534946 success                30477873922 success
parity gate             0 bytes                            0 bytes
back-merge              a969d615 -> DEV (pushed)           n/a (DEV == PROD, converged)
pointer                 106ab56170                         NO-OP (see below)
base / rollback         83afea3f                           b7c296dc
held-language scan      0 hits                             0 hits
main tree after         DEV                                DEV
```
Both: typecheck 0 errors · Step-3 PROD re-assert · foreground `bun install` · VALGATE D-1 PASS ·
pre-push `tsc` PASS · `worktree remove` MAX_PATH failure -> `worktree prune` clean (DE removed the
#5 directory under Andrew authorization).

**#6's pointer bump was a genuine NO-OP and I said so rather than implying a commit:** the workspace
pointer tracks DEV, DEV did not move (only PROD did), so there was no gitlink change. The PROD sha +
tag live in the reports and this log instead.

**FINAL TOPOLOGY:** `origin/PROD` `67675b93` == `origin/DEV` — converged, 0 apart. CLOUD 0/0.

## Verified rather than trusted — both directions of the same invariant
```
BEFORE #6 (Andrew wanted the toggle removal OFF PROD):
  72f132c5 on PROD  NO    b0fc1e75 on PROD  NO    fa687486 on PROD  YES
AFTER #6 (he retracted; wanted it ON):
  72f132c5 on PROD  YES   trendMetricType LIVE-CODE refs  ZERO   DEV-not-in-PROD  0
```
**Probe surprise, resolved not waved through:** the `trendMetricType` count returned **1**, not 0. It
is the deliberateness COMMENT (`b0fc1e75`) — *"its absence is DELIBERATE -- do not 'restore' it as
missing functionality"* — i.e. the marker naming the removed symbol, working exactly as intended.
**Consequence recorded: a bare symbol-count probe reads 1 on that file forever.**

I also verified DE's branch before merging #5 rather than taking its report: parent `rev-parse` ==
`origin/PROD`, 1 file +45/-11, `BLEND_ARCHETYPES` restored, `excluded_unfunded_count` field reads
INTACT, **the forbidden cross-artifact subtraction ABSENT (0 hits)**, `^SURFACE_ACK:` anchored,
interim markers present.

---

## THE ORACLE SAVED ITSELF ON ITS FIRST USE

Committed the re-spec at `3e945f1cc4` (deliverables/`PROMOTE_ACCEPTANCE_ORACLE_SERVED_ARTIFACT_20260729.md`),
then used it ~2 hours later:
```
16:15:31Z publisher fire moved BOTH whole-object hashes:
  aggregate-aua-timeseries   -> 9d9e8a9e     account-distribution -> 82345931
CONTENT md5 (_provenance stripped), UNMOVED on both:
  d4546d9835785a34615a15a36404f680           6dadc83315c630841fd8bc5b97a406eb
```
**The OLD whole-object oracle would have FAILED promote #5 on both keys with nothing wrong.**

**Two corrections I took in this window, both from COO, both verified before accepting:**
1. **The publisher DID fire** — my 1621Z "not moved" read was a **CDN-cached** copy. I read the SERVED
   plane to answer a PRODUCER-RAN question. And the discriminator I called unavailable
   (`_provenance.written_at`) existed at ORIGIN all along. Rule 22a on the layer axis.
2. **Citation:** I quoted `e86ea2819d` for the spec — a MERGE authored *"Andrew Berman"*. Authoring
   commit is `3e945f1cc4`, confirmed via `git log --diff-filter=A -1 -- <path>`. **In a shared tree a
   merge lands under whoever ran `git pull`, so "the hash my push printed" is systematically wrong.**
   Same class as CLAUDE.md's own provenance note.
**COO then RETRACTED its own correction** (its "the page field-reads the object" premise was false of
v2.1.151 — the tile derived `7,597+183`). **I verified the retraction at source rather than accepting
it, having just accepted the original on authority — which was itself my error: I had the code in hand
and un-hedged my own correct reasoning without checking a mechanism claim.**

---

## THE 3.5-HOUR STALL AND THE ROOT CAUSE IT UNBLOCKED

Andrew ~1455Z: *"run the producer for cottonwood ad hoc RIGHT FUCKING NOW."* At 1825Z it had **still
not fired** — AE was LIVE, had ACKed in 4 minutes, pre-run its gates, asked CTO at 153819Z, and
re-tasked to other work when no word came. **I escalated hard (182459Z) rather than filing a third
"still waiting":** the run was blocked on a routing word alone, and I named the inversion — *holding
the run to protect a design decision that the run itself informs is backwards.*

**It fired 40 minutes later (18:59:04Z, DS~A) and produced the definitive answer:**
```
DEPLOYED aggregator (fca2b76c)  7,598  $1,550,092,796.50  cottonwood ABSENT
REPO     aggregator (2b07e99d)  7,890  $1,675,987,041.89  cottonwood PRESENT
DELTA                             292  $  125,894,245.39  <- EXACTLY cottonwood
```
**The deployed aggregator contains ZERO cottonwood-fold code** (`_cottonwood_sidecar`,
`COTTONWOOD_UNITS_KEY`, `cottonwood_fold`, `account_units.json`: deployed **0**, repo **2/5/1/1**). DS
ran the DEPLOYED copy with its deployed sibling deliberately — fresh inputs, rc=0, same exclusion.
**The stale-input hypothesis is dead; the exclusion is structural.** DS then corrected its own
"not tonight" framing: **the fold is written and works — it needs DEPLOYING, not writing.** COO's
independent delta agrees to **six cents**.

## MY TWO CONTRIBUTIONS TO THAT THREAD
1. **GOLD != PLATINUM != SERVED.** DS's `7,598` and the cottonwood series repair
   (`37,237 -> 80,429 B`) are **gold-plane**. Measured at origin 1905Z: platinum global is **still
   7,597 @ written_at 16:15:31Z**, cottonwood agg still 2 non-null points. **Nothing DS did tonight is
   on Andrew's screen and will not be until the publisher runs again.** I flagged this before relaying
   DS's numbers, because "it fired, here is the count" reads as live and is not.
2. **PRE-STATED THE ACCEPTANCE NUMBER BEFORE THE DEPLOY:** the tile will read **8,073**, not 7,890 —
   because Total Holdings is currently the client-side sleeve-level interim, so the artifact's 7,890
   gains the 183 blend cohorts (cottonwood contributes ZERO blend cohorts; measured). **Anyone grading
   the deploy against `total.account_count` would find a 183 gap and could call a correct deploy
   broken.** Reconciles with Andrew's remembered 8,041 (growth + the day's `7,597->7,598` drift).

---

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| `git merge-base --is-ancestor` (x8) | yes | **PASS — the invariant instrument.** Proved the toggle removal OFF PROD before #6 and ON PROD after, in both directions, rather than inferring from the merge. |
| `aws s3api head-object` / `s3 cp` (ORIGIN plane) | yes (x8) | **PASS** — the layer that answers "did the producer run". Produced the content-baselines and the finding that platinum never moved after DS's gold work. |
| python content-md5 (`_provenance` stripped) | yes (x4) | **PASS — first real use of the new oracle; it prevented a false failure on promote #5.** |
| `gh run view --json` (x6) | yes | **PASS** — twice the watcher died on TLS timeouts and the independent re-read showed success. A dead watcher is not a failed deploy. |
| `git diff origin/DEV HEAD` (parity) | yes (x2) | **PASS** — 0 bytes both promotes. |
| `git log --diff-filter=A -1 -- <path>` | yes | **PASS — the correct self-citation instrument**, adopted after the merge-hash error. |
| comp-* tools | no | Promote execution + origin-plane artifact reads + branch topology on known refs. No estate traversal, no new resource, no search; the comp-rail HUD did not nudge. |

**What worked:** **verifying the counterparty's claims before acting on them** — DE's branch (7 checks)
and COO's two corrections. And **pre-stating numbers before the event they grade** (the 8,073
projection, the re-pinned content baselines) so nothing can be rationalised afterwards.

**What failed:** (a) **I accepted COO's mechanism claim on authority with the source in hand** and
un-hedged my own correct reasoning — the deeper error of the day; (b) I cited a merge hash as my
authoring commit on a BINDING spec; (c) my `trendMetricType`-count probe was imprecise (comments count).

**Gap found:** **the compiler-tools shared-log append is RETIRED as of today (Andrew-direct)** — this
log carries its Compiler Tools section only, and I did not touch `org/compiler-tools-log.md`. Earlier
today that same file blocked my merge twice via hook-regenerated churn and a whole-file line-ending
rewrite; the retirement removes that class outright.

---

## Current State

- **LIVE PROD `67675b93` / `portal-v2.1.154`.** DEV == PROD (converged, 0 apart). Main portal tree on
  **DEV**. CLOUD **0/0**. No open deploy ledger, no worktree of mine.
- **Total Holdings renders 7,780** = artifact `total.account_count` 7,597 + 183 blend cohorts
  (the Andrew-authorized sleeve-level interim, `fa687486`, commented in-code as an interim with
  `total.sleeve_level_count` named as the durable successor).
- **The Value/Count toggle is GONE from PROD** — zero live `trendMetricType` refs; one comment
  reference, by design.
- **Cottonwood's 292 accounts are still absent from the serve.** Root cause: deployed aggregator lacks
  the fold. **The corrected aggregator exists in repo and produces exactly 7,890 / $1,675,987,041.89.**
  **Reaching Andrew's screen needs BOTH: the aggregator deploy AND a publisher run.**
- **Acceptance pre-stated for that deploy:** artifact `total.account_count == 7,890`; **tile == 8,073**;
  footnote == the artifact's own `excluded_unfunded_count`; non-mdpf control unchanged.
- **Content baselines (current, per the new oracle):** aggregate-aua `d4546d98…`,
  account-distribution `6dadc833…`. Whole-object hashes are NOT the instrument.
- **⚠ The tile is a client-side derivation again**, so `artifact == render` does NOT hold for Total
  Holdings. That property was knowingly spent on Andrew's word; the producer-stated
  `sleeve_level_count` restores it.

## Next Steps

- **[1.0.0_SA_CTO]** (1) the **aggregator fold deploy** — now the ONLY path to the 292, his gate;
  (2) whether the **publisher is invoked tonight** so DS's gold work (incl. the 80,429 B cottonwood
  series) reaches the serve or waits for tomorrow's 16:15Z; (3) the cohort-vocabulary question if the
  aggregation shape is revisited.
- **[0.4.0_DS_ClientPlatform~A]** holds the measured repo-vs-deployed delta and the composed
  cottonwood slice.
- **[2.0.0_SA_COO]** D4 pixel read — **it matters again** now that the tile derives client-side.
- **[unowned / morning]** dangling `hotfix/global-monthly-axis-key` worktree at
  `C:/Users/AndrewBerman/Desktop/_portal_hotfix_wt`.
- **[me]** IDLE. No promote pending — both remaining legs are producer plane. Available if the deploy
  turns out to need portal-visible work; I do not believe it does.

## Blockers

**None of mine.** Everything open is dispositioned to a named owner with evidence. My lane is idle by
correctness: the two remaining changes are an aggregator deploy and a publisher invoke, neither of
which is a promote.
