# 0.4.0_DS_ClientPlatform~R -- D1_NAMEDISCOVERY purpose PRD + the proof-of-spec enum gap (1847-2115Z)

**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE, COORDINATE

**seat:** `0.4.0_DS_ClientPlatform~R` · **window:** 2026-08-26T18:47Z -> 21:15Z
**prior log:** `mdpf_aggregate_predicate_control_1520-1610Z.md` -- **written by a PREDECESSOR SESSION of this
lane that DIED between 16:14Z and 16:32Z.** This is a fresh instance; the window opens at registration.
**projects:** D1 / `D1_NAMEDISCOVERY` (primary) · D2 / `ADVI_INSURE` (re-seated to this lane mid-window)
**dispatches:** `2.0.0_SA_COO` 73245 s.2 (instance move) · 73282 s.2 (array fix, later WITHDRAWN) · 73551 (PRD)

---

## SUMMARY

Started cold: no watcher, not registered, three unread messages, and a lane whose predecessor had died
without a handoff. **Reconstructed scope from the inbox record rather than assuming continuity** -- which is
the cost this log exists to spare the next instance.

Four commits. One PRD ratified on first read and then corrected by me within thirty minutes when a sovereign
word turned out to have closed a question I had reported open. **Two authorizations were taken and NOT
executed** -- one because the schema could not express the ruling truthfully, one because it was withdrawn.

**The pattern across the window: every substantive act was a measurement that changed what someone else was
about to do.** Three of the five findings below were caught against work that looked finished.

---

## WHAT LANDED

| commit | push state (measured) | what |
|---|---|---|
| `4b358413d7` | **ON origin/CLOUD** | moved the ADVI_INSURE proof-of-spec instance `~J` -> `~R`; git-recorded rename 100%, 0 insertions/0 deletions |
| `4776a2305c` | **ON origin/CLOUD** | recorded the proof-of-spec status-enum gap as an artifact |
| `0e660a3b63` | **ON origin/CLOUD** | `D1_NAMEDISCOVERY` purpose-level PRD v1 (Rule 27 step 2) |
| `958c8e4487` | **LOCAL, rides** | PRD v2 -- corrected my own s.7.1 |

Push states measured against a FETCHED `origin/CLOUD` with an ancestry positive control, re-measured at
close. Rule 22a's new ephemeral-pin clause (`@4424c948f7`) does not apply: these are merge-based branch
commits, where ancestry remains the correct instrument.

---

## FINDINGS

*(continuing this lane's sequence; F10-F12 are in the predecessor's log)*

### F13 -- A repair that fixed one direction and broke the other, in ONE edit

`2.0.0_SA_COO`'s reseat `@8155516dbd` re-pointed `<instance_path>` from the dead `~J` tree to this lane and
**did not move the 26,484-byte instance.** VALID before, DANGLING after.

The consequence was not a broken path. **That seat's own new dispatch gate reads instance-EXISTENCE**, and it
had already recorded (72236) misreading absence-of-instance as UNSTARTED and dispatching on it. With
`status=pending` + `instance ABSENT`, the TO carried the exact signature of never-started on a project with
four of six criteria closed. **The fix that made this lane VISIBLE to `to-check` would have made its
COMPLETED work INVISIBLE to the proof-of-spec check. One edit, two directions, opposite errors.**

The move was ruled to this seat because owned-paths correctly REFUSED the issuer on this pod.

### F14 -- The proof-of-spec `status` enum cannot express ISSUER-RULED CLOSURE

Census, vintage-stamped, positive control run:

```
2026-08-26T19:59:01Z @3cb2e92679
164 files / 1,067 acceptance rows, all carrying a status field
  PASS 999 | UNCOMPUTABLE 25 | UNCOMPUTABLE-BY-CONSTRUCTION 22 | FAIL 13 |
  N/A-BY-CONSTRUCTION 5 | UNVERIFIABLE-BY-INSTRUMENT 3
CLOSED: 0        POSITIVE CONTROL: PASS=999 (matcher demonstrably finds values)
```

