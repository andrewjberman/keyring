# DSGN_AMGTV1 task order -- `AV-zzm-3` -- THE NEWS LIST IS RANKED BY THE SERVED MENTIONS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzm-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~133</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal e6fb269c (= origin DEV, round 60) -- r61c.cjs 2 of 3 (arm 1 FAILs as expected; arm 2 holds at the base as the guard; PLANTED passes); battery29 ALL PASS at the base (round-60 close).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzm-3` (round 61, decomposition v61; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round60.md` section 3 first. Do the items in this order.

The /overlay feed now serves `mentions` on each item (AMGT_RESAPP round 82, live): the gold row's mention count, or `null` when none
is counted. `components/HeaderBrief.tsx`'s `mergeNews(topItems, feedItems)` ranks only the top-band items by mentions today, and
`feedRow` sets every feed row's `mentions` to `null`.

1. **The type** (`types.ts`, `CoverageItem`): add `mentions?: number | null`.
2. **Carry it** (`components/HeaderBrief.tsx`, `feedRow`): a feed row's `mentions` is the served value when it is a number, else `null`.
3. **Rank one list** (`mergeNews`): top-band and feed items together, in descending served `mentions`. An item with no served mentions
   follows every mentioned one; among equals, served order holds (top band first, then feed, each in served order). A headline is still
   kept once (by url, else title), the first kept being the higher-ranked. With no served mentions anywhere the order is exactly today's.
   Update the doc comment over `mergeNews` to say this.
4. **The why-line** is the existing `Mentioned N times` beside a row (`data-news-mentions`); it now shows for feed rows too. Draw nothing
   else about the ranking: the feed's `most_discussed_basis` and `order` strings are not shown.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text; never compute a figure the page does not serve** (C-PRESENTATION-ONLY).
   `reasonWords.ts` and `cscTable.ts` are not yours. No non-ASCII characters (use `--`). Keep each file's line endings as you find
   them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion. In particular, if battery29 goes red on a
   harness file outside your paths, file a row naming the harness and the assertion, and stop: the issuer rules it.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~133/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/research/api/tests/test_r82_reason_and_mentions.py` (the served shape), and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round61/checks/r61c.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzm-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round61/checks/r61c.cjs"; echo "exit=$?"</invocation><expect>ROUND 61 NEWS RANKED BY MENTIONS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzm-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzm-3" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): AMD's News tab opens on its most-mentioned stories, each saying how often it was mentioned.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~133/DSGN_AMGTV1.TO-AV-zzm-3.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-61 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W133-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 61 = `ledger/ROUND_ANALYSIS.round60.md` @0b03adc339 section 3 (four items; items 1-2 are repairs, batched into
`AV-zzm-1`; items 3 and 4 are build cells `AV-zzm-2` and `AV-zzm-3`). Requested on UB-20261009T091009Z-b711 act 1. Base portal
e6fb269c (= origin DEV). The three cells' write surfaces are disjoint; only `AV-zzm-1` holds `__harness__/`.

<status>complete</status>
<round>61</round>
<to_id>DSGN_AMGTV1.TO-AV-zzm-3</to_id>
<slot>~133</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
