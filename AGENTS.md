# Project Guidelines

## Commit Message Rules

These rules apply to all commit message generation in this repository.

### Language

- Commit messages must be written in English only (both subject and body).

### Format

- Subject: `<type>(<scope>): <short summary>`
- Summary uses imperative, present tense (`add`, not `added`/`adds`), lowercase first letter, no trailing period.
- Subject line should be ≤ 72 characters.
- Body (when present) is a bullet list using `- `.
- Example:

```text
feat(storage-system): add round counter APIs for RandomEvent

- add per-event round map in StorageSystem (`randomEventId -> current round`)
- implement `IncrementRound(randomEventId)` to initialize at 1 and increment on each call
- add `CleanupRounds()` to clear all round-tracking records
```

- Body may be omitted for a single trivial change (e.g. a typo fix); subject alone is acceptable.

### Scope Rules

- Scope selection is module-first, directory-second, and must be lowercase kebab-case.
- Changes mainly in one module → use that module (e.g. `storage-system`, `rsu-app`).
- Changes spanning multiple modules serving one pipeline → use a functional scope (e.g. `rating-pipeline`).
- Changes spanning unrelated modules with no dominant theme → use `multi`.
- When no natural scope applies (global/repo-wide change), the scope may be omitted: `<type>: <summary>`.

### Type Rules

- Allowed primary types:
  - `feat`: new user-visible functionality or behavior expansion
  - `fix`: bug fix or regression fix
  - `refactor`: internal restructuring without behavior change
  - `perf`: performance improvement without semantic change
  - `test`: tests added or updated
  - `docs`: documentation-only changes
  - `build`: build system, dependency, or compilation config changes
  - `ci`: CI/CD workflow changes
  - `chore`: maintenance work not covered above, without product behavior change
  - `revert`: revert of a previous commit
- Always prefer the allowed primary types first; if none is a clean fit, default to `chore`.
- A type outside the list is allowed only when explicitly requested by the user, or already an established convention in this repo's history. If used, add one short rationale line in the body.
- Type-conflict tiebreak: if a change contains both behavior change and refactoring, choose by user-visible effect (`feat`/`fix`); use `refactor` only when the change is purely internal.

### Breaking Changes

- Mark breaking changes with `<type>(<scope>)!: <summary>`, and/or add a `BREAKING CHANGE: <description>` line in the body.

### Revert Format

- Use `revert: <subject of the reverted commit>` and reference the reverted commit hash in the body.

### Body Content Rules

- Describe only the change scope requested for that commit; if the user gives no scope, default to current changes (staged and unstaged).
- Each bullet describes a distinct change point; do not repeat the same idea.
- Body describes actual code/content changes only — never process/meta notes about conversation, review feedback, or "changes made because of user comments".

### Commit Granularity

- A single commit should cover one logically cohesive change, consistent with a single scope.

### Footer (optional)

- Link issues with `Refs #<id>` or `Closes #<id>` when applicable.

### Commit Command Quoting

- Preserve commit message literals exactly, including backticks.
- Never pass a message containing backticks via double-quoted `-m "..."` (shell command substitution risk).
- For messages containing backticks, use single-quoted `-m '...'` or `git commit -F`.

## Temporary File Hygiene

- Place any agent-created temporary files under `.agent-tmp/` in the repository root.
- Never stage or commit temporary files; verify none are included before committing.
- Deleting files outside `.agent-tmp/` requires explicit user approval.
- Do not delete files produced by normal program execution, builds, tests, or runtime workflows unless explicitly requested.
