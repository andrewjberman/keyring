# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 116 -- THE ADJUDICATOR WAS WORKING THE WHOLE TIME, AND EVERY INSTRUMENT THAT SAID OTHERWISE WAS CORRECT

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-14T14:2xZ**
Tick 115's log is `@cf89e6d29e` (+ addendum `@8d650960c8`). Delta: `008c6206d2`.

> **Tick 115 ended with a direction authored and handed for delivery against a seat read as idle. In
> this tick the delivery FAILED at the transport layer, and the read that was supposed to authorize a
> respawn found 2.56 MB of round-9 adjudication being written while I measured.**

---

## 1. THE DELIVERY FAILED, AND THE FAILURE WAS NOT IN THE TEXT

`0.0.0_AB_MSTR~Z` (msg 22765) escaped the payload correctly for SendKeys -- the peek shows literal
`(1)`, `(2)`, `(TO-S2-1, ...)`, `(LD-0521)` rendered exactly -- and **the whole block landed in the
PowerShell prompt, not the Codex composer.** It stranded at a `>>` continuation on an unterminated
quote, so **nothing executed**; cleared with `^C`, no file touched, no state changed.
⭐ **The payload was right and the TARGET was wrong** -- that seat named the distinction itself and
reported inside sixty seconds, which is why no second block was written against a dead route.

## 2. ⛔ THEN THE RESPAWN PRECONDITION READ FOUND THE SEAT WORKING

A respawn was the act being considered behind the transport problem. **I went to measure its one
precondition -- would it destroy work** -- on `git status --porcelain` of the CVO's tier-1 home, with
the tracked-file count beside it (1815) so an empty result could not read clean-or-matched-nothing.
```
?? AMGT_RESAPP_ROUND9_CVO_AUDIT_20260914_Z.json    1,990,425 B   mtime 14:17:05Z
?? AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.json       3,553 B   mtime 14:18:35Z
?? AMGT_RESAPP_ROUND9_CVO_VERIFY_20260914_Z.json     570,919 B   mtime 14:21:25Z
   all UNTRACKED (git ls-files --error-unmatch per file) · times via date -u -r, NOT ls --time-style
```
>> ⭐ **THE COUNT WAS 2 ON MY FIRST READ AND 3 ON MY SECOND, NINETY SECONDS LATER.** VERIFY appeared
   between them. **A snapshot of any plane shows a seat's output; only a REPEATED read shows the pen
   moving** -- and that single fact is what turned three files on disk into a seat at work. <<
Content opened, not inferred from the name: `"at": "2026-09-14T14:18:35.750Z"`, a `portal_pin`, sha256
of `RankedList.tsx` / `LeadPanel.tsx` / `SecurityAnalysis/constants.ts`, rendered HTML for four states.
**STOP issued same-turn (msg 22768): no respawn, no kill, no destructive re-attach.** Taken and already
in force. The files were not touched, not committed, not read beyond the 3.5 KB one.

## 3. WHAT THIS FALSIFIES -- AND EVERY INSTRUMENT WAS CORRECT

| read | verdict | and it was |
|---|---|---|
| bridge GREEN 9/9 | healthy | **correct** -- it measures the bridge |
| `unread_inbox` 0, then 0 READ of 20 rows | deaf | **correct** -- the bridge drains files |
| plane (a) author filter, control-certified | COLD | **correct** -- nothing committed |
| plane (b) `git log --author -- <home>` | COLD | **correct in its method** |
| the screen peek | idle at an empty composer | **correct about that surface** |

⛔ **THE MECHANISM, AND IT IS THE EXACT MIRROR OF THE FIX I LANDED NINETY MINUTES EARLIER.** Plane (b)
is a `git log` read: it answers about **COMMITTED** deliverables, so a seat that writes through a long
adjudication and commits at the end is invisible on it for the whole run. `Z-S82`/`Z-S86` tightened
that read to scope a shared home to one lane -- and **the same anchor is inapplicable to an untracked
file, which has no author at all.** The remedy narrowed the instrument along the attribution axis,
left it blind along the commit axis, **and made the blindness harder to see by making the read look
more rigorous.** Neither I nor the two seats that reviewed the clause noticed.
**Landed @`008c6206d2`:** plane (2) now reads the working tree beside the committed read -- porcelain
with the tracked count as discriminator, **read twice**, and an untracked file attributed by name and
content but never by the shared path. `Z-S87` records it.

## 4. ⭐ AND THE READ THAT FOUND IT WAS NOT A LIVENESS PROBE

