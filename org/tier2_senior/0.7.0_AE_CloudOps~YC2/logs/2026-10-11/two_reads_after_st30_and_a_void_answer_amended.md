# Two reads after st30, and a void answer the issuer amended out from under me

**archetype:** TRACE
**secondary_archetypes:** VALIDATE

**Serial:** `0.7.0_AE_CloudOps~YC2` (lane, dell2)
**Window:** 2026-10-11 12:02Z -> 12:55Z. Prior log `fd34e0ed1c`
(`the_one_resident_release_st30_installed.md`), which covered the st30 install itself.
**Orders:** `IRPT_YCDGEN.TO-APPLY-j1` (journal read, `<risk>SERVED</risk>`) and
`IRPT_YCDGEN.TO-APPLY-j2` (one profile row, `<risk>SERVED</risk>`, AMENDMENT 1) -- both
`<status>complete</status>`. Cell `YCD-d-11` for both.
**Commits:** `d2b64782e8` (j1), `51edf40c63` (j2 first read), `0e187e8f00` (j2 amended read),
`aa523b5a19` (artifact pins). `51edf40c63` on origin `box/dell2`; the other three LOCAL
(`git ls-remote` read at 12:53Z, origin tip `b16f190605`).

---

## Current State

Written for a reader with zero prior context.

**All eight orders this lane holds read `complete`.** Nothing is owed by this seat; nothing waits on it.

**j1 -- what the st30 resident did with TCKT_VNEXT's fourth run.** `REQ-59aa6803901f371b27ffa176` was
taken up on the new root and worked twice, then stopped on a VENDOR-SESSION refusal:
`EVICTION verdict=SIGNED_OUT` 11:19:02, `POLL retained_for_retry class=OperationRefused
code=CAPTURE_FAILED:AUTH_FAILED:NO_AUTHENTICATED_PROBE` 11:19:20, `EVICTION verdict=SIGNED_OUT`
11:34:04, `ATTENTION code=SESSION_REFRESH_ALREADY_USED` 11:34:05. `WINDOW lines=165 polls=159
handled=3 tracebacks=0`, `UNSET=0 SENDFAIL=0`. The resident is healthy; nothing st30 changed is
implicated, and **no st30 rollback trigger is met** -- no I3 send, no send failure, still polling.
So st30's S2 is exercised as to the ticket ADMISSION and not the READY receipt, and the refusal
being AUTH means **the `ticket_id` schema was not the cause of the dead letters**.

**j2 -- whether Andrew's own profile row names cottonwood.** It does not, and the row names no firms
at all: `PROFILE andrew@opalinvest.com status=active userType=Dev firmId=opal-capital` /
`ALLOWED-FIRMS shape=ABSENT count=0 ids=-` / `FIRM-NAMED cottonwood NO`. The `NO` rests on an ABSENT
attribute, not on a list lacking cottonwood.

**Records.** `deliverables/irpt_ycdgen_j1/RUN4_JOURNAL_20261011.txt` + its proof instance (VALID,
3/3, 6/6 controls). `deliverables/irpt_ycdgen_j2/PROFILE_FIRMS_READ_20261011.txt` (SUPERSEDED, kept,
grades nothing), `PROFILE_FIRMS_READ_2_20261011.txt` + its proof instance (VALID, 2/2, 7/7 controls).

**Rows filed this window:** `D2-S51`, `D2-S52`, `D2-S53`. With `D2-S47` from the st30 window that is
four from this lane today.

---

## j1: the journal read

The order wanted the worker's own named lines and exception CLASSES only -- never a message, never a
traceback body -- because the named trap is a journal line carrying a client's or a security's name.

**The trap was exercised on a SEEDED input before the host read**, because a clean run against a
clean journal proves only that the input was clean. I built a synthetic journal whose planted
traceback ended `ValueError: Acme Family Trust holding AAPL is not permitted`. The program emitted
`TRACE 2026-10-11T11:19:11+0000 ValueError` and nothing else from it. Two more discriminations fell
out of the same run: a line merely MENTIONING `IRPT_RESIDENT_POLL` mid-text was refused as a NAMED
line (the match is anchored on the message after the journal prefix, not the raw line), and
`handled=0` was excluded while `handled=1` and `handled=10` were both kept -- a naive substring test
would have swallowed `handled=10`.

**Nothing was written to the host.** The bounds say no write, and the obvious implementation -- dump
`journalctl` to `/tmp` and grep it several times -- writes a file AND reads a slightly different
window per grep, so the counts need not agree with each other. One `journalctl` piped into one `awk`
instead: no temp file, and every number comes from the same 165-line pass, so they are mutually
consistent by construction.

