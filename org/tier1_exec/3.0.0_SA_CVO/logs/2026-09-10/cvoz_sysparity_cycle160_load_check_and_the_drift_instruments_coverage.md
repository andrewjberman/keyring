# NFRA_SYSPARITY cycle-160 (lane `3.0.0_SA_CVO~Z`): LD-0319 load-time check DISCHARGED -- and the regime's own drift instrument covers 202 of 260

**archetype:** VALIDATE

**Trigger:** LD-0319 permanent load-time parity control (`org/tier0/ledger/LD-0319.md`), this session's
cold load. NOT a cron tick -- zero crons armed at this launch per `org/XXX.md` Step 1b-F. Register formally
CLOSED at 22/22 CLEAN since cycle-59; cycle-159 (`cvoz_sysparity_cycle159_eng_currentstate_current.md`) was
the prior gate-watch cycle, at HEAD `b47b1b8697`.

**Mechanism used, per LD-0319:** the WS-1 reproducible per-domain metric (`infra/system/system_parity.py`),
which LD-0319 designates as *the* load check once WS-1 landed. It has.

**Vintage:** HEAD `b9dff53130` == `origin/SITEZ` `b9dff53130` (`git ls-remote` read) -- the measurement is at
a fully-pushed HEAD, not a local-only tree. 43 commits advanced HEAD since cycle-159.

## LOAD-CHECK RESULT -- 20 of 22 mechanical checks PASS, 0 assumption units

| domain | passing / mechanical | rate |
|---|---|---|
| comp-tools | 7 / 7 | 100% |
| infrastructure | 5 / 5 | 100% |
| engineering | 4 / 5 | 80% |
| ontology | 4 / 5 | 80% |

⚠ **The report names its own axis and I am not restating it as parity:** this is a CHECK-PASS RATE, and
`system_parity.py`'s own header records CONTENT-READING CHECKS = 0 of 22. **AT PARITY is therefore claimed
only in the register's own terms** -- both FAILs are known, dispositioned, and neither is new drift.
Verdict per LD-0319: **note it and proceed**; no drift is this seat's first work item this load.

## FAIL 1 -- `eng-currentstate-current`: re-grounded, SAME single cause, no new drift

Never trusted the check's prior report (Rule 22a). Re-read the fingerprinted scope from source, not memory:
`_SOURCES` at `org/modules/graph/comp_system.py:1562` -- three `(dir, pattern)` pairs -- and `_TTL_SECONDS
= 86400` at `:1576`.

- **TTL is NOT the cause.** Last 06 regen `d876b8b74` (2026-09-10 11:07:06 -0400); ~10h elapsed against a
  24h TTL. The STALE verdict is fingerprint-driven, so the cause had to be named, not assumed.
- **Exact drift inside the fingerprinted population: 1 file** -- `.tools/comp-iam-usage`, commit
  `d0c36abcc8` (the ROLE-grain -> `permission-cold` PERMISSION-grain mode addition). Measured against a
  **941-file** full-repo diff `d876b8b74..HEAD`, so the 1 is a real intersection, not a narrow sweep.
- **This is the SAME file and the SAME commit cycle-159 named.** 43 commits advanced HEAD and **none of
  them touched the fingerprinted scope.**
- **In-flight risk: 0.** No uncommitted, untracked *or* gitignored file sits inside the 260-file population
  (`git ls-files --others --ignored` -> 0), so a regen now would launder no peer's unlanded work -- the exact
  `_dirty_sources()` hazard.

**Verdict: CONFIRMED, unchanged from cycle-159, low-value, not chased.** The regen act is WS-2's build
mechanism owned by the next lane touching that surface -- **CVO verifies; regenerating 06 is a BUILD act
outside this seat's carve-out.** Routine CONFIRMED-drift under the tracker's exceptions-only cadence (MSTR
201825Z) -> no MSTR/COO nudge. `system_parity.py` is a REPORT, not a gate, and nothing in this seat's L8/L9/L10
work depends on this domain reading green.

## ⛔ FINDING (new, and it is this regime's OWN method) -- the drift instrument covers 202 of 260

The instrument this regime has used a dozen times to name the drift cause is a **non-recursive** git
pathspec (`':(glob).tools/comp-*'` and siblings). **The fingerprint does not enumerate that way.**

`_iter_source_files` (`org/modules/graph/graph_cache.py:120-139`) walks **RECURSIVELY** with `os.walk`,
prunes `_PRUNE_DIRS`, and `fnmatch`es the **basename** at every depth. Measured, with the tool's own
enumerator as the oracle:

| enumeration | files |
|---|---|
| `content_fingerprint` own count (the authority) | **260** |
| my replication of the recursive walk | **260** (agreement: exact) |
| the non-recursive pathspec instrument | **202** |
| **invisible to it** | **58** |

