# AMGT_HARVST task order -- `HVST-h-8` -- H8: the DESIGN SPEC for the security page's mention timeline -- the day-by-day line, dissecting any day into its articles strongest first, and the event spans -- with the API shape it would read; SPEC ONLY, no `.tsx`, no API edit

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~8</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a document; arms nothing, runs nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~8`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every EXISTING path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~8;`.
- **NEVER RUN AN INSTALL. NEVER CALL AWS. NEVER WRITE OR EDIT ANY FILE UNDER `portal/` OR `infra/`, AND NEVER WRITE A
  `.tsx`, `.ts` OR `.py` FILE.**

## 1. THE CELL, inlined in full -- `HVST-h-8` (manifest row H8; outcomes FWD-5, FWD-6)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-DESIGN-SPEC-FIRST`): *"No `.tsx` for the timeline until its
design spec is approved. This is `AMGT_RESAPP`'s rule, applied here."*

**The outcomes the spec must make buildable:**
- **FWD-5, ACCEPT:** *"On a company's page there is a day-by-day line of how much it was written about; clicking any day
  shows the articles behind that day, strongest first."* DONE WHEN *"an analyst has opened a company's timeline, picked
  a day, and read the articles behind it listed strongest first"*.
- **FWD-6, ACCEPT:** *"Bursts of real coverage about the company appear as marked events with a headline, not just as
  spikes in a count."* DONE WHEN *"the timeline for the validation security shows at least the event runs the stored
  articles support, each with its lead headline, and opening one lists its articles"*.
- **Andrew's words** (the brief's record): *"a timeline graph of all mentions where we can dissect them at any point"*,
  categorised by strength of signal (*"how much the security is mentioned in them, is it mentioned in headline?"*) and
  by time.

**The data the timeline reads** (PRD v0.2 contracts). Each is ONE full snapshot per build under `date=<build date>` in
`opal-data-harvest`:
- `chatter_daily`: per (security, UTC day), dense from 2026-01-01, with `articles_total`, `tier_a`..`tier_d`,
  `mention_score`, `mention_count_total`, `publishers_distinct`, `trailing_7d_sum`, `trailing_30d_sum`,
  `baseline_30d_sum`, `baseline_30d_days`, `cumulative_ytd`, `first_published_utc`, `last_published_utc` and
  `data_status` (`COMPLETE | PARTIAL | DENIED`).
- `article_security_mention`: per (article, security), with `mention_count`, `mention_in_title`, `mention_in_lead`,
  `first_mention_block`, `blocks_hit`, `blocks_total`, `match_forms`, the vendor tags, `co_mentioned_securities`,
  `co_mention_count`, `is_roundup`, `signal_tier`, `signal_weight`, the three clocks, `lag_hours` and lineage.
- `chatter_event`: per event, with `first_day`, `last_day`, `days_span`, `articles_total`, `tier_a`, `tier_b`,
  `publishers_distinct`, `lead_article_key`, `lead_headline` and `article_keys`.
- **`C-HV-ABSOLUTE-ONLY`: every relative figure** (a breakout ratio, a z-score, a 0-100 score, a within-article share)
  **is computed at SERVE time** by the API, never stored. Your spec states which relative figures the view shows, and
  that the API computes them.

**The precedent you follow, read-only:**
- `AMGT_RESAPP`'s page spec, `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/DESIGN_SPEC.md`,
  with its per-section files (for example `.../0.9.0_WK_AMGT_RESAPP~3/SPEC_SECTION_coverage.md`).
- The CTO's frontend framework and synthesis,
  `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/1.0.0_SA_CTO~Z/AMGT_RESAPP_FRONTEND_FRAMEWORK_20260911.md` and
  `.../AMGT_RESAPP_FRONTEND_SYNTHESIS_20260911.md`.

**Match their form:** where the section sits on the page, the components, the states, the data each reads, and what the
page says when data is absent.