Issuers rule criteria CLOSED in messages. **No instance in this estate can say it.** So a ruling lands only
as an overstatement (`PASS` asserts the literal criterion was demonstrated -- AC1's landing prefix is
MEASURED ABSENT at 0 keys; AC2's requires an advisor spine the same issuer ruled structurally absent) or an
understatement (`UNCOMPUTABLE`). **The row cannot be made true by editing it.**

I was authorized to bring AC1/AC2 to the rulings, **took the authorization, measured first, and stopped.**
Authorization withdrawn at 73382. The array stays measured-honest.

⚠ **The census is PERISHABLE:** the same invocation read 163 files / 1,061 rows / PASS 994 fourteen minutes
earlier. **The SHAPE and the zero did not move; only the denominator.** The finding is the shape.

### F15 -- Two instruments, opposite errors, on one lane at one moment

`to-check.py --all --assignee 0.4.0_DS_ClientPlatform~R` -> **total=0 scanned=2115** (positive control at
`~J` -> total=1 over the same 2,115), while the broker rollup reported **4 pending TOs** for the same lane.
The truth was neither: **one project, carried all day on RULINGS, invisible to both.**

The issuer named the false-POSITIVE direction (a lane believes it holds work seated elsewhere). **The inverse
was live at this seat and is the one nobody looks for: a lane doing real, ruled, delivered work that no
assignee-based instrument can see**, because the authorizing act was a message. Root: **work authorized by
ruling leaves no TO, no proof-of-spec instance and no deploy ledger.**

### F16 -- A commit-pinned read answers about a VINTAGE, never about a record's current state

**This is my own error and it reached a ratified document.**

```
4dc2cd6087  14:06:28-04:00   item 4: "Item B ... remains OPEN at Andrew."
4b6503cdbd  14:07:24-04:00   item 4: "Item B CLOSED (~18:06Z, VERBATIM) ..."
                             ^^ 56 seconds later   (differenced in python, --date=iso-strict both sides)
```

The spine I was handed pinned `@4dc2cd6087`. I read exactly that ref, reported it faithfully in PRD v1 s.7.1
as an open sovereign question, and **was wrong about the world.** `git show <ref>:<path>` is the right
instrument for *what did this say when it was cited* and the wrong one for *what does this say*.

>> **A record cited by hash inherits that hash's staleness SILENTLY -- and the hash makes the citation look
>> MORE rigorous than a bare path, which is exactly what makes it persuasive.**

Remedy: read the pinned vintage AND `git log` the path. One command. I had it and did not run it.
**LIMIT DRAWN AND RATIFIED (73714 s.4): this is NOT a defect at the CITING seat.** The citation was accurate
when written; a hash freezes and a record moves. The obligation sits on the READER.

### F17 -- A multi-word phrase census FALSE-ZEROS across a line wrap, and the zero is byte-identical to absence

Verifying whether the claimed sovereign verbatim existed, I ran a content census for `not security grain`:
**a clean, denominator-printed ZERO over 26,902 files -- for a string that IS in the record.** The record
wraps mid-quote (`not` ends line 22, `security grain` begins line 23); a line-based matcher cannot see across
the break.

>> **Had I led with that zero instead of reading the file, it would have "confirmed" that a Tier-1 seat
>> fabricated a sovereign quotation -- a false accusation carrying an honest denominator.**

`2.0.0_SA_COO` independently hit the same vintage trap minutes later, was saved by that same grep, and
adopted "search for the quote itself" as a standing practice. **I falsified it with the measurement above:
their grep worked because the phrase they picked did not straddle a wrap -- luck about LINE WIDTH, not a
property of the method.** Corrected practice adopted at 73714: **`git log <path>` + read at HEAD is the
decider; the grep is only a trigger.** A phrase census is a NOTICING instrument, never a deciding one.

---

## BRIEFS / DOCUMENTS WRITTEN (DS role addition)

| document | commit | status |
|---|---|---|
| `D1_NAMEDISCOVERY_PURPOSE_PRD_v1.md` (now v2) | `0e660a3b63` -> `958c8e4487` | **RATIFIED** 73597; v2 correction accepted 73714 |
| `PROOF_OF_SPEC_STATUS_ENUM_GAP_20260826.md` | `4776a2305c` | recorded; remedy reserved to a fresh seat |

**PRD scope held deliberately:** WHAT and WHY only. No matcher design, no thresholds, **no schema or enum
mint**, no TO, no code, no file touched outside the document. After the 1,067-row withdrawal I minted nothing.

---

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | `"how do I grep the repo"` | PASS | A.3 startup EXERCISE -- forwarder produced its own banner, so it RAN rather than merely resolved |
| `comp-find` | `-i "<~J instance path>" --all` | PASS | 2 hits / 26,865 scanned; both a FROZEN historical sweep record -- confirmed my move dangled no LIVE pointer |
| `comp-find` | `-i "strategy_id" --band DEF` | **WARN** | 0 hits -- but the sweep reported 80 total across other bands. **Wrong BAND, not an absent term** |
| `comp-find` | `-i "strategy_id" --band CONFIG --all` | PASS | 10 hits; located the registry anchor + the 4-of-6 noded census |
| `comp-find` | `-i "not security grain" --all` | **FAIL** | **FALSE ZERO over 26,902 files for a present string** -- see F17 |
| `to-check.py` | `--all --assignee ~R` (x2, + `~J` control) | PASS | 0 -> 1 across the reseat; the control is what makes the 0 measured |

**What worked:** `comp-find`'s printed DENOMINATOR and its explicit "this is a MEASURED zero ... not a claim
the term is absent" caveat. That caveat is the only reason I re-read the file instead of trusting the zero in
F17 -- **the tool warned me about itself and it was right.**

**What failed:** the `--band DEF` zero (my error -- band choice, not the tool) and the F17 false zero.

**Gap found:** **a multi-word phrase spanning a newline is invisible to every line-based matcher in the rail,
and the resulting zero carries a full honest denominator.** `comp-find` cannot currently answer "does this
QUOTE appear" -- only "does this LINE-LOCAL string appear." Surfaced to `2.0.0_SA_COO` + `1.0.0_SA_CTO`
(73708/73709); recorded in the PRD provenance section. Not filed as a tool defect -- it is a property of
line-based matching, and the remedy is knowing which question the instrument answers.

---

## MCP TRAFFIC

**16 messages handled, all READ-acked** (`ack_messages` -- the only delivery clock an orphan cannot forge).
Significant only:

- **IN** 73551 `2.0.0_SA_COO` -- D1_NAMEDISCOVERY PRD dispatch (Rule 27 step 2)
- **IN** 73597 -- **PRD v1 RATIFIED**, step 2 DONE
- **IN** 73677 `1.0.0_SA_CTO` -- s.7.1 is NOT open; sovereign closed it 18:06Z
- **IN** 73382 -- array-fix authorization **WITHDRAWN** after my BLOCKING report
- **IN** 73245 s.2 -- instance move ruled to this seat (owned-paths refused the issuer)
- **IN** 72732 / 72766 -- **Andrew-direct ~17:2xZ non-interference rule**, received + confirmed
- **OUT** 73317 -- BLOCKING: the enum gap (0 of 1,067)
- **OUT** 73687/73688, 73708/73709 -- v2 correction + the F17 falsification, both to CTO and COO

---

## BLOCKERS

**None.** The one BLOCKING item I raised (F14, the enum gap) was ruled the same turn and the authorization
withdrawn -- it is a recorded estate finding, not an open block on this seat.

**Not blockers, recorded so they are not re-discovered:**
- `ADVI_INSURE` AC3/AC4 sit behind the **ADVI_PERFRP sovereign publish gate** (Andrew-direct 2026-08-21;
  `advi-49f-publisher` State=DISABLED by contracted design, grant unset, 3 of 4 source-gap rows open).
  **One gate, two TOs** -- ruled at 73197. Not to be re-asked per tick.
- The ADVI_INSURE TO face **contradicts itself on AC1** (header says closed, body says APPLIED-GATED).
  Issuer-owned, measured, deliberately NOT fixed -- ruled "safer written down than fixed tired."

---

## CURRENT STATE

**For a reader with zero context.**

`0.4.0_DS_ClientPlatform~R` is a Tier-2 DS lane, registered 18:47Z, watcher armed as Monitor task
`b3lc02up5`, **zero crons**. It carries the Andrew-direct ~17:2xZ non-interference rule (no agent on main
fabric disturbs `1.0.0_SA_CTO~X` or `2.0.0_SA_COO~X`; their silence is expected, not a finding; findings
whose SUBJECT is their authored work route to ANDREW, never to the seat -- their commits stay in the triage
population, only ROUTING changes).

**D1_NAMEDISCOVERY (primary):** purpose-level PRD is at
`org/tier2_senior/0.4.0_DS_ClientPlatform~R/deliverables/D1_NAMEDISCOVERY_PURPOSE_PRD_v1.md` @`958c8e4487`
(v2 content, amended IN PLACE -- single home, per this evening's two-homes lesson). **Rule 27 step 2 is
DONE and ratified.** All three scope forks are closed: grain = MODEL/SLEEVE name space with SECURITY grain
OUT (sovereign, `@4b6503cdbd`); ETF population OPEN with the four tickers as named seed members (sovereign,
`@195cfbdbe9`); input population on `1.0.0_SA_CTO`'s architecture default (declared domain = the CLASS of
partner-supplied constituent-name surfaces, v1 coverage = cottonwood's, so a second partner is a MEMBERSHIP
ADD not a schema change) with Andrew's override window open. **`2.0.0_SA_COO` takes the atom-decomp (step 3)
next.** Nothing serves off this and it is not on the critical path.

**ADVI_INSURE (re-seated to this lane `@8155516dbd`):** AC1/AC2 closed BY RULING and NOT by instance --
that discrepancy is deliberate and is the subject of `4776a2305c`. AC5/AC6 PASS. AC3/AC4 behind the sovereign
publish gate. The proof-of-spec instance now lives at
`org/tier2_senior/0.4.0_DS_ClientPlatform~R/deliverables/ADVI_INSURE.TO-R1-DS_PROOF_OF_SPEC.json`
(moved from `~J`, single home, old path gone). **Zero actionable residual.**

**Nothing owed in any direction. Working tree clean on this lane.**

---

## NEXT STEPS

1. **[`2.0.0_SA_COO`]** Atom-decomp of `D1_NAMEDISCOVERY` (Rule 27 step 3), cutting against the MODEL/SLEEVE
   name-space grain. **Do not treat 24 named strings as the complete domain** -- the ETF population is ruled
   OPEN, and a cell measuring a closed 24 measures a set that does not exist.
2. **[`2.0.0_SA_COO`]** The ADVI_INSURE TO-face AC1 self-contradiction -- issuer-owned, still pending.
3. **[a FRESH SEAT, not this one]** The `CLOSED` status-value mint: a Rule 24 enumeration act on a live
   six-value axis with 1,067 rows, changing how `proof-of-spec-check.py` scores 164 instances. Needs the
   four-postulate record, a token census including the substring trap, and an explicit decision on whether
   `status` is ONE axis or TWO (it currently mixes *was it demonstrated* with *is the question settled*).
   Re-run the census first -- it aged inside fifteen minutes.
4. **[`0.4.0_DS_ClientPlatform~R`]** If Andrew rules on the input-population span (PRD s.7.3), fold it into
   v3 -- the document is built so it closes without a rewrite.
