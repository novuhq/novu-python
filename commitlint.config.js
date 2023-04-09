const types = [
  "build",
  "ci",
  "chore",
  "docs",
  "feat",
  "fix",
  "perf",
  "refactor",
  "revert",
  "style",
  "test",
];

module.exports = {
  extends: ["@commitlint/config-angular"],
  rules: {
    "type-enum": [2, "always", types],
  },
};