It was the precondition question for a **destructive act** -- *would a respawn destroy work* -- and
that is the only question in this entire thread that points at the **working tree** rather than at a
commit, a broker row, a process or a screen. **A probe assembled from planes that answer LIVENESS will
not contain it.** The transferable form: **WHEN EVERY PLANE READS COLD, ASK WHAT A DESTRUCTIVE ACT
WOULD COST** -- that question reaches a surface the liveness planes do not.
⚠ And it very nearly did not get asked: the respawn was not my idea, it was not proposed to me, and I
only measured it because a respawn would have been **mine to authorize** and I wanted its precondition
before ruling. **Three seats spent ninety minutes on the transport and none of us read the disk.**

## 5. STATE

```
AMGT_RESAPP  active / ROUND_CLOSE  47 of 47 COMPLETE, 0 open   newest COMMITTED adjudication 34.5 h
             ADJUDICATION_v9 ABSENT at HEAD (8 siblings) -- CONSISTENT with one in progress, uncommitted
POSN_ASTTAX  active / EXECUTING    15 C / 4 ACTIVE of 19       newest COMMITTED adjudication 33.4 h
             ADJUDICATION_v4 PRESENT (5 siblings) · REMEDIATION_v4 / RA.round4 / GRADES ABSENT
denominator 2618 · ZZZZ_NOSUCH 0 · both UNPLACED in the sequence, no DRIFT
OPEN CALLS IN SCOPE: 0 · at Andrew and out of scope: 2 · NO PITCH
COMPLETION   NOT DONE -- 0 of 2 · REACHABLE 2 · UNREACHABLE 0 · HELD-AT-STOP not reached
```
⚠ **The undelivered prompt is no longer urgent for the AMGT half** -- whatever the seat is doing, it
is doing that. It stays held; transport remains `0.0.0_AB_MSTR~Z`'s. **POSN round 4 is still owed and
nothing observed this tick speaks to it.**
`Z-S46`/`Z-S55`/`Z-S56`/`Z-S61`/`Z-S79` ARMED · `Z-S82`/`Z-S84` disarmed · `Z-S85`/`Z-S86`/`Z-S87`
filed · portal `e85f6eb84f` · LD-0521 holds · freeze stands. No TO cut, no dispatch, no apply, no
promote, no gitlink move, no status flip.

## Compiler Tools

The respawn precondition measured **before** the ruling rather than after · `git status --porcelain`
carrying its **tracked-file denominator**, so an empty result could not be read as clean · the same
read **repeated ninety seconds later**, which is the only instrument in this thread that saw motion ·
untracked status confirmed **per file** with `ls-files --error-unmatch` rather than inferred from the
porcelain · mtimes via `date -u -r`, after I had typed a literal `Z` into an `ls --time-style` in the
previous call and got LOCAL time back -- the trap CLAUDE.md names, caught by the numbers disagreeing
with a reading I already had · attribution stated as a **limit** (an untracked file has no author, the
home is shared seven ways) with the operative conclusion shown not to depend on it.


---

## ADDENDUM -- MTIME IS NOT ARRIVAL TIME, AND MY OWN s.2 INVITES THAT INFERENCE

A fourth read at **14:30:34Z** put the porcelain count at **4**. The new entry is
`AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.cjs`, 4,245 B -- **mtime `14:18:35Z`.**

⛔ **That mtime PREDATES two reads that did not show the file.** The porcelain listing at ~14:21Z
printed three lines and the count at 14:22Z was three; at 14:30Z it is four, and the newcomer is
stamped twelve minutes earlier than the read that missed it.
>> ⭐ **So on this surface MTIME DOES NOT DATE APPEARANCE.** A file can arrive in the working tree
   carrying an older stamp -- a move preserves mtime, and I am naming that as the likely mechanism
   without asserting it, because I did not watch it happen. **An mtime-ordered listing therefore
   MISORDERS ARRIVAL, and pairing "the count changed" with "and its mtime is 14:21" invites exactly
   the inference that the stamp says when it showed up.** <<

**WHAT SURVIVES UNCHANGED:** the count moving 2 -> 3 -> 4 across three reads is activity, and s.2's
conclusion and the rung clause at `008c6206d2` rest on the COUNT, not on any stamp. **WHAT IS
CORRECTED:** s.2 reads as though `VERIFY`'s 14:21:25Z stamp is what places it between two reads. It
does not; the *visibility change* placed it there and the stamp merely agreed. ⚠ **No row is
filed** -- `Z-S87`'s operative claim is untouched and this corrects a supporting inference inside the
same document; minting a fourth row this hour for it would be ceremony over a sentence.


---

## ADDENDUM 2 -- I ATTACHED A LIKELY CAUSE TO A PRINTED DISCREPANCY, WHICH IS THE ONE THING MY OWN BANKED LESSON FORBIDS

The addendum above wrote: *"a move preserves mtime, and I am naming that as the likely mechanism
without asserting it."*
⛔ **That hedge IS the defect, not a defence against it.** The banked line, in this seat's own
memory and quoted in the index: *"Resolve it in the same call, or write 'unreconciled' alone and
unqualified -- NEVER THE MIDDLE."* A cause offered as *likely* and disclaimed as *not asserted*
dismisses the next reader at zero evidentiary cost, in the same formatting as the measured half. I
have now done it twice in one day, the second time inside a document correcting the first.

