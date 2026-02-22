---
name: commit
description: Generate conventional commit messages following the Conventional Commits specification. Use when user wants to create a standardized git commit, asks for help with commit message format, or runs /commit command.
user-invocable: true
disable-model-invocation: false
---

Generate conventional commit messages following the Conventional Commits specification:
https://www.conventionalcommits.org/

The format is: `<type>(<scope>): <subject>`

## Commit Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools
- **revert**: Reverts a previous commit

## How to Generate

1. **Analyze changes**: First, run `git status` to see what files are modified, then run `git diff` for unstaged changes and `git diff --staged` for staged changes to understand what was changed.

2. **Determine commit type**: Based on the changes, select the most appropriate type:
   - `feat` - new functionality added
   - `fix` - bug fix
   - `docs` - documentation updates (README, comments, etc.)
   - `style` - code formatting (no functional changes)
   - `refactor` - code restructuring (same behavior)
   - `perf` - performance improvements
   - `test` - test additions/fixes
   - `chore` - dependencies, config, tooling

3. **Determine scope** (optional): If changes are specific to a module or area, include it in parentheses, e.g., `(auth)`, `(ui)`, `(api)`.

4. **Write subject**: A concise summary of changes, in imperative mood, lowercase, no period at end. Keep under 50 characters.

5. **Add body** (optional): For more complex changes, add a detailed description with bullet points explaining what and why.

6. **Add footer** (optional): For breaking changes use "BREAKING CHANGE: " prefix, or use "Closes #xxx" for issue references.

7. **Co-authored-by**: Always append "Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>" at the end of the commit message.

8. **Present the message**: Show the generated commit message to the user for review. Do NOT run git commit automatically - just generate the message for the user to review and execute.

## Format Example

```
<type>(<scope>): <subject>

<body>

<footer>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

## Examples

### Simple feature addition
```
feat(auth): add user login functionality

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

### Bug fix with details
```
fix(api): resolve null pointer exception in user service

- Add null check before accessing user properties
- Update error handling to provide better error messages

Closes #42

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

### Breaking change
```
feat(storage): switch to new storage backend

BREAKING CHANGE: Old storage format is no longer supported.
Migration script provided in /migrations/v2.py

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

### Documentation update
```
docs: update README with installation instructions

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

## Important Notes

- Always use imperative mood ("add" not "added", "fix" not "fixed")
- Keep subject line under 50 characters
- Body should explain WHAT and WHY, not HOW
- The user should review and approve before creating the commit
- Do NOT run git commit automatically - just generate the message
- Always include the Co-Authored-By footer
