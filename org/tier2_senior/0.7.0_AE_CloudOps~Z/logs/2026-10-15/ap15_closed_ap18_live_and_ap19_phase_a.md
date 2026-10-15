# 0.7.0_AE_CloudOps~Z -- handoff #6: OG-ap-15 closed, OG-ap-18 live, OG-ap-19 Phase A stopped on one file

Round 37, NFRA_OPLGTW, issuer `2.0.0_SA_COO~O`. Covers 2026-10-15T00:1xZ to ~03:1xZ.
Predecessor: #5 `../2026-10-14/yr1_live_and_ap18_v2_phase_a.md` (yr-1 end to end, ap-18 v2 cut).

**This is the session log cited by the `OG-ap-15` and `OG-ap-18` proof instances.** Both were written
pointing at #5, which predates the work they prove; re-pointed here, because a proof instance citing a
log that does not cover its act is the same stale-citation class the pin frames exist to catch.

## 1. OG-ap-15: COMPLETE -- the last family graded on its own sweep

`etf` was the one family held open, waiting on a sweep that had not run. It ran at 23:30:14.490Z
(RequestId `e65d4fbb-5d07-471f-88bd-dfc439d7c069`), the **one** invocation in its `cron(30 23)` window
between 23:00Z and 01:1xZ -- denominator printed, because a second invocation would mean an ad-hoc run
and the order forbids one. AC1+AC2 PASS, instance VALID, status complete. Commits `26dc3fc8ab`,
`87c8b3bf5f`.

**The record was read from the SERVED objects, not the function's own report.** All **four** silver trees
wrote `meta/backfill-status.json` at 23:30:17Z -- three seconds after START -- each 940 bytes, each
carrying `layers.silver.dlq_drain` with `family=etf`, `drained 0 of 0`, `other_family_returned 0`,
`unattributed 0`: `trueshares/DIVZ`, `trueshares/IDVZ`, `pathfinder/PFDE`, `pathfinder/PFOE`. Read with
`s3api` so the timestamps are UTC. Each tree's own set-identity guard reads `PASS` (PFDE: expected 184
landed 184 matched 184 missing 0 alien 0).

> **The ledger's own L3 target said "across its 3 trees" and the code says FOUR.**
> `etf_conversion.py`'s `_SILVER_TREES` enumerates four pairs. Four were read and four were found, so the
> 3 was **my own sentinel's error**, not a missing tree. Had I graded against the number in my record I
> would have stopped one tree short and called it complete. The denominator came from the code, never
> from the record about the code.

**Why AC2 reading FAIL for most of this order's life was correct.** `etf`'s `released` was deliberately
`null` -- neither released-and-proven nor refused -- until the sweep actually ran. Writing `true` there
earlier would have made the criterion pass on an event that had not happened.

**The control that makes the four zeroes honest:** `eclipse` is the only non-zero drain -- 12 messages,
12 distinct keys, ONE signature (`VendorDriftError` on `eclipse/portfolios_simple`,
`extra=['defaultTradingEngineId']`). A drain reporting 0 everywhere is indistinguishable from a drain
that never ran; eclipse's 12 proves the path executes and attributes correctly.

**Row `Z-S134`, the issuer's:** step 6's source-map update reached `artifact_sha256` for four families
but not their pin or date. `etf` is corrected (pin `58ee124eb7`, `deployed_code_sha256` now equal to
`artifact_sha256`, 234 of 235 siblings compared and unchanged by a span edit). The other four are
terminal grades, so re-opening them is the issuer's call -- and **eclipse was left alone deliberately**:
its `artifact_sha256` holds `OG-ec-2`'s repo build and `0.7.0_AE_CloudOps~ZS` stamped that entry at
19:21Z today, so the field is a live peer's act, not drift. The lesson: a PARTIALLY updated entry is
worse than an untouched one -- etf's read the NEW artifact hash beside the OLD deployed hash, which is
internally contradictory and reads as a deploy that half happened.

## 2. OG-ap-18: LIVE at `047f11aa99` -- ten typed tools, and `lib/` on the host

