# ENDPOINT (step 2, `/endpoint --forward`) -- D8, ADVI gold redesigned to the LGIC canon

> **NOT YET LANDED IN A PRD, AND NO PROJECT CODE EXISTS YET.** This is emitted ready to paste under a section titled
> exactly `ENDPOINT (step 2, /endpoint --forward)` in this project's PRD, once L3 mints it. The candidate code is
> `ADVI_GLDLGIC`, proposed at D8 / ADVI / laptop; both are assigned at L3 by this seat, after Andrew confirms DONE WHEN.

**Cut by:** `1.0.0_SA_CTO` (L2), 2026-09-15 ~15:0xZ.

**From:** `docs/briefs/d8-advi-gold-redesign-lgic-brief-20260915.md` @`62d0ab600e`.
- 17,014 bytes, on disk and in the record alike; that is the file's latest commit.
- Author `4.0.0_SA_CRO`.
- 8 top-level parts, 8 outcome headings (O1-O8), and 6 Part III bars (O1, O2, O3, O4, O7, O8). **O5 and O6 have no bar in
  the brief; they are cut from Part I alone.**

**Commission:** Andrew-direct ~14:2xZ, *"recs approved aand all future pipelines must abide by lgic structures patterns"*
(/open-calls card 3: its own project, not folded into ADVI_FIRMBKTS), with CLAUDE.md Rule 30.

**Andrew has NOT read this brief.** Per his 2026-09-03 word, he confirms the DONE WHEN lines from this pass.

---

## THE EIGHT OUTCOMES

```
  FWD-1  An engineer changes an ADVI history table once, and every firm's
         history carries the change
         DONE WHEN  EXERCISED -- an engineer has made one such change and seen it
                    arrive for every firm after the next daily run
         ACCEPT     an engineer adds or corrects one of ADVI's history tables in a
                    single place, and after the next daily run every firm on ADVI
                    has it -- no firm is left on the old version, and there is no
                    per-firm copy anyone had to remember to update
         SOURCE     brief Part I O1; bar Part III bullet 1

  FWD-2  A new firm's ADVI history comes online from the firm list and its
         settings alone, with nothing named or located by hand
         DONE WHEN  EXERCISED -- a firm has actually been brought online this way
         ACCEPT     bringing a firm onto ADVI takes adding it to the list of firms
                    and giving it its settings; a reviewer looking for a storage
                    location or a name that someone typed in by hand finds none
         SOURCE     brief Part I O2; bar Part III bullet 2
         AT RISK    it needs a firm to bring online on demand (s.1)

  FWD-3  An analyst answers a past-date question from the firm's own history
         tables
         DONE WHEN  EXERCISED -- an analyst has answered one that way
         ACCEPT     someone asked "what was this account worth on a past date"
                    answers it from that firm's own history tables, which go back
                    as far as our data does and gain one row a day -- never from
                    the file a page reads, and never from a backup copy
         SOURCE     brief Part I O3; bar Part III bullet 3

  FWD-4  Every file an ADVI page reads has exactly one writer, and that writer
         only reads the history tables
         DONE WHEN  EXERCISED -- every such file has had its writer named and
                    confirmed to be the only one
         ACCEPT     for any file an ADVI page reads, anyone can name the single
                    thing that writes it; nothing else writes that file, the
                    writer reads the history tables and never changes them, and
                    the page's file is never also the history
         SOURCE     brief Part I O4; bar Part III bullet 4

  FWD-5  An operator can say where each ADVI job runs and why, and finds its
         code in one place beside what it produces
         DONE WHEN  APPLIED -- every ADVI history job has its place, its reason
                    and its one code location written where an operator looks
         ACCEPT     an operator asked about any ADVI history job can say whether it
                    runs as a small on-demand job or on a dedicated server, and
                    why; and finds its code in exactly one place, next to the data
                    it produces
         SOURCE     brief Part I O5 -- NO Part III bar; cut from Part I alone
         AT RISK    "why a dedicated server" rests on Andrew's heavy-job threshold,
                    which he has deferred (s.2)

  FWD-6  An operator opening an ADVI history area finds only history
         DONE WHEN  APPLIED -- run bookkeeping and backups are out of every ADVI
                    history area
         ACCEPT     someone browsing any firm's ADVI history area finds only
                    history tables; the records that track each run live in their
                    own clearly separate area, and backups sit outside it with a
                    date on which they expire
         SOURCE     brief Part I O6 -- NO Part III bar; cut from Part I alone

  FWD-7  An advisor notices nothing on their pages unless a change was announced
         DONE WHEN  EXERCISED -- each part has gone live and the figures advisors
                    see were checked on the day it did
         ACCEPT     after each part of the change goes live, every figure an
                    advisor or firm user sees on an ADVI page is what it was the
                    day before -- unless the difference was agreed and told to
                    them first -- and at no point were an old and a new version
                    running side by side
         SOURCE     brief Part I O7; bar Part III bullet 5

  FWD-8  Andrew can see every place ADVI's history departs from the house rules,
         and why
         DONE WHEN  APPLIED -- every departure ADVI keeps is on the exceptions
                    list with Andrew's acknowledgement
         ACCEPT     when Andrew asks about any place ADVI's history breaks the
                    house rules, he is shown it on the exceptions list with its
                    reason and, if it is temporary, when it ends -- and nobody
                    finds one after the fact
         SOURCE     brief Part I O8; bar Part III bullet 6
```

