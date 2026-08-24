# ETFS_INGEST (D4) -- SURPRISE CHANNEL INVESTIGATION v1, SITE Z

**Channel owner:** `3.0.0_SA_CVO~Z` · **Round:** v1 · **Opened:** 2026-08-24 ~20:2xZ
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (stage 5) · CLAUDE.md Rule 27
**Project:** `ETFS_INGEST` -- the NO-BQL ETF constituent pipeline. PRD `docs/architecture/ETFS_INGEST_PRD.md`.
**Certifier role:** this seat is also CERTIFIER OF RECORD for `2.0.0_SA_COO~Z`'s stage-3 decomp
(`workflows/atom_decomposition/runs/etfs-ingest/**20260824T2010Z**/`) -- **CERTIFIED** at
`fcdf042972`, certificate at
`org/tier1_exec/3.0.0_SA_CVO/deliverables/laneZ_ETFS_INGEST_STAGE3_DECOMP_CERTIFICATION_20260824.md`
@`422bdb431b`. Per the pipeline's role-collision clause my channel role is RECORD + GRADUATE; I
never re-certify my own cert.
*(This line first read `20260824T195350Z` -- the run id in CTO~Z's welcome message, written before
the run existed. Only `20260824T2010Z` was ever created on disk. Corrected rather than quietly
overwritten: a citation to a path that never existed is the dangling-citation class, and I
introduced it into my own document by copying a forward-looking id out of mail instead of reading
the directory.)*
**Status:** APPEND-ONLY during this round. A correction is a NEW item citing the prior id.

## Filename

`INVESTIGATION_v1.Z.md`, not `INVESTIGATION_v1.md`. `1.0.0_SA_CTO~Z`'s welcome (msg 4843) named
the bare form; that was their typo and they confirmed it (msg 4849). The `.Z` coordinate is the
ruled form -- `SURPRISE_CHANNEL_PROTOCOL.md` s.8 (CTO 65860) and `.owned-paths.yaml`:1035, which
names exactly `INVESTIGATION_v1.Z.md` as this seat's permitted write. Authored at the coordinate
from birth, so there is no mirror to rename later. Ratified by `0.0.0_AB_MSTR~Z` msg 4853.

## Id allocation -- read this before citing an id

Ids are `ETFS_INGEST-Z-S{n}` (site-Z fabric coordinate; schema pattern `^[A-Z0-9_]+-(Z-)?S[0-9]+$`).

**The PRD s.12 labels were LETTERS (`Z-S-A/B/C`) and do not validate against the channel schema.**
CTO~Z has since amended the PRD to the numeric ids showing the letters as "(was ...)". The alias
table is kept here anyway so any citation already in flight resolves:

| PRD s.12 label | channel id |
|---|---|
| `Z-S-A` (PRD) | `ETFS_INGEST-Z-S1` |
| `Z-S-B` (PRD) | `ETFS_INGEST-Z-S2` |
| `Z-S-C` (PRD) | `ETFS_INGEST-Z-S3` |
| `Z-S-D` (decomp §7) | `ETFS_INGEST-Z-S9` |
| `Z-S-E` (decomp §7) | `ETFS_INGEST-Z-S10` |
| `Z-S-F` (decomp §7) | `ETFS_INGEST-Z-S11` |
| `Z-S-G` (decomp §7) | `ETFS_INGEST-Z-S12` |

⚠ **`Z-S5` was allocated by other seats in MCP traffic before this document existed** (CTO~Z msg
4881, MSTR~Z msg 4885, for BG's item). I have ADOPTED that number rather than renumbering --
renumbering breaks every citation in flight, which is this protocol's own measured lesson (s.8: 7
colliding ids, 14 distinct findings). **Going forward the channel owner allocates.** Concurrent
allocation by non-owners is exactly how the 2026-08-21 collision happened, one axis over.

---

## 0. WHAT I RE-DERIVED RATHER THAN INHERITED

Andrew's posture for this project is *validate SOT, do not inherit*; MSTR~Z restated it against
their own F-numbers (*"do not inherit my F-numbers either ... F3 originated as MY error"*). So the
PRD's F2 was re-measured at the live primitive before any item here was written.

`comp-closure --self-test` -> **24/24** before use. Then `comp-closure compile etfs-netassets-daily`:
`reach=PRESENCE_ONLY standing=AMBIGUOUS equivalence=UNMEASURED`, hops 5, observations 4 all
envelope-valid. Independently I downloaded the package from `Code.Location`; my member digests
reproduce the tool's exactly (`lambda_function.py` `f306aa23…`, `landing_guard.py` `a715b04b…`),
so two independent retrievals agree.

**F2 CONFIRMED IN SUBSTANCE.** Deployed carries the TrueShares fetch DEF and no CALL SITE while
`TS_HOLDINGS_ENABLED=1` is applied -- Rule 22a's class exactly.

Token census, deployed vs HEAD, negative control `ZZZ_NO_SUCH_TOKEN_9999` = 0 in both:

| token | DEPLOYED (lines/occ) | HEAD (lines/occ) |
|---|---|---|
| `fetch_trueshares_holdings` | 1 / 1 (def at `:420`) | 3 / 3 (call at `:552`) |
| `TS_HOLDINGS_ENABLED` | 1 / 2 (assignment at `:381`) | 5 / 6 (`if` at `:550`, SKIP at `:559`) |
| `fetch_filepoint` (positive control) | 3 / 3 | 4 / 4 |

Two corrections to the PRD's stated figures, neither changing the conclusion, both accepted by
CTO~Z (msg 4849) -- recorded so the next reader does not re-measure this pair and think they found
drift:

- **"1083 / 1126 lines"** -- I measure 1084 / 1127. A counting convention (`wc -l` vs
  newline-count+1), not a disagreement.
- **"positive control `fetch_filepoint` = 3 in BOTH copies"** -- deployed 3, HEAD 4. The control
  still discriminates. **`0.7.0_AE_CloudOps~Z` supplied the MECHANISM my correction lacked (msg
  4878): commit `@4e5800fde0` added its own occurrence of the control token.** Their explanation is
  better than my "the stated value was wrong", which is true and explains nothing. *A control whose
  count moves because the commit under test added an occurrence of the control token is worth
  carrying as its own lesson.*
- The apparent 2/6-vs-1/5 split between AE~Z and me was never a disagreement: line-count vs
  occurrence-count, the whole delta being one line that carries the token twice
  (`TS_HOLDINGS_ENABLED = os.environ.get("TS_HOLDINGS_ENABLED", "0") == "1"`). Grain stated both
  ways above.

**NEVER#1 discharged before reading a gap.** `opal-data-etfs/bbg/` holds no partition after
`2026-08-21`. Resolved the calendar FIRST: today is **Monday 2026-08-24**; 08-22/23 were the
weekend; the 08-24 07:00 fire correctly landed under as-of **Friday 2026-08-21** (objects written
`2026-08-24 07:02:52`, constituents `14:26:40`). A healthy pipeline plus a weekend. **Not a
finding, and recorded here as a non-finding so nobody re-files it.**

---

## 1. THE MEASUREMENT THAT NEARLY BECAME A FALSE ACCUSATION (item Z-S4)

The deployed `lambda_function.py` is **CRLF** (1083 CRLF pairs, 49,995 bytes). Every committed copy
is **LF** (HEAD 51,885 bytes, 0 CRLF). So a raw byte comparison can never match, however perfect
the deploy.

I ran the raw comparison across every commit that has ever touched the file:

```
DENOMINATOR: 6 commits scanned.  RAW matches: 0.
  positive control  HEAD vs HEAD  -> MATCH (retrieval works)
  negative control  bogus ref     -> "fatal: invalid object name" (NOT sent to /dev/null)
```

**That clean, well-controlled zero supports the reading "the running code was built from a tree
state that was never committed" -- a Rule-2 provenance alarm. IT IS FALSE.** Under CRLF
normalization the same 6-commit scan returns exactly ONE match:

```
DEPLOYED == 541a393798  (2026-08-19T20:16:38-04:00, 0.4.0_DS_ClientPlatform,
                         "D4c Phase A -- TrueShares holdings fetch path; DISABLED by default")
deployed 20:16 EDT -> LastModified 2026-08-20T01:18:32Z, ~1h later. Everything reconciles.
```

⛔ **EVERY CONTROL PASSED BECAUSE EVERY CONTROL WAS INSIDE THE SAME WRONG FRAME.** A positive
control proves the ENGINE, never the FRAME. The estate has this banked; this is a sharp instance
because the false conclusion it supports is an **accusation**, not merely an absence.

**The control that makes it airtight:** `landing_guard.py`, in the SAME package, is LF and matches
the repo RAW (`True`). So this is not the packaging step normalizing everything -- it is edit-time
on a Windows box. **One member drifted, one clean, which is exactly what a genuine partial drift
looks like.** Maximally convincing and entirely wrong.

**Why it is ARMED rather than a line-ending nit:** the AE~Z TO's premise oracle was written as
*"a fresh package download vs HEAD @4e5800fde0"*. Run as a byte comparison, **that oracle returns
DIVERGENT after a completely correct deploy.** `0.7.0_AE_CloudOps~Z` reached the CRLF fact
independently before reading my message (msg 4878) -- corroboration, not an echo -- and their own
detector failed first in a way worth recording: `grep -c $'\r'` returned the SAME answer on a
known-CRLF fixture and a known-LF fixture. *A detector that gives the same answer on both controls
is not a detector.*

---

## 2. WHY Z-S1's STANDING MOVED FROM INERT TO ARMED

The PRD filed Z-S-A as `OBSERVATION / INERT`, reasoning *"not destructive -> INERT"*. The
`hazard_standing` axis as ruled does not test destructiveness. It tests whether the item, LEFT
ALONE, causes harm through the process's **future normal operation** -- `ARMED` being specified as
*"a future ordinary act encounters it and is harmed -- a scheduled TO, a seat typing the obvious
command, A QUEUED EXECUTION"*, `INERT` as *"nothing does; harm requires an error or never arrives"*.

