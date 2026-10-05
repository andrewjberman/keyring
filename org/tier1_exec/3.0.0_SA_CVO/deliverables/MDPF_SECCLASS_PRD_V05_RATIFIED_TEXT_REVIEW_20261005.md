# MDPF_SECCLASS PRD v0.5 -- ratified-text half review (3.0.0_SA_CVO, 2026-10-05 21:1xZ by `date -u`)

Delivered by `1.0.0_SA_CTO` msgs 105389 and 105390. PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`
@de649aa5b6 (prd_version v0.5), half hash 70f99f49abc1. Diff read whole against the v0.4 this seat signed (@ee234fc3d7).

**Verdict: REFUSE, on two lines of form. Each is a one-line fix; the outcomes themselves read right.**

## The two lines

1. **History inside the ENDPOINT block.** FWD-6's SOURCE (PRD lines 83-85) now ends: "amended 2026-10-05 on Andrew's word
   ("consolidating sector onto this table"): Positioning's ETF view is no longer a declared exception (FWD-12)". That is
   a dated account of what changed, and the hash binds it. The addendum at the file's end already says it (line 419).
   Fix: let the SOURCE name the word and stop there.
2. **A seat serial inside the ENDPOINT block.** FWD-12's SOURCE (PRD line 155) reads "his word at the 4.0.0_SA_CRO
   terminal". Fix: name the record or the date, not the seat.

Both are the form check this seat applied to IRPT_YCDGEN v0.2 an hour earlier (review @3bd1104913, line 1).

## The checks

| check | this seat's read | result |
|---|---|---|
| ENDPOINT against the signed v0.4 | The block (PRD lines 24-159) changes in two places: FWD-6's ACCEPT and SOURCE, and the new FWD-12. FWD-1 to FWD-5 and FWD-7 to FWD-11 are byte-equal | PASS |
| FWD-6 amended within his word | ACCEPT drops "Positioning's ETF view or" and keeps the Schwab firm data. His 204xZ word at the other terminal names "Positioning page tables" and says "ONLY the canonical ETFClassifier table"; his 21:05Z word takes option (a), a sector field on the table with the ETF view moved onto it. Removing the Positioning member follows both | PASS |
| FWD-12 within his word | "I am ok with consolidating sector onto this table" carries the outcome and the first ACCEPT sentence. "The list holds no measurements about a security" carries "the characteristics ... which I'd prefer they were not". Both quotes in SOURCE equal the two records character for character | PASS |
| no annotation, history or seat name inside the section | one history clause and one seat serial (the two lines above) | FAIL |
| every operative constraint present | a new closed-value attribute arrives with its four-postulate record and token census (C-SECTOR, rule 24); the page move is a served-output move with a before and after list (C-SERVED); no measurement enters the table (C-NOCHAR); the Bloomberg file is an input already held, so no new vendor call; seed precedence kept | PASS |
| times on the records | the 21:05Z record and the addendum each state a clock read (21:05Z, 21:06Z); the commit is 21:06:56Z. Row ESTATE_GOVERNANCE-S37's lead is not present here | PASS |
| cited code | not re-read: `etf_positioning_gold.py:986-1009`, `:1208-1219`, `:121-150` are the author's measured lines; the CRO's check @35859eb97d section 2.2 names the same producer at `:1219-1249` | NOT RE-MEASURED |

## Notes (not conditions)

1. **The Schwab exception and "ONLY".** The addendum keeps the Schwab firm data as a declared exception "since no word of
   his names it". His 204xZ word names two pages "and anywhere else where we are surfacing holdings in this form", and
   says "I do not want holdings being displayed from any other table or going through any other process". Whether the
   Schwab firm composition is such a surface was not in the CRO's five. That is his to say; this seat reads neither the
   wider nor the narrower meaning into it.
2. The same word reaches the Investor Reporting Holdings tab's fallback (the check's largest finding: 22.7 percent of
   Cottonwood's holdings value labelled outside the table). The placement note homes it under FWD-4, FWD-5 and FWD-11
   and adds no outcome. No ENDPOINT line names that tab.
3. `industry_group` stays on Bloomberg's path "until Andrew says". Under "ONLY" that is a second open question for him,
   and the addendum says so.
4. C-NAMES (line 185) still reads "No new S3 address is created" (v0.4 note 2).

-- 3.0.0_SA_CVO
