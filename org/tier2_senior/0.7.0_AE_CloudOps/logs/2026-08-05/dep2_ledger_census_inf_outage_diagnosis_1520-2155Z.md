# DEP2 deploy, ledger census inverted, and a 5-day INF outage found by retracting my own claim (1520-2155Z)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, VALIDATE

**Serial:** 0.7.0_AE_CloudOps (base) · **Window:** 2026-08-05 1520Z -> 2155Z
**Prior log:** `base_dep1_estate_runner_corpus_vintage_deploy_1410-1520Z.md`
**Commits (mine, this window):** `1f17b81e30`, `108d9dc1d`, `de64e50bc5`
*(`git log --author="0.7.0_AE_CloudOps"` is a SUBSTRING match and also returns `~A` lane commits
`8e69ae4cb0`/`93c898445e`/`2c08087905` — those are the LANE's, not mine. Noted because it would
otherwise read as my work; see "The `~A` convergence" below.)*

---

## What happened

Three threads, and the third was found by retracting a claim I had already made twice.

### 1. DEP2 — corpus DELIVERY fix deployed (OPAL_KIMIPIPELINE.DEP2)

Second deploy of the day to the same key. **HELD at COO's own tip-control** when `git diff` against
the GO's pin came back 3,150 bytes non-empty — the THIRD pin-staleness event on this file in seven hours.

Settled it by comparing **parsed ASTs** rather than the diff (Python discards comments):
```
f023857ab3  AST-sha256 6a70e3679fcc65a3a1c9288abf8b1019   68,857 B
9a1856bc03  AST-sha256 6a70e3679fcc65a3a1c9288abf8b1019   70,281 B   IDENTICAL
31 changed lines, ZERO non-comment non-blank.
```
Same program; nothing behavioural to re-adjudicate. That let COO authorise a vintage CVO had not named
without assuming an acceptance extends — the difference was MEASURABLE. COO ran the **negative control I
did not** (mutating `CORPUS_PROMPT_BUDGET` 25000->20000 CHANGED the hash), proving the instrument
discriminates. **Banked: an instrument that returns IDENTICAL is worthless until shown able to return
DIFFERENT.**

Earlier in the window I also **refused a proposed retune** on grounding: CTO~B offered
`CORPUS_PROMPT_BUDGET` 25000->20000 over "61,378 chars is 2% over the only prompt size ever exercised —
the exact dimension KIMI_EMPTY sat on." Two DIFFERENT budgets — input prompt chars vs output
`max_tokens` (`95e1f0283f` is literally `-max_tokens 4000 / +32000`; `OPAL_KIMIPIPELINE_PRD.md:38` says
starvation occurred *on* the ~60KB prompt, so that input size was already fine). And **60,000 was never
a tested boundary** — a hand-picked `[:60000]` slice at `a254104b34:826`. CTO~B verified at source,
withdrew the retune, and landed the correction **in the source comments**. CVO concurred off an
independent derivation.

### 2. Ledger census — INVERTED, and two tool defects found

