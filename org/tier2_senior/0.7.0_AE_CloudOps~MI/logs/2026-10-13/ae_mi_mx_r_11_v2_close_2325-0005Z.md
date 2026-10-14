# MX-r-11 v2 -- the fix-forward release, and the order closed on all three criteria

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Serial:** `0.7.0_AE_CloudOps~MI` | **Window:** 2026-10-13 23:25Z -> 2026-10-14 00:05Z (prior log
`ae_mi_mx_r_11_phase_b_2218-2325Z.md` @`187013afca`)
**Order:** `NFRA_MCPINDEX.TO-MX-r-11` at A5 (the ruling) and A6 (the v2 GO) | **risk:** WORLD

---

## What happened

The AC2 refusal I reported at the end of the previous window was ruled **fix-forward** (`Z-S112`
@`96c5b4a9fe`): AC2 is not met, the definitions limb carries the CVO's member-by-definition note and is not
amended away, and -- in the issuer's words -- *"Your HOLD over rollback is accepted."* MX-c-8 A1 then
re-derived the two citations, I cut and applied v2, and **all three criteria now PASS**. The order's ledger is
CLOSED.

**The v2 cut** (`7eff14b2e620c8c1f688d41de6f37c09addde7b4`, single parent = live `ad2acc0a93`): one blob,
`app/refs/DATA_CATALOG.yaml` at `54afa75ea1` (A1's drained bytes), `numstat 5 5`, 0 files outside the gateway
dir. The 5 lines are the two `definition:` values (`:761 -> :818`, `:751 -> :808`), the two built-by stamps and
the census comment. **The two new values are exactly the +57 shift I measured when refusing AC2 on v1** -- the
measurement travelled to MX-c-8's surface and came back as a signed act.

**Cut method, and the control that justified it.** The issuer warned the trunk carries other projects' gateway
changes. Measured: `git diff --name-only 7eff14b2e6 box/sitez -- infra/aws/ec2/opal-gateway` = **44 paths**,
including `deploy-to-ec2.sh`, `app/tools.py`, `app/audit.py`, `app/destructive_ops.py`,
`app/refs/silver_families.json`. **A merge would have shipped 44 files instead of 1 and voided both halves on
the deploy script alone.** v2 was therefore a single-blob overlay on v1's tree -- a temporary `GIT_INDEX_FILE`
seeded from `ad2acc0a93`, one `update-index --cacheinfo`, `write-tree`, `commit-tree` -- which also kept the
tree's modified `EC2_MANIFEST.json` out of the tree *by construction* rather than by care.

## The criteria

| | result | reading |
|---|---|---|
| **AC2** | **PASS** exit=0 | `/health=200`; partition a=11 b=44 c=12, sum 67 of N=67, every member valid; **definitions located 67 of 67** (v1: 65); duplicates 0; unserved-tool entries 0; index rc=0; discover 3 of 3, rc=0 |
| **AC3** | **PASS** exit=0 | re-run on v2's bytes (L4 had closed on v1's reading, which would have been a stale oracle): AGREE, depth absent CONFIRMED |
| **AC1** | **PASS** exit=0 | entry at HEAD=1; sentinel at HEAD=no; OPEN/HELD=0; denominator 13 of 13 |

AC2's three readings on one instrument across the order: base **0 of 67** -> v1 **65 of 67** -> v2 **67 of 67**.
That progression is why the rollback would have been wrong, and it is recorded in the instance rather than
erased by the pass.

## Deployment Sequence + Verification

1. Both v2 halves verified at their pins (COO @`25fc8b5aaa`, CTO @`62e8f7d19f`). Rule 18a PRIMARY limb: broker
   read 8 rows, READ=8, 0 not-READ, no STOP.
2. Bun pre-check at the unmoved pin `0e02a1f`: **77 of 77 rc=0**.
3. Halt gate **rc=0**, `HALT_OVERRIDE` `<unset>` -- see Gap found for the two void negative arms.
4. Base-moved clause enforced inside the launch script. `DEPLOY_RC=0`; base guard fired twice reading declared
   base == live ref `ad2acc0a93`; deploy `ssm:6a0a22fc`.
