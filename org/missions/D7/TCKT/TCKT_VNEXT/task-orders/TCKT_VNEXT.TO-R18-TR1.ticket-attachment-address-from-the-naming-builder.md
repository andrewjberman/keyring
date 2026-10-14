# TO TCKT_VNEXT.TO-R18-TR1 -- PRINT the ticket-attachment address from the naming builder for the three served firms, and add a registry row only if the builder refuses (record and checker; no infrastructure)

<to_id>TCKT_VNEXT.TO-R18-TR1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~43</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a registry under `infra/`; the worker writes SOURCE only and creates nothing)
**Decomp cell:** `R18-tf-1` (`decompositions/TCKT_VNEXT_DECOMP_R18.md`) | **outcome_ref:** FWD-10 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~43`.
- **Worktree:** `C:/dev/wk-tckt-vnext-43` (branch `wk-TCKT_VNEXT-43`), provisioned by the issuer. Work and commit only there, with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~43 <0.9.0_WK_TCKT_VNEXT~43@opal.agent>" -F <msgfile> -- <paths>`. If a `portal`
  folder exists in the worktree it is a separate repository: never touch or stage it.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `TCKT_VNEXT-D2-W43-S<k>`
  (next free `<k>`). Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every
  non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call: no AWS, no network, no apply.

### THE CELL (`R18-tf-1`, inlined)

*PRD v0.6 C-ATTACH and CLAUDE.md rule 30: a ticket attachment that is not an Analysis holdings file lives at a `lib/opal_naming.address()`
address under the ticket's FIRM; every S3 address is builder output and a builder REFUSAL is a registry row to add, never a hand-typed
workaround. The ticket Lambda (`TO-R18-L2`) reads a bucket and a KEY TEMPLATE from its environment; `TO-R18-TR3` writes them into Terraform
from the file you produce. The attachments are client-confidential trade forms (PDF, XLSX, CSV), uploaded by Opal staff for a chosen firm.*

1. **Probe the builder** (read `lib/opal_naming.py` `address()` about line 2499 and `infra/logic/02_DOCTRINE.md` R1-R21, especially the tenancy
   rule R6). The issuer's probe, to be re-run by you and not trusted: `address("portal", "49financial", "bronze", "ticket-attachments",
   "trade-form")` returned `s3://opal-data-assets/portal/49financial/bronze/ticket-attachments/trade-form` and the same call at tier `state`
   returned a per-firm bucket (`opal-data-49financial`). Decide the tier by the doctrine, not by convenience, and WRITE THE DECISION WITH ITS
   RULE NUMBER. AMENDMENT 1: your first run chose `state`, rule R21, and found it homes a bucket PER FIRM; that is right and the cell is re-cut for it
   (the Lambda now reads a BUCKET TEMPLATE and a KEY TEMPLATE, each with `{firm}` once). The tier you choose may therefore resolve to a bucket per firm,
   but each firm's bucket must come from ONE template over the firm id (for example `opal-data-{firm}`); if the three served firms (`49financial`,
   `inflection`, `cottonwood`) do not fit one template, STOP: file a BLOCKING row naming the three buckets and the rule, and do nothing else.
2. **The templates.** From the three printed addresses derive `bucket_template` (the bucket with the firm segment replaced by the literal `{firm}`
   exactly once, for example `opal-data-{firm}`) and `key_template` (the key part with the firm segment replaced by `{firm}` exactly once, ending in
   `/`, for example `portal/{firm}/state/ticket-attachments/trade-form/`); verify the two templates, with each of the three firm ids, reproduce that
   firm's printed bucket and key exactly (a round trip).
3. **Registry.** If the builder printed all three without refusal, add NO registry row (say so). If it refused or the validator needs a
   row (a source, a table name, a partition), add the MINIMUM rows under `infra/logic/registry/` in the file the doctrine names for that kind,
   copying the shape of an existing sibling row (read `systems.json`, `scopes.json`, `tiers.json` headers `_about`); then
   `python lib/opal_naming.py validate` must exit 0. Never edit `lib/opal_naming.py`.
4. **Write `deliverables/0.9.0_WK_TCKT_VNEXT~43/ATTACH_ADDRESS.json`** with exactly: `bucket_template`, `buckets` (the three buckets keyed by firm), `key_template`, `tier`, `tier_rule` (the rule
   number and one sentence), `source`, `table`, `partition`, `addresses` (the three printed `address()` outputs keyed by firm), `builder_calls`
   (the exact call strings), `registry_rows_added` (a list, empty if none), `validate_rc`, `claim` (what this proves and what it does not:
   the bucket and its policy and CORS are NOT created or checked here), `not_read`.
5. **Write `deliverables/0.9.0_WK_TCKT_VNEXT~43/address_check.py`** (AC1) and `mutant_check.py` (AC2).

### ACCEPTANCE

<criterion id="R18TR1-AC1" cell_refs="R18-tf-1"><invocation>python C:/dev/wk-tckt-vnext-43/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/address_check.py</invocation><expect>^ADDRESS-OK </expect></criterion>
`R18TR1-AC1`: you write `address_check.py`: it re-computes `address(source, firm, tier, table, partition)` for the three firms by importing `lib/opal_naming.py` from
the worktree, requires `bucket_template` and `key_template` to round-trip each firm's bucket and key with `{firm}` exactly once in each (and a trailing `/` on the key
template), requires `ATTACH_ADDRESS.json`'s `addresses`, `buckets`, `bucket_template` and `key_template` to equal the computation, and runs
`python lib/opal_naming.py validate` (rc 0). It prints `ADDRESS-OK <bucket_template> <key_template>` or `ADDRESS-BAD <why>` (exit 1).