MSTR flagged 7 past-window deploy ledgers. **ZERO are overrunning deploys.** Grounding it produced two
defects in `.tools/deploy_ledger.py` (CTO's tool):

- **`close` CRASHES** — `KeyError: 'log'` at `cmd_close:318`, while `_read_sentinel` does **not** require
  `log`. The two paths disagree on the schema, so `cmd_check` ACCEPTS these entries, reports
  `OPEN [PAST-WINDOW]` and fires RED, while `cmd_close` refuses the same file. **Four ledgers can alert
  forever and are structurally unclosable.**
- **The prescribed remedy is DESTRUCTIVE** — `_write_entry:177-179` is a full `write_text()` overwrite of
  the hand-authored markdown. Running the sanctioned fix would have erased ETag `e0ef77832f`, delta
  `0.0100`, commit `16ed33b6c6`, run id `mdpf_daily_20260728_225137`, cycle-complete first emit
  `22:55:12Z` — none reconstructible from the sentinel. **Stopped before executing it.**

Per MSTR ruling LD-0090: archived all 5 hand-authored markdowns byte-exact (md5 src==dst verified),
committed FIRST @`1f17b81e30`. MSTR then VOIDED the close half once the crash surfaced and ranks it the
primary fix.

**I reported a confident WRONG MECHANISM TWICE before grounding it, and COO propagated the first
upward:** (1) "closed in prose, never in the field" — the field said CLOSED; (2) "the checker is
defective" — it is not, `close` UNLINKS the sentinel so existence means open and `cmd_check` never reads
`status` **by design**. Both retracted with the source-confirmed version.

### 3. A 5-day INF outage — found by retracting my own claim

I twice reported `inf-nna-excusals` L2's evidence condition SATISFIED. **It was not.** The leg reads:
*"pipeline-complete.json advances off its 2026-07-18T14:59:10Z freeze, VS PIPELINE-FAILED.JSON ADVANCING
INSTEAD."* I checked `complete.json` (07-31 > 07-18, true) and **skipped `failed.json` — the
discriminator the leg explicitly names.** I read the limb that let me close and skipped the limb that
would stop me.

Going back for it: `pipeline-failed.json` `{"run_date":"2026-08-05","exit_code":1}`, advanced 08-01
through 08-05. **The INF gold chain had not completed since 2026-07-31.**

> **`inf-nna-excusals` sat 274h "past window" DOING EXACTLY ITS JOB** — refusing to close because the
> exercised verification never happened. The instrument the fabric spent the afternoon calling noise was
> carrying a true signal. **A gate that looks broken because it will not go green may be the only thing
> in the room that is working.** (COO is landing this as doctrine.)

Diagnosed read-only under COO GO. **Two blockers:**
- **#1 `INF_C_01`** — `nna_coverage_guard.py:320` correctly refusing to drop **$514,487.47 of SERVED NNA
  across 5 accounts**. Not a broken pipeline; a guard doing its job. Guard's own words: *"sum(advisors)
  == firm_total would STILL TIE, because the money leaves both sides at the same instant. That is why
  nothing else catches this."*
- **#2 `INF_D_00`** — unfixed `int(hh_id)` at `:328`, guarded only by `pd.isna()`. Chain aborts ten
  scripts earlier (`:253` vs `:263`), so it has not executed since 08-01 — **masked, not cleared.**
  `account_team.parquet` carries **5 rows `household_id='unknown'` and ZERO nulls** -> fires
  deterministically once #1 clears. **The excusal decision alone would not have restored the chain.**

### The `~A` convergence — resolved at root, by the lane, not by me

While I diagnosed from the marker/log surface, **`0.7.0_AE_CloudOps~A` independently root-caused and
resolved it**: `8e69ae4cb0` (INF gold chain frozen 5d by a **stale hand-drawn rep allowlist**; custodian
predicate REFUTED, rep-code predicate exact), then **ANDREW-DIRECT 1958Z** `93c898445e` — *Orion rep 10
(Noel Soderblom) IS in Inflection scope, **no excusal***, then `2c08087905` (rep-10 add across the
**Lambda** copies — the `accounts_v2` PRODUCER was still filtering Soderblom out, so DS's `data/` fix
alone would have re-run and changed nothing).

**This vindicates the guard completely.** The 5 accounts were legitimately Inflection's, being dropped
because a rep was wrongly absent from a hand-drawn allowlist. The remedy was NOT an excusal — Andrew
ruled explicitly against one. My framing ("a guard doing its job; this needs a DECISION, not a fix") held,
and the decision went the opposite way from the excusal path the TO anticipated.
**My blocker #2 (`INF_D_00`) is untouched by this and remains live** — `~A`'s commits address the rep
allowlist, not the `int('unknown')` cast.

### W0 (MDPF row 17) — a NO-OP, and what grounding it found

Row 17 = "`mdpf-freshness-checker`'s IAM role LIVE with a scoped policy for a Lambda that DOES NOT EXIST."
**Both are already gone:** Lambda -> `ResourceNotFoundException`; role -> `NoSuchEntity`; full enumeration
**208 roles, `IsTruncated=None`, ZERO `freshness` matches** ("mdpf" matches 8, so the zero is real).
CVO's census read it from the **graph**, not live IAM (DESIRED vs APPLIED). Nothing to delete.

But `mdpf-daily-trigger/lambda_function.py` asserts in **four places** (`:22`, `:99`, `:406`, `:778`) that
"the existing `mdpf-freshness-checker` alarm catches an unresolved defer," with a docstring at `:408`
stating the intent *"so a permanent silent DEFER can never masquerade as a legitimate fail-safe."*
**That checker does not exist — a live false premise inside production decision logic.**

I hypothesised MDPF was silently deferring. **It is not** — the floor path dispatches by design
(`:776` is `... and NOT is_floor`), and I dropped the hypothesis rather than send it. What IS true, from
its own logs on every run: `"inflection": {"fresh": false, "as_of": "2026-07-31"}`, `"spine_fresh": false`,
`"dispatched": true`. **MDPF computed off a known-stale INF spine for five days, measured it correctly
every time, and nothing carried it to a human.** Same shape as `inf-pipeline/alarms.tf:95`, which defines
an alarm for exactly "pipeline-complete.json not written." **Two independent detectors saw this outage;
neither reached anyone. It surfaced because I mis-read a ledger leg.**

---

## Deployment Sequence + Verification (AE)

**DEP2 — `s3://opal-estate-report/code/estate_report_runner.py`, vintage `9a1856bc03`**

| step | run | observed |
|---|---|---|
| pre-check | `git log -3 -- <runner>` | `9a1856bc03` is tip |
| pre-check | `git diff 9a1856bc03 -- <runner>` | **0 bytes** |
| Phase 1 | `aws s3api head-object` | ETag `"a110981492b461e19fb9be7848b9ad09"`, 62,875 B, 14:56:59Z — **= my DEP1 artifact; COO discriminator #1 PASS** |
| Phase 2 | `md5sum <runner>` | `5ff45f5e968d4a43422c973b5e8f0657` — **DIFFERS from DEP1; discriminator #2 PASS** |
| deploy | `aws s3api put-object` | rc=0 **recorded, not relied on** |
| Phase 3 | `aws s3api head-object` | ETag `"5ff45f5e968d4a43422c973b5e8f0657"`, 70,281 B, 16:45:22Z, VersionId `08mkactqbO4tmNg.DdLZgMqZBileQwav` |

Actual Phase-3 output:
```
"LastModified": "Wed, 05 Aug 2026 16:45:22 GMT",
"ContentLength": 70281,
"ETag": "\"5ff45f5e968d4a43422c973b5e8f0657\"",
"VersionId": "08mkactqbO4tmNg.DdLZgMqZBileQwav",
"ServerSideEncryption": "AES256"
```
**MANDATED READ-BACK** (the control I added on DEP1, now doctrine): `get-object` -> served md5
`5ff45f5e968d4a43422c973b5e8f0657`, `cmp` **byte-for-byte identical**, `py_compile` PASS,
**non-ASCII on served bytes = 0**. Corpus markers live: `CORPUS_PROMPT_BUDGET` 2 · `_bounded_json` 2 ·
`corpus_coverage` 11 · `KIMI_LENGTH_STARVED` 3.
**ETag == md5, no `-N` suffix -> plain md5, comparison VALID.** Prior versions retained; rollback is one
`copy-object`. RAVC-4 closed by `1.0.0_SA_CTO~B` on **independent re-derivation**; `3.0.0_SA_CVO`
verified the served layer byte-exact.

---

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-grep` | PASS | Located the artifact's sole code-reader (`instance.tf:192`), the marker writer (`orion-gold-dispatch.sh:1909`), and the T5A census. Denominator printed every run (e.g. 11 matches / 6 files, 22,294 of 24,226 in scope). |
| `comp-estate estate-report` | **FAIL — UNRUNNABLE** | *"not a known C3.ii vertical"*; no estate-report vertical among the 29. The DEP1 TO's Phase-1 step 3 cannot execute as written. CTO~B took the ontology gap onto the v3 critical path. |
| `comp-to` | PASS | Set TO context for DEP2 (race-free per-session file). |
| `deploy_ledger.py check` / `check --red` | **PARTIAL + defect found** | Surfaced the census; `--red` **DELIVERS** rather than reports (3 alerts into COO's inbox — disclosed and owned; plain `check` from here). `close` crashes: see Gap. |
| `safe-commit.sh` | PASS | 3 commits; surface-check OK, risk-reflex CLEAN against 1,659 danger nodes each time. `-F` used for every message (F-010). |
| `aws` primitives | PASS w/ 2 instrument failures | head-object / get-object / list-object-versions / iam / lambda / logs. See Gap. |

**What worked:** AST comparison as a deploy-decision instrument — it converted a 3,150-byte diff that
would have forced a full re-adjudication under deadline into a ten-second call. Positive controls caught
two lying instruments before either reached a report.

**What failed:**
- `aws iam list-roles --no-paginate` returned **ONE PAGE** (100 roles, `IsTruncated=True`). I nearly read
  "0 freshness roles" off it. **Caught by the positive control** — "mdpf" also matched 0, which cannot be
  true. Re-ran with auto-pagination: 208, `IsTruncated=None`. *A count you did not paginate is a page
  size wearing a total's clothing.*
- `aws` cannot write a `/cygdrive/...` or MSYS `/tmp/...` output path (native Windows binary). The
  round-trip `get-object` silently wrote nowhere twice, and downstream `md5sum`/`cmp` then reported the
  **absence** as `BYTE MISMATCH: FAIL` — **a retrieval failure rendered as a content verdict.** An
  `ls -l` presence check discriminated it; Windows-form absolute paths work.
- Native Python `subprocess` could not spawn `aws` (`WinError 2`) — the MSYS 5-member class;
  `.tools/msys_argv_guard.py` exists for exactly this.

**Gap found:** `.tools/deploy_ledger.py` — `cmd_close:318` dereferences `state["log"]` while
`_read_sentinel` does not require it. **A gate that can SEE an entry, alert on it indefinitely, and
structurally CANNOT close it.** Plus `_write_entry` overwriting hand-authored evidence as the *prescribed*
remedy. Both routed to `1.0.0_SA_CTO` as tool owner; MSTR ranks the crash primary.

---

## Blockers

**None blocking me.** Two items held at others, both with named owners and evidence:
- Four ledger closes: **VOID** pending CTO's tool fix (evidence: `KeyError: 'log'` traceback; archives
  intact @`1f17b81e30`; no mutation occurred — the crash precedes `_write_entry`/`_save`/`unlink`).
- `emitter-wo4c-cadence-acceptance`: `HELD-CTO-DEPLOY-FREEZE`, 3 unproven legs. **Does the freeze still
  bind?** — routed to `1.0.0_SA_CTO`, not mine to disposition.

CTO is holding all four of my asks on **Andrew's explicit word** (*"just read through them when you get
them and ill advise further"*) — a legitimate hold, not a blocker; nothing of mine waits on it.

---

## Current State

*(for a reader with zero prior context)*

- **Both P1 deploys are LIVE and verified.** `s3://opal-estate-report/code/estate_report_runner.py` =
  vintage `9a1856bc03`, md5/ETag `5ff45f5e968d4a43422c973b5e8f0657`, 70,281 B, uploaded
  2026-08-05T16:45:22Z. **DEPLOYED != EXERCISED** — the box is transient and stopped; **nothing has RUN
  either change.** First execution is the **2026-08-06 13:00Z boot**; `3.0.0_SA_CVO` owns that verdict
  and will check the emitted report carries the corpus block and coverage line.
- **Scope honesty, unchanged:** this makes a frozen corpus VISIBLE and DELIVERS 153 nuggets we already
  hold; it does **not** make them current. The corpus is still the static `AWS_ESTATE_CENSUS_20260730`
  mirror; the **B6 capture uploader** is the substrate fix and is on MSTR's board.
- **OPEN RESIDUAL, not cleared:** kimi-k3's context window is **not pinned in-repo** (`KIMI_MODEL` from
  env via `var.kimi_model`, `instance.tf:120`). "61,378 chars is comfortable" is an **ESTIMATE**.
  Settling it needs vendor egress + Andrew's per-use word — **not called.**
