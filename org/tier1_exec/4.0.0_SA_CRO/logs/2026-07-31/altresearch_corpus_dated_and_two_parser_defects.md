# OPAL_ALTRESEARCH: full transcript corpus ingested, structured and DATED -- plus two parser defects my own verification caught

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, TRACE

**Agent:** 4.0.0_SA_CRO (Chief Research Officer, Tier-1)
**Window:** 2026-07-31 ~19:37Z (session start) -> ~22:00Z
**Commits:** `6e3072b3e3`, `785eccd5f1`, `06d8db746c` (all authored 4.0.0_SA_CRO)

---

## Summary

Startup protocol completed (the predecessor session's was pre-empted mid-sequence by Andrew's
commission and left outstanding). Then the whole session was one thread: Andrew obtained the
Research Team Meeting back catalogue and asked for it structured and timestamped.

Delivered: 28 transcripts landed byte-faithfully, structured to schema 1.1, **dated 28 of 28
with a worst residual of 5 seconds**, indexed, and the alt-data build queue rebuilt over the
complete text.

The substance of the session is not the ingest -- it is that **three of my own instruments were
wrong, and each was caught by a control rather than by care.** Two were parser defects silently
discarding most of the corpus; one was a verdict I published and had to retract.

---

## What landed

**1. Corpus (`6e3072b3e3`).** 30 `.vtt` downloaded by Andrew; **28 UNIQUE** -- two byte-identical
duplicate pairs found by md5. Ingesting by filename would have double-counted two meetings; the
filename count was never the denominator. Landed byte-faithfully (0 mismatches on re-hash after
write) with a manifest recording every source file including the skipped duplicates.

**2. Dating (`06d8db746c`).** `index/meeting_calendar.tsv` -- 29 occurrences with date and
recording duration, transcribed from the Teams recap cards Andrew screenshotted. A transcript's
LAST CUE equals its recording duration to within seconds.

**Duration alone is NOT sufficient, and that is the load-bearing detail:** 2026-04-15 and
2026-06-18 both ran **1h3m22s to the second**, and greedy nearest-match split that tie
BACKWARDS. `bin/ingest_corpus.py` therefore runs a monotonic DP combining duration residual with
Andrew's stated download order (newest-first, backward), allowing a meeting to be skipped.
Duration and order are jointly sufficient where neither is alone.

Three anomalies resolved coherently, which is the actual corroboration:
- the two-GUID file is **2026-05-12** -- the meeting Teams split into TWO recordings;
- **2026-07-13** is a real meeting with NO downloadable transcript (29 meetings, 28 transcripts);
- the 12-minute chain break that defeated my earlier attempt WAS that missing meeting.

Every record carries `date_basis` plus the residual that earned it. **The dates are DERIVED, not
observed** -- a reader can audit the inference instead of inheriting it.

**3. Build queue.** 63 of 166 securities discussed; 13 of the top-20 firm positions. Top: UNH
3.019%, PM 2.609%, MPLX 2.250%, CVX 2.118%, NVDA 1.905%. Most-discussed: MSFT and ServiceNow in
17 of 28 meetings; ASML 94 mentions across 13. False positives are adjudicated IN the artifact,
and the check cut both ways: `CI` REJECTED (a transcription fragment of MSCI), `RTX` SURVIVED
against my expectation ("train technology is GE, Rolls-Royce ... we got RTX" -- aerospace peer,
not a graphics card), `UBS` LOW (a research source, not a position).

---

## The three things I got wrong

**(a) A verdict published, then retracted (`785eccd5f1`).** I declared duration-matching REFUTED
as a dating key. It was not. TWO of my own measurement bugs, stacked: I took the trailing
"Recording has been saved to OneDrive" notice as the meeting END (it posts ~9 min late -- 07-31
ended 10:42, saved 10:51), inflating every duration and inventing an offset that does not exist;
then I measured VTT length as last-cue MINUS FIRST-cue, discarding the opening silence when the
recording clock starts at zero. I read the wreckage as a property of the METHOD rather than of my
instrument. **The tell was available and I walked past it** -- the recap says 1h17m23s and the
video 1h17m19s while I was asserting an 8-minute systematic gap. Andrew's screenshot falsified
it; nothing internal would have.

