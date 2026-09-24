# AMGT_RESAPP task order -- `AMGT-rl-1` -- THE INSTRUMENT: the DOM measurement checked in beside ui-smoke, the six-state contract check that CAN FAIL, the class census, and the fixtures

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~130</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; the declaration is in the issuance commit message.
EGRESS CLASS, declared: NONE. Everything renders against a LOCAL vite dev server with a stubbed session and fixtures.
  No vendor call, no Bloomberg call, no AWS call, no fetch to any origin but localhost.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~130`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and `test -d org && test -d .tools && echo TREE-OK`;
then `git -C portal rev-parse --abbrev-ref HEAD` and `test -f portal/scripts/ui-smoke.mjs && echo PORTAL-OK`. Every Bash
call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~130;`. **NEVER RUN AN INSTALL** (`node_modules` is linked by the
provisioner). Never push, merge, rebase, `checkout --` or `clean`.

**The portal is a NESTED repository at `<worktree>/portal`** on its own branch. A portal file is committed INSIDE that
directory: `cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~130 <0.9.0_WK_AMGT_RESAPP~130@opal.agent>" -F <msgfile> -- <portal paths>`;
then the OUTER commit from the worktree root carries the moved gitlink plus your deliverables:
`bash .tools/safe-commit.sh --author "..." -F <msgfile> -- portal org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~130`.
Commit messages PURE ASCII, written by the Write tool, never `printf`. Your scripts and logs live under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~130/` (grant-free), never under `.scratch/`.

## 1. THE CELL -- `AMGT-rl-1` (round 37, decomposition s.45)

`FWD-29` says: *"The contract's render check PASSES, and CAN FAIL."* `C-RENDER-IS-THE-ORACLE` says a source read never grades
a render outcome; acceptance for `FWD-21`..`FWD-29` is **a PNG at 1440 plus the DOM measurement JSON for each of six
states**. Today the PNG half exists (`portal/scripts/ui-smoke.mjs`) and the measurement half exists only as a script the
CRO ran from a scratch directory. **This cell checks the measurement in beside ui-smoke, wraps both in ONE check over the
six states that grades the contract's predicates, adds a class census over source files, and lands the fixtures the
check renders with. Every later cell's criteria name these files, so this cell runs alone and first.**

**INPUTS, in the repository (read them; copy, do not retype):**
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round37/ui-measure.mjs` -- the CRO's measurement pass,
  sha256 `0d786803534478292fae0b497dfb60876dffd6b2d5501d8c810df8d2fed0fe8f`. Its output fields are the ones the walk's
  `MEASUREMENTS.json` carries (`bandContainersTopLevel`, `fonts`, `weights`, `sizes`, `radii`, `shadows`,
  `lowContrastChars`, `purpleFills`, ...).
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round37/uiContractFixtures.json` -- six live
  `/api/scoped/amgt` bodies captured 2026-09-24 05:03Z on the served stack (rankings + timeseries for
  `trending/chatter`, `watchlist`, and BA_US_Equity's `thesis`, `overlay`, `peers`), keyed by URL substring exactly as
  `ui-smoke.mjs --fixtures` expects (longest matching substring wins).
- `org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_FRONTEND_WALK_20260924/MEASUREMENTS.json` -- the walk's numbers
  for the six states; your baseline run must land within +/-1 band of them.
- `portal/DESIGN.md` C1, C3, C8, C9, C11, C12 -- the predicates.

## 2. WHAT YOU BUILD (portal, relative to `portal/`)

**(1) `scripts/ui-measure.mjs`** -- the CRO's script, checked in with two additions and nothing removed:
`--scope <css-selector>` restricts every count to elements inside that selector (default: the whole body), and the output
gains `bandContainersOutsideTabPanel` = top-level band containers NOT inside any `[data-tab-panel]`. Same auth stub, same
fixture router, same CLI shape as ui-smoke (`<route> [--port] [--fixtures] [--click "<name>"]... [--width]`), and the same
MSYS de-mangle. Prints ONE JSON object.

**(2) `scripts/ui-contract-check.mjs`** -- THE CHECK. `node scripts/ui-contract-check.mjs --port <n> --out <dir> [--fixtures <path>] [--states list,thesis,exec,peers,model,posture]`.
It starts nothing; it expects a vite dev server on `--port`. For each state it runs, as child processes, `ui-smoke.mjs`
(PNG at 1440, `<out>/<state>.png`) and `ui-measure.mjs` (JSON, `<out>/<state>.json`) with the same fixtures and clicks:

| state | route | clicks (role=tab names, exact) |
|---|---|---|
| `list` | `/security-analysis` | none |
| `thesis` | `/security-analysis/BA_US_Equity` | none (Thesis is the default tab) |
| `exec` | `/security-analysis/BA_US_Equity` | `Exec Management` |
| `peers` | same | `Peers` |
| `model` | same | `Model` |
| `posture` | same | `Posture` |

Then it grades each state's JSON against the `FWD-29` predicates and prints ONE table, state x predicate, each cell
`PASS` or `FAIL <measured value>`: `bandContainersTopLevel == 1` (C3) · `fonts` keys == {`Lato`} (C1) · `weights` keys
within {400, 700} (C1) · no `sizes` key below 11 (the ladder) · `radii` keys within {`2px`, `3px`, `4px`} or a pill
(any value >= 9999px) (C11) · `shadows == 0` (C11; nothing is focused in a fresh render) · `lowContrastChars == 0` (C9) ·
`purpleFills` == 0 for `list` and == 1 for every Security-mode state (C8, `FWD-27`). It prints the denominators (states
run of states asked; PNG bytes per state) and exits **1 if any cell reads FAIL, 0 only if every cell PASSES**. The
default `--fixtures` is `src/pages/SecurityAnalysis/__harness__/uiContractFixtures.json`.

**(3) `scripts/ui-class-census.mjs`** -- `node scripts/ui-class-census.mjs <file-or-dir>...` walks `.ts`/`.tsx` files and
counts, per file and per category, the class idioms the contract forbids on a light page. Categories and patterns,
exactly: **idiom** -- `text-white`, `bg-white/`, `bg-black/`, `text-(zinc|gray|slate|neutral|emerald|amber|red|blue|lime|pink|indigo|violet)-(100|200|300|400)\b`,
any `(text|bg|border|ring|divide|placeholder)-[a-z]+-\d{2,3}/\d{1,3}\b`, `opacity-\d`; **size** -- `text-\[(\d+)px\]` with
the number below 11; **weight** -- `font-(thin|extralight|light|medium|semibold|extrabold|black)\b`; **radius** --
`rounded-(md|lg|xl|2xl|3xl)\b` and `rounded-\[(\d+)px\]` with the number not in {2,3,4}; **shadow** -- `\bshadow(-(sm|md|lg|xl|2xl|inner))?\b`
not immediately preceded by `focus-visible:` or `focus:`. Output: one line per file (`<file> idiom=<n> size=<n> weight=<n> radius=<n> shadow=<n> total=<n>`),
then `FILES <k> TOTAL <n>` -- a census, exit 0 always. Comments and string literals are NOT excluded (a forbidden idiom in
a comment is a false hit the reader can see; a real one hidden by exclusion cannot).

**(4) `src/pages/SecurityAnalysis/__harness__/uiContractFixtures.json`** -- the fixtures file, copied from the input above,
byte-identical (`sha256sum` both and print).

## 3. BOUNDS

1. **No page source moves.** Nothing under `src/pages/SecurityAnalysis/` but the fixtures file; nothing under `src/ui/**`,
   `src/components/**`, `src/api/**`; no `package.json`, no vite config. `ui-smoke.mjs` is NOT edited (the check calls it).
2. **The dev server:** start it yourself from `portal/` with the bun binary at
   `C:/Users/Opal Bloomberg/AppData/Local/Microsoft/WinGet/Packages/Oven-sh.Bun_Microsoft.Winget.Source_8wekyb3d8bbwe/bun-windows-x64/bun`
   (`"<bun>" run dev --port 5181 > ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~130/dev.log 2>&1 &`),
   wait for `Local:` in that log (up to 90 s), run the check, then stop it (`taskkill` by the PID you recorded, or leave
   it and say so). Port **5181** -- no other port.
3. **No install, no fetch outside localhost, no S3 delete, no key or session hunting, no push.** Standing.
4. **REFUSE, do not rescue.** A criterion you cannot satisfy as written is REFUSED with its measurement in your report;
   never widen an expectation, never edit this order, never make the check pass by weakening a predicate.

## 4. SURFACES

<paths>
portal/scripts/ui-measure.mjs
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-class-census.mjs
portal/scripts/ui-smoke.mjs
portal/src/pages/SecurityAnalysis/__harness__/uiContractFixtures.json
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round37/ui-measure.mjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round37/uiContractFixtures.json
org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_FRONTEND_WALK_20260924/MEASUREMENTS.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~130/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5181 --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~130/contract-check-baseline; echo "exit=$?"</invocation><expect>THE CHECK CAN FAIL, PROVEN ON TODAY'S PAGE: six states run of six asked; for each state a PNG larger than 20 KB and a JSON exist under contract-check-baseline/; the state-by-predicate table printed; bandContainersTopLevel reads FAIL on EVERY state with a measured value of 2 or more (within +/-1 of the walk's 2,4,3,3,3,3); weights reads FAIL (300/500/600 present) and radii reads FAIL (8px present) and shadows reads FAIL (1) on every state; purpleFills reads FAIL on list (4); and the process exits 1. A run that exits 0 on today's page FAILS this criterion -- it means the check cannot fail</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis</invocation><expect>THE CENSUS DETECTS THE KNOWN STATE (positive control against the walk's 246 idioms over 18 files): one line per file with the five counters and a total, then FILES &lt;k&gt; TOTAL &lt;n&gt; with k at least 18 and n at least 200; PostureTab.tsx, LeadPanel.tsx, ExecManagementTab.tsx, PeersTab.tsx and SecurityOverlay.tsx each read total at least 15; SecurityAnalysis.tsx reads idiom=0. Print the exact line for each of those six files</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/ui/components/states &amp;&amp; sha256sum src/pages/SecurityAnalysis/__harness__/uiContractFixtures.json ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round37/uiContractFixtures.json</invocation><expect>THE NEGATIVE CONTROL AND THE FIXTURE PIN: the census over src/ui/components/states (the C12 states built to the contract) reads TOTAL 0 with FILES at least 2 -- if it reads non-zero, REFUSE this criterion and print the offending lines rather than tuning a pattern; and the two sha256 sums are IDENTICAL (the fixtures file landed byte-for-byte)</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~130/AMGT_RESAPP.TO-AMGT-rl-1.the-instrument.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from
the worktree root. **The status flip is the ISSUER'S** -- this order's surfaces block does not name `task-orders/`; leave
the record face alone and say so. **Report once, naming:** the six band counts your baseline measured beside the walk's,
the census TOTAL and FILES, the states-dir census result, and the portal commit hash plus the outer commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 0 of round 37. Every wave-1 order names `scripts/ui-class-census.mjs` in its criteria and the
issuer runs `scripts/ui-contract-check.mjs` at every drain, so this cell is spawned alone and merged before any surface
cell is spawned. The predicate set is `FWD-29`'s DONE WHEN line, read from the ENDPOINT fence @`1ffb156ecd`, not from
the addendum. Portal base at the cut: `c1ac41ec` (DEV HEAD = gitlink, measured equal).

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~07:1xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID on the worktree's own checker (re-run by this seat inside the worktree; the
main tree's checker correctly refuses an out-of-tree instance). The baseline measured EXACTLY the walk's band counts
(2,4,3,3,3,3), weights 300/500/600, radii 8px, shadows 1, purpleFills 4 on list, exit 1 -- the check CAN FAIL. Census
FILES 30 TOTAL 341 (the walk's 246 over 18 was a narrower file set; the census walks 30 files incl. harnesses). ONE
BLOCKING row, W130-S1: the naming gate (LGIC_ENFORCE DEC-6, ENFORCE) refused the fixtures file on captured S3-key-shaped
values; RESOLVED at the drain by placing the fixture under __harness__/tests/ -- the gate's own exemption class for fixture
data (naming-gate.py:1421-1423) -- and moving the check's default path with it (portal 513bb3c5, sha unchanged). Every
later face that names `uiContractFixtures.json` reads it at the tests/ path. Portal commits c388c70d + 513bb3c5.

<status>complete</status>
<round>37</round>
<slot>~130</slot>
<fabric>site-z</fabric>
