# AMGT_RESAPP task order -- `AMGT-ba-16` -- THE COMPARABLE AS A STATED RESTRICTED SELECTION (WITH ONE COMPANY COUNTED ONCE), AND PEERS V READ THROUGH ONE MAPPING TABLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-16</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~282</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; two pure modules and their tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no read path is added; the functions score dicts their callers already hold.
comp-adversary: RUN by the issuer at the cut -- r77_ba16 AC1 FAILS at the base (no mapping table: a 12-peer set in the scanner vocabulary yields 0 measured z-scores, and a suppressed V carries `reason` but no `absent_reason`); AC2 FAILS (a deeper-rung member with NO factor values is chosen; no restriction is printed; the subject's own second listing is chosen as its comparable); AC3 PASSES (the |K| >= 8 and |M| >= 3 floors, the subject dropped, Bloomberg-mnemonic rows still score). Row Z-S162: Peers V reads ABSENT for 33 of 33 served names, K=12 and M=0 on each (the row's figure, not re-read at the cut).
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; no pool read is needed.
</preflight>

**Your worktree:** `C:/tmp/r77-282` (branch `wk-AMGT_RESAPP-282`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-282`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-16` (round 77, decomposition s.85)

The CTO's ruling (`ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @4a89bef967, section B; rows Z-W20-S11 and Z-S162), in its words:

- The comparable pack is RESTRICTED SELECTION, stated. The set is built from names that carry a key and the factor values,
  and the pack prints its restriction (N eligible of M). A set too short to compare reads ABSENT with its reason.
- `peers_v.py` reads the peer objects through ONE declared mapping table (scanner-factor name to measure, such as fcfy and
  ey_ntm), and every ABSENT carries an `absent_reason`. Today 33 of 33 read ABSENT_SOURCE because the two vocabularies
  share no key.

And the COO's ruling (`deliverables/2.0.0_SA_COO~Z/round76/COO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` @fb9ca91ad5, section
C; row Z-W21-S3): the restricted selection deduplicates by company identifier in the same pass. One company can sit in the
peer database twice, under two identifiers that do not join, so a subject has ranked as its own top peer.

What is NOT yours: what Peers V means where a peer set is short is at Andrew. Keep the floors as they are.

**Build, with these names (the checks call them):**

