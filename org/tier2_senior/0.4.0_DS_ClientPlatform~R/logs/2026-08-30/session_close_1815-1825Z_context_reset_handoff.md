# CONTEXT-RESET HANDOFF — `0.4.0_DS_ClientPlatform~R`, written for a successor who was not here

**archetype:** SCRIBE
**Seat:** `0.4.0_DS_ClientPlatform~R` · **Written:** 2026-08-30 18:25Z · **Covers:** the whole session
(2026-08-30 00:56Z onward), not just the last window.
**Written on:** Andrew-direct edict 18:2xZ, relayed by `1.0.0_SA_CTO`: *"issue an edict to all underlying
agents on the D2 D3 work to /log and prepare for closure, because I believe a clean context reset and
alignment check would be beneficial for these continued works"*.
⛔ **"CLOSURE" MEANS A CONTEXT CLOSES, NOT THE WORK.** Nothing here is cancelled, finished early, or
narrowed. **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (a standing restriction on this project).

> **Prior logs this session, all three on the record:** `session_0056-0210Z_...` , `session_0210-0820Z_...`
> `@b339d1e367` (ON ORIGIN), `session_0820-1815Z_...` `@561f850a1e` (LOCAL at writing). **This file does
> not replace them; it is the zero-context entry point.** Read this one first, then those for detail.

---

## 0. WHAT THIS SEAT IS, IN PLAIN LANGUAGE

I am a **DS (Data Science) lane seat**. My one project is **`ADVI_INSURE`** — putting 49 Financial's
**insurance** holdings onto the Opal data platform so they can be reported *beside* asset-management
figures. My task order is **`ADVI_INSURE.TO-R1-DS`** ("R1-DS" = round 1, DS lane), which covers the
**backend data planes**: raw vendor bytes (**bronze**) -> typed tables (**silver**) -> one additive
reporting table (**gold**) -> one published file (**platinum**).

**The single most important rule on this project**, from Andrew directly: **insurance value sits BESIDE
asset-management AUM (Assets Under Management) and NEVER inside it.** If any existing asset-management
figure moves by one byte, the DESIGN is wrong, not the implementation — report and stop.

**Vocabulary a successor needs:**
- **49F / 49financial** — 49 Financial, the client firm. Its data lives under the S3 key prefix
  `blackdiamond/49financial/`. **Black Diamond** is the vendor system the data is pulled from.
- **`INS-a-5`** — the scheduled job that pulls insurance bronze from the vendor each morning at 04:35Z.
  It is NOT mine; it belongs to the ETL (Extract-Transform-Load) lane.
- **`AC1`..`AC6`** — the six acceptance criteria on my task order. A criterion is a testable claim the
  work must satisfy.
- **proof-of-spec instance** — a JSON file recording, per criterion, how it was tested and what the
  result was. Mine lives at
  `org/tier2_senior/0.4.0_DS_ClientPlatform~R/deliverables/ADVI_INSURE.TO-R1-DS_PROOF_OF_SPEC.json`.
- **A "fire"** — one run of a scheduled job.

---

## 1. DONE — closed and verified, with the pin and the instrument

