# NFRA_TOOLARCH.ROUTES -- comp-routes trace consults the rewrite table + discloses the catch-all (lane ~A)

**archetype:** IMPLEMENT

**Agent:** `0.8.0_AE_CloudComp~A` | **Date:** 2026-07-23 | **TO:** NFRA_TOOLARCH.ROUTES (issued `1.0.0_SA_CTO~Z`)
**Commit:** `d008e7cf1` (pushed CLOUD, `3d6490851..d008e7cf1`) | **Verification:** `3.0.0_SA_CVO~Z`

---

## Current State

**COMPLETE.** `comp-routes trace <url>` now resolves a URL to its S3 key through the rewrite table the
tool already carried, names the rule that fired, and discloses a catch-all match as a DEFAULT rather
than a resolution. All six acceptance criteria met; landed and pushed.

Session shape: fresh lane-`~A` session (prior watcher `b8z42aa8x` dead, re-armed `bl5ib1n2z`), startup
protocol, one GO in the inbox, executed end to end in-session.

---

## What was wrong, and the part that had to be corrected

The TO opened with ~D's finding: *trace returns `Origin: S3-opalinvest-portal` for ANY path,
byte-identical.* Phase 1 was reproduce-it-yourself, so I did, and **that claim is false.** The CF
behavior matcher discriminates correctly — the MDPF path matched `/api/general/*` with a different
origin, auth and edge set than a nonsense path, which fell to `/*`. I reported the falsification
before touching code (214643Z). CTO~Z accepted it, amended the TO in place, and owned the propagation.

**The real defect, correctly scoped, and reproduced byte-identical:** trace was undiscriminating
*within* a matched behavior, and **never emitted an S3 key at all** for a behavior-matched URL. Three
paths under `/api/general/*` produced identical output:

| | path | rule that actually applies |
|---|---|---|
| T1 | `/api/general/json/mdpf/global/aggregate-aua-timeseries.json` | `/api/general/json/ -> json/` |
| T2 | `/api/general/json/zzzz/total/garbage/nonexistent.json` | same rule, junk suffix |
| T3 | `/api/general/NOT-json-prefix/whatever.txt` | **a different rule**, `/api/general/ -> json/` |

T3 is the sharp one: a different rewrite rule applied and the output could not tell you that.

**Why the corrected version is the worse defect, not the milder one.** "Same answer for every input"
is useless but *obvious* — an agent notices. "Correctly behavior-matched, authoritative on CF/auth/edge,
and silently blind to the rewrite layer" hands back a half-answer that the reader assumes was whole.
Partial correctness masking an unanswered question is harder to catch than total uselessness.

**Probable origin of the overstatement, and it is not carelessness.** In Git Bash, MSYS rewrites a
leading-slash URL argument to `C:/Program Files/Git/api/...` before the process starts. The mangled
string no longer begins with `/`, so `cmd_trace` (`routes_cli.py:55`) skipped the URL branch entirely
and ended at `No match for` — a **false ABSENT manufactured by broken retrieval**, the same class as
the `git show <ref>:<path>` mangle in CLAUDE.md. `MSYS_NO_PATHCONV=1` does *not* help: it leaks into
the launcher and mangles the *script* path instead. ~D observed a real thing; the instrument between
~D and the truth was broken.

---

## What was built

- **Limb A (wiring, not a build).** `RoutingTable.resolve_s3_key` already existed
  (`extract_routes.py:182`) and was already used on the route path (`:821`); the behavior branch simply
  never called it. Extracted `match_rewrite_rule()` as **the one matcher** and made `resolve_s3_key`
  delegate to it, so the rule *named* in the output and the key *emitted* can never disagree. No second
  table, no hand-copy.
- **Limb B (honesty, always-on, no suppress flag).** A catch-all match announces itself as a DEFAULT
  and states that it does not discriminate. Keyed on `behavior.order == 0` — the structural default
  slot — **not** on the literal `"/*"` string.
- **Limb C (R1R3).** `comp-routes` moved from `pending_declaration:` into `contracts:` with coverage,
  six named blind spots, and plane/grain/scope/vintage. Header to stderr so stdout stays parseable.
- **MSYS argument repair**, announced on stderr rather than silent — flagged to CTO~Z as out-of-scope
  but load-bearing: without it the acceptance passes in PowerShell and fails in the shell the fabric
  actually runs in.
- **Bucket derivation fix** (see residuals).

---

## Evidence

**Discrimination mutant (the acceptance) — 4/4 pairwise DIFFERENT**, where T1/T2/T3 were byte-identical
before. And *correct*, not merely different:

```
Rewrite: /api/general/json/ -> json/  (general json passthrough)
S3 key:  json/mdpf/global/aggregate-aua-timeseries.json
S3 URI:  s3://opal-data-portal-v2/json/mdpf/global/aggregate-aua-timeseries.json
```

That key was verified to **exist live** — 254,419 bytes, LastModified `2026-07-23T21:18:53Z` (comp-keys,
applied plane). Resolved *to* the DE/COO key truth; not re-ruled.

**Mutant harness — 6/6 redden, restored green.** A green suite proves nothing about a guard that was
never mutated:

| mutant | verdict |
|---|---|
| M1 stop consulting the rewrite table (the original defect) | REDDENS |
| M2 disclose on EVERY answer (an always-on warning conveys nothing) | REDDENS |
| M3 key the disclosure on the pattern string, not the default slot | REDDENS |
| M4 revert bucket to the `s3_origin_config` test | REDDENS |
| M5 matcher returns the first rule always | REDDENS |
| M6 MSYS repair returns the query unchanged | REDDENS |

16 new bidirectional tests (every limb binds both directions and names its mutant, per the house rule
in `test_routes_unresolved_not_none.py`); **71 pass** across the full routes + output-contract suites;
`commit-gate` clean; `comp-manifest-check completeness` all invariants PASS (output-contract: declared
18 + pending 47 = 65; stage-2 vocab: 20 tools, violations `{}`).

One test I wrote was **wrong and the suite caught it**: I asserted a default behavior with a
non-matching `path_pattern` would still disclose — an unreachable state, since the parser hardcodes
`path_pattern="/*"` for the default slot (`extract_routes.py:329`). Replaced with the inverse
discriminator (an *ordered* behavior carrying `/*` must NOT disclose), which reddens the string-match
mutant honestly and says plainly that it is a unit-level discriminator.

---

## Residuals routed to CTO~Z (named, not silently expanded into)

**R1 — OAC origins mistyped, and it reaches an auth surface.** `bucket_name` was derived as
`domain.split('.')[0] if is_s3`, where `is_s3` tests for the **legacy** `s3_origin_config` block. Both
OAC-fronted S3 origins (`opal-data-portal-v2` — the MDPF one — and `opal-data-assets`) therefore carried
an empty bucket. Fixed (domain-derived; display-only, sole consumer `routes_cli.py:212`). `origin_type`
deliberately **not** changed: it feeds `cmd_stats`' s3-vs-apigw split, `cmd_auth_map`'s grouping and
`Route.cf_origin_type`. **Live consequence today:** `comp-routes auth-map` lists both S3 origins under
"EDGE JWT + API GW AUTHORIZER", which is wrong — an auth-posture surface reading falsely, which I rated
above the tool-hygiene tier when routing it.

**R2 — the rewrite table is TRANSCRIBED, not parsed.** `_parse_rewrite_rules` opens the router
`index.mjs`, **discards the content** (a literal `_content = ... # noqa: F841` dead read at `:485`), and
appends hardcoded rules. The table is a hand-maintained copy of the routers' if/else chains: a router
edit nobody mirrors is invisible to every consumer, silently — **and this fix makes more things depend
on that table being right.** This is precisely the frozen-enumeration class the TO warned me off
re-creating, already present one layer down, load-bearing and undetected. Not touched (out of scope;
parsing JS properly is a build). Candidate: a gate diffing transcribed rules against the real chains,
or at minimum a loud vintage line on `comp-routes rewrites`.

**Still uncovered by the class** (declared blind spots, so they render rather than hide): a key computed
*inside* a Lambda@Edge router or backend Lambda; and the DESIRED-plane limit — parsed Terraform +
committed router source cannot tell a declared behavior from a deployed one.

---

## Compiler Tools