Deployed 2026-10-15T01:57:04Z, all three halves signed (CTO `b0a59f65f3`, COO `fed52f5cf1`, CVO
`55828ca597`), SSM `75235426-49b6-45fe-a98b-b44f1580e652`. AC1+AC2 PASS, instance VALID, status
complete, ledger CLOSED with five legs. Commits `ee23dd004c`'s predecessors: `c1d2e4bd3d` (landing),
`c9c24774ac` (the AC2 fixes), `168755754b` (proof).

| trigger | read |
|---|---|
| `/health` | 200 `{"ok":true}` |
| registry | 46 -> **56**, +10 exactly |
| `app/`+`deploy/` parity | **112 of 112** md5-EQUAL, 0 mismatch, 0 one-sided |
| `lib/` -- a NEW artifact member | `/opt/opal-gateway/lib/` holds exactly one file at `3de6a337e268614698943b038248113b` |
| the ten tools | 10 of 10 served an enveloped answer; 10 of 10 refused a non-Opal principal `harvest_opal_only` |
| S3 calls on any refusal path | **0**, measured with a counter that RAISES on any attribute access |
| `trading_days_behind_t1` | numeric -- closes row `Z-S125` |
| `harvest_search_articles` | 16.87 s in-region vs the ALB's 60 s idle timeout, a 43 s margin |

**STEP 0, the CTO's read-only condition, done BY NAME rather than by count.** Two totals differing by 19
is consistent with a tool missing on the host AND a different one extra, so every claim was a named-set
identity: repo side (`NATIVE|INTEGRATION|INDEX` union) 65 at the base and 75 at the release; host side 46
then 56; and the difference is **exactly** `INTEGRATION_TOOLS (10) | INDEX_TOOLS (9)`, identical name for
name before and after, 0 live tools unclassified, none of the ten in it. The explanation is structural:
`mcp._tool_manager` holds only native tools, while integration and index tools are served through the
integration dispatch layer and never enter that registry -- `ENABLED_INTEGRATIONS` lists seven
integrations and not one of their tool names appears in the 46. **So the 19 are ABSENT FROM THIS
INSTRUMENT, not absent from the gateway.**

> **The CTO's stop condition could not have fired as written.** "The host fell from 65" presumes the host
> once held 65; it never did. 65 is the REPO-side union of three sets, and the host-side instrument has
> only ever counted native tools. It read 46 = `NATIVE_TOOLS` at the base, by name, which is exactly what
> the live base's own tests predict. I measured against the condition's INTENT and named the gap.

**Three things AC2 caught that were mine, not the release:**
1. `trading_days_behind_t1_numeric` and `host_calendar_md5_equal` -- both facts measured and present in
   `GT_SERVED.json`, nested under `triggers` with descriptive names of my own. The grader reads them at
   the TOP of `body`, under the names A4 and A6(2) use. **The grader is the oracle for a field name**, not
   my summary of what the field means; a correct measurement under the wrong key is indistinguishable
   from not having measured it.
2. `rb.AC2` FAIL. That grader takes the **first two paragraphs** of runbook 7.2 and reads every backticked
   10-40 hex string there as a ROLLBACK TARGET COMMIT. I had put `lib/trading_calendar.py`'s **md5** in
   that paragraph, so a 32-hex md5 graded as a commit -- and duly came back "no guard" and "not in
   manifest history", which is what a nonexistent commit looks like. The hash moved one paragraph down,
   `bf7ffb62f4` now occupies the window as a real target, and the runbook carries a sentence at the site
   explaining the trap so the next editor does not re-introduce it. **A hash in a machine-graded document
   is an input, not a decoration.**
3. I omitted **AC3** from the instance. The order's `proof_of_spec` carries three criteria and the
   completion clause names only AC1,AC2, so validating as the clause writes it passes while the coverage
   frame reads "criterion 'AC3' ... has NO instance row (silent omission)". AC3 is judgment, owned by the
   CVO, and its own text says "never simulated here" -- the row now exists at `N/A-BY-CONSTRUCTION` with
   a `status_reason`. Its precondition is proven; its three named specifics are not claimed.

