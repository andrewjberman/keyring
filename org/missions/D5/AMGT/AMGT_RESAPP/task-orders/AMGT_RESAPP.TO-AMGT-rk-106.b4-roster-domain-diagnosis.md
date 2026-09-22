# AMGT_RESAPP task order -- `AMGT-rk-106` -- B4 DIAGNOSIS, READ-ONLY: which source serves 6861_JP_Equity's officers on Exec Management today and why the B4 roster build returns 0 officers for it, and where a company domain should come from for a name with no domains.json entry; findings only, no code change, 0 writes proven

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-106</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~106</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only diagnosis; it arms no cron, alarm, monitor or cadence and
  writes no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; the live AWS acts are S3
  list/GET under the seat's existing read credentials. NO put, copy or delete. No Lambda invoke.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own findings at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~106`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
`.tools/`, `lib/research/management/roster.py`, `lib/research/management/enrich.py` and
`lib/research/api/scoped_amgt.py` exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~106;`. **NEVER RUN AN INSTALL.** **NEVER read the Lusha key, never
call Lusha, never call any vendor.** Never read, show, diff or check out branch `wk-amgt-14-50` or
`C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-106` (round 27, ahead of the B4 run)

**The ruling of record, verbatim** (1.0.0_SA_CTO~Z msg 24216, 2026-09-22T12:21:28Z, file
`org/mcp/inbox/2.0.0_SA_COO/~Z/read/20260922T122128Z_1.0.0_SA_CTO_Z_Re_24215__all_5_calls_RULED_--_round_27_.md`,
lines 19-22):

> CALL 3: YES, a read-only diagnosis cell, as recommended. It answers two questions:
> - (a) Which source serves 6861's officers on Exec Management today, and why the B4 roster build returns 0.
> - (b) Where a company domain should come from for a name with no domains.json entry.
> A code fix is cut only on what the diagnosis finds, in the next round.

**Starting points measured at SITEZ `d3ba12c64b`. They are pointers, not answers; RE-READ each at your HEAD and follow
the code wherever it goes:**
- The served Exec Management route reads `read_management` at `lib/research/api/scoped_amgt.py:2507`, which calls
  `read_pool_object(MANAGEMENT_PREFIX, key)` at `:2536` with `MANAGEMENT_PREFIX = "management/v1/"` (`:171`). The pool
  bucket is `opal-data-harvest` (`lib/research/coverage/pool_reader.py:72`). Exactly ONE served object exists:
  `management/v1/6861_JP_Equity/2026-09-19.json`.
- The B4 path (`lib/research/harvest/lusha.py` `_cli`) builds officers with `roster.load_source_object` followed by
  `roster.build_roster`:
  - `lib/research/management/roster.py:1116-1164` reads filing_source SILVER first, then the filing_attempt STATE
    marker.
  - `derive_roster` at `:1183-1217` returns 0 officers for a missing or non-RESOLVED source object, and for an empty
    officer section.
- The live state marker for 6861 (`amgt/harvest/state/filing_attempt/security_key=6861_JP_Equity/UNRESOLVED-SOURCE.json`,
  retrieved_at 2026-09-19T06:20:51Z) is UNRESOLVED-SOURCE. Its step-4 attempt names the seed `https://www.keyence.co.jp/`.
- Domains:
  - `enrich.domain_for` (`lib/research/management/enrich.py:140-148`) reads ONLY `domains.json`.
  - `enrich.verified_domain_for` (`:163-172`) reads ONLY the source object's `verified_site.host`.

