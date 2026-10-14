# A signed release that lapsed, and a Phase A whose job turned out to be disproving its own order's premises

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, DIAGNOSE

Delta to `ap15_five_released_and_ap14_b1_recut.md` (same date, earlier). Round 37. Written at the
phase boundary: every order is now on a clock or a signature, so this is the handoff.

## Where the orders stand

| order | state | what remains, and whose |
|---|---|---|
| `OG-ap-15` | **COMPLETE**, 5 of 5 live | AC2 at the five scheduled sweeps; `Z-S102` disarm is the issuer's |
| `OG-ap-14` | **B1 re-cut v2**, AC1 PASS, both halves re-signed at `92698aea8c` | B2 at 11:00Z+, C2 and C3 binding at the act |
| `OG-mg-1` | **Phase A COMPLETE**, AC1 PASS | both halves, then ap-14's ledger, then Phase B |
| `OG-hv-2` | gated | ap-14's ledger |

## The one thing a reader should carry away

**Two orders in a row were wrong about their own premises, and in both cases the measurement that
found it was one the order itself asked for.** That is the argument for doing Phase A properly rather
than treating it as paperwork before the write.

- **OG-mg-1 step 3** said to build Andrew's candidate as Alyssa's scope "with `calendar_months: 13`"
  and to put two `operations` branches to the halves. Measured: her scope **already** carries
  `calendar_months 13`, and **already** carries `download_filtered` among operations that are
  contract-maximal. So the window change was a no-op and the two branches were the same branch --
  `template_changed_keys` came back **empty for all three candidates, including the branch-b one**.
  The issuer ruled route (i) and struck the branch as its cut defect.
- **OG-mg-1's preflight** (earlier, row `Z-S103`) told me to simulate `dynamodb:TransactWriteItems`
  and treat an `implicitDeny` as a STOP. That action does not exist.

Neither was discoverable by reading harder. Both needed an instrument pointed at the live object.

## The sharpest instrument lesson of the session: two controls, both wrong, opposite directions

On `Z-S103` I had a denial I was about to act on, and the cloud-ops rules say to run a positive
control beside it. I ran one, and **the control was as misleading as the thing it was checking**:

| instrument | result for `dynamodb:TransactWriteItems` | why it misled |
|---|---|---|
| simulate against the role | `implicitDeny` | a non-existent action denies exactly like a missing grant |
| simulate against a broad principal (the "control") | **allowed** | an admin wildcard matches any string, including a bogus one |
| `accessanalyzer validate-policy` | `ERROR / INVALID_ACTION` | the only one that answers "is this name real" |
| the role's policy document | `GetItem` unconditioned; `PutItem`/`UpdateItem` conditioned on `LeadingKeys POLICY#*` | the ground truth |

A reader with only the role simulation files a BLOCKING row on the order's central write. A reader
with only the control concludes the role is under-granted against an admin. **The control did not
disarm the trap; it supplied a second wrong answer that happened to point the other way.** What
settled it was reading what the role actually grants, and then re-simulating the conditioned
statements WITH `--context-entries` -- at which point `PutItem` and `UpdateItem` read `allowed`
where they had read `implicitDeny`.

Then the writer, not the preflight, said what authorization the act needs: `activate()` builds only
`Put` ops, with the staleness check riding the Put's own `ConditionExpression` rather than a separate
`ConditionCheck` item, and the module states "Never a DeleteItem". So `DeleteItem` and
`ConditionCheckItem` being absent from the role is the design, not a gap.

## A signed release can lapse under you

C3 of the COO half said A3's GO held only while live was `7eff14b2e6`. NFRA_MCPORTAL MP-n-4 landed
`b0c75d24f1` at 01:31Z, so the GO lapsed by its own terms **after both halves had signed**. The
re-cut was rebase-free: a new branch from the new live ref with the same six commits in the same
order, producing identical content (18 files, +1262/-136).

**Nothing was carried over on trust, and that discipline paid twice.** The host md5 parity, the
suites, the conflict resolution and AC1 were all re-measured on the new ref; the pre-existing failure
`test_ogz1_ac08` was re-confirmed *at* `b0c75d24f1` in a pristine detached tree rather than inherited
from the v1 run. And re-reading MP-n-4's one module (`app/admin_fabric_gitstate.py`) showed it
registers no `@mcp.tool()`, which is why sh-1's tool-count assertion of 54 still held -- had it added
one, the v1 resolution would have been silently wrong on the new base.

**`git pull` on `box/sitez` is integrator-only** and the never-rules gate refused mine, correctly.
`git fetch` plus a read of origin's tip is the way to confirm a shared-branch value; my local
`box/sitez` already carried the drain because the tree is shared on this device, which is the only
reason AC1 could read the right live ref at all.

