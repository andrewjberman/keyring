# AMGT_CORPUS -- L5 decomposition v12.0 -- ROUND 12 (one cell, ruled ahead of the round-11 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~10:0xZ. **Source:** `1.0.0_SA_CTO~Z`'s ruling msg 26555 (READ-acked), verdict
@`e1e4ae43d4` (AMGT_RESAPP vv-4 `Z-S298`): *"AMGT_CORPUS round 12 cuts one cell. The dossier store writes to the builder's
canonical prefix, lib/opal_naming.py address() output (amgt/harvest/gold/research_dossier/). read_dossier reads it there, the old
research-dossier objects stay undeleted, and the served move goes under a pair."* Round 11's decomposition is kept as
`AMGT_CORPUS_DECOMP.round11.md`. Round 11's packet is at L8 with `3.0.0_SA_CVO~Z`; this round's write surface (the dossier table)
is the one round 11 just rewrote, so its served move follows round 11's L9 read of `m-2` AC5 only in time, not in dependency --
the move carries the same content to the new prefix.

## 0. What this round IS

| item | disposition |
|---|---|
| the dossier store to the builder's canonical prefix (R19 migration of one store) | cell `CRPS-n-1` (`~1`) |

**NOT cells** (the ruling): the other five `research-*` stores (their own R19 migrations, later); deleting the legacy objects.

## 1. The rectangle

| cell | slot | serves | `<risk>` | class | write set | the build |
|---|---|---|---|---|---|---|
| `CRPS-n-1` | `~1` | FWD-12 (the served cases reach AMGT_RESAPP's reader) | SERVED (the drain's rewrite to the new prefix) | worker-light | `lib/research/corpus/dossier.py`, `lib/research/corpus/tests/test_dossier_canonical_address.py` (new), `lib/research/corpus/tests/test_backlog.py` | `TABLE` becomes the builder's `research_dossier`; no hyphen literal left in `dossier.py`; reads and writes at the builder's prefix |

## 1a. Re-groundings at L5

- `gold.table_prefix(table)` derives the key prefix from `naming.key(SOURCE, SCOPE, TIER, table, ...)`; only the table NAME is a
  literal. Measured: `opal_naming.address("amgt", <harvest scope>, "gold", "research_dossier", "security_key=X")` ->
  `s3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=X` (the builder accepts the name). Today
  `dossier.TABLE = "research-dossier"`: prefix `amgt/harvest/gold/research-dossier/`, 846 objects (round 11).
- The hyphen literal is carried by `dossier.py` (5) and `tests/test_backlog.py` (5) under `lib/`; the issuer's round-6 check names
  it in a docstring only.
- **Sequencing hazard:** once `TABLE` changes, `read_dossier` finds no object at the new prefix until the rewrite writes one;
  every reader of the merged code sees `LookupError` in between. A fallback to the legacy prefix would re-introduce the literal
  the naming gate refused. **Ruled:** no fallback; the merge and the rewrite run in one issuer-controlled window (drain act,
  s.5), and the pair names the window.
- `write_one` at the new prefix: `read_dossier` raises `LookupError` -> stored inputs `None` -> every name writes (95 puts), no
  method bump needed (nothing is stored at the new prefix).

## 5. The round -- one issuance, fan-out as data

- `fanout: 1 of 1 chains, cap 8, reason: one cell on the dossier write surface.`
- **Drain, in ONE window:** re-grade the worker's tip -> pair signed (COO + CTO) -> change entry opened -> merge -> IMMEDIATELY
  `dossier --write --workers 10` (95 puts at the new prefix) -> verify (census at the new prefix: objects 95, serves the last write
  95 of 95; case census equal to round 11's; legacy prefix still 846) -> close. The one real run: `read_dossier` on three names
  from the new prefix.
- Surprise rows from `Z-S58`; workers `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 6. `<preflight>`

```
checks as files, dry-run at the base (checks/round12/):
  n1_AC1 FAIL (no tests ran)
  n1_AC2 FAIL ('n1 table research-dossier prefix amgt/harvest/gold/research-dossier/ equals_builder False hyphen_literal 5')
  n1_AC3 PASS (dossier import loads no PDF library)
```

## 8. Rulings this decomposition makes

- No legacy fallback in the reader; the window does the job (s.1a).
- The legacy objects are never deleted by this round (the CTO's ruling); the old prefix simply stops being written or read.
- REFUSED to assume: that no other module reads the dossier by the literal prefix (the worker greps `lib/` and names any carrier).

## 9. Holds

| hold | on | owner | what lifts it |
|---|---|---|---|
| merging `CRPS-n-1` | this seat | `2.0.0_SA_COO~X` | the pair signed; merged only in the rewrite's window |

-- `2.0.0_SA_COO~X`
