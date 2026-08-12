# FANOUT 05 — OPAL_KIMIPIPELINE ground truth (verbatim agent report, received 2026-08-12 ~20:50Z)

**Agent scope:** what the pipeline is and does today — code, schedule (verified at the live layer),
inputs/outputs, semantic-vertical meaning in implementation, user-input entry, estate-report
relationship, friction/state kinds, vendor egress. **Evidence class: agent-derived; schedule and
code-currency claims arrived verified at three layers (TF / live scheduler / today's exercised run)
with the method stated inline.**

---

## 0. Headline

The pipeline is **real, deployed, and fired this morning**. But three things in the framing do not
survive measurement:
1. **It does not produce a "semantic layer over the estate" today.** It proposes **prose-field
   edits** (4 permitted fields) on named resources. C3.ii vertical anchoring is **DESIGNED, not
   built** — and Andrew **stood C3.ii down** on 2026-08-06.
2. **The friction+state call kinds granted standing egress on 08-12 are NOT in the deployed runner.**
   Zero occurrences. They run by hand from CRO scripts.
3. **"The 9am estate report" and "the Kimi pipeline" are the same object**, not two things with a
   relationship.

## 1. Registry + PRD (both STALE)

`org\projects\OPAL_KIMIPIPELINE.json:1-19` — status `active`, owner `1.0.0_SA_CTO~B`, registered
2026-08-04, macro `OPAL`; :17 phase text describes 2026-08-04 state only.
`docs\architecture\OPAL_KIMIPIPELINE_PRD.md` (82 lines, 2026-08-04). **Both predate every
architectural change since.** PRD :26 names EC2 `i-04981b6aec3bed86b`; `aws ec2 describe-instances`
on that ID returns `[]` — **that instance no longer exists**. Live is `i-0512bd3cbaf602b7f`. The PRD
also describes the monolithic single-Kimi-call design, **removed** 2026-08-11 (`959236f60d`).

## 2. All code, and where it runs

| Component | Path | Lines | State |
|---|---|---|---|
| EC2 runner (the whole pipeline) | `infra\aws\ec2\estate-report-runner\estate_report_runner.py` | 2,253 | **DEPLOYED** |
| Orchestrator Lambda | `infra\aws\lambda\estate-report-orchestrator\lambda_function.py` | 80 | **DEPLOYED** |
| Terraform | `infra\aws\terraform\estate-report\{main,instance,orchestrator,iam,secrets}.tf` | 1,017 | **APPLIED** |
| Device-side capture | `.tools\estate-capture.py` + `.tools\estate-capture-schedule.ps1` | — | **DEPLOYED (local Windows task)** |
| friction/state calls | `org\tier1_exec\4.0.0_SA_CRO\scripts\kimi_call{1_friction,2_state}{,_v2}.py` | — | **BUILT, NOT DEPLOYED** |

**Chain:** EventBridge Scheduler → Lambda `estate-report-orchestrator` (60s, fire-and-forget,
StartInstances then returns) → EC2 `i-0512bd3cbaf602b7f` t3.medium, **TRANSIENT/self-stopping** →
systemd oneshot on boot → 90-min dead-man `shutdown -h`.

**Code currency — VERIFIED at the bytes layer (Rule 22a CODE):**
```
s3://opal-estate-report/code/estate_report_runner.py
  ETag 223b3103204100c17063fe48f2f90af1  size 120,980  mod 2026-08-11T00:08:06Z
local repo file md5 223b3103204100c17063fe48f2f90af1  size 120,980   -> MATCH
```
`instance.tf:215` `ExecStartPre` pulls that object **on every boot** — staged == executing here (NOT
the first-boot-only EC2 hazard).

## 3. Schedule — verified at the LIVE layer

- **DESIRED (TF):** `orchestrator.tf:53-76` — `state = "ENABLED"`, `cron(0 9 * * ? *)`, tz
  `America/New_York`, flex window OFF.
- **APPLIED (live `aws scheduler get-schedule`):** State ENABLED, same cron/tz/window, target =
  orchestrator Lambda ARN, input `{"mode":"daily-run"}`, LastModification 2026-08-04T18:48:19Z.
- **EXERCISED:** live instance LaunchTime 2026-08-12T13:00:45Z = 09:00:45 EDT today; manifest
  started_at 13:02:10Z, completed_at 13:30:41Z.
- `comp-trigger estate-report` corroborates ENABLED, denominator **139 event rules + 16 schedules**.

## 4. Inputs and outputs

**INPUTS (4):** (1) blobless shallow clone of ajb_workspace CLOUD via `estate-report/github-token`;
commit window resolved from the *scheduled* 09:00 ET marks, never now() (:209). (2) Corpus census —
exactly 3 hardcoded files in a **static dated mirror** (:481-486):
`AWS_ESTATE_CENSUS_20260730/{RULINGS_LEDGER.jsonl, SEMANTIC_NOTES_s3_buckets.md,
SEMANTIC_NOTES_ddb_tables.md}`. (3) Prior day's report for the set-delta (:1024-1032). (4) Kimi API
key from Secrets Manager `astn/kimi/api-key`.

**OUTPUTS — `s3://opal-estate-report/`, 7 prefixes:**

| Prefix | Writer | Live count | Shape |
|---|---|---|---|
| `daily/YYYY/MM/DD/` | runner | 20 (10 days × .md/.json) | the report |
| `manifest/YYYY-MM-DD.json` | runner | 10 | RUNNING → PENDING/FAILED |
| `adjudicated/YYYY/MM/DD/` | **CVO only** (IAM-denied to runner) | 4 | signed record |
| `config/_EPOCH.json` | CVO once | 1 | absence anchor, first_expected 2026-08-04 |
| `code/` | deploy | 1 | the runner |
| `logs/` | systemd ExecStopPost | 17 | journalctl dumps |
| `text-input/YYYY-MM-DD/{device}.json` | **device-side capture** | 6 | Andrew's typed words |

Layout still **v2 (year/month/day)** — the PRD's v4 day-first migration (:56) never happened.

**Adjudication ladder, denominator 10 days:** 3 closed (07-30 NO-SEMANTIC-CHANGES, 08-04 ADJUDICATED,
08-05 NO-SEMANTIC-CHANGES), **7 PENDING (08-06..08-12)**. Zero MISSING vs _EPOCH. 08-06 is
**half-landed**: adjudicated md exists (22,326 B) but its manifest never flipped — fail-pending, as
the skill's Step 4.3 designs for.

## 5. What "semantic vertical" means in the IMPLEMENTATION

**It does not emit C3.ii verticals. It does not propose them either.** The deployed runner proposes
**prose-field edits on individual named entities**, allowlist-constrained:
- `:179` `PROSE_FIELDS = {description, enrichment, classification, classification_reason}` — the
  ONLY proposable fields
- `:183-185` `DETERMINISTIC_FIELDS` (producers, served_artifacts, family, current_coverage,
  frontend_resolution, thread_id) — compiled, never proposed
- candidates rejected runner-side against a canon entity set (386 entities today)

"Semantic Vertical" is (a) Andrew's naming token for the system (project JSON :5) and (b) the
**DESIGNED v3 output contract** at `docs\architecture\OPAL_KIMIPIPELINE_STATE_FRICTION_DESIGN.md`
§3-4 (:97-190), which would anchor output to C3.ii verticals — **not built**.

C3.ii is ratified canon but **stood down**: `OPAL_KIMIPIPELINE_STATE_FRICTION_DESIGN.md:611`, Andrew
verbatim *"Our whole focus here is C2 and C3.i. Do not worry about C3.ii just yet."*

**The four DETECT groups are what actually runs** (:1148-1153): D naming, B relationships (14d), C
lifecycle (90d), A propagation. **Group A can never fire** — INSTRUMENT_UNAVAILABLE by construction
on a blobless clone (:1397-1412) — so max 3 detect calls/day, not 4.

## 6. Where user input enters — and the gap

**The mechanism exists and is live, but it is not wired into the pipeline.**
- Source: local Claude Code transcripts (`.tools\estate-capture.py:369-370`). Device-side is forced:
  the EC2 runner clones the repo and structurally cannot see them (:8-16).
- Upload: `:345` → `text-input/{YYYY-MM-DD}/{device}.json`; scheduled daily 06:30 local
  (`OpalEstateCaptureDaily`).
- **LIVE: 6 objects**, 08-04..08-11, 92-250KB each.
- **THE GAP:** `grep -c 'text-input' estate_report_runner.py` = **0**. The runner reads the frozen
  2026-07-30 mirror. Its docstring :424-425 says the corpus is frozen *"because the capture UPLOADER
  was never built"* — **stale**; the uploader landed 2026-08-11 (@8a789694dd). The consumer half
  (B6-3) is declared OUT_OF_SCOPE.

**Lifecycle_Value** — SYSTEM_DEFINITIONS `:365-385`, `contested_unresolved`; borrows
lifecycle_class's 7 values (RULE_BANK:401). Ratified per-vertical: **17 of 28**. At resource grain:
**zero populated**, gated by Andrew verbatim (`WS-C1_LIFECYCLE_VALUE_GATE_BOUNDARY_20260731.md:9-13`):
*"It is impossible to know the Lifecycle Value of the resource without the user input pipeline you
are building."*

## 7. Relationship to the estate report

**They are the same system.** `s3://opal-estate-report/` is the pipeline's own bucket; the "9am
Eastern Kimi/K3 estate report" is its `daily/` output. Consumer loop = `/estate-pull` (CVO-only):
enumerate PENDING → pull → adjudicate with Andrew → land to `org/estate-reports/` + `adjudicated/` +
flip manifest. `manifest/{YYYY-MM-DD}.json` confirmed as the correct oracle path (day-root form reads
false ABSENTs). **Open:** `org/estate-reports/` does not exist in the repo; day records sit in the
CVO interim home (`org\tier1_exec\3.0.0_SA_CVO\deliverables\estate-reports\`, 3 files + 1
day-record) — PRD open item 6.

## 8. The friction + state call kinds

**Ruling:** `ANDREW_DIRECT_20260812_OPEN_CALLS_THREE_RULINGS_CROB.md` @`432b2d6871`, ~1325Z.
**The Andrew verbatim is four words: "recs approved go ahead"** (:5-6). "Kimi friction+state kinds
STANDING daily production egress" is CRO~B's restatement of the approved rec — the record flags that
itself at :15-16.

**Scope** (:17-25): the two kinds may fire on the existing daily schedule to the already-in-use
endpoint. **Payload bound: estate-structural content only — instrument figures, vertical/structure
names, document PATHS + BM25 scores. NEVER document bodies, client data, PII.** Any other kind or
widened payload is a new call at Andrew.

**What they produce (BUILT, hand-fired only):**
- `friction` — F1-F4 instrument battery for one vertical → `{friction_character ∈ 6-enum, direction ∈
  4-enum, summary, cites[], blind_spots[], confidence}`. **F3 (operator signal) is UNMEASURED** — the
  axis the text-input gap starves.
- `state` — takes friction output + current ratified lifecycle_value → `{current, proposed, shift ∈
  NONE|IN-PROGRESS|PROPOSED, …}`. Proposes only; Andrew asserts.

**FOLD-IN NOT DONE.** `grep -ci friction` over the 2,253-line runner = **0**. Newest runner commit
`959236f60d` (08-10); the ruling is 08-12; deployed object == that file (ETag-verified) — the
deployed runner definitively has no friction/state kind. No open deploy ledger for it.

Governance note: this standing vendor-egress authorization has **no LD number and no
rcg/rulings/RULINGS.jsonl entry** — one CRO deliverable + four inbox broadcasts.

## 9. External vendor egress

**Yes — Moonshot AI, daily, unattended.** `https://api.moonshot.ai/v1/chat/completions`, model
**kimi-k3** (`instance.tf:134-135`), Bearer from `astn/kimi/api-key`. EC2 in a public subnet,
egress-all SG (`instance.tf:39-44`). **Measured on today's run:** 18 calls (1 narrate + 2 detect + 15
author), 1,645s wall, **49,911 prompt + 54,486 completion tokens on the wire**. Deployed kinds:
exactly 3 (`KIMI_BUDGETS` :166 — a 4th kind would KeyError).

## 10. Drift found (measured, not recommended)

1. **`infra\aws\ec2\EC2_MANIFEST.json` stale on two fields** — `instance_id: i-04981b6aec3bed86b`
   (does not exist) and `deployed_commit: ce5f0c7e45` (2026-07-30; actual `959236f60d`, 2026-08-11).
   Deployment Rule 8 names this file the source of truth.
2. **`estate-capture-writer` IAM grant matches zero live objects.** Grant:
   `opal-estate-report/????-??-??/text-input/*` (day-first). Tool writes
   `text-input/{date}/{device}.json` (text-input-first). Uploads succeed only because
   `estate-capture.py:303` uses ambient admin credentials and never assumes the role — the exact
   failure `iam.tf:466` warns about verbatim.
3. **Applied-but-unread env var.** `ESTATE_GRAPH_KEY=kuzu_nessie_db` live in user_data, `kuzu` pip-
   installed on the box; the deployed runner references it **0 times** (13 os.environ reads, none is
   GRAPH). Rule 22a's own signature: applied truth true, code path absent.
4. **Corpus frozen at 2026-07-30.** 153 nuggets, identical day over day by construction, while 6 days
   of real captured input sit unread in `text-input/`.

**INFERRED, labeled:** friction/state fold-in proven absent from the deployed runner, not from every
conceivable deployable. Defect 2's cause is grounded; whether noticed elsewhere not established.