| what | pin | instrument that closed it |
|---|---|---|
| **Step 0: which machine actually runs my converter** | `d2201132d5` | The estate's silver converters run as **AWS Lambda functions whose Python files are copied into the deployment zip** ("vendored"), NOT downloaded from S3 at run time. Measured by reading `BUILD_MANIFEST.json` + the Terraform module. **This inverted the plan** — the earlier design assumed an S3 code prefix and would have published 3 files somewhere nothing reads. |
| **The stage entry point** (the code that receives an event and converts that day's data) | `85abccfd68` | 28 test arms, then a **mutant battery**: I deliberately broke 4 things and confirmed each broke exactly the arm that should catch it. Exercised on the real 2026-08-29 vendor bytes. |
| **The manifest backfill** — 3 old silver partitions had no `manifest.json` beside them | `77f4dbaca2` | Reconverted each in memory, compared **byte-for-byte** to the stored file, wrote the manifest ONLY where they matched. 3 of 3 matched. **Control: ETag + LastModified + VersionId on all 3 stored files captured before and re-read after — 0 of 3 moved.** Accepted by the issuer and independently graded. |
| **The mint** — the converter is deployed and wired | applied 08-30 08:1xZ | Terraform apply reported 9 added / 1 changed / 0 destroyed, then read back on the LIVE plane: 11 S3 notification rules with the pre-existing 9 unchanged. **The 49F insurance data that had been landing daily into a prefix nothing consumed now reaches a converter.** |

---

## 2. IN FLIGHT — started, not finished, and exactly where it stops

### 2a. The proof-of-spec instance is INVALID and the fix is HELD (the live item)
Four rows in my instance say `commit_or_etag: PENDING-COMMIT-THIS-SESSION` — a placeholder meaning "this
will be committed shortly". **All four artifacts were committed hours ago.** The rows are therefore false,
and the checker tool now rejects the file (`rc=1`).

**The exact fix, already measured — replace the placeholder with these commit hashes, change nothing else:**
```
  insurance_silver_rule17_census.py                        -> 07e4e488de
  data/assets/scripts/silver/bd49f_insurance_conversion.py -> 77f4dbaca2
  ADVI_INSURE_TO-R1-DS_RECEIPT_SHAPE_PROPOSAL_20260828.md  -> 07e4e488de
  ADVI_INSURE_SILVER_STAGE_DESIGN_20260828.md              -> 85abccfd68
```
⛔ **WHERE IT STOPS IF NOBODY TOUCHES IT: right here.** It is waiting on **one word from `3.0.0_SA_CVO`**
(the Chief Verification Officer seat), who certified this file on 2026-08-28 and whose certification the
edit invalidates by changing the file's hash. The issuer (`2.0.0_SA_COO`) recommends doing it NOW; the
tool's author confirmed the defect is real. **Neither of those is the certifier's permission, which is why
I did not act.** The Andrew edict explicitly confirms: *"`0.4.0_DS_ClientPlatform~R`'s HOLD stands on
`3.0.0_SA_CVO`'s word — a context reset does not lift it and does not satisfy it."*
**Do NOT widen the edit.** Do not add the optional `introduces:` field the newest checker supports — the
issuer scoped this to "the placeholder replaced by the commit hash, nothing else changed" so a certifier
can read the whole diff in a minute.

### 2b. Why the file went invalid — state this correctly or a successor will chase a ghost
The verdict did **not** change because of the tool bump announced on 2026-08-30 afternoon. Measured across
three tool versions on one unchanged file:
```
  checker @6a0e8e85de  INVALID -- 0 of these violations
  checker @3948c766a7  INVALID -- all 4   <- the version that added artifact-row checking, ~05:00Z
  checker @cec2a9b663  INVALID -- the same 4
```
So: **a tool gained a new check, and that check found a real pre-existing defect of mine.** Both halves
are true and both must be said. The placeholder token I used (`PENDING-COMMIT-THIS-SESSION`) was never
the one the schema defines (`PENDING-THIS-COMMIT`) — it was wrong the day it was written and nothing
checked it until the new rung landed.

---

## 3. OWED BY THIS SEAT — named by serial

**Nothing.** No seat is waiting on `0.4.0_DS_ClientPlatform~R` for anything. Every request made of this
seat today has been answered and acknowledged:
- `2.0.0_SA_COO` — the backfill act (closed), the S1-1 handoff inputs (accepted), the two stale-face
  questions (answered as `EMIT-2` = closed-retired, `T4A` = live with 1 of 4 families delivered).
- `0.7.0_AE_CloudOps` — the runtime profile, per-feed prefixes and family string for the deployment
  (accepted and applied).
- `1.0.0_SA_CTO` — the three LF checksums the deploy gate required (accepted; they caught a bad package).

**Waiting ON others:** `3.0.0_SA_CVO` for 2a. That is the only one.

---

## 4. CLOCK/EVENT-GATED — the fire, what it proves, what failure looks like

⛔ **MONDAY 2026-08-31, 04:35Z. This is the single event this seat exists to read next.**

**What it is:** the daily scheduled vendor pull, which now — for the first time — flows through the
converter deployed today.

**What it proves (this closes `AC2`, `AC3`, `AC4` and the deployment's own acceptance):**
1. The new Lambda function's own log shows that day's `insurance_*` files converted to silver parquet at
   the correct key grammar.
2. Row counts equal the vendor's own attested totals.
3. ⛔ **The NEGATIVE CONTROL: the `cottonwood` converter's log shows NO invocation on those keys.**
   Without this, "our converter ran" cannot be distinguished from "some converter ran".
4. That fire's **`MaxMemoryUsed`** is read against the 1024 MB configured. **I sized 1024 MB from a
   `tracemalloc` measurement of 23.5 MB, which counts only Python objects — NOT the interpreter, native
   libraries or the layer. It is a FLOOR, not a peak. The fire's own number is the real measurement.**

**What a FAILURE looks like, so it is not misread:**
- **Expect 2 of 3 feeds, not 3.** The third (`insurance_relationshipdetail`) is deliberately INERT: the
  scheduled vendor pull never requests it, and extending it would mean 77 extra vendor API calls per run —
  a widened external-data pull needing Andrew's explicit permission. **This was ruled and is designed
  behaviour, NOT a gap in my stage.** A successor who reports it as a defect is re-opening a settled call.
- A day with no vendor file is `SKIP: an absent day is ABSENT` — no carried-forward values, no zero rows.
- A short pull (fewer rows than the vendor attests) **REFUSES** rather than converting. That is correct.

⛔ **A MANUAL INVOCATION DOES NOT CLOSE THIS.** Running the converter by hand is QA evidence only. The
scheduled fire is the acceptance, and running it early spends the very discriminator the acceptance needs.

---

## 5. UNVERIFIED — read this before trusting anything above

- **1024 MB rests on one instrument** (`tracemalloc`), and that instrument structurally undercounts. See 4.
- **`T4A`'s "1 of 4 families"** is measured on ARTIFACTS (one verdict file exists in the whole repo). A
  commit message says "4 T4.A tranches" — tranches are not families, and I could not reconcile the two
  from the log. **If the issuer's record disagrees with my census, the record wins.**
- **The 3 backfilled manifests** are verified byte-identical at the moment of writing. Nothing re-checks
  them; a future writer change would not be caught by anything currently in place.
- **The `insurance_relationshipdetail` absence** was diagnosed by another seat (`0.7.0_AE_CloudOps~K`) —
  **and that seat is now DEAD at the OS process level.** Its finding was independently accepted, but no
  one can now ask it a follow-up question.
- **My own two errors this session, both corrected by other seats, both worth knowing about me:** (i) I
  prescribed an infrastructure fix that would have destroyed 8 live IAM policies — the applied-plane
  listing showing all 8 still under their original names is the proof it was avoided; (ii) I counted 2
  affected code locations when there were 4, and my own search output had shown the extra ones. **I state
  numbers confidently and have twice let evidence in hand not reach the conclusion.** A successor should
  re-derive my counts rather than inherit them.

---

## 6. PUSH STATE — measured, not defaulted

```
  origin/CLOUD = 89edf8efc1                      (git ls-remote read 2026-08-30T18:2xZ)
  d2201132d5  step-0 record          ON ORIGIN
  85abccfd68  stage entry            ON ORIGIN
  77f4dbaca2  backfill gate          ON ORIGIN
  629948a4a3 / b339d1e367  logs      ON ORIGIN
  561f850a1e  the 0820-1815Z log     LOCAL  <- rides the next integration window
  THIS FILE                          LOCAL at writing; committed immediately after, lands at the next window
```
No integration-window HOLD is open as this is written (the 18:14Z window closed at 18:16Z).

## 7. Compiler Tools

None run for this file — it is a handoff document, no code or infrastructure changed. The session's tool
record is in the three prior logs; the load-bearing rows were `git ls-files --eol` (found a CRLF defect a
byte-comparison could not), `git show <pin>:<path> | sha256sum` (the reference that caught a bad
deployment package), and `proof-of-spec-check.py` run across three versions (the discrimination in 2b).
