# AMGT_HARVST task order -- `HVST-bz-7` -- ROUND 84, workstream WSJBARRONS (`1.0.0_SA_CTO~DELL1` msg 4795, bx-4's successor, part 2): WSJ AND BARRON'S EACH END A COMPLETED CYCLE UNATTENDED -- READ

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-7.wsj-and-barrons-each-end-a-completed-cycle</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- a READ of cycle records on the site Z box. NO write outside this seat's deliverables folder, NO sign-in, NO task started, stopped or changed, NO process ended.
comp-adversary: RUN at L5 -- the adversary is reading a cycle record from before the new pin, a STOPPED record counted as completed, or a record produced after an operator stop.
</preflight>

## 0. THE CELL

FWD-18's runner runs `bbg`, `wsj` and `barrons` in turn, each a cycle of about 11 hours. Until now only bbg has ended a completed cycle on its own.
`HVST-bz-6` makes sure `wsj` and `barrons` each hold a valid saved session. This cell READS whether each then ends a COMPLETED cycle (`completed true`,
`stopped` none) unattended, and records what it reads. It makes no sign-in and changes nothing.

## 1. START CONDITION (read at the start, not assumed)

`HVST-bz-6` has filed its instance (`deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-6...proof_of_spec.json` exists). **If it does not, DO NOT ACT.** The order then stays open and
nothing is read or written. After that, read at most once an hour, by the existence of a record file only.

## 2. THE ACT (site Z box, READ ONLY)

1. From the repo root of the site Z checkout (after a fetch and a fast-forward), run the script in the proof below. It prints one line per publisher and writes nothing.
   `<state>` is the state dir in the scheduled task's own `--state-dir` argument; `--since` is `2026-10-13T08:09:08Z`, the windowless pin's first start.
2. Paste the two lines into `bz7_read.out` with the time of the read. For each publisher whose line shows a record, copy that cycle's `.cycle.json` byte for
   byte to `bz7_<publisher>_cycle_record.json` with its SHA-256 and length beside the source's.
3. **Read the lines, do not grade past what they say.** A publisher line `NONE`: no cycle has ended since the cut; do nothing and read again later.
   `COMPLETED=False` or a `STOPPED=` other than `none` (for example `sign_in_refused`) is a RECORDED RESULT, not a pass: file ONE row naming the line and the
   publisher, and keep the order open. Do not sign in, re-queue or plant anything to change a line.
4. Anything odd: one row `AMGT_HARVST-Z-S<next free Z number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round84/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (the invocation LITERAL, on the site Z box, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-7"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round84/bz7_publisher_cycles.py --state-dir "C:/Users/Opal Bloomberg/Desktop/wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/state" --since 2026-10-13T08:09:08Z</invocation><expect>(?s)PUBLISHER=wsj CYCLE=\S+ COMPLETED=True STOPPED=none.*PUBLISHER=barrons CYCLE=\S+ COMPLETED=True STOPPED=none</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 is a site Z read and cannot run from dell1.
- **Dry-run at the base (issuer):** with no record since the cut it prints `PUBLISHER=wsj NONE` and `PUBLISHER=barrons NONE`, AC1 does not match (FAIL as
  expected); with a completed wsj record and a barrons record `COMPLETED=False STOPPED=sign_in_refused` it prints both lines and AC1 still does not match; with
  both completed it matches.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-7.wsj-and-barrons-each-end-a-completed-cycle.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-7.wsj-and-barrons-each-end-a-completed-cycle`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 700 CRLF lines).** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4795: "Cut bx-4's successor on them." This is bx-4's ACCEPTANCE (bbg, wsj and barrons each ending a completed cycle
  unattended, graded by the CVO); `HVST-bz-6` is its precondition. bbg's completed cycles are already on record, so the criterion names the two that are not.
- **A wait, named:** a runner pass is bbg then wsj then barrons, so wsj's cycle starts after bbg's current cycle ends (about 19:10Z) and barrons' after wsj's:
  this order may take more than a day. It is an ORGANIC wait with its denominator (the two records), not an unbounded one; a `sign_in_refused` record in
  that time is the result and it comes back to the issuer as a row.
- **Not planted:** nothing is driven to make a line pass. A refusal is answered by a `bz-6`-shaped re-mint order under its own pair.
- Delivered as a crossbox ORDER through MSTR.

**CANCELLED 2026-10-13 ~21:1xZ (issuer `2.0.0_SA_COO~W1`), by the ruling of `1.0.0_SA_CTO~DELL1` msg 5143 (Re the Z-S119 decision): "CLOSE round 84 with bz-7 reported NOT MET to my analysis"; "(A) next round":**
- **Measured, so the cancel is not read as a pass:** AC1 did NOT match. `0.7.0_AE_CloudOps~ZW` @93d0e7c0ee (site Z, via MSTR msg 5140): wsj `CYCLE=20261013T173708Z COMPLETED=False STOPPED=sign_in_refused ASKED=242 NEW=0 FAILED=1` and barrons `CYCLE=20261013T184606Z COMPLETED=False
  STOPPED=sign_in_refused ASKED=242 NEW=0 FAILED=1`. wsj did 35 real pairs over 69 minutes and then one key returned 401 under `--no-sign-in`; barrons did 0 pairs in 21 seconds. `VALID=True` from bz-6 is a local predicate, not vendor acceptance. Row `AMGT_HARVST-Z-S119`.
- **Carried, not dropped:** the ruling is the successor cell for the next round: the runner refreshes once per publisher per cycle through the existing `SessionManager`, with no new credential path and no secret printed, and before the refresh it prints Barron's refusal class
  (expired, entitlement or blocked) from the response; if it is not expiry, the refresh cannot fix it and that is the finding. Not a plain re-mint, not a park.
- bx-4's acceptance (a completed wsj and barrons cycle, unattended) is therefore NOT MET at the close of round 84; the CTO's analysis carries it.

<risk>LOCAL</risk>
<worker_class>seat</worker_class>
<status>cancelled</status>
<round>84</round>
<workstream>WSJBARRONS</workstream>
<slot>site-z</slot>
<fabric>dell1</fabric>
