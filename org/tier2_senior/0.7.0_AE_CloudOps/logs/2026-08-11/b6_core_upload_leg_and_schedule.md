# B6 CORE delivered -- F3 capture uploader: B6-1 upload leg + B6-2 daily device schedule

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE

## Context
TO F3_CAPTURE_UPLOADER.B6 (COO GO 093524Z, Andrew-directed via CRO~B, every gate pre-ruled by
CTO 093024Z, CVO layout confirm 093223Z). Governing spec
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260811_BUILD_B6_AND_COMPLETION_SPEC.md
@59dc585a3c. Fit the pre-13:28Z window per COO's capacity read; bar-day clocks untouched.

## Work

1. **B6-1 upload leg (@8a789694dd, .tools/estate-capture.py, ADDITIVE -- extractor logic
   untouched per do-not #1):** `--upload [--date D] [--catchup-days N] [--bucket B]`. Day
   bucketing on the transcript timestamp's UTC date (same token grammar as manifest/{D}.json --
   the 3b joinability point). HUMAN+UNCLASSIFIED only by construction (extract_session drops
   HARNESS pre-store). Key text-input/{D}/{device}.json; idempotent; bronze-raw; in-run
   read-back sha verify on every put; no-data-day LOUD NO-PARTITION (all-empty window rc=2);
   ts-unbucketable records excluded WITH a printed + stored count.

2. **B6-2 schedule (@8a789694dd, .tools/estate-capture-schedule.ps1 + the registered task):**
   OpalEstateCaptureDaily -- daily 06:30 local, StartWhenAvailable, cmd-wrapped append log at
   ~/.claude/estate-capture-schedule.log, `--upload --catchup-days 7` (a lidded laptop
   self-heals a week idempotently). GROUP-W floor declaration in the script header (never
   event-only). Registered this session; surfaced to Andrew AT CREATION (terminal
   PushNotification: task name + cadence + disable line; mobile push inactive, Remote Control
   off -- declared). Site-Z = declared gap (header + instance exclusions).

3. **Exercised evidence (all real, no synthetic):** scheduled-task run lastresult=0 uploading
   SIX day files (08-04..08-07, 08-10, 08-11; 08-08/08-09 -- a real quiet weekend --
   LOUD-refused, the no-data-day law firing on genuine no-data days); independent read-back
   sha match f8304098a9e1 -> content verified (67 HUMAN, 0 UNCLASSIFIED, HARNESS absent);
   byte-faithfulness 67/67 text fields byte-equal served-vs-fresh-extraction; idempotency
   (same key, VersionId replaced, exactly 1 key under the day prefix); negative 2025-01-01
   rc=2 + 404; one-ARN simulate s3:PutObject on the exact key = allowed (deny-limb
   UNCOMPUTABLE for the admin-class device principal, declared -- the exercised upload is the
   22a-superior evidence); mutant: out-of-band corrupted object -> comparator FIRED ->
   restored by idempotent re-run; determinism: two extractions 3592/3592 byte-stable;
   empty-transcript-dir mutant rc=2 loud.

## Blockers
NONE. B6-3 out of scope (CTO~B's, behind the friction-axis runner build).

## Current State (zero-context)
- Code: @8a789694dd (.tools/estate-capture.py --upload mode; .tools/estate-capture-schedule.ps1).
- Live: task OpalEstateCaptureDaily REGISTERED on the laptop (next fire 06:30 local daily);
  store s3://opal-estate-report/text-input/{YYYY-MM-DD}/Andrew.json carries 6 verified day
  files (08-04..08-11 minus the empty weekend).
- Proof instances: PROOF_OF_SPEC_B6_B6-1_20260811.json + PROOF_OF_SPEC_B6_B6-2_20260811.json
  (deliverables dir), validator-passed UNPIPED with the POSITIONAL expected-ids argument
  (the TO-template's --expected-criteria flag form exits rc=2 usage -- the banked finding,
  template root-fixed by COO @b67d79971f).
- F3's real feed now EXISTS; F3 goes live when CTO~B lands B6-3 with the friction battery.
- Disable line (also pushed to Andrew): schtasks /Change /TN OpalEstateCaptureDaily /DISABLE.

## Next Steps
- [1.0.0_SA_CTO~B] B6-3 runner F3-feed wire reads text-input/{date}/ when the friction
  battery exists -- their lane, CTO gate.
- [site Z owner] register the same task via .tools/estate-capture-schedule.ps1 -Action
  Register to close the declared device gap.
- My bar-day clocks unchanged: 13:28Z wake -> chain telemetry -> bar -> X-iii -> 14:10Z
  closer -> comp-freshness canonical ADD.

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| comp-which | "upload a day-partitioned JSON capture from a device-side python tool to S3" | NO CURATED RULE (expected -- the reuse target is estate-capture.py itself; BUILD LADDER rung 2 satisfied by EXTENDING it, zero new tools minted) |
| commit-gate | .tools/estate-capture.py | PASS (pre-existing non-ASCII WARN on the extractor's display-prefix glyph data -- load-bearing, not mine, WARN-only) |
| (live primitive) | one-ARN simulate-principal-policy s3:PutObject exact key | allowed; deny-limb UNCOMPUTABLE for admin-class principal, declared |
| proof-of-spec-check | both instances, UNPIPED, positional expected-ids | rc=0 both (see instances; the flagged --expected-criteria form is the template defect, rc=2) |
| safe-commit | @8a789694dd + the instances commit | clean |

What worked: the extractor's fail-closed design meant the upload leg needed zero
classification logic -- pure plumbing as spec'd. What failed: nothing in-lane; the weekend
NO-PARTITION refusals are the law working, not failures. Gap found: comp-which has no
curated rule for device-side capture tooling (declared above; not a defect -- the catalog is
estate-scoped and this tool is deliberately device-side).
