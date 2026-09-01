# 0.4.0_DS_ClientPlatform~V — 2026-09-01 08:55–10:35Z — two grain mismatches in the completeness marker, and three corrections of my own work

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE

## Window

08:55Z (close of the previous log) to 10:35Z. Continuous; no gap.

## Current State

**Seat.** `0.4.0_DS_ClientPlatform~V`, OPAL_ADVIPOINTERS only (Rule 27). Monitor `bt7c8rpkr` live all
window; every inbound message ACKed by id. No open act at close.

**The window's subject.** A completeness marker,
`s3://opal-data-assets/schwab/08335338/meta/complete/date=2026-08-31.json`, fired for the first time
ever at 09:46Z today and did so **ten times in 35 seconds**. I hold the producer lane (Rule 13) and
the M-2 face. Two independent structural defects found, both at the DEPLOYED bytes:

**GRAIN MISMATCH 1 (msg 91268).** The KEY is DATE-grained — `complete_marker_key` at
`conversion_manifest.py:162-163`, docstring *"One object per (master, date)"*. The PAYLOAD and the
GATE are INVOCATION x LANE-grained — `build_complete_markers` builds `by_date` from `r.silver_keys`
(`:225-235`, this invocation's own writes) and the gate at `schwab_runtime.py:92` tests
`lane_results`. The converter is S3-event-driven, so N bronze arrivals produce N invocations:
**11 distinct START lines measured 09:45-09:50Z**, ten marker writes to one key. **The defect sits in
`build_complete_markers` + the key function — the code BOTH call sites share**, so a fix at either
call site leaves the other. The `:92` gate is correct as written (per-lane deliberately, so one
master's failure cannot suppress another's) and must not be touched; what it is being asked to
AUTHORISE is the bug.

**GRAIN MISMATCH 2 (msg 91359), independent of the first.** `declared_tables()` renders every
`(feed, section)` in `SPECS` with **no reference to which master is being built**, while the claim is
per-(master, date). Measured across a denominator of 2 masters:

| feed | 08335338 (ADVI) | 08242234 (MDPF) |
|---|---|---|
| fam | 526 | 0 |
| slm | 537 | 0 |
| rlw | **0** | **46** |
| acc (control) | 541 | 660 |

**The declaration is a UNION over masters used as a PER-MASTER denominator.** So `fact_rlw` can never
appear in an ADVI marker — not because RLW is broken, but because RLW does not deliver here. This
also explained the anomaly nobody could account for: a 75-column pin on a feed with no data. **The pin
is real because the feed is real; it just lands under the other master.**

**The denominator therefore carries THREE confounds and only one is a defect:** master scoping
(permanent, correct), cadence (periodic, healthy), genuine outage (`fam` only — and already owned by
this seat's R-WATCH face). An exclusion list built on any single axis is wrong three ways.

**Other measurements delivered.** The union of ALL TEN marker versions reaches 15 tables of which 11
are declared, against a declared set of 17 — so no selection, aggregation or union over those objects
recovers completeness (this refuted `3.0.0_SA_CVO`'s stated recovery heuristic, which that seat then
retracted). And the 08-30/08-31 silence was explained at the code path: `partitions=[]`, `per_type={}`
in the run's own manifest -> `by_date` empty -> `markers == []` -> no marker, no failure, no log line,
gate OPEN. Nothing to attest.

## What I got wrong, three times, and how each was caught

1. **P2F-4 (withdrawn, msg 91186).** I spent a full read — deployed-bytes hash bind, SSM document,
   served entrypoint, S3 version history — re-deriving a criterion `2.0.0_SA_COO` had itself
   discharged on 2026-08-29 at line 87 of the face. I acted on a quoted `<status>` block and never
   opened the file. **Fifty minutes after diagnosing that exact failure in another seat's document.**
   What survived: a deploy-plane confirmation of a commit-plane finding, which on this project is
   worth one sentence and not a seat-hour.
2. **"My record is stale" (retracted, msg 91275).** I matched a census string inside a long
   `status_reason`, printed the field, and read its LEDE. The correction sat three lines below in the
   same field. **A grep tells you where a claim STARTS and never where it is OVERTURNED, and the
   correction always sits past the point where the search succeeds.** I then had to return a credit
   the issuer gave me for the non-finding (91281) — a false attribution of a GOOD act is the
   least-audited claim in the fabric, and it would have inflated a tally being used to argue a remedy.
3. **"Six dead feeds" (corrected, msg 91337) — the costly one.** I reported six declared tables as
   fed by feeds "dead 32-88 days" and four seats acted on it. **Four of the six were healthy.**
   Measured from each feed's own partition series: rly/rty are MONTHLY (median gap 31.0, p90 33) at
   32 days; rlu/rtu are QUARTERLY (median 91.0, p90 126) at 88 days; control `acc` daily at 1 day.
   Only `fam` is genuinely late. **I applied a daily expectation to non-daily feeds, and the partition
   counts (12, 37, 526) were in my own output when I wrote "dead".** This is NEVER#1 one level up —
   and I had applied it CORRECTLY at 08:18Z the same morning on the sibling feeds. **Having just
   applied a rule is the condition under which you stop checking whether it applies.**
   The correction made the conclusion STRONGER: M-2a is unsatisfiable by CONSTRUCTION (mixed cadence,
   false ~30 days in 31 with every feed healthy) rather than by outage — which is not repairable
   upstream and changes the remedy. It reached three seats before any acted: `2.0.0_SA_COO` withdrew
   a request to open an ingestion workstream against four healthy feeds, and `3.0.0_SA_CVO` retracted
   its own exclusion clause.

**And a fourth, in my reporting rather than my measurement:** I twice told Andrew "four commits" when
this seat made **three**. Corrected at close.

## Findings raised (all as measurements, no remedy proposed)

- Two independent grain mismatches, both in shared code (above). I declined to propose the mechanism
  in 91268 and declined again in 91359 — *"proposing it inside a finding is how a remedy gets adopted
  without being chosen."* `1.0.0_SA_CTO` holds the completeness-contract call; this seat builds what
  is ruled.
- The union measurement refuting the only surviving recovery heuristic.
- An alarm I refuted before sending: the chain's `NEVER_EMPTY_DIMS` 0-row guard sits on an arm that
  fails daily, which reads as a live safety gap. Opening the BUILDER instead of the DISPATCHER found
  `convert_orion_api_to_silver.py:1119-1124` (ADHC_BUGB) — an orchestrator-level 0-row refusal
  covering EVERY dim, broader than the chain's. **The live writer is guarded. No safety gap.**

## Blockers

**None.** `OW-4/5/6` on INF-ONEWRITER remain unstarted for authority reasons stated on that instance;
the M-2 contract is `1.0.0_SA_CTO`'s live call and no producer act is authorised before it. Both are
conditions, not stalls.

## Deploys

**None.** No producer edit, no deploy, no vendor call, no ad-hoc run, no monitor/alarm/debounce. Every
act this window was a read or a message. The GO authorises SEATING and READING and nothing here
exceeded it.

**PUSH STATE, MEASURED AT CLOSE and re-measured because it is perishable:** an integrator ran during
the window. `origin/CLOUD` moved `a29c2591ae -> 7f406f6e3f`. All THREE of this seat's commits —
`61aabf2ee1`, `9f134aaf3d`, `45c559bc7e` — read **ON ORIGIN** by `merge-base --is-ancestor` after an
explicit `git fetch`, with a positive control confirming the predicate fires. My earlier "LOCAL ONLY"
report was true when made at 08:52Z and is now superseded by the integrator's run, not by an error.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-read` | INF-ONEWRITER face; `inf-silver-chain/lambda_function.py`; `convert_orion_api_to_silver.py`; `proof-of-spec-check.py` | PASS | Refuted my own accounts_v2 alarm before it left the seat. |
| `comp-find` | `'*advi-49f-gold-dispatch*'`; `'build_complete_markers\|write_complete_marker_verified' --all`; `'*P2-FLOOR*' --all` | PASS | The `--all` call-site census (47 hits / 141,247 files, bands printed) located both call sites AND the shared core. One name-search returned a MEASURED zero -- the object was an AWS resource, not a repo file. |
| `aws s3api` / `logs` / `lambda` | version listings, ten VersionId downloads, package downloads bound by computed `base64(sha256(zip)) == CodeSha256`, CloudWatch windows | PASS | Every package read was BOUND to the live config hash rather than trusted by filename. |
| `python` (ad hoc) | per-feed cadence from partition series; union of ten marker payloads; `SPECS` + `sr._fact_table` resolved by running the DEPLOYED code | PASS | The cadence run is what refuted my own six-dead-feeds claim. |
| `safe-commit.sh` | (none this window) | N/A | Nothing committed 08:55-10:35Z until this log; the window's output was measurement and correction. |
| `comp-blast` / `comp-pipescript` / `comp-estate` | not run | N/A | Named rather than omitted: no code, infra or pipeline changed this window. Rule 20 does not bind a read. |

**What worked.** Running the DEPLOYED code's own resolver (`SPECS` + `sr._fact_table`) turned a
naming-convention INFERENCE into a MEASUREMENT — six of six table->feed mappings resolved. And the
per-feed cadence computation is the instrument that caught my own worst error of the session.

**What failed.** Three of my own tool calls: an unquoted heredoc let backticks command-substitute and
mangled two lines of a memory file (repaired); a `jq` expression split on `=` against prefixes that
contain none, yielding full paths where I expected dates (caught by a downstream parse returning zero
rows, then fixed); and `send_message` refused three times because I omitted a parameter namespace
prefix and misread the refusal as a content problem twice before reading my own call shape.

**Gap found.** `list-objects-v2` on a VERSIONED bucket returns only `IsLatest` — it reported ONE
object on a prefix holding TEN versions, a 90% blind read that looks clean. It is sound for the
EXISTENCE question and blind to the HISTORY question, **and nothing in its output says which one you
asked.** Three seats used it on this prefix tonight.

## MCP traffic

~30 messages handled; all ACKed by id. OUT from this seat: 91186 (P2F-4 withdrawal), 91268 (grain
mismatch 1), 91275 + 91281 (two self-corrections), 91306-91309 (the STOP on M-2a), 91337-91340
(the cadence correction), 91359-91362 (grain mismatch 2). IN: issuer amendments and rulings from
`2.0.0_SA_COO`, blast-radius and digest-refutation reads from `0.7.0_AE_CloudOps~M`, adjudications
from `3.0.0_SA_CVO`, and one instrument ruling from `1.0.0_SA_CTO`.

## Next Steps

1. **[`1.0.0_SA_CTO`]** The completeness contract — what "complete for a DATE" means over a declared
   set that is master-agnostic AND mixed-cadence. Both grain measurements are inputs; neither is an
   answer. The emit mechanism follows from it rather than beside it.
2. **[`2.0.0_SA_COO`]** M-2e's disposition of the already-written false markers, which is not
   self-healing and which the issuer has correctly refused to close on "nothing reads it".
3. **[whoever holds the word]** INF-ONEWRITER OW-4, the consumer leg. The 08-12 served defect —
   `fee_earning_aua` reading zero beside a live basis-point figure — is STILL LIVE.
4. **[`0.4.0_DS_ClientPlatform~V`]** R-WATCH A1 tomorrow, or same-turn if R fires. `fam` is the
   R-trigger feed AND `fact_fam`'s source, so R firing is also a completeness-contract event —
   `2.0.0_SA_COO` is carrying that linkage onto both faces.
