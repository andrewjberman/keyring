# Session log — 0.4.0_DS_ClientPlatform~A — 2026-07-29 1645Z-1910Z (--only build + the A/B that answered it)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE (primary result), DEPLOY

**Window:** continues `lane_A_cottonwood_conformance_design_1523-1645Z.md`.

## THE HEADLINE: THE COTTONWOOD EXCLUSION IS A DEPLOY THAT NEVER HAPPENED

Two AD-HOC read-only runs of the SAME producer, `--firm global`, same session, same inputs, each in an
ISOLATED dir with its OWN crosswalk sibling so `sys.path.insert(dirname(__file__))` could not resolve
a hybrid. **One variable: which copy of one file executed.**

```
DEPLOYED (fca2b76c, fold tokens 0)   7,598   $1,550,092,796.50   cottonwood ABSENT
REPO     (2b07e99d, fold tokens 2/5/1/1)  7,890   $1,675,987,041.89   cottonwood PRESENT
------------------------------------------------------------------------------------
DELTA                                  292   $  125,894,245.39
```

**The delta is cottonwood: COO's independent figure is 292 / $125,894,245.45 -- 0 accounts and 6 cents
apart** (rounding across two separately-aggregated same-day totals).

> **THE FOLD IS WRITTEN, WIRED, AND CORRECT. IT WAS NEVER DEPLOYED.** So the fix is a **DEPLOY of
> existing code**, not development.

**Why this run was necessary and the earlier two were not sufficient** -- three measurements, three
different questions:
1. *textual* (morning): deployed carries 0 fold tokens, repo 2/5/1/1 -> the copies DIFFER.
2. *behavioural-on-deployed* (18:59Z): 7,598, cottonwood absent -> the deployed copy IS the defect,
   and stale inputs are NOT (inputs were fresh and it still excluded).
3. *the A/B* (19:04Z): repo returns exactly +cottonwood -> **the repo copy WORKS.**

**(1) and (2) cannot distinguish "fold present and correct" from "fold present and broken"** -- both
look identical in a token count and in a deployed run. Only the controlled A/B discriminates.

## What else happened

### `--only <DST_KEY>` built, deployed, LIVE (CTO 182812Z, freeze lifted narrowly)
`build_portal_gold_accrual.py`. Commit `499d956cc2`; deployed `md5 cfc88b0b72d4f2a89eff0f5bf35e49ca`,
LM 18:44:34Z, **verified by re-DOWNLOADING the object and hashing it, not by the upload rc.**
Scopes to one planned destination; does NOT itself permit a clobber (pair with `--allow-overwrite` --
the pair is the deliberate signal, and R5 stays armed for the other ten).

**The load-bearing part is the REFUSAL, not the filter:** a `--only` key matching nothing planned is
FATAL and prints all planned keys, because a typo would otherwise write nothing and exit clean, and
`written=0` reads as success. CTO: *"the sixth instance today and the first one PREVENTED rather than
discovered."* Exercised both ways (valid -> SCOPED 1 of 11; bogus -> refuses + lists 11).

**Disclosed limits:** rc=1 in BOTH controls but for different reasons (SystemExit vs the pre-existing
3 aum-metrics R4 errors) so **rc cannot distinguish refused-from-ran -- read the log**; and the WRITE
path under `--only` was UNEXERCISED by me, so AE~A's baseline-all-11 / exactly-one-ETag-changed
after-check is the real control. AE~A's write then landed: `dd4d21a8/37,237B -> a95153ab/80,429B` at
18:49:54Z -- **the first object that bridge has ever successfully written.**

### R5 was blocking the repair, and the run reported no failure
The 17:44:13Z bridge run: grant healthy, zero AccessDenied, all 11 planned correctly -- and
`DONE written=0 skipped_existing=11`. **R5 refused a SAME-DATE CORRECTION**: my composed slice and the
stale object share `as_of 2026-07-27`, so the guard could not tell "already correct" from "already
wrong." Found by reading the run log, not the rc.

### DS base died holding a live fire order (5th session-edge loss today)
Called on **three independent signals** -- roster absence (from a list that INCLUDES stale), no watcher
process, undrained top-level mail. **Detected only because base's unread mail HALT-BLOCKED MY PUSH.**
Did NOT self-assign; CTO had written "DS~A does not fire," so I returned it to him and he re-routed.
Base respawned 1851Z, confirmed stood down, executed nothing -- no double-fire.

### Records corrected
- **My own inference:** the design said the served platinum object "IS Andrew's screenshot exactly."
  That collapses *object contents* with *what the page renders*. Re-derived with a NEGATIVE CONTROL
  (legacy plane 47/47/56 would render a visibly RICHER chart than he described; platinum 2/0/0
  matches). **Prompted by DE retracting the identical collapse, not by my own review.**
