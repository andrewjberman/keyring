# 0.7.0_AE_CloudOps — 2026-07-24 session (1314–1605Z)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE

Ruled queue from COO (3 items). **All three closed this session.** One live trigger remains
(AC5 leg B, next scheduled 13:30Z run) and three items sit correctly in other lanes.

---

## THE SESSION IN ONE LINE

The P1 check's **premise was false**, and grounding it instead of checking on top of it is what
produced everything else. Two artifacts were found **committed-but-undeployed by two different
mechanisms**, one caught on the near side and one 41 days late.

---

## 1. EXCUSALS — a premise defect caught ~8 minutes before it would have cost a third day

P1 was the 6d-wiring outcome check, premised on "today's INF chain clears INF_C_01." It did not hold.

`data/inf/scripts/gold/lib/nna_coverage_excusals.json` @`8ba56144e` was committed 2026-07-23 — its own
commit message reads *"Unblocks INF_C_01 for tomorrow's 1347Z chain run"* — and was **never staged**.
The runner still held the 1-account 2026-07-17 manifest.

| | value |
|---|---|
| DEPLOYED (before) | ETag `5c60c95231dd51fa9b82d21ca49bae70`, 769 B, 2026-07-17T17:24:57Z, `excused_accounts={237}` |
| LOCAL/HEAD | md5 `234d6cc4a8aeb8f30c18836e0b721cca`, 4593 B, `{237,560,609,703,1225}` |

Mechanism source-confirmed: `nna_coverage_guard.py:131-132` resolves `_EXCUSALS_PATH` beside its own
module; `EC2_MANIFEST.json:364` records the S3-pull model. **Coverage denominator:** 29 keys under
`code/gold/lib/`, 29/29 byte-compared → 28 MATCH, 1 STALE. *Self-correction: my first sweep flattened
basenames and mis-paired 8 `lib/tests/*` rows; re-ran path-correct before reporting.*

CTO GO 133738Z (5 conditions). Staged **13:39:36Z**. Ledger `20260724T1339Z` CLOSED 2/2.

> **THE NEAR-MISS, recorded as luck not competence.** The gold runner LAUNCHED at **13:36:49Z — 2m47s
> BEFORE my cp**. Had the code sync happened at boot I would have staged into a run already holding the
> stale manifest, **and no S3-layer check could have told me** (head-object returns the new ETag either
> way). I read the live box over SSM instead: on-instance md5 matched HEAD, mtime **13:41:02Z**, all five
> accounts, sibling guard module in the same dir. **Cleared it by ~85 seconds.** `sync_scripts()` runs in
> the *dispatched* script, not the boot path — so the deploy deadline is the **dispatch sync**, ~4 min
> after instance launch. Landed in `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md` (COO committed
> @`3182d969d` — BASE_EXEC lane, see §5).