## A correction I received, verified, and had to act on

The COO's C1 said my ap-14 ask omitted a widening. It did. I had called OG-tg-1 "NARROWS, twice
over" and pf-1 "the only widening here", reading the order's own phrase "unscopes the concierge" as
part of the narrowing. **Unscoping a principal widens what that principal may call.** Verified in the
diff before writing the correction: `app/identity_scope.py` deletes that principal's `_SEED`
frozenset entry and `identity_tool_allowlist.txt` deletes both of its overlay rows, so it goes from
SCOPED to two tools to UNSCOPED, inheriting Andrew's set. Section 2 now carries tg-1 as
NARROWS-and-WIDENS with the evidence per limb, and says the first version was wrong.

## Three traps, all mine

1. **The same one-line pin edit, wrong twice.** First a 4-space anchor read off my own
   `sed 's/^/  /'`-indented output instead of the file's bytes; then a 400-byte guard window that
   overshot the map and matched "orion" inside `silver_families`. Both failed CLOSED, which is the
   only reason it was recoverable. **A display pipe is not the file.**
2. **A count inferred from a sibling's base.** Resolving sh-1's conflict I wrote 53 (pf-1's 52 plus
   sh-1's one new tool) when the tree said 54, because the re-cut sits on a live ref that already
   carried MX-r-11's tools. The suite named the real number in one run; the resolution turned out to
   be sh-1's side verbatim, cmp-verified.
3. **The heredoc ate a backslash, again.** Twice this session, on `\\n` inside a Python string passed
   through a quoted heredoc -- once breaking a comment mid-string, once silently failing a
   `str.replace` so a lint fix did not apply. The device's memory already holds this one. Match on a
   substring with no escape, or write the file with the Write tool.

## Instrument discipline that earned its keep

- **Every apply was enumerated from `terraform show -json`, never the rendered tail.** The rendered
  plan hides unchanged elements behind `# (3 unchanged elements hidden)` -- exactly where an extra
  row would sit unseen. 1 non-no-op of 11 resources, every time.
- **Rollback values were recorded before the first upload**, so every plan's `s3_object_version`
  BEFORE field cross-checked them for free. That was not designed as a control and is the best one in
  the record.
- **Deployed bytes compared member-by-member**, with the downloaded zip's own base64 sha256 checked
  against `get-function-configuration`. Without that limb the comparison proves something about a
  package, not about the deployed one.
- **Identifiers kept off-repo by construction, then asserted.** `mg1_before.py` refuses to run if
  `X` resolves inside the worktree; the committed records were then checked to hold 0 GUIDs, 0
  at-signs and 0 `POLICY#` literals. The mg-1 ask was checked against **AC1's own email regex** --
  which would have matched the Bloomberg identity's address had I written it.
- **Zeros got their causes named.** A combined suite run at the live ref printed nothing: four of the
  seven suites do not exist there because the cells add them. Recorded with that cause rather than as
  a pass.
- **`ItemCount` was refused as a denominator.** It read 1493 against a consistent scan's 1504, then
  1510 minutes later. The scan's own count, fully paginated, is the number.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `git cherry-pick -n` + restore | PASS x2 rounds | 6 picks each; 3 outside paths restored per round; 1 real conflict, same resolution both times |
| `pytest` (7 gateway suites) | 46 passed / 1 pre-existing | classified at BOTH live refs, signature-matched |
| `ap14.AC1.sh` | PASS x2 | on `db3d1972bc`, then re-pinned on `92698aea8c` |
| `mg1.AC1.sh` | PASS | ask items 6 of 6, email addresses 0 |
| `ssm send-command` | PASS x3 | md5 parity at both refs; needed a JSON parameter file, not shorthand |
| `iam simulate-principal-policy` | PASS, with both false modes observed | see the table above |
| `accessanalyzer validate-policy` | PASS | the only instrument that answers "is this action name real" |
| `prepare()` in-process | REFUSED x3, then ACCEPTED x3 | the refusal taught where `calendar_months` lives |
| `dynamodb scan --consistent-read` | PASS x2 | 1504 then 1510, `NextToken` exhausted, denominator printed |
| `safe-merge.sh` / `safe-commit.sh` | PASS | `msg-verify MATCH` throughout; `git pull` correctly REFUSED by the gate |
| `surprise-row-gate.py` | PASS x2 | rows `Z-S103`, `Z-S104` |
| `commit-gate.sh` | caught 3 | a heredoc-mangled comment, an unused import, an ambiguous `l` binding |

**What worked:** letting the parser and the suite be the oracle instead of the order's prose; writing
down rollback values before they were needed; naming the cause of every zero. **What failed:** two
wrong pin edits, one inferred count, two heredoc backslash losses. **Gap found:** `ap15.AC1.sh`
crashes on a JSON `null` `build_commit` -- named to the issuer.

## Blockers

**None owned.** Every item is a clock, a signature, or another seat:

- `[1.0.0_SA_CTO~Z]` `[2.0.0_SA_COO~O]` -- sign or refuse OG-mg-1's R1 and R2, each alone.
- `[2.0.0_SA_COO~O]` -- `Z-S102` and `Z-S104` disarms; the `<status>` flips.
- `[0.0.3_BG_BBGTerminal]` -- OG-mg-1's AC3 positive arm, after r30 and the writes: re-run its
  capability exercise on the 8 tools it measured denied and read 8 of 8 ALLOWED.
- **Clocks** -- OG-ap-15's AC2 at the five sweeps (schwab 12:15Z, blackdiamond 13:00Z, orion and
  eclipse 16:00Z, etf 23:30Z); OG-ap-14's B2 window 11:00Z-23:00Z.

