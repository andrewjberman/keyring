# AMGT_RESAPP task order -- `AMGT-rk-19` (producer half) -- FWD-18's re-keyed verification gate, over the EXCERPT never the passage map

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-19</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~26</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected and no schedule is read or written.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  S3 bucket/prefixes and DynamoDB table this project already reads and writes) under the existing Lambda
  execution role; it grants no new permission and provisions no new resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~26`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the
paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN FP, a queue of TWO
orders (`AMGT-rk-19` producer half, then `AMGT-rk-24` producer half). Chain FP holds every write to
`lib/research/filings/` this round, so that directory has ONE writer.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~26;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-19` producer half (FWD-18; ADDENDUM 2's A2.3, replacing s.3.1 items 1 and 4)

**THE MEASURED STATE.** BA's analysis object `filings/v1/BA_US_Equity/000162828026004357.analysis.json`
carries `thesis_driver.points` = `{2025: 600, 2024: 348, 2023: 528}`, `resolution: "cited"`. A prior read
searched all 276 passages of the object's own `passage_map` for each value and found none, and reported the
values as unverifiable. **That was wrong: `passage_map` never segments TABLE blocks, and the three values
occur exactly once each, as whole numbers, in the table "BCA deliveries, including intercompany deliveries,
as of December 31," in the Total column under the row for exactly the year the analysis labels** (this is
in `excerpt.text`, fingerprinted by `excerpt_sha256`, not in `passage_map`). The 2023 row wraps across lines:
`Deliveries 396 (9) 1 / 32 (14) 26 / 73 528`.

**RULED (A2.3):**
1. **Producer, domain re-keyed:** the verification domain is the submitted excerpt, `excerpt.text` under its
   `excerpt_sha256`, **never `passage_map`**. A point is kept only when its value occurs as a whole number
   (thousands separators normalised) inside the table-or-paragraph block that carries its **matching period
   label**. The block runs from that period label to the next period label or the block's end (so a row that
   wraps across lines is still inside its block). Each kept point records its character span in the excerpt
   and the excerpt hash. A point that locates in no block moves to `held_uncited` with that reason.
