# 0.7.0_AE_CloudOps~Z -- handoff #8: OG-ap-20 Phase A closed at `06cfb6db64`, and `ap20.AC1` cannot pass as written

Continues handoff #7 (`ap19_live_and_ap20_held_at_two_gates.md`), which left OG-ap-20 held at two gates
that were not mine. Both cleared this morning within thirteen minutes of each other and Phase A ran
start to finish.

| | |
|---|---|
| **release** | `06cfb6db6471972c7304cd3d7a5b93e6f521ad72` on `rel-nfra-oplgtw-g5a`, worktree `C:/tmp/og-rel-g5a` |
| **base** | `1b18b94979d2ba0e4c6eba8ee4a0a5a0cae52bc0` -- MX-r-13's catalog v0.5 release, live 07:54:33Z |
| **trunk pin taken from** | `cf06cf8c43540426c492d16113cdd5cf09ec6d46` |
| **grant commit** | `f12b5d39bd` (box/sitez, ON ORIGIN) |
| **Phase A close commit** | `ca4ed97fe7` (box/sitez, LOCAL at this writing) |
| **ask** | `W/NEVER_WIDEN_ASK_OG-ap-20.md`, three halves, 15,571 bytes |
| **rows filed** | `Z-S141` (BLOCKING), `Z-S142` (OBSERVATION) |

## 1. The two gates cleared, and what each one actually unblocked

- **msg 34400, 08:16Z** -- MX-r-13 CLOSED, catalog v0.5 live at `1b18b94979`. This unblocked **step 4**,
  the re-cut, which A1 had held because the three modules read their key templates and bucket from
  `DATA_CATALOG.yaml` **at runtime**: on catalog v0.4 every tool would have answered `absent_reason`
  with no crash and no data.
- **msg 34402, 08:26Z** -- the `OG-ng-1` naming clause merged at `c8ca06fda0`. This unblocked **the
  `.tf` commit**. Note what it replaced: the earlier route was four `key_rulings.json` rows from
  `4.0.0_SA_CRO~Z`, which I had written and committed as a handoff at `W/G5A_KEY_RULINGS_FOR_CRO.json`.
  **Those rows are no longer owed** -- the clause answers row `Z-S140`'s refusal directly. If a future
  reader finds that handoff file, it is a dead end by design, not a missed obligation.

**The issuer predicted `IAM-PREFIX-ADMITTED n=4`; the gate printed `n=6`.** The clause graded every
2+-segment prefix, so the two rival-funds prefixes were admitted alongside the four tier-first ones;
`daily/*` is single-segment and is never graded at all. Reported.

## 2. Phase A, step by step, with the numbers

**Step 1 re-read on the new base: 117 of 117 comparable host files md5-equal, 0 mismatch, 0 one-sided.**
`W/G5A_LIVE_REF.json`.

> **The host read could not use the committed harness, and the reason is worth keeping.**
> `g36_hostread.py` goes to the host through S3 (Rule 12), and the gateway role **cannot read**
> `s3://opal-313476888478-lambda-artifacts/diagnostics/og-ap-20/` -- a 403 on HeadObject, measured from
> the instance. I replaced it with a `find -type f ... -exec md5sum` walk in one SSM call, which needs no
> object transport at all and therefore also stays inside the order's bound "no object or item written to
> any bucket or table". **I had already uploaded the 3 KB script before measuring the 403**; it is still
> sitting at that key, unreadable by the only thing that wanted it, and I did not delete it because an S3
> delete needs a human word. Someone may want to tidy it.
>
> **`dashboard/` is NOT comparable to this repo at any ref** and the parity read says so explicitly
> rather than quietly counting it: `deploy-to-ec2.sh:237-276` builds it from the **mcportal** checkout at
> the manifest's `mcportal_commit`, so it is a build product of a different repo (12 files on the host).
> Host `lib/` is exactly **one** repo-root file, `lib/trading_calendar.py` (`:270-271`). Lumping either in
> would have produced a confident verdict about files that do not exist here.