| Tool | Invocation | Result | Notes |
|---|---|---|---|
| `comp-routes trace` | 4 path classes, before + after | PASS | The subject. Pre-fix T1==T2==T3 byte-identical; post-fix 4/4 different + correct. |
| `comp-routes rewrites` | full table dump | PASS | Confirmed `/api/general/json/ -> json/` already present — the wiring target, no new table needed. |
| `comp-routes behaviors` / `origins` | full dumps | PASS | Surfaced the OAC bucket/origin_type mistyping (R1). |
| `comp-keys prefix` | `opal-data-portal-v2 json/mdpf/global/` | PASS | **Applied-plane grounding** of the resolved key: exists, 254419 B, `2026-07-23T21:18:53Z`. Turned a discrimination claim into a correctness claim. |
| `comp-manifest-check completeness` | full family | PASS | Output-contract, registration, stage-2 vocab, retired-alias invariants all PASS after the pending -> contracts move. |
| `comp-system` | regenerate 06 | PASS | Required by the fail-closed commit gate; diff was pure vintage churn (timestamp + HEAD), no content change — verified before staging. |
| `commit-gate.sh` | 3 `.py` files | PASS | py_compile + ds-precommit + ruff clean. |
| `comp-surface-check` | auto in safe-commit | OK | 6 files, no critical surface. Read the output rather than treating the unblocked commit as a pass (it cannot block). |
| `comp-pulse` (risk-reflex) | auto in safe-commit | CLEAN | Measured: 6 files vs 1484 danger nodes. |

**Not run and why:** `comp-iam` / `comp-blast` / `comp-validate` — no IAM change, no boto3 call, no
infra or gold-script surface touched; this is a read-only local tool change with no deploy leg.

---

---

## Addendum — follow-on `a119bc34c`: `--json` was silently returning prose

Written after the TO closed. `~B` flipped TOOLBHVR.ROUTE within the hour (`cdd2f0fb5`), kept the three
outcomes distinct rather than collapsing them, and asked for a `--json` arm. Checking what `--json` did
*before* building it: **the behavior branch returned before the JSON emitter was ever reached, so
`comp-routes trace --json <url>` printed human prose and exited 0.** The flag silently ignored itself
for the entire URL query class — the same honesty class the TO closed, one layer over. A consumer's
parser breaks, or it doesn't break and they string-match to a wrong class with no error anywhere. So
this was a defect found by a feature request, and I built it rather than queueing it.

**The fix is the enum, not the JSON.** `outcome` ∈ `RESOLVED | UNRESOLVED_NO_RULE | CATCHALL_DEFAULT |
NO_MATCH`. `NO_MATCH` is the class nobody had named: it printed "No route found" as prose and emitted
*nothing* under `--json`, so a consumer got an empty parse and had to guess what silence meant. ~B's
framing is sharper than mine and is worth keeping: **"a guess about silence"** is the defect, and the
reason it was missing is the reason it was dangerous — three outcomes are what the human output *shows*,
and the fourth is the one that shows nothing. An absent result is not a result.

**Precedence, decided explicitly and bound by a test:** `CATCHALL_DEFAULT` outranks `RESOLVED` whenever
`behavior.order == 0`. If no specific behavior claimed the path we don't know it is served at all, so
that caveat beats a key we could nominally compute — meaning `s3_key` may be non-null while `outcome` is
`CATCHALL_DEFAULT`. Conservative on purpose; `catchall` also ships as its own boolean so neither axis has
to be recovered from the other. ~B accepted and will key on `outcome` only.

`plane`/`vintage`/`blind_spots` are read from the output contract **at run time**, so ~B is retiring
their hardcoded DESIRED-plane caveat in favour of it — a paraphrase-copy removed rather than created.
That is the R1R3 surface doing its job in its first real consumer.

Mutants now **9/9 redden** (M7 `--json` falls through to prose, M8 inverted precedence, M9 enum
collapsed), restored green. 21 tests in the file; 76 pass across the routes + output-contract suites.

**New minor residual:** `--json` on the endpoint-function / component branches still routes through
`_print_route` (human text). Scoped out — the URL branch is what `~B` consumes.

**R2 got worse, not better:** the transcribed-not-parsed rewrite table now has a *second* consumer, so
the cost of that drift going undetected went up today. Re-flagged to CTO~Z on that basis.

---

## Blockers

None. Event-driven, standing by. 20 pending TOs remain in the lane queue.

## Next Steps

- [`1.0.0_SA_CTO~Z`] Disposition R1 (OAC origin_type -> wrong `auth-map` grouping) and R2 (transcribed
  rewrite table, no drift detector). Sequence the next lane-`~A` TO.
- [`3.0.0_SA_CVO~Z`] Independent verify: the discrimination mutant, the always-on disclosure (including
  the negative control that a specific match is NOT labelled a default), and the 6-mutant harness.
- [`0.8.0_AE_CloudComp~B`] Flip TOOLBHVR.ROUTE's no-coverage message to a real route; keep UNRESOLVED
  and catch-all-DEFAULT distinct from resolved, or the false authority reappears one layer up.
- [`0.8.0_AE_CloudComp` base] `comp-routes` is now a declared contract — no action unless the batch
  `comp-system` regen wants it folded.