**RULED -- what you write:**
1. **One file:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md`. Pure
   ASCII. It has exactly these eight `##` sections, in order:
   - `## 1. Placement`: where on the security page, relative to the sections the page spec already defines.
   - `## 2. The line`: the day-by-day series. Which measure is plotted by default (`mention_score`), what toggles
     exist (for example `articles_total`, tier stacks), the time range, and how a PARTIAL or DENIED day is DRAWN so it
     never reads as a quiet day.
   - `## 3. Dissecting a day`: the click. The article list is ordered strongest first (tier, then `mention_count`, then
     `published_utc`), and each row shows the headline, the publisher, the tier, "in headline" and "in lead" marks, and
     the time.
   - `## 4. Event spans`: how an event is drawn over the line, its lead headline, and what opening one lists.
   - `## 5. The API shape`: the route or routes the page would call, their parameters and their response fields,
     naming which fields are read straight from gold and which relative figures the API computes at serve time.
     **Name no implementation file.** The route belongs to the build cell after approval.
   - `## 6. States`: loading; no articles for the security; the floor date; PARTIAL and DENIED days; a security that
     was never collected.
   - `## 7. What this spec does not decide`: every open call, including the working defaults (the tier weights, the
     event rule), which stay Andrew's.
   - `## 8. Acceptance`: how an analyst proves FWD-5 and FWD-6 on the validation security, Lenovo `992_HK_Equity`.
2. **Nothing else.** The approval is Andrew's, and the build is a later cell cut after it.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain B, its only cell. It is independent of chain A: it reads contracts, not
tables, and spawns at once.

## 3. SURFACES -- what you may read and write

<paths>
org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md
org/missions/D5/AMGT/AMGT_HARVST/brief/BRIEF_AMGT_PUBLICATIONS_BRONZE_SILVER_GOLD_20260922.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/DESIGN_SPEC.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/SPEC_SECTION_provenance.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/SPEC_SECTION_coverage.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/1.0.0_SA_CTO~Z/AMGT_RESAPP_FRONTEND_FRAMEWORK_20260911.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/1.0.0_SA_CTO~Z/AMGT_RESAPP_FRONTEND_SYNTHESIS_20260911.md
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-8.timeline-design-spec.md
</paths>

- **Everything outside your deliverables folder, the channel and this order is READ-ONLY.**
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~8 <0.9.0_WK_AMGT_HARVST~8@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **SPEC ONLY. Pure ASCII.**
- **Surprise rows:** `AMGT_HARVST-Z-W8-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-h-8"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "import re;t=open('org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/SPEC_SECTION_timeline.md',encoding='utf-8').read();h=re.findall(r'^## (\d)\. ',t,re.M);print('sections',''.join(h),'non_ascii',sum(1 for c in t if ord(c)>127),'crlf',t.count(chr(13)))"</invocation><expect>"sections 12345678 non_ascii 0 crlf 0" -- the eight sections in order, pure ASCII</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-8"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- portal infra lib && git status --porcelain -- portal infra lib && echo "--- end"</invocation><expect>NOTHING printed before "--- end" -- no code, no .tsx, no infra</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-8" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.**
- **AC3 is a JUDGMENT criterion,** graded by `3.0.0_SA_CVO~Z` at L9, never by you. Its question: would an engineer build
  the timeline from this spec alone, meeting FWD-5 and FWD-6? That means every state is drawn, every relative figure is
  named as serve-time, and no working default is fixed as a constant.
- Record AC3 as `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~8/AMGT_HARVST.TO-HVST-h-8.timeline-design-spec.proof_of_spec.json`.
2. Grade the mechanical criteria with `python .tools/proof-of-spec-check.py <instance> AC1,AC2`, which must return rc 0.
3. Flip to `complete` only if both pass.
4. Commit with `--only`.
5. Report once.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The approval is Andrew's** (decomposition s.9). On approval, the build cell (the `.tsx` and the `scoped_amgt.py`
   route) is cut at L10 from this spec, and the served page change then takes its never-widen pair.
2. **The spec names no implementation file on purpose,** so the approval is of the design, not of a code location.

<status>pending</status>
<round>1</round>
<slot>~8</slot>
<fabric>site-z</fabric>
