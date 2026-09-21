# AMGT_RESAPP -- round-16 candidate census (the COO's pitch input, NOT an issuance)

**From:** `2.0.0_SA_COO~Z`. **Written:** 2026-09-21 ~15:1xZ at HEAD `74ada19a97` (SITEZ, LOCAL). **Addressed to:**
`1.0.0_SA_CTO~Z` (the round-16 cut is the CTO's analysis to issue, LD-0521) and `3.0.0_SA_CVO~Z` (disposition evidence
for rows with no disarm owner, which are the CVO's to adjudicate, not this seat's).

**WHY THIS EXISTS.** Andrew-direct ~14:58Z at this terminal (record @9bf58c4b95): *"This box is fully devoted to
AMGT_RESAPP, keep that in mind and allocate broadly, you should use as many agents as possible based on dependendencies
of task orders."* The round-15 analysis (@a73b85c64f s.2) states *"every item independent of the three Andrew words that
this seat could name is now closed"*. **This seat tested that claim by SUBTRACTION rather than accepting it:** the
round-14 packet s.5 and the round-14 L9 s.3/s.4 carried **26** row ids to the slug; the round-14 and round-15 analyses
between them cut or explicitly deferred a minority; **1 of 26** carried a disarm row on the channel before this seat's
commit @74ada19a97 (which filed six it owed: S186-S190). The remaining ids were measured at HEAD by **seven read-only
drafter subagents in parallel**, one per write-surface segment (no writes, no network, no AWS, no vendor call; the held
branch `wk-amgt-14-50` was never read -- its changed FILE NAMES were listed by this seat alone, content-free).

## 1. CUT-NOW candidates -- real, reproducing at HEAD, independent of all three reserved words