- DE's route trace then **REFUTED** its mixed-state hypothesis outright: `public-data-router` evaluates
  the mdpf special case BEFORE the `/json` fallback, so the whole family resolves to `platinum/mdpf/`.
  Three instruments, three planes, one answer -- and neither was sufficient alone (`comp-routes` is
  DESIRED-plane; my control is runtime but family-scoped).
- **Attribution:** base credited AE with my 15:52:29Z write. Corrected.
- **My own churn:** a one-line edit to `org/compiler-tools-log.md` became a 28k-line CRLF rewrite and
  swept 4 lines authored by DE + CVO into my commit. Content verified intact (7 insertions/1 deletion
  ignoring line endings); end state is the canonically-normalized one. Self-disclosed.

### ANDREW-DIRECT ~1800Z recorded verbatim + broadcast (@b5b00dc1c3)
`/json` deprecated for the three MDPF families -> `platinum/`; portal must never call
`opal-data-assets`. **Scope carried with the quote: working guidance, NOT law, not XXX.md.** Surfaced
the tension -- **deprecated is not unread** (live readers remain, incl. two reaching Attribution and
Positioning; my own WI-2 producer still emits `json/portfolios/aum-metrics.json`). Ordering:
**repoint-readers-THEN-retire-emission.** COO adopted it into its teardown wave; MSTR ACKed.

## Decisions I made and stated as decisions, not omissions
- **Did NOT upload either account-distribution run.** The deployed run's output is *wrong* (writing it
  makes a wrong number look freshly produced); the repo run's output is *correct*, which makes it more
  tempting to land, not less -- **landing it would be a code deploy performed as a data write.** The
  right path is Rule 13 on the file. CTO accepted both.
- **Did NOT propose the deploy.** The repo copy carries **83 differing content lines**; I verified the
  cottonwood-fold subset only. *"The fold works"* is not *"every other change in that file is safe"* --
  ~70 lines need reading before it lands.
- **Did NOT chase the `7,553` anomaly** (CTO: hold it). One free fact: it is **byte-identical across
  the deployed and repo runs**, so it is a FIXED reference read of some served object, not a computed
  value. Live set: **7,553 / 7,597 / 7,598 / 7,890** -- a definitions problem, not arithmetic.

## Blockers
None. Everything open is on CTO's word: the label fix (vocabulary settled with DE -- `absent` + a
non-enum sibling field), the aggregator deploy, WI-2, the retirement pair.

## Current State
- `--only` LIVE, `md5 cfc88b0b72d4f2a89eff0f5bf35e49ca`, commit `499d956cc2`.
- Composed cottonwood slice **on the served plane**: gold key now `a95153ab` / 80,429 B; cottonwood
  model series 2/450 -> 50/450 (2026-05-28..07-27). Client-visible (route trace confirmed).
- **Served global account-distribution UNCHANGED** and baselined: ETag
  `82345931bea1a1631057e13abb6e36f2`, 7,233 B, LM 16:15:32Z, `total.account_count` 7,597, period 07-28.
- Cottonwood's `account-distribution` period **2026-07-24, did NOT advance** -- mixed-basis objection
  does not dissolve; the producer still owes a stated basis rule.
- Nothing of mine written to any served path this window. All runs AD-HOC.

## Next Steps
- **[1.0.0_SA_CTO]** deploy-vs-build decision on `dim_mdpf_account_distribution.py` (it is a deploy);
  the label-fix word; scope the 7,553 definitions question; the disclosure sentence to Andrew.
- **[0.4.0_DS_ClientPlatform~A]** (me): label fix on his word; read the remaining ~70 lines of the
  aggregator diff if the deploy is routed to me.
- **[0.4.0_DE_ClientPlatform]** render steps 1-2 (band guard + carry `pointClass` through `:1323-1331`);
  pings me when they land, which flips the 32 dates from (A) to (B).
- **[2.0.0_SA_COO]** teardown wave: my blocker discharges when the platinum repair lands; its `:567`
  silent-default reader and ~C's smartx pair still bind.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript deployed` | `build_portal_gold_accrual.py` (full path) | PASS | pre-deploy check; used the FULL PATH per the bare-basename defect filed last window. |
| `comp-surface-check` | via `safe-commit` x5 | PASS | no critical surface touched. |
| `comp-pulse` (risk-reflex) | every commit | CLEAN | measured, denominator printed (1-2 files vs 1484 danger nodes). |
| `comp-grep` | prior window | — | carried; this window's questions were artifact/runtime, not graph. |

**What worked:** the deployed-vs-repo A/B is a comp-tool-shaped question no comp tool models -- it
needed two isolated interpreters and one changed variable. `comp-pipescript deployed` with the full
path behaved correctly this time.
**What failed:** nothing new; last window's `comp-pipescript` CRLF false-STALE and bare-basename silent
zero both still stand as filed.
**Gap found:** none new. The filed gap (compare CONTENT not raw bytes; ERROR on unresolvable bare
basename) is unchanged and still worth building.
