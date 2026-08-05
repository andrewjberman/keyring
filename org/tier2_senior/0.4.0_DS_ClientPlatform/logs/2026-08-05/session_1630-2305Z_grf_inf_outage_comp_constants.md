# Session 1630-2305Z — GRF scoping, the INF 5-day outage, and the comp-constants brief

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, SCRIBE

**Agent:** 0.4.0_DS_ClientPlatform (base, PID 18572) · **Window:** 2026-08-05 ~16:30Z -> ~23:05Z
(first log this session; whole session) · **HEAD at close:** `1ae1ac882`

---

## 1. Summary

Seated on COO's GO for the Andrew-named P1 (`MDPF_CANRTE.GRF`), delivered and closed it, then spent
most of the window on the **INF gold-chain outage that had been failing 5 consecutive days** — which
turned out to be one defect with two failure points, not the two independent blockers it was scoped
as. Ended by delivering an Andrew-requested brief on `comp-constants` as a gate surface.

**11 commits. Zero rollbacks. Nothing bypassed, no gate forced, no sentinel left open.**

---

## 2. Deliverables

| # | What | Commit | State |
|---|---|---|---|
| 1 | `MDPF_CANRTE.GRF` Global T+2 roll-forward SCOPING (design-only) | `d67659946` | RAVC-4 ACCEPTED, TO closed `51cd12630` |
| 2 | `data_contract.xml` correction (my core doc named a dead Lambda as live producer) | `d755d4193` | landed |
| 3 | `INF_D_00` unresolved-household diagnostic | `c98d3be8b` | landed + deployed |
| 4 | CTO Ruling-2: stale cottonwood sidecar = ABSENT | `5ca38064a` | landed |
| 5 | INF rep-10 allowlist, DS lane + 3 canonical entries | `8a8daae1a` | landed + DEPLOYED |
| 6 | `comp-constants` surface brief (Andrew-direct) | `b3e9a5368` | delivered to CTO base |
| 7 | Brief amendment: `index` deletes its own documentation | `9cfc470a1` | delivered |
| 8 | Phase-B plan: strike vetoed idiom (6 sites) + W-3 three->four legs | `b44f76ef0` | landed |
| 9 | INF serve-release (both sentinels) | `d7e9430e0` | DEPLOYED + verified |
| 10 | INF re-hold (both sentinels, same window) | `1ae1ac882` | verified EXERCISED |

### DS Briefs Written

| Brief | Path | Recipient | Status |
|---|---|---|---|
| GRF Global T+2 roll-forward scoping | `.../deliverables/MDPF_CANRTE_GRF_GLOBAL_T2_ROLLFORWARD_SCOPING_20260805.md` | COO + CTO | ACCEPTED |
| comp-constants gate surface | `.../deliverables/COMP_CONSTANTS_SURFACE_BRIEF_20260805.md` | 1.0.0_SA_CTO base | READ IN FULL; ruling HELD on Andrew's word |

---

## 3. The findings that carried the window

**GRF — the surface count is 1 of 3, not 3.** `comp-pipescript io` across all three of Andrew's
named surfaces exposed the dependency order (70 -> 80 -> 90). The carry lives at 80;
`aum-metrics` **inherits it by construction** and already emits a `carried` flag. Only
`account_distribution` needed design. A scope reduction earned by measurement.

**The composition gate cannot be the safety argument for a carried leg.** It is a within-date
identity and a uniformly vintage-shifted roster satisfies it exactly — evidenced in-source: global
7620 vs true 7554, **+66 at 0.86% of base, under every percentage floor, with the identity holding
7/7 dates while the sum sat on the wrong day.** The control must be a VINTAGE control, not a sum
control. COO carried this to Andrew (the symptom was on dates he flagged himself).

**The INF outage was ONE defect, not two.** COO scoped `INF_C_01` (NNA guard) and `INF_D_00` (int()
crash) as independent and asked for a ten-minute check. Measured on the artifact:
`account_team.parquet` `household_id == 'unknown'` -> `{4136,4139,4352,4356,4358}`; the guard's
reassigned-to-rep-10 set -> **identical, symmetric difference `[]`**. Five accounts moved rep 12 ->
10 on 07-31, rep 10 was absent from the allowlist, so they fell out of `accounts_v2` — starving the
guard AND leaving households unresolvable ten scripts later.
**Consequence (CTO drew it): the excusal is DEAD. $514,487.47 never left; nothing needed writing off.**

**Do not trade a loud failure for a silent one — even a visible one.** The natural `INF_D_00` patch
(bucket `'unknown'` as a counted, visible household) satisfies "no silent drop" and STILL destroys
the signal: next rep reassignment, the chain runs green with households bucketed to `firm`. **The
crash was the only detector of the upstream defect.** Kept it, named it, and put the reasoning
IN-SOURCE so a later reader reaching for a `try/except` finds it. COO named the third category:
a LEGITIMISED failure. AE~A reached the same conclusion independently.