1. **`lib/research/scores/peers_v.py`: ONE declared table, `SCANNER_FACTOR_MAP`.**
   - The landed peer rows carry the scanner's vocabulary: `factors: {fcfy, ey_ntm, shldr_yield, peg_ntm, eps_fwd_gr_1yr,
     ...}`, `market_cap_musd`, `cap_currency`. The six measure functions read Bloomberg mnemonics. The table maps each
     measure id to the scanner factor it may be read from, with the transform (for example percent to fraction, or the
     reciprocal for inverse PEG) and the factor-registry NAME the mapping rests on
     (`infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json`, read through
     `lib.research.posture.fit.load_registry()`).
   - A factor is mapped ONLY where its registry name states the same quantity as the measure. Where no scanner factor
     states a measure (EBITDA / EV and sales / EV have no code among the 26 preset codes), that measure has NO row in the
     table and reads ABSENT with an `absent_reason` saying the scanner serves no figure for it. Do not invert, combine or
     approximate one factor into another measure.
   - `score_peers_v` reads a row in EITHER vocabulary: a row carrying the Bloomberg mnemonics scores as it does today; a
     row carrying `factors` is read through the table. Nothing else in the maths moves (the winsorising, the median, the
     sample sd, the six-peer measure floor).
   - Every ABSENT carries `absent_reason`: each measure record, and the suppressed-V record (which today carries only
     `reason`; keep `reason` and add `absent_reason` with the same sentence).
2. **`lib/research/posture/comparable.py`: the restricted selection, stated.**
   - A graded member is ELIGIBLE when it carries a security key AND at least one factor value (a non-empty `factors` on
     its row). The comparable is chosen only among eligible other-side members, in the same order as today (rung, then
     log-cap distance). The re-run path applies the same rule to its candidates.
   - The record gains `restriction: {eligible: N, of: M, rule: <one plain sentence>}`, where M is the members graded.
     When no eligible other-side member exists and the re-run finds none (or is disabled), `comparable` is null and
     `reason` states the restriction with its two numbers.
   - `company_identifier(security_key, member=None) -> str or None`: ONE function that returns the company identifier
     of a key (the member's own identity cell when it carries one, else the served identity record for the key: the
     company-level FIGI, else the LEI; None when neither is stored). Before the choice, a member whose company identifier
     equals the subject's is dropped and counted in `denominators["same_company_as_subject"]`, and two members sharing
     one are counted once (`denominators["duplicate_company"]`). A member with no identifier is kept and never guessed.
     Every caller inside the module reaches it as the module-level name `company_identifier`, so a test can substitute
     it (the issuer's AC2 does).
3. **Tests.** `lib/research/scores/tests/test_peers_v_mapping.py` (new): the table against the registry names, both
   vocabularies, each ABSENT's reason. `lib/research/posture/tests/test_posture.py`: its fixtures carry no `factors`
   today, so add them where a comparable is expected, and add arms for eligible N of M, none eligible, the subject's own
   company, and a duplicated company.

`lib/research/api/tests/` holds older tests of these two modules and is another cell's directory. Do not edit it. Run it before your commit and report its last line; if a test there fails because of your change, name it in your report with the one-line reason, and the issuer grades it on the shared tree.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W282-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no producer run, no table, no schedule, no vendor, SEC or model call, no portal write.
2. Andrew's floors do not move: `MIN_PEERS_FOR_V` 8, `MIN_MEASURES_FOR_V` 3, `MIN_PEERS_PER_MEASURE` 6. The subject is never in its own peer set.
3. Keep these names: `peers_v.MEASURE_NOT_COMPUTABLE_REASON`, `peers_v.LEGACY_MEASURE_NOT_COMPUTABLE_REASON`. The serving adapter reads them. Keep every existing key of both records; you only add keys.
4. `lib/research/scores/run_scores.py` and `lib/research/scores/divergence.py` are another cell's files this round (AMGT-ba-14); `lib/research/posture/packs.py`, `fit.py` and `lib/research/peers/engine.py` are not yours either. The mapping lives inside `peers_v.py`, so the producer needs no edit.
5. Any reason you write is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
6. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/scores/peers_v.py
lib/research/posture/comparable.py
lib/research/posture/tests/test_posture.py
lib/research/scores/tests/test_peers_v_mapping.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~282/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-16"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba16.py" --crit AC1 --where local; echo "exit=$?"</invocation><expect>C1-C4 PASS: one mapping table, three or more measured z-scores and a V on a 12-peer scanner-vocabulary set, and an absent_reason on every ABSENT measure and on a suppressed V; R77 BA16 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-16"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba16.py" --crit AC2 --where local; echo "exit=$?"</invocation><expect>C0-C4 PASS: the comparable comes only from members with a key and factor values, the record prints eligible N of M, none eligible reads no comparable with the reason, and the subject's own company is never chosen and is counted; R77 BA16 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-16"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba16.py" --crit AC3 --where local; echo "exit=$?"</invocation><expect>C1-C4 PASS (the control): the ruled floors hold, V is suppressed at seven peers, the subject is dropped, a Bloomberg-mnemonic row still scores; R77 BA16 AC3 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~282 <0.9.0_WK_AMGT_RESAPP~282@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~282/AMGT_RESAPP.TO-AMGT-ba-16.comparable-restricted-selection-and-peers-v-mapping.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the mapping table as built: each measure, its scanner factor, the transform and the registry name, and the measures with no row;
- the posture and scores suites' last lines, and the api suite's last line with any test your change breaks;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Z):** ROUND_ANALYSIS.round76.md @c8bbeeac10 section 4 item 10 (the comparable / Peers V mapping); rulings CTO @4a89bef967 section B and COO @fb9ca91ad5 section C (Z-W21-S3 rides this cell). Decomposition s.85. Chain `~282`, wave 0, no inbound edge. Checks dry-run at the base: ba-16 AC1 base: FAIL as expected; ba-16 AC2 base: FAIL as expected; ba-16 AC3 base: PASS as expected. No adapter hookup: the stored record passes through `scoped_amgt._plain_score_record`. The served Peers V moves only when the scores producer is next run (a pool write, not in this cell). `test_posture.py` is in the write set because its fixtures carry no factors.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~282</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
