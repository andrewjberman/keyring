# /self-drive D2 & D3 — tick 60 (2026-08-29 17:30Z) — state: ARMED

Covers **ticks 59, 60** (tick 58 logged @1dc896e816, **ON ORIGIN**). Cron bde882a4 (:07/:37).
Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on TWO driver acts: **an arch-gate
ruling on this seat's own project**, and **the correction of a hazard I published in TEN
consecutive logs.**

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (1 complete). Open TOs **24** (D2 18, D3 6),
unchanged across ticks 59-60. Claims scan **342 of 342 JSONs**: D2 7 / D3 1, **0
claimed-not-member**. Ledger **15 rows / 0 unconsumed** (CRLF 15 of 15). No MERGE_HEAD.
✅ **`ADVI_COTKEY` `dep_stage` PRD -> DECOMP** — the first use of that ratified value anywhere in
the corpus, and the close of the episode below.

## ✅ ARCH-GATE RULED — Blocker A, refused on a ground its finder did not have

`0.7.0_AE_CloudOps` (83348) returned a pre-apply draft that **refused to invent its own design
decision**: asked for expected plan rows, it named TWO measured blockers and three options instead.
`2.0.0_SA_COO` (83351) ruled option (c) out, asked (b) to be costed, and said **"BLOCKER A IS NOT
MINE AND I AM NOT RULING IT"** — routing it here.

⛔ **RULED: do NOT set `EventBridgeConfiguration` on `opal-data-assets`.** 83348 framed it as blast
radius — bucket-wide emission into a bucket with 8 existing lambda notifications. **True, and the
smaller half.** Measured at this seat, live, read-only:
```
  opal-data-assets/               _probe/ blackdiamond/ code/ config/ eclipse/ gold/ json/
                                  orion/ pathfinder/ portal/ schwab/ smartx/ trueshares/
  opal-data-assets/blackdiamond/  49f/   49financial/   COTTONWOOD/
```
⛔ **A THREE-FIRM BUCKET.** The flag is **bucket-wide and cannot be key-prefix scoped at the
source**, so it would **convert cross-firm separation from a STRUCTURAL property into an ENUMERATED
one** — scoping surviving only in each consuming rule's pattern. **CLAUDE.md records that exact
conversion already failing here: the cot guard banned `blackdiamond/49f/` (285 obj) while
`49financial/` (8,862, live) went unbanned until 08-27 @`7b777cf0a0`.**

**THREE BOUNDS, stated so the ruling cannot be quoted wider:** (1) an S3 EventBridge notification
carries **key metadata, not object contents** — the exposure is KEY NAMES and **I did not claim a
data leak**; (2) **I did not verify the IAM limb**, which CLAUDE.md itself records as
DESIRED/apply-UNVERIFIED, so this stands on bucket structure alone; (3) it refuses **this flag, this
bucket, this purpose** — `opal-data-inf` is already TRUE and untouched, and **its being
single-tenant is exactly why the inf precedent works and does not transfer.**
✅ **Costs the preferred route nothing:** (b)-on-existing-notifications needs no bucket flag.
⛔ **Escalation named: if (b) prices badly, the flag is NEVER-class and goes to Andrew with the
three-firm structure on the card — it does not return here as an engineering trade.**

## ⛔ A HAZARD I PUBLISHED IN TEN LOGS IS WITHDRAWN

Logs ~48-55 carried: *"`safe_deploy_core.py:548` still uploading WORKING-TREE bytes, the hazard the
discharged runners_49f rule was guarding."* ⛔ **It is the documented design, and the docstring
saying so sits 270 lines ABOVE the line I kept citing** (`:813-816`): the serve-hold gate reads
*"the CURRENT (working-tree) content … the exact bytes deploy_file would upload."* **The control and
the act are CO-PLANAR ON PURPOSE; the arrangement I scored as the failure is the correct one.**

✅ **A real residual survives, in a DIFFERENT shape:** measured across all 1,350 lines, **0 guards
on working-tree cleanliness**, and the verification is `ETag == local_md5` where **`local_md5` is
computed from the file just uploaded** — a TRANSPORT oracle, structurally unable to notice the bytes
were never committed. **Nothing ties a deployed object to a commit.** ⛔ **No gate proposed: I
measured whether the guard EXISTS, not whether the event has ever OCCURRED.**

⛔ **THE DURABILITY IS THE FINDING.** *"Tracked, not mine"* removes the re-verification trigger — a
carried item is only ever **copied forward, and copying is not reading** — and ten logs asserting it
read as established when it was one unverified reading cited ten times.

## The `dep_stage` episode — every claim of mine withdrawn

`2.0.0_SA_COO` said the enum had no stage-3 value; I "sharpened" it to two missing members with a
four-postulate record; I then found the **ratified enum has SIX values** and issued a STOP, keeping
one finding. ⛔ **`3.0.0_SA_CVO` reached further and the same line killed my survivor: line 178 is
925 characters and I had quoted ~100.** The rest declares the field OPTIONAL/FORWARD-ONLY, names
`CLOSED` unreachable **"(named, not a defect)"**, and excludes the surprise channel from the axis —
**adjudicating all three of my claims five weeks before I made them.**
✅ **ONE thing survived across three seats: `TOS_CUT` (x2) is in the corpus and not in the ratified
enum.** ⛔ **Nobody found it because all three of us hunted ABSENCES, and an intruder is not an
absence — a MECE check and a CONFORMANCE check are different sweeps.**

## Completion test (§4)

**NOT DONE — 1 of 10 projects complete.** 3 REACHABLE / 6 UNREACHABLE (seat limb);
`ADVI_49FSRC` UNREACHABLE-SOVEREIGN-HELD and surfaced. Completability still separately gated on a
publisher two records say is NOT BUILT.

## RESERVED at Andrew

**ONE, unchanged since tick 58:** `ADVI_49FSRC` — his word on Mike at 49 Financial, or a
supersede-close. **Nothing added.**

state: ARMED · push state: **LOCAL at commit**, origin/CLOUD `650360a017` (ls-remote 17:28Z).

## Compiler Tools

- `python .tools/directives-check.py --json` (ticks 59/60, timestamped) · claims scan 342 JSONs ·
  **live read-only `aws s3 ls` on `opal-data-assets` top level + `blackdiamond/` — the measurement
  the ruling rests on** · `safe_deploy_core.py` read at source (**all 1,350 lines swept for
  cleanliness guards; `local_path` traced :1227 -> :1228 -> :549; the governing docstring at
  :813-816 opened**) · `DIRECTIVE_EXECUTION_PIPELINE.md:178` **read in full (925 chars) after
  quoting 100** · `git log` on the pipeline doc (5 stage-rows at every vintage) · verdict ledger
  byte-read · two-limb CLOSE oracle · `ack_messages` — ids from each opened file's own `Msg-ID`
  line, `to_serial` verified in `broker.db` (`?mode=ro`) first · `send_message` (83253-83254,
  83259-83260, 83291-83292, 83336-83337, 83375-83377; **all DELIVERED, 0 QUEUED**).
