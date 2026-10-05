# AMGT_RESAPP task order -- `AMGT-ar-1` -- FWD-39 CLOUD REPAIR: NO CLOUD CARRIES THE COMPANY'S OWN NAME IN ANY FORM, OVER EVERY NAME THAT SERVES A CLOUD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~223</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write; the range route already reads the gold headlines it counts, and the alias list is declared in code.
comp-adversary: RUN by the issuer at the cut -- r68_served c27 FAILS at the base, local and deployed: names 212, serving 199; C1 6 own-name offenders (AZN astra, GOOGL/GOOG google, HESAY herm, NSRGY nestl, XOM exxon,mobil); C2 82 clouds with a measured junk or boilerplate token.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r68-223` (branch `wk-AMGT_RESAPP-223`, cut from the issuance commit with `--portal-ref 6936e92b`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r68-223`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ar-1` (round 68, decomposition s.76; PRD v0.37 FWD-39, ACCEPT "without the company's own name")

The word cloud on `/security/<key>/timeline` is built in `lib/research/api/scoped_amgt.py`: `_word_cloud_block`,
`_word_cloud_own_words` and the declared `WORD_CLOUD_STOP_WORDS` with its `WORD_CLOUD_STOP_WORDS_SOURCE`. Round 67 removed the own
ticker root and the short and long name words. A census over every cloud-serving name (199 of the 212 in `chatter_window`) still finds the
company's name in forms the name source does not spell, and junk stems from a tokenizer that is not accent-safe.

1. **An accent-safe tokenizer.** Normalize every headline with NFKD and strip combining marks before splitting into words, so "Nestle"
   and "Hermes" in their accented forms tokenize whole. "nestl" and "herm" must never be a term.
2. **A DECLARED own-name alias list,** beside the declared stop-word list, with its own `..._SOURCE` string naming
   `ADJUDICATION_v80`. Seed it with the measured cases, keyed by the ticker root:
   - XOM: exxon, mobil;
   - GOOGL and GOOG: google;
   - NSRGY: nestle;
   - HESAY: hermes;
   - AZN: astra.
   `_word_cloud_own_words(key)` returns them for that key.
3. **A compound-name split.** A name word that joins two parts (for example "AstraZeneca", "ExxonMobil") also yields each part of 4 or
   more letters as an own-name word.
4. **The measured boilerplate joins the declared stop list:** "movers", "premarket", "sees", "estimates", "hon", "hai". Keep the
   `_SOURCE` string current.
5. **The plant test** `lib/research/api/tests/test_word_cloud_aliases.py`. It covers:
   - each measured alias is excluded for its name;
   - an accented headline tokenizes whole;
   - a compound name yields its parts;
   - the new boilerplate is excluded;
   - a control: an ordinary topical word ("diesel", "chip") still survives.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W223-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Only which terms a cloud serves may change. No route, status, key or other field moves.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~223/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_word_cloud_aliases.py; echo "exit=$?"</invocation><expect>every plant case passes (aliases excluded, an accented headline whole, compound parts, the new boilerplate excluded, the topical control kept); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell c27 --where local; echo "exit=$?"</invocation><expect>population names 212 (or the current part's count) with 0 non-200; C1 PASS 0 own-name offenders; C2 PASS 0 junk or boilerplate offenders; R68 C27 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell c23 --where local; echo "exit=$?"</invocation><expect>R67 C23 SERVED: YES (the round-67 repair holds, the inverted window keeps its reason); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~223 <0.9.0_WK_AMGT_RESAPP~223@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~223/AMGT_RESAPP.TO-AMGT-ar-1.cloud-census-repair.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the functions and declared lists you changed;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-67 analysis @2db6fd3e3d ruling 1; CVO ADJUDICATION_v80 @69ce44def1. Served by ar-3.

<status>pending</status>
<round>68</round>
<slot>0.9.0_WK_AMGT_RESAPP~223</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