2. **Passage map, extended:** the analyzer additionally segments TABLE blocks into `passage_map`, so a
   verified point also carries a `passage_id` a page can link to (this is FWD-18's click-through, and it also
   answers row `W20-S8`'s coverage question for BABA). A span with no matching passage still verifies the
   value; it is just not rendered as a link.
3. Adapter and page are unchanged by this order (see the sibling orders `AMGT-rk-19` adapter half and page
   half, chain B and chain A respectively -- **do not touch `lib/research/api/scoped_amgt.py` or
   `portal/` from this order; they are outside your grant**).
4. **Criteria (this order's half):** (a) a PLANTED negative -- a point whose value occurs in no block of the
   excerpt -- MUST move to `held_uncited`; (b) a PLANTED wrong-period point -- a real value placed under
   another year's label -- MUST also move to `held_uncited`; (c) re-running the corrected logic over BA's
   ALREADY-STORED source/analysis objects verifies exactly 3 points with span + passage id, `resolution`
   updated to reflect verified status.

**NO NEW VENDOR CALL.** This is a pure re-verification pass over `excerpt.text`, already stored -- plain
Python text matching against bytes already on disk/in the pool. It both (i) fixes `analyze.py` for every
future run and (ii) is re-applied ONCE, in this order, to BA's existing stored `analysis.json` to correct it
in place (rewrite the object at its same pool key with the corrected `thesis_driver` block; do not mint a
new accession or re-fetch the source).

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis
`ROUND_ANALYSIS.round12.md` s.3.1 @`9419550eb1` and its **ADDENDUM 2** (same commit hash, appended) s.A2.1-A2.4,
which corrects s.3.1's own measurement and re-keys the gate. PRD v0.10, ADMITTED, both L4-R halves SIGNED,
no PRD change needed (A2.4: `C-FILINGS-ANALYZER` v0.7's resolution rule is applied to values; the ratified
text is untouched).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/analyze.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~26/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.filings-producer-verification.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant (you may read anything,
  including `filings/v1/BA_US_Equity/000162828026004357.analysis.json` from the pool and any other analyzer
  module); this block governs WRITES. You may WRITE the pool object at BA's existing key via the same
  `crosswalk.write_pool()` helper `analyze.py` already imports -- that S3 write is not a repo path and needs
  no `<paths>` entry, but do not write any OTHER pool key from this order. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~26 <0.9.0_WK_AMGT_RESAPP~26@opal.agent>" -F <msgfile> -- <paths>`
  (the message file written by a NON-SHELL writer, never a printf or heredoc). Never push, merge, rebase,
  `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO -- not your surface, stated for completeness. **THE PORTAL
DEV PUSH IS RESERVED** under LD-0367/0368. **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send,
notification or freshness checker.** Secrets through `comp-secrets` only. **NO NEW VENDOR CALL of any kind
from this order** -- the fix is pure text-matching over already-stored bytes; if you find you need to
re-fetch or re-invoke an LLM to satisfy a criterion, STOP and file a row instead. No non-ASCII in anything
you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- measure it yourself.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W26-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-19"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
from lib.research.filings import analyze
excerpt = 'Deliveries as of December 31: Total 528 Some other unrelated figure 999 for a year the block does not label'
period_labels = {'2023': 0, '2099': len(excerpt)}
verified, held = analyze.verify_points_against_excerpt({'2023': 528, '2099': 528}, excerpt, period_labels) if hasattr(analyze, 'verify_points_against_excerpt') else (None, None)
print('has_verify_fn', hasattr(analyze, 'verify_points_against_excerpt'))
print('verified', verified)
print('held', held)
"</invocation><expect>has_verify_fn True, and the PLANTED wrong-period point (2099: 528, a real value placed under a label that is not its own) is present in `held`, never in `verified` -- if the function name differs from `verify_points_against_excerpt`, the worker names the actual function it wrote and re-runs this invocation against it, recording the substitution in its report</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-19"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
from lib.research.filings import analyze
excerpt = 'BCA commercial aircraft deliveries, including intercompany deliveries, as of December 31: 2025 Total 600. 2024 Total 348. 2023 Deliveries 396 (9) 1 / 32 (14) 26 / 73 528.'
points = {'2025': 600, '2024': 348, '2023': 528, '2022': 4242}
result = analyze.reverify_thesis_driver(points, excerpt) if hasattr(analyze, 'reverify_thesis_driver') else None
print(json.dumps(result) if result is not None else 'NO reverify_thesis_driver FUNCTION -- name the actual one used')
"</invocation><expect>2025, 2024 and 2023 all verify (each value is a whole number present in the block carrying its own period label, thousands-normalised), each carrying a character span; the PLANTED negative 2022:4242 (present nowhere in the excerpt) moves to held_uncited with a stated reason. If the function name differs, the worker names the real one and re-runs this exact invocation against it</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-19"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3')
obj = s3.get_object(Bucket='opal-data-harvest', Key='filings/v1/BA_US_Equity/000162828026004357.analysis.json')
doc = json.loads(obj['Body'].read())
td = doc.get('thesis_driver', {})
print('points', td.get('points'))
print('held_uncited', td.get('held_uncited'))
print('resolution', td.get('resolution'))
print('has_passage_id_on_points', all('passage_id' in v for v in (td.get('points') or {}).values()) if isinstance(td.get('points'), dict) else 'points not a dict -- inspect actual shape')
"</invocation><expect>after this order's fix is applied and BA's stored object is corrected in place, `points` carries exactly 3 verified entries (2025, 2024, 2023) each with a span and, where a matching table passage exists, a `passage_id`; `held_uncited` is empty for BA specifically (all three of BA's real points DO verify per ADDENDUM 2); `resolution` reflects the corrected, value-checked state -- this is the live pool object, read fresh, not a cached copy</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~26/AMGT_RESAPP.TO-AMGT-rk-19.filings-producer-verification.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence),
graded by YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the
verdict); flip `<status>` to `complete`; commit with `--only -- <paths>`. **Do not stop here** -- your next
order (`AMGT-rk-24` producer half) is handed to you as a continuation; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
