"use client";

import { authClient } from "@/lib/auth-client";

export function SignIn() {
  return (
    <form
      onSubmit={async (e) => {
        e.preventDefault();
        await authClient.signIn.social({
          provider: "discord",
          callbackURL: `/dashboard`,
          errorCallbackURL: `/?auth_error=discord`,
        });
      }}
    >
      <button
        type="submit"
        className="m-5 text-[var(--text-menu)] no-underline"
      >
        ダッシュボード
      </button>
    </form>
  );
}