import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";
import pluginReact from "eslint-plugin-react";
import { FlatCompat } from "@eslint/eslintrc";
import path from "path";
import url from "url";

export default [
  pluginJs.configs.recommended,
  {
    parserOptions: {
      ecmaVersion: "latest",
      ecmaFeatures: {
        jsx: true,
      },
      sourceType: "module",
      project: "./tsconfig.eslint.json",
    },
    rules: {
      "no-console": "warn",
      "linebreak-style": 0,
      "import/no-dynamic-require": 0,
      "import/no-unresolved": 0,
      "import/prefer-default-export": 0,
      "global-require": 0,
      "import/no-extraneous-dependencies": 0,
      "jsx-quotes": ["error", "prefer-single"],
      "react/jsx-props-no-spreading": 0,
      "react/forbid-prop-types": 0,
      "react/jsx-filename-extension": [
        2,
        { extensions: [".js", ".jsx", ".ts", ".tsx"] },
      ],
      "import/extensions": 0,
      "no-use-before-define": 0,
      "@typescript-eslint/no-empty-interface": 0,
      "@typescript-eslint/no-explicit-any": 0,
      "@typescript-eslint/no-var-requires": 0,
      "no-shadow": "off",
      "react/prop-types": 0,
      "no-empty-pattern": 0,
      "no-alert": 0,
      "react-hooks/exhaustive-deps": 0,
      "react/jsx-uses-react": "off",
      "react/react-in-jsx-scope": "off",
      "prettier/prettier": [
        "error",
        {
          printWidth: 80,
          trailingComma: "all",
          singleQuote: false,
          tabWidth: 2,
          semi: true,
          jsxSingleQuote: false,
          quoteProps: "as-needed",
          bracketSpacing: true,
          jsxBracketSameLine: false,
        },
      ],
    },
  },
  ...new FlatCompat({
    baseDirectory: path.dirname(url.fileURLToPath(import.meta.url)),
  }).extends("prettier", "plugin:prettier/recommended"),
  { files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"] },
  { languageOptions: { globals: globals.browser } },
  ...tseslint.configs.recommended,
  pluginReact.configs.flat.recommended,
];
