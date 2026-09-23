# AMGT_CORPUS task order -- `CRPS-c-10` -- ROUND 1: the one-call substrate read -- one call by security key returns the prior reports, the continuation artifact, the sector template, the fund form and the typecast, each with its content hash and its inputs; a second call after a new report lands shows a changed hash for exactly the artifact that changed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell READS the store and writes nothing to it; its difference arm runs on an in-memory stub.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-c-6`. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, then `git log --oneline -1 -- lib/research/corpus/` and
  `ls lib/research/corpus/`. Test that `continuation.py`, `sector_template.py`, `fund_form.py`, `typecast.py` and
  `typed.py` all exist there. Three of them were built by sibling workers and reach your worktree only because the issuer
  merged them into your branch before continuing you. **If any is absent, STOP with a BLOCKING row naming it.**
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY. NEVER WRITE TO S3 IN THIS CELL.**

## 1. THE CELL, inlined in full -- `CRPS-c-10` (manifest row R10, outcome FWD-8)

**FWD-8, verbatim:** *"A consumer can fetch, for one security, every corpus artifact it needs in one call, and can tell
when any of them has moved. DONE WHEN EXERCISED -- one call by security key returns the prior reports, the continuation
artifact, the sector template and the typecast, each with a content hash; a second call after a new report lands returns
a changed hash for exactly the artifact that changed and unchanged hashes for the rest. ACCEPT: The analysis layer never
re-derives this substrate and never guesses whether it is current."*

**Manifest R10:** *"the one-call substrate read by security key | a read path over R1-R9; no new store."*
**`C-INPUT-HASHED`:** *"Every artifact this project serves carries `{key, sha256}` for each input it was derived from, its
own content hash, and the method version that produced it. A consumer decides freshness from those hashes and never from
a clock."* **`C-NO-RAW-BRONZE-AT-SERVE`:** R1/R2 bytes are read by derivation cells and the addendum's producer, never
streamed to a page. So `prior_reports` returns KEYS and hashes, not bytes.

**THE GOLD SHAPE you wrote in `CRPS-c-6`** is shared by all four gold artifacts: `inputs` sorted `{key, sha256}`,
`content_sha256`, `method_version`, and object name `<inputs_sha16>.json`. Each gold module exposes
`current_inputs(<subject>)`. **The latest artifact for a subject is the one whose `inputs` equal `current_inputs`.** If a
sibling module deviates from that shape, that is a BLOCKING row naming the module. Do not adapt around it.

**RULED -- what you build:**
1. **`lib/research/corpus/substrate.py`:**
   - `substrate(security_key, client=None)` returns
     `{security_key, prior_reports: [{bronze_key, sha256, period, class}], continuation, sector_template, fund_form,
     typecast}`. Each artifact entry is `{uri, content_sha256, method_version, inputs_count, current: bool}`, or
     `{absent: <reason>}` when none exists (for example, a name with no business type). The sector template is the
     name's business type through `sector_template.business_type_of`. The fund form is the continuation's
     `fund_of_record`, or absent. It performs no derivation: it READS.
   - `current` is True when the stored artifact's `inputs` equal the module's `current_inputs(...)` now. That is the
     "can tell when any of them has moved" half.
   - `python -m lib.research.corpus.substrate --first-covered` calls it ONCE for the security key
     `continuation --show-first-covered` picks, and prints one line per member:
     `<member> <content_sha256 or n_reports> current <bool>` (for `prior_reports`, the count and a hash over their
     `(key, sha256)` pairs), then `members 5 present <p> absent <a>` and `call_count 1`.
   - `python -m lib.research.corpus.substrate --difference-arm` is **the second-call proof, driven on demand in an
     IN-MEMORY STUB STORE, never in S3:**
     (a) copy into a stub client (a dict keyed by bucket/key, with the list/get/put the modules use) every object that the
         first-covered name's five members and their inputs reference, READ from S3;
     (b) call 1, recording the five hashes;
     (c) add ONE new synthetic report for that name to the stub: a bronze object plus its extraction plus its silver row,
         built with the package's own writers pointed at the stub;
     (d) re-derive ONLY the continuation on the stub (`continuation.build` + `gold_put` on the stub);
     (e) call 2, and print per member `<member> call1 <h> call2 <h> changed <bool>`, then
         `changed_set [...]` and `expected_changed_set ['continuation', 'prior_reports']`, then
         `difference_ok True` if and only if the two sets are equal.
2. **`lib/research/corpus/tests/test_substrate.py`**, offline, under the package poison:
   - **ONE CALL, FIVE MEMBERS:** over a stub store, `substrate()` returns all five keys;
   - **ABSENT IS NAMED:** a name with no business type gets `sector_template: {absent: ...}`, never another type's;
   - **CURRENT FLIPS:** adding an input makes `current` False for exactly the artifact whose inputs moved;
   - **THE DIFFERENCE ARM CAN FAIL:** if the continuation is NOT re-derived in step (d), `difference_ok` is False.

**What this cell does NOT do:** no re-derivation in the live store, no S3 write, no page, API or adapter (the
`AMGT_RESAPP` addendum's), no bytes served.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain A, cell 6 of 7 on this slot. It needs all four gold cells drained VALID
(c-6 yours; c-7, c-8 and c-9 from sibling slots, merged into your branch by the issuer).

## 3. SURFACES

<paths>
lib/research/corpus/substrate.py
lib/research/corpus/tests/test_substrate.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-10.one-call-substrate-read.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` file, `lib/research/harvest/store.py`, `lib/opal_naming.py`. Scratch in
`.scratch/c10/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND** (issuer amendment on row `AMGT_CORPUS-Z-S4`): a wrong object you wrote is superseded by a
  NEW key (bump `method_version`), never deleted. An S3 delete is a human-confirmed act on this estate.
- **Pure ASCII source, LF, Python 3.9-compatible.** NO S3 write of any kind; the difference arm is stub-only by
  construction. Pass the stub client explicitly; the live read uses a default client for GETs and LISTs only.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_substrate.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.substrate --first-covered 2>&1 | tail -10</invocation><expect>(?s)prior_reports \d+ \S+ current \S+.*continuation [0-9a-f]{64} current True.*typecast [0-9a-f]{64} current True.*members 5 present \d+ absent \d+.*call_count 1</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.substrate --difference-arm 2>&1 | tail -10</invocation><expect>(?s)continuation call1 [0-9a-f]{64} call2 [0-9a-f]{64} changed True.*typecast call1 ([0-9a-f]{64}) call2 \1 changed False.*difference_ok True</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-c-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-10"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c10/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- In `--difference-arm`, print the members in the order `prior_reports`, `continuation`, `sector_template`, `fund_form`,
  `typecast`, so AC3's pattern reads them in sequence.
- `.scratch/c10/hyg.py`: the same shape as before, over this order's `<paths>`.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-c-10.one-call-substrate-read.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` returns rc 0.
3. Flip to `complete` only if every criterion passes. Commit with `--only`.
4. Report ONCE: AC2's five lines and AC3's `changed_set` and `difference_ok` lines.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the difference arm runs in a stub because a "new report lands" in the real library is not this
project's act (FWD-9), and a synthetic object in the production harvest prefix would be cruft. The stub holds real
copies of the live objects, so the call-1 hashes equal the live hashes AC2 prints. That is the bridge between the two
arms, and the CVO can check it. **Drain note for the issuer:** before continuing `~1` onto this order, merge the drained
c-7, c-8 and c-9 branches into `~1`'s worktree branch.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