**Step 2-3 re-verified before committing**: the generator re-run against the catalog **at the base** gives
9 addresses from 8 entities of 340, and the `.tf` equals that derivation exactly in both directions --
7 prefix + 2 single-object GetObject ARNs, ListBucket confined by `s3:prefix` to the **7 directory
prefixes only**. The plan reads `1 to add, 0 to change, 0 to destroy` and is **byte-identical**
(md5 `f188ef150ccd71fd2f3792444fa6d3b5`) to the copy committed before the `Z-S139` apply and rollback --
an independent read that terraform state is exactly where it was.

**Step 4, the re-cut.** Cone copied from the `og-rel-g36` worktree that worked last time. Seams CLEAR
against the new base; `app/integrations` resolves as a **package** at `app/integrations/__init__.py`, and
`graphql_plumbing/catalog_gate.py` (which A1 names as read by `portal_mdpf.py`) is reached
**transitively** through `integrations/portal_index/integration.py`, not directly -- both present at the
base, verified by hand.

## 3. The thing that would have broken the deploy: the hookup carries a seventh tool

`OG-gt-12` (`3532daff79`) sits on a parent that already had `OG-gt-5`'s
`harvest_get_published_analysis`, so its hunks carry that tool **as context**, and
`app/harvest_published.py` is **ABSENT at this base**. Taking the 3-way `theirs` side whole would have
written `from . import harvest_published as _hvpub` into `app/tools.py` and **the gateway would have died
at import on the host**. This is row `Z-S137` from the other direction: a take that pulls a seam the base
lacks is as broken as one that omits a seam the base needs. It is also exactly why the order says take by
hunk and never a whole file from trunk -- `data_entitlement.py` additionally carries `+200` lines of
`OG-cp-1` work between base and trunk that this release must not ship.

> **A LINE FILTER WAS NOT ENOUGH AND THIS IS THE LESSON OF THE DAY.** My first resolver dropped every
> line that NAMED gt-5 -- four lines matched. The gt-5 function's **other** lines carry none of those
> tokens, so a bare `@mcp.tool()` decorator, a docstring and a comment continuation **survived as an
> orphan attached to the next function**, and nothing in a token filter can see that. The fix is to bound
> the removal by the block's own start and end markers and then check the result **structurally**:
> `@mcp.tool` decorators **69 -> 75**, the base's count plus six, which an orphan decorator breaks
> immediately. A filter that works on the names of things cannot verify the shape of what is left.

The two re-pinned counts are the **base's plus six** -- `registered_tool_names` 88 -> **94**, `non_data`
79 -> **85** -- never the hookup's own 95 and 86, which counted gt-5's tool too. The final by-hunk diff
is **+56/-5**, the same size as the hookup's own diffstat.

**Measured in the release tree:** five suites **26 passed, 0 failed**; the host-shaped import check
**CLEAN** -- `app/` and `lib/` staged side by side so `app/<mod>.py` sits exactly four parents deep as on
the host, all four modules import in a fresh interpreter, the registry the module itself builds reads
**75** with all six G5 tools in it, and the trading calendar resolves by search in all three modules.

## 4. `ap20.AC1` cannot pass as written -- row `Z-S141`, BLOCKING

I **ran** it rather than reading it, and it exits 1 on a correct release. Three defects, all in the
script, which is `2.0.0_SA_COO~O`'s deliverable and outside this order's `<paths>`:

1. the grant census is captured into **`reg`** on line 16 and read from **`$g`** on line 27, a variable
   nothing ever sets -- so `policies`, `wildcard`, `only`, `rival`, `page`, `put` all arrive EMPTY;
2. **`r`, `s` and `n`** (tools registered, SAFE, NATIVE) are never computed anywhere, so it prints
   `tools registered  of 6` with a hole where the number goes;
3. the put-or-delete limb greps `s3:(Put|Delete)` over the **RAW** `.tf`, and line 43 of a correct
   `etfs_read_iam.tf` is a comment reading `no s3:PutObject, no s3:DeleteObject` -- **so that limb scores
   the file's own denial as a hit**, and would still fail after (1) is fixed.