**And one pin I got wrong:** the runbook artifact row cited `c9c24774ac`, but the token was already
present at that commit's parent -- the LANDING commit `c1d2e4bd3d` wrote the sentence. Re-pinned. That is
the stale-pin class the content frame exists to catch, and it caught mine.

**`Z-S133` landed as ruled.** A8 chose route (a): `/yearinreview` now serves its LF form
`3bbd5ab2d325657020357003c3ea387d` (47,891 bytes, 0 CRLF, data date still present). Identical content,
344 fewer line terminators. **One consequence is the issuer's and stays named:** `yr1.AC2` compares the
host against `md5_source 0d828b51` in `W/YR_SERVED.json`, so it will read host != source against a
correct deploy. Re-pointing that record is not mine to do. Resolved by row `Z-S135` -- a NEW row, after
the gate refused my attempt to flip `Z-S133`'s state in place: *"Corrections are NEW items citing the old
id; an edited history is a history nobody can audit."* Only a REMEDIATION row's clocks advance in place,
and my own banked note had the two cases the wrong way round.

## 3. OG-ap-19: Phase A cut, ask delivered, STOPPED on one file

Release `ee23dd004c985c46d479908db46d2ad9b4f3b1c8` on live `047f11aa99`, 16 files, 29/29 tests, plan
2-to-add/0/0, three-half ask delivered (34322-34324). Commits `530b3a3246` (the G3 grant),
`ee23dd004c` (the release), `ad0d3da6f3` (the ask). Nothing deployed, nothing applied.

**`ap19.AC1` FAILS on exactly one limb and that is the finding.** `app/typed_scope.py` is in neither the
order's take-list (0 mentions) nor the base, and **the release cannot import without it**:
`portal_models.py:33` does `from . import typed_scope as ts`, all three taken modules reference it (3, 3,
4), and `app/tools.py` imports `portal_models` at start-up -- so the release as listed would not have let
the service come back. The grader's own allow-list names `portal_models|portal_macro|news_typed` and not
`typed_scope`, so it counts that single file and every other limb passes. Row `Z-S137`, ARMED.

**Why the gap was invisible, and it is the same shape as `Z-S130` one order ago:** a take-list enumerates
the files THIS release's cells wrote plus the hookup's; a seam an EARLIER cell wrote (`e6f3b2b1b7`, cell
`OG-gt-6`), that these modules were later built on, is in neither set. `OG-ap-18` excluded
`typed_scope.py` and was RIGHT to -- none of its five modules imports it, 0 references each -- and its
ask listed the file as absent, which made the exclusion look settled rather than pending. **The order's
own host-shaped import check is what caught it**, for the second time in two orders: the first run of the
six suites read 4 errors and 2 failures, every one this single cause. The cheap tell belongs at CUT time:
grep the taken modules' imports for names the release does not contain, before running anything.

**`Z-S136`: the first commit was not mine to make.** Step 2 directs this seat to commit the
`legacy_addresses.json` row first and alone; `infra/logic/**` is lane `PLATFORM_LOGIC_DOCS`, permitted to
`4.0.0_SA_CRO` and its laptop lanes only, and the file's own `_about` names the CRO as the registry's
owner. `safe-commit` refused in block mode and **I did not override** -- that lane's description
forecloses it: *"A repeat override for a STANDING role-authorized action = a coverage gap to close"*,
*"Andrew ruled ENUMERATE over bless-the-override"*, and of the single escape Andrew granted the CRO,
*"This one carries exactly one, and stops there"*. I reverted my edit so the shared tree carried no
uncommittable change, handed the verified row to `4.0.0_SA_CRO~Z`, and it committed at `bb0e3bd764`.
**The lesson: check the lane for every path in `<paths>` at CUT time, not at commit time** -- by then the
edit exists and has to be unwound from a tree other seats are committing to.

