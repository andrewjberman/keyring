# 0.7.0_AE_CloudOps -- CLOCKED ITEMS, written for a successor across a REBOOT

**Written 2026-08-12 ~1545Z** under Andrew-direct reboot-pending (MSTR 154142Z). ⛔ **A REBOOT
RE-ARMS NOTHING AND RESPAWNS NO AGENT** -- site Z lost six seats to an RMM patch reboot this
morning and nothing restarted them. Everything below is inherited by READING, not by a timer.

⛔ **NOTHING HERE IS AUTHORIZATION.** Each item names its own gate. If you are a fresh seat,
re-verify liveness and read the two 08-12 session logs in `logs/2026-08-12/` before acting.

---

## 1. THE ~13:30Z SCHEDULED-BOOT READ -- the only item with a hard clock and an external gate

**WHAT:** three READ-ONLY reads on EC2 `i-083ad9ae297f88e9f` (the `inf-bronze-runner`) via SSM,
**ON ITS NEXT SCHEDULED BOOT ONLY** (`opal-inf-bronze-runner-cron` cron(30 13) starts it ~13:30Z
daily via the `inf-bronze-trigger` Lambda; the box self-stops after its run):
  (i)   the on-instance **crontab**
  (ii)  the on-disk puller's **bronze-key line, VERBATIM** (not characterised, not summarised)
  (iii) that file's **stat / mtime**

**⛔ DO NOT MANUALLY START THE INSTANCE.** Standing CTO prohibition (142641Z): a manual start is
a state change on a production box to satisfy an investigation, and it perturbs the very thing
being measured. If you miss the window, wait for the next one.
**⛔ S3 data events remain UNAUTHORIZED** (CTO, same ruling). Do not enable them.

**WHY IT EXISTS -- the question it answers:** two SCHEDULED producers write the same bronze keys
daily in two different formats. `inf-api-assets-v2` (Lambda, cron(32 13)) writes `.parquet` --
ruled out as the jsonl.gz writer by its own log. **WRITER B, which writes
`bronze/assets|positions/{date}.jsonl.gz`, IS UNNAMED.** The EC2 above is the LEADING CANDIDATE
and UNPROVEN. CTO suspended the LEG-2 port on this: unifying the FORMAT without assigning key
OWNERSHIP would put two producers on one key in one format, last-writer-wins, converting a
visible collision into an invisible one. **The survivor cannot be ruled over a producer set that
has not been enumerated.**

**WHY (iii) MTIME IS THE DECIDER:** the runner's `user-data.sh:6/:44` makes its S3 code pull
**FIRST-BOOT-ONLY**, so the S3-staged copy may be INERT and the box may execute a BAKED copy.
A baked copy dated to the AMI / last-code-change window SUPPORTS that hypothesis; one dated to
that morning KILLS it. (CTO amended Rule 22a on this: for an EC2, **STAGED = DESIRED, EXECUTING
= APPLIED**.)

**EVIDENCE THE READ MUST PRODUCE:** the three values verbatim. Nothing inferred, nothing
characterised. **CTO's branch interpretations are PRE-REGISTERED** (their 143220Z) so the result
cannot be fitted afterwards -- report the values and let the ruling follow.

**REPORT TO:** `1.0.0_SA_CTO` (survivor + decommission ruling) and `2.0.0_SA_COO` (remedy
sequencing) **the same turn**.

**STATE OF THE EVIDENCE AS IT STANDS -- do not tidy this into a conclusion:**
- Lambda RULED OUT by its own log (parquet at 13:35:42Z; the jsonl.gz lands 13:36:51Z, 68s later).
- EC2 launched in-window today (`describe-instances` LaunchTime 2026-08-12T13:30:53Z).
- Correlation 8/8: every jsonl.gz date in 08-04..08-12 carries an EC2 start; ZERO acquitting.
- ⚠ The ONE asymmetric date is **2026-08-06** -- EC2 started, NO jsonl.gz landed -- and 08-06 is
  the exact partition whose absence fails the inflection cross-axis gate daily. **CONSISTENCY,
  NOT CAUSATION** (CTO holds me to this label): a start-without-artifact is equally consistent
  with the EC2 not being the writer and something else failing that day.
- EVIDENCE AGAINST the EC2: its orchestrator's dim list OMITS positions and marks assets
  `expected_fail=True`.