- **INF:** root cause resolved by `~A` + Andrew-direct 1958Z (rep 10 in scope, no excusal). **`INF_D_00`
  remains an unfixed live defect** — `int(hh_id)` at `:328`, 5 `'unknown'` rows present, DS lane under
  Rule 13. Whether the chain now runs green end-to-end is **unverified**; the 08-06 ~13:47Z run is the
  first test of both `~A`'s fix and this residual.
- **Ledger sentinels:** 4 unclosable pending CTO; archives at
  `org/critical_paths/change_management/<slug>.hand-authored-20260805.md`.
- **W0 row 17:** no-op, needs a **status correction** in
  `org/tier2_senior/0.7.0_AE_CloudOps~F/deliverables/MDPF_GLOBAL_T5A/{KILL_LIST_CENSUS.md,kill-list.yaml}`,
  not an execution. Half B (shadow S3Key declarations) **not yet grounded**.
- **Brief to CTO base** committed @`de64e50bc5` at
  `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/BRIEF_TO_CTO_20260805_session.md`; ACKed, four asks held.
- **Nothing built:** no alert, alarm, SNS topic, SES send, freshness checker or monitor (standing
  moratorium). Every finding landed as a blocking item.

---

## Next Steps

1. **[1.0.0_SA_CTO]** Four asks held pending Andrew: `deploy_ledger` 1a-then-1b; does the `emitter-wo4c`
   freeze still bind; route `INF_D_00` to DS; atomic-mv hook scope + timing.
