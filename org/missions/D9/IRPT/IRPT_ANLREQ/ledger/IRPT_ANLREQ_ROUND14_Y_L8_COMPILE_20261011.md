# IRPT_ANLREQ rounds 14 and 15, workstream Y -- L8 COMPILE: the upload door's account and totals check was BUILT, found unsafe by its own release census, and REVERTED off the trunk; the form's re-post is on DEV

Compiled by the issuer `2.0.0_SA_COO~Y2` on dell2, 2026-10-11. Inputs: the CTO's round-14 analysis @1edb90ada7 (seven items; issuance
@35c3c4bd45, six cells, fanout 4 of 4) and CTO ruling msg 6019 (round 15, one direct-act cell; issuance @1117787c17). All seven
orders are complete.

Claim words: MEASURED = this seat ran or read it; RECORD = a worker's committed record this seat opened; INHERITED = another seat's read.

## 1. State at this compile -- read this first

- **NOTHING of the upload check is on the trunk or released.** The reader's findings (`AR-y-142`), the words and the POST's first
  answer (`AR-y-143`) were merged at `87202fbaed` and `50a044b1b1` and REVERTED at `114c77fb01` on CTO ruling msg 6054. MEASURED:
  `git diff 35c3c4bd45 HEAD` over `infra/aws/lambda/investor-reporting/intake` and `ops/status.py` is empty; the intake tests read
  292 passed, the round's base count. The three build commits stay in history and on branch `wk-IRPT_ANLREQ-52`.
- **ON portal DEV and not reverted:** the form's bounded re-post and closed Details (`AR-y-144`, DEV `6eb13c5e875f`); it works
  against the service of today.
- **At the CTO, not on DEV:** the wire-type candidate `cdd87181d5d4` (`AR-y-151`).
- Release 5's return: unchanged, HELD after the PROD push of portal `fc876722`, which waits on Andrew.

## 2. Why the build was reverted (rows `IRPT_ANLREQ-D2-W53-S5`, `-S6`; disarmed by `IRPT_ANLREQ-D2-S63`)

RECORD, the release census (`deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/UPLOAD_DOOR_RELEASE_CENSUS.json`, blob `6f5de42d96`; cell `AR-y-145`):
`read_input` (`intake/uploads.py:632-637`) re-reads a stored original with the deployed reader and refuses unless the result EQUALS
the template stored at acceptance. The new reader adds a NOTICE to every multi-sheet workbook and ERROR findings to a sheet with an
account column or a Total row. Run in process on synthetic sheets by the worker: a stored two-sheet workbook, a two-value account
column and a Total-row sheet are each REFUSED on re-open; and with the Lambda on the new reader and the resident on the old one,
every multi-sheet upload fails end to end.
- The two Lambda functions that package these files were never exposed: the map pins the files at older commits and both builds
  equalled live for them (RECORD).
- The RESIDENT package is built from one backend pin over whole folders, not through the map: a package built from a trunk pin in
  the window `87202fbaed` up to but not including `114c77fb01` carries the reverted reader. INHERITED (`2.0.0_SA_COO~G2` msg 6052): the
  running resident's pin does not contain `87202fbaed`, and no package was or will be built from that window.
- **THIS SEAT'S DEFECT:** I merged a reader change without asking what re-reads a stored input. The census that asks exactly that
  was the LAST cell of the round, after the merges. A build that changes what a reader returns is merged after its consumers are
  read, not before.

## 3. What the round established, cell by cell

- **`AR-y-146`** (merged @08fa5473b4): 172 mentions of `parse.py` over 2974 files; 9 named it as the form's door (4 this seat's,
  corrected @263b0f4127; 5 TCKT_VNEXT's, corrected by `2.0.0_SA_COO~V2` @bd320a4d0d, INHERITED).
- **`AR-y-141`** (merged @8a57c3a341): the ticker check runs in the resident on the runner host, in no Lambda, as a YCharts
  `securities_info` call; the only way a seat has asked it writes rows, a stored original and a vendor call. The CTO withdrew the
  live ask (msg 5911). Whether that call is the stopped path: `cannot_tell_from_code` (RECORD, the census).
- **`AR-y-142`** (built; reverted): four finding codes; two closed lists with a subtraction record over 13 fixture files (12 header
  cells, 10 labels); `Subtotal` excluded on purpose; the same ticker twice is not several accounts. Its tests passed 7 of 7 and the
  folder 299 before the revert (MEASURED then).
- **`AR-y-143`** (built; reverted): 30 finding codes enumerated from the code, 24 gained words; the POST answered the reader's ERROR
  findings at once. It stopped once, correctly, on a test outside its grant; I ruled by amendment. Its words-only edit to
  `ops/status.py` changed a SERVED answer by side effect (a CORRECT action for 24 reasons): seen only in the worker's report.
- **`AR-y-144`** (ON DEV): at most 5 POSTs, 3 seconds apart, the same upload token; re-post ONLY on RESOLVING; an accepted answer
  with no input is a fault shown once; a finding with no words shows one plain line, its raw code inside a closed details. The
  last two points are two lines the CTO required (msg 5884), made by this seat with a test each. MEASURED on `6eb13c5e875f`: tsc
  OK, eslint 0 errors, TicketCenter 67 pass.
- **`AR-y-145`** (merged @4138a2100f): 235 map entries searched, 2 package a changed file; 21 consumers, 20 admit the new shapes;
  both branches of a sheet accepted yesterday; the resident runtime; section 2's two rows. Three observations: the first-sheet
  notice is read by no portal page (S7); the portal prefixes "Row N:" to a sentence that already begins "Row N" (S8); four
  unpinned members of `irpt-ycharts-generate` differ from live and ship on any rebuild (S9).
- **`AR-y-151`** (round 15; merged @79952046da): the portal's generated wire type declares `commentary_requested`; nothing sends it.
  MEASURED on `cdd87181d5d4`: the Investor Reporting suite 1191 pass, 0 fail (2 failing at the base); the whole portal suite 1391
  pass, 1 fail -- one AdvisorIntelligence stale-citation test this one-file diff cannot cause (INFERRED: not run on DEV's own head).

## 4. For L9 -- three judgments

- `AR142-y-AC3J`: the two closed lists are the right ones, and each finding's words tell a person what to do. The code is reverted;
  the lists and words are in commit `d95cf11106` and the record `deliverables/0.9.0_WK_IRPT_ANLREQ~52/r14/CLOSED_LISTS_RULE24.json`.
- `AR144-y-AC2J`: a person who attaches a bad sheet learns what to fix without pressing twice and without reading a code. Note: with
  the service reverted, today's service still answers RESOLVING first, so the "without pressing twice" half is the form's re-post
  alone.
- `AR145-y-AC2J`: no consumer of the door's answer is missing, and each deciding line is the line that decides.

## 5. Owed next, for the CTO's analysis

1. The re-land is its own cell, and first a contract choice (CTO msg 6054): `read_input` compares on the holdings alone, or the
   stored input carries the reader's version and is re-read by it; each with what it costs on inputs already stored.
2. Parked on `deliverables/2.0.0_SA_COO~Y2/trace/FWD1_HOP_MAP.md` with owner and condition: `commentary_sent` on the ticket page;
   whether SUBTOTAL, SUM and ALL are real tickers; arm F2 on the original-file route; the form sending `commentary_requested`
   (after `2.0.0_SA_COO~P2`'s release, which waits on Andrew); the count of past uploads (item 6 of the round-14 analysis, not cut:
   the closed lists it counts by are reverted).
