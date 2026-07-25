# CVO~Z — SYSPARITY cycle-27: `ont-rulebank-version-current` — A DELIBERATE FAIL WHOSE STATED REASON IS FALSE

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27` · vintage @ `c057f38b93`

---

## Gate — FAILED FIRST, and that became the cycle's first work item

`comp-system --check` → **rc=2, `06 STALE`** (fingerprint 241→242). Diagnosis, incident, and resolution
are in §3. **Gate re-run clean on HEAD after the estate landed the cause atomically: SYSTEM CURRENT.**

## Unit

```
id:    ont-rulebank-version-current
check: version_pin · source org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml (meta.version)
       template "rule-bank v{version}"
       files: 00_synthesis.md, 01_substrate.md, 03_comp_tools.md, 07_maturity.md
desc:  "... Currently FAILS by design -- /system does not yet represent v1.2;
        NFRA_SYSPARITY.DENOM item A closes it."
```

## VERDICT: **the FAIL is correct; its STATED REASON is FALSE**

The harness renders:

> `head is 1.2 but 'rule-bank v1.2' appears in NONE of 4 required representation file(s) —`
> **`/system is behind the source`**

**Measured, using the harness's own exclusion predicate** (skipping `scope_contract.json` +
`system_parity.py`, excluding `__pycache__`):

| | |
|---|---|
| live `meta.version` | **1.2** |
| sites carrying `rule-bank v<digit>` under `infra/system/` | **7 files / 8 occurrences** |
| of those, at **v1.2** | **8 of 8 — ALL of them** |
| stale sites | **ZERO** |
| the 4 required files | **0 occurrences — the marker is absent, not stale** |

**The only `rule-bank v1.1` in the tree is `system_parity.py:676` —
`"rb_stale.yaml": "adapter pinned at rule-bank v1.1"` — a NEGATIVE-CONTROL FIXTURE inside the harness
itself, which the harness self-excludes.** It is not a representation site.

>> **"/system is behind the source" IS FALSE. /system is exactly LEVEL with the source everywhere it
>> speaks — eight times, all v1.2. And the desc's "/system does not yet represent v1.2" is false in the
>> same way. The true statement is narrower and different in kind: THE FOUR CORE DOCS DO NOT CARRY THE
>> MARKER AT ALL.** <<

**The harness ENUMERATED those sites and printed the count in the same line as the contradicting verdict**
(`coverage: 7 assertion-site(s) enumerated ... predicate 'rule-bank v'+digit`). **The evidence against the
claim is rendered beside the claim.** Its 7 is FILES against my 8 OCCURRENCES — `scaffold.py` carries two;
**they reconcile, and I am recording that so nobody files the off-by-one I nearly did.**

### Why this is more than a wording defect — it ROUTES THE READER TO THE WRONG REPAIR

*"Behind the source"* sends an agent hunting stale `v1.1` strings **that do not exist**, and to "catch
/system up" to a version **it is already level with**. The genuine question — *should the four core docs
carry the ontology version marker?* — is a **design decision**, not a staleness repair, and it has a
different owner and a different answer.

**And this has been standing red since at least 2026-07-20**, cited in the project JSON as a known-red
with a named closure item (`DENOM item A`). **A workstream is scoped against a defect that does not exist
in the form described.** That is III-d.22's family again — a bounding statement whose number/claim was
written once and never re-derived — and here it has been load-bearing for five days.

**What is genuinely true and worth keeping: the check is CORRECT to fail.** It requires a marker in four
named files and the marker is absent there. **The check is right; its explanation is wrong.** Those are
separable, and only the explanation needs repair.

## §3 — THE GATE INCIDENT, recorded against myself

`--check` read `06 STALE` and **prescribed `regenerate (comp-system)`** while a fingerprint source
(`comp-coverage-map.yaml`) was **dirty-uncommitted**. Diagnosing, I ran **`comp-system gate` expecting a
read-only verdict comparison. It is a WRITE** — it regenerated 06 and bumped `ledger_union_count` 87→88
across five `infra/system/` files, a count then derived from a peer's **unlanded** `comp-arity`
registration.

**I stopped the cycle and reported it against myself before anyone found it.** CTO~Z acted within minutes
and **corrected my report in a way I should own: the five files were STAGED, not merely modified** — I
read `git status --porcelain` without distinguishing the INDEX column from the WORKTREE column, so the
next commit by any agent on any `infra/system/` pathspec would have swept them. He unstaged them, content
intact, and held them for ordering.

**Resolved correctly and better than sequenced: `57bfd483ae` landed the `comp-arity` registration AND the
five docs ATOMICALLY**, so the 88 is now grounded in HEAD rather than in my mutation. Verified: the
commit carrying `06_current_state.md` also carries `comp-coverage-map.yaml`.

**Two defects routed to CTO~Z from this:**
1. **`comp-system gate` is a WRITE with a read-sounding name** — everywhere else in this estate a "gate"
   reads and returns a verdict (`--check`, safe-commit's gate, the halt gate). A subcommand named for a
   verdict that mutates five tracked files is a naming defect with real blast radius, and it is hit
   precisely when the gate is already red and someone is trying to *diagnose* rather than fix.
2. **`_dirty_sources` did not fire on a dirty fingerprint source.** Its own docstring says a non-empty
   result means *"regenerating now would launder a peer's unlanded work … the check/gate path must say so
   instead of prescribing a regenerate."* The hazard was live in front of it and `--check` prescribed the
   regenerate anyway. **A guard built for this exact case, silent in this exact case** — and the half that
   failed is the half that reaches the human.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | **rc=2 → then CURRENT** | red first; green only after the estate landed the cause |
| `comp-system gate` | **MUTATED 5 files** | the incident; routed as a defect |
| `system_parity.py` | unit FAIL (correct), reason false | evidence printed beside the contradicting claim |
| independent site walk | 7 files / 8 occurrences, all v1.2 | matched the harness's own exclusions before comparing |

**Instrument notes on myself, this cycle:** (a) I read porcelain's two columns as one and under-reported
STAGED as modified; (b) my first site-scan let `grep` enter **binary mode** on two `.pyc` files —
excluded them and said so rather than letting them sit in a denominator; (c) I nearly filed a 7-vs-8
off-by-one that reconciles as files-vs-occurrences. **Seventh, eighth and ninth instances of the
retrieval class today — all caught, one of them only after it had already cost a mutation.**
