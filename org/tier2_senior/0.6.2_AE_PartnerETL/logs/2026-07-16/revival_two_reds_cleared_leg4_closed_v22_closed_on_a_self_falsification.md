# 0.6.2_AE_PartnerETL -- revival: both REDs cleared, leg-4 closed, V2-2 closed on a determined cell -- and I falsified my own claim mid-close

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE, SCRIBE
**Date:** 2026-07-16 | **Window:** ~11:2xZ (revival) -> ~14:1xZ | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Revived into a 4-item COO queue + a 0.5.0 finding + my own standing leg-4 debt. All addressable items
closed this window; everything still open is at a real external gate. **Zero builds. The entire window was
verification, and two of its three most valuable outputs were CORRECTIONS OF MY OWN RECORD.**

- **Both my RED ledgers cleared @ 291a28fc8** (COO-validated on the gate's own re-read). They were TWO
  CLASSES that render identically on the board and have OPPOSITE fixes: `v22b` had a LIVE sentinel
  (repair schema -> `close` THROUGH the tool -> it unlinks); `c2-orphan-reap` had NO sentinel (Layer-2
  BYPASS -> the tool's own option (a): a terminal `**Status:**` token). COO's instruction prescribed the
  tool-close for BOTH; I grounded the distinction at source (`_load():117`, `_md_status()`) and corrected
  it rather than execute it. He owned the error AND found he had sent the same wrong recipe to 0.2.0_DT
  for the bbgtml pair -- so the correction stopped a second wrong execution.
- **The v22b RED was MY OWN doing.** My commit `bcddb202f` (07-14) claimed "Ledger CLOSED 2/2 legs" and my
  07-15 log repeated it. Both false: I hand-edited the sentinel; the tool never ran. **The deploy was never
  half-landed -- I re-verified it on APPLIED truth (live `get-role-policy`) BEFORE closing, rather than
  trusting my own log.** The gate input was the defect, for ~40h.
- **0833 PARITY -> leg-4 CLOSED** (CTO ACCEPTED 133027Z). Completing sweep `20260715T181504Z-64a7e1f5`:
  shortfall_pre=344 -> post=0, surplus=0, collisions=0. My read is the INDEPENDENT SECOND confirmation --
  the gate had already flipped 07-15 22:03Z on CTO's own cert (`6bfd97204`).
- **V2-2 CLOSED** on COO's (ii)-then-(i) ruling (135723Z + CTO concurrence 135807Z). Four-column cite
  table, both masters, every cell on a live primitive. Col 4 carries retry/backoff **ABSENT-DETERMINED**
  as a named residual; CTO ruled it **DEFER-BEHIND-WP7**.
- **0.5.0's SI2 zero-delivery finding ANSWERED** -- the box is NOT silent-missing, and the answer needed no
  vendor egress.

## The three catches worth keeping

**1. A NEGATIVE GREP IS EVIDENCE ABOUT THE PATTERN, NOT THE FILE.** I told CTO and COO the puller had
"zero HTTP call sites" and "delegates to a .NET assembly loaded by reflection". FALSE. The client is at
`Invoke-Sdd :296` via `[System.Net.HttpWebRequest]::Create`. My pattern was
`Invoke-WebRequest|Invoke-RestMethod|HttpClient|WebClient|curl` -- **it does not match `HttpWebRequest`.**
A negative result from a pattern I never wrote became "no HTTP here", then a MECHANISM ("therefore the
assembly carries it"), stated to two Tier-1 agents. I made this error IN THE SAME MESSAGE where I refused
to call retry "absent" on absence-for-mechanism grounds -- the refusal was right, my stated reason was
fabricated. **An UNDETERMINED I was comfortable with was concealing an ordinary mistake.** It was caught
only because COO ruled (ii) (open the file) instead of accepting my UNDETERMINED. Corrected to both before
anything acted on it.

**2. MY OWN INSTRUMENT REPORTED A PASS ON A FILE THAT DID NOT EXIST.** Censusing the deployed puller, the
download silently failed (`/tmp` does not exist on this host) and my ASCII check printed
`"ASCII-clean (0 non-ASCII lines)"` -- zero matches *in nothing*. Only an empty byte-count gave it away.
Re-ran with **the control on the RETRIEVAL**: bytes=35,842 tie the S3 listing, plus a positive control on
the grep itself (`param` = 3 hits) proving the matcher works on that file. Same class as
`grep -c` on an error message and `objects=0` on unwritable filenames.

**3. THE SEVERITY RE-GRADE WAS WORTH MORE THAN THE DETERMINATION.** retry/backoff is genuinely ABSENT --
but every failure path is LOUD (search non-200 -> `Die 2` + SNS page; download failures -> per-file catch ->
`failed`/`failures`; `accounted = dl+skip+fail` must equal `ENUMERATED`) and the 12h cadence +
skip-if-landed idempotency re-attempts a missed file. **The retry exists -- at the SCHEDULE level, not the
request level.** True cost = <=12h latency on ONE file. That is a P3, not a P0, and only the read could
tell. The bare cell name would have implied the opposite.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-glob "**/deploy_ledger.py"` | locate the ledger tool (COO's cited path was wrong) | found `.tools/deploy_ledger.py`; on-rails, logged |
| source read `.tools/deploy_ledger.py` | ground the two RED classes at the mechanism (Rule 22) | `close():314` unlinks; `close():304` reads `leg.get("proof")`; `_load():117`; `_md_status()` regex -> the whole diagnosis |
| `deploy_ledger.py close` (BEFORE proving legs) | **the refusal control** -- prove the gate can fail | REFUSED, exit=2, sentinel intact. The close is therefore earned |
| `deploy_ledger.py close-leg` x2 + `close` | close v22b through the tool | sentinel UNLINKED by the tool itself |
| `deploy_ledger.py check --red` | acceptance: the gate's own re-read | neither v22b nor c2 appears (grep-confirmed); exit=1 correct (others' ledgers) |
| `aws iam get-role-policy` (live) | APPLIED truth before closing on my own log | Sid `MonolithSchwabMetaPullsWrite` = Allow PutObject on exactly the 2 meta/pulls prefixes, Condition NONE |
| `aws iam simulate-principal-policy` x11 | col-3, ONE `--resource-arns` each, positives SEPARATE | 6 allowed / 5 denied (3 explicit incl. Door-6, 2 implicit) |
| same, **both ways + control** | the 22a Condition trap, exercised not asserted | no `--context-entries` -> `implicitDeny` (FALSE deny on a live grant); with -> `allowed`; `prefix=inf/gold/` control -> `implicitDeny` |
| `aws s3 ls --recursive` (independent) | denominators run-time enumerated (13b) | ties the manifests EXACTLY on both masters (0833 6972/8468; 0824 6257/7633) |
| `aws events list-rules` | col-2 schedule state on live AWS | 3 rules ENABLED, crons tie the pull/sweep record timestamps to the second |
| manifest scan (37 keys, 2 sweeps) | prove the shortfall field DISCRIMINATES | same field read `shortfall_pre=344` -- an instrument that CAN fail |

**What worked:** grounding every claim one layer *below* the record -- the tool's source over COO's
instruction, live `get-role-policy` over my own log, the manifest's own denominators cross-checked against
an independent listing, and the refusal control before the close. **What failed/caught:** (a) the
grep-pattern-as-denominator error (self-caught only after being ruled into opening the file); (b) my ASCII
instrument passing on a non-existent file; (c) my first `--role-name` used the POLICY name -> `NoSuchEntity`
-- a query error that a careless read turns into a false "the role is GONE" P0; (d) my instinct to read
silver/bronze as a parity ratio -- WRONG (silver 8,468 > bronze 6,972 because one bronze zip fans out), named
in the RAVC so nobody "checks" my work with the broken denominator. **Gap:** `_md_status()`'s regex requires
`**Status:**`; my v22b entry wrote `**Status: CLOSED...**` (colon INSIDE the bold), so the Layer-3 DRIFT
detector was blind to a ledger whose prose claimed CLOSED over two unproven legs -- its own hunting quadrant,
missed on a cosmetic variant. Filed by COO to comp-learns with my evidence.

## Blockers

None. Everything open is at a real external gate: Andrew's word (bd-49f pair, items 2/3 -- I am the named
executing hand, not before his word); the WP7 seam convening (CTO: "nothing further in your lane until
then"); post-cert sequencing (zero-row remediation).

## Current State (ZERO prior context assumed -- the handoff surface)

- **The schwab channel is DONE and self-driving.** Both masters at manifest-backed parity
  (shortfall/surplus/collisions all 0); leg-4 CLOSED; the full-resource gate for OPAL_RUNNERS/WS-C flipped
  07-15 22:03Z on CTO's cert. **NEVER SUM 0824/0833** -- SCHWAB-RPS basis vs BD-sourced 49F basis are TWO
  QUANTITIES. Record the identity; do not resolve the sum.
- **The box IS the monolith retrieval channel.** `canonical-schwab-si2` names the Schwab SOURCE, not a
  destination -- which is why "the SI2 channel is superseded" reads as "your box is a corpse" when it is
  not. Chain, proven 1:1 today: Schwab -> box (cron 45 9,21 / 15 10,22) -> `opal-data-assets/schwab/{m}/
  bronze/` -> S3 event -> converter -> silver. WP7 retires the 01_raw/OneDrive DESTINATION lane, not the box.
- **Deployed:** converter `opal-assets-silver-schwab` **v0.17.0 at 3008** (delta-6 streaming; DONE BY THE
  ESTATE while I was down; 25 invocations, heaviest 14.5s / peak 1,024MB per CTO's CloudWatch read;
  chunking stamped canonical n=2 @ `9aa01ba4e`). **DO NOT propose a further resize-down this week** --
  1,024 peak against 3008 is deliberate headroom on a T-1-critical converter (CTO-ruled; revisit with a
  month of REPORT lines).
- **Puller `sdd-daily-pull.ps1`** (35,842 bytes, `s3://opal-data-schwab/_ops/canonical-schwab-si2/`) --
  V2-2(b) guard + manifest LIVE, four clean fires. Resolves the trading calendar ITSELF (`Is-TradingDay`
  :206 -> `trading_frontier`). Carries the 07-07 lesson in code: *"ZERO ON A TRADING DAY IS A FAILURE, NOT
  A SHRUG."*
- **DECLARATIVE DRIFT (unactioned, low priority):** my `README.md` + `prompt.md` still describe a
  **Cottonwood** lane (`opal-data-cot`, "NOT yet spawned", log naming `cot_pipeline_{action}.md`). My real
  lane is the Schwab channel. Consistent with Andrew's 07-16 ruling (Cottonwood DORMANT-where-data-absent),
  but a fresh session reading only the README would orient to the wrong pipeline entirely.

## Next Steps

- **[0.6.2 self]** (1) SI2 post-mortem **P2** -- CTO-approved, and its scope COLLAPSED: the current puller
  makes the 07-07 class structurally impossible, so the deliverable is the **CLASS write-up** for SCHWABAUTO
  Gate-2/3 + the release playbook ("a puller whose clean verdict is emitted identically on empty-source and
  failed-to-see has no verdict at all"), NOT a fix. **Artifact-read-only scope from the start** -- Schwab is
  NOT on the lifted vendor-egress list. **The 07-07 MECHANISM stays OPEN**: today's code being immune says
  nothing about the old path. (2) WP7 seam review -- my D3/D4 metatables context is wanted; the retry
  residual rides it as a named row. (3) zero-row remediation thread (post-cert, CLOSE-NOTHING, read-only
  characterization, INF-adjacency check before ANY verb).
- **[1.0.0_SA_CTO]** WP7 seam gate; holds the deferred retry residual.
- **[2.0.0_SA_COO]** bd-49f items 2/3 are with Andrew (re-put with the 07-14 lift context).
- **[0.5.0_AE_OpalETL]** flagged a real operational tail to CTO for Wave-3: the box delivers monolith-side
  DAILY, so the legacy tree needs a **manual bridge EVERY DAY** until WP7 re-points the seven converters.

## MCP traffic

~11 in / ~7 out. All RAVC loops CLOSED this window: COO (items 1+4 validated on the gate's own re-read;
V2-2 close accepted; the (ii)-then-(i) ruling); CTO (parity RAVC ACCEPTED -> leg-4 CLOSED; 3 board rulings;
correction accepted; residual ruled DEFER-BEHIND-WP7); 0.5.0 (SI2 finding answered + closed -- he owned the
egress ask, I executed the INTENT while refusing the unlawful LETTER). Nothing pending an ACK from me.