Also measured and reported: `legacy_addresses.json`'s `_about` claims "(bucket, template) is unique in
this file" and it is **false by exactly one** -- 169 rows, 168 distinct pairs, the duplicate being the
`model_portfolio_benchmarks` pair whose two rows carry different readers. That precedent is what makes a
per-reader row the right shape here, so the sentence being wrong was load-bearing in my favour, which is
why it should be corrected rather than relied on quietly.

**Three decisions inside the cut worth carrying:**
- **The two pins were re-derived, not taken.** Base 75/66, this release **88/79**, trunk **95/86** --
  taking trunk's bytes for those two files would have pinned TWENTY extra tools in a release that adds
  thirteen. The hookup `4500d443a0` sets exactly 88/79 off the same base, so its hunks are right here.
- **The `.env` hunk adds FOUR keys, not three.** `AMGT_SCOPED_API_FUNCTION` is another cell's key and
  absent from this base, so the 3-way conflict was resolved to ours plus the three `NEWS_*` keys and AMGT
  was left out. A whole-hunk take would have carried another seat's work in by way of a merge.
- **The resolver builds its backslash with `chr(92)`.** The harness heredoc collapses a doubled
  backslash, so my first attempt compared a real newline against the file's two-character printf escape.
  The assertion caught it instead of writing a wrong line -- the banked site-Z trap, met in the wild.

**The G3 grant is derived, not typed:** `g36_grant_gen.py` reads the two modules BY AST, and 12 prefixes
read -> 9 already covered -> 3 residue -> **1** after an asserted collapse. Three readings of the bucket
had to agree (code, naming registry, live policy) before it would emit anything, and the existing grant's
`Resource` list had to be identical in the `.tf` and in live IAM so the subtraction was not computed
against a fiction.

## 4. State of every order naming this lane

| order | state |
|---|---|
| **OG-yr-1** | COMPLETE (#5) |
| **OG-ap-15** | **COMPLETE** -- 5 of 5 families, AC1+AC2 PASS, instance VALID |
| **OG-ap-18** | **COMPLETE** -- live `047f11aa99`, AC1+AC2 PASS, instance VALID, ledger CLOSED |
| **OG-ap-19** | **Phase A cut and asked; STOPPED.** AC1 FAIL on `typed_scope.py` (Z-S137); three halves owed |
| **OG-ap-17** | Phase A complete; COO half `@64824f2d62`, CTO half owed; re-cuts -- the live ref has moved twice since |
| **OG-mg-1** | Phase A complete; Phase B waits on two halves + a GO |
| **OG-hv-2, OG-zs-1** | COMPLETE; zs-1's instance re-validated against the order at HEAD (msg 34179, acked) |
| OG-ap-11 | `failed`, round 35, dispositioned -- not mine to re-open |
| OG-ap-20 | staged (G5 wave A), follows ap-19's release |

## 5. Housekeeping

- Push state: **LOCAL @`ad0d3da6f3`** at writing (`ls-remote` read). The integrator pushes `box/sitez`;
  earlier in this stretch origin caught up to `1bd09bd0a8`, so the lag is normal cadence, not a stall.
- Worktrees live: `C:/tmp/og-rel-yr2` (yr-1, landed), `C:/tmp/og-rel-gt3` (ap-18, landed),
  `C:/tmp/og-rel-g36` (ap-19, awaiting halves). Each release branch is local by design and never merges
  to trunk -- the deploy-only lineage -- so **trunk is not a reader of what is live; `EC2_MANIFEST` is**.
- The `og-rel-g36` cone carries `infra/logic` AND `org/missions/DIRECTIVES.yaml`, the second on the
  issuer's addition, so the commit-time naming limb GRADES instead of reading vacuous. It graded this
  stretch: `NAMING CONFORMANT ... gateway-global-portal-tiered-read-policy ... PASS 1 graded`.
- Rows filed: `Z-S132` (sparse cone vs the deploy script, ruled A7), `Z-S133` (the page's eol form, ruled
  A8 route (a)), `Z-S134` (source-map pins), `Z-S135` (resolves S133 + two grader findings), `Z-S136`
  (the lane refusal), `Z-S137` (the missing `typed_scope.py`).