**RULED, what you deliver (NO code change):** a findings file,
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~106/B4_ROSTER_DOMAIN_DIAGNOSIS.md`, carrying:
1. **Q-a1: which source serves 6861's officers today.**
   - Trace the route from `read_management` to the served object, and name the object's own roster-source field(s).
     Is it the filing roster, a Bloomberg fallback, or something else?
   - Print the served officer COUNT and the source field value. Print officer names only as a count, never contact
     data.
   - Cite every step `file:line @<your HEAD short hash>`.
2. **Q-a2: why `load_source_object` + `build_roster` return 0 for 6861.**
   - Run them read-only, exactly as `lusha._cli` does, with no Lusha call and no write.
   - Print the returned source label, `roster_status`, `roster_reason` and the officer count.
   - Name the exact branch of `derive_roster` taken, with its line.
   - State whether the previous claim, "its filing source resolved to an issuer-site document", holds. List every
     filing_source silver row for 6861 under BOTH vendors (`sec`, `issuer-site`), with the denominator of rows read.
3. **Q-b: where a company domain should come from.**
   - Enumerate BY SUBTRACTION. First print the denominator: EVERY field, in every object you can read for 6861, that
     carries a URL or a host. Cover at least the crosswalk record, the filing_attempt state marker, any filing_source
     silver row, the served management object, `domains.json` and the model block. Then list each candidate with:
     - its value;
     - who wrote it;
     - whether it is VERIFIED (a battery `verified_site`) or merely a SEED or display value;
     - which existing function already reads it.
   - End with ONE recommended source and the rule a later code cell would implement. Never a guessed domain: the
     `domain_for` docstring's hazard is "a guessed domain enriches the wrong company".
4. **A "What the next round would cut" section:** at most 3 code cells, each with its files.

## 2. WHERE THIS CAME FROM

**ROUND 27**, decomposition s.35 (cut by `2.0.0_SA_COO~Z`), on the CTO's ruling msg 24216 (on msg 24215).
- The held B4 draft (rk-103) found that the Lusha run would REFUSE before any call: 6861 has no `domains.json` entry,
  and the roster build returns 0 officers.
- Andrew-direct ~15:12Z governs one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~106/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-106.b4-roster-domain-diagnosis.md
</paths>

- **EVERY code file is a WALL.** Reads need no grant.
- Scratch is `<your worktree>/.scratch/r106/` only, and is never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~106 <0.9.0_WK_AMGT_RESAPP~106@opal.agent>" -F <msgfile> -- <paths>`,
  with the message file written by the Write tool. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

- **READ-ONLY.** S3 `list_objects_v2`, `get_object` and `head_object` only. No put, copy or delete. No Lambda invoke.
  No vendor call. The Lusha key is never read. A function that could write (`enrich.build_document` with a write flag,
  or any `--write` CLI) is NEVER called with that flag.
- **Contact data:** never print an email, phone or personal URL. Officer rosters are reported as counts and roles.
- **Every claim in the findings file carries `file:line @<HEAD>` or the S3 key it was read from.**
- **Scripts that carry a backslash are FILES** (W84-S1).
- **THE REFUSAL CLAUSE:**
  - A question the evidence cannot answer is answered "UNDETERMINED", with what was read and what would decide it.
    It is never guessed.
  - A criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row.
- **SURPRISE ROWS:**
  - Ids are `AMGT_RESAPP-Z-W106-S<k>`, and each row carries `"project": "AMGT_RESAPP"` and `"fabric": "site-z"`.
  - Append by textual splice inside the one fenced JSON array.
  - `disarm_owner` is `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; each runs under timeout 600)

`.scratch/r106/census.py <label>` (the 0-write control; run BEFORE any other act as `before`, and LAST as `after`):
```
import boto3, json, os, sys
s3 = boto3.client("s3", region_name="us-east-1")
B = "opal-data-harvest"
tops = [p["Prefix"] for p in s3.list_objects_v2(Bucket=B, Delimiter="/").get("CommonPrefixes", [])]
counts = {}
for t in tops:
    n = 0
    newest = ""
    for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix=t):
        for o in pg.get("Contents", []):
            n += 1
            newest = max(newest, o["LastModified"].strftime("%Y-%m-%dT%H:%M:%SZ"))
    counts[t] = [n, newest]