**(b) A circular anchor.** I assigned 07-27 by best fit, then derived the offset FROM that
assignment and reported it as corroboration. Self-caught, but only after it had already shaped a
conclusion.

**(c) A script that printed a conclusion its test did not produce.** My falsification harness
emitted "Only ONE alignment survives" while its own output showed three did. A hardcoded string,
not a measurement -- exactly the instrument-that-cannot-fail class.

**Two parser defects, both mine, found by verifying rather than shipping.** Teams wraps a long
cue across two lines; a single-line `<v ...>...</v>` regex cannot match it.
1. In the ingester: 16,402 continuation lines dropped, plus a phantom "UNATTRIBUTED" speaker that
   was really just wrapped dialogue. Now 0 dropped.
2. **The worse one:** `build_mentions.py` re-parsed raw `.vtt` with the same regex and dropped
   those cues ENTIRELY. Fixing the ingester alone would have left this lying, still emitting a
   confident and WRONG build queue.

**STATE WHAT THE NUMBER IS *OF* -- the two axes disagree and the smaller one misleads:** 14,441
vs 20,266 utterances is **29% fewer UTTERANCES**, but 250,844 vs 1,274,499 characters is **80%
fewer CHARACTERS**. The wrapped cues ARE the long ones, so the broken path kept the short
interjections and lost the content. Quoting the utterance delta alone would have made an 80%
blind spot sound like a rounding error. Measured consequence: coverage 44/166 (26.5%) ->
63/166 (38.0%); top-20 discussed 10 -> 13.

---

## Grounded finding: the m365 gateway (routes to CTO, architecture)

Andrew disbelieved my first claim, correctly -- it was too strong as stated. Teams meeting
timestamps ARE retrievable and I used them. What is missing is **paging depth, not data**:

- `read_chat_messages` (`infra/aws/ec2/m365-mcp-gateway/app/tools.py:592-595`) takes only
  `chat_id` and `top`; Graph caps `top` at 50; the gateway contains **no** `skiptoken`/`nextLink`
  handling and no generic passthrough. That is why chat-derived dates stop at 2026-07-06.
- Its `$select` omits `eventDetail`, which carries `callDuration`/`callEndTime` -- the fields
  that would make dating EXACT rather than inferred. **Same class as the `attachments` omission
  at `tools.py:597` found last session: the data exists and is dropped at the query layer.**
  Second instance, so it is a pattern, not a one-off.
- A folder shared into "Shared with me" is **structurally unreachable**: only `/me/drive` and
  `/sites/{id}/drive` are built (`app/ms_ingest.py:12`, verbatim: *"(/sites, /sites/{id}/drive,
  /me/drive) are reachable; nothing else"*), and no tool accepts a user/drive id.

Consequence: ongoing ingest stays OPERATOR-PACED (Andrew downloads, CRO ingests). Routed to CTO's
architecture gate, **not** direct to an AE lane -- repeating last session's wrong-door mistake
once was enough.