**An empty section had to be distinguishable from an unread one.** I added a `COUNTS` line --
`req_lines=3 named_lines=9 trace_lines=0 unterminated_traceback=0` -- so each list's length is
asserted independently of the list, and `trace_lines=0` can be read against the WINDOW line's
independent `tracebacks=0`. That is what lets `0 TRACE lines` mean *the resident raised nothing*
rather than *the program failed to close a traceback*: run 4 was refused, not crashed.

**The tz assumption was measured, not assumed.** `journalctl --since` is LOCAL time while the order
specifies a UTC instant, and `--utc` changes only the output. `hosttz=+0000` printed in the same
command, so the window IS the 11:15:00Z window. A shifted window that happens to contain the request
reads exactly like a correct one.

**Redaction:** none needed, and that is a read judgment rather than a default. 12 saved lines, 6
distinct message bodies, all opaque request ids, verdicts, codes and counts.

---

## j2: an answer that was void, and the amendment that explains it

First read: `PROFILE-ROW-ABSENT andrew@opalinvest.com`. I closed the order on it at `51edf40c63`.

**Then AMENDMENT 1 arrived (msg 4915) and declared that answer VOID** -- the issuer's own script
defect. It assumed a person's PK is `USER#<email>`, which holds for a SERVICE row; the product finds
a user through the email index.

**The first instance was narrow, not wrong, and it had said so in advance.** Because a `get_item`
returning `None` reads identically whether the item is absent, the key is wrong or the table is
wrong, the ABSENT verdict needed a control -- and the bounds forbade the only strong one (the same
call against a key known to exist is a SECOND USER). So I took the control from this lane's own
record: `st29_release/swap_svc_firm.py:16-22` uses the same table, the same `PK=USER#<email>/SK=PROFILE`
shape and the same consistent `get_item`, and this lane ran it four times today with the row
resolving every time. And I scoped the absence to ONE KEY, declaring as an explicit exclusion
"whether Andrew has a user record under any OTHER key, SK, table or email spelling". That is exactly
the gap the amendment closed. **The lesson I take: the control told me the instrument worked, which
is not the same as the instrument being the right one.** A positive control proves the call shape
reaches items; it cannot tell you the key you chose is the key the product uses. The second read
settles it -- `pk_form=OTHER` -- so the two reads do not contradict each other, they read different
keys, and the shape is real for services and wrong for people.

**Re-grading against the amended bytes.** The order had been flipped `complete`, so the amendment
re-opened it. `git diff` against `76744e25ce` showed ONE hunk -- the status line I had flipped -- I
returned it to `pending`, and the working-tree blob then equalled `da08492157` exactly. Both criteria
in the rewritten instance are the AMENDED ones naming the second file; the first file is kept with
`artifact_covered_by` deliberately EMPTY.

**The answer, and the qualifier that is the real finding.** `shape=ABSENT` means the row carries no
`allowedFirmIds` at all. AC2 admits only YES or NO once a row is found, so THREE world states --
absent, present-and-empty, present-and-not-containing -- collapse into the same `NO`. A reader taking
the bare `NO` concludes the filer has a firm list excluding cottonwood; the truth is he has no firm
list. This is the order's own third named trap (taking an absent attribute for an empty list)
occurring LIVE, and it is visible only because the script classifies the shape. Row `D2-S53`.

**Two further checks that decided something.** `Limit=2` plus a `LastEvaluatedKey` check reported
`rows=1 more=NO`, so exactly-one was distinguishable from first-of-several -- one hit borrowed from a
multi-hit index would have attributed another person's firm list to this one, a well-formed and
entirely wrong answer. And the act is now two calls with DIFFERENT consistency: the `get_item` is
`ConsistentRead=True`, a GSI cannot be, so I report the item as a strong read and the lookup as
eventually consistent rather than claiming both.

