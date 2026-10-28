import { auth } from "@/lib/auth";
import { headers } from "next/headers";

export async function getLoginUser(_sessionId?: string) {
    const requestHeaders = await headers();
    const session = await auth.api.getSession({ headers: requestHeaders });
    if (!session) return null;

    const account = await auth.api.accountInfo({
      headers: requestHeaders,
      query: {
        useAccountCookie: true,
      },
    });

    return account;
}