**Consumer sets must be enumerated, not assumed — four layers deep, in one day.** W-1's re-point
grew from 1 -> 2 -> 5 consumers plus an IAM shape change: (a) the emitter, (b) a HARDCODED reader
config cannot fix, (c) **the producer reading its own prefix twice**, (d) a live trigger's
`head_object` gate. Each was invisible to the search that found the previous one.
The naming-layer instance: the INF rep roster lives under **three constant names**
(`INFLECTION_REP_IDS` / `PARTNER_REP_IDS` / `INFLECTION_EXTENDED`), so a name-keyed search finds one
alias and misses two.

**A STALE PLAN IS WORSE THAN A STALE FACT, BECAUSE A PLAN IS AN INSTRUCTION.** My own Phase-B plan
(authored 08-04, the day Andrew's shadow/comparator veto landed) still prescribed
`shadow -> 3-green -> swap`. Executing it would have built a shadow channel under a standing veto
**while citing an approved design document.** Swept all SIX prescriptive sites, not the one COO named
— fixing only that one would have left the doc still instructing a future reader to build a
comparator in Phase C. COO is carrying the generalisation to CTO.

**`6b/6c/6e` resolved nowhere; the real scope is FOUR legs.** Dispatched against a label that appears
in exactly two records, both USING and neither DEFINING it. Declined to guess (the letters skip
`6d`). Ground-truthed against `mdpf-daily-dispatch.sh:521-615`: they are dispatch stage-6 steps, and
the label had **silently dropped 6d (cottonwood)** while my own prose omitted **6c (non_model)** —
two errors that cancelled in count, not content. **W-3 = 6b/6c/6d/6e.**

**Diff the artifact, not the history.** CTO could not reconcile a commit list against a diff and was
going to keep `INF_D_04` held. Pulled the deployed S3 object and diffed it: **one line**, AoR tokens
3/3 identical. Both AoR commits (07-12, 07-13) PREDATE the deployed object (07-16) — already
shipped; only CTO's base was wrong. `git log` answers what changed in the REPO, not what is RUNNING.
CTO adopted deployed-bytes diffs as their default for serve-releases.

---

## 4. Instruments that reported green over an incomplete action (4 today)

1. **`comp-constants`** — blocked my commit of Andrew's own ruling because its hand-typed canonical
   had not caught up. *It was not detecting a defect; it was detecting that I had obeyed Andrew.*
2. **`comp-constants index`** — the tool's own sanctioned command silently deleted its config's
   46-line header, including the ONLY documentation of `sovereign_held_markers`. Caught by COO
   reading `numstat`, not by the review anyone would do (the canonical bumps were correct).
3. **`safe-deploy.sh`** — `exit 0` + *"all files deployed and verified"* on a run that deployed 9 of
   11 and **skipped the root-cause file**. Caught only by reading full output then checking live S3
   with a positive control. CTO took the defect as theirs.
   **REFINEMENT from the re-hold exercise:** the all-held branch prints a CORRECT summary
   (*"all deploy-scope file(s) are SERVE-HELD; nothing served"*). The bug is confined to the MIXED
   case — the deployed branch is written as if the held set were empty. Relayed; narrows the fix.
4. **My own `--since` filter** while writing this log — git read it as LOCAL time and silently
   under-reported my commits 11 -> 6. Caught by the count looking wrong.

**Common shape: an instrument answering a question ADJACENT to the one being asked.**

---

## 5. Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | producer of Global aum-metrics/account-distribution | PASS | near-tie, routed to `comp-pipescript io` |
| `comp-glob` | `**/dim_mdpf_*.py`, `**/mdpf_aggregate_aua.py` | PASS | with systems-context routing |
| `comp-pipescript io` | x4, all `--pipeline mdpf` | PASS | **the 70->80->90 order is the whole GRF finding** |
| `comp-pipescript deployed` | ETF builder, mdpf sweep | PASS | MATCH; confirmed the hardcoded consumer is LIVE |
| `comp-grep` | rep allowlist, prefix literals, SERVE-HELD | PASS | printed denominators; **flagged its own 0-file FAILED RETRIEVAL and a >=200 TRUNCATION** — both would have been false closure |
| `comp-constants check` / `index` | canonical drift + re-index | PARTIAL | caught my incomplete fix (3 aliases); `index` ate the config header |
| `comp-to` | GRF TO id | PASS | race-free session file |
| `commit-gate.sh` | every `.py` commit | PASS | clean throughout |
| `safe-deploy.sh` | 11 files, then 2, then re-hold exercise | PARTIAL | deployed + verified, but see §4.3 |
| `.tools/to-check.py --all --assignee` | seat backlog | PASS | **61 active TOs, not the 16 in `get_agent_status`** (pending-only slice); COO corrected their figure to Andrew |

**What worked:** `comp-pipescript io` produced the single highest-value structural finding of the
session. `comp-grep`'s denominator/truncation warnings prevented two false-closure errors.
**What failed:** see §4 — three estate instruments plus one of my own filters.
**Gap found:** `comp-constants` cannot express TYPE (the rep set is str-typed in one file, int-typed
in another); a derived canonical would "match" a site comparing strings to ints and never fire. CTO
banked it for the Kimi pipeline spec.

---

## 6. Deployment Sequence + Verification

```
RELEASE  d7e9430e0  SERVE-RELEASE-ACK (non-empty, own line) citing Andrew @93c898445
                    + CTO 2200Z/2215Z + COO NEVER#2 co-sign 2245Z
DEPLOY   safe-deploy.sh -> both files
VERIFY   s3://opal-data-inf/code/silver/convert_orion_api_to_silver.py
             2026-08-05 18:48:54  57,170B  :630  INFLECTION_REP_IDS = {3, 6, 10, 11, 12}
         s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py
             2026-08-05 18:48:59 219,634B  :125  INFLECTION_REP_IDS = {'3','6','10','11','12'}
         NEGATIVE CONTROL: _orion_api_silver_lib.py unchanged @17:38:29
RE-HOLD  1ae1ac882  sentinels restored BYTE-IDENTICAL (diffed vs pre-removal capture,
                    not retyped), same line numbers, same anchor
EXERCISE re-ran safe-deploy ->
             SERVE-HELD: convert_orion_api_to_silver.py -- committed but NOT served
             SERVE-HELD: INF_D_04.client_portal_summary.py -- committed but NOT served
             OK: safe-deploy -- all deploy-scope file(s) are SERVE-HELD; nothing served
         served timestamps UNCHANGED (18:48:54 / 18:48:59) -> the gate PREVENTED a
         re-upload. Behaviour-grade, not a config read.
```

Earlier in the window, 9 DS-lane INF scripts deployed + `comp-pipescript deployed` VERIFY OK.

---

## 7. Blockers

**None assumption-blocked.** All evidence-cited and all currently routed with named owners:

- **W-1a** — waits on **W-1b** (`0.7.0_AE_CloudOps`/DT, purely additive IAM). *Note: CTO ruled this
  re-gate at 1835Z and it died in the previous COO session's inbox; I only learned at 2253Z, which
  is why my broker status read BLOCKED for ~4h. Corrected.*
- **INF chain acceptance** — `0.7.0_AE_CloudOps~A` holds terraform apply + re-run.
- **CANRTE-W3** — sequenced behind W-1a by COO.

---

## 8. Current State (written for zero prior context)

- **INF outage:** the rep-10 fix is **LIVE ON THE RUNNER**. `s3://opal-data-inf/code/silver/`
  and `code/gold/` carry `{3,6,10,11,12}`; the 2026-07-12 script is gone. Both serve sentinels are
  **restored and exercised**. `AE~A` owns terraform apply (5 Lambdas) + chain re-run.
  **ACCEPTANCE IS NOT CHAIN-GREEN:** chain-COMPLETE **AND** the five `'unknown'` rows GONE from
  `s3://opal-data-inf/gold/views/account_team.parquet` **AND** no excusal entry.
  `account_team.parquet` is frozen at 08-01, so a green chain will NOT mean the portal is current.
- **`comp-constants.config.yaml`** — canonical bumped to `{3,6,10,11,12}` across all three names;
  header restored after `index` ate it. **Ferried and landed by `0.7.0_AE_CloudOps~A` under their
  author line** (DS is owned-paths refused; I declined the audited override).
- **GRF** — delivered, accepted, TO closed. Implementation surface for `0.5.0_AE_OpalETL` is ONE
  producer. **SEAT WALL HOLDS: Andrew brings that seat in himself; I have not routed the document
  to them.**
- **comp-constants brief** — with CTO base; ruling HELD pending Andrew's word.
- **Open, not mine:** `inf-api-txn/_orion_api_silver_lib.py` still `{3,6,11,12}` (AE excluded it
  rather than absorb pre-existing GUARD_B drift 50M/400M vs 150M/300M — correct); the `:341` latent
  cast (COO's seat); 7 `manual_api` sites left visibly drifted with stated reasons.

---

## 9. Next Steps

- **[0.4.0_DS_ClientPlatform] (me):** W-1a on W-1b landing (all five consumer legs, one window,
  consumer-side acceptance, no dual-read) -> CANRTE-W3-CONSOLIDATION on the corrected FOUR-leg scope
  -> COO's backlog live-vs-closeable read (61 TOs) -> `4.0.0_SA_CRO`'s RCG ferry (9 diagnostics, no
  urgency, correctly ordered last).
- **[0.7.0_AE_CloudOps~A]:** terraform apply + chain re-run + the three-limb acceptance. Optional
  tonight: silver+gold re-convert from today's 13:47Z bronze (zero egress — the Orion token died
  ~22:05Z); QA evidence only, tomorrow's scheduled run is the acceptance (NEVER#4).
- **[1.0.0_SA_CTO]:** comp-constants ruling on Andrew's word; the `safe-deploy` mixed-case summary
  fix (§4.3 refinement narrows it); the W-3 appetite question incl. the redundant promotion hop.
- **[2.0.0_SA_COO]:** the `:341` latent cast; the 7 `manual_api` drifted sites; relaying the
  safe-deploy refinement.
- **[Andrew]:** comp-constants options (unranked, §7 of the brief); the MDPF teardown appetite.