2. **[0.7.0_AE_CloudOps]** Atomic-mv hook implementation (accepted as mine; awaiting scope).
3. **[0.7.0_AE_CloudOps]** W0 row-17 status correction + ground half B; delete the false
   `mdpf-freshness-checker` safety-net claims from `mdpf-daily-trigger` (both pending `2.0.0_SA_COO`).
4. **[2.0.0_SA_COO]** Decide whether five days of MDPF output derived from a known-stale INF spine needs
   saying to anyone — a DATA question I did not ask and is not mine.
5. **[0.7.0_AE_CloudOps]** Tomorrow ~13:47Z: verify the INF chain end-to-end. **Tripwire given to CTO —
   if the guard's 5-account set GROWS rather than staying stable, escalate STRAIGHT to Andrew**, since a
   bounded one-time call and an ongoing bleed are different decisions. Do not conflate an INF_C_01
   re-failure with the estate-runner deploys — different pipeline, different box.
6. **[0.7.0_AE_CloudOps]** Queued: audit-invoker (CRO corrected the framing — `NFRA_AUDITDEV_PRD
   @e05fad4f3` + staged `rv0057-f001` already exist; root cause is device-keying; two
   `SNAPSHOT-FAILURE COMMIT-FAILED` entries newly surfaced and unscoped), CRO's RCG cohort-A + 70-file
   bundle, `~E`'s AAS-ERR handoff.

---

## The lesson I am carrying

The wrong mechanisms got out because **I sent each one UP before grounding it**, on a day I was writing
up other people's instances of the same class. **The retraction is not the discipline — not sending it
in the first place is.** Applied to W0: nothing left my seat until it was source-grounded, and the one
hypothesis that failed there (MDPF silently deferring) died at my desk instead of in COO's inbox.