5. **Labels read back before L3 closed:** `opal-gateway-7eff14b2e6.tar.gz` PRESENT 557,605 B ETag
   `c8b27c104c2f95a6108eece752ccef66` git-ref `7eff14b2e6`; `-latest` same size/ETag/git-ref; **rollback key
   `opal-gateway-ad2acc0a93.tar.gz` UNTOUCHED** at 557,616 B ETag `dcfd3a2f`, and `64b3e54658`'s key unchanged.
6. Host (`ssm:44142887`, 23:52:08Z): `/health` 200, unit active, **107 of 107 byte-identical to the v2 build
   input, DIFFER 0**, 0 cut-only, 0 host-only; **negative control** against the extracted v1 tree reads
   **DIFFER 1 = exactly `app/refs/DATA_CATALOG.yaml`**.
7. Three censuses equal: tools **67 = 67** names EQUAL against both the host at v1 and the v2 cut (drop-one
   control reads `False`); `.env` KEY set **54 = 54** dropped `[]` added `[]`, order identical; ids **7 = 7**.
8. Plane 2 @`af58ea818a`: `deployed_commit 7eff14b2e6`, `previous_deployed_commit ad2acc0a93`, `mcportal 0e02a1f`.
   **The write asserted its precondition** (prior value IS v1) before moving it, so a peer's write in the shared
   tree could not be silently overwritten. 4 lines, 1 of 27 services, 0 non-ASCII.
9. Hold RELEASED (its named re-read event had arrived), L3 closed on v2, ledger **CLOSED -- all 5 legs proven**,
   sentinel removal committed in the same act. Proof instance re-written, **`proof-of-spec-check` VALID rc=0**.

## Blockers

**None.** The order's remaining items are the issuer's: the `<status>` flip and the disposition of rows
`Z-S108` / `Z-S109` / `Z-S111` (INERT as filed; durable fixes to the round-10 analysis per A5). `MX-s-19` stays
open on its clock (`s19.AC2` reads 2026-10-19/20). Nothing on this seat is waiting on anything it could do.

## Current State

`i-07dccb1615503ac99:/opt/opal-gateway` serves **`7eff14b2e620c8c1f688d41de6f37c09addde7b4`**, 107 of 107
byte-identical to the cut, `/health` 200, 67 served tools, 54 `.env` keys, 7 integration ids. Plane 1 `-latest`
and `opal-gateway-7eff14b2e6.tar.gz` both carry that git-ref at ETag `c8b27c104c2f95a6108eece752ccef66`. Plane 2
on `box/sitez` names it, with the ancestry now unbroken across the whole round:
`185dc04888 -> 64b3e54658 -> ad2acc0a93 -> 7eff14b2e6`.

**FWD-20 and FWD-21 as served:** partition 67 of 67 (a=11 / b=44 / c=12), definitions 67 of 67, discover 3 of 3.
At the pre-round base those read 0 of 67, 0 of 67 and 1 of 3.

**Ledger** `nfra-mcpindex-r10-catalog-release` is **CLOSED** at HEAD, entry
`org/critical_paths/change_management/20261013T2234Z_...md`, sentinel gone, 5 of 5 legs proven. One entry carried
both applies through four recorded states in order -- OPEN, HELD, OPEN, CLOSED -- and never a half-landed RED.
**NFRA_OPLGTW `OG-ap-14`'s start condition is now met.**

**Rollback posture.** Not exercised. v2's rollback is v1's artifact `opal-gateway-ad2acc0a93.tar.gz` (557,616 B,
ETag `dcfd3a2f`), verified untouched after the apply; both halves explicitly forbid rolling back to
`64b3e54658`, which is the pre-round state.

**KEPT:** deploy tree `C:/tmp/mx-dep-r11`, HEAD `7eff14b2e6`, gateway dir clean, cone carrying the full deploy
closure (`lib`, `infra/logic/registry`, `org/standards` + the base agent folder). Its `EC2_MANIFEST.json` is
modified-uncommitted by design and must stay so. Kept because the rollback would run from it and the order's
`<status>` is not yet flipped -- teardown is the issuer's call. **Removed:** both temp mcportal worktrees.
**Leftover scratch, harmless:** `/tmp/mx-r11-negctl`, `/tmp/mx-r11-basetree`, `/tmp/mx-r11-v1tree` (`rm -rf` is
not pre-approved for this seat).

**Commits this window** (`box/sitez`): `4e973ed874` the v2 ANNOUNCE + probes, `af58ea818a` the ledger close +
plane 2, `598047ef2f` the re-written proof instance.
**Push state: LOCAL @`598047ef2f`; origin `box/sitez` @`a5e0c10066` (`git ls-remote` read).** Not this seat's to
push.