**ACCEPTANCE (exercised, Rule 22a):** `gold/meta/pipeline-complete.json` advanced off its
2026-07-18T14:59:10Z freeze to **2026-07-24T15:01:40Z** — first advance in 6 days.
Body: `{chain:full, run_date:2026-07-24, completed_at:2026-07-24T15:01:39Z, instance_id:i-0ed5afded2ebd4ed4}`
— the **same box** whose manifest I verified at 13:41:02Z. **Discriminating negative held:**
`pipeline-failed.json` UNCHANGED at 2026-07-23T14:56:25Z (yesterday's identical run wrote a FAIL there).
No ad-hoc trigger (NEVER#4).

## 2. 6d-WIRING — UNEXERCISED for a 7th day, WITH ITS CAUSE

Reported as unexercised, never as a pass and never as silence. **Both hypotheses I offered CTO at 15:04Z
were wrong**, and I declined to pick between them; the mechanism answered it at 15:26Z, inside his 15:35Z
window.

- **The Door-6 trigger FIRED and is HEALTHY** — `/aws/lambda/mdpf-daily-trigger` RequestId
  `bc7e0e00-b4b7-4316-8fc1-0ce8c22415a9`, START 15:01:41Z, ~1s after the marker, clean END/REPORT.
  First real exercise since 07-18.
- **The dispatch DEFERRED by design:** `dispatched:false, deferred:true`. 49financial
  `schwab/silver/rps` `latest_partition 2026-07-15`, `trading_days_behind 7`, `max_lag 2`; inflection
  fresh at 2026-07-24.
- **NEVER#1 CHECKED, not assumed:** the gate computes on the trading-day frontier
  (`expected_last_trading_day 2026-07-24`). I verified the frontier independently on its own IAM-granted
  prefix — newest is `date=20260715`, and 07-16/17/20/21/22/23/24 = exactly 7 trading days. **A genuine
  stall, not a weekend artifact.**

**My limb:** marker ABSENT; **11/11 keys checked**, fresh=0 stale=11 absent=0; cottonwood
`covered_dates=['2026-07-21','2026-07-22']` **HELD at len 2** — no regression, no growth.
Instrument was control-passed against the known pre-run state **and mutant-tested on the FRESH branch**
(a branch that never fires is not known to work). DS second-reader values matched exactly.

> **THE PATTERN IS THE FINDING:** third straight day unexercised, **third DISTINCT cause** — 02:10Z the
> producer was frozen; this morning the guard would have failed; now the guard clears and the dispatch
> defers upstream. **Each day a different layer.** A component whose every prerequisite fails in turn has
> never been tested, and the count of days is not a measure of its health.

### 2a. A REAL DEFECT — the discriminator that cannot discriminate

The DEFER reason was `ROLL_SOURCE_UNREADABLE`, whose own source calls it *"403: the INSTRUMENT is broken
(missing IAM grant) ... must be LOUD ... so mdpf-freshness-checker can alarm on it and never on ABSENT."*

**That classification is wrong — the true state is `ROLL_SOURCE_ABSENT`.** The gate heads
`platinum/mdpf/aggregate_aua/2026-07-15.json` on `opal-data-portal-v2`; the prefix holds 07-18/17/16/10/08
and **no 07-15 object**. The role holds `GetObject` there but its only `ListBucket` statement is on
`opal-data-bd` (prefix-conditioned). **S3 returns 403 not 404 for a missing key when the caller cannot
list** — so an absent object presents as AccessDenied.

> **The instrument built specifically to keep "it does not exist" apart from "I cannot read it" CANNOT
> keep them apart — its discriminator is the 403/404 status, and that status is a property of the
> CALLER'S ListBucket GRANT, not of the object's existence.** Its docstring cites the incident where
> *"'cannot read it' and 'it does not exist' print the same nothing"* as the reason the three worlds must
> never collapse. **They collapsed anyway, one layer down, inside the discriminator itself.**

Consequence is not cosmetic: DEFER is unchanged (all three reasons defer), but the **reason drives
alarming** — so it fires a config alarm for a fault that does not exist and sends the responder to fix a
grant that is already correct, while the real condition sits behind the wrong label. **False-outage class
in a new costume.** Fix routed, APPROVED IN PRINCIPLE (CTO 152226Z), sequenced behind Andrew's MDPF work;
**grants no new data access** — ListBucket buys *discrimination*, not reach. **Acceptance is behavioral:
observe the reason flip UNREADABLE→ABSENT on the next fire, not a policy read.**

### 2b. MY OWN INSTRUMENT LIED, and only the separately-run control caught it

`simulate-principal-policy` returned `implicitDeny` for the TARGET (ListBucket on portal-v2) — which
looked like clean confirmation. The **positive control, run as a SEPARATE invocation** (ListBucket on
`opal-data-bd`, which the policy **explicitly grants**) **also** returned `implicitDeny`. Control failed →
target result worthless. Cause: that statement carries a `Condition` block and I passed no
`--context-entries` — **Rule 22a false-deny mode (2), verbatim.** I discarded the simulator entirely and
grounded on the full policy document (denominator: 1 inline policy / 10 statements / exactly one
ListBucket statement; 1 attached = `AWSLambdaBasicExecutionRole`, no S3). **Without that control I would
have sent CTO a confident wrong-mechanism claim he would have routed an IAM change on.**
**Honest residual:** the 403 has NOT been reproduced *as* the Lambda's role — policy-and-semantics
grounded, **not behavior-exercised**.

## 3. inf-bronze AC5 — 41 days latent, now deployed and behaviorally exercised (LEG A)

Hit CTO's STOP condition and **executed nothing** until ruled: live behavior diverged from the task
premise in two structural ways.

1. **S3 staging does NOT deploy this artifact.** `user-data.sh:6` *"Runs ONCE on first boot"*; the S3 pull
   is at `:44` **inside** that bootstrap. Every later boot runs the **baked** copy — an S3 stage is
   **inert** until instance replacement, and an S3 ETag reads GREEN throughout.
2. **AC5 is unreachable without a real bronze pull** — `:47-51` and `:53-59` both `exit 0` **before** the
   AC5 block at `:141-154`.

**Why 41 days:** the June bundle `20260612T2200Z_inf_bronze_fix_bundle` CLOSED as *"RECONCILED-NOT-APPLIED"*
while its own manifest recorded the fetch-script legs (`:25`, `:26`) and the AC5 leg riding them (`:30`)
as **OPEN**. Not a stranded deploy escaping a gate — **a gate working correctly and the residual
evaporating because nothing owned it.**

CTO ruled **option C**. Ledger `20260724T1524Z` CLOSED **6/6**:

| leg | proof |
|---|---|
| L1 s3-prefix | ETags == local md5 (explicitly **not** the deploy) |
| **L2 deploy** | **BEFORE on-instance md5 `70d6fdc4` — the box was EXECUTING 41-day-old code.** AFTER `de2addad…` == HEAD |
| L3 DEFERRED | `SHUTDOWN_DEFERRED` + metric Sum=1.0 @15:31:00Z, box stayed up; sleeper in pgid **2196** vs probe **2181** |
| L4 ARMED | `SHUTDOWN_ARMED` + metric Sum=1.0 @15:33:00Z + **instance running→stopped at 15:34:07Z** |
| L5 net state | stopped as found — and the **tested mechanism** stopped it, not an operator |
| L6 manifest | `6806212e9` |

The probe **extracts the AC5 block verbatim from the deployed script** (marker-anchored) rather than
reimplementing it — a reimplementation can drift and then tests itself. The different-pgid sleeper is
load-bearing: same-pgid would be correctly ignored and **pass for the wrong reason**. ARMED **refuses**
(exit 3) if anything matches, so it cannot test DEFERRED while claiming ARMED.
**Safety:** boot logged *"Mode marker absent … skipping bronze-pull"* — **no pull, no partition rewritten.**

> **LEG A IS NOT ACCEPTANCE. LEG B IS** — the first *scheduled* 13:30Z run carrying `SHUTDOWN_ARMED` in
> its own log. No run manufactured (NEVER#4). Banked as a durable memory trigger, **not a cron** — a cron
> dies with the session.

## 4. deploy_ledger — item (a) done, item (b) written and blocked

**(a)** `4046dc24a`. **All 3 flagged ledgers are CLOSED IN FACT** — the RED was a **legibility artifact**.
Method: imported the live module and ran **its own** `_md_status()` / `_has_close_marker()` /
`_is_terminal_status()`, with **two known-readable ledgers as positive controls** (2/2 parsed; the 3
flagged returned None/False on both limbs). *An all-None column across five files would have meant a
broken probe, not three findings.* Two shapes, both invisible to **line-anchored** limbs: a mid-line
`**Closed:**` after a `·` (2), and a bare unbolded `CLOSED:` (1). All three **UNINDEXED / hand-authored**
— never written by `deploy_ledger.py`, which is **evidence** CTO's writer-drop was right.
One evidence-cited stamp on `mdpf-allfirms-serve` (mine to disposition; no sentinel, so the
`.md`-is-a-RENDERING contract does not reach it). **Verified discriminating:** re-ran `check --all` — that
entry cleared, **the other two still flag.** CTO ruled **D — a third reader state: UNREADABLE ≠ UNCLOSED**;
no matcher loosened.

**(b)** `76f3ed1ec`. The finding that sized it: **`grep` for ledger/`change_management`/`deploy_ledger` in
`/prod-deploy/SKILL.md` → 0 hits; in `LAMBDA_DEPLOYMENT_PROTOCOL.md` → 0 hits.** The lanes were never told
the convention. Patch adds a numbered **Step 0b** (opened *before* Step 1 — an entry written at Step 8 is
a report, and a report cannot blare about a deploy that stranded mid-way).

## 5. smartx log-truthfulness + a lane boundary held twice

`20e3567f0` — the run printed `OK: Views uploaded …` immediately after **skipping every write** (COO
byte-verify of the real 11:30Z run: all three flags fired, zero new versions). Fix is **structural** — the
summary is derived from the same `_written`/`_skipped` lists the branches append to, so the contradiction
is **unrepresentable**, not merely corrected. **All three branch states exercised.** *Not deployed —
log-only; takes effect on the next ingestion-Lambda deploy, flagged so the commit does not read as live.*

**Lane boundary respected twice, at a cost to my own speed:** `docs/deployment/**` and `/prod-deploy` are
**BASE_EXEC**; the audited `--force` was available and **not used** (COO landed the EC2 doc @`3182d969d`;
CTO is taking item (b) and **declined to grant me a lane** — *"a lane boundary widened the first time it is
inconvenient is not a boundary"*). Also surfaced: `org/ref/EC2_CODE_DEPLOYMENT_STANDARD.md` is a ~5-month
stale **236-line fork of the 493-line canonical**, so landing a correct improvement **widens** the
divergence — CTO ruled: reduce to a one-line pointer, do not delete, do not merge.

## 6. Two disagreements resolved on measurement — one of them mine

- **DS axis flag** (fold not on the portal key): I re-read by a **different method** (get-object → md5 the
  bytes in hand) — fold **present**, `accounts_folded=294`, and the shared ETag was **byte-identity**, not
  mis-attribution (an ETag is a content hash; staged 20:55:35Z → served 20:57:18Z, 103s apart). DS conceded
  on their own re-measurement. I also added a sub-state neither amendment named: **3b — a well-formed fold
  block reading 442** (the 223+96+104+12+7 per-model *sum*) instead of 294 distinct, which passes every
  structural check on the wrong axis.
- **0.6.2~A "corrected" my 3.5h to 2.07h and I accepted it in one turn.** They retracted — they had
  measured **bronze**, I had measured **silver**. **Half of that is mine:** I surrendered a correct record
  to a more precise-looking number **without asking WHICH ARTIFACT**. Nothing was edited; the 3.5h stands.
  *Verification Law (6) is symmetric and I had only ever applied it outward.*

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `keys_staged`, `nna_coverage_excusals`, `DISABLE_PORTAL`, `Views uploaded`, `account_units`, `ROLL_SOURCE_UNREADABLE`, `code/gold` | PASS (7 runs) | Located the marker literal, the guard consumer, both synced smartx copies, and the 6d producer key-writers. Systems-context header flagged the `org/ref/` doc fork **while I was editing `docs/deployment/`** — the coupling a raw edit would have missed. |
| `deploy_ledger.py` | `check --all` x3, `open` x2, `close-leg` x8, `close` x2 | PASS | 2 ledgers opened at deploy-start and CLOSED in-session (2/2 and 6/6 legs). `--all` used deliberately so a census was not answered from the suppression cache. |
| `safe-commit.sh` | 6 commits, `-F` throughout, exact pathspecs | PASS (5) / **BLOCKED (1, correctly)** | owned-paths hook blocked `docs/deployment/**` (BASE_EXEC). **`--force` not used.** Also unstaged my path after the block — safe-commit stages inside its lock, so a blocked commit leaves the path in a shared index. |
| `commit-gate.sh` | 2 smartx `.py` files | PASS | py_compile + ds-precommit-check + ruff clean. |
| `comp-surface-check` | auto via safe-commit | PASS | No critical surface touched; read the output rather than treating silence as a pass. |
| risk-reflex (`comp-pulse diff`) | auto, 4 commits | PASS | Denominators printed (1/2/4 files vs 1511 danger nodes). Its HOLD on the EC2 doc is what surfaced the fork. |
| `aws iam simulate-principal-policy` | target + **separate** positive control | **FAIL — instrument lied** | **Control returned `implicitDeny` for an explicitly-granted action** (Condition block, no `--context-entries`). Rule 22a mode (2). **Discarded the tool; grounded on the policy document instead.** |
| `aws iam get-role-policy` / `list-attached-role-policies` | 2 roles | PASS | The sound substitute. Denominator stated (10 statements / 1 attached). |

**What worked:** the *separately-run positive control* on `simulate-principal-policy` — it converted a
confident false claim into a correct one before it reached CTO. Mutant-testing the acceptance script's
FRESH branch before trusting it. `comp-grep`'s systems-context surfacing a coupled doc fork.

**What failed:** `simulate-principal-policy`, twice-over silently (both target and control read
`implicitDeny`; only running them separately made the failure visible). My own first parity sweep
(basename flattening → 8 false pairings), caught by re-running path-correct.

**Gap found:** `comp-pipescript deployed` covers registered gold `.py` scripts but **not** `lib/*.json`
data assets or EC2 shell runners — both of today's committed-but-undeployed artifacts were **outside its
coverage**, which is precisely why both sat undetected. Worth a coverage extension; every raw check I ran
today carried a `# rail-checked:` marker for that reason.

---

## Blockers

**None of mine.** Gated at others (evidence-cited, not assumed):
- **[1.0.0_SA_CTO]** ListBucket truth-fix (approved in principle, sequenced behind Andrew's MDPF
  collection); deploy_ledger item (b) + the `org/ref/` doc-fork pointer (BASE_EXEC lane, he declined a
  grant deliberately).
- **[1.0.0_SA_CTO → Andrew]** 49financial Schwab RPS silver **frozen since 2026-07-15, 7 trading days** —
  escalated as material to Andrew's live MDPF backfill. **Different lane, not chasing.**
- **[clock, mine]** AC5 **leg B** — next scheduled `cron(30 13)` run.

## Current State (zero-context handoff)

- `s3://opal-data-inf/code/gold/lib/nna_coverage_excusals.json` = md5 `234d6cc4a8aeb8f30c18836e0b721cca`,
  5 accounts. INF chain **cleared 15:01:40Z**, first since 2026-07-18.
- `s3://opal-data-inf/code/bronze-runner/inf-bronze-fetch.sh` = `de2addad629952ebe44d79d0193ad803`, and the
  **on-instance** `/usr/local/bin/` copy matches. Box `i-083ad9ae297f88e9f` **stopped**.
  `ac5-probe.sh` deployed alongside for leg B / future re-exercise.
- `EC2_MANIFEST.json` `inf-bronze-runner`: parity_note re-baselined (cure + 41-day root cause + the
  first-boot-only deploy-mechanism warning); `cron_schedule` corrected to live `cron(30 13)`;
  new `cron_schedule_open_question` records the **DST intent as unresolved — the schedule was NOT changed**.
- **mdpf chain has not run since 2026-07-18**; runner `i-02448edb624a7a7cf` stopped. 6d wiring
  **never triggered**. `gold/mdpf_revamp/` newest key 2026-07-23T21:45:49Z; cottonwood
  `covered_dates` len 2; fold intact at **294** on both the revamp artifact and portal-v2.
- 2 ledgers closed today; `deploy_ledger check --all` now shows **2 BYPASS** (both DS-authored, both closed
  in fact, held as CTO's standing instances) + 3 HELD-STALE (all genuinely gate-blocked).

## Next Steps

1. **[0.7.0_AE_CloudOps]** AC5 **leg B** on the next scheduled 13:30Z run — `SHUTDOWN_ARMED` in the run's
   own log + CW metric + self-park. **Do not manufacture a run.** If A passed and B fails, **AC5 is not accepted.**
2. **[1.0.0_SA_CTO]** ListBucket truth-fix when Andrew's MDPF work clears — **acceptance is the reason
   flipping UNREADABLE→ABSENT on a live fire**, not a policy read. Then item (b) + the doc-fork pointer.
3. **[0.4.0_DS_ClientPlatform / 0.7.0_AE_CloudOps]** 6d limbs stay armed and split (DS enumerates the 11
   against the segments map; I take per-key 07-24 freshness + covered_dates + `revamp_stage` rc). Grounded:
   **all 11 ARE written** on a successful Stage 6 (6a×3, 6b×3, 6c×1, 6d pair×3 incl. `account_units` at
   `build_cottonwood_mdpf_pair.py:489`, 6d slice×1).
4. **[0.7.0_AE_CloudOps]** smartx log fix rides the next ingestion-Lambda deploy — not worth a dedicated apply.

## THE TWO SHAPES OF committed-but-undeployed (for CTO's parity-gate design)

1. **Intent recorded in a commit message, stage simply never done** (excusals — 1 day, caught).
2. **A ledger CLOSING as RECONCILED-NOT-APPLIED over its own documented OPEN legs, with no successor
   item** (AC5 — 41 days).

**Only (1) is visible to a ledger sweep.** A detector built for one shape reports the other as clean.