The two limbs that DO run both PASS: `base 1b18b94979 is the live ref before this release: yes` and
`files differing 12; outside the G5A set 0 (want 0)`. The three ungraded limbs all hold at the release,
measured and saved at `W/G5A_AC1_SUBSTANCE.json`: registered 6 of 6, SAFE 6 of 6, NATIVE 6 of 6,
policies 1, wildcard 0, actions exactly `s3:GetObject` and `s3:ListBucket`, rival-funds gold and page
yes, put-or-delete 0. **That measurement is evidence for the script's owner, not a pass** -- a criterion
is graded by its own invocation.

## 5. Three of my own instruments printed confident false negatives in one sitting

All three were against files that were **right**, and in all three the tell was the same: a verdict that
disagreed with something I had already measured another way.

1. **A comment that DENIES a token contains it.** My `.tf`-vs-generator check counted the file's own
   `no "*" resource` comment as a wildcard resource and printed `DRIFT` against a correct grant. **Strip
   comments before any token census of code.** `ap20.AC1` has the identical bug (defect 3 above), which
   is how I recognised it.
2. **A condition KEY is not an action.** A bare `"(s3:[A-Za-z]+)"` census counted `s3:prefix` -- the
   `ListBucket` condition key -- as a third action, so an assertion of "exactly GetObject and ListBucket"
   failed. Read actions from the `Action` blocks, not from the file's tokens.
3. **A list lives in the file that defines it.** Looking for `SAFE_TOOLS` in `tools.py` and
   `data_entitlement.py` returned **null**, which my first script reported as a finding; it is in
   `app/destructive_ops.py`. A `null` from a wrong-place read and a real zero look identical.

And one that was **not** a defect: `g5a_seams.py` reported `integrations` as present at the base, which
looked like the known "a name resolves to a module OR a package" false positive. It was not -- the
**committed** script carries a `kind: package` limb and probes `app/integrations/__init__.py`. I had been
reading a **stale copy in the scratchpad**. Read the artifact at the path that ran, not the copy you last
edited.

## 6. `Z-S142`: a sparse release cone silently demotes the naming gate to WARN

The same `etfs_read_iam.tf` was graded twice today: `NAMING-GATE: PASS 7 graded` under ENFORCE in the
shared tree, and `NAMING-GATE: WARN 6 graded` with `4 REFUSE verdict(s) did not block` in the release
worktree. ENFORCE is decided by the tracked sentinel `org/mcp/naming-gate.enforce` being **on disk**;
`org/mcp` is outside the release cone, so `ls-files -t` prints `S` (skip-worktree) for every entry there
and the gate degrades, announcing it only in a parenthetical inside a passing commit. **The commit that
most needs the gate -- the WORLD-risk release commit -- is the one that gets it in WARN.** A second,
separable cause points the same way: the release branch is cut at a base that **predates** the clause, so
it also runs the older gate code. Same family as `Z-S132`. Nothing was mis-landed: the identical bytes
passed the ENFORCE gate minutes earlier.

## 7. State

| order | state |
|---|---|
| **OG-yr-1** | COMPLETE, ledger CLOSED |
| **OG-ap-15** | COMPLETE |
| **OG-ap-18** | COMPLETE, ledger CLOSED |
| **OG-ap-19** | COMPLETE, live at `ee23dd004c`, ledger CLOSED |
| **OG-ap-20** | **Phase A CLOSED.** Phase B waits on the issuer's GO naming all three halves signed at `06cfb6db64` |
| **OG-ap-17** | Phase A complete; CTO half owed; PAUSED by the issuer, not mine to re-open |
| **OG-mg-1** | Phase A complete; Phase B waits on two halves and a GO |
| **OG-ap-21** | read, not started; waits on ap-20's ledger `nfra-oplgtw-gateway-release-g5a` being CLOSED, which is Phase B |

Release lineage, each a local branch **never merged to trunk** (trunk is not a reader of what is live;
`EC2_MANIFEST` is): `bacec95ccd` -> `bf7ffb62f4` (yr-1) -> `047f11aa99` (ap-18) -> `ee23dd004c` (ap-19)
-> `1b18b94979` (MX-r-13, **current live**) -> `06cfb6db64` (this release, **not deployed**).

**Nothing of mine is unblocked.** Phase B needs three signatures; ap-21 needs Phase B. The watcher is the
only standing act: a Monitor dies every ~30 minutes printing `[WATCHER-EXPIRED]` and is re-armed the same
turn with one Monitor call and no skill load.