os.makedirs(".scratch/r106", exist_ok=True)
json.dump(counts, open(".scratch/r106/census_%s.json" % sys.argv[1], "w"), indent=1, sort_keys=True)
print("census", sys.argv[1], "prefixes", len(tops), "objects", sum(v[0] for v in counts.values()))
```

`.scratch/r106/zero_writes.py`:
```
import json
a = json.load(open(".scratch/r106/census_before.json"))
b = json.load(open(".scratch/r106/census_after.json"))
diff = {k: (a.get(k), b.get(k)) for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)}
print("prefixes", len(a), len(b), "changed", len(diff))
for k, v in diff.items():
    print("CHANGED", k, v)
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-106"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r106/census.py before</invocation><expect>BEFORE any other act: "census before prefixes P objects O" (measured at the cut: 21 top-level prefixes). Record P and O</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-106"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "t=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~106/B4_ROSTER_DOMAIN_DIAGNOSIS.md',encoding='utf-8').read(); print('sections', [h for h in ('Q-a1','Q-a2','Q-b','What the next round would cut') if h in t]); print('citations', t.count(' @'))"</invocation><expect>"sections" lists all four headings: Q-a1, Q-a2, Q-b and "What the next round would cut". "citations" is at least 1 per answered claim, and the count is recorded. Each of Q-a1, Q-a2 and Q-b carries an explicit ANSWER line (or UNDETERMINED with what would decide it)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-106"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "t=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~106/B4_ROSTER_DOMAIN_DIAGNOSIS.md',encoding='utf-8').read(); import re; print('emails', len(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]{2,}', t)), 'phone_like', len(re.findall(r'[+][0-9][0-9 ()-]{7,}', t)))"</invocation><expect>"emails 0 phone_like 0" -- the findings carry no contact data</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-106"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r106/census.py after && python .scratch/r106/zero_writes.py && git diff --name-only d3ba12c64b HEAD -- lib integrations infra .tools portal && python -c "import glob; fs=glob.glob('.scratch/r106/*.py'); print('scratch_scripts', len(fs), 'write_calls', sum(open(f,encoding='utf-8').read().count(w) for f in fs for w in ('put_object','copy_object','delete_object','upload_file','upload_fileobj')))"</invocation><expect>
- "census after prefixes P objects O", equal to AC0's P and O, and "changed 0" with no CHANGED line.
- The bucket is SHARED with scheduled producers, so a CHANGED line is not by itself this worker's write. Each one is attributed from its newest object's key and LastModified, and recorded with a row. It is a FAIL only if a changed object falls under a key this worker's scripts address.
- The git diff prints NOTHING: 0 code files changed.
- "write_calls 0" over every scratch script, so no script this worker ran can write to S3.
</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** The findings file is itself graded at
L9 (a JUDGMENT read by the CVO); AC1-AC3 are its structural and safety criteria only.

## 6. WHEN YOU ARE DONE

1. Write your instance to
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~106/AMGT_RESAPP.TO-AMGT-rk-106.b4-roster-domain-diagnosis.proof_of_spec.json`
   per `org/standards/PROOF_OF_SPEC.schema.json`.
2. Grade it with YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3`; rc 0 is the
   verdict.
3. Flip the order's status (on the record face) to `complete` only if every criterion PASSES. Commit with
   `--only -- <paths>`.
4. Report ONCE, with the three ANSWER lines (Q-a1, Q-a2, Q-b) verbatim, the census before and after, and the findings
   path.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. Read-only by construction. The only writes are the worker's own deliverable and channel rows in the repo. AC3
   proves 0 S3 writes across all top-level prefixes of `opal-data-harvest`, and 0 code files changed.
2. The findings carry a JUDGMENT (the recommended domain source), which L9 grades. No code is cut on it until the CTO's
   round-27 analysis (msg 24216: "A code fix is cut only on what the diagnosis finds, in the next round").
3. Pinned at `d3ba12c64b`.

<status>pending</status>
<round>27</round>
<slot>~106</slot>
<fabric>site-z</fabric>
