# MX-r-11 PHASE B -- the round-10 catalog and discover release onto the opal-gateway host

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Serial:** `0.7.0_AE_CloudOps~MI` | **Window:** 2026-10-13 22:18Z -> 23:25Z (session start; prior log
`ae_mi_mx_s_19_phase_b_0552-0620Z.md` @`b1a7ba06aa`)
**Order:** `org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-11.catalog-tool-index-release.md`
(A3 seated this seat, A4 carried the GO, A5 rules the outcome) | **risk:** WORLD

---

## What happened

Seated as PHASE B applier, oriented (`/watcher`, `org/XXX.md` 1b A-F, `/cloud-ops`), read both signed
never-widen halves, and applied the deploy-only commit `ad2acc0a93` onto `i-07dccb1615503ac99` on live base
`64b3e54658`. The release is SERVING. Two of three criteria resolved; the third was refused as written and the
issuer has since ruled fix-forward.

**The act, verified on both planes:**

| read | value |
|---|---|
| host vs BUILD INPUT (the cut's own files, sha256, not by filename) | 107 of 107 common, **107 byte-identical, DIFFER 0**, 0 cut-only, 0 host-only |
| negative control, same instrument vs the extracted base tree | **DIFFER 2** = exactly the 2 shipped files, EXPECTED SET MATCH |
| `/health` | 200; unit active; deploy `ssm:465546ad-4fff-4984-970f-cce1127dc226` |
| `opal-gateway-ad2acc0a93.tar.gz` | PRESENT (was 404), 557,616 B, ETag `dcfd3a2f`, git-ref `ad2acc0a93` |
| `-latest` | same size and ETag, git-ref `ad2acc0a93`, 22:51:29Z -- moved exactly one step |
| rollback key `opal-gateway-64b3e54658.tar.gz` | UNTOUCHED, 551,109 B, ETag `527cab0d`, still 21:07:30Z |
| tools | **67 = 67, names EQUAL** (added [] removed []); name-drop control reads EQUAL=False |
| `.env` KEY set | **54 = 54**, dropped [] added [], set and order identical; no value read or printed |
| `ENABLED_INTEGRATIONS` | **7 = 7**, ids unchanged |

**What the release delivered** (left column = the same check on the same host at the base, 20 min earlier):

| | base | after |
|---|---|---|
| FWD-20 partition | 0 of 67 | **67 of 67** (a=11 b=44 c=12, every member valid) |
| definitions located | 0 of 67 | 65 of 67 |
| FWD-21 discover | 1 of 3 | **3 of 3** |

**Criteria.** AC3 **PASS** exit=0 against the deployed catalog bytes (`etfs_get_positioning`, key resolved through
`freshness.row`, latest 2026-10-13 == catalog 2026-10-13 AGREE, depth absent CONFIRMED at 1 object / dateless key) --
same pick and verdict as the issuer's run at `212f2370a3`, which is a second instrument rather than a repeat.
AC2 **FAIL** exit=1, refused as written. AC1 **UNCOMPUTABLE-BY-CONSTRUCTION** (its limbs grade a closed ledger).

## The AC2 refusal, localised

Every clause of AC2's prose is met; the parenthetical `index rc=0` is not, because the instrument also grades a
`definitions located` limb the prose never names. The 2 misses, `opal_describe` and `opal_discover`, are the only
served tools **defined in the file this release ships**. `definition_ok()` accepts the tool name anywhere in
`lines[n-6:n+5]` of the cited `path:line`:

- `opal_describe` cites `integration.py:761` -> hit **False**; at `761+57` -> hit **True**
- `opal_discover` cites `:751` -> hit **False**; at `751+57` -> hit **True**
- `git diff --numstat 64b3e54658 ad2acc0a93` on that file reads `57 0`

Both citations are stale by **exactly the insertion count of the commit that ships them**: MX-c-8 renumbered nothing
after inserting into the very file its own catalog cites. The defect is in signed content, not in this act.

**Rollback NOT taken, declared not skipped.** The signed branch table prescribes a rollback on an AC2 failure, but it
is written for a read-back that shows the act going wrong, and every read of the act is clean. A rollback restores the
zeros above and fixes no line number. MX-r-10's instance declares the identical exclusion when `r10.AC2` first read
FAIL. Scope was not adjudicated in either direction: the act was HELD at the point where spec and measurement
disagree and both readings were handed up. **The issuer ruled at 23:19Z** (`Z-S112` @`96c5b4a9fe`, order A5): reading
(ii), AC2 is NOT met, the definitions limb carries the CVO's member-by-definition note and is not amended away, the
hold over rollback is **accepted**, and the remedy is a v2 release of `DATA_CATALOG.yaml` only cut on live
`ad2acc0a93`, after MX-c-8 A1 re-derives the two values.

## Deployment Sequence + Verification

1. Re-read host + plane 1; BASE-MOVED clause false (`-latest` git-ref `64b3e54658`).
2. Bun cache pre-check at the resolved pin `0e02a1f` (the pin moved with MP-z-5, so PHASE A left it here):
   **POSITIVE `77 of 77` rc=0**; **NEGATIVE** same lockfile + one planted uncached entry ->
   `77 of 78 / zzz-mx-r11-not-in-cache@9.9.9 absent` rc=1.
3. Halt gate from the deploy tree, as a pair: **rc=3** (`SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED`) with the base
   agent folder outside the cone, then **rc=0** after adding it. `HALT_OVERRIDE` never set, printed `<unset>`.
   Pre-apply mail guard is Rule 18a's PRIMARY limb, the broker read: 13 rows, READ=13, denominator 13, 0 not-READ,
   no STOP. A HALTGT pass is NOT cited (a `~lane` seat is unhaltable; the deploy tree has no inbox path checked out).
4. Ledger `nfra-mcpindex-r10-catalog-release` OPENED, 5 legs, entry AND sentinel committed `5ecc2cb834`, both
   confirmed at HEAD by `git ls-tree` before the act.
5. **First apply attempt FAILED in 5 s having shipped NOTHING** -- see Blockers.
6. Retry, with the base-moved clause enforced mechanically in the launch script. `DEPLOY_RC=0`. The deploy's own base
   guard fired twice (early, immediately-before-upload), both reading the declared base.
7. Label read-back **before L1 closed**; then host census, tool names, env keys; then AC2, AC3.
8. Plane 2 committed `62079e4a4c`: `deployed_commit ad2acc0a93`, `previous_deployed_commit 64b3e54658` per the CTO
   half -- never the stale `185dc04888`, and never the deploy tree's own `2c0f84966d`/`daa56d81ac` vintage the
   wrapper's helper writes (the recurring MP-x-4/MP-r-2/MP-n-1 defect). MP-z-5's record had drained since the ANNOUNCE
   was cut, so the ancestry now reads unbroken `185dc04888 -> 64b3e54658 -> ad2acc0a93`; row `Z-W33-S6` is resolved in
   the world. 5 lines, 1 of 27 services, 0 non-ASCII.
9. Ledger: **L1 L2 L4 L5 CLOSED** with proof; **L3 open**; entry **HELD-SOVEREIGN-GATED**. `check` reads
   `apply legs proven, only verify open; tracked-not-stranded`, SCAN DENOMINATOR 13 of 13.

## Blockers

**Not blocked on any seat for a decision -- the ruling arrived. HELD on another seat's ACT:** v2's cut waits on
**MX-c-8 A1** re-deriving the two `definition:` values on live `ad2acc0a93`. The issuer continues this seat at that
drain. `MX-s-19` is date-gated (`s19.AC2` reads 2026-10-19/20). Neither is an idle wait this seat can shorten.

**The first apply attempt (resolved, shipped nothing, measured):** the base's `deploy-to-ec2.sh` renders two `.env`
values through `lib.opal_naming.address()`, which loads the `infra/logic/registry` JSONs and
`org/standards/NAMING_SCHEMA.json`. The cone the ANNOUNCE describes holds none of them, so the run died
`FileNotFoundError` at line 112 with `Manifest not updated`, before the mcportal build, the tar, the first
`aws s3 cp` and any SSM call. **World untouched, verified after:** target key still 404, `-latest` byte-identical at
its original LastModified, host still carrying base bytes, deploy tree still at `ad2acc0a93` porcelain 0, manifest
unchanged. Fixed by widening the cone and **exercising both `address()` calls at the call site** rather than reasoning
about the closure.

## Rows filed (all `disarm_owner 2.0.0_SA_COO~MI`)

| row | class | what |
|---|---|---|
| `Z-S108` | OBSERVATION / INERT | the first attempt; the cone lacked `lib.opal_naming`'s registry closure |
| `Z-S109` | OBSERVATION / INERT | the ANNOUNCE's `deploy-to-ec2.sh` blob figure `76a4f20a6f` is **box/sitez's** copy; the cut's and base's is `2e9e3aed36`. The halves' claim (cut == base) re-measured TRUE, so the act is **NOT void** -- but the figure names the only copy carrying the `_pf_need` pre-flight loop, so reading the script from box/sitez shows a guard the running script does not have |
| `Z-S110` | BLOCKING / ARMED | AC2's definitions limb. **RULED** by the issuer's `Z-S112` @`96c5b4a9fe` |
| `Z-S111` | OBSERVATION / INERT | `Z-S108` is a **RECURRENCE**: MX-r-10's own instance already recorded the same chain in order (`lib`, then `infra/logic/registry`, then `org/standards`, "each revealed only by the next failure"). The knowledge sat in a `declared_exclusions` field the next actor's recipe does not read. OG-ap-14 cuts next on that recipe |

## Current State

**v1 is live and correct on every limb but one.** `i-07dccb1615503ac99:/opt/opal-gateway` serves
`ad2acc0a9305456e5bac4d7fd2cc5cd42642b203`, 107 of 107 byte-identical to the cut, `/health` 200, 67 served tools,
54 `.env` keys, 7 integration ids. Plane 1 `-latest` and `opal-gateway-ad2acc0a93.tar.gz` both carry git-ref
`ad2acc0a93` at ETag `dcfd3a2fc063d7ad97a11d2ad827f429`. Plane 2 on `box/sitez` names it.

**The ledger** `nfra-mcpindex-r10-catalog-release`
(`org/critical_paths/change_management/20261013T2234Z_nfra-mcpindex-r10-catalog-release_deploy_completion.md`) is
**HELD-SOVEREIGN-GATED** with L1/L2/L4/L5 closed and **L3 open**, owned by the issuer, inside its 8 h window. Its
sentinel is deliberately still at HEAD. Per A5 the SAME ledger closes on the v2 apply: L3 closes with `r11.AC2` on v2
(definitions 67 of 67), then AC3, then the close, then AC1.

**Rollback posture.** v1's rollback remains available and unexercised (`opal-gateway-64b3e54658.tar.gz`, 551,109 B,
ETag `527cab0d`). Per A5, **v2's rollback key is v1's artifact** `opal-gateway-ad2acc0a93.tar.gz`, never the base,
because v1 is the working state.