## Current State (handoff -- zero prior context assumed)

- **Live and unchanged by this stretch:** the five `opal-assets-silver-*` converters on their signed
  packages; the gateway on `b0c75d24f1`. **No write was made to `gateway-access-state-table`** --
  `prepare()` writes nothing and `activate()` was never called.
- **Five ap-15 ledgers** L1+L2 CLOSED, L3 `HELD-SOVEREIGN-GATED` on each family's own sweep. **No
  ledger on this lane is open-and-unexplained**, and none is open for ap-14 or mg-1 yet -- Phase B
  opens those entry-and-sentinel-first.
- **Branches:** `rel-nfra-oplgtw-r30b` @`92698aea8c` is the release both halves signed;
  `rel-nfra-oplgtw-r30` @`db3d1972bc` is kept as the record of what was signed BEFORE C3 fired.
  `rel-nfra-oplgtw-fd2` holds the five ap-15 builds (keep -- the live pins name its commits);
  `rel-fd2-do3` holds the three merged drain-only releases. `rel-fd2-drainonly` and `rel-fd2-do2` are
  abandoned pin-row attempts: reachable, landed nothing, droppable.
- **Worktrees:** `C:/tmp/og-rel-r30b` (the signed release), `C:/tmp/og-r30-live` (pristine, now
  detached at `b0c75d24f1`; it exists for the pre-existing-failure classification and can go once
  ap-14 closes), plus `og-rel-fd2`, `og-rel-fd2b`, `og-rel-r30`. Four older release/rollback pins
  are `worktree lock`ed.
- **Off-repo staging:** `%LOCALAPPDATA%/opal/og-salt/mg1/` holds `mg1_identities.json`, the three
  candidates and their `prepare` diffs. **Nothing there is in git, and nothing in git names an
  identifier.**
- Push state: **LOCAL @`189bbbb8d2`**, measured by `git ls-remote`. Push is never this seat's act.

**What the next act needs, concretely:**

1. **At each ap-15 sweep**, read that sweep's `meta/backfill-status.json` silver section for
   `dlq_drain` with `family` equal to that family, record `sweep_request_id` and
   `sweep_was_scheduled`, then `deploy_ledger.py hold --release`, close L3 and close the entry. **No
   ad-hoc invoke.** If a graded sweep wrote no status section at all, the key is absent for an
   input-state reason -- re-read at the next scheduled sweep rather than roll back working code.
2. **`AP15_GRADE.json`** then takes one row per family and `ap15.AC2.sh` grades it; all five are
   `released: true`, so AC2 needs all five sweeps.
3. **OG-ap-14 B2 on the GO**, 11:00Z-23:00Z: **re-confirm live is still `b0c75d24f1`** (C3 lapses the
   GO again otherwise) and that one gateway release is in flight across every worktree; ledger
   `nfra-oplgtw-gateway-release-r30` entry and sentinel first; deploy `92698aea8c`; then one SSM md5
   read equal to the release tree, and **C2: `bbg_identity_admitted_8` reads 8, or STOP and redeploy
   `b0c75d24f1`**.
4. **OG-mg-1 Phase B** only on the GO naming both halves AND after ap-14's ledger is CLOSED. The
   candidates are staged; re-read the deny-email source at the act (**exactly one alias, or STOP with
   a BLOCKING row**), and expect `acs.ConditionFailed` to refuse the write if either record moved
   since `prepare()` -- that staleness guard is the optimistic condition's, not mine to implement.
