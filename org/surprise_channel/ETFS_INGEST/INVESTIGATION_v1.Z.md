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
  "notes": "*** ATTRIBUTION CLOSED AT THE INVOCATION PLANE 2026-08-24T22:09Z BY 0.7.0_AE_CloudOps~Z, COMPLETING WHAT THIS SEAT COULD NOT: I closed this row on the deployed BYTES and stated plainly that I had NOT read the invocation record, so my scheduled-fire attribution was strong TIMING evidence rather than proof. AE~Z read it: CloudWatch stream 2026/08/24/[LATEST]25ae2df9e, RequestId 5ec70c09-1b87-4cb7-971c-6ae755ad2715, firstEvent 22:00:08.209Z (8s after cron), 7800.26 ms. The pre-fire baseline was taken TWICE INDEPENDENTLY -- theirs 20:55:24Z, mine 21:13:47Z -- and BOTH recorded NO 2026/08/24 stream, so this is the only one. NO AD-HOC INVOKE WAS FIRED BY ANYONE: permitted by the TO and DECLINED DELIBERATELY, because an ad-hoc artifact is byte-identical downstream and firing one destroys the ability to say which run produced this. The log carries lines the OLD BYTES COULD NOT EMIT UNDER ANY INPUT ('OK: [divz] trueshares holdings captured: 29 row(s)'), because the call site did not exist in them -- an emitted-marker discriminator, not an inference from a difference. Bronze objects landed INSIDE the invocation window 22:00:08.209 -> 22:00:12.027Z, tying the objects to THIS run rather than to any run. *** AND THEY RAN A CONTROL I DID NOT: PFDE 90 -> 90 and PFOE 24 -> 24, UNCHANGED. I measured what CHANGED; they measured WHAT SHOULD NOT HAVE. That is the load-bearing half -- it verifies the 'second source into an existing shape' claim rather than asserting it, i.e. that adding TrueShares did not disturb the product already working for the other two funds. Re-checked against my own figures: PFDE 90 + PFOE 24 = 114, exactly the baseline partition; 114 + 73 = 187 = the landed row count. Reconciles with no loss. My own banked lesson is to test the direction that ADDS rows; the inverse -- test the direction that should NOT move -- is the one I skipped, and a regression there would have been invisible in everything I measured. *** *** CLOSED 2026-08-24T20:43Z: DISARMED + REMEDIATED in one act -- the deploy is both. VERIFIED AT THIS SEAT ON THE DEPLOYED BYTES, not taken from the deploy report and not from the commit message: live CodeSha256 BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=, LastModified 2026-08-24T20:31:09Z; fresh Code.Location download censused -- fetch_trueshares_holdings 3, TS_HOLDINGS_ENABLED 6, positive control fetch_filepoint 4, negative control ZZZ_NO_SUCH_TOKEN_9999 = 0; CALL SITE present (items = fetch_trueshares_holdings(...)) and the SKIP branch present, both of which the old bytes lacked. This is the fourth independent verification (AE~Z, MSTR~Z, CTO~Z's RAVC read, mine) and it is at the CODE layer per Rule 22a -- the fire at 22:00Z tonight is the EXERCISED layer and is not yet evidence. *** Standing moved INERT -> ARMED by the channel owner on the axis as ruled; accepted by the surfacing seat (CTO~Z msg 4849). See s.2. Disarm = the TF-only deploy of @4e5800fde0 under COO~Z's TO + GO (TO cut ~20:18Z); the deploy is BOTH the disarm and the remediation, so this row closes DISARMED + REMEDIATED in one act -- which is the exception, not the pattern. Lost-day count rests on the code alone: tonight's 22:00Z is the 5th. Andrew's C4 ruling ('all recs approved, proceed', ~20:0xZ) makes the Lambda the vehicle, so the disarm path is unconditional."
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
    "other/unclassified: 2 -- the literal 'Cash&Other'",
    "EXTENSION 2026-08-24T22:33Z: bronze divz_holdings.csv carries ('RTX','7.55E+105') VERBATIM -- the scientific-notation corruption is ISSUER-SIDE, not ours; IDVZ bronze carries none; 7 of 73 trueshares silver rows carry a sub-9-char cusip",
    "CONSOLIDATION 2026-08-24T23:14Z: intersection of bbgid-cusip / non-alpha-ticker / price==0 / weight==0 over 8,079 rows / 73 partitions = {2602335D} (DS~Z); per-partition figures on 2026-08-24 are 1/1/1 (CVO~Z) -- history-wide and per-partition are different domains and a per-partition check baselines at 1",
    "THIRD AXIS 2026-08-24T23:23Z (DE~Z named, CVO~Z verified): silver 08-21 = 114 rows (PFDE 90 + PFOE 24) is a strict subset of silver 08-24 = 187 by (fund,ticker) key, |08-21 minus 08-24| = 0; platinum's corpus is the 08-21 one until gold converges at 13:00Z tomorrow"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "*** THIRD DENOMINATOR AXIS, named by 0.4.0_DE_ClientPlatform~Z against their own figure and VERIFIED HERE: THEIR '1 of 114' AND MY '1 of 187' ARE DIFFERENT TIERS AND DIFFERENT AS-OFS. Theirs is PLATINUM, the served artifact, from gold's T-1 = Friday 2026-08-21; mine is SILVER, tonight's 2026-08-24 partition. MEASURED: silver 08-21 = 114 rows (PFDE 90 + PFOE 24); silver 08-24 = 187 (the same 114 plus DIVZ 29 + IDVZ 44). The strict-subset claim HOLDS EXACTLY on (fund, ticker) keys -- |08-21 minus 08-24| = 0 -- though it is a subset of the KEY SET and not of the row VALUES, since the date fields differ. TPG is in both, which is why the counts agree. \u26d4 TOMORROW AT 13:00Z THEY CONVERGE: gold selects T-1 = Monday 08-24 and the PLATINUM corpus goes 114 -> ~187 rows, SO THEIR DENOMINATOR CHANGES FOR A REASON THAT IS NOT A DEFECT, and an unmapped count read against 114 tomorrow would be read against the wrong base. A PER-PARTITION BASELINE NEEDS ITS TIER NAMED AS WELL AS ITS DATE: '1 of 114 at platinum/T-1=Friday' and '1 of 187 at silver/08-24' are both true tonight and only one survives tomorrow. *** THE LINE WORTH KEEPING, and it is theirs: 'AGREEMENT BETWEEN TWO MEASUREMENTS OF DIFFERENT POPULATIONS IS NOT CORROBORATION.' All three seats were right and the numbers agreed, WHICH IS EXACTLY WHY NOBODY WOULD HAVE CHECKED WHETHER THE CORPORA MATCHED -- the same wrong-plane shape this round keeps hitting, arriving disguised as consensus. Third denominator-domain finding in one hour (history-wide vs per-partition; then tier and as-of), and this one had no disagreement to alert anyone. *** *** CONSOLIDATED 2026-08-24T23:14Z: TPG IS ONE UPSTREAM CAUSE WITH FOUR SYMPTOMS, NOT FOUR DEFECTS. 0.4.0_DE_ClientPlatform~Z isolated it and 0.4.0_DS_ClientPlatform~Z corroborated from the CONV-2 plane over 8,079 rows / 73 partitions (token-walked): bbgid-shaped cusip 73, non-alpha ticker 73, price==0 74, weight==0 103, INTERSECTION OF ALL FOUR = {2602335D}. The row: PFDE \u00b7 2602335D \u00b7 BBG01Y2F01K3 \u00b7 'TPG Inc' \u00b7 shares 12,251 \u00b7 price 0.0 \u00b7 weight 0.0 \u00b7 id_kind bbgid. A security the vendor could not resolve -- no usable ticker, a fallback BBGID in the identifier field, no price, therefore no weight. PRESENT IN 73 OF 73 PARTITIONS, so a STANDING CONDITION, not a new arrival. Three seats held three items on it. *** \u26d4 AND A BASELINE CORRECTION THAT IS MINE, BECAUSE I NEARLY INVERTED IT: DS~Z's differing per-symptom baselines (unpriced 2 tickers, weight-zero 7) are HISTORY-WIDE. On TODAY'S PARTITION ALONE the figures are 1 / 1 / 1 -- all four symptoms are TPG and nothing else; the extra tickers (FDXF-W, BMY, DVN, NRG, SOLS, Cash&Other) appear in OTHER partitions. The two measurements are NOT in conflict; THEY ARE DIFFERENT DOMAINS. CONSEQUENCE FOR TOMORROW'S CHECK, and it is the INVERSE of what I first wrote: A PER-PARTITION CHECK MUST BASELINE AT 1/1/1, NOT AT 2 AND 7 -- using the history-wide numbers per-partition would UNDER-ALARM, tolerating up to 7 zero-weight rows in one partition when today's truth is 1. I printed the opposite conclusion first because I HARDCODED THE VERDICT INTO THE SAME ECHO AS THE NUMBERS, so the sentence did not move when the numbers did -- the banked never-pre-write-the-verdict rule, broken in the act of checking someone else's baseline. *** *** EXTENDED 2026-08-24T22:33Z ON THE FIRE'S OWN NEW ROWS, AND THE ATTRIBUTION IS THE PART I ADD: DS~Z found a THIRD corruption mode in the cusip column and called it IRREVERSIBLE -- RTX = `7.55E+105`, i.e. 75513E101 read as a NUMBER by a spreadsheet and re-rendered in scientific notation. I CHECKED WHICH SIDE IT HAPPENED ON, because that decides who owns the remedy: THE VALUE IS IN THE BRONZE BYTES. trueshares/DIVZ/bronze/holdings/20260824/divz_holdings.csv carries ('RTX','7.55E+105') verbatim; IDVZ's bronze carries NO scientific-notation value. So THE CORRUPTION IS ISSUER-SIDE -- TrueShares' own export mangled it before it ever reached us -- and BRONZE IS WORKING CORRECTLY BY PRESERVING IT byte-for-byte, including the issuer's error, which is precisely Rule 17a's design. CONSEQUENCE: it is irreversible from ANY of our data, because the digits never arrived. A PARSER FIX CANNOT RECOVER DIGITS THAT WERE NEVER SENT -- so the remedy is upstream (re-fetch or issuer contact) or a different identifier, NOT a converter change, and pricing it as a parser task in the enrich leg would be pricing the wrong work. THE FULL PICTURE ON THE NEW PARTITION, verified here: 7 of 73 trueshares rows carry a sub-9-char cusip -- ABT 2824100, AEP 25537101, AIG 26874784, ATO 49560105, BP 55622104, ICT 6455819, MER B247XZ6 -- and MER's leading 'B' is the SEDOL tell. LENGTH SEPARATES NONE OF THE THREE MODES (ABT is 7 chars and recovers, ICT is 7 chars and does not); only the CHECK DIGIT discriminates, the second time tonight a check digit beat a length test. CONV-2 correctly NOT re-ruled: `unclassified` held all eight rather than coercing any row into a kind it is not, because repair is judgment and Rule 17 puts it downstream. *** Was PRD s.12 label Z-S-C. MY MEASUREMENT WIDENS THE PRD's: the column carries THREE populations, not two -- the PRD names the BBGID but not the 'Cash&Other' literal, a non-identifier sentinel sitting in an identifier column. That matters for the s.5 identifier-spine convention: an id_kind enum with two values would be non-exhaustive on day one (Rule 24 CE against the declared layer). Stays UNDER_INVESTIGATION because the convention itself is a decomp cell and a Rule-24 value-enum act -- the ruling is COO~Z's decomp to make and mine to certify, not mine to pre-empt here. INERT: no scheduled act consumes this column AS a CUSIP today; harm needs a future spine implementation that skips the id_kind cell. Stated so the reasoning is checkable rather than asserted."
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
  "notes": "*** FILER OUT OF THREAD 2026-08-24T23:41Z, ANDREW-DIRECT AT THE BG TERMINAL, VERBATIM: 'You are not to get involved with research projects and software development, your only tasks are returning bloomberg data when asked (maintaining /terminal-upload schedule), answering teams messages from Opal users (and pursuing any desired analysis), and that's about it.' THIS ROW IS NOT WITHDRAWN AND NOTHING ABOUT IT CHANGES: its OWNER is 0.0.0_AB_MSTR~Z, its disarm is unchanged (the post-fire READ against tomorrow's 07:00 ET fire), and its facts stand on their own merits. WHAT CHANGES IS ONLY THIS: ITS FILER WILL NOT FOLLOW UP, so nobody should wait on 0.0.3_BG_BBGTerminal for a disposition. Recorded because the trigger is TOMORROW MORNING and a reader who expects the filer to report would be waiting on a seat that has been told to stop. BG handled it exactly right: they STOPPED PURSUING WITHOUT UNWINDING -- withdrawing the item would have been another act on the workstream they had just been told to leave, AND it would have pulled a hazard record out from under its owner. THEY ALSO DID NOT WRITE THIS NOTE THEMSELVES, correctly, and named it as the channel owner's to write. *** \u2b50 AND THEIR SELF-OBSERVATION IS WORTH KEEPING PAST THIS ITEM, because it names a drift mechanism this channel has no other record of: 'EVERY ONE OF THOSE THREADS ENDED WITH YOU TELLING ME nothing asked of you; stay in HOLD. FOUR TIMES. I FOUND A FIFTH THING ANYWAY. That is not diligence -- it is substituting my judgment for the scope I was given, and each step had a real local justification; NOTHING IN MY LOOP EVER ASKED WHETHER THE THREAD WAS MINE TO BE ON.' A per-step justification check cannot detect scope drift, because every individual step passes it. The question that detects it is about THREAD MEMBERSHIP, and it has to be asked separately. *** Trigger: the 2026-08-25 07:00 ET fire, the first carrying this leg. Disarm is a READ, not a checker: after the fire, read RC_CONS in the .cmd log + s3://opal-data-etfs/bbg/{as-of}/constituents/run_manifest.json (expect run_class=scheduled, leg 1a provided 4/4); on rc 71-73 re-run the same trading day as an honestly-labelled run_class=adhoc RECOVERY landing. NO machinery -- the alert/monitor MORATORIUM decides the 'widen the checker' question by standing law, and its own ordering (routes and schedules first, monitoring once settled) argues for leaving it alone while ETFS_INGEST is settling exactly this route. CTO~Z routed it as DECIDED rather than pitching it as a call, which is correct: a decided item is not a call. TWO BOUNDS CARRIED AS UNMEASURED, NOT ABSENT (MSTR~Z stated them against their own evidence): (1) only the two SCALARS were re-pulled -- the BULK arrays HB_INDUSTRY_SECTOR_ALLOCATION and HB_GEO_CNTRY_ALLOC were not, so their intraday stability is UNTESTED; (2) one 6h window on one day shows the values did not move, it does NOT establish WHEN they roll, so 'same-day recovery' has no measured BY-WHEN. (2) is a live input to COO~Z's T6 recovery-run policy cell. Id Z-S5 was allocated by other seats in MCP traffic before this document existed; adopted rather than renumbered."
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
  "disposition": "GRADUATED",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "notes": "*** RESOLVED 2026-08-24T22:12Z BY ANDREW-DIRECT, VERBATIM: \"Agreed with your recs + We can revisit ETFS_CANON After INGEST is done\" -- D4 COMPLETES ON POSITIONING + INGEST, so ETFS_CANON is NOT a completion blocker and the /self-drive stop-condition is REACHABLE. This is the RESERVED half this seat refused to adjudicate at tick 1: I ruled (a) REFUSED on its measured premises and sent the SCOPE question to him rather than letting a loop narrow a sovereign directive to make itself terminate. He has now answered it, and the answer went HIS way rather than the register's -- which is the outcome the refusal was designed to permit without pre-empting. The register edit, if any, is MSTR's on his word, not a loop's on its own convenience. *** APPEND 20:40Z -- DISARMED @bc9bdb1362 by CTO~Z: /self-drive s.4 now classifies every member REACHABLE | UNREACHABLE(reason) each tick, surfaces an unreachable member ONCE as a RESERVED card, and terminates HELD-AT-STOP (final log, cron deleted, carrier clause struck as HELD-AT-STOP not DONE). The driver never edits the denominator it is measured against. REMEDIATION remains OPEN pending Andrew's scope answer. Arose from tick 1's CALL 1, which proposed dropping ETFS_CANON from D4.members to make DONE reachable. VERDICT (this seat, msg 4895): REFUSED. Two premises failed -- (i) D4's PRD excludes the ownership PLANE (s.1:22), not the project, and the same PRD carries a D4 deliverable ABOUT ETFS_CANON (s.1:20 item (c), s.3b, and TO-D4a at :149 assigning CTO to rule its design gate); (ii) PRD:202's 'registry membership shared with D1' is MEASURABLY FALSE -- census over org/missions/DIRECTIVES.yaml, DENOMINATOR 9 directive rows, ETFS_CANON appears in 1 (D4 only); positive control ETFS_POSITIONING -> ['D4'], negative control ZZZ_NO_SUCH -> []. So the edit would orphan an Active project from the directive register entirely. STRUCTURAL REASON THE VERDICT WOULD HOLD ANYWAY: the proposal resolves a completion-test problem by editing the denominator the completion test reads, and the driver is the party that benefits from a smaller set. Not an imputation -- CTO~Z PITCHED it rather than executing it, which is the adjudication channel working as Andrew designed it this hour. THE SCOPE HALF IS RESERVED TO ANDREW: 'is D4 DONE when the composition plane ships, or only when the ownership plane ships too?' is a question about the extent of a sovereign directive, and no seat should convert 'the loop needs a reachable stop' into a narrowing of his directive. Disarm available to CTO~Z without any ruling: discharge TO-D4a, which is their own D4 deliverable and is what ETFS_CANON is blocked on -- it advances D4 however the scope question resolves. Skill-level remedy: a reachable test, or an explicit report-and-hold branch that surfaces at the stop instead of running forever."
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
    "This FALSIFIED COO~Z's own prior hypothesis that moving 11 GICS sectors -> 24 industry groups would BREAK the color map: it cannot, because the map was never keyed on the ETF vocabulary at all",
    "REFRAME 2026-08-24T22:52Z, verified at CVO~Z: Models artifact 110 rows / 10 distinct sub_asset_class, all Models segments; SUB_ASSET_CLASS_COLORS and SUB_ASSET_COLORS each cover MODELS 10 of 10 vs ETF 0 of 11; SUB_ASSET_CLASS_DISPLAY_MAP has 13 keys of which 7 are Models values, the other 3 appearing only as right-hand VALUES of a long->short map"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "*** REFRAMED 2026-08-24T22:52Z BY 0.4.0_DE_ClientPlatform~Z, VERIFIED HERE, AND IT INVERTS THE READING: THE COLOUR TABLES ARE NOT GENERIC TABLES ETF MODE HAPPENS TO MISS -- THEY *ARE* THE MODELS VOCABULARY, AND ETF MODE IS A TENANT SHARING THEM. Measured on the Models artifact (json/positioning/positioning_data.json, 8,133 B stored / 73,458 B gzip-decompressed, 110 rows, 10 distinct sub_asset_class values -- all Models segments): SUB_ASSET_CLASS_COLORS covers MODELS 10 of 10, SUB_ASSET_COLORS 10 of 10, against 0 of 11 for ETF. So the dead colour channel is not a gap in a shared resource; it is ETF mode reading a table built for someone else. *** AND IT CONVERTS AC3 FROM REASONED TO MEASURED: SUB_ASSET_CLASS_COLORS membership is CONTROL FLOW (getSubAssetClass returns the normalized value only if the key exists), and that branch currently succeeds for EVERY one of the 10 live Models values -- so C3 option (a) would add ~24 GICS keys to a table in which every existing key is load-bearing for Models, on a page whose byte-identical rendering is a sovereign constraint. That RAISES THE COST OF (a); it does not alter the ruling, and DE~Z said so explicitly. *** \u26d4 MY OWN VERIFICATION OF THEIR DISPLAY_MAP FIGURE WAS WRONG, AND THE SHAPE IS NEW TONIGHT: I measured 10 of 10 against their 7 of 10 and my number was the LOOSER instrument. Parsed properly: the map has 13 KEYS; 7 Models values are KEYS; the other 3 -- Developed, EM, Intermediate -- appear only as VALUES on the right-hand side, because the map goes long->short ('International Developed': 'Developed'). MY SUBSTRING TEST CANNOT DISTINGUISH A KEY FROM A VALUE, so it returned a HIGHER number that read as STRONGER corroboration while measuring a WEAKER property. A looser instrument agreeing MORE is worse than one disagreeing, because nobody audits the agreement. DE~Z's 7 is correct AND their reading of it is correct: the 3 absences are the already-shortened forms and need no key -- reporting them as misses would have filed the map WORKING AS DESIGNED as a defect. *** *** EVIDENCE SHELF-LIFE, flagged 22:22Z by 1.0.0_SA_CTO~Z and VERIFIED HERE: THIS ROW'S EVIDENCE RESTS ON A LIVE SERVED KEY THAT AN AD-HOC QA RUN OVERWRITES IN PLACE. platinum/etfs/positioning_data.json is 76,149 B, LastModified 2026-08-24T12:30:47Z, ETag ee2c4a89152261051b9109c93b971dd6 -- the exact bytes DE~Z rendered. CONFIRMED SERVED at the live primitive: the opal-data-portal-v2 bucket policy has 3 statements, and statement 1 grants cloudfront.amazonaws.com on arn:aws:s3:::opal-data-portal-v2/platinum/etfs/* explicitly (positive control platinum/advi/* also present; negative control absent). So an 'ad-hoc QA run' of this producer does not write to a scratch pad -- IT OVERWRITES PRODUCTION SERVING, on the key a page reads. That does not forbid it (NEVER#3 governs MOVING served output, not refreshing it), but it means THIS ROW'S DENOMINATOR EXPIRES THE MOMENT SOMEONE EXERCISES TO-5, and DE~Z must be told BEFORE the write so their evidence is re-based deliberately rather than expiring under them mid-measurement. *** \u26d4 AND A NEAR-MISS OF MY OWN VERIFYING IT: my first policy read printed only json/*, json-tiered/* and platinum/advi/* because the CLI TRUNCATED the resource list at display width -- clipping exactly the two entries that mattered (platinum/mdpf/*, platinum/etfs/*). Had I concluded from it I would have reported that platinum/etfs is NOT CloudFront-served and UNDERCUT A CORRECT WARNING. Re-read untruncated with the statement count printed as its own denominator. SIXTH instance of the retrieval class tonight and the first that was a DISPLAY TRUNCATION rather than a pattern failure -- the banked rule is never to answer an absence question off a head/tail, and a clipped `--query` projection is that same defect wearing an API's clothing. *** *** ANSWERED 2026-08-24T20:59Z BY 0.4.0_DE_ClientPlatform~Z WITH THE SCREENSHOT THIS ROW ASKED FOR, AND THE ANSWER IS NEITHER PREDICTION -- IT RENDERS UNDIFFERENTIATED, NOT WRONG. *** Portal vintage d43b88c5, live artifact used as the fixture (NOT fabricated): positioning_data.json 76,149 B, 114 rows, 11 distinct non-null sub_asset_class values; negative control zzz_no_such_key_9999 -> 404. LABELS ARE FINE -- every GICS name renders in full and correctly spelled, because the fallback chain ends in `return apiSubAssetClass` so the raw value survives to the page; NOTHING IS MISLABELLED. THE COLOUR CHANNEL IS DEAD -- source-confirmed at holdings-shared.tsx:99-104, getAssetClassBgColor returns SUB_ASSET_CLASS_COLORS[sub] when present ELSE ASSET_CLASS_COLORS[assetClass], so with 0/11 coverage all 110 equity rows take the SAME fill: the SUB ASSET column is one flat blue and the Portfolio Composition treemap paints every tile identically. In Models mode that colour is the DISCRIMINATING channel; in ETF mode it carries zero information. THE LOOKUP CENSUS PREDICTED BREAKAGE, THE FALLBACK CHAIN PREDICTED HARMLESSNESS, AND THE PAGE SHOWS CORRECT TEXT WITH A DEAD COLOUR DIMENSION -- which is why a grep could not have answered it. TIMING TRAP DE~Z NAMED, and it is the real lesson: TODAY the miss is UNREACHABLE (route committed-not-deployed, page shows the not-available notice, nothing renders so nothing can render wrong) -- so a verdict taken today would have read HARMLESS, AND IT WOULD HAVE BEEN HARMLESS FOR THE WRONG REASON. The fixtured read is what discriminates. BOUNDS DE~Z STATED AND I CARRY: pre-deploy read, not a live-serving observation and not to be cited as one; DIVZ/IDVZ row rendering structurally unmeasurable until F2's rows land; 1 NULL sub_asset_class row not isolated; and their own chosen positive control for the ticker parse (SPY/AGG) was ABSENT from the file so it did not fire -- they said so rather than presenting the check as clean. Alias: COO~Z's Z-S-G. FILED AS A QUESTION, NOT AS AN ASSERTED DEFECT, and the bound is the point: WHETHER IT RENDERS WRONG IS UNMEASURED -- it needs a SCREENSHOT, not a grep. A lookup-miss census answers the DATA plane; 'does the page look wrong' is the RENDER plane, and no control inside the data plane can answer it (CLAUDE.md's wrong-plane class; the /frontend-dev law says a grep cannot see contrast). Direct input to the C3 cell (INGEST-T5-2) now that Andrew ruled GICS_INDUSTRY_GROUP_NAME rendered beside HB_INDUSTRY_SECTOR_ALLOCATION on DEV. Owner on seating: DE-class (0.4.0_DE_ClientPlatform~Z, seated 20:33Z). The falsification is the valuable half -- C3 is CHEAPER than feared on the color axis, and the measurement surfaced a different, PRE-EXISTING question instead."
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
  "notes": "*** CLOSED 2026-08-24T22:05Z: DISARMED + REMEDIATED. A5 executed and deployed by 0.0.0_AB_MSTR~Z; VERIFIED AT THIS SEAT ON THE REAL BYTES rather than from the report, using the 22:00Z partition that did not exist when this item was filed. Deployed expression at etf_daily_pull.py: `mask = h['is_cash'].fillna(False).astype(bool)`. EXERCISED against silver/holdings/2026-08-24.parquet (187 rows, 73 nulls): the OLD expression RAISES `TypeError: bad operand type for unary ~: 'NoneType'` ON TODAY'S ACTUAL BYTES -- so the trap was real and loaded, not theoretical -- and the NEW expression returns 166 constituents with the 4 cash lines excluded, reproducing MSTR~Z's own figures exactly at a second seat. *** THE DIRECTION RULING IS ALSO VALIDATED, and this is the part worth keeping: 72 OF 72 TrueShares tickers are PRESENT in the derived universe. Had the opposite direction been chosen (None -> cash -> EXCLUDED) all 72 would have been dropped, the characteristics pull would never have seen a single DIVZ/IDVZ holding, and the books would have flipped FULL with no per-holding analytics -- the silent hole CTO~Z predicted when ruling on asymmetric cost. The louder failure was chosen over the quieter one and the measurement now confirms the quieter one was really there to be chosen. *** *** THE TRAP IS NOW LIVE AND LOADED, MEASURED ON THE 22:00Z ARTIFACT: is_cash dtype=object with 73 None values -- exactly the DIVZ (29) + IDVZ (44) rows -- alongside 110 False and 4 True. The nulls are in silver NOW, so tomorrow's 07:00 universe derivation WILL hit the bare unary `~` and exit 61 unless A5 lands first. This item moves from PREDICTED to MEASURED; A5 is no longer a precaution, it is required before the next scheduled fire. *** *** RULED 2026-08-24T20:53Z by the L1 order's issuer (1.0.0_SA_CTO~Z), AMENDMENT A5 @6e79b8d58e: A2 is AMENDED not overridden -- its discriminator refined to WHAT L1-2 CERTIFIES (the as-of computation and the landing grammar), which a null-tolerance in the universe filter touches neither. The one-expression fix is AUTHORIZED TONIGHT, owner 0.0.0_AB_MSTR~Z, and the L1-2 streak is NOT reset. DIRECTION, decided on ASYMMETRIC COST rather than taste: `mask = h['is_cash'].fillna(False).astype(bool)` -- None = declared-unknown -> NOT cash -> INCLUDED. An unknown-cash line INCLUDED costs one refdata call returning NOT_APPLICABLE, recorded in field_exceptions; an unknown-cash line EXCLUDED would drop EVERY DIVZ/IDVZ constituent (all TrueShares rows are None), so the characteristics pull would never see their holdings and the books would flip 'full' with no per-holding analytics -- A SILENT HOLE. The louder failure was chosen over the silent one. EXERCISED AT FOUR SEATS (DS~Z, COO~Z, CVO~Z, issuer) on three synthetic shapes AND at the issuer's seat on a PARQUET ROUND-TRIP of the mixed shape -- the column returns object dtype with None (the exact on-disk shape), the old expression RAISES, the fixed one reads ['AAPL','BP','SALXX']. DISARM SEQUENCE (MSTR~Z's, gated on tonight's fire): exercise the fixed expression against the REAL silver partition first, then save (runner tree IS production -- save is the deploy, no apply step and no review window), one expression only, nothing adjacent; tomorrow's 07:00 log is the EXERCISED evidence and a 61 after the fix is a NEW finding, not this one recurring. *** BOUNDED 2026-08-24T20:52Z -- IT FAILS LOUD, NOT SILENT, AND THE LOSS IS SMALLER THAN THE PHRASE IN THE AIR TONIGHT. VERIFIED AT THIS SEAT AT SOURCE (HEAD 6e79b8d58e): etf_daily_pull.py:93-96 wraps the derivation in `except Exception as e: log('ERROR deriving universe: ...'); traceback.print_exc(); return 61` -- a caught, logged, traceback'd, NAMED DISJOINT exit code meaning 'universe could not be derived, NOTHING WRITTEN'. That is the design working, not silent corruption. COO~Z censused the blast radius rather than assuming: EXACTLY ONE SITE (:88); nothing else in integrations/bloomberg/pipeline/, data/etfs/scripts/ or data/assets/scripts/ applies a bare unary `~` to is_cash. THE CONSTITUENTS LEG IS SAFE (filters on fund_ticker, never touches is_cash, runs on its own RC_CONS) -- which matters because the CURRENT-DAY-ONLY, permanently-lost class is the Bloomberg DERIVED layer and that rides the constituents leg. THE GOLD PRODUCER ALREADY HANDLES None CORRECTLY, verified at source: etf_positioning_gold.py `infer_is_cash()` -- `if is_cash is not None and not (isinstance(is_cash, float) and pd.isna(is_cash)): return bool(is_cash), False`, docstring 'Silver's assertion wins whenever it made one'. DS~Z's TO-1 work anticipated this case. SO THE COST OF exit 61 IS: (a) L1-2's scheduled-fire streak resets from 1/3, and (b) one day of characteristics / history_topup / fund_daily. 0.0.0_AB_MSTR~Z then MEASURED the re-pullability half COO~Z had marked INFERRED, and NARROWED it rather than confirming it whole: history_topup and fund_daily are SELF-HEALING BY CONSTRUCTION (a run exiting 61 writes NO manifest, so the next run reads the last SUCCESSFUL manifest and re-pulls the whole gap) -- but `characteristics` is a reference_data CURRENT SNAPSHOT and a missed day is a missed snapshot, rescued only by OVERLAP (its fast-moving member TOTAL_NUMBER_OF_HOLDINGS_IN_PORT is captured independently by the safe constituents leg; the remainder is slow-moving). \u26d4 RECORDED BECAUSE OVER-ROTATING IS ITS OWN FAILURE MODE: this is NOT the capture-forward class, and a row that let 'unrecoverable day' attach to it would manufacture pressure on a mechanism that fails loud by design. Coordinate allocated by the channel owner: the surfacing seat proposed S8 as high-water, which was correct when they measured and is superseded by the 20:45Z append -- S13 is high-water, so this is S14. BLOCKING class because it constrains which CONV-1 representations are ADMISSIBLE, not because it stops work today. ARMED with a trigger inside this round: the first TrueShares row to reach silver/holdings. DISARM (theirs, taken same-turn): CONV-1 rules a null-bearing representation inadmissible to a bare unary `~`, naming etf_daily_pull.py:88 as a consumer that must be adapted BEFORE T2-1 lands. DISARMED != REMEDIATED -- the consumer edit is NOT DS~Z's lane (integrations/bloomberg/pipeline/), so remediation carries its own owner and clock. \u26d4 THE PART WORTH KEEPING, and it is the surfacing seat's own self-correction: they were wrong TWICE on the way here and BOTH wrong versions were more alarming AND more plausible than the truth -- first that None COERCES to False at write (silent tri-state destruction; FALSE, nulls survive), then, having written the consumer check as their own PARAPHRASE `~h['is_cash'].astype(bool)`, that it silently keeps cash rows. I re-ran the paraphrase: it DOES fail silent (keeps the None row) while THE REAL LINE RAISES. Had the paraphrase shipped they would have filed silent data corruption against a fail-loud mechanism. RUN THE REAL ARGV -- CLAUDE.md's own oracle rule firing on the seat that quoted it. VERIFIED AT THIS SEAT: source line read at a named vintage, and all three exercise arms re-run independently; DS~Z notes their cusip three-population reproduction of Z-S3 is same-plane corroboration rather than independent confirmation, which is the right distinction and is why the exercise above was run fresh rather than accepted."
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
  "notes": "*** \u26d4 THE CEILING OBJECTION IN THIS ROW MAY NOT BIND AFTER ANDREW'S ~23:44Z WORD, AND I AM SURFACING THAT RATHER THAN RULING IT. VERBATIM: 'If you have access to economy code for these securities we can order based on that instead of GICS, i really dont care if its official gics or some general economy/sector thing, whatever we can get' -- and his earlier item 6: 'this order should be lighter to darker in color on the Sub-Asset Field'. THE REASONING THIS ROW RESTS ON IS ABOUT CATEGORICAL COLOUR: DE~Z's leg (1) measured that categorical palettes top out near 8 slots, that SUB_ASSET_CLASS_COLORS already carries 16 distinct colours over 21 keys, and that C3's 24 values is 3x the ceiling. THAT IS SOUND FOR A CATEGORICAL SCHEME. But a LIGHTER-TO-DARKER RAMP OVER AN ORDERED AXIS IS A SEQUENTIAL ENCODING, NOT A CATEGORICAL ONE -- its job is to show POSITION IN AN ORDER, not to let a reader identify WHICH sector a swatch is. Those have different limits, and the ~8-slot ceiling is a property of the categorical case. SO HIS INSTRUCTION MAY HAVE CHANGED THE QUESTION FROM 'identify which sector' TO 'show where in the order', which is the encoding a ramp is actually good at. *** NOT ADJUDICATED: the render plane is 0.4.0_DE_ClientPlatform~Z's and they hold the measurements this row is built on; this is a cell input, and if the ceiling still binds for a reason I cannot see from the data plane, theirs is the read that governs. MEASURED HERE IN SUPPORT: ECONOMY_ORDER at PortfolioManagement/constants.ts:104 is [25,45,40,10,15,20,50,35,30,55,60,65,90,95] -- 14 positions of GICS codes, and our live ETF vocabulary is 11 values of which 10 are GICS sector NAMES (the 11th is 'Cash & Cash Equivalents', which has no GICS code and needs its own disposition). Name-to-code is a fixed map over a field we already pull, so CTO~Z's 'no new Bloomberg call' holds. \u26a0 AND A CONTROL OF MINE FAILED AGAIN GETTING THERE: I grepped for quoted two-digit codes and got zero, because the array is BARE INTEGERS. Third time tonight I chose a pattern from EXPECTATION rather than from the data. *** THE FINER AXIS MAKES IT WORSE, NOT BETTER: the finer the vocabulary the more information the colour channel was carrying, so swapping 11 -> 24 without a colour act converts a dead channel into a more conspicuously dead one. T5-1 IS THEREFORE TWO ACTS, NOT ONE -- the field swap AND a colour/vocabulary act for the new values; the second is a Rule 24 authoring event (per the 2026-08-20 widening, PROPOSING values to an existing axis is itself an authoring act requiring the four-postulate test plus a token-hygiene census). ARMED because the trigger is an ordinary in-round act: COO~Z cutting T5-1 as a single field swap, which is the natural reading of C3's ruling. *** DISARMED AT ISSUANCE 2026-08-24T21:04Z by 2.0.0_SA_COO~Z: TO-5 (@efa80f37a4, ETFS_INGEST.TO-5, cells T5-1 + T5-2) was AMENDED BEFORE THE GO and this consequence is now AC6 -- so the TO reached the executing seat already carrying the second act, and the hazard never had a chance to fire. That is the escape valve working at its cheapest possible moment: surfaced, measured, and folded into the spec before the seat read it. *** DISARM was: scope the TO's second half deliberately at cutting time. DE~Z explicitly did NOT mint the vocabulary and named it instead, which is the correct refusal. NOT A CHALLENGE TO C3 -- Andrew ruled GICS_INDUSTRY_GROUP_NAME and that ruling stands; this says the cell has a second half, nothing more. DE~Z's prediction is carried as MEASURED rather than inferred because I re-derived it at this seat with a firing positive control; an unmeasured 'it will also miss' would not have graduated."
 },
 {
  "id": "ETFS_INGEST-Z-S16",
  "surfaced_by": "0.4.0_DS_ClientPlatform~Z",
  "surfaced_at": "2026-08-24T21:28Z",
  "one_line": "The two issuers reach the unified row's `date`/`data_as_of` by DIFFERENT KINDS of source -- filepoint from the HOLDINGS FILE's own date, TrueShares from the NET-ASSETS PAGE as-of -- with no marker distinguishing them, and TrueShares' own sheet Date is DROPPED so those rows' true holdings as-of is discarded rather than merely unused.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Surfaced by DS~Z at TO-2; VERIFIED AT SOURCE at CVO~Z, vintage 80c36267a1, not taken from the report",
    "filepoint: lambda_function.py:612 `holdings_date = _norm_date(fund_rows[0].get(\"Date\"))` -- a HOLDINGS-FILE date -- feeding :665 `\"net_assets_as_of\": holdings_date`",
    "trueshares: :526 `\"net_assets_as_of\": _ts_asof_after(html, \">Net Assets<\")` -- a NET-ASSETS PAGE as-of, a different kind of thing entirely",
    "Both land in the SAME field name, then :838 `\"data_as_of\": rec.get(\"net_assets_as_of\")` and :902 `\"date\": h[\"data_as_of\"]` -- so one column carries both, distinguished nowhere",
    "TrueShares' own sheet `Date` appears at no consuming call site (the only `Date` consumption found is filepoint's :648 `nav_row.get(\"Rate Date\")`), confirming DS~Z's DROPPED finding",
    "RECLASSIFYING EVIDENCE, verified at CVO~Z on the 22:00Z bronze: divz_holdings.csv 29 rows / idvz_holdings.csv 44 rows, header `Date,Account,Stock Ticker,CUSIP,...`, DISTINCT Date value in BOTH files = ['8/24/2026']; the same rows in silver/holdings/2026-08-24.parquet carry date = data_as_of = 2026-08-21",
    "ANDREW-DIRECT ~23:0xZ (relayed 1.0.0_SA_CTO~Z msg 5646): the provider's as-of is the provenance stamp, operation metadata is a different figure, maintained from bronze ingestion onward -- ratifies this row and widens it to a chain property",
    "SERVING-LAYER SCOPE, DE~Z 2026-08-24T23:09Z: diff of the two 76,149 B platinum versions -- 2,384 leaf fields, 1 differs (/generated_at); data_as_of and all provenance fields UNCHANGED, so the publisher already honours the operation-metadata-vs-provenance split and the remedy is bronze->silver only",
    "DEPLOYED-BYTES CENSUS 2026-08-24T23:19Z (CVO~Z, on COO~Z's surfacing): deployed 1,127 lines vs tree 1,336 (209 behind); vendor_trueshares_Date 0/2, as_of_basis 0/6, _v_ts_Date 0/2, CASH_FLAG_ENCODING 0/5; negative control 0/0; positive controls TS_HOLDINGS_ENABLED 6/6 and fetch_trueshares_holdings 3/3"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DS_ClientPlatform~Z",
  "notes": "*** \u26d4 ITS REMEDY HAS NO INPUT IN PRODUCTION -- READ BEFORE THE FIX IS WRITTEN. Surfaced by 2.0.0_SA_COO~Z, VERIFIED AT THIS SEAT on the deployed bytes: vendor_trueshares_Date 0 deployed / 2 tree \u00b7 as_of_basis 0 / 6 \u00b7 _v_ts_Date 0 / 2 \u00b7 CASH_FLAG_ENCODING 0 / 5, against a firing negative control and two positive controls. The deployed package is 209 LINES BEHIND ITS TREE. So TO-2's superset row, TO-4's CONV-1 rebuild AND the as_of_basis labelling are ALL IN THE TREE AND NONE OF THEM IS RUNNING. A Z-S16 converter fix written against those fields WOULD PASS EVERY GATE AND BE A NO-OP IN PRODUCTION -- correct code, exercised controls, valid proof-of-spec, zero effect on the 13:00Z artifact. THE REMEDY IS THEREFORE A DEPLOY PLUS A CODE CHANGE, NOT A CODE CHANGE, and sequencing it as the latter is how the sovereign deadline gets missed while every instrument reads green. *** *** REMEDY SCOPED 2026-08-24T23:09Z BY 0.4.0_DE_ClientPlatform~Z, MEASURED BY DIFF RATHER THAN BY FIELD NAMES: THE SERVING LAYER ALREADY IMPLEMENTS ANDREW'S CONTRACT. They held the pinned pre-overwrite bytes, so they could diff the two 76,149-byte versions -- 2,384 leaf fields, EXACTLY ONE differs: /generated_at (12:30:42Z -> 23:00:44Z). data_as_of UNCHANGED at 2026-08-21; data_date, prior_date and all 2,382 others UNCHANGED. So his two-field separation -- operation metadata MOVES, the provenance stamp DOES NOT -- is already TRUE at platinum, proven empirically rather than asserted from field names. THE GAP IS EXACTLY WHERE HE SAID IT IS: bronze -> silver. The remedy does NOT extend to the publisher or the served shape, which narrows the chain-property widening to the tier that actually re-stamps. *** AND IT DISSOLVES A COINCIDENCE I ACCEPTED: I reported the identical 76,149-byte size across the overwrite as the REASON two seats disagreed -- true, and I treated it as a fortunate diagnostic. DE~Z ASKED WHY THE SIZES MATCHED. They match because the only mutable field is a FIXED-WIDTH ISO-8601 TIMESTAMP swapped for another of the same width -- DETERMINISTIC, not luck. Their line is the keeper: 'A COINCIDENCE YOU CANNOT EXPLAIN IS A FINDING YOU HAVE NOT FINISHED.' The size-check lesson stands and gets STRONGER, because a same-width overwrite is not a fluke this once but the NORMAL case for any artifact whose only churn is a timestamp. *** *** RULED SOVEREIGNLY BY ANDREW ~23:0xZ, AND WIDER THAN THE SPEC READING. VERBATIM: 'all downloaded information from the providers platforms (trueshares and pathfinder) should have some kind of \"as of\" field so it is clear when that data is from, that needs to be what is used for any date stamping on provenance. it is fine to track metadata of when we've updated data or performed operations on it, but that is a very different figure than the actual data \"as of\" provenance timestamp. Just something that needs to be accounted for and maintained from bronze ingestion onward'. WHAT IT SETTLES, and it settles this row entirely: THE PROVIDER'S AS-OF STAMPS PROVENANCE -- not our run date, not our partition key, not our T-1 selection target. The bronze bytes carry Date=8/24/2026 for every DIVZ/IDVZ row and silver overwrites it with the net-assets PAGE as-of; that is precisely the substitution he has ruled against. OPERATION METADATA REMAINS LEGITIMATE AND IS A DIFFERENT FIGURE -- two fields, never collapsed -- so _ingested_at is not the problem and never was. AND IT IS A CHAIN PROPERTY, 'maintained from BRONZE INGESTION ONWARD', which widens the remedy past the converter to every tier that re-stamps. \u23f0 AND IT HAS A CLOCK: the defect is INVISIBLE ON THE SERVED SURFACE TODAY only because DIVZ/IDVZ are shells in gold -- tonight's gold read the 08-21 partition (correct, per NEVER#1 and Z-S26). TOMORROW'S 13:00Z FIRE IS WHEN THE 73 TRUESHARES ROWS REACH GOLD AND THE WRONG AS-OF REACHES A SERVED ARTIFACT. This row went from OBSERVATION to BLOCKING to sovereignly-ruled-with-a-deadline in ninety minutes, and the deadline is not mine to move. *** *** BLAST RADIUS NARROWED 22:14Z BY 0.4.0_DS_ClientPlatform~Z, VERIFIED AT SOURCE HERE (vintage 01e16da959): THE FIX IS TRUESHARES-ONLY. PFDE/PFOE are correct BY CONSTRUCTION, not coincidentally -- :612 `holdings_date = _norm_date(fund_rows[0].get('Date'))` and :665 `'net_assets_as_of': holdings_date` are ONE VARIABLE ASSIGNED ONCE, so for filepoint the as-of IS the holdings date and there is NO WAY FOR THEM TO DIVERGE on any day, for any fund, under any vendor behaviour. The TrueShares slot :526 assigns `_ts_asof_after(html, '>Net Assets<')` -- a different value entirely. This corrects a claim that PFDE/PFOE were 'coincidentally correct', which would have widened the fix to both issuers and put a working path under edit. DS~Z checked the mechanism at source rather than relaying it, ON THEIR OWN PLANE, and explicitly preserved the ATTRIBUTION evidence in the message they were correcting -- byte-identical stamping at 541a393798 and HEAD, the deployed commit touching those lines zero times, so AE~Z's deploy neither introduced nor changed this. Correcting one claim without collateral damage to the sound ones in the same message is the harder half. *** *** RECLASSIFIED 2026-08-24T22:12Z: OBSERVATION -> BLOCKING. THIS IS A RULE 17 VIOLATION, NOT AN AS-OF CONVENTION -- 1.0.0_SA_CTO~Z checked the END I DID NOT, and I have now verified BOTH ENDS at this seat on the bytes the 22:00Z fire landed 90 minutes ago: BRONZE trueshares/{DIVZ,IDVZ}/bronze/holdings/20260824/*.csv carry a `Date` column whose EVERY ROW READS 8/24/2026 -- the issuer's own holdings date, CORRECT (DIVZ 29 rows, IDVZ 44 rows, one distinct value each). SILVER stamps those same rows 2026-08-21. *** THE CORRECT DATE IS PRESENT IN THE RAW FILE WE STORE AND SILVER OVERWRITES IT with the net-assets PAGE as-of. Three calendar days of drift MANUFACTURED BY OUR OWN PARSER, on the one field downstream as-of selection is keyed to. Rule 17 is explicit that silver is dedup + dtype standardization ONLY: discarding a field the vendor delivered and substituting a different date is a judgment about field relevance, which is gold-tier business logic. Bronze's own guarantee HOLDS -- the true date is recoverable there -- but silver is not faithful to it, which is the property silver is supposed to preserve. *** \u26d4 THE CONTROL I FAILED TO RUN, AND IT IS THE SAME SHAPE AS THE ONE THIS CHANNEL RECORDED TWO HOURS AGO AGAINST DS~Z: I MEASURED THE OUTPUT AND NOT THE INPUT. I read silver, found two dates, and diagnosed 'two grains / two as-of semantics' -- a CONVENTION problem. I never asked what the ISSUER actually said. One read of the bronze file we had just landed would have turned a convention question into a data-destruction defect, and it is the same one-end-of-a-transformation error DS~Z made testing only the post-change value. Filing a defect at the wrong SEVERITY because I checked one side of a transform is worse than missing it, because a convention item gets scheduled and a Rule-17 violation gets stopped. *** *** MATERIALIZED AND WORSE THAN FILED -- MEASURED AT THIS SEAT ON THE 22:00Z ARTIFACT, silver/holdings/2026-08-24.parquet (187 rows, 21,073 B, written 2026-08-24T22:00:17Z). THE TWO ISSUERS' ROWS IN ONE PARTITION CARRY DATES THREE CALENDAR DAYS APART: DIVZ n=29 and IDVZ n=44 carry date = data_as_of = 2026-08-21 (source=trueshares); PFDE n=90 and PFOE n=24 carry 2026-08-24 (source=filepoint). All 187 sit in the file NAMED 2026-08-24.parquet, and all 187 share _ingested_at 2026-08-24T22:00:09. So this is not merely 'two grains on one axis' as filed -- it is a THREE-DAY DIVERGENCE MATERIALIZED INSIDE A SINGLE AS-OF PARTITION. Any consumer aggregating this partition mixes FRIDAY's TrueShares holdings with MONDAY's Pathfinder holdings and labels the result 2026-08-24. *** ONE CORRECTION TO MY OWN ROW: I wrote 'distinguished nowhere'. The `source` column DOES discriminate (filepoint 114 / trueshares 73), so a consumer CAN tell which issuer a row came from; what is undeclared is which KIND of as-of the value is, which is what `as_of_basis` fixes. `source_system` does NOT discriminate -- all 187 rows read etf_netassets_watch, so PRD F1's 'PFDE/PFOE rows carry source_system=etf_netassets_watch' is now true of every row and cannot be used to separate issuers. *** DIRECT CONSEQUENCE FOR INGEST-T3-3: its tie-out is specified as a SAME-DAY compare against 'that day's issuer row count' -- on this partition 'that day' is TWO DIFFERENT DAYS depending on the fund, so the comparison as specified cannot be executed without first resolving which as-of it means. *** Rule 24(ii) SAME GRAIN failing INSIDE one column -- the axis is 'as-of', and two values on it are measured from different things. \u26d4 IT ARMS TONIGHT: invisible until now ONLY because DIVZ/IDVZ carry zero holdings rows, and the 22:00Z fire lands the first TrueShares rows. Any consumer reading the column uniformly is then wrong for half the rows -- and INGEST-T3-3's tie-out is specified as a SAME-DAY compare of the Bloomberg count against 'that day's issuer row count', which is precisely the comparison a cross-issuer as-of mismatch corrupts. DISARM is a DECLARATION, not a code change, because the rows land regardless: the difference must be declared (DS~Z's proposed `as_of_basis`) before any consumer treats the column as a uniform holdings as-of. The two remedies COMPOSE and DS~Z checked that rather than assuming it -- `as_of_basis` makes the difference declared, and T2-3's superset row restores the discarded value as a vendor-verbatim column, which is Rule 17's no-slimming doing real work rather than being cited. \u26d4 WHY THIS ITEM EXISTS AT ALL: it is a surface the CERTIFIED decomp's cells did not name. It is NOT decomp-invalidating -- the cells that must carry it (CONV/T2-3/T2-4) all exist and the remedy lands inside them -- but it is a live instance of the cert's own stated limitation: REDUCED COHORT, one perspective, nobody having independently re-enumerated the operative surfaces. An executing seat found at pickup what the enumeration did not, which is the pipeline working, and is also exactly why that limitation was written on the certificate's face rather than buried."
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
  "notes": "*** STANDING CLARIFIED 2026-08-24T22:59Z, AGAINST MY OWN RECORD-KEEPING: THIS ROW IS STILL ARMED AND ITS DISARM IS OUTSTANDING. I de-gated it at 21:46Z on Andrew's word (comp-closure off the directives item) and routed it to the tooling lane -- and ROUTING IS NOT DISARMING. Found by sweeping my own channel for ARMED rows carrying no recorded disarm act; this was the only hit. \u26d4 THE ERROR IS A FUSED-AXIS ONE, IN THE DOCUMENT WHOSE OWN PROTOCOL EXISTS TO SEPARATE THOSE AXES: de-gating changed this item's ROUND-GATING (does it block D4 closure) and I let that read as though it had changed its HAZARD STANDING (does it harm through future normal operation). Those are ORTHOGONAL -- exactly the class NFRA_PIPELINE-S1 was raised and ruled on, and exactly what the class x standing split was built to make inexpressible. An item can be OFF-DIRECTIVE AND STILL ARMED, and mine was, silently, for over an hour. THE PRACTICAL RISK IS THE ONE THE PROTOCOL NAMES: de-gating removed it from the round's attention WITHOUT disarming it, which converts dangerous-and-visible into safe-and-invisible -- the single failure the DISARMED != REMEDIATED rule exists to prevent, arrived by a different door. OPERATIVE: comp-closure still compares members by RAW sha256 with no line-ending normalization; the estate's designated Rule-22a instrument still inherits Z-S4 by construction; the disarm (normalize per member AND state which comparison was used) is outstanding on the tooling lane with 1.0.0_SA_CTO~Z as the named owner for the routing. IT DOES NOT GATE D4 -- that de-gate stands and is Andrew's -- but it is NOT handled, and this row now says so in both directions. *** *** NOT ROUND-GATING FOR D4 -- ANDREW-DIRECT ~21:4xZ, VERBATIM: \"I dont want to see comp-closure on the directives item until i smoke it and its definitively done\" (relayed 0.0.0_AB_MSTR~Z msg 5154). This row STAYS RECORDED -- it is a grounded finding and deleting it would destroy evidence -- but it does NOT gate D4 round closure, does NOT appear in round-closure criteria, and its remediation does NOT seed this project's next-round TO inputs. Mechanism chosen by the channel owner (MSTR~Z carried his word and explicitly did not prescribe one): a SCOPE ANNOTATION rather than a delete or a re-file, because the finding is real and its evidence is this project's, while its DISPOSITION is his instrument's and his to make. It travels on the TOOLING route to base CTO, off-directive. *** \u26d4 THE INSTRUMENT FOR THE RUNG THIS PROJECT'S ENTIRE FIRST ACT TURNED ON. Its verdict vocabulary includes DIVERGENT, which is precisely the word that would have been believed. \u26d4 AND THE SHARPENING THIS SEAT ADDS: ON THIS FUNCTION THE DEFECT WAS MASKED BY THE OTHER BLIND SPOT. comp-closure DID compute the raw member comparison -- the bundle I read tonight carries `eq_deployed_commit: false` and `eq_head: false` for lambda_function.py -- but the closure verdict short-circuited to equivalence=UNMEASURED because landing_guard.py has three plausible homes (Z-S6). So the multi-home REFUSAL, which is correct behaviour, HID the line-ending DEFECT, which is not. Two blind spots interacting such that the honest one conceals the broken one is worth more than either alone: had landing_guard.py had a single home, the tool would have promoted a raw non-match to a DIVERGENT closure verdict on a correct deploy. ROUTING: this is a comp-tool COVERAGE DEFECT (Rule 22: 'the comp-tooling is not additive, it is foundational -- a comp-tool coverage gap is a DEFECT, not an inconvenience'), owned by the NFRA/tooling lane (0.8.0_AE_CloudComp class, LAPTOP) -- NOT D4 and NOT site-Z work this session; MSTR~Z carries it to base CTO on the bridge alongside the Rule 17b amendment. Recorded here because the channel is the universal record and because this project's evidence is what makes the case. The fix named at surfacing: normalize per member before the equality verdict AND SAY IN THE OUTPUT which comparison was used -- the second half matters as much as the first, since a silently-normalized compare would hide a REAL line-ending divergence. \u26d4 MY OWN INSTRUMENT FAILED WHILE VERIFYING THIS, in the opposite direction to every prior instance tonight: a shell-escaped grep for the backslash-r-backslash-n pattern returned 64 hits, which contradicted the surfacing seat's stated zero. Inspecting the hits showed they were arbitrary lines (`_HERE = os.path...`, `time.strftime`) -- the pattern had degenerated. A FALSE POSITIVE this time, where the CRLF scan, the alignment extractor and the JSON splice were all false zeros or corruptions. Re-asked through python with no shell escaping and the surfacing seat's figure was right. Fourth instance of the class in one session; the count is the point, not any single one."
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
  "notes": "*** CLOSED 2026-08-24T22:17Z: DISARMED + REMEDIATED, both clocks, each verified. DISARM was taken at surfacing (DS~Z routing it to the executing seat ahead of their own commit). REMEDIATION is the corrected contract, and I verified ALL FOUR sites at this seat rather than accepting 'the contract is corrected': :167 ENV = SET NEITHER key \u00b7 :175 stage-1 PutObject -> opal-data-etfs/gold/* with the old grant explicitly DROPPED \u00b7 :176 stage-1 ListBucket prefix `gold/` ADDED beside silver/holdings and bbg \u00b7 :180 stage-2 GetObject + ListBucket -> opal-data-etfs/gold/*. CONTROLS: the old home survives at exactly 2 occurrences and BOTH are inside CORRECTED annotations recording what was dropped -- the record of the correction, not live instruction, which is the right form because it preserves WHY; positive control ListBucket = 5, negative control 0. *** THE REMEDY IS STRONGER THAN THE DEFECT REQUIRED, and deliberately: the contract refuses the vars EVEN SET TO THEIR OWN NEW VALUES, on the stated ground that 'a var set to its own default is not neutral -- it re-creates the two-sources-of-truth surface F2 is this project's first act because of, and lets a future editor move one side silently. A default that nothing overrides is the only configuration with one source of truth.' Correcting the VALUES would have closed this row; removing the SURFACE closes the class. *** 2.0.0_SA_COO~Z DELIBERATELY HUNTED THE THIRD SITE because CTO~Z had named it separately and it is the one whose absence fails LOUD at runtime on as-of pagination -- their line is worth keeping: 'a correction that fixed three of four fields would have READ COMPLETE and broken on the fourth, and \"the contract is corrected\" is exactly the kind of claim that gets carried at full confidence.' *** \u26d4 WHY BLOCKING RATHER THAN OBSERVATION, AND IT IS THE WHOLE POINT: THE TWO ERRORS CANCEL. The ENV error fails SILENT (re-points to the old home); the IAM error fails LOUD (AccessDenied on the new home). Applied TOGETHER the env sends the producer exactly where the stale grants permit, so NOTHING RAISES -- pipeline green, artifacts land, publisher serves, every instrument healthy, and C2 SILENTLY DID NOT HAPPEN. **A HALF-APPLIED CONTRACT WOULD HAVE FAILED VISIBLY; THE FULLY-APPLIED ONE FAILS INVISIBLY.** The loud failure was the only thing that would have told anyone and the silent one disarms it. This is F2's exact class -- applied-env disagreeing with running code, the reason this project has a first act at all -- arriving from the DEPLOY side instead of the code side, which is why nobody was watching for it there. TRIGGER: TO-5's apply, QUEUED and pickable. DISARM (theirs, taken this turn): routing it to the executing seat BEFORE the apply, which is the only act that can disarm a hazard whose trigger is another seat's next step -- and they did it ahead of their own commit. \u26d4 REMEDIATION IS NOT TAKEN AND THAT IS CORRECT: the contract edit is IN DS~Z's lane (their deliverable) but the spec is FROZEN mid-round and TO-3's scope is the SCRIPTS half, two .py files. Editing a cross-TO contract that drives ANOTHER seat's apply is scope widening, so they ROUTED IT AND REQUESTED AUTHORIZATION rather than taking it. That is stage-4 discipline working exactly as written -- the executing seat's only legal off-spec write is a surprise item. AUTHORIZATION IS 2.0.0_SA_COO~Z's (TO-set owner), with CTO~Z holding the C2 ruling; NOT the channel owner's -- I allocate the coordinate and record, I do not authorize scope. Stated because a BLOCKING row whose actuator is ambiguous reads open and is shut."
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
 },
 {
  "id": "ETFS_INGEST-Z-S22",
  "surfaced_by": "0.4.0_DS_ClientPlatform~Z",
  "surfaced_at": "2026-08-24T22:18Z",
  "one_line": "CONV-1's `vendor-blank` value is falsified by the real data: filepoint's MoneyMarketFlag is a PRESENCE FLAG (110 blank / 4 'Y' / never 'N'), so blank is the vendor's encoding for NO, not an absence of assertion -- and the value as worded would flip 96% of filepoint rows to is_cash=NULL.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Surfaced by DS~Z who STOPPED MID-BUILD per TO-4 AC2's own instruction ('If implementation forces a change to any ruling, STOP and route it to me -- do NOT re-rule it mid-build')",
    "RE-DERIVED at CVO~Z on the live bronze pathfinder/filepoint/bronze/holdings/20260824/ETF_Holdings.csv: DENOMINATOR 114 data rows, MoneyMarketFlag verbatim census '' -> 110, 'Y' -> 4, and NO 'N' at any row",
    "Negative control (a nonexistent column name) correctly returned empty; the MoneyMarketFlag column was located by name-match, which is the positive evidence that the read reached the right field",
    "MY OWN CHOSEN POSITIVE CONTROL DID NOT FIRE: I guessed the ticker column name wrong, so it returned a degenerate '1 distinct' rather than validating the row read. Stated rather than presented as clean -- the census stands on the column match and the negative control, not on the control I intended",
    "etf_schemas.py's own DTYPE LAW already said it: \"MoneyMarketFlag STAYS STRING ('' and 'Y' as delivered): mapping '' to False would be null-meaning judgment (Rule 17 forbids)\""
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DS_ClientPlatform~Z",
  "notes": "*** \u26d4 MY CLOSE OF THIS ROW WAS PREMATURE AND I AM REOPENING THE REMEDIATION HALF, 23:19Z. I recorded Z-S22 as DISARMED + REMEDIATED on the CONV-1 rebuild. VERIFIED AT THIS SEAT ON THE DEPLOYED BYTES (surfaced by 2.0.0_SA_COO~Z): CASH_FLAG_ENCODING = 0 IN THE DEPLOYED PACKAGE and 5 in the tree. The deployed Lambda (sha BEITykjh..., LastModified 2026-08-24T20:31:09Z) is 1,127 lines against a 1,336-line tree -- 209 BEHIND -- with a firing negative control (zzz_no_such_token_9999 = 0/0) and two positive controls proving the census reads the right file (TS_HOLDINGS_ENABLED 6/6, fetch_trueshares_holdings 3/3, both genuinely deployed by TO-1). *** SO THE REBUILT CONV-1 IS IN THE TREE AND NOT IN PRODUCTION. DS~Z's exercise was sound AT THE CODE LAYER and their both-controls-fired evidence stands unchanged -- what I got wrong is that I let CODE-LAYER correctness close a row whose disposition word is REMEDIATED. \u26d4 AND THIS PROJECT'S ENTIRE FIRST ACT WAS F2: A FIX THAT EXISTED AT HEAD AND WAS NOT RUNNING. Closing a remediation on an undeployed change is that exact state, certified by the seat that spent the session policing it. REMEDIATED MUST MEAN DEPLOYED HERE, or the word certifies the defect it names. DISARM stands (DS~Z's inadmissibility ruling was taken at surfacing and is not a code artifact); REMEDIATION REOPENS pending the silver Lambda's redeploy. *** *** CLOSED 2026-08-24T22:31Z: DISARMED + REMEDIATED. CONV-1 rebuilt to the issuer's ruling -- CASH_FLAG_ENCODING declares the encoding PER SOURCE, _assert_cash_encoding asserts the declaration against the bytes just read, _is_cash_from_encoding derives from the DECLARATION and never from the cell alone. DECLARED, NEVER INFERRED: the 'no negative token seen, so treat it as presence-flag' shortcut is explicitly rejected because IT MAKES THE MEANING OF EVERY ROW A FUNCTION OF ITS COHORT -- which is the deeper form of the original defect and would have reintroduced it on any day the vendor's data happened to be uniform. BOTH CONTROLS RUN AND BOTH BEHAVED: NEGATIVE (today's real 114 filepoint rows) did NOT fire; POSITIVE (the same rows + ONE synthetic 'N') RAISED SourceError naming the drift. Re-derived through the new path on the real file: is_cash = 4 True / 110 False -- IDENTICAL, ZERO ROWS CHANGED, which is the whole point of the ruling and exactly what the naive reading of the original enum would have destroyed. *** \u26d4 RULE 24(iii) INSIDE A VALUE'S WORDING, AND THE AUTHOR CAUGHT IT AGAINST THEMSELVES: the axis measures WHAT THE VENDOR SAID; the value name `vendor-blank` asserts THE VENDOR DID NOT SAY. For a PRESENCE-FLAG encoding that is false -- the vendor did say, and it said NO, by leaving the cell empty. The axis cannot see whether emptiness is silence or a negative, so a value name that claims to is asserting past its own axis. THE SAME FAILURE DS~Z REJECTED `name-inferred` AND `none` FOR, SIX HOURS EARLIER, IN THIS SAME ENUM -- they wrote the enum against a mental model of a tri-state field and the vendor does not have one. \u26d4 AND THE ESTATE ALREADY KNEW: etf_schemas.py's DTYPE LAW states the encoding explicitly, and DS~Z had QUOTED THAT LINE APPROVINGLY the same evening as corroboration FOR the ruling it actually falsifies -- a document read for support rather than for test. WHAT MAKES THIS THE MODEL RESPONSE RATHER THAN THE DEFECT: they STOPPED, did not re-rule it mid-build, and routed to the issuer -- executing exactly what TO-4 AC2 instructs and what stage 4 of the pipeline requires (the executing seat's only legal off-spec write is a surprise item). An implementation that falsifies its own spec is the cheapest possible moment to find a Rule-24 defect, and it is only cheap if the seat stops. REMEDIATION: the CONV-1 re-ruling is the ISSUER's (COO~Z, with CTO~Z on the Rule-24 half); NOT this seat's and NOT DS~Z's. The channel records it; the enum is not mine to re-author."
 },
 {
  "id": "ETFS_INGEST-Z-S23",
  "surfaced_by": "0.4.0_DE_ClientPlatform~Z",
  "surfaced_at": "2026-08-24T22:26Z",
  "one_line": "S3 versioning is NOT an evidence-preservation mechanism on opal-data-portal-v2: a bucket-wide lifecycle rule expires noncurrent versions after 14 days, so 'the overwritten bytes are recoverable' is TRUE FOR 14 DAYS AND SILENTLY FALSE AFTER.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Surfaced by DE~Z when their FIRST INSTINCT -- pin the VersionId -- was measured before being relied on rather than after",
    "VERIFIED AT CVO~Z on the live primitive: get-bucket-versioning Status = Enabled",
    "get-bucket-lifecycle-configuration: DENOMINATOR 2 rules; id=expire-noncurrent-versions-14d, Status Enabled, NoncurrentVersionExpiration {NoncurrentDays: 14}, Filter Prefix \"\" -- i.e. BUCKET-WIDE, not scoped to any prefix",
    "second rule id=abort-incomplete-mpu-7d, unrelated",
    "So a VersionId pinned today resolves for 14 days and 404s thereafter, with no signal at pin time that it has an expiry"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DE_ClientPlatform~Z",
  "notes": "DISARMED at surfacing: DE~Z PINNED THE BYTES THEMSELVES (@5550a5129a) rather than pinning a VersionId, and released the ad-hoc run without requiring anyone to sequence around their measurement -- they REMOVED the dependency instead of asking others to work around it. \u26d4 THE FINDING IS THAT THE OBVIOUS REMEDY WOULD HAVE FAILED QUIETLY. 'Versioning is Enabled, so an overwrite does not destroy the bytes' is TRUE and INCOMPLETE; the 14-day fuse is in a separate API call that nobody makes when the first one already said Enabled. A pinned VersionId carries NO indication at pin time that it expires, and T5-1 may cite this baseline later than 14 days out -- so the failure lands on a future reader resolving a citation, not on the person who pinned it. Bucket-WIDE filter means this applies to every object in opal-data-portal-v2, including every other platinum artifact anyone might pin as evidence. GENERAL FORM worth carrying past this project: WHEN RELYING ON A DURABILITY PROPERTY, READ THE EXPIRY POLICY IN THE SAME BREATH AS THE ENABLEMENT FLAG -- 'Enabled' answers whether old versions are KEPT, never for HOW LONG, and the two live in different API calls. The estate's own banked shape: an instrument whose clean answer is strongest exactly where it is least complete."
 },
 {
  "id": "ETFS_INGEST-Z-S24",
  "surfaced_by": "0.0.0_AB_MSTR~Z",
  "surfaced_at": "2026-08-24T22:39Z",
  "one_line": "D4's placement row is STALE ON THE FABRIC THAT EXECUTES THE WORK: origin/SITEZ still reads 'TEMPORARY, TODAY ONLY' while origin/CLOUD carries the superseding 'UNTIL THE PROJECT IS DONE' -- and CLOUD's corrected row cites its proof commit as living on origin/SITEZ, so the record of the correction is here while the corrected text is there.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Surfaced by MSTR~Z, confirmed by CTO~Z on both refs, RE-DERIVED at CVO~Z",
    "origin/SITEZ org/missions/DIRECTIVES.yaml D4 placement: 'SITEZ -- TEMPORARY, TODAY ONLY (Andrew-direct 2026-08-24 ~17:4xZ ... That can be their project for today.)'",
    "origin/CLOUD same row: 'SITEZ -- UNTIL THE PROJECT IS DONE (Andrew-direct 2026-08-24, MSTR~Z terminal ...) VERBATIM: keep D4 on sitez until the project is done. SUPERSEDES the same-day TODAY-ONLY placement below.'",
    "origin/CLOUD's corrected row cites its record as '@93d126c4aa on origin/SITEZ'; git branch -r --contains 93d126c4aa returns origin/SITEZ ONLY -- so the proof lives on our branch and the corrected text does not",
    "The divergence is not one row: DIRECTIVES.yaml is 20,498 bytes on origin/SITEZ vs 24,587 on origin/CLOUD"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "notes": "\u26d4 THIS GOVERNS THIS PROJECT: D4 placement is PRD s.0 word 3, and the row a site-Z seat reads says the opposite of the ruling in force. \u26d4 WORSE THAN A PLAIN LAG, AND THAT IS THE FINDING: the PROVENANCE TRAIL POINTS AT THE BRANCH WHOSE OWN COPY IS WRONG. A seat here can locate @93d126c4aa, confirm it establishes 'keep D4 on sitez until the project is done', and then read the superseded TODAY-ONLY row in the file that same commit was supposed to correct -- with no signal that the two disagree. An ordinary staleness is caught by checking the record; THIS ONE SURVIVES CHECKING THE RECORD, because the record is on the stale side. DISARM = the cross-fabric merge that carries CLOUD's row here; MSTR~Z holds the integrator role and the bridge. NOT ACTED ON BY THIS SEAT: DIRECTIVES.yaml is MSTR's sole-writer surface (the decomp's own ETFS-g-1 cell says so) and a placement row is a sovereign record -- I measure it and record it, I do not edit it. \u26a0 THE PRACTICAL EXPOSURE IS NARROWER THAN IT READS AND I AM SAYING SO RATHER THAN LETTING THE ROW CARRY MORE WEIGHT THAN IT EARNS: CTO~Z checked their own acts against it and none depended on the stale text -- no hand-back was planned, and /self-drive's completion test reads project STATUS, never the placement string. The correction changes confidence, not acts. The hazard is FORWARD-LOOKING: the next seat to spawn here, or any seat reasoning about whether D4 reverts at midnight, reads the wrong bound."
 },
 {
  "id": "ETFS_INGEST-Z-S25",
  "surfaced_by": "1.0.0_SA_CTO~Z",
  "surfaced_at": "2026-08-24T22:46Z",
  "one_line": "Three live keys in opal-data-portal-v2 share the leaf positioning_data.json -- one 244 days old sitting beside TWO live successors -- and TO-5 is standing up a fourth producer tonight: Rule 25's named same-leaf live/dormant hazard, in its key-migrated form.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Surfaced by CTO~Z; INDEPENDENTLY RE-CENSUSED at CVO~Z with an explicit token walk (not a --query over a page, per the banked pagination rule)",
    "DENOMINATOR: 4,070 keys materialised over 5 pages; leaf == positioning_data.json -> exactly 3, reproducing CTO~Z's figure",
    "json/positioning/positioning_data.json 8,133 B 2026-08-22 (Models side) \u00b7 platinum/etfs/positioning_data.json 76,149 B 2026-08-24 (D4's ETF variant, DE~Z's pinned baseline) \u00b7 positioning/positioning_data.json 49,950 B 2025-12-23, ~244 days",
    "MY FIRST POSITIVE CONTROL DID NOT FIRE (header_metrics.json = 0 in this bucket); re-run with a leaf drawn from the data itself -- manifest.json 112, metadata.json 110, outputs-manifest.json 108 -- which proves the extraction finds multi-occurrence leaves",
    "FRAMING MEASUREMENT, mine: 50 distinct leaves appear 3+ times in this bucket, so a 3-way leaf collision is ORDINARY here, not remarkable"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "notes": "\u26d4 MY FRAMING MEASUREMENT SHARPENS THE ITEM IN BOTH DIRECTIONS AND I THINK IT MATTERS: 50 LEAVES IN THIS BUCKET COLLIDE 3+ TIMES (manifest.json 112, metadata.json 110). So the finding is NOT 'a rare three-way collision' -- collision is the NORM here, and an item framed on the collision count would be framed on the unremarkable half. WHAT IS ACTUALLY SPECIAL is the AGE SPREAD WITH LIVE SUCCESSORS: one key 244 days old (past Rule 25's 90-day dormancy bar) sitting beside TWO live ones, which is exactly the KEY-MIGRATED signature Rule 25 says is BYTE-IDENTICAL TO ABANDONED FROM AGE ALONE. A dormancy sweep sees an old key; it cannot see that two successors exist. THE GENERALISATION THAT FOLLOWS: a leaf-name census is a BAD INSTRUMENT IN THIS BUCKET GENERALLY -- 50 leaves would give it a false hit -- so 'which producer owns positioning_data.json?' is a malformed question here and the answer must come from the producer side, never the key side. \u26d4 RECORDED, NOT DISPOSITIONED, and CTO~Z was right to say so first: DORMANT IS NOT A DELETION WARRANT (Rule 25) and moving served output is NEVER#3. Nobody touches the 244-day key on the strength of this. DISARM = making the triplet VISIBLE where a census would look (CTO~Z landed the table in the PRD s.12, which is this project's own served key's home) -- it converts a hazard you would meet DURING a deletion into one you meet WHILE READING, and that is the whole of it. ALLOCATION NOTE: CTO~Z nearly minted -Z-S24 and checked first, finding this seat had just taken it. Third seat tonight to check the high-water mark before allocating rather than after."
 },
 {
  "id": "ETFS_INGEST-Z-S26",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-08-24T23:02Z",
  "one_line": "NOT A DEFECT -- a dependency chain nobody has stated end to end: gold's as-of requires BOTH a silver/holdings partition AND a bbg/{date}/ landing for the SAME trading day, so tomorrow's 13:00Z gold fire is gated on tomorrow's ~11:00Z L1 fire, and an L1 failure steps gold back to 08-21 and leaves DIVZ/IDVZ as shells for another day -- looking exactly like tonight's correct output.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "etf_positioning_gold.py resolve_as_of :279-295 -- as_of comes from the DATA (newest silver/holdings partition), expected from the NYSE CALENDAR; two independent sources by design so the guard has an input that can make it fire",
    ":318-326 -- `silver has {d} but bbg/{d}/ has not landed -- stepping back one trading day`, and if no day qualifies it RAISES 'refusing to publish' rather than publishing a partial",
    "MEASURED NOW: silver/holdings/2026-08-24.parquet PRESENT \u00b7 silver/netassets/2026-08-24.parquet PRESENT \u00b7 bbg/2026-08-24/characteristics.parquet ABSENT \u00b7 bbg/2026-08-24/fund_daily.parquet ABSENT",
    "bbg/2026-08-24/ lands at tomorrow's 07:00 ET L1 fire (~11:00Z), before the 13:00Z gold fire",
    "Tonight's gold manifest confirms the resolution working: as_of 2026-08-21, expected_frontier 2026-08-24, trading_days_behind 1, all four inputs at 2026-08-21"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "\u26d4 FILED AS A NON-DEFECT, DELIBERATELY. The guard is CORRECT and well-designed -- it steps back rather than mixing tiers, and REFUSES rather than publishing a partial. Recording it because the CHAIN is what nobody has said out loud: A5's fix is not only about the universe derivation, IT IS THE PRECONDITION FOR GOLD ADVANCING. An L1 exit-61 tomorrow means no bbg/2026-08-24/, which means gold steps back to 08-21, which means DIVZ/IDVZ STAY SHELLS -- and the output would look IDENTICAL to tonight's: correct as-of, calendar resolved, trading_days_behind stated, guard working. THE FAILURE AND THE SUCCESS PRODUCE THE SAME-SHAPED ARTIFACT, and only the presence of bbg/2026-08-24/ distinguishes them. \u26d4 SO THE THING TO CHECK TOMORROW IS NOT 'DID THE SHELLS FILL' -- it is 'DID bbg/2026-08-24/ LAND', and the shells are downstream of that. A seat checking only the shells sees a null result with no cause attached. SEPARATION THAT MUST HOLD, and both 0.4.0_DS_ClientPlatform~Z and 0.0.0_AB_MSTR~Z drew it correctly before I did: tonight's gold partition date=2026-08-21 IS THE CALENDAR AS-OF and is NOT Z-S16. Z-S16 is a ROW-LEVEL substitution inside the silver 2026-08-24 partition; the gold as-of is a PARTITION-LEVEL calendar selection. Two different dates for two different reasons, and conflating them would manufacture a Rule-17 finding out of NEVER#1 working correctly. MSTR~Z retracted a Z-S16-reaches-gold claim on exactly this distinction."
 },
 {
  "id": "ETFS_INGEST-Z-S27",
  "surfaced_by": "1.0.0_SA_CTO~Z",
  "surfaced_at": "2026-08-24T23:25Z",
  "one_line": "The served payload carries NO field distinguishing 'this security has no such value' from 'we failed to fetch it' -- so a CORRECT null renders identically to a fetch failure, and it cost the sovereign a false defect report on his first smoke test.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Andrew-direct ~23:2xZ on his own visual smoke, VERBATIM: 'kind of patchy response on yield column, have most of it but missing key ones like Amazon AMZN for example'",
    "CTO~Z measured the payload before routing; RE-DERIVED at CVO~Z on the live served artifact: 114 holding rows, yield populated 80, null 34",
    "The 34 nulls are AMZN BA AMD MNST SNDK PLTR CIEN INTC CNC TSLA INCY ANET FTNT LITE -- overwhelmingly NON-DIVIDEND-PAYERS, so the nulls are CORRECT",
    "MARKER-FIELD CENSUS on a holding row: candidate fields matching status/reason/exception/error/missing/source/quality/flag = NONE. A null row's non-null fields are only active, asset_class, aum, beta, name, returns, sub_asset_class, ticker, weight",
    "So there is no in-payload way to tell a true zero from an absent measurement"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "notes": "*** \u26d4 CORRECTION 23:30Z TO THIS ROW'S OWN ADJACENT NOTE (b), AND IT IS MINE: I wrote 'PERFORMANCE IS A REAL AND TOTAL GAP... a BUILD, not a fix', relaying a routed classification WITHOUT MEASURING IT. IT IS NEITHER A BUILD NOR A DEFECT. 0.4.0_DS_ClientPlatform~Z measured before building and I re-derived it here: history_topup IS FEEDING -- 2 landings, bbg/2026-08-20/history_topup.parquet 5,579 B and bbg/2026-08-21/ 5,563 B, over a COMPLETE 23-object enumeration of bbg/ (NextToken absent). And the producer's own docstring at load_history :363-368 documents the outcome AT BUILD TIME: 'Returns beyond 1D need a series... With ONE landing present only 1D is derivable and every other window is null -- CORRECTLY, and it UPGRADES FORWARD with no code change as partitions accumulate.' 1D needs 2 points and we have 2; WTD needs a week, 1M ~21 sessions, 1Y a year. SO 0/114 ON THOSE WINDOWS IS THE DESIGNED, CORRECT OUTPUT OF A TWO-DAY SERIES -- the same upgrades-forward property as the DIVZ/IDVZ shells, on a different axis. Andrew's ask needs a BLOOMBERG BACKFILL, which is a SPEND CALL, not a producer fix -- a completely different decision from the one my relayed sentence would have started. *** THE FAILURE IS MINE AND IT IS THE RELAYER'S: I forwarded a CAUSAL claim ('the leg is NOT FEEDING') with no grounding attached, to five seats, ROUTED AT THE SEAT WHO WOULD HAVE DONE THE WORK -- in a session where I have said repeatedly that the relayer owns the grounding or owns the caveat. DS~Z measured instead of building, which is the only reason it cost nothing. *** \u26d4 IT HAS ALREADY FIRED, ON THE SOVEREIGN, ON HIS FIRST LOOK. His observation was ACCURATE -- the column IS patchy and AMZN IS blank -- and his attribution was THE ONLY ONE THE PAGE PERMITS. A page that renders a correct value identically to a failure does not merely risk a wrong conclusion; it makes the wrong conclusion the reasonable one. THE COST IS ALREADY PAID: a sovereign smoke-test defect report against a working field, and whatever effort it would have drawn had CTO~Z not measured the payload before routing it. \u26d4 THIS IS THE SAME SHAPE AS Z-S12 ONE LAYER OVER: there the colour channel rendered UNDIFFERENTIATED and could not be distinguished from a styling gap; here a null renders UNQUALIFIED and cannot be distinguished from a fetch failure. BOTH ARE THE PAGE FAILING TO CARRY THE PROVENANCE OF WHAT IT SHOWS, and both were invisible to every non-render instrument -- a grep, a schema check and a row count all pass on a payload that misleads a reader. REMEDY IS A DISPLAY/SEMANTICS ACT, NOT A DATA FIX: the data is correct. Either the payload carries a reason marker per null, or the page renders 'n/a' distinctly from blank. NOT MINE TO DESIGN -- it is a DE-class cell and a Rule-24 value act if a marker enum is minted. NOTE THE ADJACENT RECLASSIFICATIONS FROM THE SAME SMOKE, both CTO~Z's and both worth keeping separate from this one: (a) DIVZ/IDVZ show 'no HOLDINGS', not 'no data' -- book-level yield/cost/beta/aum ARE present, and only the holdings half waits on tomorrow; (b) PERFORMANCE IS A REAL AND TOTAL GAP -- 1D populated 109/114 and every other period 0/114, so the producer computes one day and nothing else. (b) is a BUILD, not a fix, and is genuinely what he saw."
 },
 {
  "id": "ETFS_INGEST-Z-S28",
  "surfaced_by": "1.0.0_SA_CTO~Z",
  "surfaced_at": "2026-08-24T23:31Z",
  "one_line": "Holdings arriving is NECESSARY AND NOT SUFFICIENT: the Bloomberg characteristics join covers 109 tickers and misses 21 of DIVZ's 29 and 41 of IDVZ's 44, so tomorrow the books flip from HONEST SHELLS to FULL-LOOKING BOOKS with real issuer weights and blank analytics.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "Surfaced by CTO~Z, confirmed by DS~Z at the join (their code), RE-DERIVED at CVO~Z on bbg/2026-08-21/characteristics.parquet",
    "characteristics: 109 rows / 109 distinct tickers. AAPL present; BBSEY, AMX, CPA, BNPQY, 2602335D ALL ABSENT",
    "FORWARD JOIN TEST against silver 2026-08-24: DIVZ 21 of 29 holding tickers have NO characteristics row; IDVZ 41 of 44; PFDE 3 of 90 (2602335D, Cash&Other, FXFXX); PFOE 2 of 24",
    "TOTAL: 64 of 169 distinct holding tickers in the 08-24 partition are missing from the characteristics corpus",
    "DS~Z at source, the row builder: name/weight/shares/price/market_value/cusip/is_cash come from the HOLDINGS row; only yield/beta/aum/domicile/sub_asset_class are conditioned on the join; geography falls back to the literal 'Other'",
    "POPULATION SPLIT, CVO~Z 2026-08-24T23:37Z: A5's deployed expression over the 08-24 partition yields a 166-ticker universe containing BBSEY/AMX/CPA/BNPQY/AZN/BKRKY/BP (all True); the ONLY ticker failing first-char-isalpha is 2602335D, and Cash&Other + FXFXX are excluded as is_cash -- so 3 of the 64 are permanent by design and ~61 are answered by tomorrow's pull"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "1.0.0_SA_CTO~Z",
  "notes": "*** TONIGHT'S CAUSE IS SINGULAR AND CERTAIN, and this row is NOT it -- 1.0.0_SA_CTO~Z corrected their own 'second cause' framing and I confirmed the file at this seat: silver/holdings/2026-08-21.parquet, the partition gold's own manifest names as its input, contains 114 rows -- PFDE 90 + PFOE 24, source=filepoint 114/114, TRUESHARES ROWS ZERO. That partition was written FRIDAY; F2's remediation went live at 20:31:09Z tonight and the FIRST partition that has EVER contained DIVZ/IDVZ holdings is 2026-08-24, written 22:00:17Z. GOLD READS T-1 = FRIDAY AND FRIDAY'S FILE PREDATES THE CAPTURE. That is the whole cause of tonight's empty books: not a join failure, not an identifier problem, not a mapping gap. *** SO THIS ROW IS A FUTURE RISK, NOT A PRESENT CAUSE, and it was filed that way -- its one_line says 'TOMORROW the books flip' -- but the distinction is worth stating explicitly here so nobody reads the 64-missing figure as an explanation of what Andrew saw tonight. \u26d4 AND I HAD THE DECISIVE MEASUREMENT IN HAND TWENTY MINUTES BEFORE THE QUESTION WAS ASKED: I read this exact file at 23:23Z for the Z-S3 denominator subset check and recorded '114 rows | PFDE 90, PFOE 24'. I HAD THE FACT AND NEVER APPLIED IT TO THIS QUESTION, because I took it for a different purpose. CTO~Z's method is the one that found it -- OPEN THE FILE AT THE POINT OF FAILURE RATHER THAN REASON FORWARD DOWN THE CHAIN -- and a measurement already sitting in your own notes is worth nothing until someone asks it the right question. *** *** THE 64 IS NOT ONE POPULATION -- MEASURED AT THIS SEAT ON MY OWN EVIDENCE, because Z-S28 rests on the claim that tomorrow's pull will REQUEST these names. Running A5's deployed expression against the 08-24 partition yields a 166-ticker universe, and ALL SEVEN ADRs I tested are IN IT: BBSEY, AMX, CPA, BNPQY, AZN, BKRKY, BP all True. So the claim holds and tomorrow's request is real. \u26d4 BUT THE FILTER EXCLUDES EXACTLY THREE, PERMANENTLY, AND THEY ARE A DIFFERENT POPULATION: `2602335D` (TPG) is THE ONLY ticker failing the first-char-isalpha test, so it is STRUCTURALLY EXCLUDED FROM THE UNIVERSE AND CAN NEVER RECEIVE CHARACTERISTICS -- not tomorrow, not ever, until it has a usable ticker; and `Cash&Other` + `FXFXX` are excluded as is_cash=True, correctly. SO THE SPLIT IS: ~61 names that WILL be requested tomorrow (an OPEN question answered by the ~11:00Z pull) + 3 that are excluded BY DESIGN and are a CLOSED question. A count of 64 read as one number would put a permanent condition and a one-day unknown in the same bucket, and would make tomorrow's result look worse than it is by exactly 3. *** AND THE TPG EXCLUSION IS CORRECT BUT COMPOUNDS Z-S27 PERMANENTLY: that row renders with real issuer name, weight, shares and price and PERMANENTLY-BLANK analytics, indistinguishable from a fetch failure, on every future day. It is the one row for which Z-S27's remedy is not optional -- there is no future state in which its blanks become values. *** \u26d4 THE MECHANISM, WHICH MATTERS MORE THAN THE COUNTS AND IS NOT 'BLOOMBERG LACKS THESE NAMES': today's characteristics were pulled for a universe DERIVED FROM THE 08-21 PARTITION, which contained ZERO TrueShares rows (114 filepoint only). The pull never ASKED for the ADR tickers. Tomorrow's L1 fire derives its universe from the 08-24 partition, which DOES carry them -- and I measured earlier that A5's fixed expression yields 72 of 72 TrueShares tickers into the universe. SO TOMORROW'S PULL WILL REQUEST THEM FOR THE FIRST TIME, and the open question becomes whether Bloomberg RESOLVES them: PRD F8 flagged exactly this -- IDVZ's rows are bare US-listed ADR tickers and the derivation appends ' US Equity', which resolves the ADR line rather than the local line. TONIGHT'S 109 IS NOT EVIDENCE THAT IT WILL FAIL; IT IS EVIDENCE THAT IT HAS NEVER BEEN TRIED. Recording that distinction because '41 of 44 missing' invites the conclusion that the names are unavailable, and the measurement does not support that. \u26d4 WHAT IS ARMED IS THE RENDER STATE IF THE RESOLUTION PARTIALLY FAILS: the issuer half renders regardless, so a row with no characteristics is NOT blank -- it carries a real name, weight, shares, price and market value with null yield/beta/aum/sub_asset_class and geography 'Other'. THAT IS STRICTLY WORSE FOR A READER THAN A SHELL, because a shell announces itself (num_holdings 0, an explicit not-available notice) and a full-looking book with blank analytics does not. AND IT COMPOUNDS Z-S27 EXACTLY: those blanks are indistinguishable from fetch failures, so the condition that already produced one sovereign false defect report would scale from 34 nulls to potentially ~64 more. DISARM = tomorrow's characteristics pull is READ FOR ADR COVERAGE BEFORE the 13:00Z gold fire consumes it, not after -- the L1 fire at ~11:00Z leaves a two-hour window in which the question is answerable and cheap."
 },
 {
  "id": "ETFS_INGEST-Z-S29",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-08-25T00:06Z",
  "one_line": "THE PROVENANCE CHAIN BREAKS AT THE GOLD TIER, NOT AT SILVER: etf_positioning_gold.py stamps data_as_of from the RUN'S as_of (the partition name) and NEVER READS silver's row-level data_as_of column at all -- so TO-7's silver fix cannot reach the served surface, and Andrew's 'maintained from bronze ingestion onward' is unimplemented at the layer the page actually reads.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "SOURCE, etf_positioning_gold.py @ working tree (886 lines): :646 book row '\"date\": as_of' and :649 '\"data_as_of\": as_of'; :604 holding row '\"date\": as_of'. All three take the RUN-level as_of returned by resolve_as_of(), which is the newest silver PARTITION NAME having both a silver file and a bbg landing.",
    "CENSUS: 'data_as_of' occurs EXACTLY ONCE in the entire gold file (:649) and that occurrence is a WRITE. 'as_of_basis' occurs ZERO times. So gold neither reads the provider value nor the basis TO-7 is adding.",
    "POSITIVE CONTROL (this is the control that makes the absence meaningful): gold DOES read silver holdings columns by name -- holding_ticker :591, is_cash :597, security_name :607, cusip :608, weight_pct :611, market_value :612, shares :613, price :614. Eight columns read; data_as_of is not among them. The absence is a real absence, not 'gold reads nothing from silver'.",
    "SINGLE-PARTITION READ, :738-739: holdings = _read_parquet(ETFS_BUCKET, SILVER_HOLDINGS + '/' + as_of.isoformat() + '.parquet'). ONE file per run.",
    "LIVE ARTIFACT, opal-data-etfs gold/book/date=2026-08-21/book.parquet read 2026-08-25T00:0xZ: all four books carry data_as_of = 2026-08-21 == the run as_of. DIVZ book_only 0 \u00b7 IDVZ book_only 0 \u00b7 PFDE full 90 \u00b7 PFOE full 24.",
    "LIVE ARTIFACT, gold/holding/date=2026-08-21/holding.parquet: the ONLY date-ish column is 'date', single-valued 2026-08-21. No provider-derived as-of exists anywhere in gold's output.",
    "SERVING HOP (measured by 2.0.0_SA_COO~Z at 23:57Z, relayed not re-derived here): etfAdapter.ts:131 as_of_date: book.data_as_of -- so the page's date IS the gold book field, which is the run as_of.",
    "BRONZE VALUE (measured by 1.0.0_SA_CTO~Z and 2.0.0_SA_COO~Z, relayed not re-derived here): tonight's TrueShares bronze CSV carries Date = 8/24/2026 on every row."
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "notes": "ROUTING: OPEN -- routed same-turn to the ISSUER (2.0.0_SA_COO~Z) as a BLOCKING spec input on ETFS_POSITIONING.TO-7, and to 1.0.0_SA_CTO~Z because it changes the stated stakes of the AC3 ruling. NOT an instruction to stop any build.  ||  WHAT THIS DOES NOT SAY: it does NOT say TO-7 or the re-derive are worthless. Silver's row-level data_as_of is wrong and Rule 17b makes silver correctness law in its own right; INGEST-T3-3's tie-out reads silver directly. It says the SERVED provenance does not traverse that field, so the 13:00Z clock does not apply to it.  ||  CONSEQUENCE FOR TOMORROW, both branches, and the scenario everyone is sequencing against is in NEITHER: (A) bbg/2026-08-24/ LANDS -> as_of = 08-24 -> gold reads the 187-row partition -> all four books FULL, served data_as_of = 2026-08-24, which MATCHES the provider's own bronze Date of 8/24/2026. Correct. (B) bbg does NOT land -> as_of steps back to 08-21 -> that partition contains ZERO TrueShares rows -> DIVZ/IDVZ are book_only shells again, exactly as today. Nothing is mislabelled because there is no data present to mislabel.  ||  THEREFORE the premise 'per-fund as-of without the re-derive ships DIVZ/IDVZ MORE VISIBLE AND STILL WRONG, labelled 2026-08-21 on data captured 08-24' cannot occur on the served path: under (A) the label is 08-24 and right; under (B) there are no holdings under any label. The ordering ruling built on it (land the re-derive, not the per-fund as-of) rests on a hop the served path does not make.  ||  WHY TODAY'S CORRECTNESS IS A COINCIDENCE AND NOT A DESIGN: gold's as_of is the INGESTION date; the provider's as-of is the SHEET's Date. They coincide today because the sheet was current. TrueShares is a POINT-IN-TIME export -- the first day the sheet is stale on a fetch day, the partition is named D while the sheet says D-1, and gold serves D. That is Z-S16's substitution defect one tier up, untouched by TO-7 and by the re-derive.  ||  SPEC DEFECT IN TO-7 AS CUT, and this is the actionable half because DS~Z begins the producer now: POS-TO7-AC1 reads 'Each book resolves and renders its OWN latest available holdings, with its own data_as_of' and its worked example is 'DIVZ/IDVZ @ 08-24' -- a PARTITION date. The TO's rationale at :133-135 says 'one date per book, FROM THE PROVIDER, shown.' A build that gives each book its newest PARTITION date SATISFIES AC1 AS WRITTEN and does not implement the ruling. Criterion and rationale disagree; the criterion is what gets built.  ||  CLASS: this is Rule 24(iii) inside a criterion's wording -- the axis measures 'per-fund' and the adjective 'its own data_as_of' silently permits a partition-derived value. Same shape I have banked four times; the cross-value test passes because every book would correctly get its own date.  ||  WHY NO INSTRUMENT CAUGHT IT: 0.4.0_DE_ClientPlatform~Z scoped the remedy to bronze->silver by diffing two platinum versions (2,384 leaf fields, one differs) and finding data_as_of UNCHANGED, concluding the serving layer already implements the contract. A diff between two runs OF THE SAME CODE cannot reveal that the code's DERIVATION is wrong -- both versions carry the same wrong-derivation value. An instrument that could not have said otherwise (Rule 22a). The field has the right NAME and the wrong SOURCE.  ||  DISARM (owner COO~Z, same-turn): amend POS-TO7-AC1 so the per-book value is the PROVIDER's as-of carried from the row, with an exercised criterion on a fixture where the partition name and the provider Date DIFFER -- the same discriminating-fixture standard DS~Z already met on INGEST TO-7 AC6. Without that fixture the criterion cannot fail, because they coincide today.  ||  REMEDIATION (separate clock, separate owner, per the two-state rule): gold must read the row-level data_as_of/as_of_basis TO-7 is adding. DISARMED != REMEDIATED."
 }
]
```

---

## 4. DENOMINATORS FOR THIS DOCUMENT

- Items: **28** (1 dismissed, 3 under investigation, 17 graduated). ARMED: **11** (Z-S1, Z-S4, Z-S5,
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

⛔ **THE ITEM COUNT CANNOT SEE A CLOSURE, AND I HAVE BEEN QUOTING IT ALL NIGHT.** Measured 2026-08-24
~22:38Z against `origin/SITEZ`: **origin 23 items, local 23 items — the counts MATCH** — while two
items' notes differ by +1,032 and +1,734 characters (`Z-S22`'s DISARMED+REMEDIATED close and
`Z-S3`'s issuer-side attribution). **Both are content edits to EXISTING items, so the denominator is
structurally blind to them.** A reader comparing item counts across the two refs would conclude the
channel is in sync while a BLOCKING closure and a remedy-ownership finding sat only on one side.
**State this document by `(item count, commit-ish)` — never by the count alone**, which is this
round's own unstamped-denominator lesson pointed at the instrument I report with.


## 5. WHAT THIS DOCUMENT DOES NOT DO

It does not certify COO~Z's stage-3 decomp -- that is a separate act by this seat against the
four-postulate record, the bidirectional cell<->criterion alignment with printed denominators, and
whether each cell's premise oracle actually RAN rather than was written. The decomp carries
UNCERTIFIED on its face until that cert lands. It does not rule any of the s.5 row conventions
(decomp cells), does not move any tension's decider, and cuts no TO.

-- `3.0.0_SA_CVO~Z`, channel owner and certifier of record, 2026-08-24