- The boot-log oracle is **NON-DISCRIMINATING** -- 6 log-dates EVER (05-01, 05-06, 05-07, 06-12,
  07-16, 07-24) against a box that launches daily. **Its silence means nothing.** Do not read
  absence of a boot log as evidence of not-running.
- INFERRED, unmeasured: the fetch script may run only on first boot after a code change (3 of 4
  staged objects carry vintages landing exactly on a boot-log date -- but the MISS is
  `assets_v2`, the file in dispute, so the pattern fails on its own case).

---

## 2. THE CENSUS BUILD -- sequenced STRICTLY AFTER item 1

Placed with me by COO 152708Z. **EXTEND** `org/tier1_exec/3.0.0_SA_CVO/deliverables/
ref_deployed_vs_repo_compare.py` @6f2bcb314a with input-resolution. ⛔ **DO NOT REBUILD the
state machine** -- its six states took three seats to settle; a second classifier whose states
drift from the first is the expensive failure.
**WHY THE ORDERING IS NOT A QUEUE ARTIFACT (COO's reason, better than my own):** item 1 IS the
input-resolution mechanism being performed for the first time. Building the rule first would
encode a procedure nobody has executed -- and the whole point of input-resolution is that the
staged copy lies. Encode `ec2-executing` from what the read actually required, including what
failed on the box.
**SPEC OF RECORD, four inputs / three seats:** (1) EC2 staged != executing -> executing-or-
UNMEASURED · (2) normalise before comparing; hold-markers are DECLARED differences · (3)
normalisation is ARTIFACT-KIND dependent -- **for `.sh`, CRLF IS the defect** (`/bin/bash^M`),
so normalising it away silences the only comparison that matters · (4) resolve through the
BUILD INPUT (source-map / package manifest), NEVER by filename.

---

## 3. OTHER CLOCKS AND THEIR TRUE STATE (several are NOT what an older note would say)

- **~09-08 (after Labor Day 09-07): the holiday-arithmetic observation.** CPR-5 leg (b)'s BYTES
  half is CLOSED (the 00:00:19Z 08-12 fire ran ETag fb5e6bad by version-immutability). The
  HOLIDAY half is **NOT discharged and could not be**: the swept window contained no market
  holiday, so holiday-aware and weekday-only arithmetic are identical over it.
  `COT_MARKET_HOLIDAYS`' effect is UNEXERCISED until a lookback window spans a holiday.
- **X-ii-a acceptance is NOT a date.** The act is STAGED-NOT-APPLIED (@2740e4de8f);
  `portal/gold/mdpf/_staging/` does not exist and the live trigger role lacks the staged
  Resource. Acceptance is the first 13:30Z fire **AFTER** the applies land, which wait on DS's
  producer constant + gold-lambda repackage. ⚠ Reading a normal fire as an acceptance would
  report a FAILURE where the truth is the act never ran.
- **SEP-1 14:00Z ETFS month-end email** (recipients: ANDREW ONLY). Carry #1 LIVE: derive the CSV
  count from the PARTNER ROSTER, never the literal 3; `{"mode":"email_qa"}` is the ONLY oracle
  that returns the attach SET (a PDF in S3 does not evidence the CSVs). Carry #2 is
  **CLOSED-NOT-A-GAP** -- do not re-chase it.
- **P5 / T5.B `opal-data-mdpf` kill:** gated on the portal-verified taking-AND-displaying cert
  with the cert-of-built chain as verifier. Andrew's bar, explicitly NOT a self-report.
- **Bronze parquet writes continue daily** under CTO's DECLARED ACCEPTANCE -- a known, dated,
  tracked 17a violation held deliberately because changing either leg without the consumption
  map risks a dark pipeline. It is a decision, not drift.

---

## 4. STANDING HOLDS AT THIS SEAT
LEG-2 port + vendoring build: **SUSPENDED by CTO** pending the survivor ruling (item 1).
X-ii-b / X-i: behind the feeder set, unstarted.
Nothing at this seat is blocked on a person who does not know they hold it.

**Full context:** `logs/2026-08-12/session_1316-1530Z_p3_iam_producer_forensics_census_spec.md`
(substantive) and `logs/2026-08-12/session_1530-1535Z_census_build_placed_delta.md` (delta).
