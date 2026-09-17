# AMGT_RESAPP task order -- `AMGT-rk-21` -- resolve the 56 unkeyed coverage records via the chain that already resolved 158 of 161 holdings

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-21</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~28</issued_to>
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

**You are `0.9.0_WK_AMGT_RESAPP~28`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the
paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN ID, one order, the
whole of `lib/research/identity/` for this round.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~28;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-21` (FWD-1, FWD-13; S117/S120)

**THE MEASURED STATE.** FWD-1's ACCEPT is *"a company the firm already covers."* The firm covers 89 names
(`crosswalk/v1/<date>.json`); 33 carry a resolved `security_key`, 56 do not. **Every coverage bar this
project reports must print `served / 89` with `keyed 33` beside it -- grading against 33 makes the identity
gap invisible by construction.** The prior round-12 ruling's own S120 proposed measuring a "47 held-holdings"
partition and never did; that figure is now STALE (holdings resolution today reads 158 of 161) and no code
artifact defines "held-holdings partition" as a named field -- it is ledger prose, not a stored value.

**RULED:** resolve the 56 using the SAME chain that already resolved 158 of 161 ETF holdings --
`lib/research/identity/positioning_chain.py`'s `resolve_one()` (`:317-408`, precedence: CUSIP check-digit ->
FIGI-shaped -> SEDOL+domicile check-digit -> BBG-characteristics-CONFIRMED via `read_bbg_characteristics()`
`:218-250` + ETFClassifier name) and `build_positioning_identities()` (`:411-450`). **Never a bare-ticker
join and never `unknown` converted to `false`.** `crosswalk.py`'s `_record_for()` (`:257-332`) and
`_parse_bloomberg()` (`:213-247`) show an unkeyed record arises from EITHER (a) the coverage row's
`bloomberg_ticker` cell status not `MEASURED`, or (b) a MEASURED value that does not split into
`<ROOT> <CC>` (e.g. bare `SLB`, no exchange code -- the module's own docstring example) -- **the 56 are
coverage-list identity gaps UPSTREAM of `crosswalk.py`**, which does no resolution of its own beyond
exchange-code parsing.

**First criterion:** re-run `build_universe.py:832-835`'s own denominator line
(`"POSITIONING CHAIN: holdings_input=%d resolved=%d unresolved=%d"`) FRESH and print it -- never cite 158/161
or 47 from this document; both may have moved since this order was cut.

**Core act:** cross-reference the 56 unkeyed coverage records against ALREADY-RESOLVED holding identities by
company name/root (an already-held-data check, per the build ladder's own step 2, BEFORE anything is classed
as needing a new vendor lookup -- there is no known code join key between the coverage `universe.json` and
the holdings plane today; write the cross-reference, name-matched, and say so). Every record that STILL needs
a genuine Bloomberg lookup after that cross-reference is classed CARD-BOUND residue, named individually (not
a bulk "residual N"), never silently dropped and never converted to a false negative.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.3.3 @`9419550eb1`, rows
`AMGT_RESAPP-Z-S117`/`S120`. PRD v0.10, ADMITTED, s.3.3 reads FWD-1's ACCEPT literally, no PRD change.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~28/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-21.identity-resolve-56-unkeyed.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `crosswalk/v1/`, `universe/v1/`,
  the holdings plane freely); this block governs WRITES, and your write surface is the whole of
  `lib/research/identity/` (add a new module or extend `crosswalk.py` -- your choice, stated in your report).
  The pool write (a corrected/extended `crosswalk/v1/<date>.json`, or a new residue-classification artifact
  under `identity/v1/` or similar -- your choice, named in your report) is not a repo path and needs no
  `<paths>` entry. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~28 <0.9.0_WK_AMGT_RESAPP~28@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification
or freshness checker.** Secrets through `comp-secrets` only. **NO NEW VENDOR CALL of any kind from this
order** -- a residue needing a genuine Bloomberg lookup is CLASSED and CARDED, never resolved by calling out
from this order. No non-ASCII in anything you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the
push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- 89/33/56 and 158/161 are
BOTH re-measured fresh by you, never cited from this document.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W28-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-21"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.identity.build_universe --print-denominators 2>&1 | grep -i "POSITIONING CHAIN"</invocation><expect>a fresh POSITIONING CHAIN line prints holdings_input, resolved and unresolved counts, all nonzero and internally consistent (resolved + unresolved == holdings_input) -- if `build_universe.py` has no such CLI flag, the worker imports and calls the module's own denominator-printing function directly, names the actual invocation used, and re-runs this exact substitute</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-21"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='crosswalk/v1/')
latest = sorted(o['Key'] for o in resp.get('Contents', []))[-1]
doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=latest)['Body'].read())
records = doc.get('records', doc if isinstance(doc, list) else [])
total = len(records)
keyed = [r for r in records if r.get('security_key')]
unkeyed = [r for r in records if not r.get('security_key')]
print('total', total, 'keyed', len(keyed), 'unkeyed', len(unkeyed))
"</invocation><expect>total, keyed and unkeyed sum correctly and match this order's stated 89/33/56 ONLY if that is still current -- any drift from those numbers is printed and reported, not silently reconciled to match this document</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-21"><invocation>cd "$(git rev-parse --show-toplevel)" && cat "$(find org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~28 -iname '*residue*' -o -iname '*resolution*' 2>/dev/null | head -1)" 2>&1 | python -c "import sys,json; d=json.load(sys.stdin); print('newly_resolved', d.get('newly_resolved_count')); print('card_bound_residue', d.get('card_bound_residue_count')); print('residue_named', len(d.get('card_bound_residue_names', [])) == d.get('card_bound_residue_count'))"</invocation><expect>the worker's own delivered artifact (named per its report, path substituted for the find-derived placeholder above if different) shows newly_resolved_count + card_bound_residue_count == 56 (the unkeyed denominator from AC2), and every card-bound residue name is individually listed, never a bare count -- "never by silent omission" applies to this cell's own output, not just the round's fan-out</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~28/AMGT_RESAPP.TO-AMGT-rk-21.identity-resolve-56-unkeyed.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
