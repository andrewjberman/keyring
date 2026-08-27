# 4.0.0_SA_CRO — scratchpad `/tooling` folder contract, 2026-08-25 18:49–18:58Z

**archetype:** ARCHITECT  
**secondary_archetypes:** BUILD, VALIDATE

Andrew directed an alphabetical folder-by-folder repository review beginning with `/tooling`.
He clarified the controlling product distinction: internal tools are what Andrew and agents use to
build the product; external tools are customer-facing product. Lenses are an external product-tool
family, not development tooling or third-party dependencies.

## Result

The `scratchpad_tmp` tooling tree was refactored and committed:

- commit: `c7563835217b2cd65f894e5759861c0bec678558`
- subject: `refactor(tooling): separate internal build tools from external product tools`
- compiled denominator: 30 files
- input digest: `a729439f67dba132608e84e3c00e33570f71e21bc0cdceb4752603755b1d5b29`

Final structure:

```text
tooling/
  manifest.v1.json
  internal/
    registry.v1.json
    dependencies.v1.json
    compiler/
      compile_repository.py
      tests/test_compile_repository.py
  external/
    registry.v1.json
    lenses/
      registry.v1.json
```

The repository itself contains no Markdown; this CRO session log remains in the legacy workspace
governance location only.

## Folder contract

- `/tooling/internal`: tools Andrew and agents use to build, inspect, migrate, validate, release,
  and operate product development.
- `/tooling/internal/compiler`: bootstrap compiler and compiler-owned tests only.
- `/tooling/external`: customer-facing tools delivered as part of the Anatomy product.
- `/tooling/external/lenses`: productized customer lenses with input/result, authority,
  sovereignty, entitlement, release, and acceptance contracts.
- Python and Git are internal development dependencies, not external tools.
- Generated outputs live under `/build`; runtime receipts and customer results do not live in
  source `/tooling`.
- Tool source is editable/versioned; registries are editable/current-state; external releases are
  immutable snapshots; runtime events are external append-only state.
- Tests are colocated with the owning tool.
- Bytecode, Markdown, general utilities, one-off outputs, data, logs, and scratch content are
  forbidden.

## Validation

- Local compile and generated-output check: PASS.
- Unit tests: 9/9 PASS.
- New negative control proves a `.pyc` anywhere in the source tree fails compilation.
- `/tooling` Markdown count: 0.
- `/tooling` bytecode count: 0.
- Clean detached worktree: identical input digest, compile/check PASS, tests 9/9, bytecode 0;
  worktree removed.
- Git state after commit: clean `main`.