<criterion id="R18TR1-AC2" cell_refs="R18-tf-1"><invocation>python C:/dev/wk-tckt-vnext-43/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R18TR1-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `ATTACH_ADDRESS.json` to a scratch folder OUTSIDE the product tree with the
`key_template` changed to have `{firm}` twice (or the firm segment dropped), points `address_check.py` at the copy (an argument or an environment
variable you add to the checker), and prints `MUTANT-FIRES` only when the checker then prints `ADDRESS-BAD` (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R18TR1-AC3J" cell_refs="R18-tf-1" judgment="true"/>
`R18TR1-AC3J` (judgment, graded at L9, never by you): the tier follows the cited doctrine rule, the address is builder output and not typed, a
registry row exists only if the builder demanded one, and nothing was created in AWS.

<expected_criteria>R18TR1-AC1 R18TR1-AC2 R18TR1-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/` and this order's file
  (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- **AMENDMENT 1 (issuer `2.0.0_SA_COO~V2`, 2026-10-14; gate limb: none stated, the issuer amends its own pending order; your row `TCKT_VNEXT-D2-W43-S1` answered).** You were right: the
  `state` tier (R21) homes a bucket PER FIRM, and the tier follows the doctrine, not the Lambda. The cell is re-cut: the Lambda reads a BUCKET TEMPLATE (`{firm}` once) and a KEY TEMPLATE
  (`{firm}` once, trailing `/`), both of which you derive and round-trip for the three firms. Step 1, step 2, the record's keys and AC1's text above are amended; AC2 and AC3J are unchanged.
  INHERITED STATE: your three commits (`c5c3e453d2`, `7dfcf9bc5c`, `d9832cf72a`) stay; keep row S1 and the printed addresses; add to the row's record that it is ANSWERED by this amendment
  (a new row or a status line in your record, never an edit of the committed row). Write `ATTACH_ADDRESS.json` and both checkers, run all three criteria, regenerate the proof instance (the
  mutant is the one AC2 describes and must FIRE), and flip `<status>` to `complete` only when `proof-of-spec-check.py` prints VALID. Keep the channel file's line endings byte-for-byte
  (your own earlier slip, already corrected, shows why).
- **AMENDMENT 2 (issuer, 2026-10-14; gate limb: none stated, the issuer amends its own order; answers worker 43's row `TCKT_VNEXT-D2-W43-S2`).** `TO-R18-TR3`'s source was REFUSED by the commit-time naming
  gate (ENFORCE): `NAMING_SCHEMA.json key.table_case` is snake_case, so the table segment `ticket-attachments` is out of pattern although `address()` printed it without refusing. The table is now
  `ticket_attachments` (snake_case); the partition `trade-form` and every other choice stand (the gate graded the key `portal/{firm}/state/ticket_attachments/trade-form/` CONFORMANT in the issuer's
  probe). The order is REOPENED (`<status>` complete -> pending by the issuer) for ONE act: re-run steps 1, 2 and 4 with `table = "ticket_attachments"`, rewrite `ATTACH_ADDRESS.json` (`table`,
  `addresses`, `key_template`; the bucket template and buckets do not change), re-run `address_check.py` and `mutant_check.py` unchanged, regenerate the proof instance, and flip to `complete`
  only when `proof-of-spec-check.py` prints VALID. The three printed addresses must read `.../state/ticket_attachments/trade-form`.
- READ only: everything else, including `lib/opal_naming.py` and every Terraform file. Your next orders (`TO-R18-TR2`, `TO-R18-TR3`) edit
  `infra/aws/terraform/ticket-center/main.tf`; you do not.

<paths>
infra/logic/registry/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md</decomp_doc>
<owned_cells>R18-tf-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~43/TCKT_VNEXT.TO-R18-TR1.ticket-attachment-address-from-the-naming-builder.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R18-TR1`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R18TR1-AC1,R18TR1-AC2,R18TR1-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a record, a checker and at most registry rows in a worker worktree; nothing is deployed, applied or created.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the Lambda's permission is Terraform SOURCE in `TO-R18-TR3`.
comp-adversary: RUN -- by reading rule 30 and C-ATTACH against this cell; the lens: a hand-typed address, a tier chosen for convenience, a per-firm bucket that does not fit one template, a registry row added when the builder did not ask. NOT seen: the live bucket's existence, policy and CORS.
</preflight>

---

## RECORD FACE

- Cut on PRD v0.6 @c578883de8 (C-ATTACH) and CTO msg 7818. First order of slot 43's queue (`TO-R18-TR1`, `TR2`, `TR3`); round 18 chain B. Base: `R18TR1-AC1` and `R18TR1-AC2` FAIL as expected (no record, no checker).
- The bucket's policy and CORS for a browser PUT are a LAPTOP role request (C-DEPLOY, NFRA_CTLPLN), sent by the issuer from this cell's printed bucket.
