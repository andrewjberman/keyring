# MDPF consolidation — H10 external/manual-reader BOUNDED NEGATIVE

**Seat:** `3.0.0_SA_CVO~Z` (verification; not an approval step)
**TO:** `MDPF_CANRTE.P0-6` @f50291f06 · issued by `2.0.0_SA_COO~Z`
**Measured:** 2026-08-06, live plane, AWS `313476888478`, `us-east-1`. Read-only throughout.
**Class:** ABSENCE. This document is the SINGLE declaration site for the external/manual-reader
question across every deletion candidate in this consolidation.

---

## 0. The verdict, in one sentence

**NO READER IS VISIBLE TO THESE NAMED INSTRUMENTS — CloudTrail S3 object-level data events (window
2026-05-11 → 2026-08-06), S3 server access logging, and a repo-documentation search (denominator
printed per query) — AND FOR EVERY MDPF DELETION CANDIDATE THE CORRECT ROW IS `NOT-OBSERVABLE`,
NOT `ZERO`.**

Read-reader telemetry **was never enabled** on any bucket holding an MDPF deletion candidate. An
observation that was never possible is not a zero, and it cannot be created retroactively.

**SCOPE, POST-AMENDMENT:** DS~Z's census (@645a8759e) removed rows 6, 7 and 8 from the deletion set
entirely — all three have source-visible readers, and row 6 is required to calculate a PORT row.
**This declaration therefore carries real weight on ROWS 1–5 only.** On rows 6–8 it is moot in the
useful direction: nothing is being deleted, so unobservability cannot cause a wrong deletion. The rows
are retained rather than struck, because a candidate that was evaluated and cleared is evidence, and
a row deleted after it came back clean is indistinguishable from one never examined.

---

## 1. Criterion 1 — the telemetry question, answered as a measurement

Not assumed, not skipped to the caveat. The API calls and their outputs:

### 1.1 `aws cloudtrail describe-trails`

| Trail | Multi-region | Log bucket |
|---|---|---|
| `opal-organization-trail` | true | `opal-cloudtrail-logs-313476888478` |
| `opal-served-key-write-trail` | false | `opal-served-key-write-trail-logs` |

Two trails exist in the account. Both were read.

### 1.2 `aws cloudtrail get-event-selectors --trail-name opal-organization-trail`

```
Selector 1: ReadWriteType=All, IncludeManagementEvents=true, DataResources=[]
Selector 2: ReadWriteType=ReadOnly, IncludeManagementEvents=false
            DataResources: AWS::S3::Object = [ arn:aws:s3:::opal-data-bd/
                                               arn:aws:s3:::opal-data-inf/ ]
```

**S3 object-level READ data events are captured for exactly two buckets: `opal-data-bd` and
`opal-data-inf`.** Neither holds an MDPF deletion candidate.

### 1.3 `aws cloudtrail get-event-selectors --trail-name opal-served-key-write-trail`

```
AdvancedEventSelectors: name "served-firm-header-writes-only"
  eventCategory   = Data
  resources.type  = AWS::S3::Object
  resources.ARN StartsWith [ arn:aws:s3:::opal-data-inf/platinum/firm/
                             arn:aws:s3:::opal-data-bd/platinum/firm/
                             arn:aws:s3:::opal-data-cot/platinum/firm/ ]
  readOnly        = false          <-- WRITES ONLY
```

> ### ⚠ A TRAP THAT IS WORTH MORE THAN THE RESULT
>
> This trail names `platinum/` prefixes in a **data-event** selector. An agent checking "is platinum
> covered by CloudTrail data events?" will find `platinum/firm/` in a live selector and answer **YES**
> — and be exactly wrong for a reader question. **`readOnly = false` makes this trail structurally
> incapable of recording a read.** It is a write-integrity instrument wearing the costume of a reader
> instrument. It also covers `opal-data-cot`, a third firm's bucket, which makes the coverage list look
> broader than the reader-relevant coverage actually is.
>
> **Correct reading: this trail contributes NOTHING to the H10 question. Zero.**

### 1.4 `comp-whoread` — the who-DID-read instrument, exercised

`comp-which "how do I find out who reads an S3 prefix that our source code does not reference"`
routed to **`comp-whoread`** (CTO GO 20260709T210020Z). **There is no comp-tool coverage gap for this
question** — no gap report is owed to COO~Z on this TO's `if_mismatch` clause.

*Routing note, not a defect:* the router scored `comp-whoread` **third (0.55)**, behind a 1.50 tie of
`comp-estate --resource` and `comp-pipescript io` — both **source/graph** instruments, i.e. DS~Z's half,
which this TO forbids me to duplicate. The tool prints "score is overlap, NOT a confidence" and flags
the tie explicitly, so the router behaved correctly and the descriptions discriminate. Recording it
because taking the top-ranked hit here would have silently produced the MECE break CTO~Z's
classification removed.

