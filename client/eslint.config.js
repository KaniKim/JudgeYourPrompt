import globals from "globals";
import eslint from "@eslint/js";
import tseslint from "typescript-eslint";
import prettierPluginRecommended from "eslint-plugin-prettier/recommended";
import reactPlugin from "eslint-plugin-react";
import tailwindPlugin from "eslint-plugin-tailwindcss";
import { FlatCompat } from "@eslint/eslintrc";
import reactRefresh from "eslint-plugin-react-refresh";

const compat = new FlatCompat();

export default tseslint.config(
  eslint.configs.recommended,
  ...compat.extends("eslint-config-standard"),
  ...tseslint.configs.recommendedTypeChecked,
  ...tseslint.configs.stylisticTypeChecked,
  ...tailwindPlugin.configs["flat/recommended"],
  prettierPluginRecommended,
  {
    languageOptions: {
      parserOptions: {
        ecmaFeatures: { jsx: true },
        tsconfigRootDir: import.meta.dirname,
        project: ["tsconfig.node.json", "tsconfig.app.json"],
      },
      globals: { ...globals.browser },
    },
  },
  {
    files: ["**/*.{js,mjs,cjs,jsx}"],
    extends: [tseslint.configs.disableTypeChecked],
  },
  {
    plugins: {
      react: reactPlugin,
      "react-refresh": reactRefresh,
    },
    settings: { react: { version: "detect" } },
    rules: {
      ...reactPlugin.configs["recommended"].rules,
      ...reactPlugin.configs["jsx-runtime"].rules,
      "prettier/prettier": "warn",
      "react-refresh/only-export-components": "warn",
      "@typescript-eslint/no-unused-vars": "warn",
      camelcase: "off",
      "@typescript-eslint/consistent-type-definitions": "off",
      "@typescript-eslint/no-unsafe-return": "off",
      "@typescript-eslint/no-misused-promises": "off",
    },
  },
);
