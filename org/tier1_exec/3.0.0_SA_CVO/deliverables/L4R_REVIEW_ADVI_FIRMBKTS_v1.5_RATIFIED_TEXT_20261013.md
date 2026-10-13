# L4-R review, ADVI_FIRMBKTS PRD v1.5, ratified-text half (FWD-9 added; FWD-1 and FWD-4 unchanged) -- SIGN (3.0.0_SA_CVO, dell1, 2026-10-13)

**Asked by** `1.0.0_SA_CTO~DELL1` msg 5023 (acked). **Bytes reviewed:** `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md`
@594b78a036 (blob b6da547c68), equal to HEAD and to the working tree. `git diff 4289847ccf HEAD` on that file, read whole (+87 -8):
4289847ccf is the v1.2 pin of my last ratified-text stamp (half `27be69a5dca4`, signed 2026-09-14). Half hashes, recomputed with
`.tools/prd_signoff_lib.py` at HEAD and at 594b78a036: ratified-text `bc944f465a29` (equal to the CTO's quote), ENDPOINT `a4cee016e808`
(v1.2: `9e7bda0f35d0`). `prd-signoff.py status ADVI_FIRMBKTS` before this stamp: ratified-text STALE, owed by 3.0.0_SA_CVO; brief SIGNED
(auto, CRO-written brief).
**Sources read:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md` (Andrew's ADVI memo
transcript :85; O10 :314-328); `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` (the counterpart, :50, :196, :201).

## Verdict: SIGN

What moved in the ratified half, by section:

- **ENDPOINT:** one change, the new FWD-9. FWD-1 through FWD-8 are byte-identical to v1.2.
- **CONTRACTS:** byte-identical to v1.2 (section compare via `top_sections`).

Everything else in the diff sits outside the hashed sections:

- the header (`fabric`, `prd_version`, `endpoint_outcomes` gains FWD-9);
- the v1.3 F4 premise repair in the arc, cell candidates, paths and surface manifest (the brief half);
- the two L10 addenda (v1.4 sequencing; v1.5 FWD-9 and the DEC-14 REC).

## FWD-1 and FWD-4: not re-worded, nothing relaxed

My round-6 grade (`ADJUDICATION_v7` row `ADVI_FIRMBKTS-D1-C-S45`) held FWD-1 PARTIAL. The clause asks for two readers who have never
worked together and who agree with each other, and a key is not a second reader. I asked the CTO for a second fresh reader or a ruling.
v1.5 does neither: FWD-1's text is unchanged, so independence is not relaxed by this PRD, and the round-6 grade stands as written. The
same holds for FWD-4. My round-4 and round-5 grades held its live half (the validator's non-admin read) PARTIAL; the text is unchanged,
and nothing is narrowed to fit what was measured.

| | v1.2 @4289847ccf | v1.5 @594b78a036 |
|---|---|---|
| FWD-1 | Anyone who looks at where a piece of data is kept can tell what it is and whose it is, without opening it. DONE WHEN EXERCISED -- two people have actually read the same set of locations and compared answers. ACCEPT two people who have never worked together read the same list of storage locations and each says, for every one, which system made it, which firm it belongs to, how finished it is and what it holds -- and they agree -- where today the same kind of information is written three different ways and neither reader can tell whose it is. SOURCE brief Part I O1; bar Part III O1/O2 | identical (760 of 760 bytes) |
| FWD-4 | A firm's people see exactly what they saw before on the day their data moves, and cannot tell from looking that anything happened. DONE WHEN EXERCISED -- a firm has actually been moved and the result was read back deliberately. ACCEPT after a firm's data is moved, someone deliberately compares what is being served now against what was served before and finds it identical for everything a user can reach; the sign-off named every piece that moved and how to put each one back; and the old copy is still sitting there untouched for the agreed period. A real user opening the page and noticing nothing is the CONFIRMATION, never the proof. SOURCE brief Part I O4; bar Part III O4 | identical (870 of 870 bytes) |

## FWD-9 (new)

- **It is a widening, and it is on Andrew's word.** Its SOURCE is his 2026-10-13 ADVI memo. The memo is on record: the direction
  packet's transcript at :85, carried as O10 at :314-328, crossbox XB-20261013T180327Z-ba46. It asks for "a clear plan for the migration
  ... including all current operating functions ... as well as a decommissioning plan for legacy buckets and legacy operations". The
  text takes those words without widening them: (a) the plan, (b) one retirement by a recorded decision.
- **The DONE WHEN can be graded as written.**
  - (a) is read from one document against named categories: per firm, every operating function, the order of moves with a rollback per
    move, each legacy bucket's decommission, and each legacy operation to retire.
  - (b) is one recorded decision on one real legacy operation, naming its replacement or that nothing replaced it.
- **It is provable on demand.** Writing the plan and recording one retirement decision are both acts a seat can take. Nothing in either
  arm waits on an outside clock. A delete still needs Andrew's word under FWD-6 and DEC-12; FWD-9 (b) asks only for a retirement by
  decision.
- **Its consistency holds.** "Each legacy bucket's decommission (FWD-6's window)" binds the same 45-day standard that MDPF_CANON
  consumes (:201). The plan's scope (Inflection, Cottonwood) is the two firms whose moves are not started, and it does not start them:
  the v1.5 addendum's sequencing says so.

## CONTRACTS against the counterpart

CONTRACTS is unchanged, and MDPF_CANON's consumed rows still match it:

- each firm's bucket and its serving grants, produced per firm by ADVI_FIRMBKTS (:196);
- FWD-2 and FWD-6 waiting on this project's router flip per firm (:50, v2.11 R1);
- the 45-day decommission standard (:201).

The v1.4 addendum's R2 (this project owns the shared serving files through act 4) and R3 (the `mdpf/{firm}/platinum/*` grant is a named
cell of this project) are carried as addenda. The addendum states "Not changed: every ENDPOINT outcome and every contract", and the hash
agrees with it.

## Names and addresses

- v1.5 adds no address and no name.
- The one name in the diff is in the v1.4 addendum: `mdpf-49f-gold-writer-role`. It equals `lib/opal_naming.py`
  `name("mdpf","49financial","gold-writer","role")` on this seat's run. It matches `fence_patterns("49financial")` =
  `arn:aws:iam::313476888478:role/*-49f-*`.

## Carried (not grounds)

1. **How I will grade FWD-9 (a)'s "every".** That arm says "every Advisor Intelligence operating function" and "every consumer of a
   legacy-bucket input". I will grade it against named censuses with their denominators printed in the plan, and a plan that asserts
   "every" without one reads NOT MET:
   - the F1 census;
   - the IRPT invocation census (FB-g-29);
   - the SEV1 publisher census (FB-g-32);
   - the read and writer censuses (round 3 and round 4);
   - for the gold chain's schedules and triggers, `opal_naming.py targets` or the dispatcher's own map.
2. **FWD-1's agreement arm** is still open at the CTO (my round-6 ask: a second fresh reader over the same 150, or a recorded ruling). A
   later re-word of FWD-1 to "a reader agrees with the key" would be a narrowing. It needs Andrew's word, or a CTO ruling that cites the
   clause and why it changes.
3. **DEC-14's new REC (retire `mockadv`)** sits in the addendum, outside this half. The ruling stays Andrew's. The consumer census that
   reads zero before the removal is that act's own precondition.

-- 3.0.0_SA_CVO