```
$ comp-whoread opal-data-mdpf/mdpf/feeds/
CANNOT ANSWER for opal-data-mdpf/mdpf/feeds/: ZERO S3 object-level data events in range
  (since 2026-05-11). This bucket is NOT covered by an object-level data-event selector in
  that window... An empty who-read here means 'NEVER CAPTURED', not 'never read'.
  Failing closed (rc=1) rather than reporting a false clean.
  (management-level events seen: 0; object-level: 0)
```

**rc=1, FAIL CLOSED.** The tool refused to answer rather than return a clean-looking empty. Its
behaviour independently confirms the selector configuration read at 1.2/1.3.

### 1.5 A load-bearing entailment — why prefix uncertainty does not weaken the verdict

Data-event selection is configured at **bucket-ARN granularity**. If a bucket has **no** object-level
read selector, then **no prefix inside it** has one either. I did not fully resolve the exact S3
prefixes for the OWNTS outputs or the `wsb`/`wsd` outputs — **and that gap cannot change any row
below**, because every candidate's bucket is uncovered at the bucket level. The verdict is robust to
the prefix ambiguity; it is not resting on it.

---

## 2. Criterion 3 — S3 server access logging, checked SEPARATELY

A different instrument with different coverage. "No CloudTrail data events" does not mean "no access
telemetry", so this was measured independently rather than inferred.

```
$ aws s3api get-bucket-logging --bucket <B> --query 'LoggingEnabled.TargetBucket'
opal-data-mdpf         None
opal-data-portal-v2    None
opal-data-assets       None
opal-data-bd           None
opal-data-inf          None
```

**Server access logging is NOT ENABLED on any of the five buckets — including `opal-data-bd` and
`opal-data-inf`, the two that DO have CloudTrail read coverage.** So the two instruments do not
compensate for each other anywhere in this estate: where CloudTrail is blind, nothing else is looking.

---

## 3. Criteria 2, 5, 6 — one row per candidate, own instruments, own window

> ### AMENDMENT 2026-08-06 — DS~Z prefix resolution @645a8759e
>
> DS~Z resolved the prefixes I had left unresolved and **the NOT-OBSERVABLE verdict HOLDS on every
> row — no row required re-measurement.** The re-open condition I registered (rows 6/7 living in
> `opal-data-bd`/`opal-data-inf`, the only two buckets with read coverage) **did NOT fire**: every
> candidate resolves to `opal-data-mdpf` or `opal-data-assets`. Recorded as a measured negative
> result, which is what I asked them for.
>
> **Two changes that DO matter:**
>
> **(a) ROWS 6, 7, 8 ARE NO LONGER DELETION CANDIDATES.** DS~Z found source-visible readers for all
> three. Row 6 (`wsb`) is read by `mdpf_aggregate_aua.py:239-268` and is REQUIRED to calculate a PORT
> row. Row 7 (`wsd`) is **fail-green**: retiring it does not error — it silently reverts `identity_2`
> from a MEASUREMENT to an ESTIMATE the code's own docstring records as running ~1–3% high
> (`build_etf_decomposition:420-427`, enabled by `_empty_feeder():217` returning a correctly-columned
> empty frame "so every downstream op is total" — **absence is silent BY DESIGN**). Row 8: 5 of 5
> feeder artifacts resolve to a reader and a writer, 0 unresolved.
> **Consequence for this document: the external question on rows 6–8 is moot in the useful direction
> — they are not being deleted, so unobservability of external readers cannot cause a wrong deletion.
> ROWS 1–5 ARE WHERE THIS DECLARATION STILL CARRIES WEIGHT.**
>
> **(b) A BUCKET DISCREPANCY THAT LANDS ON MY OWN ROW 5.** DS~Z found
> `build_mdpf_etf_ownership_timeseries.py` contradicting itself: `:21` docstring says
> `s3://opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/{ticker}.json`, `:75` constant says
> `PLATINUM_BUCKET = "opal-data-assets"`. **The constant executes** — corroborated live by the Aug-6
> hard-stop writing `s3://opal-data-assets/platinum/mdpf/etf_ownership_timeseries/DIVZ.json` (01 s.5).
> **I must apply that to myself:** I attributed row 5 to `opal-data-portal-v2` by INFERENCE from
> CLAUDE.md Rule 17b (platinum serves from `opal-data-portal-v2/platinum/`), not from a measured
> constant. Given `platinum/mdpf/` paths in this estate demonstrably resolve to `opal-data-assets`,
> **row 5's bucket attribution is UNVERIFIED and may be wrong.**
> **The verdict is unaffected — I measured BOTH buckets** (`opal-data-portal-v2` and
> `opal-data-assets`) in §1.2 and §2, and neither has read coverage. **But I got the right answer off
> a premise I had not measured, and that is worth saying out loud rather than letting the correct
> conclusion launder the unverified input.** DS~Z's framing is exact: *here we got lucky; the next row
> may not.*

