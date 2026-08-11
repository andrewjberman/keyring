# ANDREW-DIRECT 2026-08-11 -- BUILD B6 (F3 capture uploader) + THE COMPLETION SPEC

**Recorded by:** `4.0.0_SA_CRO~B` · **Status:** SOVEREIGN (build directive). Broadcast to CTO + COO + CTO~B + CVO same turn.

## 1. THE DIRECTIVE

Andrew chose (AskUserQuestion, F3 approach): **"Build B6 (the real substrate)"** -- build the capture
uploader so F3 (operator signal) carries a real in-window value, rather than spec its form with a synthetic.
Rationale (his option text, endorsed): it makes F3 genuinely live, fixes the frozen operator corpus, and
creates the only home for the proactive-input class.

## 2. FINDING -- B6 IS ~70% BUILT (the hard part exists)

Same lesson as C3.i: I verified rather than assuming from-scratch.
- **DONE (the subtle part):** `.tools/estate-capture.py` -- the device-side EXTRACTOR. Pulls Andrew's
  terminal input from `~/.claude/projects/*.jsonl`; solves the mid-turn-input miss (union of
  user + queue-operation + attachment -- a naive `type==user` captures 40%); fail-closed provenance
  (HUMAN / HARNESS / UNCLASSIFIED), hardened at corpus scale (130 forged-quote preambles caught,
  document-shape backstop, byte-faithful `text` + display-stripped `text_for_quote`). Andrew ruling 7/7a.
- **MISSING (the plumbing):** `main()` only prints / `--json`. **There is no S3 upload and no schedule.**
  So the extractor runs but nothing lands in the store the runner would read.

## 3. COMPLETION SPEC (three bounded pieces; CRO specs, CTO gates, AE/BASE_EXEC builds, CTO~B owns the runner leg)

| # | piece | what | owner (suggested; COO staffs, CTO gates) |
|---|---|---|---|
| B6-1 | **Upload leg** | extend `estate-capture.py` with an upload mode: write the HUMAN + UNCLASSIFIED records to `s3://opal-estate-report/text-input/{YYYY-MM-DD}/{device_id}.json` (per-device key so a partial day is VISIBLY partial, per the tool's own docstring). Idempotent (re-run overwrites the day's device file). BRONZE discipline -- raw capture uploaded UNTOUCHED; character classification happens later at friction time, never at upload. | BASE_EXEC / AE (`.tools/` device-side + S3 write) |
| B6-2 | **Daily device-side schedule** | the tool MUST run on the DEVICE (the transcripts are device-local; the EC2 runner structurally cannot see them -- the docstring makes this forced, not a preference). A real daily schedule per the "production pipelines must have a schedule" rule -- Windows Task Scheduler on the laptop. Site-Z is a DECLARED GAP until the tool runs there too (already noted in the docstring). NOT a monitor/alarm -- a capture/archive cadence (moratorium-safe). | AE / ops + device owner |
| B6-3 | **Runner F3-feed wire** (downstream) | the runner reads the uploaded `text-input/{date}/` store as F3's feed, applies the character rubric (directed/corrective/exploratory/erratic/thrashing) at friction time with its denominator (utterances classified / captured). NOTE: the runner has NO friction battery yet (deployed subdivision = narrate/detect/author), so B6-3 rides the larger friction-axis runner build, not B6 itself. | CTO~B (runner/design owner) + AE, CTO gate |

**B6 CORE = B6-1 + B6-2** (get fresh operator input into S3). B6-3 is the consume leg and belongs to the
friction-axis runner build. Delivering B6-1+B6-2 makes F3's real feed EXIST; F3 goes live when B6-3 lands
with the friction battery.

## 3a. CTO ARCH-GATE PRE-RULINGS (093024Z) -- staffing has NO open gate question

- ✅ **S3 KEY LAYOUT APPROVED AS V1:** `s3://opal-estate-report/text-input/{YYYY-MM-DD}/{device_id}.json`
  -- per-device-per-day is the denominator discipline in key form (a partial day is VISIBLY partial; a
  merged-day key would hide which device didn't report = silence-reads-as-coverage).
- ✅ **v4-layout reconciliation DEFERRED to v4 EXISTING** (v4 = CTO~B's registered open scope, unbuilt;
  do NOT reconcile against a nonexistent layout). When v4 lands, the text-input prefix maps in or gets a
  dated repoint -- a one-act change either way.
- ✅ Device-side placement + capture-cadence-not-monitor framing CONFIRMED (a schedule that ARCHIVES is a route).
- ✅ B6-3 riding the friction-axis runner build = correct sequencing (no runner wire before the battery exists).
- **MECHANICAL GATE CHECKS when B6-1/B6-2 reach the gate** (named so the build arrives ready): (a) the
  upload leg's IAM verified on the LIVE primitive -- one-ARN `simulate-principal-policy` + an ISOLATED
  positive control (comp-iam's resource plane helps but does not suffice, per its own banner); (b) the
  schedule declared in GROUP-W terms (a floor, never event-only). CTO: "Build on."

## 3b. CVO LAYOUT CONFIRMATION + RIDERS (093223Z, grounded on the live bucket)

✅ **Key GO as proposed.** Measured on `opal-estate-report`: the bucket runs two date grammars --
`manifest/{YYYY-MM-DD}.json` FLAT (the contract-v2 key CVO's loop reads) vs `daily/2026/08/DD/`
NESTED. `text-input/{YYYY-MM-DD}/{device_id}.json` follows the FLAT form -- CORRECT, because on report-
day D both `manifest/D.json` and `text-input/D/*.json` resolve off the SAME date token (capture + its
manifest sibling stay joinable, which is what the loop wants); per-device grain fits the 2-device fabric
(laptop + site-Z land separate objects, no collision).

- **RIDER (a) BRONZE-RAW:** text-input is a bronze-tier RAW input (byte-faithful captured text). The
  extractor's `text` vs `text_for_quote` split is character-classification = a FRICTION-TIME act,
  correctly deferred. Upload the object RAW; name the prefix so nothing downstream reads it as processed.
  **The no-data-day law applies (same as B-9/L2): a no-capture day is NO-PARTITION, LOUD -- never a
  silent empty object.**
- **RIDER (b) GRAMMAR-SPLIT FLAG (Rule-24, not a blocker):** the bucket already carries flat-date
  (manifest, now text-input) AND nested-date (daily/adjudicated) on ONE axis = two grains, one axis.
  The flat choice is the right side (pairs with the manifest); ONE line routed to the v4-layout owner
  (CTO~B) so the split is a KNOWN choice, not discovered drift.
- ✅ **Frozen-corpus P1 discharge CONFIRMED:** building B6-1/B6-2 closes CVO's static-07-30-mirror
  ticket -- one build under three tickets (design s.9.1). The corpus half closes at the CVO seat.

## 4. DISCIPLINE
- CRO specs + drives; does not self-build infra or deploy (charter s.3). B6-1's `.tools/` change +
  S3 write + schedule route to the owning lane under CTO's gate; B6-3 is CTO~B's runner + CTO gate.
- BRONZE: capture is raw + byte-faithful (the extractor already enforces this); no classification at upload.
- Schedule, not event-trigger (the "production pipeline must have a schedule" rule).
- Coordinate with CVO (operational loop) + CTO~B (runner/design owner). This is the pipeline's
  single highest-leverage unbuilt item (design s.9.1) -- it also fixes the frozen-corpus P1.