---

## WHAT THE CUT SURFACED

### 1. FWD-2 needs a firm to bring online ON DEMAND, or it becomes a wait

No new ADVI firm is scheduled to join. Rule 27 says **no FWD is a wait**: each outcome must be provable by an act a
seat can take on demand. The on-demand act is to bring a declared stand-in firm online through exactly the same path,
from registry rows and configuration. The estate already holds one: the demo tenant, a granted DEMO-TENANT class (R20
X6). **REC: FWD-2 is exercised on the demo tenant.** A real N+1 firm later is a confirming read, never the bar. If
Andrew wants a real firm to be the bar instead, that is a wait, and it needs his word.

### 2. FWD-5 rests on a threshold Andrew has deferred

R13 leaves the heavy-job threshold to Andrew, deferred "until the first genuinely heavy case"
(`02_DOCTRINE.md:239-246`). ADVI's gold jobs run on EC2 today (brief IV.3). FWD-5's "and why" can be met without him
only if every ADVI job moves to Lambda. If any job is to stay on EC2, the project owes him the first heavy case. **This
is not raised now**: the MAP step measures the jobs first, and the question goes to him with a real job in hand, not
in the abstract.

### 3. FWD-7 and ADVI_FIRMBKTS touch the same served files, so the move and the reshape are ONE act

Brief Part II draws the boundary: ADVI_FIRMBKTS moves the existing bytes, and this project decides what writes gold
from now on. Where both touch one served file, R18 makes it a single act with one never-widen sign-off. **That is a
sequencing dependency, not an endpoint change.** It is carried to L3 (placement) and L5 (decomposition), and it is why
the proposed SEQUENCE position is right after ADVI_FIRMBKTS.

### 4. The Tax SMA valuation contract crosses this boundary

`b00_canonical_valuation` is reused as-is by MDPF_TAXSMA (brief IV.7). FWD-1's "change once, every firm carries it"
must not change b00's meaning under Tax SMA. **The PRD carries b00's contract as PRESERVED**: it changes only through
MDPF_TAXSMA's owner. This is Part II's "RELIES ON", not a new outcome.

---

## PROVENANCE

**READ, @`62d0ab600e`, from the record:** the whole brief, 259 lines, Parts I-VII and REFS.

**NOT READ:** the task-order register and any project JSON (Phase 0 reads only the brief); ADVI_GLDOPS and ADVI_GLDRST
(the brief names them as places to look, and did not read them either); the runner families' contents. The brief's
IV.1 duplication is a FILENAME census, not a content diff (its own Part VII).

**NOT CLAIMED:** that these are the outcomes Andrew wants. That is his confirmation, per his 2026-09-03 word.