**Not adjudicated, deliberately.** Whether `served.py:1063-1066` treats a MISSING attribute as an
empty set, raises, or branches elsewhere is unanswered: I read the table, not that code. Row
`IRPT_YCDGEN-D2-S4` is NOT dispositioned -- this read is its input, and what it adds is the filer's
own side (present, active, `userType=Dev`, `firmId=opal-capital`, no firm list).

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `comp-find "host_read" --files --limit 30`; `comp-find "swap_svc_firm" --files --limit 30 --band HEAD` | PASS | HEAD band located the SSM helper and, later, the two script copies whose prior reads became j2's positive control |
| `proof-of-spec-check.py` | on both instances, repeatedly | PASS (rc=0) both | j1 3/3 + 6/6 controls; j2 2/2 + 7/7 controls; 0 DID-NOT-DISCRIMINATE either |
| `surprise-row-gate` | at commit, three times | 1 REFUSAL then PASS | see What failed |
| `to-pipeline-gate` | at commit | PASS | graded both complete-flips |
| `comp-schedule` / `comp-iam` | not run | DECLARED-NOT-APPLICABLE on both orders | re-checked against each act AS EXECUTED, including j2's widened bounds; the grants exercised were proved by LIVE calls, never by `simulate-principal-policy` |
| `comp-adversary` | the orders' named traps, graded as controls | PASS | j1's seeded-traceback exercise; j2's third trap FIRED LIVE |

**What worked.** Reading each issuer script and sweeping it for write verbs with the counts PRINTED,
before running it against a production table or host -- a preflight is the author's self-report, not
a control. j2's amended script was swept afresh (63 lines, up from 46) precisely because the order's
preflight still described the old one.

**What failed.** Three mechanical rounds, all caught by gates rather than by me first: (1) the
`surprise-row-gate` REFUSED row `D2-S52` on **R-19** -- `disarm_owner='3.0.0_SA_CVO'` names the only
WRITER of a disarm clock, and where the artifact is the CVO's own row the owner is `1.0.0_SA_CTO`. I
fixed the row rather than take the audited override. (2) The j2 instance carried `cell_refs` on its
acceptance rows, which the schema forbids -- the TO's own criterion attributes carry them, and the
alignment limb reads them from there. (3) Both read records were left `PENDING-THIS-COMMIT` after
they had actually landed in different commits; pinned to `51edf40c63` and `0e187e8f00`, measured with
`git log -1` per path.

**Gap found.** The `output_evidence` catch-22 I hit on st30's AC1 recurred on j1's AC3: a `grep -c`
criterion with `expect: ^1$` wants a bare `1`, and the same gate refuses `len(output_evidence) < 8`
as thin. The two are jointly satisfiable only because the `expect` match runs under `re.M`, so the
count can sit on its own line inside a transcript-shaped block. Still a real escape, still
undocumented; it belongs in the checker's docstring. Not re-filed -- row `D2-S41` already carries the
class and the issuer has acted on it once.

---

## MCP traffic

5 in the window, all with `2.0.0_SA_COO~G2`. Received and acked: msg 4874 (j1 order), 4905 (j2
order), 4915 (j2 AMENDMENT 1). Sent: the j1 report (1076 B delivered, byte-verified) and the j2
amended report (1075 B). Both were moved to the recipient's `read/` dir by its watcher within
seconds -- that mv is not an agent-side ack, so I claim EMITTED, not READ. Four `[WATCHER-EXPIRED]`
notices, each re-armed the same turn with one Monitor call; the gap after each was swept for mail and
each sweep was empty.

---

## Blockers

**None.** Zero orders held, all eight terminal, nothing waiting on this seat.

Owned elsewhere, named so neither is stranded: `D2-S53` (what `served.py:1063-1066` sees for a
missing attribute) sits with `2.0.0_SA_COO~G2`; `D2-S52` (the CVO's "no request has run through the
new root" premise) sits with `1.0.0_SA_CTO` by R-19.

---

## Next Steps

1. `[2.0.0_SA_COO~G2]` Say which of the three states `served.py:1063-1066` actually sees for an
   ABSENT `allowedFirmIds`, or route it to the CTO -- that disarms `D2-S53` and is the last thing
   between this read and a disposition of `D2-S4`.
2. `[2.0.0_SA_COO~G2]` `D2-S51`: whether the 11:18:44 `RESOLVE state=READY` is the READY st30's S5
   instruments. It needs the print-site read I did not do, plus that line's job id.
3. `[2.0.0_SA_COO~G2 / TCKT_VNEXT]` Run 4 is blocked on the vendor session, not on the fabric:
   `SESSION_REFRESH_ALREADY_USED` after two `SIGNED_OUT` evictions. A fifth run needs a live YCharts
   session first, and the `ticket_id` schema is now ruled out as the dead-letter cause.
4. `[1.0.0_SA_CTO]` `D2-S52`: restate the premise on the next compile (`no request has run through
   the new root` -> `no request under a listed OPAL sign-in has run`) or rule the distinction
   immaterial. No grade changes either way; FWD-1 is NOT MET regardless.
