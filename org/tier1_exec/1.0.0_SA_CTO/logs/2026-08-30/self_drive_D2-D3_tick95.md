# /self-drive D2 & D3 — tick 95 (2026-08-30 15:1xZ; covers ticks 94–95) — state: ARMED

Covers the acts since the tick-93 log (`d55f2a2192`, ON origin — the 14:43Z CLOSE @`1befd43cef`; origin now
@`bbdaa9fdc8` at the 15:07Z CLOSE, own is-ancestor read). Tick 94 (14:39Z) wrote nothing. Cron `1c261f82`
:07/:37 (the 15:07Z fire folded into this stretch). Paired `/drive D2 & D3 @ 2.0.0_SA_COO` (its ticks 19–21).

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete). Open TOs **26** at the 14:39Z read (D2 22 + D3 4); since
then INF-RECORDER-SCOPE CLOSED at the grader (−1) and INF-DRIFTCENSUS cut (+1). Ledger **19 / 0 unconsumed**.
Acked READ since the tick-93 log: 87938, 87943, 87950, 87974, 87976, 88000, 88017, 88026, 88034, 88036,
88039, 88045, 88066, 88071, 88073, 88079, 88090, 88094, 88097, 88100, 88104, 88117, 88121, 88123, 88146,
88167, 88171, 88177, 88181, 88185.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 8** — R1–R5 unchanged; R6 the C02-g-11 card (AE~L files R-1); R7 CARRIED to Andrew
at 14:30Z as REC YES; **R8 new** — five scratch S3 objects under `s3://opal-data-inf/_scratch/indexbytes-face/`
(~15 KB, no reader; AE~K correctly did not delete; citation Agent Autonomy "S3 deletes"; REC YES, folded onto
R7's card as a second line).

## Verdicts since the tick-93 log (§3)

**0 on pitched calls.** Grades read, each on the grader's own instrument:
- **CVO 88034 / 88104: C02-g-13 V-1 + V-2 PASS; V-3 PASS (the 1,080 limit COUNTED); the V-4 deploy limb PASS
  on the object** (served a07 ETag `e0bde0a5…` == the index blob at 1befd43cef, third-call read); V-4
  UNCOMPUTABLE until Tuesday's second fire — one fire cannot separate a deterministic digest from one that
  ran once.
- **CVO 88071: OPAL_ADVIPOINTERS.INF-RECORDER-SCOPE CLOSED at the grader** (the arms re-run on the grader's
  instrument; the drift finding routed).
- **CVO 88097 → 88171: INDEXBYTES-DEPLOY NOT MET AS WRITTEN (the fix uncommitted) → the fix PASS at COMMITTED
  @`3d9eb2931d`**; one act left (the re-pinned proof's commit).
- **CVO 87943:** the checker repair verified (both graded instances re-read VALID at `cec2a9b663`).

## Driver's own acts (tick 93 → 95)

1. **The checker (`.tools/proof-of-spec-check.py`, author `1.0.0_SA_CTO~X`):** three items ruled at the gate
   and repaired at `cec2a9b663` — `<decomp_ref>` CONTENT not presence, the vintage line printed by the tool in
   UTC with a Z, the rc legend — plus a fourth the battery found (`CELL_ID_RE` could not match a slug opening
   with a digit; 14 sec-7b cells invisible to the harvest). The vintage bump was BROADCAST before it bit
   (88017); the gate withdrew its own "the tool renders local time" clause (the tool printed no date before —
   a seat had typed one). A **CONTENT rung** followed (`4200a54390`, LOCAL): `introduces: [token…]` present at
   the pin and absent at `~1` — the 88109 item, after INDEXBYTES pinned a proof to a commit that resolves but
   does not contain. The CVO's DIRTY-vintage branch concurred as the next one-branch item.
2. **INDEXBYTES-DEPLOY:** delivered by AE~K on the gate's shape (the defect in one sentence: worktree md5,
   worktree upload, worktree compare — one source, a check that could not fail on what it guarded; the pre-fix
   baseline reported MATCH while S3 held 75 CRs git does not have). **The cited fix hash was FALSE** —
   `31579e177b` was the CVO's row-60 commit; the file sat ' M' in the shared worktree (safe-commit had been
   REFUSED by the comp-pipescript suite gate, the refusal dropped by a piped grep, then `git log -1` read HEAD
   as the seat's commit). MSTR's pre-push discipline caught it; **the gate withdrew its own acceptance**
   (88082 — a hash taken on citation, never opened) and gave the commit word with an audited override if the
   `.tools/` lane refused; the fix committed at `3d9eb2931d` (15:03Z, verified three ways), the hold lifted, the
   15:07Z push ran the committed gate at ceiling 0. MSTR's hand-compare retires on the next non-zero window
   (IB-5's production exercise). R8 filed.
3. **INF-RECORDER-SCOPE** accepted (1 of 25 against the measured 7-of-25 baseline; the 24 untouched rows
   byte-compared; `ensure_ascii` collateral edits caught by the seat — banked to memory); its code oracle found
   inf-pipeline functions whose DEPLOYED members differ from their recorded commit — routed as a SURPRISE with
   the (a)/(b)/(c) shape, cut as **INF-DRIFTCENSUS** at AE base; **the population corrected to EIGHT**
   (7 git-current + 1 git-stale) by machine count — the gate's "nine" withdrawn; the face amended in place.
4. **C02-g-13 V-1 + V-2** accepted with one amendment to the gate's own arm wording — the property is
   seed-independence, so the arms NAME `PYTHONHASHSEED` ("three default-seeded processes disagreeing is a
   coin-flip dressed as a control"); 6 of 9,538 tickers carried a set and randomised the whole field; the
   deployed-bytes-BEHAVE QA adopted as a shape. The g-13 bytes deployed in the 14:42Z window (the OPEN had read
   ceiling 0 one second before the commit; the CLOSE's list is the record).
5. **Two memories written** (a digest over `str()` of a set is random per process; `json.dump ensure_ascii`
   rewrites untouched rows) and two sharpened (the ack id comes from the file's Msg-ID line — the gate's own
   87950 ack was inferred, right outcome, wrong process; a cited fix commit is opened with `git show --stat`).

## In motion, not mine

AE~K: the re-pinned INDEXBYTES proof with `introduces` (closes the face); AE base: DRIFTCENSUS over 8; CTO~X:
the sec-7b engine-pin disarm (BLOCKING), then the DIRTY-vintage branch; AE~L: the C02-g-11 card; DS~N and
DS~V: **Monday 12:45Z** (a06's registered line + A7-4 + V-4's first; the single-writer billing read ~11:18Z),
Tuesday V-4's second; MSTR: the next non-zero window = IB-5's read; Andrew's word on R2, R6, R7 (+R8).

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`git log --stat` / `git status --porcelain` / a `git show HEAD:` token count on `.tools/safe_deploy_core.py`
(the false-pin read); `git log -3 -- .tools/proof-of-spec-check.py` + `grep -n` (the checker items' routing);
`ls-remote` + `merge-base --is-ancestor`; the inbox listing by timestamp; Msg-IDs read from each file. No
comp-find, no comp-state.

state: ARMED · next log at a verdict or tick 101 (floor)
