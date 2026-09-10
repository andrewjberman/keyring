# DEPLOY COMPLETION LEDGER -- THE MANUAL SERVED DAY, 2026-09-10 keys (NFRA_OUTSET.TO-OS-s-24)

**Opened:** 2026-09-10T00:20Z by `0.7.0_AE_CloudOps~W`
**Status:** OPEN
**TO:** `org/missions/D11/NFRA/NFRA_OUTSET/task-orders/NFRA_OUTSET.TO-OS-s-24.the-manual-served-day.md`
(cell `OS-s-24`, PRD v0.8; issuance `26f1cd8b82`)

⛔ **OPENED BEFORE STEP (iii), THE ORCHESTRATOR INVOKE.** The invoke has not happened at this
entry's commit. This is a RULE (2) served-output move: a report run writes `daily/` and `manifest/`,
which the estate reads.

## THE NEVER-WIDEN SIGN-OFF -- BOTH HALVES, QUOTED

**COO half -- issuance `26f1cd8b82`**, TO-OS-s-24's own face, verbatim:

> The COO's half is GIVEN HERE, in this face, for exactly this run: 09-10 keys, nothing
> overwritten, the four pins named, the rollback named -- quote this face's commit hash as the
> COO's line.

**CTO half -- message id `94764`** from `1.0.0_SA_CTO`, 2026-09-09T22:30:20Z, verbatim:

> This message id is the CTO's half of the never-widen sign-off (CLAUDE.md NEVER-1) for exactly the
> run below; the COO's half is issuance 26f1cd8b82. [...] WHEN: after 2026-09-10T00:00:00Z, before
> 13:00Z, so every key is dated 2026-09-10 and nothing dated 09-09 is written or overwritten [...]
> Anything outside this shape (a 09-09-dated run, a write under a different prefix, a run without
> the token) is not covered and needs a new sign-off.

⛔ **THE ID IS 94764, NOT 94763.** I was carrying 94763 forward from an earlier note and it was
wrong. It was corrected by OPENING the message and reading its own `Msg-ID` line rather than
trusting the number I had. A sign-off quoted by the wrong id is not a sign-off.

## What this run writes -- NEW KEYS ONLY

`daily/2026/09/10/estate-report-2026-09-10.json`, the `.md` sibling, `manifest/2026-09-10.json`,
and one `logs/` key. **No existing key is overwritten.** The `outset/` seam writes of steps (i) and
(ii) are producer artifacts under their own faces' QA clauses and are explicitly OUTSIDE this
sign-off.

## THE PROTECTED RECORD -- the four 09-09 pins, measured live at 00:19Z BEFORE the invoke

| key | VersionId | LastModified | IsLatest (before) |
|---|---|---|---|
| `daily/2026/09/09/estate-report-2026-09-09.json` | `M.3hYlFn8PRvTcqxCUouBTNygDd73huK` | 15:32:41Z | **true** |
| `daily/2026/09/09/estate-report-2026-09-09.json` | `8SP4fGAuhE8twzBpucMPsYbotD6Tddty` | 13:11:02Z | false |
| `daily/2026/09/09/estate-report-2026-09-09.md` | `xfSKTGqkdljsQTyUt20nC1RJsPtPGBSU` | 15:32:41Z | **true** |
| `daily/2026/09/09/estate-report-2026-09-09.md` | `GcEjGK_GwkDzyyvVo190fPSODn9svmLx` | 13:11:02Z | false |

Version denominators before the invoke: `.json` 2, `.md` 2, `manifest/2026-09-09.json` 4 (its
latest is `68kpLcmJw.4hNCbaIjMgSFU3a.oHP9.G` @15:32:41Z).

⛔ **HOW ARM (e) IS READ, STATED BEFORE THE RUN SO IT CANNOT BE FITTED AFTERWARDS.** O24-AC1 (e)
says "the four 09-09 pins are STILL the latest versions of their keys ... IsLatest true on the
pinned id". **Taken literally that cannot hold for two of the four**: the four pins are TWO KEYS x
TWO VERSIONS, and the 13:11:02Z pair is by construction the SUPERSEDED version -- the face itself
names it "O20-AC1's negative arm". This is loose phrasing, not a defect: the face's own parenthetical
shows the issuer knows which pin is which. The SUBSTANCE the arm buys is that the manual day
overwrote nothing, and it is read as three checks, all stronger together than the literal one:

1. the version DENOMINATOR on each 09-09 key is unchanged after the run (2 / 2 / 4);
2. the IsLatest id on each key is still the 15:32:41Z pin;
3. all four pinned ids are still PRESENT and retrievable.

## Rollback

One `copy-object` from the pinned VersionId per key, in session, no Terraform. Bucket versioning is
ENABLED (all four pins listed above prove it). **Expected to be unnecessary**: this run creates
09-10 keys and touches no 09-09 key. If a 09-09 key is ever touched, that is outside the sign-off
and the entry closes RED with the copy-object executed.

## Legs

1. [x] Step (i): OS-s-25's on-demand drift run -- artifact VersionId
       `3AE8of7Q44VkfbsNNpwWD0EH8lqPj.Sn` @2026-09-09T23:58:14Z, `git_head_moved` false.
2. [x] Step (ii): freshness CodeBuild started BY HAND 2026-09-10T00:17:51Z --
       `estate-report-seam-freshness-publisher:dc71343c-9118-4037-86b5-23e9bdd5e4b0`, build #3,
       `initiator` `Andrew_Berman`, source type NO_SOURCE (the same project and call the 08:30 ET
       rule targets; `Target.Input` NULL, so the hand start and the rule start are the same call).
3. [x] All THREE seam artifacts in place and ahead of the invoke, measured 00:19Z:
       `outset/comp_heat_freshness_tools.json` @2026-09-10T00:18:59Z v`wPjEwsCY4Fg2o84Wp3bGYUs7fqSKb7Pz`
       (moved from 16:54:39Z), `outset/comp_fedobs_coevolution.json` @2026-09-10T00:19:02Z
       v`PX68UJFO3pcBlpUn.P8rl79YZ6Ado5l4` (moved from 16:54:42Z),
       `outset/laptop/comp_heat_drift.json` @2026-09-09T23:58:14Z. **Both off-host keys MOVED**, so
       the build wrote them rather than leaving yesterday's bytes to read as fresh.
4. [ ] Step (iii): orchestrator invoked with `{"mode":"daily-run","trigger":"manual"}`.
5. [ ] The 09-10 keys written; `run_bundle.trigger == "manual"` with the matching `run_id`.
6. [ ] The four 09-09 pins intact on all three checks above.
7. [ ] The host STOPPED at the read.

## The host

`i-0584e17d283fa7ef4`. The run ends with the host self-stopped by its boot units' design. **A host
still running 30 minutes after the report lands is a FINDING, not a wait** (the face's own words).
