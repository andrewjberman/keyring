# AMGT_RESAPP task order -- `AMGT-rk-128` -- the NATIONAL-REGULATOR adapter (HK) behind step 5's declared stub, keyed on LISTING VENUE and not on `domicile`, with acceptance test (c) KNOWN FAMILY binding and negative-controlled

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-128</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~128</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence and runs no producer.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant is edited and no credential is minted.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
EGRESS CLASS, declared: ONE public-regulator HTTP fetch (HKEX), the same class step 1/2 already make to EDGAR and
  step 4 makes to the issuer's own site, inside the international battery Andrew RATIFIED @4de34f0d95. NOT a vendor
  API, no credential, no key. Bounded and counted by AC4. No Bloomberg call of any kind.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~128`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
First act: print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that
`lib/research/filings/battery.py` exists. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~128;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.
⛔ **Every `.scratch/` script runs as `PYTHONPATH="$(pwd)" python .scratch/...`** (rows `Z-W117-S1`/`S3`); and
`.scratch/**` has NO static lane entry (`Z-W126-S3`), so if the validator refuses to commit your scripts, **that is
the known estate gap -- keep them, cite their output, do not fight the validator.**

## 1. THE CELL -- `AMGT-rk-128` (round 35, decomposition s.43)

**THE AUTHORITY, already ratified -- no amendment and no new word from Andrew.** `prd:801-803`, inside CONTRACTS
(the ratified-text half), ratified by Andrew @`4de34f0d95`:

> *"(1) EDGAR by ticker; (2) EDGAR by Bloomberg CIK; (3) ESEF / UKSEF by LEI; (4) the company's own site;
> **(5) the national regulator, one adapter per jurisdiction, built only for a name that step 4 fails.**"*

⚠ **That clause WRAPS ACROSS THREE LINES. Read it with `sed -n '801,803p'`, never a grep** -- a single-line
pattern cannot match it, and the only thing a grep finds is section 12a's inline QUOTE of it at `:2058`. **The
CTO reproduced exactly that failure in its own verification and caught it only because the line number was 1,255
lines from where the citation said.**

**THE SEAM ALREADY EXISTS AND IS ALREADY WIRED -- you are building an ADAPTER, not a step:**
- `battery.py:1219-1229` -- *"STEP 5 -- the national regulator (declared only; no adapter is built here)"*,
  returning `{"attempt": _attempt(5, "national-regulator", jurisdiction, "no adapter for jurisdiction %s"),
  "passed": False, "battery_extra": {}, "seeds": []}`.
- `run_battery:1309` -- `(5, lambda: _step5_national_regulator(keys))`, inside the ordered `steps` list.
- The `_attempt(...)` record shape (`:1237`) and the `{attempt, passed, battery_extra, seeds}` contract are FIXED.
  **Return the same shape.**

⛔ **THE STUB'S KEY IS `domicile` AND YOU MUST NOT USE IT. DISPATCH ON LISTING VENUE.**
**Measured by the issuer at the cut: `domicile` is present on 0 of 96 records** -- so an adapter keyed on it would
compute `"UNKNOWN"`, refuse, and never fire for any name while passing every test it wrote. **And it is the wrong
key in principle** (`1.0.0_SA_CTO~Z` msg 24670): a national regulator route asks *which regulator does this issuer
FILE with*, which is the **listing venue**, not the country of incorporation -- **a Cayman-incorporated, HK-listed
issuer files with HKEX.** ⭐ **Deriving a CORRECT `domicile` would faithfully reproduce the WRONG dispatch, which
is worse than an empty key because it looks like it works.**

**THE ACT, four parts:**
1. **Supply the dispatch key in the battery's OWN key layer** -- derive the listing venue. **No crosswalk write and
   no dependency on another chain**: `C-INSTANTIATION-ENTRY` (`prd:1837-1841`) enumerates five fields -- name,
   exchange, LEI, SEC id, CIK -- and **`domicile` is not one of them**, so nothing here crosses into chain I.
   ⚠ `keys_from_crosswalk`'s reason string claims otherwise; **that is a CODE comment asserting a CONTRACT's
   ownership and the contract does not say it.**
2. **Build the HK adapter** behind the stub, dispatched by venue, returning the fixed shape.
3. **Make ONE live HKEX fetch for `992_HK_Equity`**, bounded and counted (AC4).
4. **Mint the Rule 30 registry row** -- `infra/logic/registry/` holds **6 files, 0 naming `hkex` or `regulator`**.
   **It is this cell's own AC0, deliberately not restated as a contract.**

## 2. ⛔ THE BOUND THAT IS NOT NEGOTIABLE -- acceptance test (c)

**`1.0.0_SA_CTO~Z` made this BINDING on this cut (msg 24680), as the author of the disclosure:**

> **Acceptance test (c) KNOWN FAMILY is LOAD-BEARING for every non-US name. No cell may relax it to a warning, and
> no cell may treat (a) RIGHT ENTITY as sufficient evidence of the right document.**

**The measured reason:** five of Lenovo's EDGAR filings are `SC 13D` / `SC 13D/A` **in which Lenovo is the FILER
about ANOTHER issuer.** Test **(a)** matches on the issuer's name and **would PASS such a document.** ⭐ **The guard
holds on its THIRD leg, not its first.** ⛔ **An HKEX adapter that implements (a) and (b) and leaves (c) soft would
accept a document about a different company under a PASSING battery.** AC3 negative-controls exactly that.

## 3. ⛔ THE SEAM MUST BE WIDENED, AND IT IS TWO LINES

**Step 5 today takes `(keys)` and nothing else** -- no `http_get`, no `bronze_sink`, no `security_key`, no
`run_date`. **It cannot fetch.** Its own docstring says so: *"`bronze_sink` ... is threaded into steps 1, 2 and 4
only -- step 3 (ESEF) fetches an index, never a filing document, and **step 5 has no adapter**."*

⭐ **WIDENING IT IS TWO LINES, because `run_battery:1302-1310` builds every step as a `lambda:` CLOSURE** -- so
`security_key`, `keys`, `run_date`, `http_get`, `bronze_sink`, `cache_dir` and `seeds` are **ALREADY IN SCOPE at
step 5's own call site.** **Change step 5's OWN signature and its OWN lambda line. Nothing else moves.**

⚠ **THIS IS IN SCOPE AND THE BOUND BELOW IS PRECISE ABOUT IT** (CTO msg 24689): *"do not change the step list"*
means its **MEMBERSHIP and ORDER**, not one entry's arguments.

## 4. BOUNDS

- ⛔ **NO S3 DELETES OF ANY KIND** -- standing instruction, every AMGT project, without Andrew's word, **including
  delete markers** (a delete marker removal is itself a delete). CTO msg 24607.
- **`992_HK_Equity` ONLY.** PRD s.12 (`:1947-1949`, `:2007-2008`) makes the validation scope ONE security until the
  trial is graded, and explicitly does not authorise *"any security other than Lenovo"*.
- **No Bloomberg call. No vendor API. No credential.** The single HKEX fetch is a public regulator, declared above.
- ⛔ **STEPS 1-4 AND THE STEP LIST'S MEMBERSHIP AND ORDER ARE UNTOUCHED.** Steps 1-4's signatures and lambda lines
  **byte-identical**, `_attempt` untouched, acceptance's (a)/(b)/(c) semantics untouched. **AC5 negative-controls
  this by printing steps 1-4's signatures and call sites BEFORE and AFTER.**
- ⛔ **YOU MAY NOT WRITE `infra/logic/**`, AND IT IS NOT IN YOUR `<paths>`.** That lane is `PLATFORM_LOGIC_DOCS`,
  permitted to `4.0.0_SA_CRO` and its `~A`-`~D` lanes only -- ⛔ **`~Z` is excluded BY NAME and no permitted lane
  is live on this fabric.** **If AC0 shows a winning outcome needs a bronze address, you do NOT mint the Rule 30
  row: you RECORD that it is needed and STOP at that finding.** It is carded to Andrew with two sibling lane gaps.
- `portal/**` is NOT named and may not be written.

## 5. SURFACES

<paths>
lib/research/filings/battery.py
lib/research/filings/fetch.py
lib/research/filings/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~128/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
.scratch/r128/**
</paths>

⚠ **`infra/logic/registry/**` IS DELIBERATELY ABSENT** -- see BOUNDS. The issuing seat does not hold that lane and
may not admit you to it; naming it would be the delegation CVO ruling R5 forbids.

## 6. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-128"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r128/ac0.py</invocation><expect>⛔ THE SEAM QUESTION ANSWERED FIRST, BEFORE ANY ADAPTER CODE: does producing a WINNING step-5 outcome -- `passed: True` with a `battery_extra` that `fetch.build_source_object(..., battery=...)` ACCEPTS -- REQUIRE a `bronze_sink`? Answer it from `build_battery_source_object`'s own requirements, printed, citing file:line. NOTE the precedent and its limit: `_step3_esef_lei` FETCHES with NO bronze_sink, so fetch-without-bronze is an existing shape in this module -- but step 3 NEVER WINS by design, so it does not prove a step can WIN without one. If the answer is NO, say so and proceed. If YES, say so, RECORD that a Rule 30 registry row is needed, and do NOT mint it (see BOUNDS)</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-128"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r128/ac1_keys.py</invocation><expect>the dispatch key MEASURED before any edit, with BOTH depths printed and labelled: record-level `exchange` present on 36 of 96, `identity.exchange` present on 4 of 96 -- and a statement of WHICH DEPTH this cell reads. The eligible population printed as its own denominator: 36 records carry a `security_key`, 60 do not and CANNOT dispatch under any key. Venue derived for all 36 with 0 unparseable, the venue histogram printed, HK = 1. `domicile` present on 0 of 96</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-128"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3</invocation><expect>the filings suite BASELINE before your edit -- record passed/failed as A0. A measurement, not a bar</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-128"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r128/ac2.py</invocation><expect>the adapter exercised HERMETICALLY (stub transport, no network): for a venue-HK name the HK adapter DISPATCHES and returns the fixed `{attempt, passed, battery_extra, seeds}` shape with `step=5, route` naming the regulator; for a venue with no adapter it returns the DECLARED-STUB refusal unchanged; and ⛔ for an UNPARSEABLE or ABSENT key it returns the declared-stub refusal and does NOT silently dispatch -- print all three branches. Prove `domicile` is not read: the adapter must dispatch correctly on a record whose `domicile` is None</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-128"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r128/ac3.py</invocation><expect>⛔ TEST (c) NEGATIVE-CONTROLLED, the cell's most important arm: feed the acceptance path a document that PASSES (a) RIGHT ENTITY -- the issuer's own name present -- but is a FILER-ABOUT-ANOTHER-ISSUER form of the SC 13D class, and assert it is REJECTED, with the printed reason naming (c) KNOWN FAMILY and NOT (a). Then the positive control: a genuine annual-family document ACCEPTS. Both printed. A run where (a) alone decides is a FAILURE of this criterion</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-128"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r128/ac4.py</invocation><expect>the ONE live HKEX fetch for 992_HK_Equity, with `http_fetches` printed from a COUNTER and equal to 1, `bloomberg_calls 0`, `s3_deletes 0`. Print the HTTP status, the URL, and the acceptance outcome with which test decided it. ⚠ If HKEX is unreachable or refuses, that is a RESULT: record it with its status and reason and do NOT retry in a loop -- an UNRESOLVED with a measured reason is a legitimate outcome of this cell</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-128"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3 &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r128/ac5_untouched.py &amp;&amp; git diff --name-only $(git rev-parse HEAD) -- lib integrations infra .tools portal</invocation><expect>passed = A0.passed + your new arms, failed = 0 (pre-existing failures named if any). ⛔ THE WIDENING NEGATIVE CONTROL: steps 1-4's SIGNATURES and their four lambda lines printed BEFORE and AFTER, asserted BYTE-IDENTICAL; the step list's MEMBERSHIP and ORDER printed as [1,2,3,4,5] unchanged; `_attempt`'s signature unchanged; and ONLY step 5's signature and its own lambda line differ. The diff list names ONLY lib/research/filings/** -- ⛔ NOTHING under infra/, portal/ or .tools/, and in particular NO infra/logic/registry/ row (see BOUNDS: you record that one is needed, you do not mint it)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~128/AMGT_RESAPP.TO-AMGT-rk-128.regulator-adapter-hk.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance>
AC0,AC1,AC2,AC3,AC4,AC5` from inside it. ⚠ **The `<status>` flip is the ISSUER'S** -- this order's `<paths>` does
not name `task-orders/`. **Leave `<status>` alone and say so.** Commit messages PURE ASCII, written by the Write
tool, never `printf`. Report once naming: AC0's two depths, AC3's (c)-rejection reason, and AC4's fetch count.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** five findings were measured BEFORE this order existed (s.43a) -- the seam already exists and is
wired; its key is empty on 0 of 96; the key is WRONG in principle; the ownership blocker was a code comment, not a
contract; and this seat's own coverage number was wrong by 9x (right field name, wrong DEPTH). **Each would have
cost a round. The whole finding was four reads, no worker and no worktree.**

<status>pending</status>
<round>35</round>
<slot>~128</slot>
<fabric>site-z</fabric>