> ### AMENDMENT (c) 2026-08-06 — ROWS 1–4 BUCKET CORRECTED, AND THE THREE-RECORD DISAGREEMENT RECONCILED
>
> MSTR~Z caught rows 1–4 attributed to the wrong bucket while pulling these names for Andrew's H13
> answer. **Confirmed independently at my seat** (s3api, UTC — never `s3 ls`):
>
> ```
> opal-data-portal-v2/platinum/mdpf/etf_ownership_timeseries/
>   DIVZ.json 51098 · IDVZ.json 51080 · PFDE.json 38347 · PFOE.json 38231
>   all LastModified 2026-08-05T13:34:59+00:00
> opal-data-assets/platinum/mdpf/etf_ownership_timeseries/  -> EMPTY
> opal-data-mdpf/platinum/mdpf/etf_ownership_timeseries/    -> EMPTY
> ```
>
> **Action 2 discharged — coverage MEASURED on the corrected bucket, not inherited from row 5:**
> `comp-whoread opal-data-portal-v2 --prefix platinum/mdpf/etf_ownership_timeseries/` → **rc=1 FAIL
> CLOSED, 0 object-level data events since 2026-05-11.** Verdict holds, and it now rests on a
> measurement of the right bucket rather than on §1.5 reasoning applied to the wrong one.
>
> #### The three records are not three errors — they answer DIFFERENT QUESTIONS IN DIFFERENT TENSES
>
> | Record | Says | What it actually answers |
> |---|---|---|
> | `:21` docstring | `opal-data-portal-v2` | **Where the objects ARE.** Called "stale" — it is the only record matching the live plane. |
> | `:75` constant `PLATINUM_BUCKET` | `opal-data-assets` | Where the code **currently TRIES** to write. That prefix is EMPTY. |
> | `01` s.5 | Aug-6 hard stop = failed write to `opal-data-assets/…/DIVZ.json` | **Why it is empty.** The constant's writes have been FAILING. |
>
> **Reconciliation: the objects at `opal-data-portal-v2` dated 2026-08-05 are the LAST SUCCESSFUL
> write. The constant was repointed to `opal-data-assets`, where every write since has failed.**
>
> **⚠ THE LESSON, AND IT INVERTS THE RULE DS~Z AND I BOTH APPLIED.** "The constant executes, the
> docstring is stale" is a correct general rule and it produced the WRONG BUCKET here — because it
> silently assumes the write **SUCCEEDED**. *Execution is not success.* For a **deletion** question
> "where does the code write" is the wrong question entirely; the only instrument that answers "what
> would I be deleting" is a **live listing**. Neither of us ran one until MSTR~Z did.
>
> **A consequence beyond the bucket name:** OWNTS objects are dated **2026-08-05** and the Aug-6 write
> failed — so OWNTS has been **writing nowhere since the constant was repointed**. That corroborates
> `02`'s disposition (*Stage 5 OWNTS | RETIRE | … it was the exact August 6 blocker*) from the object
> side rather than the source side.
>
> **AND THE PART ANDREW NEEDS FOR H13:** with rows 1–4 corrected, **5 of the 8 candidates (the four
> OWNTS objects + row 5's bare aggregate) sit in `opal-data-portal-v2` — the LIVE SERVED BUCKET that
> CloudFront reads.** Under my original table they read as sitting in an internal pipeline bucket.
> The specific objects are not the served MDPF artifact family, but **five of eight proposed deletions
> are inside the serving surface**, and that is a materially different question from the one my table
> posed. It is his to answer with the true shape.

> ### ⚠ AMENDMENT (d) 2026-08-06 ~21:42Z — ROWS 1–5 MOVED MID-SESSION. THE ROW PATHS ABOVE NOW 404.
>
> **The paths in rows 1–5 no longer resolve.** Surfaced by AE~Z, **verified independently at my seat
> with a positive control** (not accepted on report):
>
> ```
> head-object platinum/mdpf/aggregate_aua_timeseries.json          -> 404 Not Found
> head-object platinum/mdpf/archive/aggregate_aua_timeseries.json  -> 2026-08-06T21:41:59Z, 451518 B
> POSITIVE CONTROL platinum/mdpf/global/aum-metrics.json           -> 200, 13:50:50Z, 5894 B
> list-object-versions platinum/mdpf/etf_ownership_timeseries/DIVZ.json
>                                                                  -> Versions=19, DeleteMarkers=1
> ```
>
> The positive control returning 200 establishes the 404 is a **real absence**, not a broken call.
> 19 versions + 1 delete marker = **copy-then-delete-marker MOVE, fully reversible** — not a deletion.
> New home: `platinum/mdpf/archive/…`. Byte sizes unchanged, so these are the objects I measured.
>
> #### ⛔ A WRONG INFERENCE OF MINE, CORRECTED — I ISSUED IT TO TWO SEATS
>
> On measuring no depth-1 `platinum/mdpf/aggregate_aua_timeseries.json`, I wrote that this was
> *"consistent with 02's 'Retired Stage 4 bare aggregate rollup | KEEP RETIRED' — the row-5 deletion
> target may already be gone."* **That is wrong. The object existed until 21:41:59Z today.** I listed
> at ~22:07Z and attributed a **27-minute-old move** to a **months-old retirement decision**.
>
> **This is the session's own dominant class, landing on me: I observed an absence and reached for the
> explanation the documents made available instead of establishing the mechanism.** The documents
> supplied a ready-made story that fit the observation perfectly and was not its cause. Rule 22 — a
> causal claim is a hypothesis until source-confirmed — and I offered mine as the likely reading.
>
> **What saved it was the bound, not the reasoning.** I wrote: *"one bucket, one prefix, no global
> absence claim — whoever owns the deletion should confirm the target EXISTS before scheduling
> removal."* That bound is the reason this is a correction and not a bad deletion plan.
>
> #### A NEW MEMBER OF THE CLEAN-ZERO CLASS (AE~Z's observation, adopted)
>
> The four OWNTS objects are now findable **only** at the new prefix. **Any future census run against
> this document's original paths returns a clean, confident zero — for objects that exist.** Same
> shape as the mangled-pattern and truncated-list zeros catalogued in §6, arriving by a third door: a
> **correct query against a stale path**. The retrieval works perfectly. **This is the strongest
> argument in this document for H7's re-pin obligation being a standing constraint rather than a
> checklist item** — AE~Z's P0-1 baseline froze these keys at 21:01Z and they moved at 21:42Z.
> **Forty-one minutes.** H7 demonstrating itself inside one session.
>
> #### WHAT THE MOVE DOES AND DOES NOT DO TO MY VERDICTS
>
> - **Does NOT resolve any NOT-OBSERVABLE row.** An archive move is not a reader census. Nothing about
>   it says anyone did or did not read those objects. **The composition rule (§6a) is untouched** — a
>   move upgrades no bounded negative. If anything it is the *correct* action under that rule:
>   relocating with versioning intact is what you do when you cannot establish that nobody reads
>   something.
> - **Does change the H13 posture for rows 1–5.** They are out of the live served prefix with every
>   version preserved — strictly more reversible than either deleting them or leaving them served.
>   A later real deletion is still H13 and still Andrew's.
>
> #### DISPOSITION RECORD — these were already ruled, and I re-derived it independently
>
> CTO~Z reports Andrew ruled ~2137Z (recorded by COO~Z @1893e4f58): **"3 scoped underscore twins
> TRASH"**, and the root bare object **"TRASH with checker-first-then-object ordering."** I measured
> the twins at ~22:07Z without knowledge of that ruling; the independent re-derivation carries byte
> sizes and the 3-of-4 asymmetry the ruling does not.
> **My count corrects CTO-base's F7** (08-06 1256Z trace), which recorded **four** twins awaiting
> deletion. I measure **three** per-scope twins plus a root bare object that has now moved. A deletion
> plan written against four targets would hunt a fourth that does not exist.
> **Not a live client-facing defect:** the portal read-path is confirmed scoped-**hyphen** on all four
> scopes, so the stale underscore twins are residue, not a served bug. Stated plainly so nobody
> escalates it as an incident on top of a ruling that already exists.

Every candidate gets its own row. No group verdict.

| # | Deletion candidate | Bucket | CT read data events | CT write trail | S3 access log | **Row verdict** | Window |
|---|---|---|---|---|---|---|---|
| 1–4 | OWNTS — `platinum/mdpf/etf_ownership_timeseries/{DIVZ,IDVZ,PFDE,PFOE}.json` | **`opal-data-portal-v2`** — MEASURED, 4 objects @ `2026-08-05T13:34:59+00:00` (s3api UTC). `opal-data-assets` and `opal-data-mdpf` are EMPTY at this prefix. See Amendment (c) | **not selected — measured EXPLICITLY on this bucket+prefix: `comp-whoread` rc=1, 0 object-level events** | n/a (writes-only; bucket not listed) | not enabled | **NOT-OBSERVABLE** | 2026-05-11→08-06 |
| 5 | `platinum/mdpf/aggregate_aua_timeseries.json` (bare product-level object) | **UNVERIFIED** — attributed `opal-data-portal-v2` by inference from Rule 17b; may be `opal-data-assets`. **Both measured, neither covered** | not selected | **selector names `platinum/firm/` but `readOnly=false` and neither candidate bucket is listed — contributes nothing** | not enabled | **NOT-OBSERVABLE** | 2026-05-11→08-06 |
| 6 | `wsb-49f-model-aua-daily` → `mdpf/feeds/model_aua_positions/49financial/{date}.parquet` (writer `wsb_49f_smartx_model_aua.py:247`) | `opal-data-mdpf` | not selected | n/a | not enabled | **NOT-OBSERVABLE** — but **NO LONGER A DELETION CANDIDATE** (source-visible reader `mdpf_aggregate_aua.py:239-268`; required to calculate a PORT row) | 2026-05-11→08-06 |
| 7 | `wsd-49f-partner-held-etf-daily` → `mdpf/feeds/partner_held_etf/49financial/{date}.parquet` (writer `wsd_partner_held_etf.py:42`, put `:194`) | `opal-data-mdpf` | not selected | n/a | not enabled | **NOT-OBSERVABLE** — but **NO LONGER A DELETION CANDIDATE**; retirement is **FAIL-GREEN** (silently downgrades `identity_2` measurement→estimate, ~1–3% high) | 2026-05-11→08-06 |
| 8 | `s3://opal-data-mdpf/mdpf/feeds/*` | `opal-data-mdpf` | **exercised: `comp-whoread` rc=1, 0 object-level events** | n/a | not enabled | **NOT-OBSERVABLE** — but **NO LONGER A DELETION CANDIDATE** (5 of 5 feeder artifacts resolve to reader + writer, 0 unresolved) | 2026-05-11→08-06 |

**Row 8 differs from its neighbours** and the difference is shown: it is the only candidate where the
who-DID-read instrument was actually *run* against the prefix and returned a fail-closed refusal,
rather than being resolved from selector configuration alone. Rows 1–7 rest on 1.2/1.3 + §1.5.

**RE-OPEN CONDITION — REGISTERED, THEN RESOLVED, AND IT DID NOT FIRE.** I originally left rows 1–4,
6, 7 with unresolved prefixes and registered an explicit re-open: *if those outputs live in
`opal-data-bd` or `opal-data-inf`, those rows MUST be re-measured*, because those two buckets DO have
read coverage and a genuine `comp-whoread` answer would then exist. DS~Z resolved every prefix
@645a8759e: **all resolve to `opal-data-mdpf` or `opal-data-assets`; none to `opal-data-bd` or
`opal-data-inf`.** The condition did not fire and no row required re-measurement.

**This is recorded as a discharged condition rather than deleted.** A re-open that was registered,
tested, and cleared is evidence; a re-open silently removed once it came back clean is
indistinguishable from one that was never written.

---

## 4. Criterion 4 — operational runbooks and human-facing surfaces

A manual consumer lives in a runbook, not in code. Searched via `comp-grep` (on-rails, denominator
printed). Surface searched: **`docs/`**.

| Query | Matches | Files | **Denominator** |
|---|---|---|---|
| `OWNTS` | 29 | 3 | scanned **1031 of 1034** files in scope |
| `wsb-49f-model-aua-daily` | 3 | 2 | scanned **1031 of 1034** |
| `wsd-49f-partner-held-etf-daily` | 3 | 2 | scanned **1031 of 1034** |
| `aggregate_aua_timeseries` | 108 | 33 | scanned **1031 of 1034** |
| `mdpf/feeds` | 11 | 8 | scanned **1031 of 1034** |

**The 3 unscanned files of 1034 are an unclosed bound and are stated rather than rounded away.**
`comp-grep` prints scanned-vs-in-scope precisely so this is visible; a bare `grep` has no denominator
at all, which is why it was not used (see §6, instrument 5).

**Surfaces NOT searched, and therefore NOT covered by this row:** `org/` records, Slack/Teams history,
email, Confluence-or-equivalent, any human's local notes, and any runbook that exists only in a
person's head. **A documentation search is bounded by what was written down and committed.**

---

## 5. Criterion 8 — FINAL-FORM LIMITATION TEXT

Written now, cold, before Phase 6. Drafted in advance precisely because an honesty caveat improvised
under deploy pressure is where silent upgrade happens. **Paste verbatim; do not paraphrase, and do not
soften it at the moment of use — the moment of use is the moment it is least trustworthy to edit.**

> ### For the deploy ledger and the closure statement
>
> **EXTERNAL/MANUAL READER STATUS: BOUNDED NEGATIVE — NOT-OBSERVABLE.**
>
> No reader of any MDPF deletion candidate was visible to the instruments named below. This is a
> statement about the instruments, not about the world.
>
> **Instruments checked, with windows:**
> 1. CloudTrail S3 object-level data events, window 2026-05-11 → 2026-08-06. Read coverage exists for
>    `opal-data-bd` and `opal-data-inf` ONLY (`opal-organization-trail`, ReadOnly selector). **No
>    bucket holding an MDPF deletion candidate is covered.**
> 2. `opal-served-key-write-trail` — data events on `platinum/firm/` prefixes of `opal-data-inf`,
>    `opal-data-bd`, `opal-data-cot`, with `readOnly=false`. **Writes only; contributes nothing to a
>    reader question.**
> 3. `comp-whoread` (who-DID-read, CloudTrail/Athena) — exercised on
>    `opal-data-mdpf/mdpf/feeds/`; returned rc=1 FAIL CLOSED, zero object-level data events in range.
> 4. S3 server access logging — **not enabled on any bucket examined**, including the two with
>    CloudTrail read coverage.
> 5. Repository documentation search of `docs/` via `comp-grep`, denominator 1031 of 1034 files.
>
> **THE FINDING IS THAT THE TELEMETRY DOES NOT EXIST, NOT THAT THE READERS DO NOT EXIST.**
> Read-reader telemetry was never enabled on these buckets. An observation that was never possible is
> not a zero and cannot be created retroactively. No statement in this record asserts that no external
> or manual reader exists; no such statement is available at any price from the evidence that exists
> today.
>
> **This census is a FLOOR.** Combined with DS~Z's source-visible census — which asserts only "no
> SOURCE-VISIBLE reader" and does not close this item — the joint claim is: *no reader was found by a
> source census, and no reader-observation instrument was ever pointed at these objects.*

**Reserved-word self-check.** The words *proof, provably, definitively, root cause, source-confirmed,
proved no external reader, mathematically certain* appear nowhere in the verdict (§0), the rows (§3),
or the limitation text (§5). Their only appearances in this document are in this sentence and in the
prohibition that governs them.

---

## 6. Criterion 10 — BLIND SPOTS OF EVERY INSTRUMENT I USED

An instrument list without a blind-spot column reads as coverage.

| # | Instrument | What it saw | **What it CANNOT see** |
|---|---|---|---|
| 1 | `cloudtrail get-event-selectors` | Which buckets have data-event selectors, and their read/write polarity | Whether a selector existed and was **removed** earlier. Config is current-state; it has no history. A bucket covered in April and uncovered in May reads identical to never-covered. |
| 2 | `opal-organization-trail` ReadOnly selector | Reads on `opal-data-bd`, `opal-data-inf` | Every other bucket in the estate. Also: coverage began when the selector was added — a window wider than coverage returns clean partitions that never held an event. |
| 3 | `opal-served-key-write-trail` | Writes to three `platinum/firm/` prefixes | **All reads, by construction (`readOnly=false`).** Structurally incapable of answering this TO's question despite naming platinum prefixes. |
| 4 | `comp-whoread` | Who DID read, from CT object data events via Athena | Anything outside the CT window; any bucket with no selector (it fails closed instead of guessing — the correct behaviour, and the reason its silence is informative rather than misleading). Per its own header: observed reads are a **FLOOR** on what a principal can reach, never a ceiling — **do not derive a grant narrowing from it.** |
| 5 | `comp-grep` over `docs/` | Committed documentation text, with a printed denominator | Uncommitted docs, `org/` records, Slack/Teams, email, wikis, personal notes, and any runbook never written down. **3 of 1034 in-scope files were not scanned.** |
| 6 | `s3api get-bucket-logging` | Whether server access logging is on **now** | Whether it was ever on before. Same current-state blindness as #1. |
| 7 | *(deliberately unused)* `comp-blast` / graph edges | — | **Excluded as evidence per TO rule.** Measured false zero at `c801ec9d5`: `comp-blast mdpf_aggregate_aua` reported "No downstream consumers found" against ledger evidence of **four** real consumers. **No conclusion in this document rests on a graph edge count.** |
| 8 | *(deliberately unused)* `comp-pipescript consumers` | — | **Excluded, and DS~Z measured WHY today.** `comp-pipescript consumers wsb_49f_smartx_model_aua --pipeline mdpf` → *"no downstream pipeline consumers (terminal or portal-only)"* — **wrong**, and the mechanism is known: neither writer nor reader contains the literal composite key; both compose it by f-string (`prefix = f"{FEEDER_PREFIX}/{artifact}/"`, artifact iterating `FEEDER_COLUMNS`). Positive-controlled: literal `mdpf/feeds/model_aua_positions` in the reader = **0**; `FEEDER_PREFIX` in the same file via the same command = **3**. **The retrieval works; the edge is structurally unextractable.** Same family as CLAUDE.md 22a's `boto3.resource()` two-hop blindness. |

> **A GENERALISATION WORTH MORE THAN EITHER INSTANCE.** Rows 7 and 8 are not two flaky tools. For this
> pipeline, **a zero-consumer graph result is not weak evidence — it is the EXPECTED output for an
> entire class of real dependency** (runtime-composed keys, which have no literal for a static
> extractor to find). An agent acting on DS~Z's zero would have retired a producer feeding a PORT row.
> **Treat any graph-derived zero on this pipeline as uninformative by default, not as a weak signal to
> be weighed.**

**My own blind spot, stated plainly:** I resolved candidate coverage from *selector configuration*
plus one exercised `comp-whoread` call. I did not run `comp-whoread` against all eight rows
individually, because §1.5 makes the bucket-level result dispositive for all of them. If §1.5's
entailment is wrong — i.e. if data-event selection can be configured below bucket granularity in a way
I have not accounted for — then rows 1–7 are unmeasured rather than NOT-OBSERVABLE. **I believe the
entailment holds and I have not adversarially tested it.**

---

## 6a. ⚠ THE COMPOSITION RULE — THREE NOT-OBSERVABLE RESULTS DO NOT COMPOSE INTO AN OBSERVED ABSENCE

**This is the single most likely way this document gets misused, and it belongs at the declaration
site.** Raised by `0.7.0_AE_CloudOps~Z` (P0-5 deployed-plane half) and adopted here verbatim in
substance.

Three independent surfaces have now returned nothing on these candidates:

| Surface | Owner | Result | Its named limit |
|---|---|---|---|
| Source-visible census | DS~Z @645a8759e | no source-visible reader | blind to unregistered external/manual readers by construction |
| CloudTrail object data events | **this document** | **NOT-OBSERVABLE** — 0 events in range | telemetry was never enabled on these buckets |
| Deployed Lambda env-var config | AE~Z, denominator **196 functions, explicitly paginated** | **NOT-OBSERVABLE** — 0 functions name any candidate | sees a reader only if the prefix appears in CONFIGURATION |

**STACKING THREE BOUNDED NEGATIVES YIELDS A BOUNDED NEGATIVE WITH THREE NAMED LIMITS — NOT A ZERO.**
If anyone later cites *"three independent surfaces found nothing"* as convergent evidence of no
readers, **that is the silent upgrade this document exists to prevent, and it would then have three
sources to launder it through.** Convergence between instruments is only evidence when the
instruments' blind spots are independent AND at least one of them could have seen the thing.

**AE~Z DEMONSTRATED THEIR BLIND SPOT RATHER THAN CONCEDING IT**, and the demonstration is the reason
this rule is stated so strongly. Nine deployed functions carry `opal-data-portal-v2` as a bare bucket
env var and can construct any key inside it at runtime. To test whether that blindness was real or
theoretical they went to the sharpest case — `opal-portal-data-proxy`, documented as the `/v1/*`
portal API reading `s3://opal-data-portal-v2/*`:

```
opal-portal-data-proxy   python3.11, role opal-portal-lambda-role
ENVIRONMENT VARIABLES: []      <- EMPTY. Zero keys. Does not appear in the nine.
```

**The env-var surface cannot see the live portal API reading the exact bucket that holds all five
remaining candidates.** The blindness is measured, not asserted. The discriminating instrument for
that residual is deployed Lambda **CODE** — the packages of the nine bucket-carriers plus
`opal-portal-data-proxy` — **not their config.** That remains OPEN and is named here as the true
shape of what is unclosed.

**A pagination note that applies to my own work.** AE~Z flagged that `--no-paginate` returns only the
FIRST page (`lambda list-functions` → 50 of 196, a 74% shortfall). **I used that flag once**, on the
snapshot range underpinning F4. **Self-audited three ways — CLI default, forced `--page-size 5`
multi-page walk, and `--no-paginate` — all three returned the same count.** My denominator was not a
paging artifact. *(The count has since moved 31→32 for a real reason: see §7a.)*

## 7. Criterion 9 — H13 attaches to the delete step

**H13 is OPEN and is named here so it is not discovered AT the delete step.**

S3 object deletion sits on CLAUDE.md's standing human-confirmation list ("dropping tables / deleting
S3 objects"). **Andrew's 2026-08-06 teardown word @c801ec9d5 — *"Teardown is fine just need to make
sure any necessary code on that ec2 is properly ported to the lambda"* — is about the EC2 and its
code. It does not mention S3 objects and does not authorize their deletion.**

**This is PRE-EXISTING LAW, NOT A NEW GATE.** I am not creating an approval step, and nothing in this
document is a precondition for any agent's work proceeding.

How this deliverable composes with H13: the deletion, if it happens, would be authorized by Andrew
against a census **honestly labelled a floor** — which is precisely the information he needs in order
to give or withhold that word. **The stakes moved on 2026-08-06:** with teardown authorized, a
zero-reader claim now sits upstream of an irreversible act rather than a reversible one. A row that
reads NOT-OBSERVABLE and is *reported* as ZERO is the silent upgrade this seat exists to prevent.

---

## 7a. CAPTURE-BEFORE-TERMINATE — VERIFIED DISCHARGED, and it closes two of my own findings

My earlier F3/F5 findings (routed to MSTR~Z/COO~Z) held that the pre-teardown capture was preserved
only *incidentally*, and that the newest daily snapshot **predated today's run by 6h40m** — leaving
runtime-installed dependency state uncaptured. **AE~Z executed P0-7 and both are now closed.
Verified at my seat, because "the reaper will not delete this" is an ABSENCE claim and therefore
mine to check rather than accept:**

```
snap-0fa2186f01fbc3785   2026-08-06T20:48:38.684+00:00   State=completed
  Desc: "MDPF_CANRTE P0-7 capture-before-terminate pre-enumeration baseline ... taken BEFORE any
         enumeration because a snapshot does not enumerate and therefore cannot miss"
  Tags: Purpose=capture-before-terminate · Retention=DO-NOT-DELETE-until-P6-0-discharge
        Project=MDPF_CANRTE · TaskOrder=P0-7 · CreatedBy=0.7.0_AE_CloudOps~Z
```

**F5 CLOSED — the timing gap is gone.** Instance started `13:40:23+00:00`; this snapshot is
`20:48:38+00:00`, **7h08m AFTER the run**, with the instance stopped. It captures post-run state
including any runtime-installed packages. It supersedes the daily set as the evidence baseline.

**F3's mechanical concern CLOSED for this snapshot, and by the correct mechanism.** MSTR~Z's F4
source read established the reaper filters on `tag:Purpose = DailySnapshot` (`:562`) and keeps
anything it cannot positively date (`:571-573`). This snapshot carries **`Purpose=capture-before-terminate`**
and **no `SnapshotDate` tag** — so it is **outside the reaper's filter universe entirely**, which is
the stronger of the two available exemptions (exiting the universe rather than relying on a
keep-branch). AE~Z took the right one.

**Residual, small but real, stated rather than left implicit:**
1. `Retention=DO-NOT-DELETE-until-P6-0-discharge` is a **documentary** tag — it does nothing
   mechanically. The load-bearing protection is `Purpose != DailySnapshot`. **A later tag
   "normalization" that added `Purpose=DailySnapshot` would silently re-enter this snapshot into the
   reaper universe.**
2. The **31 pre-existing daily snapshots still carry `Purpose=DailySnapshot`** and remain on the
   measured 30-day rolling cutoff. After termination no new dailies are created and the whole set
   ages out. **That is now acceptable** — the P0-7 baseline supersedes them — but it means the daily
   set must not be cited as long-term evidence.

## 8. Seat discipline

This is a verification product. **It is not a sign-off, and no one is waiting on my blessing.**
Per the TO's own instruction I will refuse to become a gate **even by invitation**, including from
COO~Z. If any TO, agent, or ledger row makes this verification a precondition for another agent
advancing, I will refuse it and say so to COO~Z the same turn.

Adverse findings in this document are findings to act on, loudly — not holds anyone must clear.

## 9. Coordination

`0.4.0_DS_ClientPlatform~Z` owns the **source-visible** half (P0-4) and asserts only "no SOURCE-VISIBLE
reader"; they are explicitly forbidden from reporting that census as closing H10. **I own the external
declaration and have not re-run their source census.** Two halves, one list, no overlap and no gap.
Candidate-list alignment with DS~Z is required so neither of us assumes the other covered a row —
coordination artifact, not an approval step.

---

*Read-only. No repository file outside this deliverable, no AWS resource, S3 object, schedule, Lambda,
IAM policy, branch, or served artifact was changed in producing it.*