**`0.0.0_AB_MSTR~Z` then tested the nearest neighbour of my hypothesis and it FAILED:**
`git check-ignore -v` on the `.cjs` returns **NOT ignored**, and its mtime `14:18:35Z` is **six
minutes before that seat's own 14:24:19Z read** which also missed it. That seat declined to close the
gap with any hypothesis and named this fabric's own lesson as the reason. **Correct, and it is my
lesson to have applied first.**

**ONE CANDIDATE I CAN NAME BECAUSE I OBSERVED IT, AND IT IS STILL NOT A CLOSURE:** at ~14:31Z my own
`safe-commit` was REFUSED with `Unable to create .git/index.lock: File exists` -- a peer was writing
the index in that window, and `22776` reports the four files transitioned `??` -> `A`, so **that peer
was the adjudicator staging exactly these files.** A concurrent index write overlapping a
`git status` read is a *testable* candidate for a racy listing. **I have not tested it and it is not
the explanation until someone does.** The gap stays **UNEXPLAINED**, and **FOUR is the operative
count** -- three was wrong from before anyone first looked.

⭐ **AND THE STAGED STATE RAISES THE STAKES ON THE STOP RATHER THAN LOWERING THEM:** 2.5 MB sits in
the SHARED index. `safe-commit.sh` runs `git commit --only -- <pathspec>` and never falls back to a
bare commit, so the scoped commits this loop has been making all evening cannot sweep them -- measured
by `2.0.0_SA_COO~ZZZ`, and this seat has been relying on it unknowingly for four commits. **Anything
that drops that process now strands a prepared commit in the shared index**, which is the
foreign-staged-index condition `safe-merge` refuses on.


---

## ADDENDUM 3 -- THE GAP IS CLOSED BY MEASUREMENT, AND **THREE WAS RIGHT**

`2.0.0_SA_COO~Z` found the field that answers it: **on NTFS `os.stat` exposes `st_ctime` as CREATION
time**, so a file written in place has `mtime == ctime` and a file COPIED or MOVED in keeps its source
mtime and gets a NEW creation time. Re-derived here on this seat's own instrument rather than taken
from the table, with the same controls:
```
file                                          bytes    mtime          ctime(CREATE)   delta
..._AUDIT_20260914_Z.json                   1,990,425  14:17:05.189   14:17:05.185     -0.0 s
..._RENDER_20260914_Z.json                      3,553  14:18:35.751   14:18:35.751     +0.0 s
..._RENDER_20260914_Z.cjs                       4,245  14:18:35.013   14:25:57.226   +442.2 s  <<
..._VERIFY_20260914_Z.json                    570,919  14:21:25.429   14:21:25.429     +0.0 s
..._COMPILE_20260914_Z.json                     1,832  14:36:00.186   14:36:00.186     +0.0 s
CVOZ_ADVERSARY_DECL_LIFECYCLE_20260820.md       2,780  12:55:18.463   12:55:18.463     -0.0 s  [control]
CVOZ_ADVERSARY_DECL_LIFT_20260820.md            2,789  12:55:18.398   12:55:18.398     +0.0 s  [control]
```
**Four files and both controls agree to the millisecond; one file is 442 seconds apart, and it is
exactly the one in dispute.**

>> ⛔ **SO THE `.cjs` ARRIVED AT 14:25:57Z -- AFTER my 14:21/14:22 reads and after
   `0.0.0_AB_MSTR~Z`'s 14:24:19Z read. EVERY LISTING WAS CORRECT. THERE WAS NO GAP.** Addendum 2's
   closing clause -- *"FOUR is the operative count; three was wrong from before anyone first looked"*
   -- **is FALSE.** Three was right at its vintage. <<

⭐ **AND THE LESSON IS NOT THE ONE I BANKED AN HOUR AGO.** Addendum 2 chose the honest ending --
`UNEXPLAINED` -- when **a discriminating FIELD was one `os.stat` away and had been there the whole
time.** "Unexplained" is truthful and it is not free: it parks the work on the next reader, and here
the next reader simply ran the read I had not thought to run. **Ending (b) is legitimate only AFTER
you have hunted for the discriminator and failed to find one. I had not hunted.**
**What addendum 1 got right survives and is now mechanised:** mtime is not arrival time -- **and
`ctime` is the field that separates them on this device.**

⚠ **One attribution correction in the other direction:** msg 22782/22780 credited the count of FOUR
to `2.0.0_SA_COO~Z`'s plane-7 message, which contains no such count. The FOUR came from this seat's
own 14:30:34Z read and from `2.0.0_SA_COO~ZZZ`'s 14:29:38Z read. Noted so the number stays attached to
the read that produced it.
