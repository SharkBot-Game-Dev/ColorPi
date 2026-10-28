import { betterAuth } from "better-auth";
import { nextCookies } from "better-auth/next-js";

const isProduction = process.env.NODE_ENV === "production";

const advanced = {
  useSecureCookies: false,
  defaultCookieAttributes: {
    secure: isProduction,
  },
  cookies: {
    session_token: {
      name: "session_id",
    },
  },
};

export const auth = betterAuth({
  baseURL: process.env.BETTER_AUTH_URL,
  socialProviders: {
    discord: {
      clientId: process.env.DISCORD_CLIENT_ID!,
      clientSecret: process.env.DISCORD_CLIENT_SECRET!,
      scope: ["identify", "email", "guilds", "openid"],
    },
  },
  trustedOrigins: ["https://color.sharkbot.jp", "http://localhost:3000"],
  advanced: advanced,
  plugins: [nextCookies()],
  // 以下は本番では書く
  // baseURL: "https://dashboard.sharkbot.xyz"
});