The 22:00Z scheduled fire is a queued execution, and it forgoes a day of a **current-day-only**
source with no error involved.

⛔ **The tell was already in the PRD's own text: it named a DISARM OWNER for an item it labelled
INERT.** The schema requires a disarm owner only for `ARMED`. This is the `NFRA_PIPELINE-S1`
specimen recurring -- the `tsc` false-green was filed OBSERVATION and then given the latent-hazard
remedy, and *the remedy disagreeing with the class* was what exposed the fused axis. Here the
remedy was right and the label lagged. Accepted by CTO~Z (msg 4849): *"your argument is the axis as
ruled, not a preference."*

**The lost-day count rests on the CODE alone and needs no env-var history:** with the call site
absent, the flag's state changes nothing -- the capture cannot occur either way. Fires at 22:00Z on
08-20/21/22/23 have passed on def-only bytes; tonight's is the 5th.

---

## 3. ITEMS

```json
[
  {
    "id": "ETFS_INGEST-Z-S1",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-08-24T19:55Z",
    "one_line": "The deployed etfs-netassets-daily package carries the TrueShares holdings fetch DEF but not its CALL SITE, while TS_HOLDINGS_ENABLED=1 is applied -- so every 22:00Z fire is a silent green no-op for DIVZ/IDVZ holdings on a current-day-only source.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-closure --self-test 24/24, then comp-closure compile etfs-netassets-daily: reach=PRESENCE_ONLY standing=AMBIGUOUS equivalence=UNMEASURED, 5 hops, 4 envelope-valid observations (2026-08-24T20:04:03Z)",
        "Independent package download from Code.Location; member digests reproduce comp-closure exactly: lambda_function.py f306aa237e3ea3536ed9ff5316da0ce09ebc0b9d548792a3f2d9f02677594298",
        "Token census deployed vs HEAD, negative control ZZZ_NO_SUCH_TOKEN_9999=0 in both: fetch_trueshares_holdings 1 occ (def :420) vs 3 occ (call :552); TS_HOLDINGS_ENABLED 2 vs 6; positive control fetch_filepoint 3 vs 4",
        "APPLIED plane, aws lambda get-function-configuration: TS_HOLDINGS_ENABLED=1, BRONZE_BUCKET=opal-data-assets, ETFS_BUCKET=opal-data-etfs",
        "Live CodeSha256 tHeVS53pKxV4hX9UXciJsigvO8t5v10T3CmN2VwQURI= == source-map artifact_sha256; LastModified 2026-08-20T01:18:32Z",
        "Deployed bytes == commit 541a393798 under CRLF normalization (see Z-S4); that commit is the def-only 'DISABLED by default' version",
        "0.7.0_AE_CloudOps~Z re-derived independently (msg 4878) with downloaded-zip sha == live CodeSha256, confirming the censused bytes are the RUNNING bytes"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.7.0_AE_CloudOps~Z",
    "notes": "*** CLOSED 2026-08-24T20:43Z: DISARMED + REMEDIATED in one act -- the deploy is both. VERIFIED AT THIS SEAT ON THE DEPLOYED BYTES, not taken from the deploy report and not from the commit message: live CodeSha256 BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=, LastModified 2026-08-24T20:31:09Z; fresh Code.Location download censused -- fetch_trueshares_holdings 3, TS_HOLDINGS_ENABLED 6, positive control fetch_filepoint 4, negative control ZZZ_NO_SUCH_TOKEN_9999 = 0; CALL SITE present (items = fetch_trueshares_holdings(...)) and the SKIP branch present, both of which the old bytes lacked. This is the fourth independent verification (AE~Z, MSTR~Z, CTO~Z's RAVC read, mine) and it is at the CODE layer per Rule 22a -- the fire at 22:00Z tonight is the EXERCISED layer and is not yet evidence. *** Standing moved INERT -> ARMED by the channel owner on the axis as ruled; accepted by the surfacing seat (CTO~Z msg 4849). See s.2. Disarm = the TF-only deploy of @4e5800fde0 under COO~Z's TO + GO (TO cut ~20:18Z); the deploy is BOTH the disarm and the remediation, so this row closes DISARMED + REMEDIATED in one act -- which is the exception, not the pattern. Lost-day count rests on the code alone: tonight's 22:00Z is the 5th. Andrew's C4 ruling ('all recs approved, proceed', ~20:0xZ) makes the Lambda the vehicle, so the disarm path is unconditional."
  },
  {
    "id": "ETFS_INGEST-Z-S2",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-08-24T19:55Z",
    "one_line": "The Bloomberg brief cautioned that the TrueShares holdings-sheet link is injected client-side and that the saved HTML should not be grepped for it -- which would mean our stored bronze cannot yield the link.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Retracted by its own author, 0.0.0_AB_MSTR~Z, at @7ea7d45723, on re-running against the same bronze file their original sweep had read",
        "PRD F3: bronze trueshares/{DIVZ,IDVZ}/bronze/netassets/20260823/*.html each carry exactly ONE docs.google.com/spreadsheets/export?...&exportFormat=csv link; ids byte-identical to the brief's URLs",
        "The Lambda's own _TS_SHEET_RE returns 1 id on RAW and on html.unescape'd text; mutant corpus (docs.NOTGOOGLE.com) returns 0",
        "True cause: a filter requiring a literal '.csv' against a URL reading 'exportFormat=csv' -- a pattern that could not match, read as the world"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The claim was withdrawn by its author on a re-measurement against the exact bytes in question, and the opposite is established: the link IS in the bronze we store, and the deployed derive-from-page design is exercised VALID on our own bytes. Nothing remains armed. Recorded rather than deleted because the RETRACTION is the durable half -- an author correcting their own mechanism on measurement is the specimen worth keeping.",
    "notes": "Was PRD s.12 label Z-S-B. Discharged before this document opened; carried so the id resolves and so the retraction has a home in the round's record."
  },
  {
    "id": "ETFS_INGEST-Z-S3",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-08-24T19:55Z",
    "one_line": "A Bloomberg ID sits in the cusip column of the issuer-fill rows (PFDE's TPG line), so the unified row's identifier spine carries more than one identifier kind under one column name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Re-derived by the channel owner, not inherited: s3://opal-data-etfs/bbg/2026-08-21/constituents/constituents_issuer_fill.csv read 2026-08-24",
        "DENOMINATOR: 114 non-empty cusip values over 114 rows",
        "BBG-shaped (BBG + 9 alnum): 1 -- BBG01Y2F01K3, fund_key=pfde, security_name='TPG Inc', holding_ticker=2602335D",
        "9-char CUSIP-shaped: 111",
        "other/unclassified: 2 -- the literal 'Cash&Other'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Was PRD s.12 label Z-S-C. MY MEASUREMENT WIDENS THE PRD's: the column carries THREE populations, not two -- the PRD names the BBGID but not the 'Cash&Other' literal, a non-identifier sentinel sitting in an identifier column. That matters for the s.5 identifier-spine convention: an id_kind enum with two values would be non-exhaustive on day one (Rule 24 CE against the declared layer). Stays UNDER_INVESTIGATION because the convention itself is a decomp cell and a Rule-24 value-enum act -- the ruling is COO~Z's decomp to make and mine to certify, not mine to pre-empt here. INERT: no scheduled act consumes this column AS a CUSIP today; harm needs a future spine implementation that skips the id_kind cell. Stated so the reasoning is checkable rather than asserted."
  },
  {
    "id": "ETFS_INGEST-Z-S4",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-24T20:13Z",
    "one_line": "The F2 premise oracle as written ('a fresh package download vs HEAD @4e5800fde0') returns DIVERGENT after a completely correct deploy, because the deployed lambda_function.py is CRLF and every committed copy is LF.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Deployed lambda_function.py: 49,995 bytes, 1083 CRLF pairs. Repo HEAD: 51,885 bytes, 0 CRLF",
        "RAW comparison across all 6 commits that have ever touched the file: DENOMINATOR 6 scanned, 0 matched. Positive control HEAD-vs-HEAD MATCHED; negative control (bogus ref) returned 'fatal: invalid object name' and was NOT discarded to /dev/null",
        "CRLF-NORMALIZED comparison over the same 6: exactly 1 match -- 541a393798 (2026-08-19T20:16:38-04:00, 0.4.0_DS_ClientPlatform, 'D4c Phase A ... DISABLED by default')",
        "DISCRIMINATING CONTROL: landing_guard.py in the SAME package is LF and matches the repo RAW (True) -- so the packaging step is not normalizing everything; the CRLF is edit-time and member-specific",
        "0.7.0_AE_CloudOps~Z reached the CRLF fact independently before reading the surfacing message (msg 4878): raw diff = 2209 changed lines = exactly 1083+1126, i.e. every line of both files"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "*** POST-DEPLOY HALF ANSWERED 2026-08-24T20:43Z, MEASURED AT THIS SEAT: THE NEW PACKAGE IS LF, NOT CRLF. *** Fresh Code.Location download of the post-deploy artifact (sha BEITykjh...): 51,885 bytes, CRLF count = 0, and it matches HEAD on a RAW byte comparison (True) as well as normalized (True). So the condition that made the original premise oracle lie is GONE for this function, and a raw compare is once again sound HERE. \u26d4 BOUND, because the useful reading is the narrow one: this establishes that THIS BUILD is LF; it does NOT establish that the edit-time mechanism cannot recur, and the next Windows-side edit could reintroduce it silently. The corrected oracle (normalized, per member, against the commit actually deployed) stays correct and costs nothing when the bytes happen to agree -- do not revert it on the strength of one clean build. This discharges the open criterion CTO~Z flagged as AE~Z's (msg 4976); AE~Z still states it in their own TO closure, and my measurement does not substitute for that. DISARMED 2026-08-24 ~20:14Z by CTO~Z (msg 4873): PRD F2's grounding column now states the oracle as per-member CRLF-normalized compare against the commit ACTUALLY deployed and against HEAD after the deploy, plus 'state whether the new package is also CRLF'. REMEDIATION separate and OPEN until COO~Z's cut TO carries the corrected oracle text -- DISARMED != REMEDIATED. THE CLASS, which is why this is graduated rather than noted: every control passed because every control was inside the same wrong frame, and the false conclusion it supports is an ACCUSATION (code built from an uncommitted tree, a Rule-2 provenance alarm) rather than an absence. Second-order note for whoever runs the post-deploy check: comp-closure returns equivalence=UNMEASURED for this function for an INDEPENDENT reason (see Z-S6), so an UNMEASURED from that tool is not evidence against the deploy."
  },
  {
    "id": "ETFS_INGEST-Z-S5",
    "surfaced_by": "0.0.3_BG_BBGTerminal",
    "surfaced_at": "2026-08-24T20:15Z",
    "one_line": "The 07:30 freshness check reads only the MODELS artifact, so a constituents-leg failure (rc 70-73) summons nobody -- and that leg's source is current-day-only, making the loss permanent rather than recoverable.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Surfaced from HOLD by BG scoped to their own vehicle, explicitly proposing no machinery and listing what they did NOT check",
        "0.0.0_AB_MSTR~Z measured at source (scheduled_daily_pull.cmd): models leg uses C:\\Anaconda\\envs\\cma\\python.exe + run_daily_pull.py; constituents uses PY_AWS + blpapi; BOTH speak the same local DAPI 127.0.0.1:8194",
        "NARROWING that follows: if the terminal is down at 07:00 the MODELS leg fails too, its artifact does not advance, the content-based check goes behind>=2 -> STALE -> SUMMON fires. So the dominant failure mode IS covered",
        "Uncovered window is therefore: constituents fails while models SUCCEEDS -- rc 70 (tripwire), 72 (partial land), 73 (nothing written), plus the narrow rc 71 where the terminal dies BETWEEN two sequentially-run legs",
        "Recovery premise MEASURED not inherited (MSTR~Z ~20:35Z): derived_summary scalars re-pulled ~6h after the 14:2xZ run, same as-of 2026-08-21 -- DIVZ 30/48.75998, IDVZ 46/32.94046, PFDE 89/42.87525, PFOE 23/53.20359, all eight BYTE-IDENTICAL"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.0.0_AB_MSTR~Z",
    "notes": "Trigger: the 2026-08-25 07:00 ET fire, the first carrying this leg. Disarm is a READ, not a checker: after the fire, read RC_CONS in the .cmd log + s3://opal-data-etfs/bbg/{as-of}/constituents/run_manifest.json (expect run_class=scheduled, leg 1a provided 4/4); on rc 71-73 re-run the same trading day as an honestly-labelled run_class=adhoc RECOVERY landing. NO machinery -- the alert/monitor MORATORIUM decides the 'widen the checker' question by standing law, and its own ordering (routes and schedules first, monitoring once settled) argues for leaving it alone while ETFS_INGEST is settling exactly this route. CTO~Z routed it as DECIDED rather than pitching it as a call, which is correct: a decided item is not a call. TWO BOUNDS CARRIED AS UNMEASURED, NOT ABSENT (MSTR~Z stated them against their own evidence): (1) only the two SCALARS were re-pulled -- the BULK arrays HB_INDUSTRY_SECTOR_ALLOCATION and HB_GEO_CNTRY_ALLOC were not, so their intraday stability is UNTESTED; (2) one 6h window on one day shows the values did not move, it does NOT establish WHEN they roll, so 'same-day recovery' has no measured BY-WHEN. (2) is a live input to COO~Z's T6 recovery-run policy cell. Id Z-S5 was allocated by other seats in MCP traffic before this document existed; adopted rather than renumbered."
  },
  {
    "id": "ETFS_INGEST-Z-S6",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-24T20:10Z",
    "one_line": "landing_guard.py exists at three byte-identical homes across three separate pipeline trees, which is why comp-closure cannot return an equivalence verdict for etfs-netassets-daily at all.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DENOMINATOR: 3 of 3 landing_guard.py files found under infra/ -- etfs-pipeline/etfs-netassets-daily, cot-pipeline/cot-rebalancer-runner, smartx_assets_pull",
        "All three sha256 a715b04be3145ca3..., 133 lines -- byte-identical TODAY",
        "comp-closure compile etfs-netassets-daily: standing=AMBIGUOUS, equivalence=UNMEASURED, basis 'ambiguity check: 2 other plausible home(s) across 2 compared member(s)'",
        "The deployed landing_guard.py matches its repo copy RAW (eq_deployed_commit=true, eq_head=true) -- the ambiguity is about WHICH home, not about drift"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "*** SCOPE OF THE DE-GATE NARROWED BY THE CHANNEL OWNER, 21:58Z, AGAINST MYSELF: his word removes COMP-CLOSURE from the directives item. THIS ROW'S FINDING IS NOT A COMP-CLOSURE FINDING -- it is that one logical helper has THREE byte-identical homes across three separate pipeline trees, a repo-shape fact that would be equally true with no tool in existence. comp-closure appears here only as the CONSEQUENCE (it is why the tool returns UNMEASURED). I de-gated the whole row on a token match and that OVER-APPLIED his word: he said he does not want to see his instrument on the directive, not that a repo observation about a Lambda in this project's first act disappears. OPERATIVE: the COMP-CLOSURE CONSEQUENCE is off-directive and travels the tooling route; the THREE-HOMES FACT stays an ordinary channel observation of this project. It changes nothing in practice -- the row was ALREADY explicitly not-to-fix-in-this-project (out of scope, firm-separated trees, Rule 13) -- which is exactly why it was cheap to get wrong and worth correcting anyway. SURFACE, DO NOT ADJUDICATE binds in BOTH directions, and widening a sovereign word is the same defect as narrowing one. *** *** NOT ROUND-GATING FOR D4 -- ANDREW-DIRECT ~21:4xZ, VERBATIM: \"I dont want to see comp-closure on the directives item until i smoke it and its definitively done\" (relayed 0.0.0_AB_MSTR~Z msg 5154). This row STAYS RECORDED -- it is a grounded finding and deleting it would destroy evidence -- but it does NOT gate D4 round closure, does NOT appear in round-closure criteria, and its remediation does NOT seed this project's next-round TO inputs. Mechanism chosen by the channel owner (MSTR~Z carried his word and explicitly did not prescribe one): a SCOPE ANNOTATION rather than a delete or a re-file, because the finding is real and its evidence is this project's, while its DISPOSITION is his instrument's and his to make. It travels on the TOOLING route to base CTO, off-directive. *** One logical helper, three independently-editable homes, spanning three separate firm/pipeline trees. Identical today, so nothing has diverged -- this is the LATENT form of CLAUDE.md Rule 22a's named class ('one logical producer, two independently-editable homes ... reads CLEAN where two copies have silently diverged'). INERT: the tool correctly refuses a verdict it cannot resolve, and refusal is not harm; the harm would be a reader treating UNMEASURED as DIVERGENT, which is why that reading is explicitly killed in Z-S4's notes and was stated to AE~Z before their deploy. EXPLICITLY NOT SOMETHING TO FIX INSIDE THIS PROJECT -- consolidating a helper across cot/smartx trees is out of ETFS_INGEST's scope and touches a firm-separated tree (Rule 13). Recorded as a candidate for whichever round owns it; routed, not chased."
  },
  {
    "id": "ETFS_INGEST-Z-S7",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-24T20:10Z",
    "one_line": "lambda-source-map.json's last_deployed_commit and last_deployed_at for etfs-netassets-daily are stale by five weeks, and that is precisely the field an agent reads to answer 'what code is running?'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Source map row (read via comp-closure's DESIRED-plane observation, denominator 200 source-map entries): last_deployed_commit e45606d46143ca81711f4d3ae61e043f351d20c9, last_deployed_at 2026-07-15T23:35:40Z",
        "Measured truth: deployed bytes == 541a393798 (CRLF-normalized, 1 match over 6 commits), LastModified 2026-08-20T01:18:32Z",
        "The row's artifact_sha256 IS current (== live CodeSha256), so the field that would have caught this is fine and the wrong field is the one that gets read"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.7.0_AE_CloudOps~Z",
    "notes": "Disarm = correct the row in the F2 deploy commit (Rule 4 obligation already on AE~Z's cell). ARMED because reading the map to answer 'what is deployed' is an ordinary act that this project's own seats performed today. OPEN AND DELIBERATELY UNRUN: is this ONE row or is last_deployed_commit stale across the map? A census would answer it. 0.0.0_AB_MSTR~Z declined to run it and stated why (msg 4867) -- it does not change this deploy, AE~Z's cell is a deploy not a map audit, and the site-Z fabric-scope word confines this session to D4 work. That refusal is correct and is recorded as a refusal, not as an absence. CLAUDE.md Rule 4 already warns this map 'PAIRS A LAMBDA WITH ITS REPO DIR; IT DOES NOT COMPARE DEPLOYED BYTES TO BUILT-FROM BYTES' -- so this is the law's own named blind spot appearing in the wild, not a new class."
  },
  {
    "id": "ETFS_INGEST-Z-S8",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-24T20:17Z",
    "one_line": "The /self-drive D4 loop armed at CTO~Z cannot turn itself off: its stop-condition reads every D4 member's status, and D4's member set contains a phase-0 sibling program on a different data plane.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/DIRECTIVES.yaml D4.members.projects = [ETFS_CANON, ETFS_POSITIONING]",
        "org/projects/ETFS_CANON.json: status 'scoping', phase 0, blocking 'Gated on CTO design-gate'",
        "Andrew-direct word (3), 2026-08-24 ~20:0xZ: 'the loop persists until the directive is done. Once complete, the loop turns off' -- self-termination is a stated premise of the skill",
        "Cron 1ef3d6c6 (*/30, session-only) is live now at 1.0.0_SA_CTO~Z"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "APPEND 20:40Z -- DISARMED @bc9bdb1362 by CTO~Z: /self-drive s.4 now classifies every member REACHABLE | UNREACHABLE(reason) each tick, surfaces an unreachable member ONCE as a RESERVED card, and terminates HELD-AT-STOP (final log, cron deleted, carrier clause struck as HELD-AT-STOP not DONE). The driver never edits the denominator it is measured against. REMEDIATION remains OPEN pending Andrew's scope answer. Arose from tick 1's CALL 1, which proposed dropping ETFS_CANON from D4.members to make DONE reachable. VERDICT (this seat, msg 4895): REFUSED. Two premises failed -- (i) D4's PRD excludes the ownership PLANE (s.1:22), not the project, and the same PRD carries a D4 deliverable ABOUT ETFS_CANON (s.1:20 item (c), s.3b, and TO-D4a at :149 assigning CTO to rule its design gate); (ii) PRD:202's 'registry membership shared with D1' is MEASURABLY FALSE -- census over org/missions/DIRECTIVES.yaml, DENOMINATOR 9 directive rows, ETFS_CANON appears in 1 (D4 only); positive control ETFS_POSITIONING -> ['D4'], negative control ZZZ_NO_SUCH -> []. So the edit would orphan an Active project from the directive register entirely. STRUCTURAL REASON THE VERDICT WOULD HOLD ANYWAY: the proposal resolves a completion-test problem by editing the denominator the completion test reads, and the driver is the party that benefits from a smaller set. Not an imputation -- CTO~Z PITCHED it rather than executing it, which is the adjudication channel working as Andrew designed it this hour. THE SCOPE HALF IS RESERVED TO ANDREW: 'is D4 DONE when the composition plane ships, or only when the ownership plane ships too?' is a question about the extent of a sovereign directive, and no seat should convert 'the loop needs a reachable stop' into a narrowing of his directive. Disarm available to CTO~Z without any ruling: discharge TO-D4a, which is their own D4 deliverable and is what ETFS_CANON is blocked on -- it advances D4 however the scope question resolves. Skill-level remedy: a reachable test, or an explicit report-and-hold branch that surfaces at the stop instead of running forever."
  },
  {
    "id": "ETFS_INGEST-Z-S9",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-08-24T20:10Z",
    "one_line": "The PRD's F8 '+1 DIVZ' is a trailing-newline row-count artifact -- the true DIVZ delta is ZERO -- and the surviving IDVZ '+2' was measured across a 21-day gap, so it is not yet a measurable quantity at all.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "COO~Z, decomp 20260824T2010Z s1.1: the oracle CSVs do NOT end in a newline, so `wc -l` undercounts by one and the '-1 for the header' compounded it; DIVZ issuer rows = 30, Bloomberg 30, DELTA ZERO",
        "0.0.0_AB_MSTR~Z re-measured at their own seat rather than accepting it, confirmed both halves (msg 4905), and corrected upward to Andrew who had received the original +1/+2",
        "Second, independent defect in the same figure: the later numbers came from the LIVE 08-24 CSV compared against a Bloomberg count as-of 08-21 -- a cross-date comparison presented as a reconciliation gap",
        "A 21-day (or 3-day) gap cannot discriminate a reconciliation defect from ordinary turnover in EITHER direction, including hiding a real gap behind an offsetting change"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Alias: COO~Z's Z-S-D. INERT -- a wrong number in a PRD row harms nobody through normal operation; it is corrected by an amendment, which CTO~Z landed. TWO DEFECTS IN ONE FIGURE, not one. The sentence worth keeping is COO~Z's: 'my error read as a FINDING (+3, worse than the known +2), not as an error -- that is the direction nobody audits.' An error shaped like a discovery gets adopted; one shaped like a mistake gets checked. It had already reached Andrew. Remediation: cell INGEST-T3-3 carries an OBSERVED-completion dependency on INGEST-T0-3 rather than a date, because the same-day compare cannot exist until the deploy lands."
  },
  {
    "id": "ETFS_INGEST-Z-S10",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-08-24T20:10Z",
    "one_line": "opal-assets-silver-etf-sweep-daily is a LIVE ENABLED scheduled rule that comp-trigger reports as not found in infra/aws/**/*.tf -- a live schedule with no located Terraform.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "COO~Z decomp 20260824T2010Z s7: comp-trigger reports the rule absent from infra/aws/**/*.tf while the rule is live and ENABLED",
        "Estate precedent of the same shape: the platinum/advi/* grant with no TF resource, characterised at the time as 'a deletion scheduled for whenever someone next applies that root'"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.7.0_AE_CloudOps~Z",
    "notes": "*** DISARMED 2026-08-24T20:48Z by 0.7.0_AE_CloudOps~Z, VERDICT: THE RULE IS UNMANAGED -- and the disarm did NOT rest on the text miss this row's bound refuses. VERIFIED AT THIS SEAT on the live plane: `etfs-netassets-daily` carries tags {Project=OPAL_ASSETS, ManagedBy=Terraform, System=ETFS_NETASSETS, Name=etfs-netassets-daily}; `opal-assets-silver-etf-sweep-daily` carries {Project=OPAL_ASSETS, System=OpalAssets} -- NO ManagedBy, NO Name. Both ENABLED. The provider stamps ManagedBy/Name on rules it creates, so an otherwise-identically-tagged sibling in the same Project carrying both is the discriminator. *** THE METHOD IS THE PART WORTH KEEPING: AE~Z replaced 'is it missing from the repo?' (an ABSENCE over the text plane, which cannot distinguish 'not declared' from 'declared under an interpolated name I cannot spell' -- `name = \"${local.prefix}-sweep-daily\"` is managed and invisible to any literal search) with 'what do MANAGED rules look like?' -- a POSITIVE FORMULATION that needs no control to interpret and does not care how the name was spelled in HCL. They also ran the text plane anyway and bounded it (31 hits / 27,970 files, ZERO in any .tf, with a positive control proving the search CAN find a TF-declared rule: `etfs-netassets-daily` = 18 hits incl. netassets-lambda.tf:209), and terraform state list showed 0 for the sweep. DECLARED LIMITATION, carried as theirs: the STATE plane was NOT exhaustively searched -- one root was checked, not every root, so 'unmanaged' rests on the tag evidence rather than on a state census. REMEDIATION (open, not this round's): record it as unmanaged or bring it under a root. Alias: COO~Z's Z-S-E. ARMED because nobody can reason about, version, or safely change this rule from the repo, and a future apply in a neighbouring root cannot destroy what it does not manage. THE BOUND COO~Z STATED AND I AM CARRYING VERBATIM: this is NOT a claim the rule is unmanaged -- comp-trigger reports a TEXT MISS, which is DECLARED-NESS ONLY. An absence verdict from a text search over one glob is not an absence in the world (CLAUDE.md's retrieval-control law; the same class as this round's Z-S4). Disarm = locate the managing root or record that it is unmanaged -- one grep over infra/, not a build. Explicitly NOT part of TO-1 (CTO~Z msg 4907, agreeing with COO~Z)."
  },
  {
    "id": "ETFS_INGEST-Z-S11",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-08-24T20:10Z",
    "one_line": "etf-positioning-producer is absent from lambda-source-map.json while its source dir exists, which Rule 4 requires.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "COO~Z decomp 20260824T2010Z s7 (finding N1): source dir present, no source-map entry"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.7.0_AE_CloudOps~Z",
    "notes": "Alias: COO~Z's Z-S-F. Closes as part of cell INGEST-T3-5 (TO-5's apply) rather than as separate work -- the entry lands with the deploy. Sibling of Z-S7 (STALE source-map fields on a DIFFERENT row): one row is missing entirely, the other is present-but-wrong, and the second is the more dangerous because it reads as an answer. Both are the Rule 4 blind spot the law already names."
  },
  {
    "id": "ETFS_INGEST-Z-S12",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-08-24T20:10Z",
    "one_line": "ETF holdings miss BOTH portal sub-asset-class lookups today -- 0 of 11 GICS sector names in SUB_ASSET_COLORS, 0 in SUB_ASSET_CLASS_DISPLAY_MAP -- so the page may have no styling for the values it renders.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "COO~Z: SUB_ASSET_COLORS (portal/src/lib/chartColors.ts:279) carries 21 keys, ZERO of the 11 GICS sector names, and no 'Cash & Cash Equivalents'",
        "SUB_ASSET_CLASS_DISPLAY_MAP's 13 keys are ALL Models-side segment vocabulary",
        "Negative control absent; positive control prints real Models keys -- so the lookup census discriminates",
        "This FALSIFIED COO~Z's own prior hypothesis that moving 11 GICS sectors -> 24 industry groups would BREAK the color map: it cannot, because the map was never keyed on the ETF vocabulary at all"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "*** ANSWERED 2026-08-24T20:59Z BY 0.4.0_DE_ClientPlatform~Z WITH THE SCREENSHOT THIS ROW ASKED FOR, AND THE ANSWER IS NEITHER PREDICTION -- IT RENDERS UNDIFFERENTIATED, NOT WRONG. *** Portal vintage d43b88c5, live artifact used as the fixture (NOT fabricated): positioning_data.json 76,149 B, 114 rows, 11 distinct non-null sub_asset_class values; negative control zzz_no_such_key_9999 -> 404. LABELS ARE FINE -- every GICS name renders in full and correctly spelled, because the fallback chain ends in `return apiSubAssetClass` so the raw value survives to the page; NOTHING IS MISLABELLED. THE COLOUR CHANNEL IS DEAD -- source-confirmed at holdings-shared.tsx:99-104, getAssetClassBgColor returns SUB_ASSET_CLASS_COLORS[sub] when present ELSE ASSET_CLASS_COLORS[assetClass], so with 0/11 coverage all 110 equity rows take the SAME fill: the SUB ASSET column is one flat blue and the Portfolio Composition treemap paints every tile identically. In Models mode that colour is the DISCRIMINATING channel; in ETF mode it carries zero information. THE LOOKUP CENSUS PREDICTED BREAKAGE, THE FALLBACK CHAIN PREDICTED HARMLESSNESS, AND THE PAGE SHOWS CORRECT TEXT WITH A DEAD COLOUR DIMENSION -- which is why a grep could not have answered it. TIMING TRAP DE~Z NAMED, and it is the real lesson: TODAY the miss is UNREACHABLE (route committed-not-deployed, page shows the not-available notice, nothing renders so nothing can render wrong) -- so a verdict taken today would have read HARMLESS, AND IT WOULD HAVE BEEN HARMLESS FOR THE WRONG REASON. The fixtured read is what discriminates. BOUNDS DE~Z STATED AND I CARRY: pre-deploy read, not a live-serving observation and not to be cited as one; DIVZ/IDVZ row rendering structurally unmeasurable until F2's rows land; 1 NULL sub_asset_class row not isolated; and their own chosen positive control for the ticker parse (SPY/AGG) was ABSENT from the file so it did not fire -- they said so rather than presenting the check as clean. Alias: COO~Z's Z-S-G. FILED AS A QUESTION, NOT AS AN ASSERTED DEFECT, and the bound is the point: WHETHER IT RENDERS WRONG IS UNMEASURED -- it needs a SCREENSHOT, not a grep. A lookup-miss census answers the DATA plane; 'does the page look wrong' is the RENDER plane, and no control inside the data plane can answer it (CLAUDE.md's wrong-plane class; the /frontend-dev law says a grep cannot see contrast). Direct input to the C3 cell (INGEST-T5-2) now that Andrew ruled GICS_INDUSTRY_GROUP_NAME rendered beside HB_INDUSTRY_SECTOR_ALLOCATION on DEV. Owner on seating: DE-class (0.4.0_DE_ClientPlatform~Z, seated 20:33Z). The falsification is the valuable half -- C3 is CHEAPER than feared on the color axis, and the measurement surfaced a different, PRE-EXISTING question instead."
  },
  {
    "id": "ETFS_INGEST-Z-S13",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-08-24T20:28Z",
    "one_line": "The decomp's s5 alignment enumerated only 34 of its 36 cells, so two cells appeared in NEITHER the covered nor any uncovered list and no count in that section could ever have revealed them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Mechanical extraction over three vintages; four negative controls (T9-7/CONV-9/INV-8/T2-99) all absent, positive control T0-3 present",
        "committed 796c92888c: s5 stated denominator 26, enumerated 34, absent INGEST-T3-3 + INGEST-T6-6",
        "worktree b134d70230: s5 stated denominator 36, enumerated 34, absent INGEST-T3-3 + INGEST-T6-5",
        "certified fcdf042972 (sha 1bc5eba5def48aa6...): s5 stated 36, enumerated 36, absent NONE -- closed by the author before certification",
        "Certificate: org/tier1_exec/3.0.0_SA_CVO/deliverables/laneZ_ETFS_INGEST_STAGE3_DECOMP_CERTIFICATION_20260824.md @422bdb431b"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Raised mid-run so the author could fix it while still in the file; CLOSED at the certified vintage. THE INSTRUCTIVE MIDDLE VINTAGE: COO~Z's own 26->36 denominator correction fixed the TOTAL but SWAPPED which cell was orphaned (T6-6 -> T6-5) rather than closing the gap, because the stated total and the uncovered list were two separately-maintained hand-written facts -- the count stayed at 2 while looking repaired. A cell absent from BOTH directions is worse than an uncovered one: uncovered is a disclosed state with a reason, absent is invisible to the instrument. The two that fell out were T3-3 (the cell s4(iv) itself names as the stability defect) and the four-clocks as-of cell -- an enumeration drops its awkward members first. DURABLE REMEDY, still open and COO~Z's: DERIVE the uncovered list as ALL minus covered so the two can never disagree again; s5 already says 'RE-RUN, NEVER RE-TYPED', which is a rule needing a mechanism rather than a restatement. INERT: a mis-stated alignment misleads a reader but no scheduled act consumes it. MY OWN FIRST MEASUREMENT OF THIS WAS FALSE -- the first extractor reported 36 of 36 absent, because s5 writes ids BARE while s3 writes them PREFIXED and my pattern required the prefix, and because my negative control was INGEST-ZZ-99 which the decomp's own s4.1 quotes verbatim, so THE CONTROL FIRED POSITIVE and that is the only reason I looked. Third instance of that shape this session."
  },
  {
    "id": "ETFS_INGEST-Z-S14",
    "surfaced_by": "0.4.0_DS_ClientPlatform~Z",
    "surfaced_at": "2026-08-24T20:44Z",
    "one_line": "etf_daily_pull.py:88 does a bare unary ~ on is_cash, so the Bloomberg daily universe derivation RAISES TypeError the moment a TrueShares row with is_cash=None lands in silver/holdings -- which is exactly what INGEST-T0-3/T2-1 deliver this round.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Source verbatim at HEAD 9f03776fc5, integrations/bloomberg/pipeline/etf_daily_pull.py:88 -- `cons = sorted({str(t).strip() for t in h.loc[~h[\"is_cash\"], \"holding_ticker\"] ...})`",
        "EXERCISED at CVO~Z independently of the surfacing seat: CONTROL filepoint-only [True,False,False] dtype=bool -> NO RAISE, keeps 2 rows",
        "UNDER TEST filepoint+TrueShares [True,False,None] dtype=object -> TypeError: bad operand type for unary ~: 'NoneType'",
        "NEGATIVE CONTROL all-None -> also raises, so the discriminator is the presence of a null and not the dtype alone",
        "DS~Z's own prior reads at source: nulls SURVIVE the parquet write (_parquet_bytes casts only `inferred` at :889-890, never is_cash), so silver stores the tri-state correctly today and the defect is entirely on the CONSUMER side"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.4.0_DS_ClientPlatform~Z",
    "notes": "*** RULED 2026-08-24T20:53Z by the L1 order's issuer (1.0.0_SA_CTO~Z), AMENDMENT A5 @6e79b8d58e: A2 is AMENDED not overridden -- its discriminator refined to WHAT L1-2 CERTIFIES (the as-of computation and the landing grammar), which a null-tolerance in the universe filter touches neither. The one-expression fix is AUTHORIZED TONIGHT, owner 0.0.0_AB_MSTR~Z, and the L1-2 streak is NOT reset. DIRECTION, decided on ASYMMETRIC COST rather than taste: `mask = h['is_cash'].fillna(False).astype(bool)` -- None = declared-unknown -> NOT cash -> INCLUDED. An unknown-cash line INCLUDED costs one refdata call returning NOT_APPLICABLE, recorded in field_exceptions; an unknown-cash line EXCLUDED would drop EVERY DIVZ/IDVZ constituent (all TrueShares rows are None), so the characteristics pull would never see their holdings and the books would flip 'full' with no per-holding analytics -- A SILENT HOLE. The louder failure was chosen over the silent one. EXERCISED AT FOUR SEATS (DS~Z, COO~Z, CVO~Z, issuer) on three synthetic shapes AND at the issuer's seat on a PARQUET ROUND-TRIP of the mixed shape -- the column returns object dtype with None (the exact on-disk shape), the old expression RAISES, the fixed one reads ['AAPL','BP','SALXX']. DISARM SEQUENCE (MSTR~Z's, gated on tonight's fire): exercise the fixed expression against the REAL silver partition first, then save (runner tree IS production -- save is the deploy, no apply step and no review window), one expression only, nothing adjacent; tomorrow's 07:00 log is the EXERCISED evidence and a 61 after the fix is a NEW finding, not this one recurring. *** BOUNDED 2026-08-24T20:52Z -- IT FAILS LOUD, NOT SILENT, AND THE LOSS IS SMALLER THAN THE PHRASE IN THE AIR TONIGHT. VERIFIED AT THIS SEAT AT SOURCE (HEAD 6e79b8d58e): etf_daily_pull.py:93-96 wraps the derivation in `except Exception as e: log('ERROR deriving universe: ...'); traceback.print_exc(); return 61` -- a caught, logged, traceback'd, NAMED DISJOINT exit code meaning 'universe could not be derived, NOTHING WRITTEN'. That is the design working, not silent corruption. COO~Z censused the blast radius rather than assuming: EXACTLY ONE SITE (:88); nothing else in integrations/bloomberg/pipeline/, data/etfs/scripts/ or data/assets/scripts/ applies a bare unary `~` to is_cash. THE CONSTITUENTS LEG IS SAFE (filters on fund_ticker, never touches is_cash, runs on its own RC_CONS) -- which matters because the CURRENT-DAY-ONLY, permanently-lost class is the Bloomberg DERIVED layer and that rides the constituents leg. THE GOLD PRODUCER ALREADY HANDLES None CORRECTLY, verified at source: etf_positioning_gold.py `infer_is_cash()` -- `if is_cash is not None and not (isinstance(is_cash, float) and pd.isna(is_cash)): return bool(is_cash), False`, docstring 'Silver's assertion wins whenever it made one'. DS~Z's TO-1 work anticipated this case. SO THE COST OF exit 61 IS: (a) L1-2's scheduled-fire streak resets from 1/3, and (b) one day of characteristics / history_topup / fund_daily. 0.0.0_AB_MSTR~Z then MEASURED the re-pullability half COO~Z had marked INFERRED, and NARROWED it rather than confirming it whole: history_topup and fund_daily are SELF-HEALING BY CONSTRUCTION (a run exiting 61 writes NO manifest, so the next run reads the last SUCCESSFUL manifest and re-pulls the whole gap) -- but `characteristics` is a reference_data CURRENT SNAPSHOT and a missed day is a missed snapshot, rescued only by OVERLAP (its fast-moving member TOTAL_NUMBER_OF_HOLDINGS_IN_PORT is captured independently by the safe constituents leg; the remainder is slow-moving). \u26d4 RECORDED BECAUSE OVER-ROTATING IS ITS OWN FAILURE MODE: this is NOT the capture-forward class, and a row that let 'unrecoverable day' attach to it would manufacture pressure on a mechanism that fails loud by design. Coordinate allocated by the channel owner: the surfacing seat proposed S8 as high-water, which was correct when they measured and is superseded by the 20:45Z append -- S13 is high-water, so this is S14. BLOCKING class because it constrains which CONV-1 representations are ADMISSIBLE, not because it stops work today. ARMED with a trigger inside this round: the first TrueShares row to reach silver/holdings. DISARM (theirs, taken same-turn): CONV-1 rules a null-bearing representation inadmissible to a bare unary `~`, naming etf_daily_pull.py:88 as a consumer that must be adapted BEFORE T2-1 lands. DISARMED != REMEDIATED -- the consumer edit is NOT DS~Z's lane (integrations/bloomberg/pipeline/), so remediation carries its own owner and clock. \u26d4 THE PART WORTH KEEPING, and it is the surfacing seat's own self-correction: they were wrong TWICE on the way here and BOTH wrong versions were more alarming AND more plausible than the truth -- first that None COERCES to False at write (silent tri-state destruction; FALSE, nulls survive), then, having written the consumer check as their own PARAPHRASE `~h['is_cash'].astype(bool)`, that it silently keeps cash rows. I re-ran the paraphrase: it DOES fail silent (keeps the None row) while THE REAL LINE RAISES. Had the paraphrase shipped they would have filed silent data corruption against a fail-loud mechanism. RUN THE REAL ARGV -- CLAUDE.md's own oracle rule firing on the seat that quoted it. VERIFIED AT THIS SEAT: source line read at a named vintage, and all three exercise arms re-run independently; DS~Z notes their cusip three-population reproduction of Z-S3 is same-plane corroboration rather than independent confirmation, which is the right distinction and is why the exercise above was run fresh rather than accepted."
  },
  {
    "id": "ETFS_INGEST-Z-S15",
    "surfaced_by": "0.4.0_DE_ClientPlatform~Z",
    "surfaced_at": "2026-08-24T20:59Z",
    "one_line": "C3's ruled vocabulary (GICS_INDUSTRY_GROUP_NAME, 24 values) misses the same three portal lookup tables the current 11 sector names miss, so a T5-1 build that only swaps the FIELD inherits the dead colour channel at FINER grain -- 24 undifferentiated values instead of 11, strictly worse.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Predicted by 0.4.0_DE_ClientPlatform~Z from the Z-S12 render; MEASURED at CVO~Z rather than carried as their inference",
        "Portal vintage d43b88c5. All 24 GICS level-2 industry-group names tested against each table: SUB_ASSET_CLASS_COLORS (Attribution/constants/holdings-shared.tsx) covers 0 of 24; SUB_ASSET_COLORS (lib/chartColors.ts) 0 of 24; SUB_ASSET_CLASS_DISPLAY_MAP (Positioning/tabs/HoldingsTab.tsx) 0 of 24",
        "POSITIVE CONTROL: 'US Large Cap' IS present in SUB_ASSET_COLORS (True) -- the search can find a value that is really there",
        "NEGATIVE CONTROL: a bogus label -> False",
        "SANITY: the CURRENT 11 sector names also miss ('Information Technology' -> False), reproducing Z-S12's 0/11 on the same instrument",
        "Mechanism unchanged from Z-S12: getAssetClassBgColor (holdings-shared.tsx:99-104) falls back to ASSET_CLASS_COLORS[assetClass] on a miss, so every row takes one fill"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "2.0.0_SA_COO~Z",
    "notes": "THE FINER AXIS MAKES IT WORSE, NOT BETTER: the finer the vocabulary the more information the colour channel was carrying, so swapping 11 -> 24 without a colour act converts a dead channel into a more conspicuously dead one. T5-1 IS THEREFORE TWO ACTS, NOT ONE -- the field swap AND a colour/vocabulary act for the new values; the second is a Rule 24 authoring event (per the 2026-08-20 widening, PROPOSING values to an existing axis is itself an authoring act requiring the four-postulate test plus a token-hygiene census). ARMED because the trigger is an ordinary in-round act: COO~Z cutting T5-1 as a single field swap, which is the natural reading of C3's ruling. *** DISARMED AT ISSUANCE 2026-08-24T21:04Z by 2.0.0_SA_COO~Z: TO-5 (@efa80f37a4, ETFS_INGEST.TO-5, cells T5-1 + T5-2) was AMENDED BEFORE THE GO and this consequence is now AC6 -- so the TO reached the executing seat already carrying the second act, and the hazard never had a chance to fire. That is the escape valve working at its cheapest possible moment: surfaced, measured, and folded into the spec before the seat read it. *** DISARM was: scope the TO's second half deliberately at cutting time. DE~Z explicitly did NOT mint the vocabulary and named it instead, which is the correct refusal. NOT A CHALLENGE TO C3 -- Andrew ruled GICS_INDUSTRY_GROUP_NAME and that ruling stands; this says the cell has a second half, nothing more. DE~Z's prediction is carried as MEASURED rather than inferred because I re-derived it at this seat with a firing positive control; an unmeasured 'it will also miss' would not have graduated."
  },
  {
    "id": "ETFS_INGEST-Z-S16",
    "surfaced_by": "0.4.0_DS_ClientPlatform~Z",
    "surfaced_at": "2026-08-24T21:28Z",
    "one_line": "The two issuers reach the unified row's `date`/`data_as_of` by DIFFERENT KINDS of source -- filepoint from the HOLDINGS FILE's own date, TrueShares from the NET-ASSETS PAGE as-of -- with no marker distinguishing them, and TrueShares' own sheet Date is DROPPED so those rows' true holdings as-of is discarded rather than merely unused.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Surfaced by DS~Z at TO-2; VERIFIED AT SOURCE at CVO~Z, vintage 80c36267a1, not taken from the report",
        "filepoint: lambda_function.py:612 `holdings_date = _norm_date(fund_rows[0].get(\"Date\"))` -- a HOLDINGS-FILE date -- feeding :665 `\"net_assets_as_of\": holdings_date`",
        "trueshares: :526 `\"net_assets_as_of\": _ts_asof_after(html, \">Net Assets<\")` -- a NET-ASSETS PAGE as-of, a different kind of thing entirely",
        "Both land in the SAME field name, then :838 `\"data_as_of\": rec.get(\"net_assets_as_of\")` and :902 `\"date\": h[\"data_as_of\"]` -- so one column carries both, distinguished nowhere",
        "TrueShares' own sheet `Date` appears at no consuming call site (the only `Date` consumption found is filepoint's :648 `nav_row.get(\"Rate Date\")`), confirming DS~Z's DROPPED finding"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.4.0_DS_ClientPlatform~Z",
    "notes": "Rule 24(ii) SAME GRAIN failing INSIDE one column -- the axis is 'as-of', and two values on it are measured from different things. \u26d4 IT ARMS TONIGHT: invisible until now ONLY because DIVZ/IDVZ carry zero holdings rows, and the 22:00Z fire lands the first TrueShares rows. Any consumer reading the column uniformly is then wrong for half the rows -- and INGEST-T3-3's tie-out is specified as a SAME-DAY compare of the Bloomberg count against 'that day's issuer row count', which is precisely the comparison a cross-issuer as-of mismatch corrupts. DISARM is a DECLARATION, not a code change, because the rows land regardless: the difference must be declared (DS~Z's proposed `as_of_basis`) before any consumer treats the column as a uniform holdings as-of. The two remedies COMPOSE and DS~Z checked that rather than assuming it -- `as_of_basis` makes the difference declared, and T2-3's superset row restores the discarded value as a vendor-verbatim column, which is Rule 17's no-slimming doing real work rather than being cited. \u26d4 WHY THIS ITEM EXISTS AT ALL: it is a surface the CERTIFIED decomp's cells did not name. It is NOT decomp-invalidating -- the cells that must carry it (CONV/T2-3/T2-4) all exist and the remedy lands inside them -- but it is a live instance of the cert's own stated limitation: REDUCED COHORT, one perspective, nobody having independently re-enumerated the operative surfaces. An executing seat found at pickup what the enumeration did not, which is the pipeline working, and is also exactly why that limitation was written on the certificate's face rather than buried."
  },
  {
    "id": "ETFS_INGEST-Z-S17",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-08-24T21:32Z",
    "one_line": "comp-closure -- the estate's designated Rule-22a code-layer instrument -- compares package members by RAW sha256 with no line-ending normalization, so it inherits Z-S4 by construction and would report a correct deploy as non-identical.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Surfaced by CTO~Z after CORRECTING what COO~Z routed (the claim 'no comp-tool does this' is FALSE -- comp-closure's declared job IS build-input -> package -> deployed bytes -> repo bytes); VERIFIED AT SOURCE at CVO~Z",
        "org/modules/graph/comp_closure.py:94-95 `def _sha256(b: bytes) -> str: return hashlib.sha256(b).hexdigest()` -- RAW BYTES; a difflib.SequenceMatcher ratio fallback is the only other comparison",
        "Normalization census on that file, read via python to avoid shell-escaping ambiguity: literal backslash-r = 0, literal backslash-r-backslash-n = 0, actual CR bytes = 0, 'crlf' 0, 'CRLF' 0, 'normaliz' 0, 'splitlines' 0, 'universal' 0",
        "POSITIVE CONTROLS proving the search reaches the comparison code: sha256 = 58, equivalence = 22, eq_head = 6, SequenceMatcher = 1. NEGATIVE CONTROL zzz_no_such_tok = 0",
        "DEMONSTRATED, not theorised: this seat's own 6-commit scan of the pre-deploy artifact returned RAW 0 matches / CRLF-NORMALIZED exactly 1 (541a393798) -- so a raw member compare against the TRUE build commit returns non-identical on a correctly-deployed function"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "*** NOT ROUND-GATING FOR D4 -- ANDREW-DIRECT ~21:4xZ, VERBATIM: \"I dont want to see comp-closure on the directives item until i smoke it and its definitively done\" (relayed 0.0.0_AB_MSTR~Z msg 5154). This row STAYS RECORDED -- it is a grounded finding and deleting it would destroy evidence -- but it does NOT gate D4 round closure, does NOT appear in round-closure criteria, and its remediation does NOT seed this project's next-round TO inputs. Mechanism chosen by the channel owner (MSTR~Z carried his word and explicitly did not prescribe one): a SCOPE ANNOTATION rather than a delete or a re-file, because the finding is real and its evidence is this project's, while its DISPOSITION is his instrument's and his to make. It travels on the TOOLING route to base CTO, off-directive. *** \u26d4 THE INSTRUMENT FOR THE RUNG THIS PROJECT'S ENTIRE FIRST ACT TURNED ON. Its verdict vocabulary includes DIVERGENT, which is precisely the word that would have been believed. \u26d4 AND THE SHARPENING THIS SEAT ADDS: ON THIS FUNCTION THE DEFECT WAS MASKED BY THE OTHER BLIND SPOT. comp-closure DID compute the raw member comparison -- the bundle I read tonight carries `eq_deployed_commit: false` and `eq_head: false` for lambda_function.py -- but the closure verdict short-circuited to equivalence=UNMEASURED because landing_guard.py has three plausible homes (Z-S6). So the multi-home REFUSAL, which is correct behaviour, HID the line-ending DEFECT, which is not. Two blind spots interacting such that the honest one conceals the broken one is worth more than either alone: had landing_guard.py had a single home, the tool would have promoted a raw non-match to a DIVERGENT closure verdict on a correct deploy. ROUTING: this is a comp-tool COVERAGE DEFECT (Rule 22: 'the comp-tooling is not additive, it is foundational -- a comp-tool coverage gap is a DEFECT, not an inconvenience'), owned by the NFRA/tooling lane (0.8.0_AE_CloudComp class, LAPTOP) -- NOT D4 and NOT site-Z work this session; MSTR~Z carries it to base CTO on the bridge alongside the Rule 17b amendment. Recorded here because the channel is the universal record and because this project's evidence is what makes the case. The fix named at surfacing: normalize per member before the equality verdict AND SAY IN THE OUTPUT which comparison was used -- the second half matters as much as the first, since a silently-normalized compare would hide a REAL line-ending divergence. \u26d4 MY OWN INSTRUMENT FAILED WHILE VERIFYING THIS, in the opposite direction to every prior instance tonight: a shell-escaped grep for the backslash-r-backslash-n pattern returned 64 hits, which contradicted the surfacing seat's stated zero. Inspecting the hits showed they were arbitrary lines (`_HERE = os.path...`, `time.strftime`) -- the pattern had degenerated. A FALSE POSITIVE this time, where the CRLF scan, the alignment extractor and the JSON splice were all false zeros or corruptions. Re-asked through python with no shell escaping and the surfacing seat's figure was right. Fourth instance of the class in one session; the count is the point, not any single one."
  },
  {
    "id": "ETFS_INGEST-Z-S18",
    "surfaced_by": "0.7.0_AE_CloudOps~Z",
    "surfaced_at": "2026-08-24T21:33Z",
    "one_line": "proof-of-spec-check returns VALID on an instance whose EXERCISED-class criterion never ran -- it certifies SHAPE and COVERAGE and structurally cannot certify that the WORK HAPPENED, so a complete flip rides a VALID instance either way.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Surfaced by AE~Z from staging their own TO-1 instance early while waiting on the fire; accepted and routed by CTO~Z (5092)",
        "VERIFIED AT SOURCE at CVO~Z, .tools/proof-of-spec-check.py:35-36: `if row.get('status') != 'PASS' and not row.get('status_reason')` -- a non-PASS status is a violation ONLY IF it lacks a reason, so `status: UNCOMPUTABLE` WITH prose passes cleanly",
        ":37-38 requires substantive output_evidence for PASS rows (>= 8 chars, 'a bare value; INVALID') -- so the tool is strict about evidence on rows that CLAIM a pass and silent about rows that decline to",
        "No check anywhere in the file asserts that an EXERCISED-class criterion produced a measurement; exit 0 = VALID is computed purely from the violations list (:176-177)",
        "AE~Z's second half: a malformed controls block CRASHES the checker rather than printing a violation"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "notes": "\u26d4 THE SAME FAMILY AS THIS ROUND'S F2 -- A CONFIG READ PASSING FOR A BEHAVIOUR READ -- ONE LAYER UP, IN THE GATE THAT GUARDS EVERY TO THE FABRIC ISSUES. The vocabulary is NOT the defect and CTO~Z was right to say so: UNCOMPUTABLE / UNVERIFIABLE-BY-INSTRUMENT / N/A-BY-CONSTRUCTION are real outcomes and a gate refusing them would force seats to lie. The defect is that NOTHING DOWNSTREAM DISTINGUISHES A MEASURED CLOSE FROM A DECLARED-UNMEASURABLE ONE. Note the asymmetry at :37-38 vs :35-36: the tool is STRICT about evidence on a row that claims PASS and SILENT about a row that declines to claim one -- so the cheapest way past the gate is to not claim. INERT tonight, and only because CTO~Z's ruling covers this round by hand: an UNCOMPUTABLE on an EXERCISED-class criterion is NOT a close; TO-1 does not reach `complete` on a VALID instance whose AC4 is a placeholder. *** THIS SEAT ADOPTS THE SAME BAR AT CERTIFICATION, and it is the channel owner's to hold: a ROUND DOES NOT CLOSE on instances whose exercised criteria are declared unmeasurable while the thing that would measure them is scheduled and pending. Round v1 therefore cannot close on tonight's TOs until the 22:00Z fire is READ. *** AE~Z's second half (a malformed controls block CRASHES rather than printing a violation) fails in the direction where the operator retries with the block REMOVED -- a gate that dies on bad input teaches deletion. ROUTING: NFRA/tooling lane, LAPTOP, carried to base CTO by MSTR~Z on the same bridge as Z-S17; NOT D4 work and not a build anyone here is starting. AE~Z found this by staging the instance EARLY rather than waiting idle for the fire -- the right use of a wait, and the reason it was found before it mattered rather than after."
  },
  {
    "id": "ETFS_INGEST-Z-S19",
    "surfaced_by": "0.4.0_DS_ClientPlatform~Z",
    "surfaced_at": "2026-08-24T21:40Z",
    "one_line": "ETFS_POSITIONING.TO-5's invocation contract is stale in three places after TO-3's C2 re-point, and the two errors CANCEL: the ENV override silently re-points the producer back to the OLD home, which is exactly where the stale IAM grants access -- so a fully-applied contract runs GREEN while Andrew's C2 ruling silently does not happen.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Surfaced by DS~Z same-turn, AHEAD of their own commit; VERIFIED AT SOURCE at CVO~Z, vintage dea23978a7",
        "TO-3's re-point landed in the CODE DEFAULTS: etf_positioning_gold.py:98-99 `GOLD_BUCKET = os.environ.get(\"ETFS_GOLD_BUCKET\", \"opal-data-etfs\")` / `GOLD_ROOT = os.environ.get(\"ETFS_GOLD_ROOT\", \"gold\")`; publisher identical at :62-63",
        "os.environ.get(NAME, default) RETURNS THE ENV VALUE WHEN SET -- so the contract's s.7 ENV (ETFS_GOLD_BUCKET=opal-data-assets, ETFS_GOLD_ROOT=portal/gold/etfs/positioning) OVERRIDES the new defaults and re-points to the OLD home. The env is an override by construction.",
        "The contract's s.8 IAM grants are scoped to opal-data-assets/portal/gold/etfs/positioning/* 'this prefix only' -- stale against a producer that now PUTs to opal-data-etfs/gold/*",
        "THE WRITE-BOUNDARY GUARD DOES NOT CATCH IT: _assert_write_boundary at :180-183 tests `full.startswith(GOLD_BUCKET + '/' + GOLD_ROOT)` -- keyed to the CONFIGURED values, so under the env override it validates the WRONG target happily"
      ]
    },
    "disposition": "GRADUATED",
    "disarm_owner": "0.4.0_DS_ClientPlatform~Z",
    "notes": "\u26d4 WHY BLOCKING RATHER THAN OBSERVATION, AND IT IS THE WHOLE POINT: THE TWO ERRORS CANCEL. The ENV error fails SILENT (re-points to the old home); the IAM error fails LOUD (AccessDenied on the new home). Applied TOGETHER the env sends the producer exactly where the stale grants permit, so NOTHING RAISES -- pipeline green, artifacts land, publisher serves, every instrument healthy, and C2 SILENTLY DID NOT HAPPEN. **A HALF-APPLIED CONTRACT WOULD HAVE FAILED VISIBLY; THE FULLY-APPLIED ONE FAILS INVISIBLY.** The loud failure was the only thing that would have told anyone and the silent one disarms it. This is F2's exact class -- applied-env disagreeing with running code, the reason this project has a first act at all -- arriving from the DEPLOY side instead of the code side, which is why nobody was watching for it there. TRIGGER: TO-5's apply, QUEUED and pickable. DISARM (theirs, taken this turn): routing it to the executing seat BEFORE the apply, which is the only act that can disarm a hazard whose trigger is another seat's next step -- and they did it ahead of their own commit. \u26d4 REMEDIATION IS NOT TAKEN AND THAT IS CORRECT: the contract edit is IN DS~Z's lane (their deliverable) but the spec is FROZEN mid-round and TO-3's scope is the SCRIPTS half, two .py files. Editing a cross-TO contract that drives ANOTHER seat's apply is scope widening, so they ROUTED IT AND REQUESTED AUTHORIZATION rather than taking it. That is stage-4 discipline working exactly as written -- the executing seat's only legal off-spec write is a surprise item. AUTHORIZATION IS 2.0.0_SA_COO~Z's (TO-set owner), with CTO~Z holding the C2 ruling; NOT the channel owner's -- I allocate the coordinate and record, I do not authorize scope. Stated because a BLOCKING row whose actuator is ambiguous reads open and is shut."
  },
  {
    "id": "ETFS_INGEST-Z-S20",
    "surfaced_by": "0.4.0_DE_ClientPlatform~Z",
    "surfaced_at": "2026-08-24T21:43Z",
    "one_line": "CORRECTION TO ETFS_INGEST-Z-S5 AND ETFS_INGEST-Z-S14: the characteristics/constituents overlap that both rows carry as the reason a missed L1 day is survivable is ONE field, not two -- FUND_PCT_TOP_TEN_HOLD is SOLE-SOURCED to the constituents leg, so for that member the dependency runs the OTHER WAY and a constituents failure loses it outright.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Surfaced by DE~Z at ETFS_INGEST.TO-5's AC5; RE-DERIVED at CVO~Z on the same landed 2026-08-21 artifacts",
        "TOTAL_NUMBER_OF_HOLDINGS_IN_PORT: present in characteristics.csv AND in constituents/derived_summary.csv -> a REAL overlap",
        "FUND_PCT_TOP_TEN_HOLD: ABSENT from characteristics.csv, present in derived_summary.csv -> SOLE-SOURCED to the constituents leg",
        "derived_summary.csv header (5 cols): fund_ticker,as_of_source,name,total_number_of_holdings_in_port,fund_pct_top_ten_hold",
        "\u26d4 MY FIRST PASS WAS WRONG AND THE ERROR IS RULE 21's NAMED ONE: I censused with UPPERCASE field names while derived_summary's header is LOWERCASE, so both fields read ABSENT from it -- a confident, well-formed FALSE that would have made the sole-sourcing look like a total absence. Re-run case-insensitively; DE~Z's figures then reproduce exactly."
      ]
    },
    "disposition": "GRADUATED",
    "notes": "APPEND-ONLY CORRECTION, per the protocol: a correction is a NEW item citing the prior ids, never an edit in place. Z-S5 and Z-S14 both carry the sentence that `characteristics` survives a missed day via OVERLAP with the constituents leg, sourced from MSTR~Z's measurement and repeated by this seat in two rows. THAT SENTENCE IS HALF TRUE. \u26d4 AND THE DIRECTION OF THE ERROR IS THE POINT, in DE~Z's words: a premise offered as REASSURANCE -- 'a missed L1 day is survivable' -- is, for half its members, THE OPPOSITE. FUND_PCT_TOP_TEN_HOLD has no characteristics copy to fall back on, so a constituents-leg failure loses it outright, which INVERTS the comfort Z-S5's disarm rests on. Z-S5's disarm (MSTR~Z's post-fire READ + same-day recovery run) is UNCHANGED and still correct -- it is the RATIONALE that narrows, not the remedy. Recorded because a reassuring premise that nobody re-measures is exactly how a real exposure stays invisible, and because I PROPAGATED it into two rows on a relay rather than measuring it myself. The relayer's obligation is to forward the grounding or forward the caveat; I forwarded neither and restated it as settled."
  },
  {
    "id": "ETFS_INGEST-Z-S21",
    "surfaced_by": "0.4.0_DS_ClientPlatform~Z",
    "surfaced_at": "2026-08-24T21:52Z",
    "one_line": "The gold producer's write-boundary guard used startswith() WITHOUT a trailing separator, so it admitted any prefix-string SIBLING of the declared root -- a boundary check that reads as exact and was not. PRE-EXISTING, not introduced by the C2 re-point; now fixed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Surfaced by DS~Z at TO-3; the PRE-EXISTING attribution is 2.0.0_SA_COO~Z's correction, re-derived by them on the OLD long root",
        "EXERCISED AT CVO~Z on both forms: OLD `full.startswith(B+'/'+R)` permits opal-data-etfs/gold_backup/x.parquet = True and opal-data-etfs/goldenrod/x.parquet = True; NEW `...+'/'` refuses both = False",
        "Both forms correctly permit the legit target (opal-data-etfs/gold/book/date=.../book.parquet) and correctly refuse the other bucket -- so the fix narrows only the sibling case",
        "COO~Z's control on the OLD value: opal-data-assets/portal/gold/etfs/positioning_backup/x.parquet was ALSO permitted -- so the separator was missing all along",
        "Fix landed at 14b67e4cf3 with the mechanism in a code comment; the guard now reads `if not full.startswith(GOLD_BUCKET + '/' + GOLD_ROOT + '/')`"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "CLOSED -- the separator is landed and exercised six ways in TO-3's AC3 battery, both limbs, refusals distinguishable. Filed INERT because nothing remains to disarm; had it been caught BEFORE the fix it would have been ARMED, since the C2 re-point made it reachable. \u26d4 WHAT THE RE-POINT ACTUALLY CHANGED WAS REACHABILITY, NOT THE FLAW: a SHORT GENERIC root (`gold`) has plausible siblings (`gold_backup`, `gold-tmp`, `goldarchive`) where a LONG SPECIFIC one (`portal/gold/etfs/positioning`) did not. The defect was equally present before and effectively unreachable. \u26d4\u26d4 THE METHOD LESSON IS THE PART WORTH KEEPING, AND IT IS DS~Z's OWN AGAINST THEMSELVES: they reported 'MY re-point SHRANK the guard's margin / I introduced it' -- A HYPOTHESIS ABOUT THEIR OWN CHANGE THAT THEY TESTED ONLY ON THE NEW VALUE. COO~Z ran the one control that could separate the two readings -- the OLD value -- and it came back PERMITTED. **When attributing a defect to a change, exercise the PRE-CHANGE state; it costs one line and it is the only thing that distinguishes 'I broke this' from 'this was already broken'.** Both directions of that error are costly: claiming authorship of a pre-existing flaw misdirects the fix's scope, and the opposite mistake hides a real regression. DS~Z adopted the correction into the code comment, the proof-of-spec and the commit message in COO~Z's framing rather than their own. SEPARATELY DISCLOSED BY DS~Z AND RECORDED HERE BECAUSE IT IS DURABLE HISTORY: the authorization to land the separator IN THE SAME COMMIT as the re-point arrived after 8bf8b39131 was already committed, so the widened state exists at exactly one commit, now on the remote, closed at 14b67e4cf3. They did NOT amend -- an amend was available and would have erased the very sequence the disclosure exists to record. Reporting the compliance they did not have, rather than the one they were asked for."
  }
]
```

---

## 4. DENOMINATORS FOR THIS DOCUMENT

- Items: **21** (1 dismissed, 3 under investigation, 17 graduated). ARMED: **11** (Z-S1, Z-S4, Z-S5,
  Z-S7, Z-S8, Z-S10, Z-S14, Z-S15, Z-S16, Z-S17) -- each with a named disarm owner, per the schema's conditional rule.
  Class split: 13 OBSERVATION + 1 BLOCKING (Z-S14, the first BLOCKING item this round).
  **These figures are the validator's output, not a hand count** -- see the note below.
  *(At the 8-item version this line read "ARMED: 4" and omitted Z-S8 until the validator's own count
  contradicted it. Recorded rather than silently fixed: a hand-written denominator beside a
  machine-countable one is the exact defect this document polices in others, and it survived my own
  proofread. It is also, precisely, the defect I then found in the decomp's §5 -- Z-S13 -- which is
  why that item is filed without any suggestion that I was immune to it.)*
- Re-derived rather than inherited: **F2 in full** (comp-closure self-test 24/24 + independent package download + token census with a negative control), **Z-S3's identifier populations** (114/114 rows read at source), **the D4 member census** (9 directive rows, positive and negative controls).
- Inherited with attribution, NOT re-measured by this seat: Z-S2's bronze-HTML regex figures (author's own retraction @7ea7d45723), Z-S5's DAPI-shared-port and 6h-stability measurements (MSTR~Z, with their two UNMEASURED bounds carried forward as stated).
- Non-findings recorded so they are not re-filed: the `opal-data-etfs/bbg/` partition gap (weekend + T-1, NEVER#1 discharged before reading).

## 5. WHAT THIS DOCUMENT DOES NOT DO

It does not certify COO~Z's stage-3 decomp -- that is a separate act by this seat against the
four-postulate record, the bidirectional cell<->criterion alignment with printed denominators, and
whether each cell's premise oracle actually RAN rather than was written. The decomp carries
UNCERTIFIED on its face until that cert lands. It does not rule any of the s.5 row conventions
(decomp cells), does not move any tension's decider, and cuts no TO.

-- `3.0.0_SA_CVO~Z`, channel owner and certifier of record, 2026-08-24