**KEPT, with why:** deploy tree `C:/tmp/mx-dep-r11`, HEAD `ad2acc0a93`, porcelain 0, sparse cone now
`.tools / data/transcripts/scripts/teams / infra/aws/ec2/opal-gateway / infra/logic/registry / lib /
org/mcp/inbox/0.7.0_AE_CloudOps / org/standards / org/tier2_senior/0.7.0_AE_CloudOps`. A5 names this tree as where v2
is cut. Its `EC2_MANIFEST.json` is modified-uncommitted (the wrapper's write, whose commit failed closed) and must
stay uncommitted so HEAD never leaves the cut. **Leftover scratch, harmless:** `/tmp/mx-r11-negctl` and
`/tmp/mx-r11-basetree` (`rm -rf` is not pre-approved for this seat; two small temp dirs).

**Proof instance:**
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-r-11.catalog-tool-index-release.proof_of_spec.json`
-- `proof-of-spec-check` **VALID rc=0**, bound to the governing order, 3 of 3 criteria carry cell refs, 1 of 1
declared cell reachable, 4 of 4 surprises resolve to channel rows. Probes:
`deliverables/0.7.0_AE_CloudOps~MI/probes_r11_phaseb/`.

**Commits** (`box/sitez`): `5ecc2cb834` ledger open, `e17cef39c8` rows Z-S108/S109, `62079e4a4c` plane 2,
`a5f0dc2202` the PHASE B record + rows Z-S110/S111 + proof instance (19 files, +1116/-16).
**Push state: LOCAL @`a5f0dc2202`; origin `box/sitez` @`9d45d46977` (`git ls-remote` read).** Not this seat's to
push -- `box/*` is pushed by an MSTR or the box's scheduled `box-sync` (org/XXX.md Step 1b SHARED-BRANCH LAW).

## Files Modified

See commit messages: `5ecc2cb834`, `e17cef39c8`, `62079e4a4c`, `a5f0dc2202`. The order file itself was **not**
touched -- `task-orders/` is outside this order's `<paths>`, so the `<status>` flip (still `issued` at HEAD) is the
issuer's.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` | PASS | startup forwarder exercise; 102 of 102 comp-tools resolve bare |
| `comp-find` | `comp-find 'proof_of_spec.json$' <deliverables> --files --limit 8` | PARTIAL | DENOMINATOR 1 hit / 681 files. comp-find searches **CONTENT**; the hit was a DOC-band prose mention. Glob (rail-FREE) returned 74 |
| `deploy_ledger.py` | `open` 5 legs; `close-leg` L1/L2/L4/L5; `hold --gate-type external`; `check` | PASS | entry + sentinel committed at open and confirmed at HEAD before the act |
| `surprise-row-gate.py` | at commit, twice | PASS (after a refusal) | first run BLOCKED the `Z-W33-S7` form; re-minted to the seat series `Z-S108/109`. Override NOT used |
| `proof-of-spec-check.py` | `<instance> AC1,AC2,AC3 --governing-order <order>` | PASS (after 3 violations) | `NOT-RUN` is not a valid status; AC1 -> `UNCOMPUTABLE-BY-CONSTRUCTION`, and both non-PASS rows need `status_reason`. Then VALID rc=0 |
| `halt-gate-check.sh` | from `C:/tmp/mx-dep-r11`, twice | PASS | rc=3 negative / rc=0 positive pair; `HALT_OVERRIDE` `<unset>` |
| `bun_cache_precheck.py` | real lockfile at `0e02a1f`, then + one planted entry | PASS | 77 of 77 rc=0 / 77 of 78 rc=1 naming the plant |
| `commit-gate.sh` | rode every `safe-commit` | WARN | `checked 0 of 1 file(s)` -- it reads only `.py/.sh/.tf/org/projects/*.json`. **Not cited as validation**; the JSON artifacts were validated by `json.load` + the schema checker |
| `comp-pipescript` / `comp-iam` / `comp-blast` / `comp-schedule` / `comp-adversary` | NOT RUN | N/A | declared, not omitted: no gold run, no Terraform, no IAM, no boto3 call added. The order's `<preflight>` declares the last three NOT-APPLICABLE with reasons |

**What worked.** The pre/post discrimination pair is what makes "the host runs the cut" a measurement: one sha256
instrument, two inputs (the cut and the extracted base tree), run from a single host read -- DIFFER 0 one way and
DIFFER 2 the other, with the pre-apply run reading the mirror image. Every claim in the record carries a control that
can fail: a name-drop on the tool census, a planted package on the bun check, an rc=3 refusal on the halt gate.
Enforcing the BASE-MOVED clause inside the launch script rather than as a human read closed the gap between the
pre-read and the act.

**What failed.** (1) The first apply, on a cone that could not run the deploy script -- and the closure was
discovered one `FileNotFoundError` at a time until I stopped guessing and **exercised both `address()` calls at the
call site**, which is the only oracle that settles it. (2) `comp-find` read 1 where 74 exist, because I asked a
content tool a filename question; a `1` that would have read as "almost nothing to compare against". (3) I wrote the
surprise rows with the order's prescribed `W33` id form, which the gate correctly refuses for a seat.

**Gap found.** `deploy-to-ec2.sh`'s `_pf_need` pre-flight (which exists only on box/sitez's newer copy) **stats**
`lib/opal_naming.py` without ever reading a registry JSON, so it reads CLEAN on the exact tree that fails. One
`address()` call in that loop is the fix, and it would have caught both occurrences -- this one and MX-r-10's. The
order's section 3 also prescribes a row id form (`-Z-W33-S<k>`) that its own assignee is mechanically barred from
committing; MX-r-10's applier hit the same refusal. Both go to the round-10 analysis per A5.

## Next Steps

1. **[`0.9.0_WK_NFRA_MCPINDEX~*` / `2.0.0_SA_COO~MI`]** MX-c-8 A1: re-derive the two `definition:` values on live
   `ad2acc0a93`. This seat's v2 cut starts at that drain, on the issuer's continuation.
2. **[`0.7.0_AE_CloudOps~MI`]** On that continuation: cut v2 (`app/refs/DATA_CATALOG.yaml` ONLY) on live
   `ad2acc0a93` in `C:/tmp/mx-dep-r11`, write `ANNOUNCE_MX-r-11_v2.md` with the three censuses, and stop for the
   fresh never-widen pair. v2's rollback key is `opal-gateway-ad2acc0a93.tar.gz`.
3. **[`2.0.0_SA_COO~MI`]** Disposition rows `Z-S108`, `Z-S109`, `Z-S111` (INERT as filed; durable fixes to the
   round-10 analysis), and flip the order's `<status>` -- the assignee does not edit the order file.
4. **[`2.0.0_SA_COO~O`]** NFRA_OPLGTW `OG-ap-14`'s start condition is **NOT** met: it cuts on this ledger reading
   CLOSED at HEAD, and the ledger is HELD until v2's apply closes L3.
5. **[`0.7.0_AE_CloudOps~MI`]** `MX-s-19` stays open on its clock (`s19.AC2` reads 2026-10-19/20).