| # | item | defect, measured at HEAD | write surface | held-branch collision | served output |
|---|---|---|---|---|---|
| C1 | `doc-` accession key (Z-S177/Z-S179 residual) | `lib/research/management/roster.py:831-838` `_is_accession_key` accepts only all-digit names, so a resolved non-EDGAR winner `doc-<sha16>.source.json` is grouped WITH the `UNRESOLVED-SOURCE` placeholder and beats it only because `'d'` (100) sorts after `'U'` (85). Measured: a `Doc-` capital variant picks the PLACEHOLDER. Exposure only today (the one live key with both, 6861_JP_Equity, resolves correctly). **Plus an adjacent, unfiled twin:** `integrations/bloomberg/research/management_posture_batch.py:105` picks with bare `sorted(keys)[-1]` while its docstring `:97-98` claims it reads "the same way roster.py's own load_source_object does" -- false | `roster.py`, `lib/research/management/tests/test_management.py` (+ optionally `management_posture_batch.py`) | **none** -- `wk-amgt-14-50` changes `enrich.py`, `domains.json`, `management.schema.json`, `tests/test_lusha_domain.py` (names only, 9 paths) and not these | none (offline batch code; no infra/Lambda/portal references `research.management`) |
| C2 | `.tools/wk-provision.sh` self-test prunes the REAL repos | `W60-S3`'s remove verb is FIXED at HEAD (`3795d4f487`; `cmd_remove` :200-248 has no prune, :235 recreates the placeholder). But `cmd_self_test`'s own cleanup runs an unconditional `git worktree prune` (:388) and `git -C "$nested" worktree prune` (:397) against the real superproject and portal -- the same hazard class, live every time anyone runs `--self-test`. Matters more under Andrew's word: wide parallel fan-out means more worktrees whose prunable registrations a self-test run clears | `.tools/wk-provision.sh` | none | none |
| C3 | `comp-secrets` output contract | `.tools/comp-secrets:236` `if args.json and not args.reveal:` -- `--json --reveal` silently falls through to the TEXT block (rc 0); `--reveal` text is a 4-line block, so `$(comp-secrets get X --reveal)` captures the block, not the key. 145 occurrences in 70 files; ONE real parser (`lib/research/social/collect.py:183-193`, parses `value:`); no code caller uses `--json` with `get` -> additive change breaks nothing if the default text block stays byte-identical. **ALREADY RULED by the CTO** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_COMP_SECRETS_REVEAL_CONTRACT_20260919T155xZ.md` point 2), **held by that ruling for "a quiet window or Andrew's word"** -- the hold is the CTO's own, and the fix does NOT depend on the credential rotation (the ruling itself says no comp-secrets change would have prevented the leak) | `.tools/comp-secrets`, new `.tools/tests/test_comp_secrets.py` (stubbed client, a sentinel value -- no real secret ever printed) | none | none |

## 2. CTO-RULING-NEEDED -- real, but a contract/design/budget question comes first

| # | item | the question the CTO decides | cuttable piece if ruled |
|---|---|---|---|
| R1 | `W54-S2` crosswalk read is UNPINNED | `lib/research/identity/crosswalk.py:706-723` `_read_pool_latest()` reads `sorted(keys)[-1]` over `crosswalk/v1/` with no key-shape filter (a `latest.json` would sort after every dated file and WIN). Callers include the PAGE ROUTE (`scoped_amgt.py:1729`, `:1773`) and `management/batch.py:92` (newest on purpose). PRD `:1617` names the population but not the vintage rule. **Rule: "newest, recorded on the answer" vs "fixed by the order/environment."** | Independent of the ruling: a key-shape filter (`^crosswalk/v1/\d{4}-\d{2}-\d{2}\.json$`, loud on anything else) in `crosswalk.py` + `tests/test_crosswalk.py` (baseline 19 passed). NOTE: the `run_scores.py:81-92` copy of the same logic is chain P -- HELD, leave it. Reaches the served plane only on the next adapter redeploy (never-widen pair then) |
| R2 | `W54-S1` five no-lookup-key names | CAT/CSL/Keyence are SUPERSEDED (MEASURED in `registrations.json`, @0add9d26c1). AAPL, NVDA, MSFT, JPM, TSLA: 0 hits in `registrations.json`, 15 in `~4/universe.json`. **Rule: are these five in scope?** If yes, `add_security` needs a Bloomberg call + a crosswalk pool write | none until ruled |
| R3 | `W42-S4` finding-language rule, zh/ko unproven | The fix is IN (`analyze.py:226-235`, `PROMPT_VERSION rj6-two-pass/3`). Chinese and Korean never exercised. **Rule: is a budgeted live check worth it** (one PASS-1 run per language, ~USD 0.45 each, bar VERBATIM-CHARS >= 0.90)? This is an Anthropic API call -- vendor egress, so a yes needs Andrew's per-use word as well | a single live-proof cell, if both words land |
| R4 | `S169` (surfaced again by `W57-S2`'s check) | `surprise-row-gate.py --acceptance AMGT_RESAPP --round 13` -> `PASS 26 / FAIL 3 / UNVERIFIABLE 3 of 32`; rk-20 AC1, rk-23 AC1, rk-30 scores-adapter AC1 read FAIL while their orders are terminal on a VALID proof instance. **Rule: grade-vs-terminality policy** | none until ruled |

## 3. HELD -- on a reserved word, unchanged

`W37-S1` (the registry gate: `nm.address('sec','harvest','bronze',...)` -> `opal-data-assets`; `tiers.json:19-20`) is the
bucket/tenancy word verbatim, and its write surface collides with held cell `rk-32` (`build_universe.py`). `W49-S2`,
`W49-S4` sit behind the Bright Data word (the code is built to the STRICTER reading, `require_verified_domain=True`,
`ceo_search.py:459/:512`; the step-7 wording question belongs to rk-48's live re-open section).

## 4. NOTHING-TO-CUT -- disposition evidence for the CVO (no disarm owner on these rows; closing them is L9's)

| row | evidence at HEAD |
|---|---|
| `W42-S3` | fixed by rk-40's worker @`2e388452dd`: `analyze.py:583-595` `range(start_block, end_block)` (exclusive end, SDK semantics), `:598-607` joins multi-block citations; `pytest ... -k PrecutCitationBlocks` 2 passed |
| `W42-S7` | fixed: `drafting_build.py:314-317` carries `text_translated`/`translation`; `drafting/pipeline.py:173` keeps the dict; `pytest ... test_translation.py -k DraftedSentenceCarriesTranslation` 1 passed. Whole filings+drafting suite 91 passed |
| `W38-S3` | criterion defect of terminal rk-34, repaired @`361c3aaa90`; `scoped_amgt.py:2002` serves `model_status` top-level, `:2011` also nests it (rk-36); every portal reader uses the top-level key |
| `W39-S1` | criterion defect of terminal rk-35, repaired @`0f6e7ae2fa`; the row's own evidence measured 0 movement on the 33 covered names |
| `W59-S1` | criterion defect of terminal rk-59, repaired @`aec251f0b7`. (A cosmetic `terraform fmt` hunk remains at `chatter-axis-schedule.tf:114-116`; not cut -- no FWD served, and "no cell is cut for coverage alone") |
| `W60-S3` | remove verb fixed @`3795d4f487` (the row's own measured defect). **The round-14 L9 s.4 item 7 (`:116-120`) still calls it "unrepaired" -- stale at HEAD.** The residual self-test hazard is C2 above, a separate item |
| `W57-S1` | criterion defect of terminal rk-57, repaired (AC2 now uses rk-20 AC1 as the control); `.tools/tests/test_acceptance_sweep.py` 0 of 7 failed |
| `W57-S2` | record-face gap, repaired (rk-20/rk-23/rk-30 carry `<round>13</round>` with comments citing W57-S2); `--acceptance --round 13` rc 0, unrounded 0. Residual is R4 |

## 5. Pending

Drafter F (the management segment: `W44-S1`, `W46-S2`, `W48-S1`) had not reported at this write; its result is
appended below when it lands.

## 6. This seat's REC

1. **Issue round 16 now with C1 and C2** (independent of every word, disjoint surfaces, no served output, offline proof),
   plus **C3 if the CTO lifts its own hold** -- Andrew's word names allocation, not this specific change, so this seat
   does NOT read it as the "Andrew's word" the comp-secrets ruling waits on; the "quiet window" half is the CTO's to
   judge, and this box is dedicated to AMGT_RESAPP right now.
2. **Rule R1** (vintage contract). This seat's REC: newest-wins stays (batch.py depends on it) but the resolved key is
   RECORDED on the returned document and the key-shape filter lands now -- cut as a fourth cell. R2/R3/R4 are
   Andrew-adjacent or policy; park or rule at the CTO's discretion.
3. **Fan-out:** C1/C2/C3(/R1-filter) are pairwise disjoint (roster.py; wk-provision.sh; comp-secrets; crosswalk.py) --
   one wave, every cell spawned at once, no chain. The width is small because the independent backlog is small, not
   because of a cap.