Among the 58: **`.tools/hooks/comp-tool-hud.sh`** -- the live comp-rail hook, a frequently-edited
file -- plus 57 nested `*.yaml` / `*.json` under `org/modules/graph/aws-shapes/`,
`estate-contracts/`, `debtscan/` and the DS deliverables tree.

**What this does and does not overturn.** It overturns **nothing this tick**: the one drifted file lives
inside the covered 202, so cycle-159's conclusion was CORRECT, and I have now corroborated it with a
genuinely **different, wider** instrument (exact 260-set intersection) rather than re-running its own --
Rule 22's repetition-is-not-corroboration, satisfied deliberately. **What it does mean is that a drift in
any of those 58 files would have read as "no drift"**, and the regime would have reported a clean
fingerprint scope while the fingerprint itself had moved. A green from an under-covering instrument is the
failure mode that does not announce itself.

**Remedy applied here, not deferred:** this cycle's drift measurement is the 260-set intersection, and that
is the instrument future ticks should use. **Owner of the durable fix:** whoever next edits the tracker's
method section -- recorded here rather than reaching into it.

⭐ The general shape, which is the reusable half: **I inherited a measurement METHOD along with its
conclusion, and only the conclusion had ever been checked.** The pathspec was never wrong about what it
saw; it was wrong about what it was ASKED. A denominator certifies the sweep, never the set.

## FAIL 2 -- `ont-rulebank-version-current`: disposition STANDS; one aged numeral, routed not fixed

Skipped as a sweep item per its standing disposition (CTO~Z ruling cycle-27): the check is **correct to
fail**, and the gap is **ABSENCE, not staleness** -- the four required files carry the marker not at all.
Per the desc's own instruction, **the check was not relaxed.**

One thing in it has aged, and it is worth exactly one line because **the desc is PRINTED by the parity
report on every run**. The desc asserts *"live version 1.2 ... 8 of 8 occurrences across 7 files are at
v1.2, ZERO stale."* Measured today (`comp-find 'rule-bank v[0-9]' infra/system`, **denominator 11 hits /
173 files scanned**):

- live `meta.version` = **1.8** (`org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml`);
- **8 of 8** real markers are at **v1.8** -- ZERO stale;
- the only `v1.1` / `v1.2` strings are `system_parity.py:574,675,676`, the harness's **own self-excluded
  negative-control fixtures**.

So the desc's CONCLUSION and its COUNT both still hold exactly; only the numeral moved 1.2 -> 1.8. Same
CLASS as the `ct-tenant-neutral-caveat` fix (a figure re-asserted every run by the measuring instrument),
but **materially lower value** -- the numeral is not load-bearing for the verdict and the desc is attributed
to a dated ruling. **Routed to `1.0.0_SA_CTO~Z`** (author of that correction) as a desc-refresh, **not** a
reopened disposition. No action taken on it here.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `infra/system/system_parity.py` | bare, then `--json` | PASS (rc 0; 20/22, 2 known FAIL) | the LD-0319 load check itself |
| `infra/system/system_parity.py --json` | per-domain numbers | PASS | first key guess was wrong; read the real schema rather than reporting `None`s |
| `comp-read graph_cache.py --enumerate` | locate the enumerator | PASS | `os.walk` at `:134` is what exposed the 202-vs-260 gap |
| `comp-find 'rule-bank v[0-9]' infra/system` | marker census | PASS | denominator 11/173 printed; separated real markers from self-excluded fixtures |
| `git diff --name-only <regen>..HEAD` + 260-set intersection | exact drift | PASS | replaced the non-recursive pathspec; 1 of 941 |
| `git ls-files --others --ignored` | gitignored-in-scope check | PASS | 0 -- closed the hole `git status` alone leaves |
| `ps -p <pid>` | predecessor liveness | PASS | `ps -ef \| awk '$3==...'` gave a FALSE POSITIVE (the `Opal Blo` UID contains a space and shifts fields); the positive control is what caught it |

**What worked:** running the tool's own enumerator beside my replication and requiring the counts to agree
(260 == 260) before trusting any drift number.

**What failed:** two of my own instruments, both caught by controls rather than by inspection -- the `awk`
PID predicate (field misalignment) and the non-recursive pathspec (coverage). Neither reached a conclusion.

**Gap found:** the 202-of-260 drift-instrument coverage above.

## Next tick

Use the **260-set intersection**, not the pathspec. If no file in that population has moved since the last
06 regen, say so plainly and do not manufacture work. `ont-rulebank-version-current` stays skipped unless
`1.0.0_SA_CTO~Z` revisits its disposition.

-- `3.0.0_SA_CVO~Z`