---

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-which` | A.3 startup exercise (resolution is not execution) | **PASS** -- 94/94 resolve bare AND a forwarder actually RAN (produced its banner) |
| `comp-grep` | locate the m365 gateway source for the endpoint census | **PASS** -- but see gap: the on-rails hit came only after `find`; earlier attempts surfaced `.fedobs_tmp/` derived JSON |
| `.tools/commit-gate.sh` | mandatory pre-commit on 2 new `.py` | **PASS after 2 real BLOCKS** -- E702 (semicolon statements) and the E402 docstring-after-`__future__` trap. Genuine catches |
| `.tools/safe-commit.sh` | 3 commits | **PASS** -- risk-reflex REFLEX CLEAN, denominator printed (4 files vs 1622 danger nodes) |
| `comp-surface-check` (via safe-commit) | critical-surface screen | **PASS** -- no critical surface touched |
| `python .tools/audit-archive-invoker.py` | startup A.2 | **rc=1, 2 findings** -- snapshot deferred (CRO not GOVERNANCE_AUDIT-permitted, expected); flagged an uncovered audit log + a 30.2h stale baseline |

**What worked:** the commit gate earned its keep twice on real defects. More importantly, the
*verification steps I chose to run* -- re-hashing after write, counting dropped lines, printing
the speaker distribution -- are what exposed the two parser defects. None of them was required.

**What failed:** nothing in the toolchain. The failures this session were all in instruments I
wrote myself, which is the point.

**Gap found (repeat, still unrouted):** no comp-tool answers "where does fund X's constituent
holdings data live" -- logged last session, unchanged. New this session: **no instrument in the
estate can tell you whether a parser is silently discarding input.** Both parser defects were
found by hand-checking a count I had no obligation to check. That is care, not a control.

---

## MCP traffic

3 messages, all inbound and already handled. `check_inbox` empty at startup; the one unread
(`0.0.0_AB_MSTR`, 142258Z, grant landed `0e696c4ebd` / LD-0366) was answered by the predecessor's
commit. Nothing owed out. `/watcher` armed Monitor `b0eilflh0`, confirmed `running` via
`TaskOutput` -- the only probe that observes a consumer.

---

## Blockers

**None.** Two residuals, neither blocking:

- **2026-07-13** has no downloadable transcript. Its calendar row is already in place if it can
  be retrieved.
- **2026-05-12** is dated `LOW-NO-DURATION`: its recap card shows "2 recordings" with no single
  duration, so it was placed by ORDER alone and the second recording was never downloaded.

---

## Current State

`OPAL_ALTRESEARCH` is active, owner `4.0.0_SA_CRO`, Phase 1 COMPLETE. Everything below is on
CLOUD, committed, tree clean; **not pushed** (lanes commit, integrators push).

`C:\Users\AndrewBerman\Desktop\ajb_workspace\research_transcripts\`:
- `bin/ingest_corpus.py` -- block-wise VTT parser + monotonic-DP dater. `--apply` writes; bare
  run is a dry run reporting the alignment.
- `bin/build_mentions.py` -- reads `structured/` ONLY (never raw `.vtt`); emits the build queue.
- `bin/ingest_transcript.py`, `bin/ingest_vtt.py` -- predecessor parsers, superseded for corpus
  work by `ingest_corpus.py`; **both still carry the single-line-cue defect and must not be
  reused without the block-wise fix.**
- `index/meeting_calendar.tsv` -- 29 occurrences, operator ground truth, the dating key.
- `index/transcripts.jsonl` -- 28 rows, 2026-04-07 -> 2026-07-31.
- `structured/RT-YYYYMMDD-HHMM.json` -- 28 docs, schema 1.1, 20,266 utterances, 1,274,499 chars.
- `raw/{date}/RT-YYYYMMDD-HHMM.vtt` -- 28 byte-faithful raws + `raw/MANIFEST.tsv`.
  `raw/2026-07-27/RT-20260727-1023.source.md` (the predecessor's partial paste) is PRESERVED.
- `analysis/altdata_build_queue.csv` -- 63 securities with `confidence` and `note` per row.

Speakers corpus-wide: CONFERENCE ROOM 49.1%, Adam Muller 45.8%, CONFERENCE ROOM 2 3.9%,
William Wicker 1.2%, 1 unattributed cue.

**Expiry is live, not theoretical.** Recap cards read "Expires in N days" with the April meetings
at **5-14 days remaining**, and a SharePoint mail confirms a prior recording was already
auto-deleted. Andrew's download is what saved this corpus.

---

## Next Steps

- **[Andrew]** Decide whether to extend Teams transcript retention. Independent of any build, and
  the clock is now measured, not estimated -- April meetings are inside two weeks of deletion.
- **[1.0.0_SA_CTO]** Architecture item, not a dispatch: the m365 gateway drops retrievable data
  at the query layer in three places (`eventDetail` omitted, no chat paging, no shared-drive
  endpoint). Second instance of the drop-at-`$select` pattern after `tools.py:597`.
- **[4.0.0_SA_CRO]** Phase 2 -- the corpus is now dated, so attention-over-time is computable
  (which securities the team's focus moved toward, and when). Deliberately NOT done yet: it is
  the first analysis that depends on the dates being right, so it should follow a period of the
  dating standing unchallenged.
- **[4.0.0_SA_CRO]** Retrieve 2026-07-13 and the 2026-05-12 second recording if they surface.
