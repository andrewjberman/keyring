# L4-R REVIEW -- AMGT_RESAPP PRD v0.42 @6eda215ac4, ratified-text half -- REFUSE

**Reviewer:** `3.0.0_SA_CVO`, substituting for `3.0.0_SA_CVO~Z` (the lane owed the half; no live session). **Delivery:** `1.0.0_SA_CTO~DELL1`
msg 5022. **Prior signed:** v0.41 @b5f90bbf8d (half_hash ff51e26ae300, endpoint_hash 58aef047a6cc, `3.0.0_SA_CVO~Z`, 2026-10-06).
**Reviewed bytes:** `git show 6eda215ac4:org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` (equal at HEAD e457a025b9: the file's last commit is
6eda215ac4), ratified-text half_hash **a337e56d195aad79596d3f6e5dc0eae728db0a1feec7bb8c049303cb63f6e9f9**, endpoint_hash 1ccf18950c08
(`prd_signoff_lib.half_hashes` / `endpoint_hash`; `prd-signoff.py status` reads the half STALE against 58aef047a6cc).

## The change

`git diff b5f90bbf8d 6eda215ac4` on the PRD, read whole: 115 lines, two commits.
- **9bac67f9d0** (CTO~DELL1, 10-08): the header's `fabric` site-z -> dell1. A header-only change.
- **6eda215ac4** (CTO~DELL1, 10-13):
  - the header's `prd_version` v0.42 and `endpoint_outcomes` + FWD-40, FWD-41;
  - the two new FWD blocks in ENDPOINT (`:1109-1148`);
  - ADDENDUM F at the end (brief half).

Nothing else in ENDPOINT or CONTRACTS moved. No existing outcome's text and no contract changed, as ADDENDUM F states.

## Against the record this seat has graded under (AMGT_RESAPP rounds 89-102)

- **FWD-38's standard** (a figure within one trading day of the header, or the page says why; the CTO's rendered-page read): FWD-40 (a)
  "content OR a stated reason" is consistent with it.
- **Self-peer exclusion** (ss-3, REMEDIATED at ADJUDICATION_v113): untouched.
- **Minor-unit currency** (qq-1, C-S55 REMEDIATED at v112): untouched. (a)'s "0 broken values" would catch a relapse if it were defined (item 3 below).
- **Classification withheld for a disagreeing table row, sector by listing key** (aa-2, bd-1; v115, v118): "content OR a stated reason" admits
  the withheld-with-reason form.
- **The first overlay on a container costs about 20 s, 91 percent of it the feed phase** (C-S112, C-S113; W402-S1 graduated ARMED at
  REMEDIATION_v39): FWD-40 (b) makes that an outcome. It is consistent, but see items 1 and 2.

There is no contradiction with a ruling graded here. The refusal is on gradeability and on the no-wait rule.

## FWD-40 -- what is gradeable as written, and what is not

1. **(b) is a wait, unqualified.** "The FIRST request of a trading day, on a container that has served nothing" can be produced once per
   trading day, after the 12:30Z snapshot write, and only if no seat or user has touched the function first. Rule 27 L2: every outcome
   is provable by an act a seat can take on demand, or the wait is "expressly qualified on the outcome with its reason and Andrew's word".
   (b) is neither.
   **Fix:** state the drivable form as the grade. The CTO accepted it in round 102 for the feed cell's close: "a first request on a new
   package, cold by construction, driven alone", or a container past the idle recycle. Keep "the first request of a trading day" as a
   corroborating arm. Also state whether "under 3 s" is the handler time (REPORT Duration, which the per-phase lines sum to) or the
   client's latency (Init, about 0.6-0.7 s, sits outside the handler).
2. **(b) and the addendum's "keep one instance warm" cannot both hold.** A kept-warm instance has served something, so it can never be "a
   container that has served nothing", and the arm would be graded on a different, fresh container. Round 102's measurement also shows
   that the 20 s is the first OVERLAY on a container, not its first request: a keep-warm that does not run an overlay leaves it in place.
   **Fix:** either drop the keep-warm option, or word (b) so that it grades a keep-warm: the first overlay of the day on the warmed
   instance, the warm-up's own work declared, with its denominator.
3. **(a) "0 broken values" is defined nowhere in the PRD** (`grep -i broken` finds only `:1988` S8 "BROKEN TODAY" and prose at
   `:2016`). This is the ADVI_BDPRCE ground: a DONE WHEN that counts a class the PRD never sets.
   **Fix:** define it or cite the instrument that counts it. For example, the ui-walk classes `unconnected-field`, `raw-code` and
   `format:money`, plus the minor-unit census, with "raw codes" as FWD-5 already uses the term (`:536`).
4. **(d) "a browser walk of a drawn sample on PROD"** has two gaps:
   - no sample size is set;
   - the estate's walker refuses any base URL that is not `localhost` (`.claude/skills/ui-walk/SKILL.md`, safety model). What it can
     walk is a local build at a stated commit against the live services.

   **Fix:** set the sample (n, how drawn), and say "the PROD build" as the commit walked, or name another instrument.

## FWD-41 -- what is gradeable as written, and what is not

5. **"every other thin high-profile text block (the hard thesis items) is filled"** names a set the PRD never enumerates
   (`grep -i "high-profile\|hard thesis"` finds only `:1137`). The census of "source class per name per block" has no denominator of
   blocks until it is.
   **Fix:** list the blocks (or cite where the list lives at a pin). The management bio and recent-developments blocks are already named.

The rest of FWD-41 is gradeable and provable on demand: a census run, five names read on PROD by the CVO, the source class and
citations per block, FWD-9's machine-written marking, and the existing Anthropic path with its server-side web search tool. Andrew's
word is quoted ("We can use anthropic path").

## Recorded, not blocking

- **Names and addresses (rule 30):** v0.42 types no new S3 address or resource name. The AI fill will write stored objects (the fill's
  outputs, any re-enabled site-Z task's keys). Each must be `lib/opal_naming.py address()` / `name()` output at the cut, and the pair
  that carries it cites the builder output.
- **The BAR DISTRIBUTION line** (`:1151`, "19 of 20 are EXERCISED; only FWD-9 is APPLIED") predates v0.42 and is stale against the
  41 outcomes. Restate it at the next PRD touch.
- The header's `fabric` change and the brief-half ADDENDUM F re-open nothing on their own. The ENDPOINT change does.

## Verdict

**REFUSE**, ratified-text half, at half_hash a337e56d195aad79596d3f6e5dc0eae728db0a1feec7bb8c049303cb63f6e9f9.

The re-sign needs five things:
1. FWD-40 (b) driven on demand, with the measured time (handler or client) named;
2. (b) reconciled with keep-warm;
3. "broken values" defined;
4. (d)'s sample and walked build stated;
5. FWD-41's block list.

Each is a wording change inside the two new blocks. No graded ruling stands against the outcomes themselves.

-- 3.0.0_SA_CVO (for 3.0.0_SA_CVO~Z)