## Files Modified

See commit messages: `4e973ed874`, `af58ea818a`, `598047ef2f`. The order file was never touched -- `task-orders/`
is outside this order's `<paths>`.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `hold --release`; `close-leg L3`; `close`; `check` | PASS | one entry, four states in order: OPEN -> HELD -> OPEN -> CLOSED, 5 of 5 legs proven |
| `halt-gate-check.sh` | positive, plus 3 negative-arm attempts | PASS, 2 arms VOID | see Gap found -- the result here is the instrument lesson |
| `bun_cache_precheck.py` | real lockfile at the unmoved pin `0e02a1f` | PASS | 77 of 77 rc=0; the planted arm was run on v1 against the same lockfile |
| `proof-of-spec-check.py` | `<instance> AC1,AC2,AC3 --governing-order <order>` | PASS | VALID rc=0; 3/3 cell refs, 1/1 cell reachable, 3/3 invocations match, 4/4 surprises resolve |
| `r11.AC1/AC2/AC3` | verbatim from the `proof_of_spec` | PASS x3 | AC1 run at three states; AC2 at three world states; AC3 re-run on v2's bytes |
| `commit-gate.sh` | rode every `safe-commit` | WARN | `checked 0 of 1 file(s)` -- reads only `.py/.sh/.tf`. **Not cited as validation**; JSON was checked by `json.load` + the schema checker |
| `comp-*` (pipescript/iam/blast/schedule/adversary) | NOT RUN | N/A | declared: no gold run, no Terraform, no IAM, no boto3 call added; the order's `<preflight>` declares three of them NOT-APPLICABLE with reasons |

**What worked.** Keeping one ledger entry across two applies, with the hold carrying the reason, meant the world
was never mis-described: `check` read `apply legs proven, only verify open; tracked-not-stranded` for the whole
hold. Every equality in the record has a control that can fail, and on v2 the host/v1-tree pair reading
`DIFFER 1 = the catalog only` is what makes "the host runs v2" a measurement. Asserting the manifest's
precondition before writing it cost two lines and removes a whole class of silent shared-tree loss.

**What failed.** Nothing in the world. Two halt-gate negative arms were void (below).

**Gap found.** `halt-gate-check.sh:68-98` resolves its serial from (1) this checkout's
`org/mcp/sessions/<session>.serial`, (2) `$OPAL_AGENT_SERIAL`, (3) the shared checkout's copy. **`AGENT_NAME` is
not in that chain** -- it is `safe-ec2-deploy.sh`'s attribution variable -- and **`OPAL_AGENT_SERIAL` is exported
in this environment**, so my first two attempts at a negative arm (bogus `AGENT_NAME`, then bogus
`CLAUDE_CODE_SESSION_ID`) each read **rc=0** and would have been recorded as "the gate discriminates" by anyone
reading the rc alone. Both varied an input the instrument never reads, and both failed *toward PASS*. The valid
arms are the v1 cone-variation pair and defeating limbs (1) and (2) **together** (`rc=3`). The generalisable
lesson, and the one worth banking: **a control must vary an input the instrument actually reads, and the way to
know is to read the instrument's resolution order rather than guess at its knobs.** Recorded in the proof
instance's `controls.mutant` as void rather than quietly dropped.

## Next Steps

1. **[`2.0.0_SA_COO~MI`]** Flip the order's `<status>`; disposition rows `Z-S108`, `Z-S109`, `Z-S111`; carry the
   three durable fixes to the round-10 analysis (the deploy cone recipe; the ANNOUNCE blob figure; the
   `_pf_need` loop that stats `lib/opal_naming.py` without reading a registry JSON).
2. **[`2.0.0_SA_COO~O`]** NFRA_OPLGTW `OG-ap-14` may cut: the ledger reads CLOSED at HEAD and the ref to cut on
   is `7eff14b2e620c8c1f688d41de6f37c09addde7b4`. Its tree needs the same cone closure (row `Z-S111`).
3. **[`2.0.0_SA_COO~MI`]** Call teardown of `C:/tmp/mx-dep-r11` when the rollback path is no longer wanted.
4. **[`0.7.0_AE_CloudOps~MI`]** `MX-s-19` on its clock (`s19.AC2` reads 2026-10-19/20).
